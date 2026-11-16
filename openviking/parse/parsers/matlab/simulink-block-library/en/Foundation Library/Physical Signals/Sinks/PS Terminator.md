---
type: simulink-block
title: 'PS Terminator'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Sinks'
documentation_page: 'psterminator'
documentation_source_path: 'ref/psterminator.html'
language: en
---

# PS Terminator

## Ports

### Input

### **I** — Input physical signal, untyped physical signal

Input physical signal.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.

## Parameters

Not documented in R2025b.

## Libraries

Simscape / Foundation Library / Physical Signals / Sinks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2014b**

### R2019a: Unit Propagation

Prior to R2019a, this block did not propagate physical units.

If your model contains legacy blocks without unit propagation, use the Upgrade Advisor to
upgrade your blocks to the latest version. For more information, see Upgrading Models with Legacy Physical Signal Blocks.

## Description

Terminator for unconnected physical signal outputs

Use the PS Terminator block to cap physical signal output
ports that do not connect to other blocks.

Unlike conserving ports in physical modeling, or Simulink® output ports, unconnected physical signal output ports do not generate warnings.
However, you can use a PS Terminator block for clarity, to
indicate that the signal was not inadvertently left unconnected.

The block icon size allows you to connect the PS Terminator
block to an open port without rerouting the adjacent lines:
