---
type: simulink-block
title: 'Lock Time Measurement'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'PLL / Measurements & Testbenches'
documentation_page: 'locktimemeasurement'
documentation_source_path: 'ref/locktimemeasurement.html'
language: en
---

# Lock Time Measurement

## Ports

### Input

### **pll out** — Input clock signal scalar

Input clock signal to the Lock Time Measurement block, specified as
a scalar. The **pll out** port is connected to the output of a PLL
system.

**Data Types:** `double`
### Output

### **lock time** — Time required to achieve lock in PLL real positive scalar

Time at which locking takes place in a PLL system, returned as a real positive
scalar in seconds.

**Data Types:** `double`

## Parameters

### **Target frequency (Hz)** — Target operating frequency of PLL to measure lock time `2.1e9` (default) | real positive scalar

Target operating frequency of the PLL device under test (DUT) to measure the lock
time of the PLL, specified as a real positive scalar in Hz.

#### Programmatic Use

- Use `get_param(gcb,'TargetFreq')` to view the current value
  of **Target frequency**.
- Use `set_param(gcb,'TargetFreq',value)` to set
  **Target frequency** to a specific value.

### **Error tolerance (Hz)** — Error tolerance for lock time measurement `1e5` (default) | real positive scalar

Error tolerance for lock time measurement, specified as a real positive scalar in
Hz.

#### Programmatic Use

- Use `get_param(gcb,'FreqErrorTol')` to view the current
  value of **Error tolerance**.
- Use `set_param(gcb,'FreqErrorTol',value)` to set
  **Error tolerance** to a specific value.

## Libraries

Mixed-Signal Blockset / PLL / Measurements & Testbenches

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Measure time a PLL takes to reach target frequency within given tolerance

The Lock Time Measurement block measures the lock time of a phase-locked
loop (PLL) system. Lock time is the time required by the PLL to reach the target frequency
within the given error tolerance.
