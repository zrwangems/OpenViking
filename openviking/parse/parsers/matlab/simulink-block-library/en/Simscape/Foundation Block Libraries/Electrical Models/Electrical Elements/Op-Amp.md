---
type: simulink-block
title: 'Op-Amp'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Electrical Models / Electrical Elements'
documentation_page: 'opamp'
documentation_source_path: 'ref/opamp.html'
language: en
---

# Op-Amp

## Ports

### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the op-amp positive terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the op-amp negative terminal.

### **out** — Output terminal electrical

Electrical conserving port associated with the output node of the op-amp.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.

## Parameters

Not documented in R2025b.

## Libraries

Simscape / Foundation Library / Electrical / Electrical Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

## Description

Ideal operational amplifier

The Op-Amp block models an ideal operational amplifier
(op-amp). The figure shows the implementation schematic.

Implementation schematic of the Op-Amp block

The block implementation is based on the following assumptions:

- The ideal op-amp gain *A* is assumed to be infinite
- Then, for finite output, must have *V1* = 0
- Ideal op-amp also implies current from p to n is zero (*i1* = 0)

These assumptions result in the following equations for the block:

```
equations
    v1 == p.v - n.v;
    v1 == 0;
    i1 == 0;
end
```

For more information, click the **Source code** link in the
**Description** tab of the block dialog box.

The block has no parameters. However, you can initialize the **Current into output
node** variable prior to simulation. For more information, see Block-Level Variable Initialization.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
