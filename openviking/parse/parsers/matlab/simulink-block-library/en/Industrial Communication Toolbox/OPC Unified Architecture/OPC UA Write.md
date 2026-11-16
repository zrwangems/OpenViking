---
type: simulink-block
title: 'OPC UA Write'
family: 'icomm'
product_id: 'icomm'
product_name: 'Industrial Communication Toolbox'
documentation_release: R2025b
official_category: 'OPC Unified Architecture'
documentation_page: 'opcuawrite'
documentation_source_path: 'ug/opcuawrite.html'
language: en
---

# OPC UA Write

## Ports

### Input

### **Value** — Vector of node values vector

Values to write to OPC UA server nodes. The number of
input ports corresponds to the number of nodes you select
in the **Nodes** parameter.

For more information on the data types supported at the
**Value** port, see OPC UA Server Data Types.

#### Dependencies

To enable this port, specify one or more nodes in
the **Nodes** parameter.

**Data Types:** `Boolean` | `single` | `double` | `datetime` | `duration` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint8 vector` | `uint16` | `uint32` | `uint64` | `struct` | `char vector`

## Parameters

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

Select nodes to write to the specified server.

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
  the block inputs the signals at the input
  ports.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NodeList` |
| **Type:** `string` | `character vector` |

### **Sample time** — Sample time for write operation -1 (default) | nonnegative scalar

Define the sample time of the block in seconds. The block writes
the data to the server synchronously at the specified sample
time. You can specify `0` for continuous mode,
or `-1` to inherit the sample time of the block
connected to the input of the OPC UA Write block.
For more information, see Specify Sample Time (Simulink).

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

Write data to OPC UA server

The OPC UA Write block writes data to one or more nodes on an OPC
Unified Architecture (UA) server. The write operation takes place synchronously at
a specified sample time.

Each input port writes data to a corresponding node in the
**Nodes** list of the OPC UA Write block.
Each node can accept data of different data types.

**Note**

You need a license for Industrial Communication Toolbox™ and Simulink® to use this block.

**Note**

You must connect at least one OPC UA server to use the OPC UA Read block.
You can create an OPC UA client using the **OPC
Configuration** pane in the Configuration Parameters dialog
box of the model. You must add at least one OPC UA
Read or OPC UA Write block in the model to enable this pane.
For more information, see Configure OPC UA Client in Simulink.
