---
type: simulink-block
title: 'WiFi MQTT Subscribe'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Wi-Fi'
documentation_page: 'wifimqttsubscribe'
documentation_source_path: 'supportpkg/arduino_ref/wifimqttsubscribe.html'
language: en
---

# WiFi MQTT Subscribe

## Ports

### Output

### **isNew** — New message indicator `0` (default) | `1`

The block outputs `1` if the client receives a new message since
the last sample time. Otherwise, the block outputs `0`.

**Data Types:** `Boolean`

### **message** — Message received from MQTT broker scalar

The block outputs the message received from the MQTT broker as an array of ASCII
characters.

**Data Types:** `uint8`

### **topic** — Topic of message `topic/level/#`

The block outputs ASCII values corresponding to the topic name of the received
message. For example, if the topic of the received message is
`model/data`, the port outputs the topic as `109 111 100
101 108 47 100 97 116 97`.

To convert the ASCII values into their alphanumeric equivalent, attach an ASCII to
String block to the output of the **topic**
port. A topic can have a maximum of 128 characters. For information on topics and
their structure, see Topics in MQTT.

#### Dependencies

To enable this port, include a wildcard entry in the **Topic**
parameter. For more information on wildcards in MQTT, see Wildcards in MQTT Topics.

**Data Types:** `uint8`

## Parameters

### **Topic** — Topic for subscription `channels/<channelID>/subscribe` (default) | any valid topic name

Specify a topic to which the client subscribes. A topic can have a maximum of 128
characters. For information on topics and their structure, see Topics in MQTT.

### **Data length** — Length of data read from the MQTT broker `10` (default) | `positive integer`

Specify the length of the data you want to receive at each sample time.

### **Print diagnostic messages** — Print MQTT broker response on serial port `off` (default) | `on`

Select this option to print the response from the MQTT broker on the Arduino serial port for each publish request.

### **Sample time** — Frequency to check for messages from MQTT broker `1` (default) | `-1` | any positive integer

Specify how often the client checks for a new message from the broker. When you
specify the sample time as `-1`, the block inherits its sample time
based on the context of the block within the model.

## Libraries

Simulink Support Package for Arduino Hardware / WiFi

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022b**

## Description

Receive messages from message queuing telemetry transport (MQTT) broker

Use the WiFi MQTT Subscribe block to receive messages from the message
queuing telemetry transport (MQTT) broker on the specified topic.

**Note**

The WiFi MQTT Subscribe block supports MQTT over TCP/IP sockets
only.

The WiFi MQTT Subscribe block supports these hardware boards.

- Arduino MKR WiFi 1010
- Arduino MKR 1000
- Arduino Nano 33 IoT
- Arduino® compatible ESP32 – WROOM board
- Arduino compatible ESP32 – WROVER board
