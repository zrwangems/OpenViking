---
type: simulink-block
title: 'PS Subtract'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Functions'
documentation_page: 'pssubtract'
documentation_source_path: 'ref/pssubtract.html'
language: en
---

# PS Subtract

## Ports

### Input

### **I1** — Input physical signal, untyped physical signal

First input physical signal. In the block icon, this port is marked with a plus
sign (**+**).

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.

### **I2** — Input physical signal, untyped physical signal

Second input physical signal, to be subtracted from the first. In the block icon,
this port is marked with a minus sign (**-**).

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

Compute simple subtraction of two input physical signals

The PS Subtract block subtracts one physical signal input
from another and outputs the difference:

O=I1−I2

where

|  |  |
| --- | --- |
| *I*1 | Physical signal at the first input port (marked with the plus sign) |
| *I*2 | Physical signal at the second input port (marked with the minus sign) |
| *O* | Physical signal at the output port |

Physical signals at the two input ports must have commensurate units. The unit at the
output port is determined by unit propagation rules. For more information, see Physical Signal Unit Propagation.
