---
type: simulink-block
title: 'Discharger'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Battery Management System / C\u200byclers'
documentation_page: 'discharger'
documentation_source_path: 'ref/discharger.html'
language: en
---

# Discharger

## Ports

### Input

### **t** — Trigger, unitless physical signal

Physical signal input port that controls the discharging behavior of
the block.
### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the positive terminal of
the discharger.

### **-** — Negative terminal electrical

Electrical conserving port associated with the negative terminal of
the discharger.

## Parameters

### **Constant discharging current** — Constant discharging current `5` `A` (default) | positive scalar

Value of the constant discharging current at which the block discharges a
battery.

### **Voltage threshold** — Voltage threshold for constant discharging current `10` `V` (default) | positive scalar

Threshold at which the block stops performing constant current discharging
on the battery.

## Libraries

Simscape / Battery / Cyclers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

## Description

Ideal battery discharger

This block implements an ideal discharger. When the signal at the input port,
**t**, changes from a value below `0.5` to a value
equal to or greater than `0.5`, the block performs constant current
discharging at the value of the **Constant discharging current**
parameter until the voltage is less than or equal to the value of the **Voltage
threshold** parameter.

This figure shows the behavior of the Discharger block
when the **t** input crosses `0.5`:
