---
type: simulink-block
title: 'NvMServiceCaller'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Composition and ECU Software Simulation'
documentation_page: 'nvmservicecaller'
documentation_source_path: 'ref/nvmservicecaller.html'
language: en
---

# NvMServiceCaller

## Ports

Not documented in R2025b.

## Parameters

### **Client port name** — Name of client port AUTOSAR component uses to call NvM service interface `NvMService` `NvMService` (default) | character vector

Enter the name of the client port the AUTOSAR software
component uses to call the NvM service interface
`NvMService`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PortName` |
| **Type:** character vector |
| **Values:** `'NvMService' |` unique name |
| **Default:** `'NvMService'` |

### **Operation** — Specify operation defined in NvM service interface `NvMService` `GetDataIndex` (default) | `GetErrorStatus` | `EraseNvBlock` | `InvalidateNvBlock` | `ReadBlock` | `RestoreBlockDefaults` | `SetDataIndex` | `SetRamBlockStatus` | `WriteBlock`

Select the operation that the AUTOSAR software
component calls from the NvM service interface
`NvMService`. The AUTOSAR
standard defines the operations. After you select
the operation, the inports and outports for the
block are generated to support the operation.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Operation` |
| **Type:** character vector |
| **Values:** `'GetDataIndex' | 'GetErrorStatus' | 'EraseNvBlock' | 'InvalidateNvBlock' | 'ReadBlock' | 'RestoreBlockDefaults' | 'SetDataIndex' | 'SetRamBlockStatus' | 'WriteBlock'` |
| **Default:** `'GetDataIndex'` |

### **Argument specification** — Specify data type and dimensions for operation read or write access `uint8(1)` (default) | character vector

A MATLAB expression that specifies data type and
dimensions for data to be read or written by the
operation.

- To specify a multidimensional data type, you
  can use array syntax, such as `int8([1 1;
  1 1])`.
- To specify a structured data type, you can
  create a `Simulink.Parameter`
  data object, type it with a
  `Simulink.Bus` object, and
  reference the parameter name.

For examples, see Argument Specification for Simulink Function Blocks.

#### Dependencies

Specify this parameter when
**Operation** is set to
`ReadBlock`,
`RestoreBlockDefaults`, or
`WriteBlock`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ArgumentSpecification` |
| **Type:** character vector |
| **Values:** `'uint8(1)' |` character vector |
| **Default:** `'uint8(1)'` |

### **Sample time** — Block sample time -1 (default) | scalar

Block sample time. The default sets the block to
inherit its sample time from the model.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `st` |
| **Type:** scalar |
| **Values:** `'-1' |` scalar |
| **Default:** `'-1'` |

## Libraries

AUTOSAR Blockset / Classic Platform / Basic Software / NVRAM Manager (NvM)

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

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

Call AUTOSAR NVRAM Manager (NvM) service interface NvMService

The AUTOSAR standard defines a NVRAM Manager (NvM) service as a part of Basic
Software (BSW) that runs in the AUTOSAR Runtime Environment (RTE). AUTOSAR
software components access NvM services through client-server calls. The
NvMServiceCaller block calls the AUTOSAR NvM service interface
`NvMService` by to initiate specified
operation.
