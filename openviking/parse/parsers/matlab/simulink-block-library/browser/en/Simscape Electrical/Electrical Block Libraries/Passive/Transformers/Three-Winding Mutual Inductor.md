---
type: simulink-block
title: 'Three-Winding Mutual Inductor'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Passive / Transformers'
documentation_page: 'threewindingmutualinductor'
documentation_source_path: 'ref/threewindingmutualinductor.html'
language: en
---

# Three-Winding Mutual Inductor

## Ports

### Conserving

### **1+** — First inductor positive voltage electrical

Electrical conserving port associated with the positive voltage of the
first mutual inductor.

### **1-** — First inductor negative voltage electrical

Electrical conserving port associated with the negative voltage of the
first mutual inductor.

### **2+** — Second inductor positive voltage electrical

Electrical conserving port associated with the positive voltage of the
second mutual inductor.

### **2-** — Second inductor negative voltage electrical

Electrical conserving port associated with the negative voltage of the
second mutual inductor.

### **3+** — Third inductor positive voltage electrical

Electrical conserving port associated with the positive voltage of the
third mutual inductor.

### **3-** — Third inductor negative voltage electrical

Electrical conserving port associated with the negative voltage of the
third mutual inductor.

## Parameters

### **Inductance L1** — First winding self inductance `0.001` `H` (default) | positive scalar

Self inductance of the first winding.

### **Inductance L2** — Second winding self inductance `0.001` `H` (default) | positive scalar

Self inductance of the second winding.

### **Inductance L3** — Third winding self inductance `0.001` `H` (default) | positive scalar

Self inductance of the third winding.

### **Perfect coupling - no leakage** — Option to enable perfect coupling `Off` (default) | `On`

*Since R2025a*

Option to enable perfect coupling with no leakage and no fast pole. If you
select this parameter, the block sets the coefficients of coupling to 1
while also retaining the correct low-frequency behavior, blocking DC.

### **Coefficient of coupling, K12** — Coefficient of coupling between the first and second windings `0.9` (default) | scalar in the range [-1,1]

Coefficient of coupling that defines the mutual inductance between the
first and second windings. Negative values yield an inverted output. Do not
use magnitudes very close to 1, such as 0.9999, because these values can
introduce fast simulation dynamics. To enable perfect coupling, select the
**Perfect coupling - no leakage** parameter
instead.

#### Dependencies

To enable this parameter, clear the **Perfect coupling - no
leakage** parameter.

### **Coefficient of coupling, K13** — Coefficient of coupling between the first and third windings `0.9` (default) | scalar in the range [-1,1]

Coefficient of coupling that defines the mutual inductance between the
first and third windings. Negative values yield an inverted output. Do not
use magnitudes very close to 1, such as 0.9999, because these values can
introduce fast simulation dynamics. To enable perfect coupling, select the
**Perfect coupling - no leakage** parameter
instead.

#### Dependencies

To enable this parameter, clear the **Perfect coupling - no
leakage** parameter.

### **Coefficient of coupling, K23** — Coefficient of coupling between the second and third windings `0.9` (default) | scalar in the range [-1,1]

Coefficient of coupling that defines the mutual inductance between the
second and third windings. Negative values yield an inverted output. Do not
use magnitudes very close to 1, such as 0.9999, because these values can
introduce fast simulation dynamics. To enable perfect coupling, select the
**Perfect coupling - no leakage** parameter
instead.

#### Dependencies

To enable this parameter, clear the **Perfect coupling - no
leakage** parameter.

## Libraries

Simscape / Electrical / Passive / Transformers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

### R2025a: Model ideal three-winding mutual inductor with no fast pole

You can now model an ideal three-winding mutual inductor with no leakage and no
fast pole. To set the coefficients of coupling to 1 while also retaining the correct
low-frequency behavior, blocking DC, select the **Perfect coupling - no
leakage** parameter.

## Description

Three coupled inductors

The Three-Winding Mutual Inductor block represents a
set of three coupled inductors or windings. The voltage across the three windings is

V1=L1dI1dt+M12dI2dt+M13dI3dtV2=M12dI1dt+L2dI2dt+M23dI3dtV3=M13dI1dt+M23dI2dt+L3dI3dt

where:

- *Vi* is voltage across the
  *i*th winding.
- *Ii* is current through the
  *i*th winding.
- *Li* is self inductance of the
  *i*th winding.
- *Mij* is mutual inductance of the
  *i*th and *j*th windings, Mij=KijLiLj.

In these equations, currents are positive when flowing into the positive
node of their respective inductor terminals.

To set the coefficients of coupling to 1 while also
retaining the correct low-frequency behavior, blocking DC, select the
**Perfect coupling - no leakage** parameter *(since R2025a)*.

Simscape™ and Simscape
Electrical™ libraries include several blocks than can model the same type of transformer device. However, these blocks make different modeling assumptions. To choose the right block for your application, you must understand how these assumptions impact the block behavior as a function of frequency. For more information, see Choose Blocks to Model Transformers.

When you run a simulation that includes this block, the software checks the specified
parameter values to ensure that the resulting device is passive. If it is not, the
software issues an error.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Use nominal values to specify the expected magnitude of a variable in a model. Using
system scaling based on nominal values increases the simulation robustness. Nominal values
can come from different sources. One of these sources is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
