---
type: simulink-block
title: 'Conveyor System'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'conveyorsystem'
documentation_source_path: 'ref/conveyorsystem.html'
language: en
---

# Conveyor System

## Ports

### Input

### **Port\_1** — Incoming entity scalar | vector | matrix

Input entity port for entities entering the queue. Entities are not
accepted by the block when the speed of the conveyor is
`0`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **S** — Incoming anonymous entity scalar

Input port for anonymous entities entering the block. The entity
carries data that specifies the new conveyor speed upon its arrival. The
entity data must be a non-negative value between `0`
and `Inf`. The new speed applies to all entities in the
block including the incoming and existing ones.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
### Output

### **Port\_1** — Exiting entity scalar | vector | matrix

Output entity port for entities leaving the queue

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_d** — Number of entities departed off (default) | on

Selecting this check box outputs the number of entities that have
exited the block.

#### Dependencies

To enable this port, select the **Statistics** > **Number of entities departed, d** check box.

**Data Types:** `double`

### **Port\_n** — Number of entities in block off (default) | on

Selecting this check box outputs the number of entities in the
block.

#### Dependencies

To enable this block, select the **Statistics** > **Number of entities in block, n** check box.

**Data Types:** `double`

### **Port\_pe** — Pending entity in block off (default) | on

Selecting this check box outputs the value `1` for a
pending entity in the block, and `0` otherwise.

#### Dependencies

To enable this port, select the **Statistics** > **Pending entity in block, pe**.

**Data Types:** `double`

### **Port\_s** — Conveyor speed off (default) | on

Selecting this check box outputs the conveyor speed.

#### Dependencies

To enable this port, select the **Statistics** > **Conveyor speed, s**.

**Data Types:** `double`

## Parameters

### **Conveyor length** — Length of surface 100 (default) | numeric

Length of surface that entities travel on. For more information, see Description.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `mConveyorLength` |
| **Type**: character vector |
| **Values**: `'100'` | scalar |
| **Default**: `'100'` |

### **Conveyor speed** — Speed of the conveyor surface 1000 (default) | numeric

Speed of surface that entities travel on. The speed can take values
greater than `0` and its value can be zero only when the
**Variable conveyor speed** check box is selected. For
more information, see Description.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `mConveyorSpeed` |
| **Type**: character vector |
| **Values**: `'1000'` | scalar |
| **Default**: `'1000'` |

### **Minimum distance between entities** — Minimum physical separation 0 (default) | numeric

Minimum physical separation entities maintain while moving across the
conveyor system. For more information, see Description.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `mMinDisBetEntity` |
| **Type**: character vector |
| **Values**: `'0'` | scalar |
| **Default**: `'0'` |

### **Entity length source** — Entity length source `Dialog` (default) | `Attribute`

Provide entity length, selected from the drop-down list.

#### Dependencies

- `Dialog` — Selecting this option
  enables the **Entity length value**
  parameter.
- `Attribute` — Selecting this option
  enables the **Entity length attribute name**
  parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `mEntityLengthSource` |
| **Type**: character vector |
| **Values**: `'Dialog'` | `'Attribute'` |
| **Default**: `'Dialog'` |

### **Entity length value** — Length of entities 1 (default) | numeric

Length of entities, specified as a numeric value. For more information,
see Description.

#### Dependencies

To enable this parameter, select `Dialog` for
**Entity length source**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `mEntityLength` |
| **Type**: character vector |
| **Values**: `'1'` | scalar |
| **Default**: `'1'` |

### **Entity length attribute name** — Name of entity length attribute `Length` (default) | character vector

Name of entity length attribute, specified as a character vector.

#### Dependencies

To enable this parameter, select `Attribute`
for **Entity length source**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `mEntityLengthAttrName` |
| **Type**: character vector |
| **Values**: `'Length'` | character vector |
| **Default**: `'Length'` |

### **Blocked output behavior** — Behavior when the output is blocked `Accumulate` (default) | `Pause` | `Error`

Behavior when output is blocked, selected from drop-down list:

- `Accumulate` — Accumulate entities. In
  `Accumulate` mode, an entity continues
  to move on the conveyor surface until its movement is blocked by
  another entity ahead.

  For example, if one or more entities are extracted out of the
  conveyor surface by the Entity Find block, entities
  that are behind the extracted entity continue to move forward until
  they occupy the empty space due to the extraction.
- `Pause` — Pause conveyor system. In
  `Pause` mode, all entities on the
  conveyor surface stop and move together. The conveyor surface stops
  moving when an entity at the exit is unable to depart. During the
  pause, the conveyor system does not accept new entities.
- `Error` — Return an error. In
  `Error` mode, when an entity is blocked
  from entering the conveyor surface the error is displayed.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `mOutputBlockedOpt` |
| **Type**: character vector |
| **Values**: `'Accumulate'` | `'Pause'` | `'Error'` |
| **Default**: `'Accumulate'` |

