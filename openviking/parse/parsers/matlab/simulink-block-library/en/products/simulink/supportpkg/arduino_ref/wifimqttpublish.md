---
type: simulink-block
title: 'WiFi MQTT Publish'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Wi-Fi'
documentation_page: 'wifimqttpublish'
documentation_source_path: 'supportpkg/arduino_ref/wifimqttpublish.html'
language: en
---

# WiFi MQTT Publish

## Ports

### Input

### **message** — Message to publish scalar

Specify the message you want the publisher to publish to the MQTT broker as an
array of ASCII characters of type `uint8`.

**Data Types:** `uint8`
### Output

### **status** — Status code from MQTT broker `0` | `1`

The block outputs the status code issued by the MQTT broker in response to the
publish request. If the broker accepts the message for publishing, the block outputs
`1` at this port. The block outputs `0` when the
broker rejects the message. The broker can reject a message for various reasons, such
as an incorrect user name or password or if the message requires a protocol version
that the broker cannot accept.

**Data Types:** `int8`

## Parameters

### **Broker service** — MQTT broker service provider `ThingSpeak` (default) | `Other`

Select the MQTT broker service provider that receives, filters, and sends messages
to the clients.

- `ThingSpeak` — When you specify this option, the MQTT
  access to your channels is handled by a ThingSpeak™ MQTT broker. To create an MQTT device, follow the steps in Create a ThingSpeak MQTT Device (ThingSpeak).
- `Other` — Specify this option when the MQTT access to
  your channels is handled by other MQTT public brokers such as HiveMQ®, Mosquitto™, and so on.

Configure the same MQTT broker properties as in the MQTT properties.

### **Topic** — Routing information for MQTT broker `channels/<channelID>/publish` (default) | any valid topic name

Specify a topic that the publisher uses to filter messages. A topic can have a
maximum of 128 characters. For information on topics and their structure, see Topics in MQTT.

### **Retain message** — Option to send message to new subscribers `off` (default) | `on`

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

### **Print diagnostic messages** — Print MQTT broker response on serial port `off` (default) | `on`

Select this option to print the response from the MQTT broker on the Arduino serial port for each publish request.

## Libraries

Simulink Support Package for Arduino Hardware / WiFi

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022b**

## Description

Publish messages to message queuing telemetry transport (MQTT) broker

Use the WiFi MQTT Publish block to publish messages from your publisher
(hardware) to the MQTT broker on the topic you specify in the **Topic** parameter.

**Note**

The WiFi MQTT Publish block supports MQTT over TCP/IP sockets
only.

The WiFi MQTT Publish block supports these hardware boards.

- Arduino MKR WiFi 1010
- Arduino MKR 1000
- Arduino Nano 33 IoT
- Arduino® compatible ESP32 – WROOM board
- Arduino compatible ESP32 – WROVER board
