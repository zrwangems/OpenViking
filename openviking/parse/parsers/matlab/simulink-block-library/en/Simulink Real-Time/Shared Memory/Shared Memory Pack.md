---
type: simulink-block
title: 'Shared Memory Pack'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Shared Memory'
documentation_page: 'sharedmemorypack'
documentation_source_path: 'io_ref/sharedmemorypack.html'
language: en
---

# Shared Memory Pack

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters:
- name: Partition struct
  summary: Name of structure [] (default)
  group: ''
  block_parameter: partition
```

### **Partition struct** — Name of structure `[]` (default)

Enter the name of the predefined shared memory partition structure.

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

Shared memory pack

The Shared Memory Pack block packs the specified partition structure into
an unstructured double word array vector. It converts one or more Simulink® signals of varying data types into the vector. Typically, the input to a pack
block is the output from a write block. The Simulink interface is not aware of structures; pass the output of each structure segment
as input to the Shared Memory Pack block.

Memory partitions consist of groups of Simulink signals, which are combined into blocks (packets) of 32-bit words. Before you
begin to configure this block, be sure that you have a predefined shared memory partition
structure as required by the shared memory manufacturer.

This block ignores the **Address** field of the partition
structure.
