---
type: simulink-block
title: 'PS Product'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Functions'
documentation_page: 'psproduct'
documentation_source_path: 'ref/psproduct.html'
language: en
---

# PS Product

## Ports

### Input

### **I1** — Input physical signal, untyped physical signal

First input physical signal to be added.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.

### **I2** — Input physical signal, untyped physical signal

Second input physical signal to be added.

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

Multiply two physical signal inputs

The PS Product block outputs the element-wise product of
two input physical signals:

O=I1.\*I2

where

|  |  |
| --- | --- |
| *I*1 | Physical signal at the first input port |
| *I*2 | Physical signal at the second input port |
| *O* | Physical signal at the output port |

The signal unit at the output port is determined by unit propagation rules. For more
information, see Physical Signal Unit Propagation.
