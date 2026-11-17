---
type: simulink-block
title: 'PS Divide'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Functions'
documentation_page: 'psdivide'
documentation_source_path: 'ref/psdivide.html'
language: en
---

# PS Divide

## Ports
```yaml
ports:
- name: I1
  summary: Numerator input, untyped physical signal
  direction: input
- name: I2
  summary: Denominator input, untyped physical signal
  direction: input
- name: O
  summary: Output physical signal, untyped physical signal
  direction: output
```

### Input

### **I1** — Numerator input, untyped physical signal

First input physical signal, representing the numerator. In the block icon, this
port is marked with the **x** sign.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.

### **I2** — Denominator input, untyped physical signal

Second input physical signal, representing the denominator. In the block icon,
this port is marked with the **÷** sign.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.
### Output

### **O** — Output physical signal, untyped physical signal

Output physical signal.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

Simscape / Foundation Library / Physical Signals / Functions

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

### R2019a: Unit Propagation

Prior to R2019a, this block did not propagate physical units.

If your model contains legacy blocks without unit propagation, use the Upgrade Advisor to
upgrade your blocks to the latest version. For more information, see Upgrading Models with Legacy Physical Signal Blocks.

## Description

Compute element-wise division of two input physical signals

The PS Divide block divides one physical signal input by
another and outputs the quotient:

O=I1./I2

where

|  |  |
| --- | --- |
| *I*1 | Physical signal at the first input port (marked with the **x** sign) |
| *I*2 | Physical signal at the second input port (marked with the **÷** sign) |
| *O* | Physical signal at the output port |

The signal unit at the output port is determined by unit propagation rules. For more
information, see Physical Signal Unit Propagation.
