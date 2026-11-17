---
type: simulink-block
title: 'Verification Subsystem'
family: 'sldv'
product_id: 'sldv'
product_name: 'Simulink Design Verifier'
documentation_release: R2025b
official_category: 'Verification Utilities'
documentation_page: 'verificationsubsystem'
documentation_source_path: 'ref/verificationsubsystem.html'
language: en
---

# Verification Subsystem

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

Simulink Design Verifier / Verification Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

| Architecture | Description |
| --- | --- |
| `No HDL` | Do not generate HDL code for this block. |

**HDL Block Properties**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | Control the removal of unconnected logic. The default is `off`, which means unconnected logic is not preserved in HDL code. For more details, see PreserveUpstreamLogic (HDL Coder). |

## Version History

**Introduced in R2007b**

## Description

Specify proof or test objectives without impacting simulation results or generated code

This block is a Subsystem block that is preconfigured to
serve as a starting point for creating a subsystem that specifies proof or test
objectives for use with the Simulink®
Design Verifier™ software.

The Simulink
Coder™ software ignores Verification Subsystem blocks during code generation,
behaving as if the subsystems do not exist. A Verification Subsystem
block allows you to add Simulink
Design Verifier components to a model without affecting its generated code.

**Note**

If a Verification Subsystem block contains blocks that depend on
absolute time, and you select an ERT-based target (Simulink Coder) for code
generation, set the software environment to absolute time. Open the Configuration
Parameters dialog box. In the **Code Generation** > **Interface** pane under **Software environment**, select
**absolute time**. Do not select **continuous
time**. For more information on this setting, see Support: absolute time (Embedded Coder).

When collecting model coverage, the Simulink
Coverage™ software only records coverage for Simulink
Design Verifier blocks in the Verification Subsystem block; it does not record coverage
for any other blocks in the Verification
Subsystem.

To create a Verification Subsystem in your model:

1. Copy the Verification Subsystem block from the Simulink
   Design Verifier library into your model.
2. Open the Verification Subsystem block by double-clicking it.
3. In the Verification Subsystem window, add blocks that specify proof or test
   objectives. Use Inport blocks to represent input
   from outside the subsystem.

The Verification Subsystem block in the Simulink
Design Verifier library is preconfigured to work with the Simulink
Design Verifier software. A Verification Subsystem block must:

- Contain no
  Outport blocks.
- Enable its **Treat as Atomic Unit** parameter.
- Specify its **Mask type** parameter as
  `VerificationSubsystem`.

If you alter the
Verification Subsystem block so that the preceding conditions are not met, the
Simulink
Design Verifier software displays a warning.
