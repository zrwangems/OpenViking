---
type: simulink-block
title: 'Negative Supply Rail'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Sources'
documentation_page: 'negativesupplyrail'
documentation_source_path: 'ref/negativesupplyrail.html'
language: en
---

# Negative Supply Rail

## Ports

### Conserving

### **-** — Negative voltage electrical

Electrical conserving port associated to the negative supply rail
negative voltage.

## Parameters

### **Constant voltage** — Constant output voltage `-1` `V` (default)

The voltage at the output port relative to the Electrical
Reference block ground port.

## Libraries

Simscape / Electrical / Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

## Description

Ideal negative supply rail

The Negative Supply Rail block represents an ideal
negative supply rail. Use this block instead of the Simscape™
DC Voltage Source block to define the output voltage
relative to the Simscape
Electrical Reference block that must appear in each
model.

**Note**

Do not attach more than one Negative Supply Rail
block to any connected line.
