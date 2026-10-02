# C#/.NET handbook outline

[Deutsch](../de/README.md) · [Shared specifications](../../../../spec/README.md)

Status: planned. No C# statistical API is available here yet.

| Chapter | Required content when implemented |
| --- | --- |
| Installation | Supported SDK/runtime/platforms, NuGet/project dependency and Math pin |
| First analysis | A real runnable summary example with interpretation |
| Data contracts | Arrays/spans/matrices, ownership and missingness |
| Results and errors | Typed results, unavailable estimates and exception/status mapping |
| Procedures | Definitions, assumptions, options and C# examples per validated procedure |
| Numerical diagnostics | Precision, rank/conditioning, failure and convergence |
| Integration | Packaging, adapters and application/workflow boundaries |
| Validation | Shared cases, independent references and supported configuration |

Public APIs use /// XML documentation explaining domains and numerical choices.
The first implementation replaces this outline with actual chapter links and
adds tested restore/build/test/run instructions. API names are deliberately undecided.
