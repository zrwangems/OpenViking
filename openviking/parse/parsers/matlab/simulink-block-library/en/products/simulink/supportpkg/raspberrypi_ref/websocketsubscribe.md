---
type: simulink-block
title: 'Websocket Subscribe'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Network'
documentation_page: 'websocketsubscribe'
documentation_source_path: 'supportpkg/raspberrypi_ref/websocketsubscribe.html'
language: en
---

# Websocket Subscribe

## Ports

### Output

### **Out** — Received data row vector

The data received by the WebSocket server, specified as a row vector.

The block provides an option to add up to 10 **Out** ports to
obtain signal data, with each signal being an *N*-by-1 vector.
*N* is the number of data points in a signal.

**Example:** `[1.5,3]`

#### Dependencies

To enable the port, specify the total number of output signals in the
**Number of outputs** parameter. When you specify
**Number of outputs**, the block generates equal number of output
ports. For example, if you specify **Number of outputs** as
`4`, the block generates four output ports.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Status** — Validity of received data scalar

The block outputs the status indicating the validity of the received data.

The status is:

- `1`: Valid data
- `0`: Received data is empty or is of invalid JSON
  format
- `-1`: Mismatch in number of data fields

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## Parameters

### **Server IP address** — IP address of WebSocket server `127.0.0.1` (default) | any IP address

The IP address of the WebSocket server on which the JSON data is hosted.

### **Server Port** — Port number on WebSocket server `9000` (default) | any port number

The port number on the WebSocket server on which the JSON data is hosted.

**Note**

To avoid any resource conflicts, the **Server IP address** and
**Server Port** parameters of all the WebSocket
Subscribe blocks in a Simulink® model must be unique.

### **Specify output info via** — Source to obtain properties of JSON data `Mask Dialog` (default) | `JSON file`

Specify the properties of the data using the Block Parameters dialog box or from a
JSON file.

- `Mask Dialog` –– Specify the total number of signal
  data using the block parameters dialog box. The block generates output ports that
  are equal in number to the total number of signals specified. You must also
  specify data size and data type of each signal using the dialog box.
- `JSON file` –– If you have a JSON file that contains
  the signal data, upload the file by clicking the **Browse**
  button. On successfully uploading the file, the block generates output ports that
  are equal in number to the data signals in the specified file. The data size and
  data type of each signal is inherited from the file.

### **Number of outputs** — Total number of output signals `1` (default) | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10`

Specify the total number of output signals received by the WebSocket server. When
you specify a value in this parameter, the block generates output ports that are equal
in number to the value specified in this parameter. For example, if you specify
**Number of outputs** as `4`, the block generates
four output ports.

#### Dependencies

To enable the parameter, set the **Specify output info via**
parameter to `Mask Dialog`.

### **Data Size** — Total number of data points `1` (default)

Specify the total number of data points in an output signal.

#### Dependencies

To enable the parameter, set the **Specify output info via**
parameter to `Mask Dialog`.

### **Data Type** — Data type of output signal `double` (default) | `single` | `uint32` | `int32` | `uint16` | `int16` | `uint8` | `int8` | `Boolean`

The data type of the output signal.

#### Dependencies

To enable the parameter, set the **Specify output info via**
parameter to `Mask Dialog`.

### **JSON File Path** — Path of JSON file valid JSON file path

Click the **Browse** button to choose a JSON file that contains
the signal data. On successfully uploading the JSON file, the block generates output
ports that are equal in number to the data signals in the specified file. The data size
and data type of each signal is inherited from the file.

#### Dependencies

To enable the parameter, set the **Specify output info via**
parameter to `JSON file`.

### **Sample time** — Time interval to receive data from WebSocket server `0.1` (default) | `-1` | any positive integer

Specify how often the block receives the data from the WebSocket server. When you
specify **Sample time** as `-1`, the block inherits
its sample time based on the context of the block within the model.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Network

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020a**

## Description

Subscribe to the JSON data received by a WebSocket server

The WebSocket Subscribe block subscribes to the data received by a
WebSocket server identified by an IP address and a port. The received data must be in JavaScript Object Notation (JSON)
format, which can be interpreted by a WebSocket client to manipulate the data.

### WebSocket JSON Data

This figure shows the signals in JSON format with a unique
block label.

WebSocket JSON Data
