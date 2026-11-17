---
type: simulink-block
title: 'PS Floor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Nonlinear Operators'
documentation_page: 'psfloor'
documentation_source_path: 'ref/psfloor.html'
language: en
---

# PS Floor

## Ports
```yaml
ports:
- name: I
  summary: Input physical signal, untyped physical signal
  direction: input
- name: O
  summary: Output physical signal, untyped physical signal
  direction: output
```

### Input

### **I** — Input physical signal, untyped physical signal

Input physical signal. Arguments passed to rounding functions (such as
`floor`) must be dimensionless. Therefore, the input signal does
not have to be a scalar but must have the unit of `1`
(unitless).

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

Simscape / Foundation Library / Physical Signals / Nonlinear Operators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2009a**

### R2019a: Unit Propagation

Prior to R2019a, this block did not propagate physical units.

If your model contains legacy blocks without unit propagation, use the Upgrade Advisor to
upgrade your blocks to the latest version. For more information, see Upgrading Models with Legacy Physical Signal Blocks.

## Description

Output the largest integer smaller than or equal to input physical signal

The PS Floor block rounds the input physical signal toward
negative infinity, that is, to the nearest integer smaller than or equal to the input value:

O=floor(I)

where

|  |  |
| --- | --- |
| *I* | Physical signal at the input port |
| *O* | Physical signal at the output port |

Both the input and the output are physical signals. Untyped physical ports facilitate the
signal size propagation. However, arguments passed to rounding functions (such as
`floor`) must be dimensionless. Therefore, the input signal must have the
unit of 1 (unitless), and the output signal is also unitless.
