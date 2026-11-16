---
type: simulink-block
title: 'Exponential Current Source'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Sources'
documentation_page: 'exponentialcurrentsource'
documentation_source_path: 'ref/exponentialcurrentsource.html'
language: en
---

# Exponential Current Source

## Ports

### Conserving

### **+** — Positive voltage electrical

Electrical conserving port associated with the DC current source
positive voltage

### **-** — Negative voltage electrical

Electrical conserving port associated with the DC current source
negative voltage

## Parameters

### **Initial value, I1** — Output current initial value `0` `A` (default)

Value of the output current at time zero, in A.

### **Pulse value, I2** — Output current asymptotic value `0` `A` (default)

Asymptotic value of the output current when the output is high, in
A.

### **Rise delay time, TDR** — Rise delay time `0` `s` (default)

Rise time delay, in s.

### **Rise time, TR** — Rise time `1e-9` `s` (default) | positive scalar

Time it takes the output current to rise from the **Initial Value,
I1** value to the **Pulse Value, I2**
value.

### **Fall delay time, TDF** — Fall delay time `0` `s` (default)

Fall time delay. The default value is
`0``s`, which differs from the
SPICE default value.

### **Fall time, TF** — Fall time `1e-9` `s` (default) | positive scalar

Time it takes the output current to fall from the **Pulse value,
I2** value to the **Initial value, I1**
value.

### **Include parallel conductance, GMIN** — Whether to include parallel conductance `Yes` (default) | `No`

Specify if the current source includes a parallel conductance. The value of the parallel conductance, *GMIN*, depends on whether your model contains an Environment Parameters block.

This table shows the possible values of the parallel conductance,
*GMIN*:

**Values of parallel conductance, GMIN**

| Include parallel conductance, GMIN | | | | |
| --- | --- | --- | --- | --- |
| *`Yes`* | | *`No`* | | |
| **Model contains Environment Parameters block** | **Model does not contain Environment Parameters block** | Parallel conductance, *GMIN*, is not included and it does not affect the current source. | | |
| *GMIN* is equal to the value of the **GMIN** parameter in the Environment Parameters block. | *GMIN* = `1e-12` `Ohm` |

## Libraries

Simscape / Electrical / Additional Components / SPICE Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

## Description

Exponential pulse current source

The Exponential Current Source block represents a
current source whose output current value is an exponential pulse as a function of time
and is independent of the voltage across the terminals of the source. The following
equations describe the current through the source as a function of time:

Iout(0≤Time≤TDR))=I1Iout(TDR<Time≤TDF)=I1+(I2-I1)\*(1-e-(Time-TDR)/TR)Iout(TDF<Time)=I1+(I2-I1)\*(e-(Time-TDF)/TF-e-(Time-TDR)/TR)

where:

- *I1* is the **Initial value, I1**
  parameter value.
- *I2* is the **Pulse value, I2**
  parameter value.
- *TDR* is the **Rise delay time, TDR**
  parameter value.
- *TR* is the **Rise time, TR** parameter
  value.
- *TDF* is the **Fall delay time, TDF**
  parameter value.
- *TF* is the **Fall time, TF** parameter
  value.

The block uses a small conductance internally to prevent numerical simulation issues.
The conductance connects the **+** and **-** ports of
the device and has a conductance *GMIN*:

- By default, *GMIN* matches the **GMIN**
  parameter of the Environment Parameters
  block, whose default value is `1e–12`.
- To change *GMIN*, add an Environment
  Parameters block to your model and set the
  **GMIN** parameter to the desired value.
