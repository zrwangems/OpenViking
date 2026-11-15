---
type: simulink-block
title: 'PVCCS'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Additional Components / SPICE Sources'
documentation_page: 'pvccs'
documentation_source_path: 'ref/pvccs.html'
language: en
---

# PVCCS

## Ports

### Conserving

### **p1** — Positive voltage of the controlling input electrical

Electrical conserving port associated with the PVCCS positive voltage
of the controlling input.

### **n1** — Negative voltage of the controlling input electrical

Electrical conserving port associated with the PVCCS negative voltage
of the controlling input.

### **p2** — Positive output voltage electrical

Electrical conserving port associated with the PVCCS positive output
voltage.

### **n2** — Negative output voltage electrical

Electrical conserving port associated with the PVCCS negative output
voltage.

## Parameters

### **Polynomial coefficients** — Polynomial coefficients `[0, 1]` (default)

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

**Introduced in R2008a**

## Description

Polynomial voltage-controlled current source

The PVCCS (Polynomial Voltage-Controlled Current
Source) block represents a current source whose output current value is a polynomial
function of the voltage across the input ports. The following equations describe the
current through the source as a function of time:

- If you specify an *n*-element vector of polynomial
  coefficients for the **Polynomial coefficients** parameter:

  Iout=p(0)+p(1)\*Vin+...+p(n−1)\*Vinn−1+p(n)\*Vinn
- If you specify a scalar coefficient for the **Polynomial
  coefficients** parameter:

  Iout=p\*Vin

where:

- *Vin* is the voltage across the
  input ports.
- *p* is the **Polynomial coefficients**
  parameter value.

The block uses a small conductance internally to prevent numerical simulation issues.
The conductance connects the output ports of the device and has a conductance
*GMIN*:

- By default, *GMIN* matches the **GMIN**
  parameter of the Environment Parameters
  block, whose default value is `1e–12`.
- To change *GMIN*, add an Environment
  Parameters to your model and set the
  **GMIN** parameter to the desired value.
