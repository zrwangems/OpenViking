---
type: simulink-block
title: 'DC Current Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Electrical Models / Electrical Sources'
documentation_page: 'dccurrentsource'
documentation_source_path: 'ref/dccurrentsource.html'
language: en
---

# DC Current Source

## Ports

### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the source positive terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the source negative terminal.

## Parameters

### **Constant current** — Output current `1 A` (default) | scalar

Current through the source. You can specify positive or negative values.

## Libraries

Simscape / Foundation Library / Electrical / Electrical Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

## Description

Ideal constant current source

The DC Current Source block represents an ideal current
source that is powerful enough to maintain specified current through it regardless of the
voltage across the source.

You specify the output current by using the **Constant current**
parameter, which can be positive or negative.

The positive direction of the current flow is indicated by the arrow.
