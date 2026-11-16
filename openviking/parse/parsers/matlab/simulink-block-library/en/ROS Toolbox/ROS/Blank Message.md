---
type: simulink-block
title: 'Blank Message'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS'
documentation_page: 'blankmessage'
documentation_source_path: 'ref/blankmessage.html'
language: en
---

# Blank Message

## Ports

### Output

### **Msg** — Blank ROS message nonvirtual bus

Blank ROS message, returned as a nonvirtual bus. To specify the type
of ROS message, use the **Type** parameter. All
elements of the bus are initialized to 0. The lengths of the
variable-length arrays are also initialized to 0.

**Data Types:** `bus`

## Parameters

### **Class** — Class of ROS message `Message` (default) | `Service Request` | `Service Response`

Class of ROS message, specified as `Message`, `Service Request`, or `Service Response`. For basic publishing and subscribing, use the `Message` class.

### **Type** — ROS message type `'geometry_msgs/Point'` (default) | character vector | dialog box selection

ROS message type, specified as a character vector or a dialog box selection. Use **Select** to select from a list of supported ROS messages. The list of messages given depends on the **Class** of message you select.

### **Sample time** — Interval between outputs `Inf` (default) | numeric scalar

Interval between outputs, specified as a numeric scalar. The default value
indicates that the block output never changes. Using this value speeds
simulation by eliminating the need to recompute the block output. Otherwise,
the block outputs a new blank message at each interval of **Sample
time**.

For more information, see Specify Sample Time (Simulink).

## Libraries

ROS Toolbox / ROS

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

## Description

Create blank message using specified message type

The Blank Message block creates a Simulink® nonvirtual bus corresponding to the selected ROS message type. The block creates ROS message buses that work with Publish, Subscribe, or Call Service blocks. On each sample hit, the block outputs a blank or “zero” signal for the designated message type. All elements of the bus are initialized to 0. The lengths of the variable-length arrays are also initialized to 0.
