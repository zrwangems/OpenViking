---
type: simulink-block
title: 'Call Service'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS 2'
documentation_page: 'callserviceros2'
documentation_source_path: 'ref/callserviceros2.html'
language: en
---

# Call Service

## Ports
```yaml
ports:
- name: Req
  summary: Request message nonvirtual bus
  direction: input
  data_types: bus
- name: Resp
  summary: Response message nonvirtual bus
  direction: output
  data_types: bus
- name: ErrorCode
  summary: Error conditions for service call integer
  direction: output
  data_types: uint8
```

### Input

### **Req** — Request message nonvirtual bus

Request message, specified as a nonvirtual bus. The request message type
corresponds to your service type. To generate an empty request message bus to populate
with data, use the Blank Message
block.

**Data Types:** `bus`
### Output

### **Resp** — Response message nonvirtual bus

Response message, returned as a nonvirtual bus. The response is based on the input
**Req** message. The response message type corresponds to your
service type. To generate an empty response message bus to populate with data, use the
Blank Message
block.

**Data Types:** `bus`

### **ErrorCode** — Error conditions for service call integer

Error conditions for service call, specified as an integer. Each integer
corresponds to a different error condition for the service connection or the status of
the service call. If an error condition occurs, **Resp** outputs the
last response message or a blank message if a response was not previously
received.

| Error Code | Condition |
| --- | --- |
| `0` | The service response was successfully retrieved and is available in the `Resp` output. |
| `1` | The connection was not established within the specified `Connection timeout`. |
| `2` | The response from the server was not received. |

#### Dependencies

This output is enabled when the **Show ErrorCode output port**
check box is `on`.

**Data Types:** `uint8`
## Parameters
```yaml
parameters:
- name: Source
  summary: Source for specifying service name Select from ROS network | Specify your own
  group: ''
  type: . You must match a service name exactly.
- name: Name
  summary: Service name character vector
  group: ''
- name: Type
  summary: Service type character vector
  group: ''
- name: Connection timeout
  summary: Timeout for service server connection 5 (default) | positive numeric scalar
  group: ''
- name: Show ErrorCode output port
  summary: Enable error code output port on (default) | off
  group: ''
- name: History
  summary: Mode of storing requests in the queue Keep last (default) | Keep all
  group: ''
- name: Depth
  summary: Size of the request queue 1 (default) | positive scalar
  group: ''
- name: Reliability
  summary: Delivery guarantee of requests Reliable (default) | Best effort
  group: ''
- name: Durability
  summary: Persistence of requests Volatile (default) | Transient local
  group: ''
- name: Deadline
  summary: Maximum amount of time allowed between sending service request and receiving response Inf (default) | positive
    scalar
  group: ''
- name: Lifespan
  summary: Length of time a service request is considered valid Inf (default) | positive scalar
  group: ''
- name: Liveliness
  summary: Level of liveliness reporting provided by the block and expected from service server automatic (default)
  group: ''
- name: Lease Duration
  summary: Maximum amount of time before which connected service server has to assert liveliness Inf (default) | positive
    scalar
  group: ''
```

#### Main

### **Source** — Source for specifying service name `Select from ROS network` | `Specify your own`

Source for specifying the service name:

- `Select from ROS network` — Use
  **Select** to select a service name. The
  **Name** and **Type** parameters are set
  automatically. You must be connected to a ROS 2 network.
- `Specify your own` — Enter a service name in
  **Name** and specify its service type in
  **Type**. You must match a service name exactly.

### **Name** — Service name character vector

Service name, specified as a character vector. The service name must match a service
name available on the ROS service server. To see a list of valid services in a ROS 2
network, see `ros2`.

### **Type** — Service type character vector

Service type, specified as a character vector. Each service name has a corresponding
type.

### **Connection timeout** — Timeout for service server connection `5` (default) | positive numeric scalar

Timeout for service server connection, specified as a positive numeric scalar in
seconds. If a connection cannot be established with the ROS service server in this time,
then **ErrorCode** outputs `1`.

