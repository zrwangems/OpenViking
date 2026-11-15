---
type: simulink-block
title: 'Action Port'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Modeling / Design Model Behavior / Conditionally Executed Subsystems and Models / Other'
documentation_page: 'actionport'
documentation_source_path: 'slref/actionport.html'
language: en
---

# Action Port

## Ports

Not documented in R2025b.

## Parameters

### **States when execution is resumed** — Select handling of internal states `held` (default) | `reset`

Select how to handle internal states when a subsystem with an
Action Port block reenables.

`held`
:   When the subsystem reenables, retain the previous state values
    of the subsystem. Previous state values between calls are
    retained even if you call other subsystem blocks connected to
    the If or Switch Case
    block.

`reset`
:   When the subsystem reenables, reinitialize the state
    values.

    A subsystem reenables when the logical expression for its
    action port evaluates to true after having been previously
    false. In the following example, the Action Port
    blocks for both subsystems `A` and
    `B` have the **States when
    execution is resumed** parameter set to
    `reset`.

    When **case[1]** is `true`,
    subsystem **A** is executed. Repeated calls to
    subsystem **A** while **case
    [1]** continues to be `true`, does
    not reset its state values. The same behavior applies to
    subsystem **B**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InitializeStates` |
| **Type**: character vector |
| **Value**: `'held'` | `'reset'` |
| **Default**: `'held'` |

### **Propagate sizes of variable-size signals** — Select when to propagate a variable-size signal `Only when execution is resumed` (default) | `During execution`

Select when to propagate a variable-size signal.

`Only when execution is resumed`
:   Propagate variable-size signals only when reenabling the
    subsystem containing the Action Port
    block.

`During execution`
:   Propagate variable-size signals at each time step.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PropagateVarSize` |
| **Type**: character vector |
| **Values**: `'Only when execution is resumed'` | `'During execution'` |
| **Default**: `'Only when execution is resumed'` |

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

## Version History

**Introduced before R2006a**

## Description

Control port for action signal to If Action Subsystem or Switch Case Action Subsystem block

The Action Port block controls the execution of these subsystem blocks:

- If Action Subsystem blocks
  connected to If blocks.
- Switch Case Action
  Subsystem blocks connected to Switch Case blocks.
- Simulink based states in Stateflow® charts. See Create and Edit Simulink Based States (Stateflow).
