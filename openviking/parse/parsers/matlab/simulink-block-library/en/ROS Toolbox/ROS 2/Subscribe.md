---
type: simulink-block
title: 'Subscribe'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS 2'
documentation_page: 'subscriberos2'
documentation_source_path: 'ref/subscriberos2.html'
language: en
---

# Subscribe

## Ports

### Output

### **IsNew** — New message indicator `0` | `1`

New message indicator, returned as a logical. If the output is `1`, then a new message was received since the last sample hit. This output can be used to trigger subsystems for processing new messages received in the ROS 2 network.

### **Msg** — ROS 2 message non-virtual bus

ROS 2 message, returned as a non-virtual bus. The type of ROS message is specified in the **Message type** parameter. The Subscribe ROS 2 block outputs blank messages until it receives a message on the topic name you specify. These blank messages allow you to create and test full models before the rest of the network has been setup.

**Data Types:** `bus`

## Parameters

#### Main

### **Topic source** — Source for specifying topic name `Select from ROS network` | `Specify your own`

Source for specifying the topic name, specified as one of the following:

- `Select from ROS network`
  — Use **Select** to select a topic name. The **Topic** and **Message type** parameters are set automatically. You must be connected to a ROS network.
- `Specify your own`
  — Enter a topic name in **Topic** and specify its message type in **Message type**. You must match a topic name exactly.

### **Topic** — Topic name to subscribe to string

Topic name to subscribe to, specified as a string. When **Topic source** is set to `Select from ROS network`, use **Select** to select a topic from the ROS network. You must be connected to a ROS 2 network to get a list of topics. Otherwise, set **Topic source** to `Specify your own` and specify the topic you want.

### **Message type** — ROS 2 message type string

ROS 2 message type, specified as a string. Use **Select** to select from a full list of supported ROS 2 messages. Service message types are not supported and are not included in the list.

### **Sample time** — Interval between outputs `–1` (default) | scalar

Interval between outputs, specified as a scalar. In simulation, the sample time follows simulation time and not actual wall-clock time.

This default value indicates that the block sample time is *inherited*.

For more information about the inherited sample time type, see Specify Sample Time (Simulink).

#### Quality of Service (QoS)

### **History** — Mode of storing messages in the queue `Keep last` (default) | `Keep all`

Determines the mode of storing messages in the queue. The queued messages will be sent to late-joining subscribers. If the queue fills with messages waiting to be processed, then old messages will be dropped to make room for new. When set to `Keep last`, the queue stores the number of messages set by the `Depth` property. Otherwise, when set to `Keep all`, the queue stores all messages up to the MATLAB® resource limits.

### **Depth** — Size of the message queue `10` (default) | positive scalar

Number of messages stored in the message queue when `History` is set to `Keep last`.

### **Reliability** — Delivery guarantee of messages `Reliable` (default) | `Best effort`

Affects the guarantee of message delivery. If `Reliable`, then delivery is guaranteed, but may retry multiple times. If `Best effort`, then attempt delivery and do not retry.

### **Durability** — Persistence of messages `Volatile` (default) | `Transient local`

Affects persistence of messages in publishers, which allows late-joining subscribers to receive the number of old messages specified by `Depth`. If `Volatile`, then messages do not persist. If `Transient local`, then publisher will retain the most recent messages.

### **Deadline** — Expected interval between consecutive message receptions `Inf` (default) | positive scalar

Outlines the permissible duration between message receptions by subscriber,
specified as a positive scalar. In case the messages are not received within the
deadline, the client application receives a notification.

The default value is `Inf` which implies that expected interval
between subsequent message receptions is infinite. If `Deadline` is
set to `3`, it ensures that the subscriber subscribes to every
succeeding message is published to the topic after 3 seconds of subscribing to the
preceding message.

### **Lifespan** — Message validity window between publishing and reception `Inf` (default) | positive scalar

Defines the duration a message is deemed valid, beyond which it will not be received
by subscriber, specified as a positive scalar. Messages that have expired are silently
discarded.

The default value is `Inf` which implies that a message is deemed
valid and received by subscriber for infinite duration. If `Lifespan`
is set to 5, it means that a message is considered valid for 5 seconds after being
published. If subscriber has not received the message within that time frame, the
message is considered expired.

### **Liveliness** — Publisher aliveness asserting protocol `"automatic"` (default)

Determines the reporting standard expected from the publishers to which they are
subscribed, specified as a string.

`Liveliness` set to `"automatic"` implies that
when any of the publishers has published a message, the system will consider all
publishers of the node to be alive for an additional `Lease
Duration`.

### **Lease Duration** — Maximum time window between liveliness assertions `Inf` (default) | positive scalar

Defines the maximum duration for which a subscriber expects a publisher to
demonstrate its liveliness before the system considers it to have lost liveliness,
specified as a positive scalar. Losing liveliness could serve as an indication of
failure.

The default value is `Inf` which implies that a publisher can
assert its liveliness for infinite period of time. If the `Lease
Duration` is set to 5, it implies that the subscriber can expect the
publisher to demonstrate its liveliness within a maximum of 5 seconds. If the publisher
does not send any messages or explicitly assert its liveliness within that time frame,
it is considered to have lost liveliness.

## Libraries

ROS Toolbox / ROS 2

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

### R2025a: Change in `Depth` QoS setting default value

As of R2025a, the default value of `Depth` QoS setting in ROS 2
Subscribe block parameter is `10`. You can increase the
`Depth` value to minimize the message drops or set it to
`1` to work on the latest message in Simulink generated code.

## Description

Receive messages from ROS 2 network

The Subscribe block creates a Simulink® non-virtual bus that corresponds to the specified ROS 2 message type. The block
uses the node of the Simulink model to create a ROS 2 subscriber for a specific topic. This node is created
when the model runs and is deleted when the model terminates. If the model does not have a
node, the block creates one.

On each simulation step, the block checks if a new message is available on the specific topic. If a new message is available, the block retrieves the message and converts it to a Simulink bus signal. The **Msg** port outputs this new message. If a new message is not available, **Msg** outputs the last received ROS 2 message. If a message has not been received since the start of the simulation, **Msg** outputs a blank message.

Quality of Service (QoS) events related to different QoS policies trigger default warnings
for Subscribe block. For more information on the different QoS events and the
triggered warnings respectively, see **QoS Events** section in
Manage Quality of Service Policies in ROS 2 example.
