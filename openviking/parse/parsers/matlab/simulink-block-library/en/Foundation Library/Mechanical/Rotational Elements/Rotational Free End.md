---
type: simulink-block
title: 'Rotational Free End'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Rotational Elements'
documentation_page: 'rotationalfreeend'
documentation_source_path: 'ref/rotationalfreeend.html'
language: en
---

# Rotational Free End

## Ports
```yaml
ports:
- name: W
  summary: Zero torque mechanical rotational
  direction: conserving
```

### Conserving

### **W** — Zero torque mechanical rotational

Mechanical rotational conserving port that rotates freely, without torque.
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

Simscape / Foundation Library / Mechanical / Rotational Elements

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

Rotational port terminator with zero torque

The Rotational Free End block represents a mechanical
rotational port that rotates freely, without torque.

You can use this block to terminate mechanical rotational ports on other blocks that you
want to leave unconnected. This is not necessary because if you leave a conserving port
unconnected, the physical network sets all the Through variables at that port to 0. However,
terminator blocks improve diagram readability.

You can also use this block to set the initial rotational velocity at a node.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
