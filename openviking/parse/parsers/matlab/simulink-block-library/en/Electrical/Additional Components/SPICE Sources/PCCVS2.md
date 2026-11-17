---
type: simulink-block
title: 'PCCVS2'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Sources'
documentation_page: 'pccvs2'
documentation_source_path: 'ref/pccvs2.html'
language: en
---

# PCCVS2

## Ports
```yaml
ports:
- name: 1+
  summary: Positive voltage of the first controlling input electrical
  direction: conserving
- name: 1-
  summary: Negative voltage of the first controlling input electrical
  direction: conserving
- name: 2+
  summary: Positive voltage of the second controlling input electrical
  direction: conserving
- name: 2-
  summary: Negative voltage of the second controlling input electrical
  direction: conserving
- name: +
  summary: Positive output voltage electrical
  direction: conserving
- name: '-'
  summary: Negative output voltage electrical
  direction: conserving
```

### Conserving

### **1+** — Positive voltage of the first controlling input electrical

Electrical conserving port associated with the PCCVS2 positive voltage
of the first controlling input.

### **1-** — Negative voltage of the first controlling input electrical

Electrical conserving port associated with the PCCVS2 negative voltage
of the first controlling input.

### **2+** — Positive voltage of the second controlling input electrical

Electrical conserving port associated with the PCCVS2 positive voltage
of the second controlling input.

### **2-** — Negative voltage of the second controlling input electrical

Electrical conserving port associated with the PCCVS2 negative voltage
of the second controlling input.

### **+** — Positive output voltage electrical

Electrical conserving port associated with the PCCVS2 positive output
voltage.

### **-** — Negative output voltage electrical

Electrical conserving port associated with the PCCVS2 negative output
voltage.
## Parameters
```yaml
parameters:
- name: Polynomial coefficients
  summary: Polynomial coefficients [ 0 1 1 ] (default)
  group: ''
```

### **Polynomial coefficients** — Polynomial coefficients `[ 0 1 1 ]` (default)

The polynomial coefficients that relate the input current to the output
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

Polynomial current-controlled voltage source with two controlling inputs

The PCCVS2 (Two-Input Polynomial Current-Controlled
Voltage Source) block represents a voltage source whose output voltage value is a
polynomial function of the currents through the pairs of controlling input ports. This
equation describes the voltage across the source as a function of time:

Vout=p1+p2\*Iin1+p3\*Iin2+p4\*Iin12+p5Iin1\*Iin2+p6\*Iin22+…

where:

- *Iin1* is the current through the
  first pair of input ports.
- *Iin2* is the current through the
  second pair of input ports.
- *p* is the **Polynomial coefficients**
  parameter value.
