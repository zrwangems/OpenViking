---
type: simulink-block
title: 'PS Abs'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Nonlinear Operators'
documentation_page: 'psabs'
documentation_source_path: 'ref/psabs.html'
language: en
---

# PS Abs

## Ports

### Input

### **I** — Input physical signal, untyped physical signal

Input physical signal.

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

**Introduced in R2008a**

### R2025a: Optional zero-crossing detection

Starting in R2025a, the block contains the **Enable zero-crossing
detection** check box. Clearing this check box provides the ability to disable
zero-crossing detection and increase simulation speed.

### R2019a: Unit propagation

Prior to R2019a, this block did not propagate physical units.

If your model contains legacy blocks without unit propagation, use the Upgrade Advisor to
upgrade your blocks to the latest version. For more information, see Upgrading Models with Legacy Physical Signal Blocks.

## Description

Output absolute value of input physical signal

The PS Abs block returns the absolute value of the input
physical signal:

O=|I|

where

|  |  |
| --- | --- |
| *I* | Physical signal at the input port |
| *O* | Physical signal at the output port |

Untyped physical ports facilitate unit propagation. The output signal has the same
physical unit as the input signal.
