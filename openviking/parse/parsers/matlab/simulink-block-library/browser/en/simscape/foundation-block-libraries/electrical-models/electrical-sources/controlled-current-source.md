---
type: simulink-block
title: 'Controlled Current Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Electrical Models / Electrical Sources'
documentation_page: 'controlledcurrentsource'
documentation_source_path: 'ref/controlledcurrentsource.html'
language: en
---

# Controlled Current Source

## Ports

### Input

### **iT** — Current control signal, A physical signal

Input physical signal that specifies the current value.

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

Ideal current source driven by input signal

The Controlled Current Source block represents an ideal
current source that is powerful enough to maintain the specified current through it regardless
of the voltage across the source.

The output current is *I = Is*, where *Is* is the
numerical value presented at the physical signal port.

The positive direction of the current flow is indicated by the arrow.
