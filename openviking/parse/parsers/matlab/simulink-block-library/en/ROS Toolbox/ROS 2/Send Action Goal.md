---
type: simulink-block
title: 'Send Action Goal'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS 2'
documentation_page: 'sendactiongoalros2'
documentation_source_path: 'ref/sendactiongoalros2.html'
language: en
---

# Send Action Goal

## Ports

### Input

### **Goal** — ROS 2 action goal message input non-virtual bus

ROS 2 action goal message input, specified as a non-virtual bus.

**Data Types:** `bus`

### **Enable** — Boolean value to send action goal if there is no goal running `true` | `false`

Boolean value to send action goal if there is no goal running, specified as
`1 (true)` or `0 (false)`. If there is no goal
running and the **Enable** port is `true`, the block sends
any goal message available at **Goal** input. To check if a goal is running,
use the **StatusCode**
output of the paired Monitor Action Goal block.

**Data Types:** `Boolean`
### Output

### **UUID** — Unique ID dedicated to any goal message non-virtual bus

Unique ID dedicated to any goal message, specified as a non-virtual bus of message
type `unique_identifier_msgs/UUID`.

**Data Types:** `bus`

### **ErrorCode** — Error conditions for send action goal request integer

Error conditions corresponding to the send action goal request, specified as an
integer.

| Error Code | Condition |
| --- | --- |
| `0` | The action client sent the goal successfully and the action server accepted the goal. |
| `1` | The action client sent the goal but the action server rejected the goal. |
| `2` | The action client failed to send the goal but the action server is available. |
| `3` | The action client failed to send the goal because the action server is not available. |

#### Dependencies

This output is enabled when the **Show ErrorCode output
port** is checked.

**Data Types:** `uint8`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Main

### **Source** — Source for specifying action name `Select from ROS network` | `Specify your own`

Source for specifying the action name:

- `Select from ROS network` — Use
  **Select...** to select an action name and type from a full
  list of supported ROS 2 actions. The **Name** and
  **Type** parameters are set automatically. You must be
  connected to a ROS 2 network.
- `Specify your own` — Enter an action name in
  **Name** and specify its type in **Type**. You
  must match an action name exactly.

### **Name** — ROS 2 action name character vector

ROS 2 action name, specified as a character vector. The action name must match the
one available on the ROS 2 network.

### **Type** — ROS 2 action type character vector

ROS 2 action type, specified as a character vector. Each action name has a
corresponding action type.

### **Paired Monitor Action Goal Block** — Path to paired Monitor Action Goal block block path

Path to the Monitor Action Goal  block paired with this Send
Action Goal block. To create a paired Monitor Action
Goal for the first time, click **Create paired Monitor Action Goal
block**.

After you create a paired Monitor Action Goal block, clicking the
path displays and highlights the Monitor Action Goal block in your
model.

#### Tips

For correct action client implementation, use only **Create paired
Monitor Action Goal block** to create the Monitor Action Goal
 associated with this Send Action Goal block. Adding a
Monitor Action Goal  block from the library is not
recommended.

### **Show ErrorCode output port** — Enable error code output port `off` (default) | `on`

Check this box to enable the **ErrorCode** output.

### QoS

Quality of Service (QoS) settings of action client for establishing communication with
the action server, returned as a character vector. You can set the **Goal Service QoS**, **Result Service QoS**,
**Cancel Service QoS**, **Feedback Topic
QoS** and **Status QoS** with these following
options:

### **History** — Mode of storing goal requests in the queue `Keep last` (default) | `Keep all`

Determines the mode of storing send goal requests in the queue. If the queue fills with requests waiting to be processed, then old requests will be dropped to make room for new. If set to `Keep last`, the queue stores the number of requests set by the `Depth` parameter. If set to `Keep all`, the queue stores all requests up to the MATLAB® resource limits.

### **Depth** — Size of the goal request queue `1` (default) | `non-negative scalar integer`

Size of the goal request queue, specified as a `non-negative scalar integer`. This only applies when `History` is set to `Keep last`.

