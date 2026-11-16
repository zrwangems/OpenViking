---
type: simulink-block
title: 'MQTT Client Subscribe'
family: 'icomm'
product_id: 'icomm'
product_name: 'Industrial Communication Toolbox'
documentation_release: R2025b
official_category: 'MQTT'
documentation_page: 'mqttclientsubscribe'
documentation_source_path: 'ug/mqttclientsubscribe.html'
language: en
---

# MQTT Client Subscribe

## Ports

### Output

### **Topic\_*`x`*** — Current messages from subscribed topics vector

Messages read from subscribed MQTT topics. The number of output ports corresponds
to the number of topics you add in the Topics to subscribe parameter. The block
outputs messages from all the subscribed topics at the specified sample time. The
block holds the previous message at this port until a new message is available.

#### Dependencies

To enable this port, specify one or more topics in the **Topics to
subscribe** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string`

### **IsNew** — Flag indicating if read message is new `0` | `1` | vector of logicals

This port returns logical `1` to indicate that the read message
is new. When the block reads multiple messages, the port returns a vector of logicals.
For example, if the block is subscribed to three topics and the **IsNew**
port returns a vector [ 0, 0, 1], the output indicates that the message read from the
third topic is new.

#### Dependencies

To enable this port, specify one or more topics in the **Topics to
subscribe** parameter.

**Data Types:** `Boolean`

## Parameters

### **Client** — Select MQTT client drop-down list

Select the MQTT client to associate with the block. The block updates the
**Broker address** parameter once you select a client.

- To add the clients using the **MQTT** pane, click
  **Configure clients**. For more information, see Configure MQTT Client in Simulink.
- To update the client list and to show the latest MQTT clients, click
  **Refresh**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `ClientList` |
| **Values:** | MQTT client name |
| **Data Types:** | `character vector` | `string` |

### **Topics to subscribe** — List of MQTT topics table

Add topics to subscribe.

- To add a topic, click **Add**. This action adds a row in
  the **Topics to subscribe** table with `Output data
  type` and `QoS` set to the default values of
  `double` and `0`, respectively. You must
  specify a topic name for the client to subscribe to in the `Topic
  name` column. Each time you click **Add**, the block
  adds a new row in the **Topics to subscribe** table and
  increments the serial number by 1.

  - `Sl`
    `no`: This field is noneditable and specifies the serial
    number of the topic. The serial number determines the order in which the
    block outputs the signals at the output ports.
  - `Topic name`: This is an editable text field that
    specifies the name of the topic. This field also defines the names for the
    output ports.
  - `Output data type`: This field specifies the data type
    of the block output. You can set this field to one of the values in the
    drop-down list: `int8`, `uint8`,
    `int16`, `uint16`,
    `int32`, `uint32`,
    `int64`, `uint64`,
    `single`, `double`, or
    `string`. The block parses messages read from the
    corresponding topic to the selected data type.
  - `QoS`: This field specifies the quality of service
    (QoS) for message delivery. You can set this field to one of the values in
    the drop-down list:

    - `0` : To deliver messages at most once and not
      more
    - `1` : To deliver messages at least once and not
      less
    - `2` : To deliver messages exactly once, not more
      or less
- To delete topics, select the topics and click
  **Delete**.

**Note**

- The MQTT Client Subscribe block does not support topic names with wildcard
  characters.
- When you set `Output data type` for this block to
  `string`, you must configure Simulink to use a fixed-step discrete solver. To configure the solver, open
  the Configuration Parameters dialog box, navigate to the **Solver
  selection** section of the **Solver** pane, and set
  **Type** to `Fixed-step` and**Solver** to `discrete`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `TopicsTable` |
| **Values:** | MQTT topic name and information |
| **Data Types:** | `character vector` | `string` |

### **Block sample time** — Sample time for read operation -1 (default) | nonnegative scalar

Define the sample time of the block in seconds. The block reads messages from the
MQTT topic synchronously at the specified sample time. For more information, see Specify Sample Time (Simulink).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | -1 (default) | nonnegative scalar |
| **Data Types:** | `double` |

## Libraries

Industrial Communication Toolbox / MQTT

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2025a**

## Description

Read messages from subscribed MQTT topics

The MQTT Client Subscribe block subscribes to MQTT topics specified in the
**Topics to subscribe** parameter. The block reads messages from these
topics and returns the messages at the corresponding output ports. The read operation takes
place synchronously at the specified sample time.

The **IsNew** port outputs a Boolean value or vector of Boolean values depending
on the number of subscribed topics. The Boolean values indicate if a new message is available
in the corresponding topic.

**Note**

You need a license for Industrial Communication Toolbox™ and Simulink® to use this block.

**Note**

You must associate the MQTT Client Subscribe block with an MQTT Client. You can create
the client to connect to the MQTT broker using the **MQTT** pane in the
Configuration Parameters dialog box of the model. You must add at least one MQTT Client
Subscribe or MQTT Client Publish
block in the model to enable this pane. For more information, see Configure MQTT Client in Simulink.
