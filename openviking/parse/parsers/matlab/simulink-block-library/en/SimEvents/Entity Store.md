---
type: simulink-block
title: 'Entity Store'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'entitystore'
documentation_source_path: 'ref/entitystore.html'
language: en
---

# Entity Store

## Ports
```yaml
ports:
- name: Port_1
  summary: Input entity scalar | vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | enumerated | bus
    | fixed point
- name: Port_1
  summary: Output entity scalar | vector | matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | enumerated | bus
    | fixed point
- name: Port_d
  summary: Number of entities that have departed the block scalar
  direction: output
  data_types: double
- name: Port_n
  summary: Number of entities that have not yet departed the block scalar
  direction: output
  data_types: double
- name: Port_w
  summary: Average wait time for entities in the block scalar
  direction: output
  data_types: double
- name: Port_l
  summary: Average store size scalar
  direction: output
  data_types: double
- name: Port_ex
  summary: Number of entities extracted scalar
  direction: output
  data_types: double
```

### Input

### **Port\_1** — Input entity scalar | vector | matrix

Input entity port for entities entering the storage.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
### Output

### **Port\_1** — Output entity scalar | vector | matrix

Output entity port for entities exiting the storage.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_d** — Number of entities that have departed the block scalar

Number of entities that have departed the block.

#### Dependencies

To enable this port, click the **Statistics** tab
and select the box labeled **Number of entities departed,
d**.

**Data Types:** `double`

### **Port\_n** — Number of entities that have not yet departed the block scalar

Number of entities that have not yet departed the block.

#### Dependencies

To enable this port, click the **Statistics** tab
and select the box labeled **Number of entities in block,
n**.

**Data Types:** `double`

### **Port\_w** — Average wait time for entities in the block scalar

Average wait time for entities in the block.

#### Dependencies

To enable this port, click the **Statistics** tab
and select the box labeled **Average wait,
w**.

**Data Types:** `double`

### **Port\_l** — Average store size scalar

Average size of the store.

#### Dependencies

To enable this port, click the **Statistics** tab
and select the box labeled **Average store size,
l**.

**Data Types:** `double`

### **Port\_ex** — Number of entities extracted scalar

Number of entities that are pulled out of this block.

#### Dependencies

To enable this port, click the **Statistics** tab
and select the box labeled **Number of entities extracted,
ex**.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Capacity
  summary: Specify the capacity of the storage 25 (default) | scalar
  group: ''
  block_parameter: Capacity
  type: character vector
  values: '''25'' | scalar'
  default: '''25'''
- name: Number of entities departed, d
  summary: Outputs the number of entities that have departed the block off (default) | on
  group: ''
  block_parameter: NumberEntitiesDeparted
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Number of entities in block, n
  summary: Outputs the number of entities present in the block, which have yet to depart off (default) | on
  group: ''
  block_parameter: NumberEntitiesInBlock
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Average wait, w
  summary: Outputs the average wait time off (default) | on
  group: ''
  block_parameter: AverageWait
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Average store size, l
  summary: Outputs the average store size off (default) | on
  group: ''
  block_parameter: AverageStoreSize
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Number of entities extracted, ex
  summary: Number of entities extracted from this block off (default) | on
  group: ''
  block_parameter: NumEntitiesExtracted
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
```

### **Capacity** — Specify the capacity of the storage `25` (default) | scalar

Specify the maximum number of entities contained in the storage.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Capacity` |
| **Type**: character vector |
| **Values**: `'25'` | scalar |
| **Default**: `'25'` |

### **Number of entities departed, d** — Outputs the number of entities that have departed the block `off` (default) | `on`

Selecting this check box outputs the number of entities that have exited
the block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumberEntitiesDeparted` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Number of entities in block, n** — Outputs the number of entities present in the block, which have yet to depart `off` (default) | `on`

Selecting this check box outputs the number of entities present in the
block, which have yet to depart.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumberEntitiesInBlock` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Average wait, w** — Outputs the average wait time `off` (default) | `on`

Sum of the wait times for entities departing the block divided by their
total number. *Wait time* is the duration between the
Entity Store block entry and exit of an entity. For more
information, see Interpret SimEvents Models Using Statistical Analysis.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `AverageWait` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Average store size, l** — Outputs the average store size `off` (default) | `on`

Accumulated time-weighted average store size. *Store
size* is the number of entities stored in the block. The
block computes average store size by:

1. Multiplying the store size by its duration to calculate
   time-weighted store size
2. Summing up all time-weighted store sizes and averaging them
   over total time

For more information, see Interpret SimEvents Models Using Statistical Analysis.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `AverageStoreSize` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Number of entities extracted, ex** — Number of entities extracted from this block `off` (default) | `on`

Outputs the number of extracted entities which are pulled out from this
block by the Entity Find block. When an entity is extracted,
**Number of entities departed, d**, **Number of
entities in block, n**, **Average wait, w**,
and **Average store size, l** statistics are updated
accordingly. For more information about finding and extracting entities, see
Find and Extract Entities in SimEvents Models.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumEntitiesExtracted` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |
## Libraries

SimEvents

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018a**

## Description

Store entities

The Entity Store block serves as a container or bin to store unordered
entities. The entities are ready to leave the block immediately provided they are
accepted by the next block. The Entity Store block attempts to forward an
entity immediately upon its arrival. If the attempt fails, the block puts the entity in
a pending state. The entity can then leave when the next block can start accepting
it.

To customize actions when entities enter, exit, or are blocked, enter MATLAB® code in the `Entry action`, `Exit
action`, or `Blocked action` field of the **Event
actions** tab.
