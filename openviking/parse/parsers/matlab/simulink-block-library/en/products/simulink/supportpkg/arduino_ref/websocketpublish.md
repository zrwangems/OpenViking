---
type: simulink-block
title: 'WebSocket Publish'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Wi-Fi'
documentation_page: 'websocketpublish'
documentation_source_path: 'supportpkg/arduino_ref/websocketpublish.html'
language: en
---

# WebSocket Publish

## Ports

### Input

### **Signal** — Input data to be published row vector

The signal data to be published to the WebSocket server, specified as a row
vector.

The block provides an option to add up to 10 **Signal** input
ports that you can use to obtain signal data, with each signal being a row
vector.

**Example:** `[1.5,3]`

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## Parameters

### **Server port** — Port number on WebSocket server `9000` (default) | any port number

Specify the port number on the WebSocket server on which the JSON data is
hosted.

### **Number of Inputs** — Total number of input signal connections `1` (default) | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10`

Select the total number of input signal connections to the block, which is then
converted to JSON format.

## Libraries

Simulink Support Package for Arduino Hardware / WiFi

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020b**

## Description

Publish data to WebSocket server in JSON format

The WebSocket Publish block publishes data from the Arduino® hardware to a WebSocket server identified by an IP address and a port. The
published data is in JavaScript Object Notation
(JSON) format, which can be interpreted by a WebSocket client to visualize the data.

If the WebSocket Server is hosted on Arduino hardware, any device on the network can
connect to the server and access the data.

### Supported Arduino Boards

- Arduino MKR1000
- Arduino MKR WIFI 1010
- Arduino Nano 33 IoT
- Arduino compatible ESP32 – WROOM board
- Arduino compatible ESP32 – WROVER board

### WebSocket JSON Data

This figure shows the signals in JSON format.

JSON format for Arduino WebSocket Publish

If the JSON string size is more than 1024 bytes, the published data is replaced with the
error messages.

Error Format for WebSocket Publish
