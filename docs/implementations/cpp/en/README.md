# C++ handbook outline

[Deutsch](../de/README.md) · [Shared specifications](../../../../spec/README.md)

Status: planned. No C++ API is available yet.

| Chapter | Required content when implemented |
| --- | --- |
| Installation | Supported compilers/platforms, CMake/package dependency and Math pin |
| First analysis | A real buildable summary example with interpretation |
| Data contracts | Ranges/spans/matrices, ownership, lifetime and missingness |
| Results and errors | Optional values, status/error mapping and exception policy |
| Procedures | Definitions, assumptions, options and C++ examples per validated procedure |
| Numerical diagnostics | Precision, rank/conditioning, failure and convergence |
| Integration | Linking, ABI, adapters and application/workflow boundaries |
| Validation | Shared cases, independent references and supported configuration |

Public headers use Doxygen comments explaining domains and numerical choices.
The first implementation replaces this outline with actual chapter links and
adds tested build/run instructions. API names are deliberately undecided.
