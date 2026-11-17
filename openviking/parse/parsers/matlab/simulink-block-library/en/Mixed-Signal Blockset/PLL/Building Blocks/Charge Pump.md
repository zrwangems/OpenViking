---
type: simulink-block
title: 'Charge Pump'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'PLL / Building Blocks'
documentation_page: 'chargepump'
documentation_source_path: 'ref/chargepump.html'
language: en
---

# Charge Pump

## Ports
```yaml
ports:
- name: up
  summary: Input port scalar
  direction: input
  data_types: double
- name: down
  summary: Input port scalar
  direction: input
  data_types: double
- name: out
  summary: Output port scalar
  direction: output
  data_types: double
```

### Input

### **up** — Input port scalar

Input port, connected to the **up** output of a
PFD in a PLL system.

**Data Types:** `double`

### **down** — Input port scalar

Input port, connected to the **down** output of
PFD in a PLL system.

**Data Types:** `double`
### Output

### **out** — Output port scalar

Output port, connected to the Loop
Filter block in a PLL system. **out**
delivers current proportional to the difference in duty cycles between
**up** and **down** input
ports.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Output current (A)
  summary: Design output current 1e-3 (default) | positive real scalar
  group: Configuration
- name: Input threshold (V)
  summary: Logic switching threshold at input ports 0.5 (default) | real scalar
  group: Configuration
- name: Enable increased buffer size
  summary: Enable increased buffer size off (default) | on
  group: Configuration
- name: Buffer size
  summary: Number of samples of the input buffering available during simulation 10 (default) | positive integer scalar
  group: Configuration
- name: Enable current impairments
  summary: Add current impairments to simulation on (default) | off
  group: Impairments
- name: Current imbalance (A)
  summary: Difference between full scale positive and negative current 1e-7 (default) | positive real scalar
  group: Impairments
- name: Leakage current (A)
  summary: Output current without any input 1e-8 (default) | nonnegative real scalar
  group: Impairments
- name: Enable timing impairments
  summary: Add timing impairments to simulation on (default) | off
  group: Impairments
- name: Output step size calculation
  summary: Determine how output step size is calculated Default (default) | Advanced
  group: Impairments
- name: Maximum frequency of interest (Hz)
  summary: Maximum frequency of interest at output 10e9 (default) | positive real scalar
  group: Impairments
- name: Rise/fall time (s)
  summary: 20%-80% rise/fall time for up input port 5e-9 (default) | positive real scalar
  group: Impairments
- name: Up propagation delay
  summary: Total propagation delay for up input port 6e-9 (default) | positive real scalar
  group: Impairments
- name: Rise/fall time
  summary: 20%-80% rise/fall time for down input port 2e-9 (default) | positive real scalar
  group: Impairments
- name: Down propagation delay
  summary: Total propagation delay for down input port 4e-9 (default) | positive real scalar
  group: Impairments
