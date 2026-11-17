---
type: simulink-block
title: 'State Control'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Subsystems'
documentation_page: 'statecontrol'
documentation_source_path: 'ref/statecontrol.html'
language: en
---

# State Control

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters:
- name: State control
  summary: Select the state control type Synchronous (default) | Classic
  group: ''
```

### **State control** — Select the state control type `Synchronous` (default) | `Classic`

Specify whether to use synchronous or classic semantics. The default is
`Synchronous`.
## Libraries

HDL Coder / HDL Subsystems

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that
affect HDL implementation and synthesized logic.

**HDL Architecture**

This block has a single, default HDL architecture. HDL Coder does not generate HDL code specific to the State Control
block. How you set the State Control block affects other blocks inside the
subsystem that have state.

## Version History

**Introduced in R2016a**

## Description

Specify synchronous reset and enable behavior for blocks with state

Use the State Control block to toggle subsystem behavior between the
default Simulink® simulation behavior and the synchronous hardware simulation behavior.

- For default Simulink simulation behavior, set **State control** to
  `Classic`. The simulation behavior in
  `Classic` mode is the same as when you do not use the State
  Control block inside the subsystem.
- For synchronous hardware simulation behavior, set **State control**
  to `Synchronous`. The State Control block in
  `Synchronous` mode improves the HDL simulation behavior of blocks
  with state, or blocks that have reset or enable ports. When use the
  `Synchronous` mode of the block, the generated HDL code uses fewer
  hardware resources and the Simulink simulation behavior closely matches that of the digital hardware.

See Synchronous Subsystem Behavior with the State Control Block.
