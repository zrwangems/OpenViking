---
type: simulink-block
title: 'MAVLink Deserializer'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'MAVLink Support'
documentation_page: 'mavlinkdeserializer'
documentation_source_path: 'ref/mavlinkdeserializer.html'
language: en
---

# MAVLink Deserializer

## Ports

### Input

### **Data** — MAVLink data stream vector

The `uint8` byte stream that contains serialized MAVLink packets.
The byte stream is usually received over a communication channel such as UDP, TCP, or
Serial. At each sample time, the communication channel receives data and returns a
byte stream that contains one or more MAVLink packets. The byte stream can also return
a MAVLink packet partially in over multiple sample times. This input port accepts
variable-length signals.

**Data Types:** `uint8`

### **Length** — Length of valid MAVLink data at Data input port scalar

Optional input port to include the length of valid MAVLink data. To enable this
port, select the **Input data stream length is available** parameter.
Use this option when you know the exact length of the valid MAVLink data in the data
stream.

This option is useful when you have a communication channel receive peripheral
that outputs partially received data that contains trailing zeros. Such peripherals
also output the length of the actual number of valid data bytes received. You can
connect the length output of the peripheral directly with the
**Length** input port of MAVLink Deserializer block,
so that trailing zeros in the input byte stream do not affect the decoding
logic.

**Data Types:** `uint16`
### Output

### **IsNew** — New message indicator `0` | `1`

New MAVLink message indicator returned as a logical. A value of
`1` indicates that a new message is available since the last sample
was received by the block. This output can be used to trigger subsystems to process
new messages received from the MAVLink Deserializer block.

**Data Types:** `Boolean`

### **Msg** — MAVLink packet nonvirtual bus

MAVLink packet, returned as a nonvirtual bus. The type of Payload in the MAVLink
packet is a Simulink bus corresponding to the MAVLink message specified in the MAVLink
message type parameter. The block outputs blank messages until it receives a message
on the message name that you specify. The **Msg** port outputs this
new message. If a new message is not available, it outputs the last received MAVLink
message. If a message has not been received since the start of the simulation,
**Msg** port outputs a blank MAVLink message.

**Data Types:** `bus`

## Parameters

#### Main

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

If the parameter **MAVLink dialect source** parameter is set to
`Specify your own`, you need to specify the message
definition file (.`xml`) that is on the current MATLAB path, or you can
provide the full path of the XML file.

### **MAVLink version** — MAVLink protocol version `2` (default) | `1`

MAVLink protocol version that the block uses to serialize and deserialize the
MAVLink messages.

### **MAVLink Message type** — MAVLink message `HEARTBEAT` (default)

MAVLink message, specified as a string. Click **Select** to select
from a full list of available MAVLink messages. The list varies based on the values that
you selected for **MAVLink dialect** and **MAVLink
version** parameters.

**Data Types:** `string`

#### Advanced

### **Input data stream length is available** — Length of valid MAVLink data in the input byte stream is known `off` (default) | `on`

When you select this option, the MAVLink Deserializer block provides
an additional input port called **Length**. This input port can be used
to pass the actual length of MAVLink data (if known) in the input byte stream. The input
byte stream is cropped for this length.

This option is useful when you have a communication channel receive peripheral that
outputs partially received data that contains trailing zeros. Such peripherals also
output length of the actual number of valid data bytes received. You can connect the
length output of the peripheral directly to the **Length** input port
of MAVLink Deserializer block so that trailing zeros in the input byte
stream do not affect the decoding logic.

### **Filter output MAVLink messages by System ID** — Filter received messages by System ID `off` (default) | `on`

Select this option to filter the received MAVLink messages for the System ID value
mentioned in the **System ID** parameter. This option helps you to
filter the received messages by both System ID and Component ID.

### **System ID** — System ID value `1` (default) | scalar in the range `[0,255]`

