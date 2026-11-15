---
type: simulink-block
title: 'Monitor Action Goal'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'Network Access / ROS 2 Network Access / ROS 2 Network Access in Simulink'
documentation_page: 'monitoractiongoalros2'
documentation_source_path: 'ref/monitoractiongoalros2.html'
language: en
---

# Monitor Action Goal

## Ports

### Input

### **UUID** — Unique ID dedicated to any goal message non-virtual bus

Unique ID dedicated to any goal message, specified as a non-virtual bus of message
type `unique_identifier_msgs/UUID`.

**Data Types:** `bus`
### Output

### **StatusCode** — Execution status of action goal corresponding to `UUID` input scalar

Execution status of action goal corresponding to the **UUID** input,
specified as an integer.

| Error Code | Condition |
| --- | --- |
| `-1` | The action server rejected the goal. |
| `0` | The action server accepted the goal but failed to set the status properly. This implies `unknown` status of the goal message. |
| `1` | The action server accepted the goal and is awaiting execution. This implies the `accepted` status of the goal message. |
| `2` | The action server accepted the goal and is currently in the process of execution. This implies the `executing` status of the accepted goal message. |
| `3` | The action server has accepted the cancel goal request initiated by the action client. This implies the `canceling` status of the accepted goal message. |
| `4` | The action server completed the goal successfully. This implies the `succeeded` status of the accepted goal message. |
| `5` | The action server canceled the goal based on an external request sent by the action client. This implies the `canceled` status of the accepted goal message. |
| `6` | The action server terminated the goal without an external request sent by the action client. This implies the `aborted` status of the accepted goal message. |

**Data Types:** `int8`

### **Result** — Result message associated with a particular action goal non-virtual bus

Result message associated with a particular action goal, specified as a
non-virtual bus.

**Data Types:** `bus`

### **Feedback** — Feedback message associated with a particular action goal non-virtual bus

Feedback message associated with a particular action goal, specified as a
non-virtual bus.

- When a feedback message is available at a particular time step, the
  **Feedback** port outputs the latest feedback.
- When a feedback message is not available at a particular time step, the
  **Feedback** port outputs the last known feedback.

#### Dependencies

This output is enabled when the **Show Feedback output port**
is checked.

**Data Types:** `bus`

### **ErrorCode** — Error conditions while monitoring action goal integer

Error conditions while monitoring an action goal, specified as an integer.

| Error Code | Condition |
| --- | --- |
| `0` | The action client sent the goal successfully and the action server accepted the goal. |
| `1` | The action client sent the goal but the action server rejected the goal. |
| `2` | The UUID input is invalid but the action server is available. |
| `3` | The action client failed to send the goal because the action server is not available. |

#### Dependencies

This output is enabled when the **Show ErrorCode output
port** is checked.

**Data Types:** `uint8`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Name** — Action name inherited from paired `Send Action Goal` block character vector

Action name inherited from paired `Send Action Goal` block,
specified as a character vector.

### **Type** — Action type inherited from paired `Send Action Goal` block character vector

Action type inherited from paired `Send Action Goal` block,
specified as a character vector.

### **Paired Send Action Goal Block** — Path to paired Send Action Goal block block path

Path to the Send Action Goal block paired with this Monitor
Action Goal block. To create a paired Send Action Goal
for the first time, click **Create paired Send Action Goal
block**.

After you create a paired Send Action Goal block, clicking the path
displays and highlights the Send Action Goal block in your model.

#### Tips

- For correct action client implementation, use only **Create paired
  Send Action Goal block** to create the Send Action Goal
  associated with this Monitor Action Goal block. Adding a
  Send Action Goal block from the library is not
  recommended.

### **Show Feedback output port** — Enable feedback output port `off` (default) | `on`

Check this box to enable the **Feedback** output.

### **Show ErrorCode output port** — Enable error code output port `off` (default) | `on`

Check this box to enable the **ErrorCode** output. If an error condition
occurs, the **Result** port outputs a blank message.

## Libraries

ROS Toolbox / ROS 2

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Usage notes and limitations:

The Monitor Action Goal block follows rate-based execution and not event-driven
execution.

## Version History

**Introduced in R2024a**

## Description

Monitor action goal in ROS 2 network

The Monitor Action Goal block enables you to monitor the status, feedback and result of an active
action goal in a ROS 2 network. This block accepts the UUID input as a Simulink non-virtual
bus of `unique_identifier_msgs/UUID` message type.

To use this block, you must have a paired Send Action Goal block
of a matching action name and type. Selections made in the Send Action Goal
block are automatically synchronized with the Monitor Action Goal block.

You can use this block to monitor these states of the action goal after it is accepted by
an action server.

ROS 2 Action Client Monitor Goal State
