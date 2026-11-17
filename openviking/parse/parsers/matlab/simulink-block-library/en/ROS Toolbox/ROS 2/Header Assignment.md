---
type: simulink-block
title: 'Header Assignment'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS 2'
documentation_page: 'headerassignmentros2'
documentation_source_path: 'ref/headerassignmentros2.html'
language: en
---

# Header Assignment

## Ports
```yaml
ports:
- name: InputMsg
  summary: ROS 2 message to update nonvirtual bus
  direction: input
  data_types: bus
- name: OutputMsg
  summary: ROS 2 message with an updated header nonvirtual bus
  direction: output
  data_types: bus
```

### Input

### **InputMsg** — ROS 2 message to update nonvirtual bus

ROS 2 message with a `std_msgs/header` field, specified as a
nonvirtual bus.

**Data Types:** `bus`
### Output

### **OutputMsg** — ROS 2 message with an updated header nonvirtual bus

ROS 2 message with an updated header, returned as a nonvirtual bus.

**Data Types:** `bus`
## Parameters
```yaml
parameters:
- name: Set Frame ID
  summary: Specify frame associated with message data off (default) | on
  group: ''
- name: Set Timestamp
  summary: Set timestamp in header off (default) | on
  group: ''
- name: Header field name
  summary: Specify Header field name Use the default Header field name (default) | Specify your own
  group: ''
```

### **Set Frame ID** — Specify frame associated with message data `off` (default) | `on`

Select this parameter to specify the frame that the message data is associated with.
Specify the frame ID in the text box enabled when you select this parameter. The block
populates the `frame_id` field of the ROS 2 message header with the
specified frame.

**Example:** `base_link`

### **Set Timestamp** — Set timestamp in header `off` (default) | `on`

Select this parameter to set the `stamp` value of the header to
the current ROS 2 system time.

### **Header field name** — Specify Header field name `Use the default Header field name` (default) | `Specify your own`

Specify the name of the Header field as one of the following:

- `Use the default Header field name` — The
  block sets the name of the header field in the ROS 2 message to the default value,
  `header`.
- `Specify your own` — Enables a text box in
  which you can specify a custom name for the header field in the ROS 2 message.

**Example:** `my_custom_header`
## Libraries

ROS Toolbox / ROS 2

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

## Description

Update fields of ROS 2 message header

The Header Assignment block updates the values in the header field of a ROS
2 message. When a ROS 2 message contains a header field of type
`std_msgs/header`, you can use this block to update the
`frame_id` and `stamp` values in its header field. During
each sample hit, the block updates the `frame_id` and
`stamp` fields in the header. The accuracy of the timestamp depends on the
step size of the solver. Smaller step sizes result in more accurate timestamps.
