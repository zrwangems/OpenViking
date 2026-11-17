---
type: simulink-block
title: 'Cap (IL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Elements'
documentation_page: 'capil'
documentation_source_path: 'ref/capil.html'
language: en
---

# Cap (IL)

## Ports
```yaml
ports:
- name: A
  summary: Mass flow rate is zero isothermal liquid
  direction: conserving
```

### Conserving

### **A** — Mass flow rate is zero isothermal liquid

Isothermal liquid conserving port where the mass flow rate is equal to
zero.
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

Simscape / Foundation Library / Isothermal Liquid / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2025a**

## Description

Isothermal liquid port terminator with zero flow

The Cap (IL) block represents a terminus to an isothermal
liquid branch. There is no mass flow through the cap.

You can use this block to terminate isothermal liquid ports on other blocks that you want
to cap. Using this block is not necessary because if you leave a conserving port unconnected,
the physical network sets all the Through variables at that port to 0. However, terminator
blocks improve diagram readability.

You can also use this block to set the initial pressure at a node.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
