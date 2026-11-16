---
type: simulink-block
title: 'Cap (2P)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Elements'
documentation_page: 'cap2p'
documentation_source_path: 'ref/cap2p.html'
language: en
---

# Cap (2P)

## Ports

### Conserving

### **A** — Mass flow rate and energy flow rate are zero two-phase fluid

Two-phase fluid conserving port where the mass flow rate and energy
flow rate are both equal to zero.

## Parameters

Not documented in R2025b.

## Libraries

Simscape / Foundation Library / Two-Phase Fluid / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2015b**

### R2019b: Capping unconnected ports is no longer required

This block is no longer required. Starting in R2019b, the restriction that disallowed
unconnected conserving ports in Simscape™ models has been lifted. Now, if you leave a conserving port unconnected, the
physical network sets all the Through variables at this port to 0. However, you can still
use terminator blocks to improve diagram readability.

There are no plans to remove the terminator blocks. All existing models that use these
blocks work the same as in previous releases.

## Description

Perfectly insulated stop to fluid flow

The Cap (2P) block represents a perfectly insulated
terminus for a two-phase fluid branch. There is no fluid flow or heat transfer through
the cap.

You can use this block to terminate two-phase fluid ports on other blocks that you
want to cap. This is not necessary because if you leave a conserving port unconnected,
the physical network sets all the Through variables at that port to 0. However,
terminator blocks improve diagram readability.

You can also use this block to set the initial pressure and specific internal energy
at a node.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables and Initial Conditions for Blocks with Finite Gas Volume.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
