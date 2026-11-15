---
type: simulink-block
title: 'PCCVS'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Additional Components / SPICE Sources'
documentation_page: 'pccvs'
documentation_source_path: 'ref/pccvs.html'
language: en
---

# PCCVS

## Ports

### Conserving

### **p1** — Positive voltage of the controlling input electrical

Electrical conserving port associated with the PCCVS positive voltage
of the controlling input.

### **n1** — Negative voltage of the controlling input electrical

Electrical conserving port associated with the PCCVS negative voltage
of the controlling input.

### **p2** — Positive output voltage electrical

Electrical conserving port associated with the PCCVS positive output
voltage.

### **n2** — Negative output voltage electrical

Electrical conserving port associated with the PCCVS negative output
voltage.

## Parameters

### **Polynomial coefficients** — Polynomial coefficients `[0, 1]` (default)

The polynomial coefficients that relate the input current to the output
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

Polynomial current-controlled voltage source

The PCCVS (Polynomial Current-Controlled Voltage
Source) block represents a voltage source whose output voltage value is a polynomial
function of the current through the input ports. The following equations describe the
voltage across the source as a function of time:

- If you specify an *n*-element vector of polynomial
  coefficients for the **Polynomial coefficients** parameter:

  Vout=p(0)+p(1)\*Iin+...+p(n−1)\*Iinn−1+p(n)\*Iinn
- If you specify a scalar coefficient for the **Polynomial
  coefficients** parameter:

  Vout=p\*Iin

where:

- *Iin* is the current through the
  input ports.
- *p* is the **Polynomial coefficients**
  parameter value.
