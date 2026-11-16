---
type: simulink-block
title: 'Charger'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'Cyclers'
documentation_page: 'charger'
documentation_source_path: 'ref/charger.html'
language: en
---

# Charger

## Ports

### Input

### **t** — Trigger, unitless physical signal

Physical signal input port that controls the charging behavior of the
block.
### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the positive terminal of
the charger.

### **-** — Negative terminal electrical

Electrical conserving port associated with the negative terminal of
the charger.

## Parameters

### **Constant charging current** — Constant charging current `5` `A` (default) | positive scalar

Value of the constant charging current at which the block charges a
battery.

### **Voltage threshold** — Voltage threshold for constant current charging `12` `V` (default) | positive scalar

Threshold at which the block stops performing a constant current charging
on the battery.

### **Constant charging voltage** — Constant charging voltage `12` `V` (default) | positive scalar

Value of the constant charging voltage at which the block charges a
battery.

### **Current threshold** — Current threshold for constant voltage charging `0.5` `A` (default) | positive scalar

Threshold at which the block stops performing a constant voltage charging
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

Ideal battery charger

The Charger block implements an ideal battery charger.
When the signal at the input port, **t**, changes from a value below
`0.5` to a value equal to or greater than `0.5`,
this block performs constant current charging at the value of the **Constant
charging current** parameter. When the voltage is greater than or equal to
the value of the **Voltage threshold** parameter, this block performs
constant voltage charging at the value of the **Constant charging
voltage** parameter until the current is less than or equal to the value of
the **Current threshold** parameter.

This figure shows the behavior of the Charger block
when the **t** input crosses `0.5`:
