---
type: simulink-block
title: 'NvMAdminCaller'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Composition and ECU Software Simulation'
documentation_page: 'nvmadmincaller'
documentation_source_path: 'ref/nvmadmincaller.html'
language: en
---

# NvMAdminCaller

## Ports

Not documented in R2025b.

## Parameters

### **Client port name** — Name of client port AUTOSAR component uses to call NvM service interface `NvMAdmin` `NvMAdmin` (default) | character vector

Enter the name of the client port the AUTOSAR software
component uses to call the NvM service interface
`NvMAdmin`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PortName` |
| **Type:** character vector |
| **Values:** `'NvMAdmin' |` unique name |
| **Default:** `'NvMAdmin'` |

### **Operation** — Operation defined in NvM service interface `NvMAdmin` `SetBlockProtection` (default)

Select the operation that the AUTOSAR software
component calls from the NvM service interface
`NvMAdmin`. The AUTOSAR standard
defines the operations. After you select the
operation, the inports and outports for the block
are generated to support the operation. One
operation is supported:
`SetBlockProtection`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Operation` |
| **Type:** character vector |
| **Values:** `'SetBlockProtection'` |
| **Default:** `'SetBlockProtection'` |

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

Call AUTOSAR NVRAM Manager (NvM) service interface NvMadmin

The AUTOSAR standard defines a NVRAM Manager (NvM) service as a part of Basic
Software (BSW) that runs in the AUTOSAR Runtime Environment (RTE). AUTOSAR
software components access NvM services through client-server calls. The
NvMAdminCaller block calls the AUTOSAR NvM service interface
`NvMAdmin` to initiate a specified
operation.
