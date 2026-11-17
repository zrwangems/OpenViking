---
type: simulink-block
title: 'PCCCS'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Sources'
documentation_page: 'pcccs'
documentation_source_path: 'ref/pcccs.html'
language: en
---

# PCCCS

## Ports
```yaml
ports:
- name: p1
  summary: Positive voltage of the controlling input electrical
  direction: conserving
- name: n1
  summary: Negative voltage of the controlling input electrical
  direction: conserving
- name: p2
  summary: Positive output voltage electrical
  direction: conserving
- name: n2
  summary: Negative output voltage electrical
  direction: conserving
```

### Conserving

### **p1** — Positive voltage of the controlling input electrical

Electrical conserving port associated with the PCCCS positive voltage
of the controlling input.

### **n1** — Negative voltage of the controlling input electrical

Electrical conserving port associated with the PCCCS negative voltage
of the controlling input.

### **p2** — Positive output voltage electrical

Electrical conserving port associated with the PCCCS positive output
voltage.

### **n2** — Negative output voltage electrical

Electrical conserving port associated with the PCCCS negative output
voltage.
## Parameters
```yaml
parameters:
- name: Polynomial coefficients
  summary: Polynomial coefficients [0, 1] (default)
  group: ''
- name: Include parallel conductance, GMIN
  summary: Whether to include parallel conductance Yes (default) | No
  group: ''
```

### **Polynomial coefficients** — Polynomial coefficients `[0, 1]` (default)

Polynomial coefficients that relate the input current to the output
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

Polynomial current-controlled current source

The PCCCS (Polynomial Current-Controlled Current
Source) block represents a current source whose output current value is a polynomial
function of the current through the input ports. The following equations describe the
current through the source as a function of time:

- If you specify an *n*-element vector of polynomial
  coefficients for the **Polynomial coefficients** parameter:

  Iout=p(0)+p(1)\*Iin+...+p(n−1)\*Iinn−1+p(n)\*Iinn
- If you specify a scalar coefficient for the **Polynomial
  coefficients** parameter:

  Iout=p\*Iin

where:

- *Iin* is the current through the
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
  Parameters block to your model and set the
  **GMIN** parameter to the desired value.