### **Show ErrorCode output port** — Enable error code output port `on` (default) | `off`

Check this box to output the **ErrorCode** output. If an error
condition occurs, **Resp** outputs the last response message or a blank
message if response was not previously received.

#### Quality of Service (QoS)

### **History** — Mode of storing requests in the queue `Keep last` (default) | `Keep all`

Determines the mode of storing requests in the queue. If the queue fills with
requests waiting to be processed, then old requests will be dropped to make room for
new. If set to `Keep last`, the queue stores the number of
requests set by the `Depth` parameter. If set to `Keep
all`, the queue stores all requests up to the MATLAB resource limits.

### **Depth** — Size of the request queue `1` (default) | positive scalar

Number of requests stored in the request queue when `History` is
set to `Keep last`.

### **Reliability** — Delivery guarantee of requests `Reliable` (default) | `Best effort`

Affects the guarantee of request delivery. If `Reliable`, then
delivery is guaranteed, but may retry multiple times. If `Best
effort`, then attempt delivery and do not retry.
`Reliable` setting is recommended for services.

### **Durability** — Persistence of requests `Volatile` (default) | `Transient local`

Affects persistence of requests, which allows late-starting servers to receive the
number of old requests specified by `Depth`. If
`Volatile`, then requests do not persist. If
`Transient local`, then the block will persist most recent
requests.

### **Deadline** — Maximum amount of time allowed between sending service request and receiving response `Inf` (default) | positive scalar

Maximum amount of time allowed between sending a service request and receiving a
response, specified as a positive scalar. The `Deadline` QoS
parameter of service servers receiving request from the block must be less than or equal
to the value of this parameter.

The default value is `Inf` which implies that after the service
client sends a request, it can wait for an infinite period of time before receiving
response to that request.

**Note**

The quality of service settings must be compatible between service servers and clients for
a connection to be made.

### **Lifespan** — Length of time a service request is considered valid `Inf` (default) | positive scalar

Length of time a service request is considered valid, specified as a positive
scalar. This value determines the time for which the service requests sent are stored in
the queue.

The default value is `Inf` which implies that a service request
sent by service client is considered valid for infinite period of time.

**Note**

The quality of service settings must be compatible between service servers and clients for
a connection to be made.

### **Liveliness** — Level of liveliness reporting provided by the block and expected from service server `automatic` (default)

Level of liveliness reporting provided by the block and expected from the connected
service server, specified as `automatic`.

Liveliness set to `automatic` implies that after the block
receives a service response from the connected server, the block considers that server
to be alive for another `Lease Duration`.

**Note**

The quality of service settings must be compatible between service servers and clients for
a connection to be made.

### **Lease Duration** — Maximum amount of time before which connected service server has to assert liveliness `Inf` (default) | positive scalar

Maximum amount of time before which the connected service server has to assert
liveliness, specified as a positive scalar.

The default value is `Inf` which implies that the service server
connected to the client can assert liveliness for infinite period of time.

**Note**

The quality of service settings must be compatible between service servers and clients for
a connection to be made.
## Libraries

ROS Toolbox / ROS 2

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021b**

## Description

Call service in ROS 2 network

Use the Call Service block to implement a ROS 2 Service client in
Simulink®. The Call Service block takes a ROS 2 service request message,
sends it to the ROS 2 service server, and waits for a response. A ROS 2 service server should
be set up somewhere on the network before using this block. Check the available services on a
ROS 2 network by executing `ros2 service list` command, which uses `ros2` function. Use
`ros2svcserver` to set
up a service server in MATLAB®.

Specify the name for your ROS 2 service and the service type in the block mask. If
connected to a ROS 2 network, you can select from a list of available services. You can create
a blank service request or response message to populate with data using the Blank Message
block.

Always specify the quality of service (QoS) parameters in the block mask. QoS parameters
for this block must be compatible with the service server to send requests and receive
responses.
