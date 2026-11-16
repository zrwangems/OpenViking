---
type: simulink-block
title: 'PS Concatenate'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Functions'
documentation_page: 'psconcatenate'
documentation_source_path: 'ref/psconcatenate.html'
language: en
---

# PS Concatenate

## Ports

### Input

### **I1** — Input physical signal, untyped physical signal

First input physical signal to be concatenated.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.

### **I2** — Input physical signal, untyped physical signal

Second input physical signal to be concatenated.

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

### **Concatenate horizontally** — Specify concatenation method for matrices `Off` (default) | `On`

If the input signals are matrices, then by default the block concatenates them
vertically. To concatenate the matrices horizontally, select the **Concatenate
horizontally** check box.

## Libraries

Simscape / Foundation Library / Physical Signals / Functions

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023b**

## Description

Concatenate two vector or matrix physical signals

The PS Concatenate block concatenates two input vectors or
matrices into a single output.

Physical signals at the two input ports must have commensurate units. The unit at the
output port is determined by unit propagation rules. For more information, see Physical Signal Unit Propagation.

By default, the block concatenates the matrices vertically. To concatenate horizontally,
select the **Concatenate horizontally** check box.
