---
type: simulink-block
title: 'DiagnosticEventAvailableCaller'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Composition and ECU Software Simulation'
documentation_page: 'diagnosticeventavailablecaller'
documentation_source_path: 'ref/diagnosticeventavailablecaller.html'
language: en
---

# DiagnosticEventAvailableCaller

## Ports

Not documented in R2025b.

## Parameters

### **Client port name** — Name of client port AUTOSAR component uses to call Dem service interface `EventAvailable` `EventAvailable` (default) | character vector

Enter the name of the client port the AUTOSAR software component uses to call the
Dem service interface `EventAvailable`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PortName` |
| **Type:** character vector |
| **Values:** `'EventAvailable'` |
| **Default:** `'EventAvailable'` |

### **Operation** — Specify operation defined in Dem service interface `EventAvailable` `SetEventAvailable` (default)

This block supports the Dem operation `SetEventAvailable`
and generates inports and outports for the operation. You can use this operation to
configure events as unavailable. An unavailable event is treated as if it is not
configured in the system and returns E\_NOT\_OK when accessed by other operations.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Operation` |
| **Type:** character vector |
| **Values:** `'SetEventAvailable'` |
| **Default:** `'SetEventAvailable'` |

### **Sample time** — Block sample time -1 (default) | scalar

Block sample time. The default sets the block to inherit its sample time from the
model.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `st` |
| **Type:** character vector |
| **Values:** `-1 |` scalar |
| **Default:** `-1` |

## Libraries

AUTOSAR Blockset / Classic Platform / Basic Software / Diagnostic Event Manager (Dem)

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

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

Call AUTOSAR Diagnostic Event Manager (Dem) service interface EventAvailable

For the AUTOSAR Classic Platform, the AUTOSAR standard defines important services as part
of Basic Software (BSW) that runs in the AUTOSAR Runtime Environment (RTE). Examples include
services provided by the Diagnostic Event Manager (Dem), the Function Inhibition Manager
(FiM), and the NVRAM Manager (NvM). In the AUTOSAR RTE, AUTOSAR software components typically
access BSW services by using client-server communication.

To support system-level modeling and simulation of AUTOSAR components and services,
AUTOSAR Blockset provides an AUTOSAR Basic Software block library. The library contains
preconfigured blocks for modeling component calls to AUTOSAR BSW services and reference
implementations of the BSW services.

The DiagnosticEventAvailableCaller block calls the Dem service interface
`EventAvailable` to initiate the
`SetEventAvailable` operation. A component uses
`SetEventAvailable` to temporarily disable and enable a specific
event, for example, an event of the same name associated with an existing Dem
`SetEventStatus` caller block. Typically you connect a true/false
Boolean constant block to the `SetEventAvailable` input, so that you
can switch the event off (false) or on (true). When disabled, the event fired by the
`SetEventStatus` block has no effect.
