---
type: simulink-block
title: 'MAVLink Blank Message'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'MAVLink'
documentation_page: 'mavlinkblankmessage'
documentation_source_path: 'ref/mavlinkblankmessage.html'
language: en
---

# MAVLink Blank Message

## Ports

### Output

### **Msg** — MAVLink packet nonvirtual bus

MAVLink packet, returned as a Simulink nonvirtual bus. The bus contains the fields
Message ID, System ID, Component ID, Sequence, and Payload. The Payload is another
nonvirtual bus corresponding to the MAVLink message type that you selected in the
**MAVLink message type** parameter. The Message ID is initialized
to the numeric value of the selected MAVLink message ID. The System ID and Component
ID are initialized to the corresponding **System ID** and
**Component ID** parameters.

**Data Types:** `bus`

## Parameters

### **MAVLink dialect source** — Source for specifying the MAVLink message definition `Select from standard MAVLink dialects` (default) | `Specify your own`

Source for specifying the MAVLink message definition XML name, specified as one of
the following:

- `Select from standard MAVLink dialects` - Use this option to
  select a definition XML among the 12 commonly used message definition XML names
  listed in the **MAVLink dialect** parameter.
- `Specify your own` - Enter an XML name in the text box that
  appears for the **MAVLink dialect** parameter.

### **MAVLink dialect** — Message definition to parse for MAVLink messages `common.xml` (default) | string

MAVLink message definition file (.`xml`) to parse for MAVLink
messages, specified as a string.

If the **MAVLink dialect source** parameter is set to
`Select from standard MAVLink dialects`, you need to select a
message definition among the available message definition names from the drop down
list.

If the **MAVLink dialect source** parameter is set to
`Specify your own`, you need to specify the message
definition file (.`xml`) that is on current MATLAB path or you can
provide the full path of the XML file.

### **MAVLink version** — MAVLink protocol version `2` (default) | `1`

MAVLink protocol version that is used to serialize and deserialize the MAVLink
messages.

### **MAVLink Message type** — MAVLink message `HEARTBEAT` (default)

MAVLink message, specified as a string. Click **Select** to select
from a full list of available MAVLink messages that depends on the values that you
selected for **MAVLink dialect** and **MAVLink
version** parameters.

**Data Types:** `string`

### **System ID** — System ID of the sender `1` (default)

MAVLink system ID, specified as a positive integer between 1 and 255. MAVLink
protocol only supports up to 255 systems. Each UAV has its own system ID, but multiple
UAVs can be considered as one system.

**Data Types:** `uint8`

### **Component ID** — Component ID of the sender `1` (default)

MAVLink component ID, specified as a positive integer between 1 and 255.

**Data Types:** `uint8`

### **Sample time** — Interval between outputs `inf` (default) | scalar

The default value (`inf`) indicates that the block output never
changes. If you use this value, the simulation and code generation are faster by
eliminating the need to recompute the block output. For other values, the block outputs
a new blank message at each interval of Sample time.

For more information, see Specify Sample Time (Simulink) (Simulink).

**Data Types:** `uint8`

## Libraries

UAV Toolbox / MAVLink

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Usage and Limitations:

- The C/C++ code generated for the block can be deployed only on a Linux target or a
  Speedgoat.

## Version History

**Introduced in R2020b**

## Description

Create blank MAVLink message bus by specifying payload information and MAVLink message type

The MAVLink Blank Message block creates a Simulink® nonvirtual bus representing a MAVLink packet based on the specified Message ID,
System ID, Component ID, Sequence, Payload information, and MAVLink message type.

Payload information is another nonvirtual bus within the MAVLink packet bus. The block
creates Simulink buses for the MAVLink packet and the corresponding message that work with
MAVLink Serializer and MAVLink Deserializer blocks. On each
sample hit, the block outputs a blank or zero signal for the payload for the designated
message type.

All elements of the bus other than the Message ID, System ID, and Component ID are
initialized to `0`. The only exception is the
`mavlink_version` field in the HEARTBEAT message
of the `common.xml` dialect which is initialized to
`3`.
