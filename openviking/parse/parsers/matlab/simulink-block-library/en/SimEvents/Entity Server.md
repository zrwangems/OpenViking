---
type: simulink-block
title: 'Entity Server'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'entityserver'
documentation_source_path: 'ref/entityserver.html'
language: en
---

# Entity Server

## Ports

### Input

### **Port\_1** — Input entity scalar | vector | matrix

Input entity that carries scalar, bus, or vector data to enter the
server.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `string` | `fixed point`

### **Port\_2** — Input signal port for service time source scalar

Input signal port to determine service time.

#### Dependencies

This port is visible when **Service time source**
is set to `Signal port`.

**Data Types:** `double`
### Output

### **Port\_1** — Output entity scalar | vector | matrix

Output entity port for entities exiting the server.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `string` | `fixed point`

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

### **Port\_pe** — Pending entity in block off (default) | on

Selecting this check box outputs the value `1` for a
pending entity in the block, and `0` otherwise.

#### Dependencies

To enable this port, select the **Statistics** > **Pending entity in block, pe**.

**Data Types:** `double`

### **Port\_np** — Number of pending entities off (default) | on

Selecting this check box outputs the number of pending entities in the
block.

#### Dependencies

To enable this port, select the **Statistics** > **Number of pending entities, np**.

**Data Types:** `double`

### **Port\_w** — Average wait time for entities in the block scalar

Average wait time for entities in the block.

#### Dependencies

To enable this port, click the **Statistics** tab
and select the box labeled **Average wait,
w**.

**Data Types:** `double`

### **Port\_util** — Outputs the average time the server is occupied scalar

Average time the server is occupied.

#### Dependencies

To enable this port, click the **Statistics** tab
and select the box labeled **Utilization,
util**.

**Data Types:** `double`

### **Port\_p** — Outputs the number of preempted entities scalar

Number of preempted entities.

#### Dependencies

To enable this port, first click the
**Preemption** tab, then click
**Statistics** tab and select the box labeled
**Number of entities preempted, p**.

**Data Types:** `double`

### **Port\_ex** — Number of entities extracted scalar

Number of entities that are pulled out of this block.

#### Dependencies

To enable this port, click the **Statistics** tab
and select the box labeled **Number of entities extracted,
ex**.

**Data Types:** `double`

## Parameters

### **Capacity** — Specify the capacity of the server `1` (default) | scalar

Specify the number of entities the block can serve simultaneously.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Capacity` |
| **Type**: character vector |
| **Values**: `'1'`| scalar |
| **Default**: `'1'` |

### **Service time source** — Choose the source to specify the service time `Dialog` (default) | `Signal port` | `Attribute` | `MATLAB action`

Determine the source that specifies the service time.

You can select:

- `Dialog`

  Enter the constant value in the **Service time
  value** parameter.
- `Signal port`

  Connect a time source to the resulting signal port.
- `Attribute`

  Enter the name of the attribute that contains data to be
  interpreted as service.
- `MATLAB action`

  In the **Service time action** section, enter
  MATLAB code to vary the service time. Assign the variable
  *dt*, which the model uses as service
  time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ServiceTimeSource` |
| **Type**: character vector |
| **Values**: `'Dialog'` | `'Signal port'` | `'Attribute'`| `'MATLAB action'` |
| **Default**: `'Dialog'` |

### **Service time attribute name** — Specify service time source attribute name `ServiceTime` (default) | character vector

Determine the name of the attribute that is used as the service time
value.

#### Dependencies

This parameter is visible when **Service time
source** is set to
`Attribute`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ServiceTimeAttributeName` |
| **Type**: character vector |
| **Values**: `'ServiceTime'` | character vector |
| **Default**: `'ServiceTime'` |

### **Service time value** — Specify the value of the service time `1` (default) | scalar

**Tunable:** Yes

#### Dependencies

This parameter is visible when **Service time
source** is set to
`Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ServiceTimeValue` |
| **Type**: character vector |
| **Values**: `'1.0'` | scalar |
| **Default**: `'1.0'` |

### **Service time action** — Specify service time `dt = rand(1,1)` (default) | MATLAB code

Use MATLAB code to specify service time. `dt` specifies
the service time. You can manually specify `dt` or use
**Insert pattern** button to specify service time from
a repeating sequence or from a distribution. For an example, see Count Simultaneous Departures from a Server.

#### Dependencies

This parameter is visible when **Service time
source** is set to `MATLAB
action`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ServiceTimeAction` |
| **Type**: character vector |
| **Values**: MATLAB code |
| **Default**: `'dt = rand(1,1);'` |

### **Event action** — Specify the behavior of the entity in certain events `Entry` (default) | `Service complete` | `Exit` | `Blocked` | `Preempt`

Specify the behavior of the entity in certain events. Define the behavior
in the **Event action** parameter. The
**Entry** and the **Exit** actions are
called just after the entity entry and just before entity exit. The
**Service complete** action is called after the
completion of the entity service. The **Blocked** action is
called after an entity is blocked. The **Preempt** is
called after the preemption.

**Note**

