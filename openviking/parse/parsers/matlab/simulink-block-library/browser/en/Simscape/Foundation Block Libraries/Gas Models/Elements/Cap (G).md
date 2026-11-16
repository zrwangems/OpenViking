---
type: simulink-block
title: 'Cap (G)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Gas Models / Elements'
documentation_page: 'capg'
documentation_source_path: 'ref/capg.html'
language: en
---

# Cap (G)

## Ports

### Conserving

### **A** — Mass flow rate and energy flow rate are zero gas

Gas conserving port where the mass flow rate and energy flow rate are
both equal to zero.

## Parameters

Not documented in R2025b.

## Libraries

Simscape / Foundation Library / Gas / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

### R2019b: Capping unconnected ports is no longer required

This block is no longer required. Starting in R2019b, the restriction that disallowed
unconnected conserving ports in Simscape™ models has been lifted. Now, if you leave a conserving port unconnected, the
physical network sets all the Through variables at this port to 0. However, you can still
use terminator blocks to improve diagram readability.

There are no plans to remove the terminator blocks. All existing models that use these
blocks work the same as in previous releases.

## Description

Gas port terminator with zero flow

The Cap (G) block represents a perfectly insulated
terminus for a gas network branch. There is no mass or energy flow through the
cap.

You can use this block to terminate gas ports on other blocks that you want to cap.
This is not necessary because if you leave a conserving port unconnected, the physical
network sets all the Through variables at that port to 0. However, terminator blocks
improve diagram readability.

You can also use this block to set the initial pressure and temperature at a node.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables and Initial Conditions for Blocks with Finite Gas Volume.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
