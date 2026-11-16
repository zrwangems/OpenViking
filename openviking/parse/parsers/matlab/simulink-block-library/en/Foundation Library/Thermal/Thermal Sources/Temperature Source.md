---
type: simulink-block
title: 'Temperature Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal / Thermal Sources'
documentation_page: 'temperaturesource'
documentation_source_path: 'ref/temperaturesource.html'
language: en
---

# Temperature Source

## Ports

### Conserving

### **A** — Source outlet thermal

Thermal conserving port associated with the source outlet.

## Parameters

### **Temperature** — Absolute temperature at source outlet 293.15 K (default)

Constant absolute temperature at the source outlet port.

## Libraries

Simscape / Foundation Library / Thermal / Thermal Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Constant source of thermal energy, characterized by temperature

The Temperature Source block represents an ideal source of thermal
energy that is powerful enough to maintain specified temperature at its outlet
regardless of the heat flow consumed by the system.

The source generates constant absolute temperature, defined by the
**Temperature** parameter value.