Specify the System ID value to use while filtering the decoded MAVLink messages. The
block outputs the received MAVLink messages whose System ID matches the specified value
and whose Message ID matches the MAVLink message (selected in the **MAVLink
Message type** parameter).

#### Dependencies

To enable this parameter, select **Filter Output MAVLink messages by
System ID**.

### **Filter output MAVLink messages by Component ID** — Filter received messages by System ID and Component ID `off` (default) | `on`

Select this option to filter the received MAVLink messages for the both the System
ID and the Component ID mentioned in the **System ID** and
**Component ID** parameters, respectively.

#### Dependencies

This parameter appears only if you select the **Filter output MAVLink
messages by System ID** parameter.

### **Component ID** — Component ID value `1` (default) | [`0,255`]

Specify the Component ID value to use while filtering the decoded MAVLink messages.
The block outputs those received MAVLink messages whose System ID and Component ID
values match the specified values in the **System ID** and
**Component ID** parameters, respectively, and whose Message ID
matches the MAVLink message (selected in the **MAVLink Message type**
parameter).

#### Dependencies

To enable this parameter, select **Filter Output MAVLink messages by
Component ID**.

### **Queue MAVLink messages in output** — Enable queuing of the received MAVLink messages `off` (default) | `on`

Select this option to output messages using the first-in-first-out pattern. If you
do not select this option, the MAVLink Deserializer block outputs the
latest received MAVLink message for the selected **MAVLink message
type** (and with matching System ID and Component ID if those parameters are
selected) at each simulation step. If more than one message matches the given parameters
that are received in a simulation step, the latest message is passed as output, and the
rest are discarded. You can reverse this behavior by selecting this option.

When you select this parameter, the behavior of the MAVLink
Deserializer block at each simulation step is:

- The block stores the decoded MAVLink messages matching the selected MAVLink
  message type (and matching System ID and Component ID if the those parameters are
  selected) in a queue. If there are no messages among the received messages that
  match the required parameters, no messages are queued.
- If the queue is not empty, the first message in the queue is sent as an output
  first, and the signal at **IsNew** port is set to
  `1`.

Selecting the **Queue MAVLink messages in output** parameter makes
the **Number of messages to be queued** parameter visible. You can fix
the size of the queue by setting the value of this parameter.

### **Number of messages to be queued** — Size of MAVLink message queue `50` (default) | scalar in the range (`0,65535`]

Specify the size of the queue to be used to store the received MAVLink messages
matching the desired parameters.

#### Dependencies

To enable this parameter, select **Queue MAVLink messages in
output**.

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

Convert serialized uint8 MAVLink data stream to Simulink nonvirtual bus

The MAVLink Deserializer block receives a `uint8` buffer
and decodes the buffer for MAVLink messages. Once the block receives the MAVLink message for
the selected MAVLink message type, the block outputs a Simulink® nonvirtual bus representing a MAVLink packet containing the Message ID, System
ID, Component ID, Sequence, and Payload information corresponding to the selected MAVLink
message type.

At each simulation step, the block decodes the input `uint8` buffer and
retrieves the MAVLink messages that are received after decoding. If a new message for the
selected MAVLink message type has been received, the block retrieves that message from the
list of received messages and converts it to a Simulink nonvirtual bus signal.

The MAVLink decoding logic in the block takes care of scenarios where a MAVLink packet has
been received partially from a communication channel. The MAVLink Deserializer
block internally stores the current state of parsing and resumes decoding from the previous
step when the new buffer has been received over the communication channel. If the complete
MAVLink packet has been received and the received checksum matches the computed checksum for
the received bytes, then this indicates that a MAVLink message has been received. Storing the
state of parsing ensures that the block can decode the MAVLink packets received in multiple
parts.

By default, the block outputs the latest received MAVLink message for the selected MAVLink
message type (if received). This behavior can be changed by selecting **Queue
Messages in output** parameter. In this case, all the received MAVLink messages
for the desired type are queued and at each Simulation step, the block outputs the oldest
message.
