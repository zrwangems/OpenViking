---
type: simulink-block
title: 'Receive Service Request'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS 2'
documentation_page: 'receiveservicerequestros2'
documentation_source_path: 'ref/receiveservicerequestros2.html'
language: en
---

# Receive Service Request

## Ports
```yaml
ports:
- name: IsNew
  summary: New service request indicator 0 | 1
  direction: output
  data_types: Boolean
- name: Req
  summary: Service request message non-virtual bus
  direction: output
  data_types: bus
- name: DefaultResp
  summary: Default response message non-virtual bus
  direction: output
  data_types: bus
```

### Output

### **IsNew** — New service request indicator `0` | `1`

New service request indicator, returned as a logical. If the output is
`1`, then a new service request was received since the last sample
hit. You can use this output to trigger subsystems for processing new messages
received in the ROS 2 network.

**Data Types:** `Boolean`

### **Req** — Service request message non-virtual bus

Service request message, returned as a non-virtual bus corresponding to the
service request type. The service request message type depends on the service type
specified in the **Service Type** parameter.

**Data Types:** `bus`

### **DefaultResp** — Default response message non-virtual bus

Default response message, returned as a non-virtual bus corresponding to the
default response message type.

#### Dependencies

- To enable this output port, select the **Show Default Response
  output port** parameter.

