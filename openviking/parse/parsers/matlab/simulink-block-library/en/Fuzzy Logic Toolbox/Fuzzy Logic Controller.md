---
type: simulink-block
title: 'Fuzzy Logic Controller'
family: 'fuzzy'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'fuzzylogiccontroller'
documentation_source_path: 'fuzzylogiccontroller.html'
language: en
---

# Fuzzy Logic Controller

## Ports
```yaml
ports:
- name: in
  summary: Input signal scalar | vector
  direction: input
- name: out
  summary: Defuzzified output signal scalar | vector
  direction: output
- name: fi
  summary: Fuzzified input values matrix
  direction: output
- name: rfs
  summary: Rule firing strengths column vector
  direction: output
- name: ro
  summary: Rule outputs matrix
  direction: output
- name: ao
  summary: Aggregated output matrix | row vector
  direction: output
```

### Input

### **in** — Input signal scalar | vector

For a single-input fuzzy inference system, the input is a scalar signal. For a
multi-input fuzzy system, combine the inputs into a vector signal using blocks such
as:

- Mux (Simulink)
- Vector Concatenate (Simulink)
- Bus Creator (Simulink)
### Output

### **out** — Defuzzified output signal scalar | vector

For a single-output FIS, the output is a scalar signal. For a multi-output FIS,
the output is a vector signal. To split system outputs into scalar signals, use the
Demux (Simulink) block.

### **fi** — Fuzzified input values matrix

Fuzzified input values, obtained by evaluating the input membership functions of
each rule at the current input values.

For a type-1 FIS, **fi** is an
*NR*-by-*NU*
matrix signal, where *NR* is the number of FIS
rules. Element (*i*,*j*)
of **fi** is the value of the input membership function for the *j*th input in the *i*th
rule.

For a type-2 FIS, **fi** is an
*NR*-by-(2\**NU*)
matrix signal. The first *NU* columns contain
the fuzzified values of the upper membership function for each rule, and the last
*NU* columns contain the fuzzified values
from the lower membership functions.

For more information on fuzzifying input values, see Fuzzify Inputs.

#### Dependencies

To enable this port, select the **Fuzzified inputs (fi)**
parameter.

### **rfs** — Rule firing strengths column vector

Rule firing strengths, obtained by evaluating the antecedent of each rule; that
is, applying the fuzzy operator to the values of the fuzzified inputs.

For a type-1 FIS, **rfs** is a column vector signal of length
*NR*, where
*NR* is the number of rules, and element
*i* is the firing strength of the *i*th
rule.

For a type-2 FIS, **rfs** is an
*NR*-by-2 matrix signal. The first column
contains the rule firing strengths generated using upper membership functions, and the
second column contains the rule firing strengths generated using lower membership
functions.

For more information on applying fuzzy operators, see Apply Fuzzy Operator.

#### Dependencies

To enable this port, select the **Rule firing strengths
(rfs)** parameter.

### **ro** — Rule outputs matrix

Rule outputs, obtained by applying the rule firing strengths to the output
membership functions using the implication method specified in the FIS.

For a type-1 Mamdani FIS, **ro** is an
*NS*-by-(*NR**NY*)
matrix signal, where *NR* is the number of
rules, *NY* is the number of outputs, and
*NS* is the number of sample points used
for evaluating output variable ranges. Each column of **ro** contains the
output fuzzy set for one rule. The first *NR*
columns contain the rule outputs for the first output variable, the next
*NR* columns correspond to the second
output variable, and so on.

For a type-2 Mamdani FIS, **ro** is an
*NS*-by-(2\**NR*\**NY*)
matrix signal. The first
*NR*\**NY*
columns contain the rule outputs generated using upper membership functions, and the
last
*NR*\**NY*
columns contain the rule outputs generated using lower membership functions.

For a type-1 Sugeno system, each rule output is a scalar value. In this case,
**ro** is an
*NR*-by-*NY*
matrix signal. Element (*j*,*k*) of **ro**
is the value of the *k*th output variable for the
*j*th rule.

For a type-2 Sugeno system, **ro** is an
*NR*-by-(3\**NY*)
array. The first *NY* columns contain the rule
output levels. The next *NY* columns contain
the corresponding rule firing strengths generated using upper membership functions.
The last *NY* columns contain the rule firing
strengths generated using lower membership functions. For example, in a three-output
system, columns 4 and 7 contain the firing strengths for the output levels in column
1.

For more information on fuzzy implication, see Apply Implication Method.

#### Dependencies

- To enable this port, select the **Rule outputs (ro)**
  parameter.
- To specify *NS*, use the
  **Number of samples for output discretization**
  parameter.

### **ao** — Aggregated output matrix | row vector

Aggregate output for each output variable, obtained by combining the corresponding
outputs from all the rules using the aggregation method specified in the FIS.

