---
type: simulink-block
title: 'Translational Free End'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Mechanical Models / Translational Elements'
documentation_page: 'translationalfreeend'
documentation_source_path: 'ref/translationalfreeend.html'
language: en
---

# Translational Free End

## Ports

### Conserving

### **V** — Zero force mechanical translational

Mechanical translational conserving port that moves freely, without force.

## Parameters

Not documented in R2025b.

## Libraries

Simscape / Foundation Library / Mechanical / Translational Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012b**

### R2019b: Capping unconnected ports is no longer required

This block is no longer required. Starting in R2019b, the restriction that disallowed
unconnected conserving ports in Simscape™ models has been lifted. Now, if you leave a conserving port unconnected, the
physical network sets all the Through variables at this port to 0. However, you can still
use terminator blocks to improve diagram readability.

There are no plans to remove the terminator blocks. All existing models that use these
blocks work the same as in previous releases.

## Description

Translational port terminator with zero force

The Translational Free End block represents a mechanical
translational port that moves freely, without force.

You can use this block to terminate mechanical translational ports on other blocks that
you want to leave unconnected. This is not necessary because if you leave a conserving port
unconnected, the physical network sets all the Through variables at that port to 0. However,
terminator blocks improve diagram readability.

You can also use this block to set the initial translational velocity at a node.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
