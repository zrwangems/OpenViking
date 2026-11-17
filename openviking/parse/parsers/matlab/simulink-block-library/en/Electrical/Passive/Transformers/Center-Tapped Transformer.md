---
type: simulink-block
title: 'Center-Tapped Transformer'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / Transformers'
documentation_page: 'centertappedtransformer'
documentation_source_path: 'ref/centertappedtransformer.html'
language: en
---

# Center-Tapped Transformer

## Ports
```yaml
ports:
- name: 1+
  summary: Positive polarity of primary winding electrical
  direction: conserving
- name: 1-
  summary: Negative polarity of primary winding electrical
  direction: conserving
- name: 2+
  summary: Positive polarity of secondary winding electrical
  direction: conserving
- name: 2-
  summary: Negative polarity of secondary winding electrical
  direction: conserving
- name: c
  summary: Center tap of secondary winding electrical
  direction: conserving
```

### Conserving

### **1+** — Positive polarity of primary winding electrical

Electrical conserving port associated with the positive polarity of
the primary winding.

### **1-** — Negative polarity of primary winding electrical

Electrical conserving port associated with the negative polarity of
the primary winding.

### **2+** — Positive polarity of secondary winding electrical

Electrical conserving port associated with the positive polarity of
the secondary winding.

### **2-** — Negative polarity of secondary winding electrical

Electrical conserving port associated with the negative polarity of
the secondary winding.

### **c** — Center tap of secondary winding electrical

Electrical conserving port associated with the center tap of the
secondary winding.
## Parameters
```yaml
parameters:
- name: Modeling option
  summary: Option to model ideal or non-ideal center-tapped transformer Ideal (default) | Non-Ideal
  group: ''
- name: Winding ratio
  summary: Winding ratio of transformer 1 (default) | positive scalar
  group: ''
- name: Center tap position (0~1)
  summary: Location of center tap on secondary winding 0.5 (default) | scalar in the range (0, 1)
  group: ''
- name: Primary winding resistance
  summary: Series resistance of primary winding 0.01 Ohm (default) | positive scalar
  group: ''
- name: Primary leakage inductance
  summary: Leakage inductance of primary winding 0.0001 H (default) | positive scalar
  group: ''
- name: Secondary winding resistance
  summary: Series resistance of secondary winding 0.01 Ohm (default) | positive scalar
  group: ''
- name: Secondary leakage inductance
  summary: Leakage inductance of secondary winding 0.0001 H (default) | positive scalar
  group: ''
- name: Magnetization resistance
  summary: Magnetization resistance of transformer 100 Ohm (default) | positive scalar
  group: ''
- name: Magnetization inductance
  summary: Magnetization inductance of transformer 0.04 H (default) | positive scalar
  group: ''
```

### **Modeling option** — Option to model ideal or non-ideal center-tapped transformer `Ideal` (default) | `Non-Ideal`

Option to model an ideal or non-ideal center-tapped transformer. If you
set this parameter to `Non-Ideal`, the block also
models the winding, fundamental reluctance, and eddy current.

### **Winding ratio** — Winding ratio of transformer `1` (default) | positive scalar

Winding ratio of the transformer, which is equal to the ratio of the
number of primary coil turns to the number of secondary coil turns.

### **Center tap position (0~1)** — Location of center tap on secondary winding `0.5` (default) | scalar in the range (0, 1)

Location of the center tap on the secondary winding.

### **Primary winding resistance** — Series resistance of primary winding `0.01` `Ohm` (default) | positive scalar

Series resistance of the primary winding.

#### Dependencies

To enable this parameter, set **Modeling option** to
`Non-Ideal`.

### **Primary leakage inductance** — Leakage inductance of primary winding `0.0001` `H` (default) | positive scalar

Leakage inductance of the primary winding.

#### Dependencies

To enable this parameter, set **Modeling option** to
`Non-Ideal`.

### **Secondary winding resistance** — Series resistance of secondary winding `0.01` `Ohm` (default) | positive scalar

Series resistance of the secondary winding.

#### Dependencies

To enable this parameter, set **Modeling option** to
`Non-Ideal`.

### **Secondary leakage inductance** — Leakage inductance of secondary winding `0.0001` `H` (default) | positive scalar

Leakage inductance of the secondary winding.

#### Dependencies

To enable this parameter, set **Modeling option** to
`Non-Ideal`.

### **Magnetization resistance** — Magnetization resistance of transformer `100` `Ohm` (default) | positive scalar

Magnetization resistance of the transformer.

#### Dependencies

To enable this parameter, set **Modeling option** to
`Non-Ideal`.

### **Magnetization inductance** — Magnetization inductance of transformer `0.04` `H` (default) | positive scalar

Magnetization inductance of the transformer.

#### Dependencies

To enable this parameter, set **Modeling option** to
`Non-Ideal`.
## Libraries

Simscape / Electrical / Passive / Transformers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023b**

## Description

Single-phase center-tapped transformer

The Center-Tapped Transformer block implements a
center-tapped transformer. In switch-mode power supplies applications, you often use a
center-tapped transformer inside a full-wave rectifier, which needs the entire DC output
from the AC input.

The two electrical networks that connect to the primary and secondary windings of the
Center-Tapped Transformer block must each have their
own Electrical Reference block.
Normally, you also connect the center tap of the secondary winding to an Electrical
Reference block.

### Equations

This figure shows the equivalent circuit of the Center-Tapped
Transformer block when you set the **Modeling
option** parameter to `Ideal`:

This figure shows the equivalent circuit of the Center-Tapped
Transformer block when you set the **Modeling
option** parameter to `Non-Ideal`:

You must determine the relation between the electrical domain parameters from the
block mask and the magnetic domain parameters used in the equivalent circuit model:

- *n* is the value of the **Winding
  ratio** parameter.
- *L*1 is the value of the
  **Primary leakage inductance** parameter.
- *R*m is the value of the
  **Magnetization resistance** parameter.
- *L*m is the value of the
  **Magnetization inductance** parameter.
- *T* is the value of the **Center tap position
  (0~1)** parameter.
- *L*2 is the value of the
  **Secondary leakage inductance** parameter.
- *Rw*2 is the value of the
  **Secondary winding resistance** parameter.
- R1=n2L1 is the primary winding leakage reluctance.
- R=n2Lm is the shunt magnetizing resistance.
- Leddy=n2Rm is the conductance of the eddy current loop.
- R2=(1−T)2+T2L2 is the secondary winding leakage reluctance.
- Rw2p=Rw2(1−T) is the secondary top winding resistance.
- Rw2n=Rw2T is the secondary bottom winding resistance.
