---
type: simulink-block
title: 'PS Min'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Nonlinear Operators'
documentation_page: 'psmin'
documentation_source_path: 'ref/psmin.html'
language: en
---

# PS Min

## Ports

### Input

### **I1** — Input physical signal, untyped physical signal

First input physical signal.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.

### **I2** — Input physical signal, untyped physical signal

Second input physical signal.

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

### **Enable zero-crossing detection** — Whether to enable zero-crossing detection `on` (default) | `off`

Clear to disable zero-crossing detection and increase simulation speed. For more
information, see Managing Zero Crossings in Simscape Models.

## Libraries

Simscape / Foundation Library / Physical Signals / Nonlinear Operators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007b**

### R2025a: Optional zero-crossing detection

Starting in R2025a, the block contains the **Enable zero-crossing
detection** check box. Clearing this check box provides the ability to disable
zero-crossing detection and increase simulation speed.

### R2019a: Unit propagation

Prior to R2019a, this block did not propagate physical units.

If your model contains legacy blocks without unit propagation, use the Upgrade Advisor to
upgrade your blocks to the latest version. For more information, see Upgrading Models with Legacy Physical Signal Blocks.

## Description

Output minimum of two input physical signals

The PS Min block outputs the minimum of its two input
physical signals:

O=min(I1,I2)

where

|  |  |
| --- | --- |
| *I*1 | Physical signal at the first input port |
| *I*2 | Physical signal at the second input port |
| *O* | Physical signal at the output port |

Physical signals at the two input ports must have commensurate units. The unit at the
output port is determined by unit propagation rules. For more information, see Physical Signal Unit Propagation.
