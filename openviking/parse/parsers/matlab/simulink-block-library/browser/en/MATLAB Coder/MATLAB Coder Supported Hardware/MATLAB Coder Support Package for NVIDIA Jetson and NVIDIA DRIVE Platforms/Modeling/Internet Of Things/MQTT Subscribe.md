---
type: simulink-block
title: 'MQTT Subscribe'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Internet Of Things'
documentation_page: 'mqttsubscribe'
documentation_source_path: 'nvidia/ref/mqttsubscribe.html'
language: en
---

# MQTT Subscribe

## Ports

### Output

### **IsNew** — New message indicator `0` (default) | `1`

If the client receives a new message since the last time step, the
**IsNew** port outputs `1`. Otherwise, the port
outputs `0`.

**Data Types:** `Boolean`

### **Message** — Received message `0` (default)

The message received from the MQTT broker, specified as an
*N*-by-1 vector. *N* is the length of the message
specified by the **Message length (N)** parameter.

**Data Types:** `double`

### **Topic** — Topic of message `topic/level/#` (default)

ASCII values that correspond to the topic name of the received message. For
example, if the topic of the received message is `model/data`, the
port outputs the topic as `109 111 100 101 108 47 100 97 116 97`.

To convert the ASCII values into the alphanumeric equivalent, attach an ASCII to
String (Simulink) block to the output of the **Topic** port. For
information on topics and their structure, see Topics in MQTT.

**Note**

A topic can have a maximum of 128 characters.

#### Dependencies

The **Topic** port is available only if the
**Topic** parameter value specified in the Block Parameters
dialog box includes a wildcard entry. For information on wildcards, see Wildcards in MQTT Topics.

**Data Types:** `uint8`

## Parameters

### **Topic** — Topic for subscription `topic/level` (default) | valid topic name

Specify a topic to which the client subscribes. For information on topics and its
structure, see Topics in MQTT.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Topic` |
| **Type:** character vector |
| **Values:** `'topic/level'`|`valid topic name` |
| **Default:**  `'topic/level'` |

### **QoS** — Levels of QoS `0` (default) | `1` | `2`

Quality of Service (QoS) defines the reliability of the message delivery process in
MQTT. MQTT provides three QoS levels for message delivery: QoS 0, QoS 1, and QoS 2. The
MQTT broker that you are using might not support three levels of QoS. For example,
ThingSpeak™ MQTT supports only QoS 0.

Select a QoS level from the list:

- `0` (At most once): The MQTT broker sends the message
  to the client. The client does not send an acknowledgment of the receipt.
- `1` (At least once): The MQTT broker sends the
  message to the client at least once. The broker resends the message if it does not
  receive an acknowledgment from the client.
- `2` (Exactly once): The MQTT broker sends the message
  to the client exactly once. The broker and client exchange acknowledgments so that
  the message is received only once.

For more information on QoS levels, see Levels of QoS in MQTT.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `QoS` |
| **Type:** character vector |
| **Values:** `'0'`|`'1'`|`'2'` |
| **Default:**  `'0'` |

### **Message length (N)** — Length of message to be received `1` (default) | integer between 1 and 64 inclusive

Specify the length of the message to be received from the MQTT broker. If the length
of the received message is greater than the length specified in **Message length
(N)**, the block outputs only the first *N* characters of
the received message. If the length of the received message is less than the length
specified in **Message length (N)**, the block appends zeros to the
received message.

### **Output the last received message** — Option to view last received message on Message port `off` (default) | `on`

When you select this option, the last received message is displayed on the **Message** output port.

- For a high **isNew** output port, the new message
  is displayed on the **Message** output port.
- For a low **isNew** output port, the message
  received at the last sample time is displayed on the **Message** output port.

When you clear this option, the messages received for the specified topic form a
queue in a first-in-first-out order and these messages are displayed in the **Message** output port accordingly.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputMessage` |
| **Type:** character vector |
| **Values:** `'off'`|`'on'` |
| **Default:**  `off` |

### **Sample time** — Sampling rate for new messages `1` (default) | `-1` | positive integer

Specify how often the subscriber checks for a new message from the broker. When you
specify **Sample time** as `-1`, Simulink determines the best sample time for the block based on the block context
within the model.

## Libraries

NVIDIA Jetson and NVIDIA DRIVE / Internet Of Things

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023a**

## Description

Receive messages from the MQTT broker for specified topic

The MQTT Subscribe block receives messages from the MQ Telemetry Transport
(MQTT) broker for the specified topic.

At each time step, the block checks if a new message is available on the specified topic.
If a new message is available, the block receives the message. The
**Message** port outputs the new message. If a new message is not
available, **Message** outputs the last received message. The
**Topic** port outputs the topic of the received message. The string
**topic/level/#** on the block icon is specified by the
**Topic** parameter.

For more information on MQTT, see Introduction to MQTT.

**Note**

The MQTT Subscribe block supports MQTT only over TCP/IP sockets.