### **Error if conveyor full** — Conveyor behavior when the maximum number of entities is reached `on` (default) | `off`

Conveyor behavior when the conveyor surface is full.

Selected check boxon
:   Return an error if the conveyor system is full.

Unselected check boxoff
:   Do not return an error if the conveyor system is full.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `mErrorUponFullOpt` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'on'` |

### **Variable conveyor speed** — Constant or variable conveyor speed `off` (default) | `on`

Specify if the conveyor system has constant or variable speed.

Unselected check boxoff
:   Constant speed conveyor system. You can specify the speed
    using the **Conveyor speed** parameter.

Selected check boxon
:   Variable speed conveyor system. An input port appears to
    accept anonymous entities which carry data to specify the new
    conveyor speed.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `mIsVariableSpeed` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'on'` |

### **Number of entities departed, d** — Number of entities departed `off` (default) | `on`

Number of entities that have departed the block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `mNumEntitiesDepOpt` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Number of entities in block, n** — Number of existing entities `off` (default) | `on`

Outputs the number of entities present in the block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `mNumEntitiesInBlockOpt` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Pending entity in block, pe** — Pending entities `off` (default) | `on`

Indicates whether an entity that is yet to depart is present in the block.
The value is `1` for a pending entity, and
`0` otherwise.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `mEntityPendingOpt` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Number of entities extracted, ex** — Number of entities extracted from this block `off` (default) | `on`

Outputs the number of extracted entities which are pulled out from this
block by the Entity Find block. When an entity is extracted,
**Number of entities departed, d**,and **Number
of entities in block, n** statistics are updated accordingly.
For more information about finding and extracting entities, see Find and Extract Entities in SimEvents Models.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `mNumExtractedFromBlockOpt` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Conveyor speed, s** — Speed of the conveyor for the duration of the simulation `off` (default) | `on`

Outputs the speed of the conveyor during the course of the
simulation.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `mConveyorSpeedOpt` |
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

**Introduced in R2017b**

## Description

Transport entities

The Conveyor System block transports entities across the surface of a
conveyor. Entities enter the block by sliding onto the conveyor surface and they depart
the block by sliding off. You can specify the speed of the conveyor. If the conveyor
speed is variable, a second input port appears on the block to accept anonymous entities
that carry data for specifying the new conveyor speed. Use this block to model
transportation applications involving production systems, or logistical systems.

In the Conveyor System block:

- You can specify the speed and the surface length of the conveyor. You can
  specify the length and the minimum distance between the transported
  entities.

  Simple stick diagram showing conveyor length, entity length, minimum distance between entities and conveyor speed.
- Entities slide into the conveyor surface and an entity is considered as inside
  the conveyor surface when its front side coincides with the surface
  entry.

  Simple stick diagram showing the front end of an entity lined up with the surface entry of a conveyor.
- Entities slide out of the conveyor surface and an entity is considered as
  outside the conveyor surface when its back side coincides with the surface
  entry.

  Simple stick diagram showing the back end of an entity lined up with the surface entry.
- Conveyor speed determines the total time between an entity entry to the
  surface and its exit from the surface.

  Entity can enter and exit the conveyor surface provided that:

  - There are no other entities blocking the entity when the
    **Blocked output behavior** is set to
    `Accumulate`.
  - The conveyor surface is not paused when the **Blocked output
    behavior** is set to `Pause`. For
    more information, see Blocked output behavior.

  Simple stick diagram showing an entity entering, moving over and exiting a conveyor.

  For instance, suppose that the conveyor length is `10`,
  entity length is `1`, and conveyor speed is
  `5`. Then, it takes `2.2` simulation time
  for the entity to depart the surface. `10/5 = 2` to travel
  through the surface and `1/5 = 0.2` to depart from the surface
  because its length is `1`.
- After an entity enters the conveyor surface, the next entity enters after the
  first one travels to the specified minimum distance between entities.

  Simple stick diagram showing an entity entering the conveyor only after the entity in front has reached the specified minimum distance between entities.
- The capacity of the conveyor system is the maximum number of entities allowed
  on the surface. The capacity is determined by the total surface length, entity
  length, and the minimum distance between entities.

  For example, suppose that the entity length is `1` meter,
  conveyor system surface length is `100` meters, and the
  distance between entities is `15` meters. The capacity of the
  conveyor system becomes `6` entities.

  Simple stick diagram illustrating how six entites of length 1 meter can fit onto a conveyor system of surface length 100 meters with distance between entities as 15 meters.
- When using the **Conveyor length**, **Conveyor
  speed**, **Minimum distance between entities**,
  and **Entity length value** parameters ensure that the values
  are consistent with each other.

  For example, specify the entity length of 10 cm and a conveyor system of
  length 100 m to achieve consistency:

  - Set the **Conveyor length** parameter to
    `100`.
  - Set the **Entity length** parameter to 0.1.
