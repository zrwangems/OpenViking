---
type: simulink-block
title: 'Hydraulic Cap'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Elements'
documentation_page: 'hydrauliccap'
documentation_source_path: 'ref/hydrauliccap.html'
language: en
---

# Hydraulic Cap

## Ports
```yaml
ports:
- name: P
  summary: Zero flow rate hydraulic
  direction: conserving
```

### Conserving

### **P** — Zero flow rate hydraulic

Hydraulic conserving port with zero flow rate.
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

Simscape / Foundation Library / Hydraulic / Hydraulic Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012b**

### R2023a: To be removed

The Hydraulic library will be removed in a future release. Use the Isothermal Liquid library
instead. Blocks in the Isothermal Liquid library provide increased accuracy, usability, and
numerical performance.

For more information on updating your models, see Upgrading Hydraulic Models to Use Isothermal Liquid Blocks.

### R2019b: Capping unconnected ports is no longer required

This block is no longer required. Starting in R2019b, the restriction that disallowed
unconnected conserving ports in Simscape™ models has been lifted. Now, if you leave a conserving port unconnected, the
physical network sets all the Through variables at this port to 0. However, you can still
use terminator blocks to improve diagram readability.

There are no plans to remove the terminator blocks. All existing models that use these
blocks work the same as in previous releases.

## Description

(To be removed) Hydraulic port terminator with zero flow

The Hydraulic Cap block represents a hydraulic plug, that
is, a hydraulic port with zero flow through it.

You can use this block to terminate hydraulic ports on other blocks that you want to cap.
This is not necessary because if you leave a conserving port unconnected, the physical network
sets all the Through variables at that port to 0. However, terminator blocks improve diagram
readability.

You can also use this block to set the initial gauge pressure at a node.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
