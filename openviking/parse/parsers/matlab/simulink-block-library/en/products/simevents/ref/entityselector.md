---
type: simulink-block
title: 'Entity Selector'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: 'Queue, Service, and Route Modeling / Route Entities and Simulink Messages'
documentation_page: 'entityselector'
documentation_source_path: 'ref/entityselector.html'
language: en
---

# Entity Selector

## Ports

### Input

### **Key** — Incoming reference entity scalar | vector | matrix

Input entity port for reference entities entering the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_1** — Incoming entity scalar | vector | matrix

Input entity port for matching entities entering the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
### Output

### **Port\_1** — Exiting reference entity scalar | vector | matrix

Output entity port for reference entities exiting the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_2** — Exiting matched entity scalar | vector | matrix

Output entity port for matching entities exiting the selector.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_d** — Number of entities that have departed the block scalar

Number of entities that have departed the block.

#### Dependencies

To enable this port, click **Statistics** and select the **Number of entities departed, d** check box.

**Data Types:** `double`

### **Port\_n** — Number of entities that have not yet departed the block scalar

Number of entities that have not yet departed the block.

#### Dependencies

To enable this block, click **Statistics** and select the **Number of entities in block, n** check box.

**Data Types:** `double`

### **Port\_ex** — Number of entities extracted scalar

Number of entities that are pulled out of this block.

#### Dependencies

To enable this port, click the **Statistics** tab
and select the box labeled **Number of entities extracted,
ex**.

**Data Types:** `double`

## Parameters

### **Number of matching streams** — Determine how many input entity streams the block accepts `1` (default) | numerical

Specify the number of entity streams to be matched to the reference
entity. The block can accept at most `8` matching
streams.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `mNumberOfStreams` |
| **Type**: character vector |
| **Values**: `'1'` | scalar |
| **Default**: `'1'` |

### **Key entity attribute Name** — Specify name of reference attribute `{'ID'}` (default) | character vector

Name of the reference attribute that is used to evaluate a match.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `mKeyEntityAttributeName` |
| **Type**: character vector |
| **Values**: `'{'ID'}'` | character vector |
| **Default**: `'{'ID'}'` |

### **Matching entity attribute name(s)** — Specify name of selected attribute names `{'Type'}` (default) | character vector

Name of the matching entity attribute that is used to evaluate a match.
You can specify one attribute name, or an array of attribute names that are
compared with the key value to evaluate a match.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `mEntityAttributeName` |
| **Type**: character vector |
| **Values**: `'{'Type'}'` | character vector |
| **Default**: `'{'Type'}'` |

### **Number of entities source** — Source to determine the number of entities to be matched `Dialog` (default) | `Attribute`

Source that determines the number of entities to be selected from each
stream.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `mMatchingNumberSource` |
| **Type**: character vector |
| **Values**: `'Dialog'` | `'Attribute'` |
| **Default**: `'Dialog'` |

### **Number of entities to select** — Number of entities to select from each of the incoming entity streams `1` (default) | scalar

Number of entities to be selected from each matching stream. You can
specify `0`, a positive integer, or an array of positive
integers to determine the number of entities to select from each matching
entity stream.

#### Dependencies

To enable this parameter, set the **Number of entities
source** parameter to
`Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `mNumberOfMatches` |
| **Type**: character vector |
| **Values**: `'1'` | scalar |
| **Default**: `'1'` |

### **Key attribute for number of entities** — Key attribute name that determines the number of entities to be matched `Name` (default) | character vector

The name of the key attribute that determines the number of entities to be
selected from each matching stream. The attribute value can be an integer or
an array of integers of size equal to the number of incoming entity
streams.

#### Dependencies

To enable this parameter, set the **Number of entities
source** parameter to
`Attribute`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `mNumberOfMatchesAttribute` |
| **Type**: character vector |
| **Values**: `'Name'` | character vector |
| **Default**: `'Name'` |

### **Number of entities departed, d** — Outputs the number of entities that have departed the block `off` (default) | `on`

Number of entities that have exited the block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `mNumEntitiesDepOpt` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Number of entities in block, n** — Outputs the number of entities present in the block, which have yet to depart `off` (default) | `on`

Number of entities present in the block, which have yet to depart.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `mNumEntitiesInBlockOpt` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Number of entities extracted, ex** — Outputs the number of entities extracted from the block `off` (default) | `on`

Outputs the number of extracted entities which are pulled out from this
block by the Entity Find block. If a key entity is extracted,
the Entity Selector block waits until all the matching
entities arrive at the block. Then, the matching entities depart from the
corresponding output port. If a matching entity is extracted, the block
looks for another matching entity. When an entity is extracted,
**Number of entities departed, d**, and
**Number of entities in block, n** statistics are
updated accordingly.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `mNumEntitiesExtractedOpt` |
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

Select entities

The Entity Selector block selects entities from multiple streams of
ready-to-leave entities, and matches them to a reference entity. You can use this block
for modeling scenarios which involve items to be matched based on input. For instance,
you can model a facility that produces parts which are matched to the corresponding
order.

The block first accepts a reference entity with its **Key entity attribute
name**. Then the block selects a matching entity with **Matching
entity attribute name(s)** from each of the other input ports accepting
incoming entities. The match is based on the equality of the specified attribute values.
When a match is found across all the entity streams, the set of matching entities and
the key entity become ready to depart.

The Entity
Store block can be used as a temporary container for entities to be selected
by the Entity Selector block. For an example, see Match Entities Based on Attributes.
