---
type: simulink-block
title: 'Exponential Voltage Source'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Additional Components / SPICE Sources'
documentation_page: 'exponentialvoltagesource'
documentation_source_path: 'ref/exponentialvoltagesource.html'
language: en
---

# Exponential Voltage Source

## Ports

### Conserving

### **+** — Positive voltage electrical

Electrical conserving port associated with the DC current source
positive voltage

### **-** — Negative voltage electrical

Electrical conserving port associated with the DC current source
negative voltage

## Parameters

### **Initial value, V1** — Output voltage initial value `0` `V` (default)

Value of the output voltage at time zero, in V.

### **Pulse value, V2** — Output voltage asymptotic value `0` `V` (default)

Asymptotic value of the output voltage when the output is high, in
V.

### **Rise delay time, TDR** — Rise delay time `0` `s` (default)

Rise time delay, in s.

### **Rise time, TR** — Rise time `1e-9` `s` (default) | positive scalar

Time it takes the output current to rise from the **Initial Value,
V1** value to the **Pulse Value, V2**
value.

### **Fall delay time, TDF** — Fall delay time `0` `s` (default)

Fall time delay.

### **Fall time, TF** — Fall time `1e-9` `s` (default) | positive scalar

Time it takes the output current to fall from the **Pulse value,
V2** value to the **Initial value, V1**
value.

## Libraries

Simscape / Electrical / Additional Components / SPICE Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

## Description

Exponential pulse voltage source

The Exponential Voltage Source block represents a
voltage source whose output voltage value is an exponential pulse as a function of time
and is independent of the current through the source. The following equations describe
the output current as a function of time:

Vout(0≤Time≤TDR))=V1Vout(TDR<Time≤TDF)=V1+(V2-V1)\*(1-e-(Time-TDR)/TR)Vout(TDF<Time)=V1+(V2-V1)\*(e-(Time-TDF)/TF-e-(Time-TDR)/TR)

where:

- *V1* is the **Initial value, V1**
  parameter value.
- *V2* is the **Pulse value, V2**
  parameter value.
- *TDR* is the **Rise delay time, TDR**
  parameter value.
- *TR* is the **Rise time, TR** parameter
  value.
- *TDF* is the **Fall delay time, TDF**
  parameter value.
- *TF* is the **Fall time, TF** parameter
  value.
