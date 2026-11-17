---
type: simulink-block
title: 'PS Sign'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Nonlinear Operators'
documentation_page: 'pssign'
documentation_source_path: 'ref/pssign.html'
language: en
---

# PS Sign

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

Input physical signal.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.
### Output

### **O** — Output physical signal, untyped physical signal

Output physical signal. The signal size is the same as the size of the input
signal, but the unit is always `1` (unitless).

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

**Introduced in R2007b**

### R2019a: Unit Propagation

Prior to R2019a, this block did not propagate physical units.

If your model contains legacy blocks without unit propagation, use the Upgrade Advisor to
upgrade your blocks to the latest version. For more information, see Upgrading Models with Legacy Physical Signal Blocks.

## Description

Output sign of input physical signal

The PS Sign block returns the sign of the input physical
signal:

- The output is 1 when the input is greater than zero.
- The output is 0 when the input is equal to zero.
- The output is –1 when the input is less than zero.

Both the input and the output are physical signals. Untyped physical ports facilitate the
signal size propagation. The output signal is always unitless.
