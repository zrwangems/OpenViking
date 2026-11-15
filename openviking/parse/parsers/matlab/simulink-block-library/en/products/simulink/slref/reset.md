---
type: simulink-block
title: 'Reset'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Modeling / Design Model Behavior / Conditionally Executed Subsystems and Models / Other'
documentation_page: 'reset'
documentation_source_path: 'slref/reset.html'
language: en
---

# Reset

## Ports

Not documented in R2025b.

## Parameters

### **Reset trigger type** — Select the type of trigger event `level` (default) | `rising` | `falling` | `either` | `level hold`

Select the type of trigger signal that resets the subsystem block
states.

`level`
:   Reset the block states when the trigger signal is nonzero at
    the current time step or changes from nonzero at the previous
    time step to zero at the current time step.

`rising`
:   Reset the block states when the trigger signal rises from a
    zero to a positive value or from a negative to a positive
    value.

`falling`
:   Reset the block states when the trigger signal falls from a
    positive value to zero or from a positive to a negative
    value.

`either`
:   Reset the block states when the trigger signal changes from a
    zero to a nonzero value or changes sign.

`level hold`
:   Reset the block states when the trigger signal is nonzero at
    the current time step.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ResetTriggerType` |
| **Type**: character vector |
| **Value**: `'level'` | `'rising'` | `'falling'` | `'either'` | `'level hold'` |
| **Default**: `'level'` |

### **Propagate sizes of variable-size signals** — Select when to propagate a variable-size signal `During execution` (default) | `Only when enabling`

Select when to propagate a variable-size signal.

`During execution`
:   Propagate variable-size signals at each time step.

`Only when resetting`
:   Propagate variable-size signals when resetting a
    Subsystem block containing a
    Reset port block. When you select this
    option, sample time must be periodic.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PropagateVarSize` |
| **Type:** character vector |
| **Value:** `'During execution'` | `'Only when resetting'` |
| **Default:** `'During execution'` |

### **Enable zero-crossing detection** — Control zero-crossing detection on (default) | off

Control zero-crossing detection.

on
:   Detect zero crossings.

off
:   Do not detect zero crossings.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ZeroCross` |
| **Type:** character vector |
| **Value:** `'on'` | `'off'` |
| **Default:** `'on'` |

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

**Introduced in R2015a**

### R2025a: Variant control variables in mask and model workspaces supported

You can define variant control variables in the mask and model workspaces to
control active variants in the Reset Function block, provided the
**Generate preprocessor conditionals** parameter is
`off`.

## Description

Control block for resettable subsystem

A Reset block placed at the root level of a Subsystem
block adds a control port to the block. When a reset trigger signal occurs on the signal
connected to the port, the block states of the subsystem are reset to their initial
condition. See Resettable Subsystem.
