---
type: simulink-block
title: 'Read Scan'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS'
documentation_page: 'readscanblock'
documentation_source_path: 'ref/readscanblock.html'
language: en
---

# Read Scan

## Ports
```yaml
ports:
- name: Msg
  summary: ROS or ROS 2 laser scan message nonvirtual bus
  direction: input
  data_types: bus
- name: Ranges
  summary: Range values for each point array
  direction: output
  data_types: single
- name: Angles
  summary: Angle values for each point array
  direction: output
  data_types: single
- name: Intensities
  summary: Intensity value for each point array
  direction: output
  data_types: single
- name: ErrorCode
  summary: Error code for message parsing scalar
  direction: output
  data_types: uint8
```

### Input

### **Msg** — ROS or ROS 2 laser scan message nonvirtual bus

ROS 2 laser scan message, specified as a nonvirtual bus. You can use the ROS
Subscribe or the ROS 2 Subscribe
blocks to get a message from the network.

**Data Types:** `bus`
### Output

### **Ranges** — Range values for each point array

Range values for each point in the scan, returned as an array of length
*M*.

**Data Types:** `single`

### **Angles** — Angle values for each point array

Angle values for each point in the scan, returned as an array of length
*M*.

#### Dependencies

Enable `Show Angles output port` parameter.

**Data Types:** `single`

### **Intensities** — Intensity value for each point array

Intensity values for each point in the scan, returned as an array of length
*M*.

#### Dependencies

Enable `Show Intensities output port` parameter.

**Data Types:** `single`

### **ErrorCode** — Error code for message parsing scalar

Error code for message parsing, returned as a scalar. The error code values are:

- `0` — Successfully parsed the laser scan message.
- `1` — The `Data` field of the laser scan
  message was truncated.

#### Dependencies

Enable `Show ErrorCode output port` parameter.

**Data Types:** `uint8`
## Parameters
```yaml
parameters:
- name: Maximum array length
  summary: Maximum length of the laser scan array 100 (default) | positive scalar
  group: ''
- name: Show Angles output port
  summary: RGB port toggle off (default) | on
  group: ''
- name: Show Intensity output port
  summary: Intensity port toggle off (default) | on
  group: ''
- name: Show ErrorCode output port
  summary: ErrorCode port toggle on (default) | off
  group: ''
- name: Output variable-size signals
  summary: Variable-size signal output toggle off (default) | on
  group: ''
```

### **Maximum array length** — Maximum length of the laser scan array `100` (default) | positive scalar

Maximum length of the laser scan array, specified as a positive scalar.

Select **Configure using ROS...** to set this parameter
automatically using an active topic on a ROS or ROS 2 network. You must be connected to
the network.

### **Show Angles output port** — `RGB` port toggle `off` (default) | `on`

Select this parameter to enable the **Angles** port. If
you enable this parameter, the message must contain RGB data or the block returns an
error code.

### **Show Intensity output port** — `Intensity` port toggle `off` (default) | `on`

Select this parameter to enable the **Intensity** port.
If you enable this parameter, the message must contain intensity data or the block
returns an error code.

### **Show ErrorCode output port** — `ErrorCode` port toggle `on` (default) | `off`

Select this parameter to enable the **ErrorCode** port
and monitor errors.

### **Output variable-size signals** — Variable-size signal output toggle `off` (default) | `on`

Toggle whether to output a variable-size signal. Use variable-sized signals only if
you expect the image size to change over time. For more information about variable-size
signals, see Variable-Size Signal Basics (Simulink).
## Libraries

ROS Toolbox / ROS ROS Toolbox / ROS 2

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

## Description

Extract scan data from ROS or ROS 2 laser scan message

The Read Scan block extracts range, scan and intensity data from a ROS or
ROS 2 laser scan message. You can select the message parameters of a topic active on a live
ROS or ROS 2 network, or specify the message parameters separately. The input messages are
specified as a nonvirtual bus. Use the ROS Subscribe or the ROS 2 Subscribe block to
receive a message from the network and input the message to the Read Scan
block. For ROS and ROS 2 models, you must use the blocks in the respective ROS and ROS 2
library.
