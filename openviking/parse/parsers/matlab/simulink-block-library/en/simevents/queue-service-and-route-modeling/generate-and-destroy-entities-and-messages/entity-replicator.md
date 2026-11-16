---
type: simulink-block
title: 'Entity Replicator'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: 'Queue, Service, and Route Modeling / Generate and Destroy Entities and Messages'
documentation_page: 'entityreplicator'
documentation_source_path: 'ref/entityreplicator.html'
language: en
---

# Entity Replicator

## Ports

### Input

### **Port\_1** — Input entity scalar | vector | matrix

Input entity port for entities entering the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `string` | `fixed point`
### Output

### **Port\_1** — Output replica entity scalar | vector | matrix

Output entity port for replica entities exiting the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `string` | `fixed point`

### **Port\_2** — Output the entity that is replicated scalar | vector | matrix

Output entity port for original entities exiting the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `string` | `fixed point`

## Parameters

### **Replicas depart from** — Choose how replicas depart `Separate output ports` (default) | `Single output port`

Choose if the replicas depart from separate output ports or a single
output port.

- `Separate output ports` — Outputs one
  replica entity from each output port
- `Single output port` — Outputs all
  replicas from a single output port

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ReplicasDepartFrom` |
| **Type**: character vector |
| **Values**: `'Separate output ports'` | `'Single output port'` |
| **Default**: `'Separate output ports'` |

### **Replication amount source** — Specify source of replica number `Dialog` (default) | `Attribute`

Specify the source of replica number.

- Select `Dialog` to specify the number
  of replicas in the dialog box.
- Select `Attribute` to select an
  attribute that specifies the number of replicas.

#### Dependencies

This parameter is visible when you set **Replicas depart
from** to `Single output
port`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ReplicationAmountSource` |
| **Type**: character vector |
| **Values**: `'Dialog'` | `'Attribute'` |
| **Default**: `'Dialog'` |

### **Number of replicas** — Specify the number of replicas 1 (default) | scalar

Specify the number of replicas. If you select `Single output
port`, all replicas depart from this output port. If you
select `Separate output ports`, each replica has
its own port.

#### Dependencies

This parameter is visible when you set **Replicas depart
from** to `Separate output ports`
or `Single output port` and
**Replication amount source** to
`Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumberReplicas` |
| **Type**: character vector |
| **Values**: `'1'` | scalar |
| **Default**: `'1'` |

### **Replicate attribute name** — Specify the attribute that determines the number of replicas `ReplicateAttribute` (default) | character vector

#### Dependencies

Specify the attribute that determines the number of replicas. This
parameter is visible when you set **Replicas depart
from** to `Single output port` and
**Replication amount source** to
`Attribute`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ReplicateAttributeName` |
| **Type**: character vector |
| **Values**: `'ReplicateAttribute'` | character vector |
| **Default**: `'ReplicateAttribute'` |

### **Hold original entity until all replicas depart** — Choose how replicas depart `off` (default) | `on`

Select this check box to hold the original entity until all the replicas
have departed. The block first attempts to send all the replicas before it
sends out the original entity. Selecting this check box prevents destruction
of replica entities when they do not depart the block before the original
entity.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `HoldOriginalEntityUntilAllReplicasDepart` |
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

Replicate entities

The Entity Replicator block duplicates entities. It outputs replica
entities and can also output the original entity. The block provides an output port for
the original entity.

If the original entity departs the block before the replicas, then its replicas are
destroyed. Selecting the **Hold original entity until all replicas
depart** check box ensures that the replicas depart the block before the
original entity.

An original entity can be extracted from this by block by the Entity
Find block. If an original entity waiting in the Entity
Replicator block is extracted, all the replicas are destroyed. Only the
original entities can be extracted because the replicas can not acquire resources in
this block. For more information about finding and extracting entities, see Find and Extract Entities in SimEvents Models.
