---
type: simulink-block
title: 'M-PAM Modulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / PAM/QAM'
documentation_page: 'mpammodulatorbaseband'
documentation_source_path: 'ref/mpammodulatorbaseband.html'
language: en
---

# M-PAM Modulator Baseband

## Ports
```yaml
ports:
- name: In
  summary: Input signal scalar | column vector
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
- name: Out
  summary: '*M*-PAM-modulated baseband signal scalar | column vector'
  direction: output
  data_types: single | double | fixed point
```

### Input

### **In** — Input signal scalar | column vector

Input signal, specified as a scalar or column vector. The input data
must be binary values or integers in the range [0, (*M* – 1)], where *M* is the modulation order as
specified by the **M-ary
number** parameter. This port is unnamed on the
block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### Output

### **Out** — *M*-PAM-modulated baseband signal scalar | column vector

*M*-PAM-modulated baseband signal, returned as a
scalar or column vector. Use the **Output
data type** parameter to specify the output data type.
This port is unnamed on the block.

**Data Types:** `single` | `double` | `fixed point`
## Parameters
```yaml
parameters:
- name: M-ary number
  summary: Modulation order 4 (default) | positive, even integer
  group: Main
- name: Input type
  summary: Type of input value Integer (default) | Bit
  group: Main
- name: Constellation ordering
  summary: Mapping order of symbols Binary (default) | Gray
  group: Main
- name: Normalization method
  summary: Scaling method for constellation Min. distance between symbols (default) | Average Power | Peak Power
  group: Main
- name: Minimum distance
  summary: Distance between two nearest constellation points 2 (default) | positive scalar
  group: Main
- name: Average power, referenced to 1 ohm (watts)
  summary: Average power 1 (default) | positive scalar
  group: Main
- name: Peak power, referenced to 1 ohm (watts)
  summary: Maximum power 1 (default) | positive scalar
  group: Main
- name: View Constellation
  summary: Option to plot reference constellation button
  group: Main
- name: Output data type
  summary: 'Output data type double (default) | single | fixdt(1,16) | fixdt(1,16,0) | Inherit: Inherit via back propagation
    | <data type expression>'
  group: Data Types
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Main

### **M-ary number** — Modulation order `4` (default) | positive, even integer

Modulation order, specified as a positive, even integer. The
modulation order, *M*, specifies the number of points
in the signal constellation. The block scales the signal constellation
based on how you set the **Normalization method** parameter. For more information,
see Constellation Size and Scaling.

### **Input type** — Type of input value `Integer` (default) | `Bit`

Type of input value, specified as `Integer`
or `Bit`. When you set this parameter to
`Bit`, the **M-ary
number** parameter must be
2*K* for some
positive integer *K*.

### **Constellation ordering** — Mapping order of symbols `Binary` (default) | `Gray`

Mapping order of the symbols, specified as
`Gray` or
`Binary`. This parameter indicates how the
block maps binary words to points of the signal constellation.

- When you set this parameter to
  `Binary`, the block uses
  binary-coded constellation.
- When you set this parameter to
  `Gray`, the block uses a Gray-coded
  constellation.

### **Normalization method** — Scaling method for constellation `Min. distance between symbols` (default) | `Average Power` | `Peak Power`

Scaling method for the constellation, specified as `Min.
distance between symbols`, `Average
Power`, or `Peak Power`. For
more information, see Constellation Size and Scaling.

### **Minimum distance** — Distance between two nearest constellation points `2` (default) | positive scalar

Distance between the two nearest constellation points, specified as a
positive scalar.

#### Dependencies

This parameter appears when you set **Normalization method** to `Min. distance
between symbols`.

### **Average power, referenced to 1 ohm (watts)** — Average power `1` (default) | positive scalar

Average power of the symbols in the constellation in watts, specified
as a positive scalar. Power values assume a nominal impedance of 1
ohm.

#### Dependencies

This parameter appears when you set **Normalization method** to `Average
Power`.

### **Peak power, referenced to 1 ohm (watts)** — Maximum power `1` (default) | positive scalar

Maximum power of the symbols in the constellation in watts, specified
as a positive scalar. Power values assume a nominal impedance of 1
ohm.

#### Dependencies

This parameter appears when you set **Normalization method** to `Peak
Power`.

### **View Constellation** — Option to plot reference constellation button

Click **View
Constellation** on the block mask to visualize a signal constellation for the
specified block parameters. Before viewing a constellation, apply the parameter settings. For
more information, see View Constellation of Modulator Block.

### Data Types

### **Output data type** — Output data type `double` (default) | `single` | `fixdt(1,16)` | `fixdt(1,16,0)` | `Inherit: Inherit via back propagation` | `<data type expression>`

Output data type, specified as `double`,
`single`,
`fixdt(1,16)`,
`fixdt(1,16,0)`, `Inherit:
Inherit via back propagation`, or `<data
type expression>`.

- `fixdt(1,16)`,
  `fixdt(1,16,0)`, or
  `<data type expression>`
  enables parameters in which you can further specify
  details.
- `Inherit: Inherit via back
  propagation` sets the output data type and
  scaling to match the following block.

For information about specifying data types, see Data Type Assistant.
## Libraries

Communications Toolbox / Modulation / Digital Baseband Modulation / AM

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed pointa, b` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
|  |  |
| --- | --- |
| a ufix(1) at the input if ''input type'' is set to ''bit''. ufix(ceil(log2(M))) at input if ''input type'' is set to ''integer'' for M-ary modulation.  b Fixed-point outputs must be signed. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Modulate using M -ary pulse amplitude modulation

The M-PAM Modulator Baseband block modulates a signal by using
*M*-ary pulse amplitude modulation. The output is a baseband
representation of the modulated signal.

**Note**

All values of power assume a nominal impedance of 1 ohm.
