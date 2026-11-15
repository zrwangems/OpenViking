---
type: simulink-block
title: 'PVCVS2'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Additional Components / SPICE Sources'
documentation_page: 'pvcvs2'
documentation_source_path: 'ref/pvcvs2.html'
language: en
---

# PVCVS2

## Ports

### Conserving

### **1+** — Positive input voltage of the first controlling input electrical

Electrical conserving port associated with the PVCVS2 positive input
voltage of the first controlling input.

### **1-** — Negative input voltage of the first controlling input electrical

Electrical conserving port associated with the PVCVS2 negative input
voltage of the first controlling input.

### **2+** — Positive input voltage of the second controlling input electrical

Electrical conserving port associated with the PVCVS2 positive input
voltage of the second controlling input.

### **2-** — Negative input voltage of the second controlling input electrical

Electrical conserving port associated with the PVCVS2 negative input
voltage of the second controlling input.

### **+** — Positive output voltage electrical

Electrical conserving port associated with the PVCVS2 positive output
voltage.

### **-** — Negative output voltage electrical

Electrical conserving port associated with the PVCVS2 negative output
voltage.

## Parameters

### **Polynomial coefficients** — Polynomial coefficients `[ 0 1 1 ]` (default)

The polynomial coefficients that relate the input voltage to the output
voltage, as described in the preceding section.

## Libraries

Simscape / Electrical / Additional Components / SPICE Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2009a**

## Description

Polynomial voltage-controlled voltage source with two controlling inputs

The PVCVS2 (Two-Input Polynomial Voltage-Controlled
Voltage Source) block represents a voltage source whose output voltage value is a
polynomial function of the voltages across the pairs of controlling input ports. This
equation describes the voltage across the source as a function of time:

Vout=p1+p2\*Vin1+p3\*Vin2+p4\*Vin12+p5Vin1\*Vin2+p6\*Vin22+…

where:

- *Vin1* is the voltage across the
  first pair of input ports.
- *Vin2* is the voltage across the
  second pair of input ports.
- *p* is the **Polynomial coefficients**
  parameter value.
