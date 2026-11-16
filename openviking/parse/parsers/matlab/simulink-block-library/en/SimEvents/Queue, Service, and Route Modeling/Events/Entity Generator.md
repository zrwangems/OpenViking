---
type: simulink-block
title: 'Entity Generator'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: 'Queue, Service, and Route Modeling / Generate and Destroy Entities and Messages'
documentation_page: 'entitygenerator'
documentation_source_path: 'ref/entitygenerator.html'
language: en
---

# Entity Generator

## Ports

### Input

### **Port\_1** — Input to trigger entity generation upon arrival of events scalar | vector | matrix

#### Dependencies

To enable this port, click the **Entity
generation** tab and select
`Event-based` for the
**Generation method**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_2** — Input for the signal that determines the intergeneration time value for the next entity generation scalar | vector | matrix

#### Dependencies

To enable this port, click the **Entity
generation** tab and select
`Time-based` for the
**Generation method** and `Signal
port` for the **Time
source**.

**Data Types:** `double`
### Output

### **Port\_1** — Output generated entity scalar | vector | matrix

Output port for the generated entities departing the generator.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_d** — Number of entities that have departed the block scalar

Number of entities that have departed the block.

#### Dependencies

To enable this port, click the **Statistics** tab
and select the box labeled **Number of entities departed,
d**.

**Data Types:** `double`

### **Port\_pe** — Pending entity in block off (default) | on

Outputs `1` for a pending entity, and
`0` otherwise.

#### Dependencies

To enable this port, select the **Statistics** > **Pending entity in block, pe**.

**Data Types:** `double`

### **Port\_w** — Average intergeneration time off (default) | on

Outputs the average time between generation of entities.

#### Dependencies

To enable this port, select the **Statistics** > **Average intergeneration time, w**.

**Data Types:** `double`

## Parameters

### **Generation method** — Select the method of entity generation `Time-based` (default) | `Event-based`

Choose the entity generation method. Choose
`Time-based` to generate entities using
intergeneration times from an input signal or statistical distribution.
Choose `Event-based` for an external event to
determine the entity intergeneration time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `GenerationMethod` |
| **Type**: character vector |
| **Values**: `'Time-based'` | `'Event-based'` |
| **Default**: `'Time-based'` |

### **Time source** — Select the source of the intergeneration time `Dialog` (default) | `Signal port` | `MATLAB action`

Specify the source for entity intergeneration time.

- Select `Dialog` to specify a fixed
  period between entity generations.
- Select `Signal port` to generate
  entities based on an input signal.
- Select `MATLAB action` to define a
  MATLAB Script that defines the intergeneration time
  represented by `dt`.

For more information about specifying intergeneration times for entities,
see Specify Intergeneration Times for Entities.

#### Dependencies

This parameter is visible when the **Generation
method** is set to
`Time-based`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `TimeSource` |
| **Type**: character vector |
| **Values**: `'Dialog'` | `'Signal port'` | `'MATLAB action'` |
| **Default**: `'Dialog'` |

### **Period** — Define the period between the generation of entities `1` (default) | scalar

Specify the time between entity intergeneration. For instance, if the
**Period** is `1`, the block waits
`1` simulation time in between entity generations. See,
Specify Intergeneration Times for Entities for more information.

**Tunable:** Yes

#### Dependencies

This parameter is visible when **Generation method**
is set to `Time-based`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Period` |
| **Type**: character vector |
| **Values**: `'1'` | scalar |
| **Default**: `'1'` |

### **Intergeneration time action** — Specify the time between entity generations `dt = rand(1,1)` (default) | MATLAB code

Use MATLAB code to specify service time. `dt` specifies
the time between entity generations. You can manually specify
`dt` or use **Insert pattern** button
to generate entities with a repeating sequence or from a distribution. The
block uses this parameter every time it is ready for entity generation. For
an example, see Specify Intergeneration Times for Entities.

#### Dependencies

This parameter is visible when **Service time
source** is set to `MATLAB
action`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `IntergenerationTimeAction` |
| **Type**: character vector |
| **Values**: MATLAB code |
| **Default**: `'dt = rand(1,1);'` |

### **Generate entity at simulation start** — Generate an entity at the start of the simulation `on` (default) | `off`

Generates entity at the start of the simulation.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `GenerateEntityAtSimulationStart` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'on'` |

### **Entity type** — Choose the type of entity to generate `Structured` (default) | `Anonymous` | `Bus object`

Choose the type of entity to generate.

- The `Anonymous` type has one data
  value associated with it.
- The `Structured` type (default)
  includes name and initial value attributes that you can
  specify.

  - You can attach more than one attribute to an entity by
    clicking Green plus symbol.
  - You can delete attributes by clicking Red cross symbol.
  - You can change the order of the attributes by clicking Blue arrow pointing upward and Blue arrow pointing downward.
  - You can convert a
    `Structured` type entity to
    a bus object by clicking File symbol with two smaller symbols atop: a green down arrow on the top left, and a group of three parallel black lines on the bottom right.
