---
type: simulink-block
title: 'OPC UA Read'
family: 'icomm'
product_id: 'icomm'
product_name: 'Industrial Communication Toolbox'
documentation_release: R2025b
official_category: 'OPC Unified Architecture'
documentation_page: 'opcuaread'
documentation_source_path: 'ug/opcuaread.html'
language: en
---

# OPC UA Read

## Ports
```yaml
ports:
- name: Value
  summary: Current data values of selected nodes scalar | bus
  direction: output
  data_types: Boolean | single | double | datetime | int8 | int16 | int32 | int64 | uint8 | uint8 vector | uint16 | uint32
    | uint64 | struct | char vector | bus
- name: Timestamp
  summary: Timestamp of selected nodes data seconds (default) | date number
  direction: output
  data_types: double
- name: Quality
  summary: Quality of read data from selected nodes boolean
  direction: output
  data_types: Boolean
```

### Output

### **Value** — Current data values of selected nodes scalar | bus

The block outputs the values of the selected nodes as one
of these:

- A scalar Simulink signal when you select a
  single node. The signal has the same data type as
  the selected node.
- A Simulink bus signal when you select
  multiple nodes. Each signal in the bus inherits
  the data type of its corresponding node. Extract
  the value of a node from the Simulink bus signal
  using a Bus Selector (Simulink) block.

For more information on the data types supported at the
**Value** port, see OPC UA Server Data Types.

#### Dependencies

To enable this port, specify one or more nodes in
the **Nodes** parameter.

**Data Types:** `Boolean` | `single` | `double` | `datetime` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint8 vector` | `uint16` | `uint32` | `uint64` | `struct` | `char vector` | `bus`

### **Timestamp** — Timestamp of selected nodes data seconds (default) | date number

The block outputs the timestamp of the selected nodes data
as one of these values:

- `Seconds since start`
  (default): Represents the simulation time at which
  the Simulink client received data from the
  server.
- `Serial date number`:
  Represents the real-world time at which the source
  provided data to the server.

#### Dependencies

To enable this port, select the **Show
timestamp port** parameter.

**Data Types:** `double`

### **Quality** — Quality of read data from selected nodes boolean

The block outputs the quality of read data from selected
nodes as Boolean values. A logical `0`
output indicates `'Bad'` or
`'Uncertain'` quality and logical
`1` indicates
`'Good'` quality. For details on
the quality format, see OPC UA Quality.

#### Dependencies

To enable this port, select the **Show
quality port** parameter.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters:
- name: Server
  summary: Define OPC UA server for block drop-down list
  group: ''
  block_parameter: ServerList
  type: string | character vector
- name: Nodes
  summary: List of OPC UA server nodes table
  group: ''
  values: port.
  block_parameter: NodeList
  type: string | character vector
- name: Show quality port
  summary: Add quality output to block on (default) | off
  group: ''
  block_parameter: ShowQualityPort
  type: string | character vector
  values: '''on'' | ''off'''
  default: '''on'''
- name: Show timestamp port
  summary: Add timestamp output to block on (default) | off
  group: ''
  block_parameter: ShowTimestampPort
  type: string | character vector
  values: '''on'' | ''off'''
  default: '''on'''
- name: Show timestamp port as
  summary: Set timestamp basis Seconds since start (default) | Serial date number
  group: ''
  block_parameter: ShowTimestampPortAs
  type: string | character vector
  values: '''Seconds since start'' | ''Serial date number'''
  default: '''Seconds since start'''
- name: Sample time
  summary: Sample time for read operation -1 (default) | nonnegative scalar
  group: ''
  block_parameter: SampleTime
  type: string | character vector
  values: nonnegative scalar
  default: '''-1'''
```

### **Server** — Define OPC UA server for block drop-down list

Select the OPC UA client to associate with the block.

- To add the required clients using
  the **OPC configuration** pane,
  click **Configure servers**. For
  more information, see Configure OPC UA Client in Simulink.
- To update the block to the latest OPC
  configuration, click
  **Refresh**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ServerList` |
| **Type:** `string` | `character vector` |

### **Nodes** — List of OPC UA server nodes table

Select nodes to read from the specified server.

- To add variable type nodes, click
  **Add**. This action opens the
  Browse Namespace dialog box for the selected OPC
  UA server. Using this browser, you can select the
  nodes that you want to add to the
  **Nodes** list.
- To delete selected nodes, click
  **Delete**.
- To change the order of the selected nodes in
  the list, click **Move Up** or
  **Move Down**. The serial
  number of the nodes determines the order in which
  the block outputs the signals in the bus at the
  **Value** port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NodeList` |
| **Type:** `string` | `character vector` |

### **Show quality port** — Add quality output to block on (default) | off

When you select this parameter, the block outputs the quality of the read data at the
**Quality** port, as a Boolean value. A
quality value of `'good'` is indicated by
logical `1` and a value of either
`'bad'` or `'uncertain'`
is indicated by a logical `0`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowQualityPort` |
| **Type:** `string` | `character vector` |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Show timestamp port** — Add timestamp output to block on (default) | off

When you select this parameter, the block outputs the timestamps
of the selected nodes data at the **Timestamp**
port, as a vector of doubles. You can select the timestamp basis
using the Show
timestamp port as parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowTimestampPort` |
| **Type:** `string` | `character vector` |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Show timestamp port as** — Set timestamp basis `Seconds since start` (default) | `Serial date number`

Set the timestamp basis as `Seconds since
start` or `Serial date
number`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowTimestampPortAs` |
| **Type:** `string` | `character vector` |
| **Values:** `'Seconds since start'` | `'Serial date number'` |
| **Default:** `'Seconds since start'` |

### **Sample time** — Sample time for read operation -1 (default) | nonnegative scalar

Define the sample time of the block in seconds. The block reads
the data from the server synchronously at the specified sample
time. For more information, see Specify Sample Time (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |
| **Type:** `string` | `character vector` |
| **Values:** nonnegative scalar |
| **Default:** `'-1'` |
## Libraries

Industrial Communication Toolbox / OPC Unified Architecture

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

## Description

Read data from OPC UA server

The OPC UA Read block reads data from one or more nodes on an OPC Unified
Architecture (UA) server. The read operation takes place synchronously at a
specified sample time.

The block outputs the values of the selected nodes as a Simulink® bus signal. It optionally outputs the timestamps and the quality
value associated with each node in separate outputs. The nodes that you select in
the block can have different data types, which remain unchanged in the Simulink
bus signal. The block outputs the timestamp as a serial date number (real-world
time), or as the number of seconds from when you start simulating the model
(simulation time).

**Note**

You need a license for Industrial Communication Toolbox™ and Simulink to use this block.

**Note**

You must connect at least one OPC UA server to use the OPC UA Read block.
You can create an OPC UA client using the **OPC
Configuration** pane in the Configuration Parameters dialog
box of the model. You must add at least one OPC UA Read or OPC UA
Write block in the model to enable this pane. For more
information, see Configure OPC UA Client in Simulink.
