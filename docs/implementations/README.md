# Separate implementation documentation

| Implementation | English handbook | Deutsches Handbuch |
| --- | --- | --- |
| C++ | [cpp/en](cpp/en/README.md) | [cpp/de](cpp/de/README.md) |
| C#/.NET | [dotnet/en](dotnet/en/README.md) | [dotnet/de](dotnet/de/README.md) |

Current files are editorial outlines, not API manuals. Each implementation keeps
its own installation, API examples, diagnostics mapping, limitations and build
instructions. Shared mathematics is referenced from spec rather than silently
changed in one language manual.

When implementation begins, use language-specific Markdown chapters as editorial
sources. Plan separate LaTeX/PDF editions per language and locale; add typesetting
sources and reproducible render/verification commands once there are real chapters.
Do not publish empty PDFs. Generated editions must match the accepted code and
contracts, identify their versions and pass structural plus visual release checks.
