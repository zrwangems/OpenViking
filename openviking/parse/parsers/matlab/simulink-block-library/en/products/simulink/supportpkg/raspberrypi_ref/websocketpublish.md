---
type: simulink-block
title: 'Websocket Publish'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Network'
documentation_page: 'websocketpublish'
documentation_source_path: 'supportpkg/raspberrypi_ref/websocketpublish.html'
language: en
---

# Websocket Publish

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

### **Block label** — Unique label to identify published JSON data `webPub 1` (default)

Specify a unique label for the block to identify the published JSON data (which gets created
from the input signal data). The label can have a maximum of 128 characters.

### **Server IP address** — IP address of WebSocket server `127.0.0.1` (default) | any IP address

IP address of the WebSocket server on which the JSON data is hosted.

### **Server Port** — Port number on WebSocket server `9000` (default) | any port number

Specify the port number on the WebSocket server on which the JSON data is
hosted.

**Note**

You can use multiple Websocket Publish blocks in a Simulink model if the
**Server IP address** and **Server Port**
parameters are unique.

### **Number of inputs** — Total number of input signal connections `1` (default) | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10`

Select the total number of input signal connections to the block, which is then
converted to JSON format.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Network

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019b**

## Description

Publish data to WebSocket server in JSON format

The WebSocket Publish
block publishes the data from the Raspberry Pi® to a WebSocket server identified by an IP address and a port. The published data
is in JavaScript Object Notation (JSON)
format, which can be interpreted by a WebSocket client to visualize the data.

If the WebSocket server is hosted on a network IP address, any
device on the network can connect to the sever and access the data.

### WebSocket JSON data

This figure shows the signals in JSON format with a unique
block label.

WebSocket JSON Data