- The `Bus object` type lets you
  generate bus objects as entities.

  To open the Type Editor to generate bus objects,
  click **Open Type Editor**. A bus object can
  be an element of another bus object which can be used to create
  hierarchy in the data that is attached to an entity.

For more information, see Entities in a SimEvents Model.

#### Limitations

For the `Structured` entity type, you can
create a maximum of 31 attributes from the Block Parameters dialog box.
To create more than 31 attributes, use the `set_param` function for the
`EntityType` block parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `EntityType` |
| **Type**: character vector |
| **Values**: `'Structured'` | `'Anonymous'` | `'Bus object'` |
| **Default**: `'Structured'` |

### **Entity priority** — Specify the priority of the generated entity `300` (default) | scalar

Determines the priority of the generated entity. The lower the value the
higher the priority For more information, see Working with Entity Attributes and Entity Priorities.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `EntityPriority` |
| **Type**: character vector |
| **Values**: `'300'` | scalar |
| **Default**: `'300'` |

### **Entity type name** — Specify the name of the generated entity `Entity` (default) | character vector

Determines the name of the generated entity.

#### Dependencies

This parameter is visible when **Entity type** is set
to `Bus object` or
`Structured`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `EntityTypeName` |
| **Type**: character vector |
| **Values**: `'Entity'` | character vector |
| **Default**: `'Entity'` |

### **Data initial value** — Specify the initial value of anonymous entity data `0` (default) | scalar | vector | matrix

Set the anonymous entity data initial value. This value cannot be of type
int64 or fixed-point.

#### Dependencies

This parameter is visible when you set **Entity
type** to `Anonymous`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `DataInitialValue` |
| **Type**: character vector |
| **Values**: `'0'` | scalar | vector | matrix |
| **Default**: `'0'` |

### **Attribute Name** — Define the name of the generated entity attribute `Attribute1` (default) | character vector

Define entity attribute name.

**Note**

When done, you can export the structured entity type as a bus
object, with the name **Entity type name**, to the
base workspace. Export the bus object when using the MATLAB
Discrete-Event System and Discrete Event
Chart blocks.

#### Dependencies

This parameter is visible when **Entity type** is set
to `Structured`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `AttributeName` |
| **Type**: character vector |
| **Values**: `'Attribute1'` | character vector |
| **Default**: `'Attribute1'` |

### **Attribute Initial Value** — Define the generated entity attribute initial value `1` (default) | scalar

Specify the entity attribute initial value. This parameter is visible when
**Entity type** is set to
`Structured`. This value can not be of type
fixed-point.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `AttributeInitialValue` |
| **Type**: character vector |
| **Values**: `1` | scalar |
| **Default**: `'1'` |

### **Event actions** — Specify the behavior of the entity on certain events `Generate` (default) | `Exit`

Define the behavior in the **Event action** parameter.
The `Generate` action is called when an entity is generated
and the `Exit` action is called just before an entity exits
the block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `GenerateAction, ExitAction` |
| **Type**: character vector |
| **Values**: MATLAB code |
| **Default**: `''` |

### **Number of entities departed, d** — Outputs the number of entities that have departed the block `off` (default) | `on`

Number of entities that have departed the block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumberEntitiesDeparted` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Pending entity present in block, pe** — Pending entities `off` (default) | `on`

Indicates whether an entity that is yet to depart is present in the block.
The value is `1` for a pending entity, and
`0` otherwise. This block can have at most one pending
entity because its storage capacity is one. If there is an existing pending
entity, the block does not generate another entity until the pending entity
departs the block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PendingEntityInBlock` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Average intergeneration time, w** — Average time between generation of entities `off` (default) | `on`

Outputs the average time between generation of entities. **Average
intergeneration time, w** is the ratio of the total generation
time to the total number of generated entities.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `AverageIntergenerationTime` |
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

Generate entities

The Entity Generator block generates entities. Entities are discrete
items of interest that you can define in a discrete-event simulation. An entity can
carry scalar, bus, or vector data. The meaning of an entity depends on the model.
Entity can represent customers in a queuing system, data packets from a remote
controller to an actuator, or any discrete item you define.

By default the block entity generation method is
`Time-based`. In this method, the block generates entities
using intergeneration times specified by the **Period**, from an input
signal or statistical distribution. See Entities in a SimEvents Model, for more information about creating
time-based and randomized entities.

The block also creates event-based entities. Choose
`Event-based` as the **Generation Method**
for an external event to specify the entity intergeneration time. For an example, see
Generate Entities When Events Occur.

To customize actions when the entity is generated or it exits the block, in the
**Event actions** tab, in the `Generate action`,
or `Exit action` field, enter MATLAB® code. For more information, see Events and Event Actions.
