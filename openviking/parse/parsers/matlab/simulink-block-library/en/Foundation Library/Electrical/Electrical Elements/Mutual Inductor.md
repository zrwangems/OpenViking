---
type: simulink-block
title: 'Mutual Inductor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Elements'
documentation_page: 'mutualinductor'
documentation_source_path: 'ref/mutualinductor.html'
language: en
---

# Mutual Inductor

## Ports
```yaml
ports:
- name: 1+
  summary: Primary winding positive terminal electrical
  direction: conserving
- name: 1-
  summary: Primary winding negative terminal electrical
  direction: conserving
- name: 2+
  summary: Secondary winding positive terminal electrical
  direction: conserving
- name: 2-
  summary: Secondary winding negative terminal electrical
  direction: conserving
```

### Conserving

### **1+** — Primary winding positive terminal electrical

Electrical conserving port associated with the positive terminal of the primary
winding.

### **1-** — Primary winding negative terminal electrical

Electrical conserving port associated with the negative terminal of the primary
winding.

### **2+** — Secondary winding positive terminal electrical

Electrical conserving port associated with the positive terminal of the secondary
winding.

### **2-** — Secondary winding negative terminal electrical

Electrical conserving port associated with the negative terminal of the secondary
winding.
## Parameters
```yaml
parameters:
- name: Inductance L1
  summary: Self-inductance of primary winding 10 H (default) | positive scalar
  group: ''
- name: Inductance L2
  summary: Self-inductance of secondary winding 0.1 H (default) | positive scalar
  group: ''
- name: Perfect coupling – no leakage
  summary: Use ideal mutual inductor Off (default) | On
  group: ''
- name: Coefficient of coupling
  summary: Coefficient of coupling for mutual inductance 0.9 (default) | scalar in the range (0,1)
  group: ''
```

### **Inductance L1** — Self-inductance of primary winding `10 H` (default) | positive scalar

Self-inductance of the primary winding.

### **Inductance L2** — Self-inductance of secondary winding `0.1 H` (default) | positive scalar

Self-inductance of the secondary winding.

### **Perfect coupling – no leakage** — Use ideal mutual inductor `Off` (default) | `On`

If you select this checkbox, the block sets the coefficient of coupling to 1 and
the leakage reluctances to 0. In this case, the block represents the ideal mutual
inductor with no leakages and no fast pole, while also retaining the correct
low-frequency behavior, blocking DC.

### **Coefficient of coupling** — Coefficient of coupling for mutual inductance `0.9` (default) | scalar in the range (0,1)

Coefficient of coupling, which defines the mutual inductance. The parameter value
should be greater than zero and less than 1. Avoid setting this parameter to values
close to 1 (such as 0.9999) because that can introduce fast simulation dynamics.

#### Dependencies

To enable this parameter, clear the **Perfect coupling – no
leakage** check box.
## Libraries

Simscape / Foundation Library / Electrical / Electrical Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

## Description

Mutual inductor in electrical systems

The Mutual Inductor block models a mutual inductor,
described with the following equations:

V1=L1dI1dt+MdI2dt

V2=L2dI2dt+MdI1dt

M=kL1·L2

where:

- *V1* is the voltage across the primary winding.
- *V2* is the voltage across the secondary winding.
- *I1* is the current flowing into the **+** terminal
  of the primary winding.
- *I2* is the current flowing out of the **+**
  terminal of the secondary winding.
- *L1*, *L2* are the winding self-inductances.
- *M* is the mutual inductance.
- *k* is the coefficient of coupling, 0 < *k* <
  1.
- *t* is time.

The two electrical networks connected to the primary and secondary windings must each have
their own Electrical Reference block.

Use this block to represent an AC transformer. If inductance and mutual inductance terms
are not important in a model, or are unknown, you can use the Ideal
Transformer block instead.

Simscape™ and Simscape
Electrical™ libraries include several blocks than can model the same type of transformer
device. However, these blocks make different modeling assumptions. To choose the right block
for your application, you must understand how these assumptions impact the block behavior as a
function of frequency. For more information, see Choose Blocks to Model Transformers (Simscape Electrical).

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
