---
type: simulink-block
title: 'Fuzzy Logic Controller with Ruleviewer'
family: 'fuzzy'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'fuzzylogiccontrollerwithruleviewer'
documentation_source_path: 'fuzzylogiccontrollerwithruleviewer.html'
language: en
---

# Fuzzy Logic Controller with Ruleviewer

## Ports
```yaml
ports:
- name: Port_1(In1)
  summary: Input signal scalar | vector
  direction: input
- name: Port_1(Out1)
  summary: Defuzzified output signal scalar | vector
  direction: output
```

### Input

### **Port\_1(In1)** — Input signal scalar | vector

For a single-input fuzzy inference system, the input is a scalar.
For a multi-input fuzzy system, combine the inputs into a vector signal
using blocks such as:

- Mux (Simulink)
- Vector Concatenate (Simulink)
- Bus Creator (Simulink)
### Output

### **Port\_1(Out1)** — Defuzzified output signal scalar | vector

For a single-output fuzzy inference system, the output is a
scalar. For a multi-output fuzzy system, the output is a vector. To
split system outputs into scalar signals, use the Demux (Simulink) block.
## Parameters
```yaml
parameters:
- name: FIS structure
  summary: Fuzzy inference system mamfisobject | sugfisobject
  group: ''
  block_parameter: fismatrix
  values: '"fis" (default) | variable name in quotes'
- name: Refresh rate
  summary: Time between rule viewer updates positive scalar
  group: ''
  block_parameter: Ts
  values: '"2" (default) | positive scalar in quotes'
```

### **FIS structure** — Fuzzy inference system `mamfis`object | `sugfis`object

Fuzzy inference system to evaluate, specified as a `mamfis` or `sugfis` object. Specify the name of a FIS object in the
MATLAB® workspace.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `fismatrix` |
| **Values:** | `"fis"` (default) | variable name in quotes |

### **Refresh rate** — Time between rule viewer updates positive scalar

Time between rule viewer updates in seconds, specified as a positive
scalar. During simulation, the Rule Viewer display updates at the specified
rate to show the inference process for the latest input signal
values.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `Ts` |
| **Values:** | `"2"` (default) | positive scalar in quotes |
## Libraries

Fuzzy Logic Toolbox

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Usage notes and limitations:

- Generating code using the Fuzzy Logic Controller with
  Ruleviewer block produces the same code as using the
  Fuzzy Logic Controller block. However, the Fuzzy
  Logic Controller with Ruleviewer block does not support:

  - Generating code for single-point or fixed-point data.
  - Changing the number of samples for discretizing the output
    variable range.

## Version History

**Introduced before R2006a**

### R2024b: Fuzzy inference system structures not supported

This block no longer supports fuzzy inference system structures. Use `mamfis` and
`sugfis`
objects instead. To convert existing fuzzy inference system structures to objects,
use the `convertfis` function.

### R2019b: Fuzzy inference system structures will not be supported

Support for fuzzy inference systems structures will be removed in a future
release. This change was announced in R2018b. Using fuzzy inference system
structures with this block issues a warning starting in R2019b.

## Description

Evaluate fuzzy inference system and view rules

The Fuzzy Logic Controller with Ruleviewer block implements a fuzzy
inference system (FIS) in Simulink® and displays the fuzzy inference process in the Rule Viewer during the
simulation. You specify the FIS to evaluate using the **FIS structure**
parameter. To change the time between Rule Viewer updates, specify the **Refresh
rate** in seconds.

For more information on fuzzy inference, see Fuzzy Inference Process.

The Fuzzy Logic Controller with Ruleviewer block does not support all
the features supported by the Fuzzy Logic Controller block. The Fuzzy
Logic Controller with Ruleviewer block:

- Only supports double-precision data.
- Uses `101` points for discretizing output variable
  ranges.
- Only supports `Interpreted execution` simulation
  mode.
- Does not have additional output ports for accessing intermediate fuzzy
  inference results.
