---
type: simulink-block
title: 'MQTT Subscribe'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Communications'
documentation_page: 'mqttsubscribe'
documentation_source_path: 'supportpkg/android_ref/mqttsubscribe.html'
language: en
---

# MQTT Subscribe

## Ports

### Output

### **Data Length** — Length of data scalar (default)

The port outputs the actual length of the data received from the MQTT
broker.

**Data Types:** `int32`

### **Data** — Data received from MQTT broker scalar

The block outputs the data received from the MQTT broker as an array of ASCII
characters.

**Data Types:** `uint8`

## Parameters

### **Topic** — Topic for subscription `channels/<channelID>/subscribe` (default) | any valid topic name

Specify a topic to which the client subscribes. A topic can have a maximum of 128
characters. For information on topics and their structure, see Topics in MQTT.

### **Maximum length of output message** — Maximum length of data read from the MQTT broker `256` (default) | `positive integer`

Specify the maximum length of the data you want to receive at each sample time.

### **Sample time** — Frequency to check for messages from MQTT broker `1` (default) | `-1` | scalar

Specify how often the client checks for a new message from the broker. When you
specify the sample time as `-1`, the block inherits its sample time
based on the context of the block within the model.

## Libraries

Simulink Support Package for Android Devices / Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023a**

## Description

Subscribe to an MQTT topic and receive message from the broker

Use the MQTT Subscribe block to receive messages from the message queuing
telemetry transport (MQTT) broker on the specified topic.