For a type-1 Mamdani fuzzy inference system, the aggregate result for each output
variable is a fuzzy set. In this case, **ao** is as an
*NS*-by-*NY*
matrix signal, where *NY* is the number of
outputs and *NS* is the number of sample
points used for evaluating output variable ranges. Each column of **ao**
contains the aggregate fuzzy set for one output variable.

For a type-2 Mamdani FIS, the aggregate result for each output variable is a fuzzy
set. In this case, **ao** is as an
*NS*-by-(2\**NY*)
matrix signal. The first *NY* columns contain
the aggregated outputs generated using upper membership functions, and the last
*NY* columns contain the aggregated
outputs generated using lower membership functions.

For a type-1 Sugeno system, the aggregate result for each output variable is a
scalar value. In this case, **ao** is a row vector of length
*NY*, where element *k*
is the sum of the rule outputs for the *k*th output variable.

For a type-2 Sugeno system, **ao** is an
*NR*-by-(3\**NY*)
array. **ro** contains the same data as **ao** with the columns
sorted based on the output levels. For example, in a three-output system, when the
output levels in column 1 are sorted, the corresponding firing strengths in columns 4
and 7 are adjusted accordingly.

For more information on fuzzy aggregation, see Aggregate All Outputs.

#### Dependencies

- To enable this port, select the **Aggregated outputs
  (ao)** parameter.
- To specify *NS*, use the
  **Number of samples for output discretization**
  parameter.
