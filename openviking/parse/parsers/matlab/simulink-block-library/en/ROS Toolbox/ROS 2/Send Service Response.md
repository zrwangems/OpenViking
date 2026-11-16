---
type: simulink-block
title: 'Send Service Response'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS 2'
documentation_page: 'sendserviceresponseros2'
documentation_source_path: 'ref/sendserviceresponseros2.html'
language: en
---

# Send Service Response

## Ports

### Input

### **Resp** — Service response message to send to client non-virtual bus

Service response message to send to the service client, specified as a non-virtual
bus. The response message type is based on the service type specified in the paired
Receive Service request block.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Name** — Service name Read-only: character vector

This parameter is read-only.

Service name, specified as a character vector. This is the name of the service
server which clients can then use to connect and send service requests.

#### Dependencies

The service name is same as that specified in the paired Receive Service
request block.

### **Type** — Service type Read-only: character vector

This parameter is read-only.

Service type, specified as a character vector. Each service name has a corresponding
type. Click the **Select** button to select from a full list of
supported ROS 2 service types.

If you are using a custom service type, first build the associated service
definitions using the `ros2genmsg`
function. Then, you can specify your custom service type using the
**Select** button.

#### Dependencies

The service type is same as that specified in the paired Receive Service
request block.

### **Paired Receive Request Block** — Path to paired Receive Service Request block block path

Path to the Receive Service Request block paired with this
Send Service Response block. To create a paired Receive Service
Request for the first time, click `Create paired Receive Request
block`.

After you create a paired Receive Service Request block, clicking the
path displays and highlights the Receive Service Request block in your
model.

#### Tips

- For correct service server implementation, only use `Click to create
  paired Receive Request block` to create the Receive Service
  Request associated with this Send Service Response block.
  Do not add a Send Service Response block from the library.

## Libraries

ROS Toolbox / ROS 2

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Usage notes and limitations:

- The generated service server follows rate-based execution and not event-driven
  execution.

## Version History

**Introduced in R2024a**

## Description

Send service response to ROS 2 service client

Use the Receive Service Request block and the Send Service
Response in the same model to implement a ROS 2 service server in Simulink®. The Send Service Response block enables you to send service
response messages to service clients after processing the service requests the clients sent.
To configure the service parameters and receive service requests, you must first create a
paired Receive Service Request
block and specify all the parameters in the Receive Service Request block mask.
You can then process incoming service requests in the model, construct appropriate responses,
and then use the Send Service Response to return the service response to the
clients. The service server is associated with the node of the Simulink model.

**Note**

For each Send Service Response block you add in a model, you must create
a paired Receive Service Request block only by clicking **Click to
create paired Receive Request block** in the block mask.
