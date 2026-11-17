---
type: simulink-block
title: 'PS Signal Specification'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Utilities'
documentation_page: 'pssignalspecification'
documentation_source_path: 'ref/pssignalspecification.html'
language: en
---

# PS Signal Specification

## Ports
```yaml
ports:
- name: I
  summary: Input physical signal, typed by the block parameter value physical signal
  direction: input
- name: O
  summary: Output physical signal, typed by the block parameter value physical signal
  direction: output
```

### Input

### **I** — Input physical signal, typed by the block parameter value physical signal

Input physical signal. The signal type (size and unit) is determined by the
**Signal size and unit** parameter value.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.
### Output

### **O** — Output physical signal, typed by the block parameter value physical signal

Output physical signal. The signal type (size and unit) is determined by the
**Signal size and unit** parameter value.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.
## Parameters
```yaml
parameters:
- name: Signal size and unit
  summary: Size and unit of the input and output physical signal zeros(1, 1) 1 (default)
  group: ''
```

### **Signal size and unit** — Size and unit of the input and output physical signal `zeros(1, 1) 1` (default)

The size and unit of the physical signal, to be propagated to untyped physical
signal ports connected to the block.

The first edit box represents the signal size. Specify it as `zeros(m,
n)`. The default size, `zeros(1, 1)`, is scalar.

The second combo box represents the signal unit. By default, the unit is
`1` (unitless). You can select a unit from the drop-down list or type
the desired unit name, such as `rpm`, or a valid expression, such as
`rad/s`. For more information and a list of unit abbreviations, see
How to Specify Units in Block Dialogs
and Unit Definitions.
## Libraries

Simscape / Foundation Library / Physical Signals / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019a**

## Description

Specify size and unit of physical signal

The PS Signal Specification block lets you explicitly
specify the size and unit of a physical signal. Use this block when the signal size and unit
cannot be determined implicitly, based on port connections in the model.

The input signal at port **I** and the output signal at port
**O** have the same size and unit. Both are determined by the value of the
**Signal size and unit** parameter. Connect this block to untyped physical
signal ports to specify the desired signal type.

Specify the signal size as `zeros(m, n)`. For example, a scalar is
`zeros(1, 1)`.

The unit combo box includes a drop-down list of common units, such as those available in
the Simulink-PS Converter and the
PS-Simulink Converter block dialog
boxes. It also contains a field where you can type a unit name or expression. For more
information, see How to Specify Units in Block Dialogs.
