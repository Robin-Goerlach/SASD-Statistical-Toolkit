#!/usr/bin/env python3
"""Check repository documentation and fixture structure, not numerical results."""

import json
import math
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
ERRORS = []


def require(condition, message):
    if not condition:
        ERRORS.append(message)


def read_json(relative):
    try:
        return json.loads((ROOT / relative).read_text(encoding="utf-8"),
                          parse_constant=lambda token: (_ for _ in ()).throw(
                              ValueError("Non-JSON numeric constant: " + token)))
    except (OSError, ValueError) as error:
        ERRORS.append(f"{relative}: {error}")
        return {}


def check_links():
    # This project uses simple inline links without spaces or nested parentheses.
    pattern = re.compile(r"!?\[[^\]\n]*\]\(([^\s)]+)\)")
    markdown = list(ROOT.rglob("*.md"))
    for path in markdown:
        if ".git" in path.relative_to(ROOT).parts:
            continue
        text = path.read_text(encoding="utf-8")
        require(text.endswith("\n"), f"{path.relative_to(ROOT)}: missing final newline")
        for target in pattern.findall(text):
            if target.startswith("#") or urlsplit(target).scheme:
                continue
            local = (path.parent / unquote(target.split("#", 1)[0])).resolve()
            require(local.is_relative_to(ROOT) and local.exists(),
                    f"{path.relative_to(ROOT)}: missing/escaping link {target}")
    return len(markdown)


def check_pairs():
    english = {p.name: p for p in (ROOT / "docs/en").glob("*.md")}
    german = {p.name: p for p in (ROOT / "docs/de").glob("*.md")}
    require(english.keys() == german.keys(), "English/German planning page names differ")
    ids = re.compile(r"\b(?:ST|AC|ADR)-\d{3}\b|\bMATH-[A-Z]+\b")
    for name in english.keys() & german.keys():
        en_ids = set(ids.findall(english[name].read_text(encoding="utf-8")))
        de_ids = set(ids.findall(german[name].read_text(encoding="utf-8")))
        require(en_ids == de_ids, f"{name}: English/German stable IDs differ")
    for language in ("cpp", "dotnet"):
        for parent in ("src", "tests", "samples"):
            require((ROOT / parent / language / "README.md").is_file(),
                    f"Missing {parent}/{language}/README.md")
        for locale in ("en", "de"):
            require((ROOT / "docs/implementations" / language / locale / "README.md").is_file(),
                    f"Missing {language}/{locale} handbook outline")


def check_catalog(catalog):
    require(catalog.get("schema_version") == 1, "Unknown procedure catalog schema")
    entries = catalog.get("procedures", [])
    require(isinstance(entries, list) and bool(entries), "Procedure catalog must be a nonempty list")
    known = set()
    stages = {"catalogued", "draft", "approved", "implemented", "validated", "released"}
    implementations = {"not_started", "implemented", "validated", "released"}
    math_keys = set(re.findall(r"\bMATH-[A-Z]+\b",
                    (ROOT / "docs/en/MATH-DEPENDENCY.md").read_text(encoding="utf-8")))
    for item in entries:
        if not isinstance(item, dict):
            ERRORS.append("Invalid procedure entry")
            continue
        pid = item.get("id", "")
        require(bool(re.fullmatch(r"STAT-[A-Z]{4}-\d{3}", pid)), f"Invalid procedure ID {pid}")
        require(pid not in known, f"Duplicate procedure ID {pid}")
        known.add(pid)
        require(item.get("specification_status") in stages, f"{pid}: invalid specification status")
        require(item.get("milestone") in {"M1", "M2", "M3", "M4", "M5"}, f"{pid}: invalid milestone")
        require(bool(item.get("name")) and bool(item.get("family")), f"{pid}: missing name/family")
        binding = item.get("implementations", {})
        require(set(binding) == {"cpp", "dotnet"}, f"{pid}: language status keys differ")
        require(all(value in implementations for value in binding.values()), f"{pid}: invalid language status")
        contract = item.get("contract_path")
        require(contract is not None or item.get("specification_status") == "catalogued",
                f"{pid}: non-catalogued entry needs a contract")
        if contract:
            require((ROOT / contract).is_file(), f"{pid}: missing contract {contract}")
            require(bool(item.get("contract_version")), f"{pid}: missing contract version")
            if (ROOT / contract).is_file():
                require(pid in (ROOT / contract).read_text(encoding="utf-8"),
                        f"{pid}: ID absent from contract")
        capabilities = item.get("math_capabilities", [])
        require(isinstance(capabilities, list) and set(capabilities) <= math_keys,
                f"{pid}: unknown Math capability")
    return known, len(entries)


def check_fixtures(fixtures, known):
    require(fixtures.get("schema_version") == 1, "Unknown fixture schema")
    require(fixtures.get("contract_version") == "0.1", "Unexpected descriptive contract version")
    require(bool(fixtures.get("provenance", {}).get("derivation")), "Missing fixture derivation")
    tolerance = fixtures.get("default_tolerance", {})
    require(set(tolerance) == {"atol", "rtol"}, "Fixture tolerance keys must be atol/rtol")
    require(all(isinstance(x, (int, float)) and math.isfinite(x) and x >= 0
                for x in tolerance.values()), "Invalid fixture tolerance")
    cases = fixtures.get("cases", [])
    require(isinstance(cases, list) and bool(cases), "Fixtures must be a nonempty list")
    seen = set()
    statuses = {"success", "partial", "insufficient_data", "invalid_input",
                "undefined_statistic", "numerical_failure"}
    for case in cases:
        cid = case.get("id")
        require(bool(cid) and cid not in seen, f"Missing/duplicate case ID {cid}")
        seen.add(cid)
        require(case.get("procedure_id") in known, f"{cid}: unknown procedure ID")
        data = case.get("input", {})
        require("x" in data, f"{cid}: missing x input")
        for values in data.values():
            require(isinstance(values, list), f"{cid}: input must be a list")
            if isinstance(values, list):
                require(all((type(x) in (int, float) and math.isfinite(x)) or
                            (isinstance(x, str) and x in {"NaN", "+Infinity", "-Infinity"})
                            for x in values), f"{cid}: invalid numeric input token")
        expected = case.get("expected", {})
        require(expected.get("status") in statuses, f"{cid}: invalid expected status")
        require(bool(case.get("options", {}).get("missing_policy")), f"{cid}: missing policy")
        counts = ["input_count", "used_count", "excluded_count"]
        if any(key in expected for key in counts):
            require(all(key in expected and type(expected[key]) is int and expected[key] >= 0
                        for key in counts), f"{cid}: incomplete/invalid counts")
            if all(key in expected for key in counts):
                require(expected["input_count"] == expected["used_count"] + expected["excluded_count"],
                        f"{cid}: counts do not reconcile")
                require(expected["input_count"] == len(data["x"]), f"{cid}: input_count differs from x")
        require(all(value in statuses for value in case.get("expected_metric_status", {}).values()),
                f"{cid}: invalid per-metric status")
    return len(cases)


def main():
    markdown_count = check_links()
    check_pairs()
    catalog = read_json("spec/procedures.json")
    known, procedure_count = check_catalog(catalog)
    case_count = check_fixtures(read_json("conformance/descriptive-cases.json"), known)
    if ERRORS:
        for message in ERRORS:
            print("ERROR:", message, file=sys.stderr)
        return 1
    print(f"Documentation OK: {markdown_count} Markdown files, "
          f"{procedure_count} catalog entries, {case_count} fixture structures.")
    print("No statistical implementation or numerical test was run.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