If an event action changes an entity, related block behavior such
as resorting a priority queue, and rescheduling of any events, will
occur after the event action has fully finished and returned.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `EntryAction, ServiceCompleteAction, ExitAction, BlockedAction, PreemptAction` |
| **Type**: character vector |
| **Values**: MATLAB code |
| **Default**: `''` |

### **Permit preemption based on attribute** — Enable preemption of entities `off` (default) | `on`

Select this check box if you want to allow preemption of entities.
Preemption is the replacement of an entity in a server block by an entity
that satisfies certain criteria. Selecting this check box enables these
parameters:

- **Sorting attribute name** in the
  **Preemption** tab
- **Sorting direction** in the
  **Preemption** tab
- **Write residual time to attribute** in the
  **Preemption** tab
- **Number of entities preempted, p** in the
  **Statistics** tab

For an example, see Task Preemption in a Multitasking Processor.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PermitPreemptionBasedOnAttribute` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Sorting attribute name** — Specify the name of the attribute used to determine the priority `entity` | `entitySys.priority` | character vector

Specify the name of the attribute used to determine the priority.

#### Dependencies

This parameter is visible when the **Permit preemption based
on attribute** box is selected.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SortingAttributeName` |
| **Type**: character vector |
| **Values**: `'entity'` | `'entitySys.priority'` | character vector |
| **Default**: `'entity'` |

### **Sorting direction** — Choose the direction of sorting the entities `Ascending` (default) | `Descending`

Specify if the entities are sorted in `ascending`
or `descending` order.

- `ascending` — Sorting entities with
  smaller key values to have a higher priority
- `descending` — Sorting entities with
  greater key values to have a higher priority

#### Dependencies

This parameter is visible when the **Permit preemption based
on attribute** box is selected.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SortingDirection` |
| **Type**: character vector |
| **Values**: `'Ascending'` | `'Descending'` |
| **Default**: `'Ascending'` |

### **Write residual time to attribute** — Save the residual service time from a preempted entity to an attribute `off` (default) | `on`

#### Dependencies

This parameter is visible when the **Permit preemption based
on attribute** box is selected.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `WriteResidualTimeToAttribute` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Residual time attribute name** — Specify the name of the attribute to contain the residual service time of a preempted entity `ResidualTime` (default) | character vector

#### Dependencies

This parameter is visible when the **Write residual time to
attribute** box is selected.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ResidualTimeAttributeName` |
| **Type**: character vector |
| **Values**: `'ResidualTime'` | character vector |
| **Default**: `'ResidualTime'` |

### **Number of entities departed, d** — Outputs the number of entities that have departed the block `off` (default) | `on`

Number of entities that have departed the block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumberEntitiesDeparted` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Number of entities in block, n** — Outputs the number of entities present in the block, that are yet to depart `off` (default) | `on`

Number of entities present in the block that are yet to depart.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumberEntitiesInBlock` |
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
| **Block Parameter**: `PendingEntityPresentInBlock` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Number of pending entities, np** — Number of Pending entities `off` (default) | `on`

Outputs the number of pending entities the block has served that are yet
to depart.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumberEntitiesPending` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Average wait, w** — Outputs the average wait time `off` (default) | `on`

Sum of the wait times for entities departed the block divided by their
total number. *Wait time* is the duration between the
Entity Server block entry and exit of an entity. For more
information, see Interpret SimEvents Models Using Statistical Analysis.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `AverageWait` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Utilization, util** — Outputs the average time the server is occupied `off` (default) | `on`

Average time the server is occupied. The block calculates this time as the
ratio of the total wait time for entities to the server capacity multiplied
by the total simulation time.

Wait time is the duration between the Entity Server block
entry and exit of an entity. Total wait time is the sum of the wait times
for entities departed the block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Utilization` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Number of entities preempted, p** — Outputs the number of preempted entities `off` (default) | `on`

Outputs the number of preempted entities. Preemption is the replacement of
an entity in a server block by an entity that satisfies certain
criteria.

#### Dependencies

This check box appears if the **Permit preemption based on
attribute** check box is selected.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumberEntitiesPreempted` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Number of entities extracted, ex** — Number of entities extracted from this block `off` (default) | `on`

Outputs the number of extracted entities which are pulled out from this
block by the Entity Find block. If an entity is being served
during the extraction, the service is terminated. If an attribute that
defines the service time and it is modified by the Entity
Find block, service time does not change. When an entity is
extracted, **Number of entities departed, d**,
**Number of entities in block, n**, **Average
wait, w**, and **Utilization, util**
statistics are updated accordingly. For more information about finding and
extracting entities, see Find and Extract Entities in SimEvents Models.

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

**Introduced in R2016a**

## Description

Serve entities

The Entity Server block serves entities as they arrive. In a
discrete-event simulation, a server stores entities for a length of time, called
*service time*, and then attempts to output the entity. During
the service period, the block is said to be *serving* the entity
that it stores. The block can serve multiple entities simultaneously and output each
entity through the output port, unless the port is blocked. When the block permits
preemption, an entity in the server can depart early through a second port.

To customize actions when entities enter, complete service, exit, and are blocked or
preempted by the block, enter MATLAB® code in the `Entry action`, `Service complete
action`, `Exit action`, `Blocked action`,
or `Preempt action` field of the **Event actions**
tab. For more information, see Events and Event Actions.
