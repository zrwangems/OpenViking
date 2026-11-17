---
type: simulink-block
title: 'Entity Terminator'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'entityterminator'
documentation_source_path: 'ref/entityterminator.html'
language: en
---

# Entity Terminator

## Ports
```yaml
ports:
- name: Port_1
  summary: Input entity scalar | vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | enumerated | bus
    | fixed point
- name: Port_a
  summary: Number of entities arrived scalar
  direction: output
  data_types: double
```

### Input

### **Port\_1** — Input entity scalar | vector | matrix

Input entity port for entities entering the terminator.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
### Output

### **Port\_a** — Number of entities arrived scalar

Number of entities that have arrived at the block.

#### Dependencies

To enable this port, click the **Statistics** tab
and select the box labeled **Number of entities arrived,
a**.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Event action
  summary: Specify the behavior of the entity in certain events Entry
  group: ''
  block_parameter: EntryAction
  type: character vector
  values: MATLAB code
  default: ''''''
- name: Number of entities arrived, a
  summary: Outputs the number of entities that have arrived at the block off (default) | on
  group: ''
  block_parameter: NumberEntitiesArrived
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
```

### **Event action** — Specify the behavior of the entity in certain events `Entry`

Specify the behavior of the entity in certain events. Define the behavior
in the **Event action** parameter. The
**Entry** action is called just after the entity entry
to the block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `EntryAction` |
| **Type**: character vector |
| **Values**: MATLAB code |
| **Default**: `''` |

### **Number of entities arrived, a** — Outputs the number of entities that have arrived at the block `off` (default) | `on`

Number of entities that have arrived at the block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumberEntitiesArrived` |
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

**Introduced in R2016a**

## Description

Terminate entities

The Entity Terminator block accepts and destroys entities. Use this
block to represent the entity departure from the model.

To customize actions when entities enter, use MATLAB® code in the `Entry action` field of the **Event
actions** tab. See Events and Event Actions, for more information.
