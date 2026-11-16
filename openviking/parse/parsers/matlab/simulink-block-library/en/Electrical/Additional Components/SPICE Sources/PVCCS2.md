---
type: simulink-block
title: 'PVCCS2'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Sources'
documentation_page: 'pvccs2'
documentation_source_path: 'ref/pvccs2.html'
language: en
---

# PVCCS2

## Ports

### Conserving

### **1+** — Positive voltage of the first controlling input electrical

Electrical conserving port associated with the PVCCS2 positive voltage
of the first controlling input.

### **1-** — Negative voltage of the first controlling input electrical

Electrical conserving port associated with the PVCCS2 negative voltage
of the first controlling input.

### **2+** — Positive voltage of the second controlling input electrical

Electrical conserving port associated with the PVCCS2 positive voltage
of the second controlling input.

### **2-** — Negative voltage of the second controlling input electrical

Electrical conserving port associated with the PVCCS2 negative voltage
of the second controlling input.

### **+** — Positive output voltage electrical

Electrical conserving port associated with the PVCCS2 positive output
voltage.

### **-** — Negative output voltage electrical

Electrical conserving port associated with the PVCCS2 negative output
voltage.

## Parameters

### **Polynomial coefficients** — Polynomial coefficients `[ 0 1 1 ]` (default)

The polynomial coefficients that relate the input voltage to the output
current, as described in the preceding section.

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

**Introduced in R2009a**

## Description

Polynomial voltage-controlled current source with two controlling inputs

The PVCCS2 (Two-Input Polynomial Voltage-Controlled
Current Source) block represents a current source whose output current value is a
polynomial function of the voltages across the pairs of controlling input ports. This
equation describes the current through the source as a function of time:

Iout=p1+p2\*Vin1+p3\*Vin2+p4\*Vin12+p5Vin1\*Vin2+p6\*Vin22+…

where:

- *Vin1* is the voltage across the
  first pair of input ports.
- *Vin2* is the voltage across the
  second pair of input ports.
- *p* is the **Polynomial coefficients**
  parameter value.

The block uses a small conductance internally to prevent numerical simulation issues.
The conductance connects the output ports of the device and has a conductance
*GMIN*:

- By default, *GMIN* matches the **GMIN**
  parameter of the Environment Parameters
  block, whose default value is `1e–12`.
- To change *GMIN*, add an Environment
  Parameters block to your model and set the
  **GMIN** parameter to the desired value.
