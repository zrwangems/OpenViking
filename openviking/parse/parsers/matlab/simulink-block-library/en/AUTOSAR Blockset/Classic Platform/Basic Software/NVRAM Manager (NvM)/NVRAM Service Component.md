---
type: simulink-block
title: 'NVRAM Service Component'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Classic Platform / Basic Software / NVRAM Manager (NvM)'
documentation_page: 'nvramservicecomponent'
documentation_source_path: 'ref/nvramservicecomponent.html'
language: en
---

# NVRAM Service Component

## Ports

Not documented in R2025b.

## Parameters

### **Block ID** — ID that identifies service block 1 (default) | scalar

The RTE tab table lists component client ports and their mapping to NvM
service block IDs. Each row in the table represents a call into NvM services
from a Basic Software caller block. Calls that act on the same NvM block use
the same block ID. Check the block ID mappings. For examples of mapping NvM
client ports to block IDs, see Simulate AUTOSAR Basic Software Services and Run-Time Environment.

### **Maximum number of memory blocks** — Maximum number of memory blocks to use in NvM service operations 10 (default) | scalar

Specify maximum number of memory blocks to use in NvM service
operations.

### **Initial Value** — Initial values of NvM client ports 0 (default) | real, finite scalar or vector

Specify the initial values of the NvM client ports as finite, real-valued
scalars or vectors. The values must be scalar, or have the same dimensions
as the input signal.

## Libraries

AUTOSAR Blockset / Classic Platform / Basic Software / NVRAM Manager (NvM)

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017b**

### R2022b: Initial values for NVRAM Service Component blocks

R2022b enables you to define initial values for NVRAM services that are accessed
during simulation by basic software. To configure the initial values, you can open
the NVRAM Service Component block parameters, click the **Initial
Values** tab, and set an initial value for each NvM client port.

## Description

Configure AUTOSAR NVRAM Services and Runtime Environment (RTE) for emulation

The NVRAM Service Component block provides reference implementations of NVRAM Manager
(NvM) services supported by AUTOSAR Basic Software (BSW) caller blocks. When coupled
with NvM caller blocks, the reference implementations enable you to configure and run
system-level or composition-level simulations of AUTOSAR NvM service calls.

The block has prepopulated parameters, including RTE block ID parameters and NvM
**NVRAM Properties** parameters. Examine the parameter settings and
consider if modifications are required based on how you are using the NvM service
operations.
