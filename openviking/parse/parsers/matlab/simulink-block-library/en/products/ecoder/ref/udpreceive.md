---
type: simulink-block
title: 'UDP Receive'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Architecture and Component Design / Blocks for Embedded Targets'
documentation_page: 'udpreceive'
documentation_source_path: 'ref/udpreceive.html'
language: en
---

# UDP Receive

## Ports

### Output

### **Port\_1** — UDP packet vector

UDP packet, specified as a data vector, which is received from an IP network port.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

### **Local IP port** — Number of IP port 25000 (default) | scalar in the range [1, 65535]

Specify the IP port number on which to receive UDP
packets. This parameter is tunable in the
generated code but is not tunable during
simulation.

On Linux®, to set the IP port number below
1024, run MATLAB with root privileges. For example,
at the Linux command line, enter:

```
sudo matlab
```

### **Remote IP address ('0.0.0.0' to accept all)** — IP address from which to accept packets '0.0.0.0' (default) | IP address

Specify the IP address from which to accept UDP
packets. Specify a specific IP address to block
UDP packets from other addresses. To accept
packets from any IP
address, specify `'0.0.0.0'`.

### **Receive buffer size (bytes)** — Size of buffer that receives UDP packets 8192 (default) | scalar in the range [1, 67108864]

Specify the size of the buffer, in bytes, that
receives the UDP packets. Make the buffer large
enough to avoid data loss caused by buffer
overflows.

### **Maximum length for Message** — Maximum length of output data 255 (default) | scalar

Specify the maximum length, in vector elements, of the
data output vector. Set this parameter to a value
equal or greater than the data size of a UDP
packet. The system truncates data that exceeds
this length.

#### Parameter Dependencies

If you disable **Output
variable-size signal**, the block output
is the length specified by this parameter.

### **Data type for Message** — Data type of message uint8 (default) | single | double | int8 | int16 | int32 | int64 | uint16 | uint32 | uint64 | boolean | fixed point | enumerated | bus

Specify the data type of the vector elements in the
message output. Match the data type to the data
input used to create the UDP packets.

### **Message is complex** — Message data complexity off (default) | on

Specify whether the block receives a message as
complex data. Select this parameter to receive a
message as complex data. Clear this parameter if a
received message is real data.

### **Output variable-size signal** — Message output that varies in length on (default) | off

Specify whether your model supports signals of varying
length. If your model supports signals of varying
length, select this parameter. In that
case:

- The output vector varies in length,
  depending on the amount of data in the UDP
  packet.
- The block emits the data vector from a
  single unlabeled output.

If your model does not support signals of varying
length, clear this parameter. In that case:

- The block emits a fixed-length output that
  is the same length as specified by
  **Maximum length for Message**.
- If the UDP packet contains less data than
  the fixed-length output, the difference contains
  invalid data.
- The block emits the data vector from the
  **Message** output.
- The block emits the length of the valid data
  from the **Length**
  output.
- The **Data type for
  Length** parameter is enabled.

#### Parameter Dependencies

If you disable this parameter, the block
emits output that is the length specified by
**Maximum length for Message**.

### **Blocking time (seconds)** — Number of seconds to wait for UDP packet inf (default) | scalar

For each sample, specify the number of seconds to wait
for a UDP packet before returning control to the
scheduler. To wait indefinitely, specify
`inf`.

**Note**

This parameter applies to the Embedded Coder® UDP Receive block only.

### **Sample time (seconds)** — Frequency of calls to block 0.01 (default) | scalar

Specify the frequency at which the scheduler calls the
UDP Receive block, in seconds. Enter a value
greater than zero. In real-time operation, setting
this parameter to a smaller value reduces the
likelihood of dropped UDP messages.

## Libraries

Embedded Coder / Embedded Targets / Host Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2011a**

## Description

Receive UDP packet

The UDP Receive block receives UDP packets from an IP network port and saves them to its
buffer. Due to the nature of the UDP transmission protocol, the receiver is not guaranteed
to receive all the data packets that you send using the UDP Send block. With
each sample, the block outputs the contents of a single UDP packet as a data vector.

The local IP port number on which the block receives the UDP packets is tunable in the
generated code. The generated code for this block relies on prebuilt `.dll`
files. You can run this code outside the MATLAB® environment or redeploy it, but you must account for the extra
`.dll` files. The `packNGo` function creates a ZIP
file that contains the pieces required to run or rebuild this code. For more details, see
How To Run a Generated Executable Outside MATLAB (DSP System Toolbox).
