---
type: simulink-block
title: 'Derating Function'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Control Algorithm Design / Controls / Controllers'
documentation_page: 'deratingfunction'
documentation_source_path: 'ref/deratingfunction.html'
language: en
---

# Derating Function

## Ports

### Input

### **fmax** — Maximum reference signal limit scalar

Maximum limit of the reference signal value beyond which the derating factor
becomes zero.

**Data Types:** `single` | `double` | `fixed point`

### **ffeedback** — Reference feedback signal scalar

Reference signal that the block uses to generate the derating factor, which you
can then use to derate a control signal.

**Data Types:** `single` | `double` | `fixed point`
### Output

### **y** — Derating factor scalar

Derating factor that the block generates based on the feedback and maximum limit
values of the reference signal when the signal exceeds the value of the
**Derating threshold** parameter.

**Data Types:** `single` | `double` | `fixed point`

## Parameters

### **Derating threshold** — Threshold beyond which derating must occur `0.9` (default) | scalar in the range [0,1)

The reference signal value beyond which the block generates the derating
factor.

## Libraries

Motor Control Blockset / Controls / Controllers Motor Control Blockset HDL Support / Controls / Controllers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL implementation and
synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2020a**

## Description

Compute derating factor

The Derating Function block generates the derating factor
(*y*) according to the feedback
(*ffeedback*) and maximum limit
(*fmax*) values of the input reference
signal.

The derating factor:

- Remains equal to one when *ffeedback* lies
  between positive and negative values of the **Derating threshold**. The
  derating factor varies linearly outside this range according to
  *ffeedback*.
- Remains equal to zero when the reference signal lies beyond (positive or negative)
  *fmax*.

Therefore, you can use the generated derating factor to derate a control signal after the
reference signal crosses the specified **Derating threshold**.

This figure shows the block output when you use a sinusoidal wave as
*ffeedback*.

### Equations

The **Derating threshold** parameter, x indicates the percentage of peak amplitude for the reference signal. The
**Derating threshold** is 0.5 in the block output shown, which results in
a threshold value of 2 (for the peak amplitude value of 4 for the sinusoidal reference
signal).

x=[0,1)

This equation describes how the block computes the derating factor
(*y*).

Derating factor (y)=1−ffeedback−xfmax(1−x)fmax
