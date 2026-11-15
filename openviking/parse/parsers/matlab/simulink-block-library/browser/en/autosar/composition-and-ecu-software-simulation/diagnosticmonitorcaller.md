---
type: simulink-block
title: 'DiagnosticMonitorCaller'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Composition and ECU Software Simulation'
documentation_page: 'diagnosticmonitorcaller'
documentation_source_path: 'ref/diagnosticmonitorcaller.html'
language: en
---

# DiagnosticMonitorCaller

## Ports

Not documented in R2025b.

## Parameters

### **Client port name** — Name of client port AUTOSAR component uses to call Dem service interface `DiagnosticMonitor` `DiagnosticMonitor` (default) | character vector

Enter the name of the client port the AUTOSAR software
component uses to call the Dem service interface
`DiagnosticMonitor`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PortName` |
| **Type:** character vector |
| **Values:**`'DiagnosticMonitor' |`unique name |
| **Default:** `'DiagnosticMonitor'` |

### **Operation** — Specify operation defined in Dem service interface `DiagnosticMonitor` `SetEventStatus` (default) | `ResetMonitorStatus` | `ResetEventStatus` | `PrestoreFreezeFrame` | `ClearPrestoredFreezeFrame` | `SetEventDisabled`

Select the operation that the AUTOSAR software
component calls from the Dem service interface
`DiagnosticMonitor`. The
operations are defined by the AUTOSAR standard.
After the operation is selected, the inports and
outports for the block are generated to support the
operation.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Operation` |
| **Type:** character vector |
| **Values:** `'SetEventStatus' | 'ResetMonitorStatus' | 'ResetEventStatus' | 'PrestoreFreezeFrame' | 'ClearPrestoredFreezeFrame' | 'SetEventDisabled'` |
| **Default:** `'SetEventStatus'` |

### **Data type for EventStatus** — Specify a data type to represent a Dem event type `Enum: Dem_EventStatusType` (default)

Specify an enumerated data type to represent a Dem
event type required for some operations. For more
information, see the AUTOSAR standard
*Specification of Diagnostic Event
Manager*.

#### Dependencies

Specify this parameter when
**Operation** is set to
`SetEventStatus`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Datatype` |
| **Type:** character vector |
| **Values:** `'Enum: Dem_EventStatusType' |`enumerated data type |
| **Default:** `'SetEventStatus'` |

### **Sample time** — Block sample time `'-1'` (default) | scalar

Block sample time. The default sets the block to
inherit its sample time from the model.

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

**Introduced in R2016b**

### R2025a: Use operations with any supported schema version

Starting R2025a, you can use any operation that is associated with the block, regardless of the configured schema version of the model and other blocks in the model.

### R2024a: Use operation `ResetMonitorStatus`

Starting in R2024a, use Diagnostic Event Manager (Dem) operation
`ResetMonitorStatus`. To use this operation
your model must be mapped to an AUTOSAR component.

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

Call AUTOSAR Diagnostic Event Manager (Dem) service interface DiagnosticMonitor

The AUTOSAR standard defines a Diagnostic Event Manager (Dem) service as a
part of Basic Software (BSW) that runs in the AUTOSAR Runtime Environment
(RTE). AUTOSAR software components access Dem services through client-server
calls. The DiagnosticMonitorCaller block calls the Dem service interface
`DiagnosticMonitor` to initiate a specified
operation.
