---
type: simulink-block
title: 'Ideal Transformer'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Elements'
documentation_page: 'idealtransformer'
documentation_source_path: 'ref/idealtransformer.html'
language: en
---

# Ideal Transformer

## Ports

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

### **Winding ratio** — Ratio of primary coil turns to secondary coil turns `1` (default) | positive scalar

Winding ratio of the transformer, which is the ratio of primary coil turns to
secondary coil turns.

## Libraries

Simscape / Foundation Library / Electrical / Electrical Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

## Description

Ideal transformer in electrical systems

The Ideal Transformer block models an ideal
power-conserving transformer, described with the following equations:

V1=N·V2

I2=N·I1

where:

- *V1* is the primary voltage.
- *V2* is the secondary voltage.
- *I1* is the current flowing into the primary **+**
  terminal.
- *I2* is the current flowing out of the secondary
  **+** terminal.
- *N* is the winding ratio.

The two electrical networks connected to the primary and secondary windings must each have
their own Electrical Reference block.

Use this block to represent either an AC transformer or a solid-state DC to DC converter.
To model a transformer with inductance and mutual inductance terms, use the
Mutual Inductor block.

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
