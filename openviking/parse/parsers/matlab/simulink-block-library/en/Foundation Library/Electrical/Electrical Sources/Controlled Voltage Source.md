---
type: simulink-block
title: 'Controlled Voltage Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Sources'
documentation_page: 'controlledvoltagesource'
documentation_source_path: 'ref/controlledvoltagesource.html'
language: en
---

# Controlled Voltage Source

## Ports

### Input

### **vT** — Voltage control signal, V physical signal

Input physical signal that specifies the voltage value.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.
### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the source positive terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the source negative terminal.

## Parameters

Not documented in R2025b.

## Libraries

Simscape / Foundation Library / Electrical / Electrical Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

## Description

Ideal voltage source driven by input signal

The Controlled Voltage Source block represents an ideal
voltage source that is powerful enough to maintain the specified voltage across its terminals
regardless of the current flowing through the source.

The output voltage is *V = Vs*, where *Vs* is the
numerical value presented at the physical signal port.
