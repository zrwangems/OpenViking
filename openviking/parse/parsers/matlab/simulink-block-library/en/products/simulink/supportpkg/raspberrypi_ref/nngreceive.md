---
type: simulink-block
title: 'NNG Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Communication'
documentation_page: 'nngreceive'
documentation_source_path: 'supportpkg/raspberrypi_ref/nngreceive.html'
language: en
---

# NNG Receive

## Ports

### Output

### **Data** — Received data [Nx1] array

The data received from the publisher, specified as a *N*-by-1
vector. *N* is the length of the message specified by the
**Data length (N)** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Status** — New message indicator `0` | `1`

If the subscriber receives a new message since the last sample time, the
**Status** port outputs `1`. Otherwise, the port outputs
`0`.

**Data Types:** `Boolean`

## Parameters

### **IPC name** — Name of inter process communication `pubsub` (default) | string

Enter the name of the inter process communication (IPC). This IPC name reflects in
the URL.

### **URL** — Service address to send and receive data `ipc:///tmp/pubsub.ipc` (default) | string

A URL is a service address used by the publisher to identify rightful subscribers
for delivering data. This URL is used by the publisher to receive data sent on the same
URL. The IPC name reflects in the URL.

**Note**

You cannot edit this parameter.

### **Data type** — Type of input data `uint8` (default) | `int8` | `uint16` | `int16` | `uint32` | `int32` | `single` | `double`

Select the type of input data that the subscriber receives at each sample
time.

### **Data length (N)** — Length of input data `1` (default) | integer between 1 and 2^31

Enter the maximum length of data that the subscriber receives at each sample
time.

### **Print diagnostic messages** — Save subscriber response to log file off (default) | on

Select this option to save the response from the subscriber to a log file each time
the data is received by the subscribers. The name of the log file is the Simulink® model name followed by `.log`.

### **Sample time** — Frequency to check for data from server `-1` (default) | any positive integer

Enter how often the subscriber checks for new data from the publisher. When you
specify the sample time as `-1`, the block inherits its sample time
based on the context of the block within the Simulink model.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023a**

## Description

Receive data through nanomsg next gen (NNG) using publish/subscribe protocol

Use the NNG Receive block to receive data from the publisher for the
specified uniform resource locator (URL). The block uses a publish/subscribe protocol for all
inter process communications. In the publish/subscribe protocol, each publisher that wants to
send data publishes them on a certain URL while, each subscriber that wants to receive data
subscribes to the same URL.
