---
type: simulink-block
title: 'MQTT Publish'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Internet of Things'
documentation_page: 'mqttpublish'
documentation_source_path: 'supportpkg/raspberrypi_ref/mqttpublish.html'
language: en
---

# MQTT Publish

## Ports

### Input

### **Message** — Message to be published vector

Specify the message you want the publisher to publish to the MQTT broker as an
array of ASCII characters of type `uint8`.

**Example:** `[0,3]`

**Data Types:** `uint8`
### Output

### **Status** — Status code from MQTT broker scalar

The status code issued by the MQTT broker in response to the publish request. If
the broker accepts the message for publishing, the port outputs `0`.
Any nonzero output indicates that the broker has rejected the message. A message can
be rejected for various reasons, such as an incorrect user name or password or an
unacceptable protocol version. For more information on status codes from MQTT brokers,
see MQTT Status Codes.

**Data Types:** `int8`

## Parameters

### **Topic** — Topic of the message `topic/level` (default) | any valid topic name

Specify a topic on which the message is to be published. A topic can have a maximum
of 128 characters. For information on topics and its structure, see Topics in MQTT.

### **QoS** — Levels of QoS `0` (default) | `1` | `2`

Quality of Service (QoS) defines the reliability of the message delivery process in
MQTT. MQTT provides three QoS levels for message delivery: QoS 0, QoS 1, and QoS 2. The
MQTT broker that you are using might not support all three levels of QoS. For example,
ThingSpeak™ MQTT supports only QoS 0.

Select a QoS level from the list:

- `0`: The publisher sends the message to the MQTT
  broker once. The broker does not send an acknowledgment of the receipt.
- `1`: The publisher sends the message to the MQTT
  broker at least once. The publisher resends the message if it does not receive an
  acknowledgment from the broker.
- `2`: The publisher sends the message to the MQTT
  broker exactly once. The publisher and broker exchange acknowledgments to ensure
  that the message is received only once.

For more information on QoS levels, see Levels of QoS in MQTT.

### **Retain message** — Option to send message to new subscribers `off` (default) | `on`

The **Retain message** parameter controls how new subscriptions are
handled:

- `on` –– When a new subscription is made to a topic, the
  broker identifies the message in its database with the matching topic name and
  sends the message immediately.

  **Note**

  The MQTT broker retains only the last known message published on a
  topic.
- `off` –– When a new subscription is made to a topic, the
  subscriber must wait until the publisher sends the next message.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Internet Of Things

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Publish messages to MQTT broker on specified topic

The MQTT Publish block publishes messages from your hardware (publisher) to
the Message Queuing Telemetry Transport (MQTT) broker on the specified topic.

The block has a **Message**
input port and a **Status**
output port. The **Message** port accepts the message to be published to the
broker. The **Status** port outputs the status of the publish request. The
string **topic/level** on the block icon is specified by the
**Topic** parameter.

For more information on MQTT, see Publish MQTT Messages and Subscribe to Message Topics.

**Note**

The MQTT Publish block supports MQTT only over TCP/IP sockets.
