---
type: simulink-block
title: 'Control Function Available Caller'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Classic Platform / Basic Software / Function Inhibition Manager (FiM)'
documentation_page: 'controlfunctionavailablecaller'
documentation_source_path: 'ref/controlfunctionavailablecaller.html'
language: en
---

# Control Function Available Caller

## Ports

Not documented in R2025b.

## Parameters

### **Client port name** — Name of client port AUTOSAR component uses to call FiM service interface `ControlFunctionAvailable` `ControlFunctionAvailable` (default) | character vector

Enter the name of the client port the AUTOSAR software component uses to call the
FiM service interface `ControlFunctionAvailable`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PortName` |
| **Type:** character vector |
| **Values:** `'ControlFunctionAvailable' |` unique name |
| **Default:** `'ControlFunctionAvailable'` |

### **Operation** — Specify operation defined in FiM service interface `ControlFunctionAvailable` `SetFunctionAvailable` (default)

This block supports the FiM operation
`SetFunctionAvailable` and generates inports and outports for
the operation. Passing a true value marks the function associated with the client port
as available, a false value marks the function as not available. A
`GetPermission` operation (Function Inhibition Caller
block) associated with a function that is not available returns false.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Operation` |
| **Type:** character vector |
| **Values:** `'SetFunctionAvailable'` |
| **Default:** `'SetFunctionAvailable'` |

### **Sample time** — Block sample time -1 (default) | scalar

Block sample time. The default sets the block to inherit its sample time from the
model.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `st` |
| **Type:** scalar |
| **Values:** `-1 |` scalar |
| **Default:** `-1` |

## Libraries

AUTOSAR Blockset / Classic Platform / Basic Software / Function Inhibition Manager (FiM)

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

Call AUTOSAR Function Inhibition Manager (FiM) service interface ControlFunctionAvailable

For the AUTOSAR Classic Platform, the AUTOSAR standard defines important services as part
of Basic Software (BSW) that runs in the AUTOSAR Runtime Environment (RTE). Examples include
services provided by the Diagnostic Event Manager (Dem), the Function Inhibition Manager
(FiM), and the NVRAM Manager (NvM). In the AUTOSAR RTE, AUTOSAR software components typically
access BSW services using client-server communication.

To support system-level modeling and simulation of AUTOSAR components and services,
AUTOSAR Blockset provides an AUTOSAR Basic Software block library. The library contains
preconfigured blocks for modeling component calls to AUTOSAR BSW services and reference
implementations of the BSW services.

As defined in the AUTOSAR specification, the Function Inhibition Manager provides a
control mechanism for selectively inhibiting (deactivating) function execution in software
component runnables based on function identifiers (FIDs) with inhibit conditions.

The Function Inhibition Manager is closely related to the Diagnostic Event Manager because
inhibiting conditions can be based on the status of diagnostic events. The Control Function
Available Caller block calls the FiM service interface
`ControlFunctionAvailable` to initiate the
`SetFunctionAvailable` operation.
