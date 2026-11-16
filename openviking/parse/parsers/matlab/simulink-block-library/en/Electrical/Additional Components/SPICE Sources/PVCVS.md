---
type: simulink-block
title: 'PVCVS'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Sources'
documentation_page: 'pvcvs'
documentation_source_path: 'ref/pvcvs.html'
language: en
---

# PVCVS

## Ports

### Conserving

### **p1** — Positive voltage of the controlling input electrical

Electrical conserving port associated with the PVCVS positive voltage
of the controlling input.

### **n1** — Negative voltage of the controlling input electrical

Electrical conserving port associated with the PVCVS negative voltage
of the controlling input.

### **p2** — Positive output voltage electrical

Electrical conserving port associated with the PVCVS positive output
voltage.

### **n2** — Negative output voltage electrical

Electrical conserving port associated with the PVCVS negative output
voltage.

## Parameters

### **Polynomial coefficients** — Polynomial coefficients `[0, 1]` (default)

The polynomial coefficients that relate the input voltage to the output
voltage, as described in the preceding section.

## Libraries

Simscape / Electrical / Additional Components / SPICE Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

## Description

Polynomial voltage-controlled voltage source

The PVCVS (Polynomial Voltage-Controlled Voltage
Source) block represents a voltage source whose output voltage value is a polynomial
function of the voltage across the input ports. The following equations describe the
voltage across the source as a function of time:

- If you specify an *n*-element vector of polynomial
  coefficients for the **Polynomial coefficients** parameter:

  Vout=p(0)+p(1)\*Vin+...+p(n−1)\*Vinn−1+p(n)\*Vinn
- If you specify a scalar coefficient for the **Polynomial
  coefficients** parameter:

  Vout=p\*Vin

where:

- *Vin* is the voltage across the
  input ports.
- *p* is the **Polynomial coefficients**
  parameter value.
