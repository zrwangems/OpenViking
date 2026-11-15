---
type: simulink-block
title: 'Open Circuit'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Connectors and References\u200b'
documentation_page: 'opencircuit'
documentation_source_path: '../simscape/ref/opencircuit.html'
language: en
---

# Open Circuit

## Ports

### Conserving

### **V** — Zero current electrical

Electrical conserving port that draws no current.

## Parameters

Not documented in R2025b.

## Libraries

Simscape / Foundation Library / Electrical / Electrical Elements Simscape / Electrical / Connectors & References

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

Electrical port terminator that draws no current

The Open Circuit block represents an electrical terminal
that draws no current.

You can use this block to terminate electrical ports on other blocks that you want to
leave open circuit. This is not necessary because if you leave a conserving port unconnected,
the physical network sets all the Through variables at that port to 0. However, terminator
blocks improve diagram readability.

You can also use this block to set the initial absolute voltage at a node.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
