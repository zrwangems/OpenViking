---
type: simulink-block
title: 'FIS Tree'
family: 'fuzzy'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'fistreeblock'
documentation_source_path: 'fistreeblock.html'
language: en
---

# FIS Tree

## Ports
```yaml
ports:
- name: in
  summary: Input signal scalar | vector
  direction: input
- name: out
  summary: Defuzzified output signal scalar | vector
  direction: output
```

### Input

### **in** — Input signal scalar | vector

For a single-input FIS tree, the input is a scalar signal. For a multi-input FIS
tree, combine the inputs into a vector signal using blocks such as:

- Mux (Simulink)
- Vector Concatenate (Simulink)
- Bus Creator (Simulink)
### Output

### **out** — Defuzzified output signal scalar | vector

For a single-output FIS tree, the output is a scalar signal. For a multi-output
FIS tree, the output is a vector signal. To split system outputs into scalar signals,
use the Demux (Simulink) block.
## Parameters
```yaml
parameters:
- name: FIS tree name
  summary: FIS tree to evaluate fistree object | MAT file name in quotes
  group: General
  block_parameter: FIS
  values: '''"weightedTipper"'' (default) | variable name in quotes | file name in quotes'
- name: Number of samples for output discretization
  summary: Number of points in output fuzzy sets 101 (default) | integer greater than 1
  group: General
  block_parameter: OutputSampleNumber
  values: '"101" (default) | integer greater than 1 in quotes'
- name: Data type
  summary: Signal data type double (default) | single | fixed-point | expression
  group: General
  block_parameter: DataType
  values: '"double" (default) | "single" | "fixdt(1,16,0)" | "fixdt(1,16,2^0,0)"'
- name: Simulate using
  summary: Simulation mode Interpreted execution (default) | Code generation
  group: General
  block_parameter: SimulateUsing
  values: '"Interpreted execution" (default) | "Code generation"'
- name: Out of range input value
  summary: Diagnostic message behavior when an input is out of range warning (default) | error | none
  group: Diagnostics
  block_parameter: OutOfRangeInputValueMessage
  values: '"warning" (default) | "error" | "none"'
- name: No rule fired
  summary: Diagnostic message behavior when no rules fire warning (default) | error | none
  group: Diagnostics
  block_parameter: NoRuleFiredMessage
  values: '"warning" (default) | "error" | "none"'
- name: Empty output fuzzy set
  summary: Diagnostic message behavior when an output fuzzy set is empty warning (default) | error | none
  group: Diagnostics
  block_parameter: EmptyOutputFuzzySetMessage
  values: '"warning" (default) | "error" | "none"'
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### General

### **FIS tree name** — FIS tree to evaluate `fistree` object | MAT file name in quotes

FIS tree to evaluate, specified as one of the following:

- `fistree` object in the MATLAB® workspace.
- Name of a MAT file (`*.mat`) in the current working folder or
  on the MATLAB path. The MAT file must contain only one FIS object. Including the
  file extension in the file name is optional. Specify the filename in
  quotes.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `FIS` |
| **Values:** | `'"weightedTipper"'` (default) | variable name in quotes | file name in quotes |

### **Number of samples for output discretization** — Number of points in output fuzzy sets 101 (default) | integer greater than `1`

Number of samples for discretizing the range of FIS output variables, specified as an integer greater than `1`. This value corresponds to the number of points in the output fuzzy set for each rule.

To reduce memory usage while evaluating Mamdani FISs, specify a lower number of samples. Doing so sacrifices the accuracy of the defuzzified output value. Specifying a low number of samples can make the output area for defuzzification zero. In this case, the defuzzified output value is the midpoint of the output variable range.

**Note**

The block ignores this parameter when evaluating Sugeno FISs.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `OutputSampleNumber` |
| **Values:** | `"101"` (default) | integer greater than `1` in quotes |

### **Data type** — Signal data type `double` (default) | `single` | `fixed-point` | `expression`

Signal data type, specified as one of the following:

- `double` — Double-precision signals
- `single` — Single-precision signals
- `fixdt(1,16,0)` — Fixed-point signals with binary point scaling
- `fixdt(1,16,2^0,0)` — Fixed-point signals with slope and bias scaling
- Expression — Expression that evaluates to one of these data types

For fixed-point data types, you can configure the signedness, word length, and scaling parameters using the **Data Type Assistant**. For more information, see Specifying a Fixed-Point Data Type (Simulink).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `DataType` |
| **Values:** | `"double"` (default) | `"single"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` |

### **Simulate using** — Simulation mode `Interpreted execution` (default) | `Code generation`

Simulation mode, specified as one of these values:

- `Interpreted execution` — Simulate fuzzy systems
  using precompiled MEX files for `single` and
  `double` data types. Using this option reduces the
  initial compilation time of the model.
- `Code generation` — Simulate fuzzy system without
  precompiled MEX files. Use this option when simulating fuzzy systems for code
  generation applications.

For fixed-point data types, the FIS Tree block always simulates
using `Code generation` mode.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `SimulateUsing` |
| **Values:** | `"Interpreted execution"` (default) | `"Code generation"` |

### Diagnostics

### **Out of range input value** — Diagnostic message behavior when an input is out of range `warning` (default) | `error` | `none`

Diagnostic message behavior when an input is out of range, specified as one of the following:

- `warning` — Report the diagnostic message as a warning.
- `error` — Report the diagnostic message as an error.
- `none` — Do not report the diagnostic message.

When an input value is out of range, corresponding rules in the fuzzy system can have unexpected firing strengths.

#### Dependencies

- Diagnostic messages are provided only when the **Simulate using** parameter is `Interpreted execution`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `OutOfRangeInputValueMessage` |
| **Values:** | `"warning"` (default) | `"error"` | `"none"` |

### **No rule fired** — Diagnostic message behavior when no rules fire `warning` (default) | `error` | `none`

Diagnostic message behavior when no rules fire for a given output variable, specified as one of the following:

- `warning` — Report the diagnostic message as a warning.
- `error` — Report the diagnostic message as an error.
- `none` — Do not report the diagnostic message.

When **No rule fired** is `warning` or `none` and no rules fire for a given output, the defuzzified output value is set to its mean range value.

#### Dependencies

- Diagnostic messages are provided only when the **Simulate using** parameter is `Interpreted execution`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `NoRuleFiredMessage` |
| **Values:** | `"warning"` (default) | `"error"` | `"none"` |

### **Empty output fuzzy set** — Diagnostic message behavior when an output fuzzy set is empty `warning` (default) | `error` | `none`

Diagnostic message behavior when an output fuzzy set is empty, specified as one of the following:

- `warning` — Report the diagnostic message as a warning.
- `error` — Report the diagnostic message as an error.
- `none` — Do not report the diagnostic message.

When **Empty output fuzzy set** is `warning` or `none` and an output fuzzy set is empty, the defuzzified value for the corresponding output is set to its mean range value.

#### Dependencies

- This diagnostic message applies to Mamdani systems only.
- Diagnostic messages are provided only when the **Simulate using** parameter is `Interpreted execution`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `EmptyOutputFuzzySetMessage` |
| **Values:** | `"warning"` (default) | `"error"` | `"none"` |
## Libraries

Fuzzy Logic Toolbox

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2024a**

## Description

Evaluate fuzzy inference system tree

The FIS Tree block implements a tree of fuzzy inference systems (FISs) in
Simulink®. You specify the FIS tree to evaluate using the **FIS tree
name** parameter.

For more information on FIS trees, see FIS Trees.
