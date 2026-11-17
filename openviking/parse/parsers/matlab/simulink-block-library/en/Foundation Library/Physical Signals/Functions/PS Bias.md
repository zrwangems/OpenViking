---
type: simulink-block
title: 'PS Bias'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Functions'
documentation_page: 'psbias'
documentation_source_path: 'ref/psbias.html'
language: en
---

# PS Bias

## Ports
```yaml
ports:
- name: I
  summary: Input physical signal, untyped physical signal
  direction: input
- name: O
  summary: Output physical signal, untyped physical signal
  direction: output
```

### Input

### **I** — Input physical signal, untyped physical signal

Input physical signal.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.
### Output

### **O** — Output physical signal, untyped physical signal

Output physical signal.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.
## Parameters
```yaml
parameters:
- name: Bias
  summary: Constant bias to add to input signal 1 1 (default)
  group: ''
```

### **Bias** — Constant bias to add to input signal `1 1` (default)

The constant bias to add to the input signal. The first edit box represents the
value of the bias. If the input signal is a scalar, this value must also be a scalar. If
the input signal is a vector or a matrix, then this value can either be a scalar, or a
vector or matrix matching the dimensions of the input signal. You can specify both
positive and negative values.

The second combo box represents the unit of the bias. This unit must be commensurate
with the unit of the input signal. By default, the unit is `1`
(unitless). You can select a unit from the drop-down list or type the desired unit name,
such as `rpm`, or a valid expression, such as `rad/s`.
For more information and a list of unit abbreviations, see How to Specify Units in Block Dialogs and Unit Definitions.
## Libraries

Simscape / Foundation Library / Physical Signals / Functions

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023b**

## Description

Add constant bias to input physical signal

The PS Bias block adds a constant bias to the input
physical signal:

y=u+b

where:

- *y* is the physical signal at the output port
  **O**.
- *u* is the physical signal at the input port
  **I**.
- *b* is the bias.
