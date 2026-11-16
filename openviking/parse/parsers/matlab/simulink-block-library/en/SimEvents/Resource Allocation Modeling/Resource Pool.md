---
type: simulink-block
title: 'Resource Pool'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: 'Resource Allocation Modeling'
documentation_page: 'resourcepool'
documentation_source_path: 'ref/resourcepool.html'
language: en
---

# Resource Pool

## Ports

### Input

### **Port\_1** — Change resource amount scalar | vector | matrix

Input entity port for changing resource amount. The input cannot be a
negative value.

#### Dependencies

To enable this port, select the `Change amount through
control port` as the **Resource amount
source**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_u** — Outputs the number of resources that are in use scalar

Number of resources that are in use.

#### Dependencies

To enable this port, click the **Statistics** tab
and select the box labeled **Amount in use,
u**.

**Data Types:** `double`

### **Port\_util** — Outputs the average time the pool is utilized scalar

Average wait time the pool is utilized.

#### Dependencies

To enable this port, click the **Statistics** tab
and select the box labeled **Average utilization,
util**.

**Data Types:** `double`

### **Port\_avail** — Outputs the number of resources that are available scalar

Number of resources that are available.

#### Dependencies

To enable this port, click the **Statistics** tab
and select the box labeled **Amount available,
avail**.

**Data Types:** `double`

## Parameters

### **Resource name** — Name for the resources in the pool `Resource1` (default) | character vector

Enter name of entity resource.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ResourceName` |
| **Type**: character vector |
| **Values**: `'Resource1'` | character vector |
| **Default**: `'Resource1'` |

### **Resource granularity** — Select granularity of resource use `Discrete unit` (default) | `Fractional amount`

Select granularity of resource use.

- `Discrete unit` — Use whole number
  increment.
- `Fractional amount` — Use
  fractional increment.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ResourceGranularity` |
| **Type**: character vector |
| **Values**: `'Discrete unit'` | `'Fractional amount'` |
| **Default**: `'Discrete unit'` |

### **Reusable upon release** — Specify if the resource is reusable upon release `off` (default) | `on`

- Select this check box to allow this resource to return to the
  resource pool upon release. An example of such a resource is a
  table in a restaurant, which is available for reuse when a
  customer leaves.
- Clear this check box to prevent this resource from returning
  to the resource pool upon release. In this case, when the
  resource is released, it is no longer available in the resource
  pool. An example of such a resource is food in a restaurant,
  which is not reusable upon consumption.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ReusableUponRelease` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Resource amount source** — Select resource amount source `Dialog` (default) | `Change amount through control port`

Select resource amount source.

- `Dialog`
- `Change amount through control
  port`

  Select this option to enable an input entity port and a variable
  capacity resource. The payload of the arriving message increments
  the existing number of resources for the block. For example, if the
  resource pool has five resources, and a message with a payload of
  three arrives at the input port, the block has eight resources
  available. The number of resources cannot decrement.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ResourceAmountSource` |
| **Type**: character vector |
| **Values**: `'Dialog'` | `'Change amount through control port'` |
| **Default**: `'Dialog'` |

### **Resource amount** — Set the amount of resource `10` (default) | scalar

Enter amount of resource.

#### Dependencies

Select the `Dialog` to enable the
**Resource amount source**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ResourceAmount` |
| **Type**: character vector |
| **Values**: `'10'` | scalar |
| **Default**: `'10'` |

### **Initial resource amount** — Enter initial amount of resource `10` (default) | scalar

Enter initial amount of resource.

#### Dependencies

Select the `Change amount through control
port` to enable the **Resource amount
source**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InitialResourceAmount` |
| **Type**: character vector |
| **Values**: `'10'` | scalar |
| **Default**: `'10'` |

### **Resource visibility** — Select the availability of the resources `Global` (default) | `Scoped`

Choose the behavior of the resources acquired from this pool as
`Global` or
`Scoped`.

When `Global` is selected:

- Resource pool names must be unique in the model.
- All resources have global scope and they can be referenced
  from anywhere in a model hierarchy.
- An entity carrying a resource acquired from this block, must
  explicitly relinquish the resource.
- When an entity is destroyed, the resources that are associated
  with it are returned to the pool, if the **Reusable upon
  release** check box is selected.

When `Scoped` is selected:

- Resources are locally visible and can be referenced only from
  the subsystem that contains the Resource Pool
  block and all the subsystems inside.
- Resource pool names must be unique within the model hierarchy
  where the Resource Pool block is visible.
- An entity carrying the resource acquired from this block, must
  explicitly relinquish the resource.
- When an entity leaves the scope, any resources that are local
  to that scope and not already released, are automatically
  released. If **Reusable upon release** check
  box is selected, they are returned to the pool.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InitialResourceAmount` |
| **Type**: character vector |
| **Values**: `'10'` | scalar |
| **Default**: `'10'` |

### **Amount in use, u** — Number of resources that are in use `off` (default) | `on`

Outputs the amount of resources that the block has acquired and has not
yet released. For example, if the resource pool has `10`
resources, and the entity acquires all of them, this port shows
`10`. When the block releases the resources, this port
shows `0`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `AmountInUse` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Average utilization, util** — Outputs the average resource utilization `off` (default) | `on`

Outputs the average resource utilization.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `AverageUtilization` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Amount available, avail** — Outputs the amount of resources available `off` (default) | `on`

Outputs the amount of resources available.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `AmountAvailable` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

## Libraries

SimEvents / Entity Management SimEvents

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016a**

## Description

Pool entity resources

The Resource Pool block defines resources that entities can use during
model simulation. Use the Resource Acquirer and Resource
Releaser blocks to work with these resources.

Initialize the block with the specified amount of available resources. Then:

- Use one or more Resource Acquirer blocks to reserve those
  resources.
- Use a Resource Releaser block to return resources back to this
  block for future use.

You can determine the visibility of available resources in a model hierarchy. You can
choose `Global` or `Scoped` resources
in the pool.

- `Global` — Resources can be referenced from anywhere
  in a model hierarchy.
- `Scoped` — Resources are locally visible and can be
  referenced only from the subsystem that contains the Resource
  Pool block and all the subsystems inside.
