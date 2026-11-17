---
type: simulink-block
title: 'Average-Value DC-DC Converter'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'averagevaluedcdcconverter'
documentation_source_path: 'ref/averagevaluedcdcconverter.html'
language: en
---

# Average-Value DC-DC Converter

## Ports
```yaml
ports:
- name: DutyCycle
  summary: Duty cycle physical | scalar
  direction: conserving
  data_types: double
- name: Iref
  summary: Current reference physical
  direction: conserving
  data_types: double
- name: Vref
  summary: Voltage reference physical
  direction: conserving
  data_types: double
- name: 1+
  summary: Positive DC voltage 1 electrical | scalar
  direction: conserving
  data_types: double
- name: 1-
  summary: Negative DC voltage 1 electrical | scalar
  direction: conserving
  data_types: double
- name: 2+
  summary: Positive DC voltage 2 electrical | scalar
  direction: conserving
  data_types: double
- name: 2-
  summary: Negative DC voltage 2 electrical | scalar
  direction: conserving
  data_types: double
```

### Conserving

### **DutyCycle** — Duty cycle physical | scalar

Electrical conserving port associated with the duty cycle.

#### Dependencies

To enable this port, set **Control Input** to `Duty
Cycle`.

**Data Types:** `double`

### **Iref** — Current reference physical

Electrical conserving port associated with the current
reference.

#### Dependencies

To enable this port, set **Control Input** to `Current
reference`.

**Data Types:** `double`

### **Vref** — Voltage reference physical

Electrical conserving port associated with the voltage
reference.

#### Dependencies

To enable this port, set **Control Input** to `Voltage
reference`.

**Data Types:** `double`

### **1+** — Positive DC voltage 1 electrical | scalar

Electrical conserving port associated with the positive terminal of
the first DC voltage.

**Data Types:** `double`

### **1-** — Negative DC voltage 1 electrical | scalar

Electrical conserving port associated with the negative terminal of
the first DC voltage.

**Data Types:** `double`

### **2+** — Positive DC voltage 2 electrical | scalar

Electrical conserving port associated with the positive terminal of
the second DC voltage.

**Data Types:** `double`

### **2-** — Negative DC voltage 2 electrical | scalar

Electrical conserving port associated with the negative terminal of
the second DC voltage.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Implementation mode
  summary: Converter implementation mode Behavioral (default) | Average value
  group: ''
- name: Converter type
  summary: Converter type Buck converter (default) | Buck-boost converter | Boost converter
  group: ''
- name: Control input
  summary: Control input Duty cycle (default) | Current reference | Voltage reference
  group: ''
- name: Converter efficiency
  summary: Converter efficiency parameterization Constant (default) | Tabulated
  group: ''
- name: Efficiency (%)
  summary: Converter efficiency 100 (default) | positive scalar
  group: ''
- name: Output current vector
  summary: Vector of output current [0, 2, 5] A (default) | row vector of at least two elements
  group: ''
- name: Efficiency vector (%)
  summary: Vector of efficiencies [90, 95, 98] (default) | row vector of at least two elements
  group: ''
- name: Inductance
  summary: Inductance 1e-6 H (default) | positive scalar
  group: ''
- name: Inductor series resistance
  summary: Series resistance of inductor 0 Ohm (default) | nonnegative scalar
  group: ''
- name: Capacitance
  summary: Capacitance 1e-7 F (default) | positive scalar
  group: ''
- name: Capacitor effective series resistance
  summary: Series resistance of capacitor 1e-6 Ohm (default) | nonnegative scalar
  group: ''
