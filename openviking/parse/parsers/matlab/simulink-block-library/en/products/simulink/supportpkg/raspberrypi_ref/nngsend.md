---
type: simulink-block
title: 'NNG Send'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Communication'
documentation_page: 'nngsend'
documentation_source_path: 'supportpkg/raspberrypi_ref/nngsend.html'
language: en
---

# NNG Send

## Ports

### Input

### **Port\_1** — Input data vector

The block accepts the input data to be published to the server, specified as a
vector.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### Output

### **Status** — Status code from publisher scalar

The block outputs the status code issued by the publisher in response to the
publish request. If the publisher accepts the message for publishing, the port outputs
`0`. Any nonzero output indicates that the publisher has rejected
the message.

**Data Types:** `int8`

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

### **Print diagnostic messages** — Save publisher response to log file off (default) | on

Select this option to save the response from the publisher to a log file each time
the data is sent to subscribers. The name of the log file is the Simulink® model name followed by `.log`.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023a**

## Description

Send data through nanomsg next gen (NNG) using publish/subscribe protocol

Use the NNG Send block to broadcast data to all applications subscribing to
the same uniform resource locator (URL). The block uses a publish/subscribe protocol for all
inter process communications. In the publish/subscribe protocol, each publisher that wants to
send data publishes them on a certain URL while, each subscriber that wants to receive data
subscribes to the same URL.
