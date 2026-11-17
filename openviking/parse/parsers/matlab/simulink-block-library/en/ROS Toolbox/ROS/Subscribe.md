---
type: simulink-block
title: 'Subscribe'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS'
documentation_page: 'subscribe'
documentation_source_path: 'ref/subscribe.html'
language: en
---

# Subscribe

## Ports
```yaml
ports:
- name: IsNew
  summary: New message indicator 0 | 1
  direction: output
- name: Msg
  summary: ROS message nonvirtual bus
  direction: output
  data_types: bus
```

### Output

### **IsNew** — New message indicator `0` | `1`

New message indicator, returned as a logical. If the output is `1`, then a new message was received since the last sample hit. This output can be used to trigger subsystems for processing new messages received in the ROS network.

### **Msg** — ROS message nonvirtual bus

ROS message, returned as a nonvirtual bus. The type of ROS message is specified in the **Message type** parameter. The Subscribe block outputs blank messages until it receives a message on the topic name you specify. These blank messages allow you to create and test full models before the rest of the network has been setup.

**Data Types:** `bus`
## Parameters
```yaml
parameters:
- name: Topic source
  summary: Source for specifying topic name Select from ROS network | Specify your own
  group: ''
- name: Topic
  summary: Topic name to subscribe to string
  group: ''
- name: Message type
  summary: ROS message type string
  group: ''
- name: Sample time
  summary: Interval between outputs –1 (default) | scalar
  group: ''
- name: Length of subscribe callback queue
  summary: Message queue length 1 (default) | integer
  group: ''
```

### **Topic source** — Source for specifying topic name `Select from ROS network` | `Specify your own`

Source for specifying the topic name, specified as one of the following:

- `Select from ROS network`
  — Use **Select** to select a topic name. The **Topic** and **Message type** parameters are set automatically. You must be connected to a ROS network.
- `Specify your own`
  — Enter a topic name in **Topic** and specify its message type in **Message type**. You must match a topic name exactly.

### **Topic** — Topic name to subscribe to string

Topic name to subscribe to, specified as a string. When **Topic source** is set to `Select from ROS network`, use **Select** to select a topic from the ROS network. You must be connected to a ROS network to get a list of topics. Otherwise, set **Topic source** to `Specify your own` and specify the topic you want.

### **Message type** — ROS message type string

ROS message type, specified as a string. Use **Select** to select from a full list of supported ROS messages. Service message types are not supported and are not included in the list.

### **Sample time** — Interval between outputs `–1` (default) | scalar

Interval between outputs, specified as a scalar. In simulation, the sample time follows simulation time and not actual clock time.

This default value indicates that the block sample time is *inherited*.

For more information about the inherited sample time type, see Specify Sample Time (Simulink).

### **Length of subscribe callback queue** — Message queue length `1` (default) | integer

Message queue length in code generation, specified as an integer. In simulation, the message queue is always 1 and cannot be adjusted. To ensure each message is caught, use a smaller model step or only execute the model if `IsNew` returns `1`.
## Libraries

ROS Toolbox / ROS

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

## Description

Receive messages from ROS network

The Subscribe block creates a Simulink® nonvirtual bus that corresponds to the specified ROS message type. The block uses the node of the Simulink model to create a ROS subscriber for a specific topic. This node is created when the model runs and is deleted when the model terminates. If the model does not have a node, the block creates one.

On each simulation step, the block checks if a new message is available on the
specific topic. If a new message is available, the block retrieves the message and
converts it to a Simulink bus signal. The **Msg** port outputs this new message. If
a new message is not available, **Msg** outputs the last received ROS
message. If a message has not been received since the start of the simulation,
**Msg** outputs a blank message.
