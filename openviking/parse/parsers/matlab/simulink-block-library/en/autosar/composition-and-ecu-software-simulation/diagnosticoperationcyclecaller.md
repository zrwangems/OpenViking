---
type: simulink-block
title: 'DiagnosticOperationCycleCaller'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Composition and ECU Software Simulation'
documentation_page: 'diagnosticoperationcyclecaller'
documentation_source_path: 'ref/diagnosticoperationcyclecaller.html'
language: en
---

# DiagnosticOperationCycleCaller

## Ports

Not documented in R2025b.

## Parameters

### **Client port name** — Name of client port AUTOSAR component uses to call Dem service interface `OperationCycle` `OperationCycle` (default) | character vector

Enter the name of the client port the AUTOSAR software component uses to call the
Dem service interface `OperationCycle`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PortName` |
| **Type:** character vector |
| **Values:**`'OperationCycle' |`unique name |
| **Default:** `'OperationCycle'` |

### **Operation** — Specify operation defined in Dem service interface `OperationCycle` `RestartOperationCycle` (default) | `SetOperationCycleState` | `GetOperationCycleState`

Select a Dem operation to control or monitor operation cycles. To start and stop
operation cycles, select `SetOperationCycleState`. To query the current
state of an operation cycle, select `GetOperationCycleState`. After you
select an operation, the inports and outports for the block are generated to support
that operation.

#### Dependencies

The operation `RestartOperationCycle` is only available if there
are no input ports on the block. If there are input ports on the block then only
`GetOperationCycle` and `SetOperationCycle` are
available.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Operation` |
| **Type:** character vector |
| **Values:** `'RestartOperationCycle' | 'SetOperationCycleState' | 'GetOperationCycleState'` |
| **Default:** `'RestartOperationCycle'` |

### **Data type for CycleState** — Specify to start or stop operation cycles `Enum:Dem_OperationCycleStateType` (default)

Specify an enumerated data type to represent a Dem format type required for some
operations.

#### Dependencies

Specify this parameter when **Operation** is set to
`SetOperationCycleState`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Datatype` |
| **Type:** character vector |
| **Values:** `'Enum:Dem_OperationCycleStateType' |` enumerated data type |
| **Default:** `'Enum:Dem_OperationCycleStateType'` |

### **Sample time** — Block sample time `'-1'` (default) | scalar

Block sample time. The default sets the block to inherit its sample time from the
model.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `st` |
| **Type:** character vector |
| **Values:** real scalar |
| **Default:** `'-1'` |

## Libraries

AUTOSAR Blockset / Classic Platform / Basic Software / Diagnostic Event Manager (Dem)

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

### R2025a: Use operations with any supported schema version

Starting R2025a, you can use any operation that is associated with the block, regardless of the configured schema version of the model and other blocks in the model.

### R2024a: Use operation `RestartOperationCycle`

Starting in R2024a, use Diagnostic Event Manager (Dem) operation
`RestartOperationCycle`. To use this operation your model must be mapped
to an AUTOSAR component.

### R2023a: Basic Software caller blocks support all AUTOSAR schema versions

Starting in 23a, Basic Software caller (BSW) blocks support all AUTOSAR schema versions
supported by AUTOSAR Blockset. The BSW blocks inherit the same schema version specified by the model. Code
and ARXML generated from the component reflect the schema version specified on the model.
When you change the schema version specified by the model, the software automatically
replaces software calls to the correct operation.

In some cases, the software may prompt you to confirm a change when moving between schema
versions. The software may also display a warning as you update to new schema versions as
some modeling patterns are no longer compliant with the configured AUTOSAR schema
version.

## Description

Call AUTOSAR Diagnostic Event Manager (Dem) service interface OperationCycle

For the AUTOSAR Classic Platform, the AUTOSAR standard defines important services as part
of Basic Software (BSW) that runs in the AUTOSAR Runtime Environment (RTE). Examples include
services provided by the Diagnostic Event Manager (Dem), the Function Inhibition Manager
(FiM), and the NVRAM Manager (NvM). In the AUTOSAR RTE, AUTOSAR software components typically
access BSW services by using client-server communication.

To support system-level modeling and simulation of AUTOSAR components and services,
AUTOSAR Blockset provides an AUTOSAR Basic Software block library. The library contains
preconfigured blocks for modeling component calls to AUTOSAR BSW services and reference
implementations of the BSW services.

As defined in the AUTOSAR specification, the Function Inhibition Manager provides a
control mechanism for selectively inhibiting (deactivating) function execution in software
component runnables based on function identifiers (FIDs) with inhibit conditions.

The Function Inhibition Manager is closely related to the Diagnostic Event Manager because
inhibiting conditions can be based on the status of diagnostic events. An operation cycle
affects events that share the same Diagnostic Service Component. The
DiagnosticOperationCycleCaller block calls the Dem service interface
`OperationCycle` to control operation cycles.
