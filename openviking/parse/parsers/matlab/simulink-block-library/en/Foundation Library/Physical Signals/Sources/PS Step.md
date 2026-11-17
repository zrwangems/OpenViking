---
type: simulink-block
title: 'PS Step'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Sources'
documentation_page: 'psstep'
documentation_source_path: 'ref/psstep.html'
language: en
---

# PS Step

## Ports
```yaml
ports:
- name: O
  summary: Output physical signal, typed by the block parameter values and units physical signal
  direction: output
```

### Output

### **O** — Output physical signal, typed by the block parameter values and units physical signal

Output physical signal. The signal size matches the size of **Initial
value** and **Final value** parameter values. The signal
unit is determined by the **Initial value** and **Final
value** parameter units.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.
## Parameters
```yaml
parameters:
- name: Step time
  summary: Time when step occurs 1 s (default) | scalar
  group: ''
- name: Initial value
  summary: Output before step 0 1 (default) | scalar | vector | matrix
  group: ''
- name: Final value
  summary: Output after step 1 1 (default) | scalar | vector | matrix
  group: ''
```

### **Step time** — Time when step occurs `1 s` (default) | scalar

Time when the signal changes value. Between the start of simulation and
**Step time**, the output of the block remains at **Initial
value**, then instantaneously changes to **Final value** and
remains at that value until the end of simulation.

### **Initial value** — Output before step `0 1` (default) | scalar | vector | matrix

Block output until the simulation time reaches **Step time**. The
first edit box represents the parameter value. You can specify a scalar, vector, or
matrix. By default, the value is a scalar, `0`. If you specify a vector
or a matrix, **Final value** must also be a vector or a matrix of the
same size or a scalar.

The second combo box represents the parameter unit. The specified unit must be
commensurate with the unit of the **Final value** parameter. By
default, the unit is `1` (unitless). You can select a unit from the
drop-down list or type the desired unit name, such as `Pa`, or a valid
expression, such as `m^2`. For more information and a list of unit
abbreviations, see How to Specify Units in Block Dialogs
and Unit Definitions.

### **Final value** — Output after step `1 1` (default) | scalar | vector | matrix

Block output when the simulation time reaches and exceeds **Step
time**. The first edit box represents the parameter value. You can specify a
scalar, vector, or matrix. By default, the value is a scalar, `1`. If
you specify a vector or a matrix, **Initial value** must also be a
vector or a matrix of the same size or a scalar.

The second combo box represents the parameter unit. The specified unit must be
commensurate with the unit of the **Initial value** parameter. By
default, the unit is `1` (unitless). You can select a unit from the
drop-down list or type the desired unit name, such as `Pa`, or a valid
expression, such as `m^2`. For more information and a list of unit
abbreviations, see How to Specify Units in Block Dialogs
and Unit Definitions.
## Libraries

Simscape / Foundation Library / Physical Signals / Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

## Description

Generate physical signal shaped as step function

The PS Step block generates a physical signal that starts
at a specified initial value and changes instantaneously to a new value at a specified time.
The **Step time**, **Initial value**, and **Final
value** parameters determine the characteristics of the output signal:

- The **Step time** parameter determines when the signal value changes
  from **Initial value** to **Final value**.
- The **Initial value** and **Final value** parameter
  values determine whether the output signal is a scalar, vector, or matrix. If one of these
  parameters is a vector or a matrix, the other must be a vector or a matrix of the same
  size or a scalar. The output signal is then also a vector or a matrix of the same
  size.
- The **Initial value** and **Final value** parameters
  must have commensurate units. The unit at the output port is determined by unit
  propagation rules. If the two parameters have the same units, then the output signal unit
  is also the same. If the parameter units are different, then the unit of the output signal
  is the base unit commensurate with the units of the parameters. For more information, see
  Physical Signal Unit Propagation.