```

### Configuration

### **Output current (A)** — Design output current `1e-3` (default) | positive real scalar

Full scale magnitude of design output current, specified as a
positive real scalar in amperes. This parameter is tunable.

#### Programmatic Use

- Use `get_param(gcb,'OutputCurrent')` to
  view the current value of **Output current
  (A)**.
- Use
  `set_param(gcb,'OutputCurrent',value)` to
  set **Output current (A)** to a specific
  value.

### **Input threshold (V)** — Logic switching threshold at input ports `0.5` (default) | real scalar

Logic switching threshold at input ports, specified as a real scalar
in volts.

#### Programmatic Use

- Use `get_param(gcb,'InputThreshold')`
  to view the current value of **Input threshold
  (V)**.
- Use
  `set_param(gcb,'InputThreshold',value)`
  to set **Input threshold (V)** to a
  specific value.

### **Enable increased buffer size** — Enable increased buffer size off (default) | on

Select to enable increased buffer size during simulation. This
increases the buffer size of the Logic Decision and Slew
Rate inside the Charge Pump block. By
default, this option is deselected.

### **Buffer size** — Number of samples of the input buffering available during simulation `10` (default) | positive integer scalar

Number of samples of the input buffering available during simulation,
specified as a positive integer scalar. This sets the buffer size of the
Logic Decision and Slew
Rate inside the Charge Pump block.

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

### Impairments

### **Enable current impairments** — Add current impairments to simulation on (default) | off

Select to add current impairments such as current imbalance and
leakage current to simulation. By default, this option is
selected.

### **Current imbalance (A)** — Difference between full scale positive and negative current `1e-7` (default) | positive real scalar

Difference between full scale positive and negative current, specified
as a positive real scalar in amperes.

#### Dependencies

To enable this parameter, select **Enable current
impairments** in the **Impairments**
tab.

#### Programmatic Use

- Use `get_param(gcb,'CurrentImbalance')`
  to view the current value of **Current imbalance
  (A)**.
- Use
  `set_param(gcb,'CurrentImbalance',value)`
  to set **Current imbalance (A)** to a
  specific value.

**Data Types:** `double`

### **Leakage current (A)** — Output current without any input `1e-8` (default) | nonnegative real scalar

Output current when both inputs are at logic zero, specified as a
nonnegative real scalar in amperes.

#### Dependencies

To enable this parameter, select **Enable current
impairments** in the **Impairments**
tab.

#### Programmatic Use

- Use `get_param(gcb,'LeakageCurrent')`
  to view the current value of **Leakage current
  (A)**.
- Use
  `set_param(gcb,'LeakageCurrent',value)`
  to set **Leakage current (A)** to a
  specific value.

**Data Types:** `double`

### **Enable timing impairments** — Add timing impairments to simulation on (default) | off

Select to add timing impairments such as rise/fall time and
propagation delay to simulation. By default, this option is
selected.

### **Output step size calculation** — Determine how output step size is calculated `Default` (default) | `Advanced`

Determine how output step size is calculated:

- Select `Default` to calculate output step
  size from rise/fall time. Output step size (ΔT) is given by ΔT=(Rise/fall time)26 · 0.22.
- Select `Advanced` to calculate output step
  size from maximum frequency of interest. Output step size (ΔT)
  is given by ΔT=Rise/fall time6 · Maximum frequency of interest.

#### Dependencies

To enable this parameter, select **Enable timing
impairments** in the **Impairments**
tab.

### **Maximum frequency of interest (Hz)** — Maximum frequency of interest at output `10e9` (default) | positive real scalar

Maximum frequency of interest at the output, specified as a positive
real scalar in Hz.

#### Dependencies

To enable this parameter, select **Enable timing
impairments** in the **Impairments**
tab and choose **Advanced** for **Output
step size calculation**.

#### Programmatic Use

- Use `get_param(gcb,'MaxFreqInterest')`
  to view the current value of **Maximum frequency of
  interest (Hz)**.
- Use
  `set_param(gcb,'MaxFreqInterest',value)`
  to set **Maximum frequency of interest
  (Hz)** to a specific value.

**Data Types:** `double`

#### up

### **Rise/fall time (s)** — 20%-80% rise/fall time for up input port `5e-9` (default) | positive real scalar

20%-80% rise/fall time for **up** input port,
specified as a positive real scalar in seconds.

#### Dependencies

To enable this parameter, select **Enable timing
Impairments** in the **Impairments**
tab.

#### Programmatic Use

- Use `get_param(gcb,'RiseFallUp')` to
  view the current value of **up Rise/fall
  time**.
- Use `set_param(gcb,'RiseFallUp',value)`
  to set **up Rise/fall time** to a specific
  value.

### **Up propagation delay** — Total propagation delay for up input port `6e-9` (default) | positive real scalar

Total propagation delay for **up** input port,
specified as a positive real scalar in seconds.

#### Dependencies

To enable this parameter, select **Enable
Impairments** in the **Impairments**
tab.

#### Programmatic Use

- Use `get_param(gcb,'PropDelayUp')` to
  view the current value of **Up propagation
  delay**.
- Use
  `set_param(gcb,'PropDelayUp',value)` to
  set **Up propagation delay** to a specific
  value.

#### down

### **Rise/fall time** — 20%-80% rise/fall time for down input port `2e-9` (default) | positive real scalar

20%-80% rise/fall time for **down** input port,
specified as a positive real scalar in seconds.

#### Dependencies

To enable this parameter, select **Enable
Impairments** in the **Impairments**
tab.

#### Programmatic Use

- Use `get_param(gcb,'RiseFallDown')` to
  view the current value of **down Rise/fall
  time**.
- Use
  `set_param(gcb,'RiseFallDown',value)` to
  set **down Rise/fall time** to a specific
  value.

### **Down propagation delay** — Total propagation delay for down input port `4e-9` (default) | positive real scalar

Total propagation delay for **down** input port,
specified as a positive real scalar in seconds.

#### Dependencies

To enable this parameter, select **Enable
Impairments** in the **Impairments**
tab.

#### Programmatic Use

- Use `get_param(gcb,'PropDelayDown')` to
  view the current value of **Down propagation
  delay**.
- Use
  `set_param(gcb,'PropDelayDown',value)` to
  set **Down propagation delay** to a
  specific value.
## Libraries

Mixed-Signal Blockset / PLL / Building Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Output a current proportional to the difference in duty cycle between two input ports

The Charge Pump block produces an output current which is proportional
to the difference in duty cycles between the signals at its **up** and
**down** input ports. In a phase-locked loop (PLL) system, the
Charge Pump block converts the phase error as represented by the two
outputs of the PFD block
into a single current at the input to the Loop
Filter.
