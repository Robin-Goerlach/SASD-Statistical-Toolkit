# C#/.NET implementation home

Reserved for the future C# library. No project, solution or NuGet package exists
here yet. Candidate baseline: .NET 10; confirm it against the actual Math dependency.

Before introducing code:

1. Complete the C# Math readiness gate and approve the pilot contracts.
2. Select namespace, public API, result/exception mapping and exact Math dependency.
3. Add real restore/build/test/pack commands, SDK configuration and CI.
4. Run shared conformance cases from tests/dotnet and add samples/dotnet.
5. Maintain the separate [C# handbooks](../../docs/implementations/dotnet/en/README.md).

Öffentliche APIs mit /// XML-Dokumentation erklären; // erläutert lokale
numerische Entscheidungen. Keine GUI-Framework-Abhängigkeit im Rechenkern.
