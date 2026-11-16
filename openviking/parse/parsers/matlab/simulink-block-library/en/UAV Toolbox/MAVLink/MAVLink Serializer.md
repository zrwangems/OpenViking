---
type: simulink-block
title: 'MAVLink Serializer'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'MAVLink'
documentation_page: 'mavlinkserializer'
documentation_source_path: 'ref/mavlinkserializer.html'
language: en
---

# MAVLink Serializer

## Ports

### Input

### **Msg** — MAVLink packet nonvirtual bus

MAVLink packet as a nonvirtual bus. This is the output of the MAVLink Blank
Message block in which the values for Message ID, System ID, and Component ID are
already initialized. The fields in the Payload bus can be modified using a Bus
Assignment block before passing it as an input to MAVLink Serializer
block.

**Data Types:** `bus`
### Output

### **Data** — MAVLink data stream vector

The serialized MAVLink data for the input MAVLink message bus. MAVLink protocol
version 2 removes trailing zeros in the payload. Therefore, the length of the payload
in the serialized data can be less than the maximum payload length of the MAVLink
message in the dialect. In this case, the block outputs the serialized data stream
with the trailing zeros included.

**Data Types:** `uint8`

### **Length** — Length of the serialized data scalar

The true length of the serialized data including headers and payload. This might
be less than the maximum possible length for a MAVLink message depending on how many
trailing zeros are removed in the MAVLink payload during serialization.

**Data Types:** `uint16`

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
message definition among the available message definition names from the dropdown
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
from a full list of available MAVLink messages that are specific to the values that you
selected for **MAVLink dialect** and **MAVLink
version** parameters.

**Data Types:** `string`

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

Serialize messages of MAVLink packet by converting Simulink nonvirtual bus to uint8 data stream

The MAVLink Serializer block accepts a Simulink® nonvirtual bus and converts it into a `uint8` MAVLink data
stream. The nonvirtual bus represents a MAVLink packet containing the Message ID, System ID,
Component ID, Sequence, and Payload information corresponding to the selected MAVLink message.
Payload information is another nonvirtual bus within the MAVLink packet bus.

MAVLink v2 removes trailing zeros in the payload. Therefore, the length of the payload in
the serialized MAVLink data can be less than the maximum payload length of a selected MAVLink
message type.

The **Data** port outputs the MAVLink data stream, and the length of the
output data is the maximum possible length for the selected MAVLink message. If the length of
the serialized data is less than the maximum possible length, trailing zeros are added to the
data stream. The **Length** port outputs the true length of the serialized
MAVLink data.
