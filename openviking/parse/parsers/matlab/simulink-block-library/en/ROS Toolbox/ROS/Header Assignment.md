---
type: simulink-block
title: 'Header Assignment'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS'
documentation_page: 'headerassignment'
documentation_source_path: 'ref/headerassignment.html'
language: en
---

# Header Assignment

## Ports

### Input

### **InputMsg** — ROS message to update nonvirtual bus

ROS message with a `std_msgs/Header` field, specified as a
nonvirtual bus.

**Data Types:** `bus`
### Output

### **OutputMsg** — ROS message with an updated header nonvirtual bus

ROS message with an updated header, returned as a nonvirtual bus.

**Data Types:** `bus`

## Parameters

### **Set Frame ID** — Specify frame associated with message data `off` (default) | `on`

Select this parameter to specify the frame that the message data is associated with.
Specify the frame ID in the text box enabled when you select this parameter. The block
populates the `frame_id` field of the ROS message header with the
specified frame.

**Example:** `base_link`

### **Set Timestamp** — Set timestamp in header `off` (default) | `on`

Select this parameter to set the `stamp` value of the header to
the current ROS system time. In order to use the custom time published on the
`/clock` topic instead of the ROS system time, set the
`use_sim_time` ROS parameter to `true`.

### **Header field name** — Specify Header field name `Use the default Header field name` (default) | `Specify your own`

Specify the name of the Header field as one of the following:

- `Use the default Header field name` — The
  block sets the name of the header field in the ROS message to the default value,
  `Header`.
- `Specify your own` — Enables a text box in
  which you can specify a custom name for the header field in the ROS message.

**Example:** `my_custom_header`

## Libraries

ROS Toolbox / ROS

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

## Description

Update fields of ROS message header

The Header Assignment block updates the values in the header field of a ROS
message. When a ROS message contains a header field of type
`std_msgs/Header`, you can use this block to update the
`frame_id` and `stamp` values in its header field. During
each sample hit, the block updates the `frame_id` and
`stamp` fields in the header. The accuracy of the timestamp depends on the
step size of the solver. Smaller step sizes result in more accurate timestamps.
