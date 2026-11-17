---
type: simulink-block
title: 'Publish'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS'
documentation_page: 'publish'
documentation_source_path: 'ref/publish.html'
language: en
---

# Publish

## Ports
```yaml
ports:
- name: Msg
  summary: ROS message nonvirtual bus
  direction: input
  data_types: bus
```

### Input

### **Msg** — ROS message nonvirtual bus

ROS message, specified as a nonvirtual bus. To specify the type of ROS message, use the **Message type** parameter.

**Data Types:** `bus`
## Parameters
```yaml
parameters:
- name: Topic source
  summary: Source for specifying topic name Select from ROS network | Specify your own
  group: ''
- name: Topic
  summary: Topic name to publish to string
  group: ''
- name: Message type
  summary: ROS message type string
  group: ''
- name: Length of publish queue
  summary: Message queue length 1 (default) | integer
  group: ''
```

### **Topic source** — Source for specifying topic name `Select from ROS network` | `Specify your own`

Source for specifying the topic name, specified as one of the following:

- `Select from ROS network`
  — Use **Select** to select a topic name. The **Topic** and **Message type** parameters are set automatically. You must be connected to a ROS network.
- `Specify your own`
  — Enter a topic name in **Topic** and specify its message type in **Message type**. You must match a topic name exactly.

### **Topic** — Topic name to publish to string

Topic name to publish to, specified as a string. When **Topic source** is set to `Select from ROS network`, use **Select** to select a topic from the ROS network. You must be connected to a ROS network to get a list of topics. Otherwise, set **Topic source** to `Specify your own` and specify the topic you want.

### **Message type** — ROS message type string

ROS message type, specified as a string. Use **Select** to select from a full list of supported ROS messages. Service message types are not supported and are not included in the list.

### **Length of publish queue** — Message queue length `1` (default) | integer

Message queue length in code generation, specified as an integer. In
simulation, the message queue is always 1 and cannot be adjusted. To ensure
each message is processed, use a smaller model step or only execute the
model when publishing a new message.
## Libraries

ROS Toolbox / ROS

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

## Description

Send messages to ROS network

The Publish block takes in as its input a Simulink® nonvirtual bus that corresponds to the specified ROS message type and publishes it to the ROS network. It uses the node of the Simulink model to create a ROS publisher for a specific topic. This node is created when the model runs and is deleted when the model terminates. If the model does not have a node, the block creates one.

On each sample hit, the block converts the **Msg** input from a
Simulink bus signal to a ROS message and publishes it. The block does not
distinguish whether the input is a new message but merely publishes it on every sample
hit. For simulation, this input is a MATLAB® ROS message. In code generation, it is a C++ ROS message.
