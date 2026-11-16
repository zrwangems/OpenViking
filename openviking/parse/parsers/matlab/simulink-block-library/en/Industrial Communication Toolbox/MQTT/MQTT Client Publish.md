---
type: simulink-block
title: 'MQTT Client Publish'
family: 'icomm'
product_id: 'icomm'
product_name: 'Industrial Communication Toolbox'
documentation_release: R2025b
official_category: 'MQTT'
documentation_page: 'mqttclientpublish'
documentation_source_path: 'ug/mqttclientpublish.html'
language: en
---

# MQTT Client Publish

## Ports

### Input

### **Topic\_*`x`*** — Messages to publish to MQTT topics double

Messages to publish to MQTT topics. The number of input ports corresponds to the
number of topics you add in the Topics to publish parameter. The block
publishes messages to topics when the input data changes. You can toggle this setting
using the Publish only on input data change parameter.

#### Dependencies

To enable this port, specify one or more topics in the **Topics to
publish** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string`

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

### **Topics to publish** — List of MQTT topics table

Add topics to publish.

- To add a topic, click **Add**. This action adds a row in
  the **Topics to publish** table with `QoS` and
  `Retain` set to the default values of `0` and
  `off`, respectively. You must specify a topic name for the
  client to publish to in the `Topic name` column. Each time you
  click **Add**, the block adds a new row in the **Topics
  to publish** table and increments the serial number by 1.

  - `Sl`
    `no`: This field is noneditable and specifies the serial
    number of the topic. The serial number determines the order in which the
    block receives the signals at the input ports.
  - `Topic name`: This is an editable text field that
    specifies the name of the topic. This field also defines the names for the
    input ports.
  - `QoS`: This field specifies the quality of service
    (QoS) for message delivery. You can set this field to one of the values in
    the drop-down list:

    - `0` : To deliver messages at most once and not
      more
    - `1` : To deliver messages at least once and not
      less
    - `2` : To deliver messages exactly once, not more
      or less
  - `Retain`: This field specifies whether the broker
    retains a message for new subscribers to the topic. Select this check box to
    retain the message.
- To delete topics, select the topics and click
  **Delete**.

**Note**

Topic names that begin with the `$` character are not supported
for publishing messages. These topics are reserved exclusively for server-side
implementations and should not be used by clients.

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

### **Publish only on input data change** — Determines when to publish messages on (default) | off

When you select this parameter, the block publishes messages to topics only when
there is a change in input data.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `PublishOnDataChange` |
| **Values:** | on (default) | off |
| **Data Types:** | `character vector` | `string` |

### **Block sample time** — Sample time for read operation -1 (default) | nonnegative scalar

Define the sample time of the block in seconds. The block publishes messages to the
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

Publish messages to MQTT Topics

The MQTT Client Publish block publishes messages to one or more MQTT topics.

Each input port publishes messages to a corresponding MQTT topic specified in the
**Topics to publish** parameter.

**Note**

You need a license for Industrial Communication Toolbox™ and Simulink® to use this block.

**Note**

You must associate the MQTT Client Publish block with an MQTT Client. You can create the
client to connect to the MQTT broker using the **MQTT** pane in the
Configuration Parameters dialog box of the model. You must add at least one MQTT Client
Subscribe or MQTT Client Publish block in the model to enable this pane. For more
information, see Configure MQTT Client in Simulink.
