---
type: simulink-block
title: 'Heat Flow Rate Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Thermal Models / Thermal Sources'
documentation_page: 'heatflowratesource'
documentation_source_path: 'ref/heatflowratesource.html'
language: en
---

# Heat Flow Rate Source

## Ports

### Conserving

### **A** — Source inlet thermal

Thermal conserving port associated with the source inlet.

### **B** — Source outlet thermal

Thermal conserving port associated with the source outlet.

## Parameters

### **Heat flow rate** — Heat flow rate through the source 0 W (default)

Constant Heat flow rate through the source. Positive heat flow rate flows
from port A to port B.

## Libraries

Simscape / Foundation Library / Thermal / Thermal Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Constant source of thermal energy, characterized by heat flow

The Heat Flow Rate Source block represents an ideal source of thermal
energy that is powerful enough to maintain specified heat flow at its outlet regardless
of the temperature difference across the source.

The source generates constant heat flow rate, defined by the **Heat flow
rate** parameter value.
