---
type: simulink-block
title: 'Blank Message'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS 2'
documentation_page: 'blankmessageros2'
documentation_source_path: 'ref/blankmessageros2.html'
language: en
---

# Blank Message

## Ports

### Output

### **Msg** — Blank ROS 2 message non-virtual bus

Blank ROS 2 message, returned as a non-virtual bus. To specify the type of ROS
message, use the **Type** parameter. All elements of the bus are
initialized to 0. The lengths of the variable-length arrays are also initialized to
`0`.

**Data Types:** `bus`

## Parameters

### **Class** — Class of ROS 2 message `Message` (default) | `Service Request` | `Service Response` | `Action Goal` | `Action Feedback` | `Action Result`

Class of ROS 2 message, specified as `Message`, `Service
Request`, `Service Response`, `Action
Goal`, `Action Feedback` and `Action Result`.

For basic publishing and subscribing, use the `Message` class. To
create a service request message for Call Service
input, use the `Service Request` class. To create an action goal
message for **Goal** input of Send Action Goal,
use the `Action Goal` class. You can use the `Action
Feedback` or `Action Result` classes to create an action
feedback message or action result message of specific type respectively.

### **Message type** — ROS 2 message type `'geometry_msgs/Point'` (default) | character vector | dialog box selection

ROS 2 message type, specified as a character vector or a dialog box
selection. Use **Select** to select from a list of supported ROS
messages. The list of messages given depends on the **Class** of
message you select.

### **Sample time** — Interval between outputs `Inf` (default) | positive numeric scalar

Interval between outputs, specified as a numeric scalar. The default value indicates
that the block output never changes. Using this value speeds simulation by eliminating
the need to recompute the block output. Otherwise, the block outputs a new blank message
at each interval of **Sample time**.

For more information, see Specify Sample Time (Simulink).

## Libraries

ROS Toolbox / ROS 2

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

## Description

Create blank ROS 2 message using specified message type

The Blank Message block creates a Simulink® nonvirtual bus corresponding to the selected ROS message type. The block creates
ROS message buses that work with Publish, Subscribe, Call Service and Send Action Goal
blocks.