## Parameters
```yaml
parameters:
- name: FIS name
  summary: Fuzzy inference system to evaluate mamfis object | sugfis object | mamfistype2 object | sugfistype2 object | FIS
    file name in quotes | MAT file name in quotes
  group: General
  block_parameter: FIS
  values: '''"tipper.fis"'' (default) | variable name in quotes | file name in quotes'
- name: Design
  summary: Open Fuzzy Logic Designer button
  group: General
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
- name: Implement FIS as lookup table
  summary: Convert FIS to lookup table off (default) | on
  group: General
  block_parameter: UseLookupTable
  values: '"off" (default) | "on"'
- name: Number of input breakpoints (samples)
  summary: Number of lookup table breakpoints 10 (default) | positive integer
  group: General
  block_parameter: NumBreakpoints
  values: '"10" (default) | positive integer in quotes'
- name: Fuzzified inputs (fi)
  summary: Enable fi output port off (default) | on
  group: General
  block_parameter: FuzzifiedInputs
  values: '"off" (default) | "on"'
- name: Rule firing strengths (rfs)
  summary: Enable rfs output port off (default) | on
  group: General
  block_parameter: RuleFiringStrengths
  values: '"off" (default) | "on"'
- name: Rule outputs (ro)
  summary: Enable ro output port off (default) | on
  group: General
  block_parameter: RuleOutputs
  values: '"off" (default) | "on"'
- name: Aggregated outputs (ao)
  summary: Enable ao output port off (default) | on
  group: General
  block_parameter: AggregatedOutputs
  values: '"off" (default) | "on"'
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

### **FIS name** — Fuzzy inference system to evaluate `mamfis` object | `sugfis` object | `mamfistype2` object | `sugfistype2` object | FIS file name in quotes | MAT file name in quotes

Fuzzy inference system to evaluate, specified as one of the following:

- `mamfis` or
  `sugfis`
  object — Specify the name of a type-1 FIS object in the MATLAB® workspace.
- `mamfistype2` or `sugfistype2` object — Specify the name of a type-2 FIS object in the
  MATLAB workspace.
- Name of a FIS file (`*.fis`) in the current working folder or
  on the MATLAB path. Including the file extension in the file name is optional.
  Specify the filename in quotes.
- Name of a MAT file
  (`*.mat`) in the current working folder or on the MATLAB path. The MAT file must contain only one FIS object. Including the
  file extension in the file name is optional. Specify the filename in
  quotes. *(since R2024a)*

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `FIS` |
| **Values:** | `'"tipper.fis"'` (default) | variable name in quotes | file name in quotes |

### **Design** — Open Fuzzy Logic Designer button

Open Fuzzy Logic Designer to view and modify the FIS
design. You can then update the block to use the modified FIS design. For more
information, see Design Fuzzy Inference System in Simulink.

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

### **Implement FIS as lookup table** — Convert FIS to lookup table `off` (default) | `on`

*Since R2025a*

To reduce the processing time for the controller, you can represent your FIS as a
lookup table.

The block divides the input range of each FIS input into equally sized regions
based on the number of breakpoints, which you specify using the **Number of
input breakpoints** parameter.

For each input combination, the block calculates a corresponding FIS output.
During evaluation, the controller uses these precomputed outputs instead of performing
the fuzzy inference process.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `UseLookupTable` |
| **Values:** | `"off"` (default) | `"on"` |

### **Number of input breakpoints (samples)** — Number of lookup table breakpoints `10` (default) | positive integer

*Since R2025a*

Number of lookup table breakpoints, specified as a positive integer. Increasing
the number of breakpoints improves the accuracy of the lookup table while increasing
its memory requirements.

#### Dependencies

- To enable this parameter, select the **Implement FIS as lookup
  table** parameter.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `NumBreakpoints` |
| **Values:** | `"10"` (default) | positive integer in quotes |

### **Fuzzified inputs (fi)** — Enable `fi` output port `off` (default) | `on`

Enable **fi** output port for accessing intermediate fuzzified input
data.

#### Dependencies

- Intermediate inference outputs are not
  available when you select **Implement FIS as lookup
  table**. *(since R2025a)*

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `FuzzifiedInputs` |
| **Values:** | `"off"` (default) | `"on"` |

### **Rule firing strengths (rfs)** — Enable `rfs` output port `off` (default) | `on`

Enable **rfs** output port for accessing intermediate rule firing
strength data.

#### Dependencies

- Intermediate inference outputs are not
  available when you select **Implement FIS as lookup
  table**. *(since R2025a)*

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `RuleFiringStrengths` |
| **Values:** | `"off"` (default) | `"on"` |

### **Rule outputs (ro)** — Enable `ro` output port `off` (default) | `on`

Enable **ro** output port for accessing intermediate rule output
data.

#### Dependencies

- Intermediate inference outputs are not
  available when you select **Implement FIS as lookup
  table**. *(since R2025a)*

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `RuleOutputs` |
| **Values:** | `"off"` (default) | `"on"` |

### **Aggregated outputs (ao)** — Enable `ao` output port `off` (default) | `on`

Enable **ao** output port for accessing intermediate aggregate output
data.

#### Dependencies

- Intermediate inference outputs are not
  available when you select **Implement FIS as lookup
  table**. *(since R2025a)*

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `AggregatedOutputs` |
| **Values:** | `"off"` (default) | `"on"` |

### **Simulate using** — Simulation mode `Interpreted execution` (default) | `Code generation`

Simulation mode, specified as one of these values:

- `Interpreted execution` — Simulate fuzzy systems
  using precompiled MEX files for `single` and
  `double` data types. Using this option reduces the
  initial compilation time of the model.
- `Code generation` — Simulate fuzzy system without
  precompiled MEX files. Use this option when simulating fuzzy systems for code
  generation applications.

For fixed-point data types, the Fuzzy Logic Controller block always
simulates using `Code generation` mode.

#### Dependencies

- Setting the simulation mode is not supported when you select
  **Implement FIS as lookup table**.

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

**Introduced before R2006a**

### R2025a: Open Fuzzy Logic Designer from block

You can now open Fuzzy Logic Designer from the Fuzzy Logic
Controller block by clicking **Design**. The app opens and
imports the FIS specified by the **FIS name** parameter.

### R2025a: Implement FIS as lookup table

You can represent your FIS as a lookup table, which reduces processing time. To use a
lookup table, select the **Implement FIS as lookup table** parameter. The
block divides the input range of each FIS input into equally sized regions based on the
number of breakpoints, which you specify using the **Number of input
breakpoints** parameter.

### R2024b: Fuzzy inference system structures not supported

This block no longer supports fuzzy inference system structures. Use `mamfis` and `sugfis` objects
instead. To convert existing fuzzy inference system structures to objects, use the `convertfis` function.

### R2024a: Specify FIS using MAT file

You can specify the FIS to evaluate using a MAT file in the current working folder or on
the MATLAB path. The MAT file must contain only one FIS object.

### R2019b: Fuzzy inference system structures will not be supported

Support for fuzzy inference systems structures will be removed in a future release. This
change was announced in R2018b. Using fuzzy inference system structures with this block
issues a warning starting in R2019b.

### R2017b: Access intermediate fuzzy inference results

Using the Fuzzy Logic Controller block, you can access intermediate fuzzy
inference results by enabling the following output ports.

- `fi` — Fuzzified input values
- `rfs` — Rule firing strengths
- `ro` — Rule outputs
- `ao` — Aggregated membership function for each output
  variable

### R2017b: Expanded data type support

The Fuzzy Logic Controller block supports double-precision,
single-precision, and fixed-point data types.

### R2017b: Improved code generation support

When generating code using Simulink
Coder™, the Fuzzy Logic Controller block supports code generation for
fuzzy systems that use:

- Single-precision data.
- Fixed-point data. To generate code for fixed-point data, you need Fixed-Point Designer™ software.
- Custom membership functions and custom inference functions. For more information on
  specifying custom functions for a fuzzy system, see Build Fuzzy Systems Using Custom Functions.

### R2017b: PLC code generation support

The Fuzzy Logic Controller block supports generation of IEC 61131-3
Structured Text for PLC deployment using Simulink
PLC Coder™ software.

## Description

Evaluate fuzzy inference system

The Fuzzy Logic Controller block implements a fuzzy inference system (FIS)
in Simulink®. You specify the FIS to evaluate using the **FIS name**
parameter.

For more information on fuzzy inference, see Fuzzy Inference Process.

To display the fuzzy inference process during simulation, use the Fuzzy Logic
Controller with Ruleviewer block.
