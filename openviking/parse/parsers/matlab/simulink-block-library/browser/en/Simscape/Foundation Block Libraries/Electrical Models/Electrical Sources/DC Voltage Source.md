---
type: simulink-block
title: 'DC Voltage Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Electrical Models / Electrical Sources'
documentation_page: 'dcvoltagesource'
documentation_source_path: 'ref/dcvoltagesource.html'
language: en
---

# DC Voltage Source

## Ports

### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the source positive terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the source negative terminal.

## Parameters

### **Constant voltage** — Output voltage `1 V` (default) | scalar

Voltage across the source. You can specify positive or negative values.

## Libraries

Simscape / Foundation Library / Electrical / Electrical Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

## Description

Ideal constant voltage source

The DC Voltage Source block represents an ideal voltage source that is
powerful enough to maintain specified voltage across its terminals regardless of the current
flowing through the source.

You specify the output voltage by using the **Constant voltage**
parameter, which can be positive or negative.

Connections **+** and **-** are conserving electrical
ports corresponding to the positive and negative terminals of the voltage source,
respectively. The current is positive if it flows from positive to negative, and the voltage
across the source is equal to the difference between the voltage at the positive and the
negative terminal, *V*(+) – *V*(-).
