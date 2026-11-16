---
type: simulink-block
title: 'Call Service'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS'
documentation_page: 'callserviceros1'
documentation_source_path: 'ref/callserviceros1.html'
language: en
---

# Call Service

## Ports

### Input

### **Req** — Request message nonvirtual bus

Request message, specified as a nonvirtual bus. The request message type corresponds to your service type. To generate an empty request message bus to populate with data, use the Blank Message block.

**Data Types:** `bus`
### Output

### **Resp** — Response message nonvirtual bus

Response message, returned as a nonvirtual bus. The response is based on the input **Req** message. The response message type corresponds to your service type. To generate an empty response message bus to populate with data, use the Blank Message block.

**Data Types:** `bus`

### **ErrorCode** — Error conditions for service call integer

Error conditions for service call, specified as an integer. Each integer corresponds to a different error condition for the service connection or the status of the service call. If an error condition occurs, **Resp** outputs the last response message or a blank message if a response was not previously received.

| Error Code | Condition |
| --- | --- |
| `0` | The service response was successfully retrieved and is available in the `Resp` output. |
| `1` | The connection was not established within the specified `Connection timeout`. |
| `2` | The response from the server was not received. |
| `3` | The service call failed for unknown reasons. |

#### Dependencies

This output is enabled when the **Show ErrorCode output port** check box is `on`.

**Data Types:** `uint8`

## Parameters

### **Source** — Source for specifying service name `Select from ROS network` | `Specify your own`

Source for specifying the service name:

- `Select from ROS network`
  — Use **Select** to select a service name. The **Name** and **Type** parameters are set automatically. You must be connected to a ROS network.
- `Specify your own`
  — Enter a service name in **Name** and specify its service type in **Type**. You must match a service name exactly.

### **Name** — Service name character vector

Service name, specified as a character vector. The service name must match a service name available on the ROS service server. To see a list of valid services in a ROS network, see `rosservice`.

### **Type** — Service type character vector

Service type, specified as a character vector. Each service name has a corresponding type.

### **Connection timeout** — Timeout for service server connection `5` (default) | positive numeric scalar

Timeout for service server connection, specified as a positive numeric scalar in seconds. If a connection cannot be established with the ROS service server in this time, then **ErrorCode** outputs 1.

### **Keep persistent connection** — Keep connection to service server `off` (default) | `on`

Check this box to maintain a persistent connection with the ROS service server. When `off`, the block creates a service client every time a request message is input into **Req**.

### **Show ErrorCode output port** — Enable error code output port `on` (default) | `off`

Check this box to output the **ErrorCode** output. If an error condition occurs, **Resp** outputs the last response message or a blank message if response was not previously received.

## Libraries

ROS Toolbox / ROS

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

## Description

Call service in ROS network

The Call Service block takes a ROS service request message, sends it to the ROS service server, and waits for a response. Connect to a ROS network using `rosinit`. A ROS server should be set up somewhere on the network before using this block. Check the available services on a ROS network using `rosservice`. Use `rossvcserver` to set up a service server in MATLAB®.

Specify the name for your ROS service and the service type in the block mask. If connected to a ROS network, you can select from a list of available services. You can create a blank service request or response message to populate with data using the Blank Message block.
