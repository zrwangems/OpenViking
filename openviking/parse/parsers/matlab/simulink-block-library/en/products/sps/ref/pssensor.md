---
type: simulink-block
title: 'PS Sensor'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Sensors and Transducers / Sensors'
documentation_page: 'pssensor'
documentation_source_path: 'ref/pssensor.html'
language: en
---

# PS Sensor

## Ports

### Input

### **U** — Physical input signal physical signal

Physical input signal.
### Conserving

### **+** — Positive voltage electrical

Electrical conserving port associated with the PS sensor positive
voltage.

### **-** — Negative voltage electrical

Electrical conserving port associated with the PS sensor negative
voltage.

## Parameters

### **Output type** — Sensor output type `Variable voltage` (default) | `Variable current` | `Variable resistor`

Indicates whether the sensor output is a `Variable
voltage` of *Y* V, a `Variable
current` of *Y* A, or
`Variable resistor` with a value of
*Y* Ω.

### **Sensor gain, A** — Output sensitivity `1` (default)

Sensitivity of the output *Y* with respect to the input
*U*, *dY/dU*.

### **Sensor offset, B** — Sensor offset `0` (default)

Output when the input *U* is zero. The output does not
exceed the limits *Y*max and
*Y*min.

### **Maximum output, Ymax** — Maximum output `5` (default)

Upper limit on the sensor output. The following table shows the units of
this parameter, which depend on the selected value of the **Output
type** parameter.

| **Output type** | Units |
| --- | --- |
| `Variable voltage` | V |
| `Variable current` | A |
| `Variable resistor` | Ω |

### **Minimum output, Ymin** — Minimum output `0.01` (default)

Lower limit on the sensor output. The following table shows the units of
this parameter, which depend on the selected value of the **Output
type** parameter.

| **Output type** | Units |
| --- | --- |
| `Variable voltage` | V |
| `Variable current` | A |
| `Variable resistor` | Ω |

If you select `Variable resistance` for the
**Output type** parameter, the minimum resistance
*Y*min must be greater than
zero.

## Libraries

Simscape / Electrical / Sensors & Transducers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

## Description

Generic linear transducer with electrical output

The PS Sensor block represents a generic linear sensor.
The block converts the physical signal input *U* into an electrical
output *Y* across the + and - ports. The **Output
type** parameter value determines which of the following electrical outputs
the block produces:

- Output voltage
- Output current
- Output resistance

*Y* is related to *U* as *Y* = max(min(*A* ·
*U* +
*B*,*Y*max),*Y*min), where *Y*min and
*Y*max are minimum and maximum limits on the
output, respectively.