### **Reliability** — Delivery guarantee of goal requests `Reliable` (default) | `Best effort`

Requirement on delivery guarantee of goal requests, specified as `Reliable` or `Best effort`. If `Reliable`, then delivery is guaranteed, but may retry multiple times. If `Best effort`, then attempt delivery and do not retry. `Reliable` setting is recommended for actions.

### **Durability** — Persistence of action goal requests `Volatile` (default) | `Transient local`

Requirement on persistence of the action goal requests, specified as
`Volatile` or `Transient
local`. If `Volatile`, then requests are
not required to persist. If `Transient local`, then the
server will require clients to persist the most recent requests specified by
`Depth`. `Volatile` setting is
recommended to prevent servers from receiving out of date requests in the event of a
server restart.

### **Deadline** — Maximum amount of time allowed between receiving a goal request and sending goal result `Inf` (default) | positive scalar

Maximum amount of time allowed between receiving a goal request and sending a goal result,
specified as a positive scalar. The `Deadline` QoS parameter of
action clients sending goal requests must be greater than or equal to the value of
the action server `Deadline` QoS parameter. The default value is
`Inf` which implies that expected interval between subsequent
messages is infinite.

### **Lifespan** — Length of time a goal request is considered valid `Inf` (default) | positive scalar

Length of time a goal request is considered valid, specified as a positive scalar. The block
does not process goal requests persisting longer than the specified lifespan in the
queue. The default value is `Inf` which implies that a goal request
is valid for infinite length of time.

### **Liveliness** — Liveliness check of action server by action client `automatic` (default)

Liveliness check of action server by action client, specified as
`automatic`. This parameter is a measure of whether the
action server is still alive.

Liveliness set to `automatic` implies that after the
action server has sent a goal response to the action client, the client considers
the server to be alive for an additional `Lease Duration`.

### **Lease Duration** — Maximum amount of time before an action client has to assert liveliness `Inf` (default) | positive scalar

Maximum amount of time before an action client has to assert liveliness, specified
as a positive scalar. The `Lease Duration` QoS parameter of
action clients sending goal requests must be greater than or equal to the value of
the action server `Lease Duration` QoS parameter. The default
value is `Inf` which implies that action client can assert its
liveliness for infinite amount of time.

### QoS Compatibility Considerations

**Note**

The quality of service (QoS) settings must be compatible between action servers and
action clients for a connection to be made.

## Libraries

ROS Toolbox / ROS 2

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Usage notes and limitations:

The generated action client from the Send Action Goal follows rate-based execution and not
event-driven execution.

## Version History

**Introduced in R2024a**

## Description

Send action goal messages to ROS 2 network

The Send Action Goal block enables you to send action goal messages to an action server
available in a ROS 2 network. It takes in a simulink non-virtual bus as its **Goal**
input, that corresponds to the specified ROS 2 action type.

To create a ROS 2 action client, create a ROS 2 Blank Message block
with class set to `Action Goal`. The output of this block is
connected to the **Goal** input of the Send Action Goal block. The action client is
associated with the node of the Simulink® model.

**Note**

To monitor an active action goal, you must first create a paired Monitor Action Goal
block. The paired block will be based on the action parameters specified in the Send
Action Goal block.

### Behavior

On each simulation step, the Send Action Goal block examines whether a
goal is currently in progress (active goal), leading to one of these possible outcomes or
occurrences:

- If true, the block ignores any goal message available at **Goal** input and
  outputs the active goal UUID as a Simulink non-virtual bus of
  `unique_identifier_msgs/UUID` message type.
- If there is no goal running and the **Enable** port is
  `true`, the block sends any goal message available at
  **Goal** input and outputs new goal UUID as a Simulink non-virtual bus of
  `unique_identifier_msgs/UUID` message type.
- If there is no goal running and the **Enable** port is
  `false`, the block ignores any goal message available at
  **Goal** input and outputs default goal UUID (empty message) as a Simulink
  non-virtual bus of `unique_identifier_msgs/UUID` message type.

ROS 2 Action Client Block Behavior
