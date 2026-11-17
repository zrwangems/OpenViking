---
type: simulink-block
title: 'Average-Value Chopper'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'averagevaluechopper'
documentation_source_path: 'ref/averagevaluechopper.html'
language: en
---

# Average-Value Chopper

## Ports
```yaml
ports:
- name: DutyCycle
  summary: Duty Cycle electrical | scalar
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

### **DutyCycle** — Duty Cycle electrical | scalar

Electrical conserving port associated with the duty cycle.

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
- name: Chopper type
  summary: Chopper class Class A - first quadrant (default) | Class B - second quadrant | Class C - first and second quadrant
    | Class D - first and fourth quadrant | Class E - four quadrant
  group: ''
- name: Converter efficiency
  summary: Converter efficiency parameterization Constant (default) | Tabulated
  group: ''
- name: Efficiency (%)
  summary: Converter efficiency 100 (default) | scalar
  group: ''
- name: Output current vector
  summary: Vector of output current [0, 2, 5] A (default) | row vector of at least two elements
  group: ''
- name: Efficiency vector (%)
  summary: Vector of efficiencies [90, 95, 98] (default) | row vector of at least two elements
  group: ''
```

### **Chopper type** — Chopper class `Class A - first quadrant` (default) | `Class B - second quadrant` | `Class C - first and second quadrant` | `Class D - first and fourth quadrant` | `Class E - four quadrant`

Chopper class.

### **Converter efficiency** — Converter efficiency parameterization `Constant` (default) | `Tabulated`

Specify the parameterization of the converter efficiency. If you select
`Tabulated`, conduction losses will depend on
the provided output current.

### **Efficiency (%)** — Converter efficiency 100 (default) | scalar

Efficiency of the converter, in percentage.

#### Dependencies

To enable this parameter, set **Converter
efficiency** to `Constant`.

### **Output current vector** — Vector of output current [0, 2, 5] `A` (default) | row vector of at least two elements

Vector of output currents.

#### Dependencies

To enable this parameter, set **Converter
efficiency** to
`Tabulated`.

### **Efficiency vector (%)** — Vector of efficiencies [90, 95, 98] (default) | row vector of at least two elements

Vector of efficiencies for each output current specified in
**Output current vector**, in percentage. This
parameter must have the same size of **Output current
vector**.

#### Dependencies

To enable this parameter, set **Converter
efficiency** to
`Tabulated`.
## Libraries

Simscape / Electrical / Semiconductors & Converters / Converters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

## Description

Average-value chopper

The Average-Value Chopper block represents a controlled
average-value chopper. Use the duty cycle input to convert the electrical energy between
the two sides. The figure shows the equivalent circuit for the block.

### Equations

The input current and output voltage depend on the chopper class that you
specify.

**Voltage and Current Equations**

| Chopper Class | Quadrants | Output Voltage, v2 | | | Input Current, i1 | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| i2<0 | i2=0 | i2>0 | i2<0 | i2=0 | i2>0 |
| **A** | 1st | v2=v1 | v2=DutyCycle⋅v1 | | i1=i2 | i1=DutyCycle⋅i2 | |
| **B** | 2nd | v2=(1−DutyCycle)⋅v1 | | v2=0 | i1=(1−DutyCycle)⋅i2 | | i1=0 |
| **C** | 1st and 2nd | v2=DutyCycle⋅v1 | | | i1=DutyCycle⋅i2 | | |
| **D** | 1st and 4th | v2=v1 | v2=(2⋅DutyCycle−1)⋅v1 | | i1=i2 | i1=(2⋅DutyCycle−1)⋅i2 | |
| **E** | Four | v2=(2⋅DutyCycle−1)⋅v1 | | | i1=(2⋅DutyCycle−1)⋅i2 | | |

### Limitations and Assumptions

- Input voltage, *v1* is
  positive.
- Power losses are neglected.
- The Average-Value Chopper block represents
  an ideal implementation of a controlled average-value chopper with no
  dynamics, and it is suitable for low fidelity simulations. For higher
  fidelity models, use the One-Quadrant Chopper, Two-Quadrant Chopper, or Four-Quadrant Chopper blocks.
