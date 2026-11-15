---
type: simulink-block
title: 'Loop Filter'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'Phase-Locked Loops / Building Blocks'
documentation_page: 'loopfilter'
documentation_source_path: 'ref/loopfilter.html'
language: en
---

# Loop Filter

## Ports

### Input

### **in** — Input current scalar

Input current, specified as a scalar. In a phase-locked loop (PLL)
system, the **in** port is connected to the output of a
Charge Pump block, which provides the current value.

**Data Types:** `double`
### Output

### **out** — Output voltage scalar

Output voltage, specified as a scalar. In a PLL system, the
**out** port is connected to the input port of a
VCO block and provides the control voltage to VCO.

**Data Types:** `double`

## Parameters

### Configuration

### **Loop filter type** — Order of the loop filter `3rd Order passive` (default) | `2nd Order passive` | `4th Order passive`

Order of the loop filter. Simulates a second-, third-, or fourth-order
passive RC loop filter.

#### Programmatic Use

- Use `get_param(gcb,'FilterType')` to
  view the current order of **Loop filter
  type**.
- Use `set_param(gcb,'FilterType',value)`
  to set **Loop filter type** to a specific
  order.

### **C1 (F)** — Capacitance 1 `14.5661e-15` (default) | positive real scalar

Capacitor value C1, specified as a positive real scalar in
farads.

#### Programmatic Use

- Use `get_param(gcb,'C1')` to view the
  current value of **C1 (F)**.
- Use `set_param(gcb,'C1',value)` to set
  **C1 (F)** to a specific value.

**Data Types:** `double`

### **C2 (F)** — Capacitance 2 `160.276e-15` (default) | positive real scalar

Capacitor value C2, specified as a positive real scalar in
farads.

#### Programmatic Use

- Use `get_param(gcb,'C2')` to view the
  current value of **C2 (F)**.
- Use `set_param(gcb,'C2',value)` to set
  **C2 (F)** to a specific value.

**Data Types:** `double`

### **C3 (F)** — Capacitance 3 `1.0452e-15` (default) | positive real scalar

Capacitor value C3, specified as a positive real scalar in
farads.

#### Dependencies

To enable this parameter, select `3rd Order
passive` or `4th Order
passive` in **Loop filter
type**.

#### Programmatic Use

- Use `get_param(gcb,'C3')` to view the
  current value of **C3 (F)**.
- Use `set_param(gcb,'C3',value)` to set
  **C3 (F)** to a specific value.

**Data Types:** `double`

### **C4 (F)** — Capacitance 4 `1e-12` (default) | positive real scalar

Capacitor value C4, specified as a positive real scalar in
farads.

#### Dependencies

To enable this parameter, select `4th Order
passive` in **Loop filter
type**.

#### Programmatic Use

- Use `get_param(gcb,'C4')` to view the
  current value of **C4 (F)**.
- Use `set_param(gcb,'C4',value)` to set
  **C4 (F)** to a specific value.

**Data Types:** `double`

### **R2 (ohms)** — Resistance 2 `3.9955e6` (default) | positive real scalar

Resistor value R2, specified as a positive real scalar in ohms.

#### Programmatic Use

- Use `get_param(gcb,'R2')` to view the
  current value of **R2 (ohms)**.
- Use `set_param(gcb,'R2',value)` to set
  **R2 (ohms)** to a specific
  value.

**Data Types:** `double`

### **R3 (ohms)** — Resistance 3 `51.0435e6` (default) | positive real scalar

Resistor value R3, specified as a positive real scalar in ohms.

#### Dependencies

To enable this parameter, select `3rd Order
passive` or `4th Order
passive` in **Loop filter
type**.

#### Programmatic Use

- Use `get_param(gcb,'R3')` to view the
  current value of **R3 (ohms)**.
- Use `set_param(gcb,'R3',value)` to set
  **R3 (ohms)** to a specific
  value.

**Data Types:** `double`

### **R4 (ohms)** — Resistance 4 `12e3` (default) | positive real scalar

Resistor value R4, specified as a positive real scalar in ohms.

#### Dependencies

To enable this parameter, select `4th Order
passive` in **Loop filter
type**.

#### Programmatic Use

- Use `get_param(gcb,'R4')` to view the
  current value of **R4 (ohms)**.
- Use `set_param(gcb,'R4',value)` to set
  **R4 (ohms)** to a specific
  value.

**Data Types:** `double`

### **Enable increased buffer size** — Enable increased buffer size off (default) | on

Select to enable increased buffer size during simulation. This
increases the buffer size of the Convert Sample Time subsystem inside
the Loop Filter block. By default, this option is
deselected.

### **Buffer size** — Number of samples of the input buffering available during simulation `1000` (default) | positive integer scalar

Number of samples of the input buffering available during simulation,
specified as a positive integer scalar. This sets the buffer size of the
Convert Sample Time subsystem inside the Loop Filter
block.

Selecting different simulation solver or sampling strategies can
change the number of input samples needed to produce an accurate output
sample. Set the **Buffer size** to a large enough value
so that the input buffer contains all the input samples required.

#### Dependencies

This parameter is only available when **Enable increased
buffer size** option is selected in the
**Configuration** tab.

#### Programmatic Use

- Use `get_param(gcb,'NBuffer')` to view
  the current value of **Buffer
  size**.
- Use `set_param(gcb,'NBuffer',value)` to
  set **Buffer size** to a specific
  value.

**Data Types:** `double`

### Impairments

### **Enable impairments** — Add circuit impairments to simulation off (default) | on

Select to add circuit impairments to simulation. By default, this
option is disabled.

### **Operating temperature (℃)** — Temperature to determine the level of thermal noise `30` (default) | scalar

Temperature of the resistor, specified as a scalar in degree Celsius.
**Operating temperature (℃)** determines the level
of thermal (Johnson) noise.

#### Dependencies

To enable this parameter, select **Enable
impairments** in the **Impairments**
tab.

#### Programmatic Use

- Use `get_param(gcb,'Temperature')` to
  view the current value of **Operating temperature
  (℃)**.
- Use
  `set_param(gcb,'Temperature',value)` to
  set **Operating temperature (℃)** to a
  specific value.

**Data Types:** `double`

## Libraries

Mixed-Signal Blockset / PLL / Building Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Model second-, third-, or fourth-order passive loop filter

The Loop Filter subsystem block is a passive filter whose order can
vary from two to four. In a phase-locked loop (PLL) system, the subsystem filters the
output of Charge Pump
block and delivers the control voltage to a VCO block to
generate required frequency signal.

**nth Order Passive Loop Filter**
