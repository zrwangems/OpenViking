---
type: simulink-block
title: 'Cancel Action Goal'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS 2'
documentation_page: 'cancelactiongoalros2'
documentation_source_path: 'ref/cancelactiongoalros2.html'
language: en
---

# Cancel Action Goal

## Ports

### Input

### **UUID** — Unique ID dedicated to any goal message non-virtual bus

Unique ID dedicated to any goal message, specified as a non-virtual bus of message
type `unique_identifier_msgs/UUID`.

**Data Types:** `bus`

### **Enable** — Boolean value to send cancel request for an active action goal `true` or `1` | `false` or `0`

Boolean value to send cancel request for an active action goal, specified as a
non-virtual bus set to `true (1)` or `false (0)`. If
you set the **Enable** port to `true` and a goal
corresponding to the **UUID** input is running, this block sends a cancel
goal request to the action server in the same time step.

**Data Types:** `Boolean`
### Output

### **Response** — Response message for cancel goal request non-virtual bus

Response message for cancel goal request, specified as a non-virtual bus of
`action_msgs/CancelGoalResponse` message type. If the action server
accepts the cancel goal request, the goal will transition to
`canceling` state.

**Data Types:** `bus`

### **ErrorCode** — Error conditions while canceling action goal integer

Error conditions while canceling action goal, specified as an integer.

| Error Code | Condition |
| --- | --- |
| `0` | The action client sent the cancel goal request to the action server successfully. |
| `1` | The action goal cannot be cancelled because it is rejected or already in a terminal state. Terminal state refers to one of these action goal states: - Goal is in `succeeded` state. - Goal is in `canceled` state. - Goal is in `aborted` state. |
| `2` | The action client failed to send the cancel goal request but the action server is available. |
| `3` | The action client failed to send the cancel goal request because the action server is unavailable. |

#### Dependencies

This output is enabled when the **Show ErrorCode output
port** is checked.

**Data Types:** `uint8`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Show ErrorCode output port** — Enable error code output port `off` (default) | `on`

Check this box to enable the **ErrorCode** output. If an error condition
occurs, the **Response** port outputs a blank message specified as a
non-virtual bus of `action_msgs/CancelGoalResponse` message
type.

## Libraries

ROS Toolbox / ROS 2

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Usage notes and limitations:

The Cancel Action Goal block follows rate-based execution and not event-driven
execution.

## Version History

**Introduced in R2024a**

## Description

Cancel active action goal in ROS 2 network

The Cancel Action Goal block enables you to cancel an active action goal in a ROS 2 network. This
block accepts the UUID input as a Simulink non-virtual bus of
`unique_identifier_msgs/UUID` message type.

**Note**

To use this block, you must have at least one Send Action Goal that
provides the UUID input to this block.