**Data Types:** `bus`
## Parameters
```yaml
parameters:
- name: Name
  summary: Service name character vector
  group: ''
- name: Type
  summary: Service type character vector
  group: ''
- name: Paired Send Response Block
  summary: Path to paired Send Service Response block block path
  group: ''
- name: Sample time
  summary: Interval between outputs –1 (default) | scalar
  group: ''
- name: Show Default Response output port
  summary: Enable default response output port on (default) | off
  group: ''
- name: History
  summary: Mode of storing requests in the queue Keep last (default) | Keep all
  group: ''
- name: Depth
  summary: Size of the request queue 1 (default) | non-negative scalar integer
  group: ''
- name: Reliability
  summary: Delivery guarantee of requests Reliable (default) | Best effort
  group: ''
- name: Durability
  summary: Persistence of requests Volatile (default) | Transient local
  group: ''
- name: Deadline
  summary: Maximum amount of time allowed between receiving a service request and sending response Inf (default) | positive
    scalar
  group: ''
- name: Lifespan
  summary: Length of time a service request is considered valid Inf (default) | positive scalar
  group: ''
- name: Liveliness
  summary: Level of liveliness reporting provided by the block and expected from service clients automatic (default)
  group: ''
- name: Lease Duration
  summary: Maximum amount of time before which a connected service client has to assert liveliness Inf (default) | positive
    scalar
  group: ''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

#### Main

### **Name** — Service name character vector

Service name, specified as a character vector. This is the name of the service
server which clients can then use to connect and send service requests.

### **Type** — Service type character vector

Service type, specified as a character vector. Each service name has a corresponding
type. Click the **Select** button to select from a full list of
supported ROS 2 service types.

If you are using a custom service type, first build the associated service
definitions using the `ros2genmsg`
function. Then, you can specify your custom service type using the
**Select** button.

### **Paired Send Response Block** — Path to paired Send Service Response block block path

Path to the Send Service Response block paired with this
Receive Service Request block. To create a paired Send Service
Response for the first time, click `Create paired Send Response
block`.

After you create a paired Send Service Response block, clicking the
path displays and highlights the Send Service Response block in your
model.

#### Tips

- For correct service server implementation, only use `Click to create
  paired Send Response block` to create the Send Service
  Response associated with this Receive Service Request
  block. Do not add a Send Service Response block from the
  library.

### **Sample time** — Interval between outputs `–1` (default) | scalar

Interval between outputs, specified as a scalar. In simulation, the sample time
follows simulation time and not actual wall-clock time.

This default value indicates that the block sample time is
*inherited*.

For more information about the inherited sample time type, see Specify Sample Time (Simulink).

### **Show Default Response output port** — Enable default response output port `on` (default) | `off`

Check this box to enable the **DefaultResp** output.

#### Quality of Service (QoS)

### **History** — Mode of storing requests in the queue `Keep last` (default) | `Keep all`

Determines the mode of storing requests in the queue. If the queue fills with
requests waiting to be processed, then old requests will be dropped to make room for
new. If set to `Keep last`, the queue stores the number of
requests set by the `Depth` parameter. If set to `Keep
all`, the queue stores all requests up to the MATLAB® resource limits.

### **Depth** — Size of the request queue `1` (default) | `non-negative scalar integer`

Size of the request queue in number of requests stored in the queue, specified as a
`non-negative scalar integer`.This only applies when
`History` is set to `Keep last`.

### **Reliability** — Delivery guarantee of requests `Reliable` (default) | `Best effort`

Requirement on delivery guarantee of request and response, specified as
`Reliable` or `Best effort`. If
`Reliable`, then delivery is guaranteed, but may retry multiple
times. If `Best effort`, then attempt delivery and do not
retry. `Reliable` setting is recommended for services.

**Note**

The quality of service settings must be compatible between service servers and clients for
a connection to be made.

### **Durability** — Persistence of requests `Volatile` (default) | `Transient local`

Requirement on persistence of the client, specified as
`Volatile` or `Transient local`. If
`Volatile`, then requests are not required to persist. If
`Transient local`, then the server will require clients to
persist and receive responses for the number of previous requests specified by
`Depth`. `Volatile` setting is recommended
to prevent servers from receiving out of date requests in the event of a server
restart.

**Note**

The quality of service settings must be compatible between service servers and clients for
a connection to be made.

### **Deadline** — Maximum amount of time allowed between receiving a service request and sending response `Inf` (default) | positive scalar

Maximum amount of time allowed between receiving a service request and sending a
response, specified as a positive scalar. The `Deadline` QoS
parameter of service clients sending requests to the block must be greater than or equal
to the value of this parameter.

The default value is `Inf` which implies that after the service
server receives a service request, it can wait for an infinite period of time before
sending response to that request.

**Note**

The quality of service settings must be compatible between service servers and clients for
a connection to be made.

### **Lifespan** — Length of time a service request is considered valid `Inf` (default) | positive scalar

Length of time a service request is considered valid, specified as a positive
scalar. The block does not process service requests persisting longer than the specified
lifespan in the queue.

The default value is `Inf` which implies that a service request
received by service server is considered valid for infinite period of time.

**Note**

The quality of service settings must be compatible between service servers and clients for
a connection to be made.

### **Liveliness** — Level of liveliness reporting provided by the block and expected from service clients `automatic` (default)

Level of liveliness reporting provided by the block and expected from the connected
service clients, specified as `automatic`.

Liveliness set to `automatic` implies that after the block
receives a service request from a connected client, the block considers that client to
be alive for another `Lease Duration`.

**Note**

The quality of service settings must be compatible between service servers and clients for
a connection to be made.

### **Lease Duration** — Maximum amount of time before which a connected service client has to assert liveliness `Inf` (default) | positive scalar

Maximum amount of time before which a connected service client has to assert
liveliness, specified as a positive scalar.

The default value is `Inf` which implies that the service client
connected to the server can assert liveliness for infinite period of time.

**Note**

The quality of service settings must be compatible between service servers and clients for
a connection to be made.
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

Receive service request from ROS 2 network

Use the Receive Service Request and Send Service Response
blocks in the same model to implement a ROS 2 service server in Simulink®. The Receive Service Request block enables you to receive a ROS 2
service request message from a service client, process it in the model to construct an
appropriate response, and then send the response to the client using a Send Service
Response block. The service server is associated with the ROS 2 node of the
Simulink model.

On each simulation step, the Receive Service Request block checks if a new
service request has been sent by a client. If a new service request is available, the block
retrieves it and outputs a non-virtual bus which corresponds to the service request message
type. If the block does not receive a service request at a time step, it outputs the last
service request message received.

Specify the name for your ROS 2 service, the service type, and the quality of service
(QoS) parameters in the block mask. QoS parameters for this block must be compatible with the
service clients to receive requests and send responses.

**Note**

For each Receive Service Request you add to a model, you must click
**Click to create paired Send Response block** in the block mask to
create a paired Send Service Response
block. Do not add a Send Service Response block from the library.
