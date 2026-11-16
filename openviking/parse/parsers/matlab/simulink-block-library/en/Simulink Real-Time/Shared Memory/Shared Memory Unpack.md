---
type: simulink-block
title: 'Shared Memory Unpack'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Shared Memory'
documentation_page: 'sharedmemoryunpack'
documentation_source_path: 'io_ref/sharedmemoryunpack.html'
language: en
---

# Shared Memory Unpack

## Ports

Not documented in R2025b.

## Parameters

### **Partition struct** — Name of structure `[]` (default)

Enter the name of the predefined shared memory partition structure. The block
unpacks the double word array vector into this structure.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `partition` |

## Libraries

Simulink Real-Time / Shared Memory

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2006a**

## Description

Shared memory unpacking

The Shared Memory Unpack block unpacks an unstructured double word array
vector (from the Shared Memory Pack block) into the specified partition structure.

Before you begin to configure this block, be sure that you have a predefined shared memory
partition structure as required by the shared memory manufacturer.

This block ignores the **Address** field of the partition
structure.
