---
type: simulink-block
title: 'MQTT Publish'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Communications'
documentation_page: 'mqttpublish'
documentation_source_path: 'supportpkg/android_ref/mqttpublish.html'
language: en
---

# MQTT Publish

## Ports

### Input

### **message** — Message to publish scalar

Specify the message you want the publisher to publish to the MQTT broker as an
array of ASCII characters of type `uint8`.

**Data Types:** `uint8`

## Parameters

### **Broker Service** — MQTT broker service provider `ThingSpeak` (default) | `Other`

Select the MQTT broker service provider that receives, filters, and sends messages
to the clients.

- `ThingSpeak` — When you specify this option, the MQTT
  access to your channels is handled by a ThingSpeak™ MQTT broker. To create an MQTT device, follow the steps in Create a ThingSpeak MQTT Device (ThingSpeak)
- `Other` — Specify this option when the MQTT access to
  your channels is handled by other MQTT public brokers such as HiveMQ®, Mosquitto™, and so on.

Configure the same MQTT broker properties as in the MQTT properties.

### **Topic** — Routing information for MQTT broker `channels/<channelID>/publish` (default) | any valid topic name

Specify a topic that the publisher uses to filter messages. A topic can have a
maximum of 128 characters. For information on topics and their structure, see Topics in MQTT.

### **Quality of Service** — Level of quality of service `0` (default) | `1` | `2`

Quality of Service (QoS) defines the reliability of the message delivery process in
MQTT. MQTT provides three QoS levels for message delivery: QoS 0, QoS 1, and QoS 2. The
MQTT broker that you are using might not support all three levels of QoS. For example,
ThingSpeak MQTT supports only QoS 0.

Select a QoS level from the drop-down menu:

- `0` — The publisher sends the message to the MQTT
  broker once. The broker does not send an acknowledgment of the receipt.
- `1` — The publisher sends the message to the MQTT
  broker at least once. The publisher resends the message if it does not receive an
  acknowledgment from the broker.
- `2` — The publisher sends the message to the MQTT
  broker exactly once. The publisher and broker exchange acknowledgments to ensure
  that the message is received only once.

### **Retain Message** — Option to send message to new subscribers `off` (default) | `on`

Control how the MQTT broker handles new subscriptions.

- `on` — When a new subscription is made to a topic, the broker
  identifies the message in its database with the matching topic name and sends the
  message immediately.

  **Note**

  The MQTT broker retains only the last published message related to the
  specified topic.
- `off` — When a new subscription is made to a topic, the
  subscriber must wait until the publisher sends the next message.

#### Dependencies

To enable this parameter, set **Broker Service** to
`Other`.

### **Update interval (seconds)** — Rate of publishing message(s) `60` (default) | scalar

Enter the time interval in seconds to publish message(s) to the MQTT broker.

## Libraries

Simulink Support Package for Android Devices / Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023a**

## Description

Publish message to an MQTT broker with the specified Topic

Use the MQTT Publish block to publish messages from your publisher
(hardware) to the MQTT broker on the topic you specify in the **Topic**
parameter.