```

### **Implementation mode** — Converter implementation mode `Behavioral` (default) | `Average value`

*Since R2025a*

Option to specify the implementation mode of the converter. To control the
inverter state variables, set this parameter to `Average
value`. For fast simulation with no dynamics, set this
parameter to `Behavioral`.

### **Converter type** — Converter type `Buck converter` (default) | `Buck-boost converter` | `Boost converter`

Type of converter.

#### Dependencies

To enable this parameter, set **Control Input** to
`Duty Cycle` or **Implementation
mode** to `Average value`.

### **Control input** — Control input `Duty cycle` (default) | `Current reference` | `Voltage reference`

Specify the control input to convert the electrical energy between the two
sides.

#### Dependencies

To enable this parameter, set **Implementation mode**
to `Behavioral`.

### **Converter efficiency** — Converter efficiency parameterization `Constant` (default) | `Tabulated`

Specify the parameterization of the converter efficiency. If you select
`Tabulated`, the conduction losses depend on
the provided output current.

**Note**

For tabulated efficiency, the extrapolation method is nearest.
Therefore, the efficiency does not go above the highest value or below
the lowest value in the **Efficiency vector (%)**
parameter.

#### Dependencies

To enable this parameter, set **Implementation mode**
to `Behavioral`.

### **Efficiency (%)** — Converter efficiency `100` (default) | positive scalar

Efficiency of the converter, in percentage.

#### Dependencies

To enable this parameter, set **Implementation mode** to
`Behavioral` and **Converter
efficiency** to `Constant`.

### **Output current vector** — Vector of output current `[0, 2, 5]` `A` (default) | row vector of at least two elements

Vector of output currents.

#### Dependencies

To enable this parameter, set **Implementation mode** to
`Behavioral` and **Converter
efficiency** to
`Tabulated`.

### **Efficiency vector (%)** — Vector of efficiencies `[90, 95, 98]` (default) | row vector of at least two elements

Vector of efficiencies for each output current specified in
**Output current vector**, in percentage. This
parameter must have the same size of **Output current
vector**.

#### Dependencies

To enable this parameter, set **Implementation mode** to
`Behavioral` and **Converter
efficiency** to
`Tabulated`.

### **Inductance** — Inductance `1e-6` `H` (default) | positive scalar

*Since R2025a*

Inductance.

#### Dependencies

To enable this parameter, set **Implementation mode**
to `Average value`.

### **Inductor series resistance** — Series resistance of inductor `0` `Ohm` (default) | nonnegative scalar

*Since R2025a*

Series resistance of the inductor.

#### Dependencies

To enable this parameter, set **Implementation mode**
to `Average value`.

### **Capacitance** — Capacitance `1e-7` `F` (default) | positive scalar

*Since R2025a*

Capacitance.

#### Dependencies

To enable this parameter, set **Implementation mode**
to `Average value`.

### **Capacitor effective series resistance** — Series resistance of capacitor `1e-6` `Ohm` (default) | nonnegative scalar

*Since R2025a*

Series resistance of the capacitor.

#### Dependencies

To enable this parameter, set **Implementation mode**
to `Average value`.
## Libraries

Simscape / Electrical / Semiconductors & Converters / Converters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

### R2025a: Support bidirectional power flow and model LC dynamics

The Average-Value DC-DC Converter block now supports bidirectional power flow. You can also model
the converter LC dynamics. To model LC dynamics, set the **Implementation
mode** parameter to `Average value`. This
option exposes the LC parameters, including the inductance and the
capacitance.

## Description

Average-value DC-DC converter

The Average-Value DC-DC Converter block represents a
controlled average-value DC-DC converter. You can program the block as a buck converter,
boost converter, or buck-boost converter by providing the duty cycle. The diagram shows
the equivalent circuit for the block with duty cycle as input. The converter contains a
controlled current source and a controlled voltage source. Use the duty cycle, the
current reference, or the voltage reference ports as control input to convert the
electrical energy between the connected components on either side of the converter.

### Equations

If you set the **Control input** parameter to `Duty
cycle`, the input current and output voltage are a function of the
duty cycle and depend on the converter type.

**Voltage and Current Equations**

| Converter Type | Output Voltage, v2 | Input Current, i1 |
| --- | --- | --- |
| **Buck** | v2=DutyCycle⋅v1 | i1=DutyCycle⋅i2 |
| **Boost** | v2=v11−DutyCycle | i1=i21−DutyCycle |
| **Buck-Boost** | v2=DutyCycle⋅v11−DutyCycle | i1=DutyCycle⋅i21−DutyCycle |

If you set the **Control input** parameter to `Current
reference`, the converter sets the output current and it computes
the voltage.

Similarly, if you set the **Control input** parameter to
`Voltage reference`, the converter sets the output
voltage and it computes the current.

### Variables

*Since R2025a*

To enable the **Initial Targets** and **Nominal
Values** sections, set the **Implementation mode**
parameter to `Average value`.

To set the priority and initial target values for the block variables before
simulation, use the **Initial Targets** section in the block dialog
box or Property Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a
model. Using system scaling based on nominal values increases the simulation
robustness. You can specify nominal values using different sources, including the
**Nominal Values** section in the block dialog box or Property
Inspector. For more information, see System Scaling by Nominal Values.

### Limitations and Assumptions

- The input voltage is positive.
- All converter types use the same polarity for input and output.
