---
type: simulink-block
title: 'UDP Receive'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'udpreceive'
documentation_source_path: 'ref/udpreceive.html'
language: en
---

# UDP Receive

## Ports
```yaml
ports:
- name: Message
  summary: Data received vector
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
- name: Length
  summary: Length of data packet scalar
  direction: output
  data_types: uint16
```

### Output

### **Message** — Data received vector

Data received by the UDP Receive block, returned as a
one-dimensional vector of the data type specified in **Data type for
Message**. If you select **Message is complex**, the block
treats the received message as complex data.

If the packet gets dropped during transmission and the receiver does not receive
the packet, the data received output is empty.

This port is unnamed until you clear the **Output variable-size
signal** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
**Complex Number Support:** Yes

### **Length** — Length of data packet scalar

Length of the data packet received, returned as a scalar. This value is determined
by the value of the **Maximum length for Message** parameter.

#### Dependencies

This port appears only when you clear the **Output variable-size
signal** parameter.

**Data Types:** `uint16`
## Parameters
```yaml
parameters:
- name: Local IP port
  summary: Number of IP port 25000 (default) | scalar in the range [1, 65535]
  group: ''
- name: Remote IP address ('0.0.0.0' to accept all)
  summary: IP address from which to accept packets '0.0.0.0' (default) | IP address
  group: ''
- name: Receive buffer size (bytes)
  summary: Size of buffer that receives UDP packets 8192 (default) | scalar in the range [1, 67108864]
  group: ''
- name: Maximum length for Message
  summary: Maximum length of output data 255 (default) | scalar
  group: ''
- name: Data type for Message
  summary: Data type of message uint8 (default) | single | double | int8 | int16 | int32 | uint16 | uint32 | boolean
  group: ''
- name: Message is complex
  summary: Message data complexity off (default) | on
  group: ''
- name: Output variable-size signal
  summary: Message output that varies in length on (default) | off
  group: ''
- name: Sample time (seconds)
  summary: Frequency of calls to block 1 (default) | scalar
  group: ''
```

### **Local IP port** — Number of IP port 25000 (default) | scalar in the range [1, 65535]

Specify the IP port number on which to receive UDP packets. This parameter is
tunable in the generated code but is not tunable during simulation.

On Linux®, to set the IP port number below 1024, run MATLAB with root privileges. For example, at the Linux command line, enter `sudo matlab`.

### **Remote IP address ('0.0.0.0' to accept all)** — IP address from which to accept packets '0.0.0.0' (default) | IP address

Specify the IP address from which to accept UDP packets. Specify a specific IP
address to block UDP packets from other addresses. To accept packets from
any IP address, specify `'0.0.0.0'`.

### **Receive buffer size (bytes)** — Size of buffer that receives UDP packets 8192 (default) | scalar in the range [1, 67108864]

Specify the size of the buffer, in bytes, that receives the UDP packets. Make the
buffer large enough to avoid data loss caused by buffer overflows.

### **Maximum length for Message** — Maximum length of output data 255 (default) | scalar

Specify the maximum length, in vector elements, of the data output vector. Set this
parameter to a value equal to or greater than the data size of a UDP packet. The system
truncates data that exceeds this length.

If you disable **Output variable-size signal**, the block output is
the length specified by this parameter.

### **Data type for Message** — Data type of message `uint8` (default) | `single` | `double` | `int8` | `int16` | `int32` | `uint16` | `uint32` | `boolean`

Specify the data type of the vector elements in the message output. Match the data
type to the data input used to create the UDP packets.

### **Message is complex** — Message data complexity off (default) | on

Specify whether the block receives a message as complex data. Select this parameter
to receive a message as complex data. Clear this parameter if a received message is real
data.

### **Output variable-size signal** — Message output that varies in length on (default) | off

Specify whether your model supports signals of varying length. If your model
supports signals of varying length, select this parameter. In that case:

- The output vector varies in length, depending on the amount of data in the UDP
  packet.
- The block emits the data vector from a single unlabeled output.

If your model does not support signals of varying length, clear this parameter. In
that case:

- The block emits a fixed-length output that is the same length as specified by
  **Maximum length for Message**.
- If the UDP packet contains less data than the fixed-length output, the
  difference contains invalid data.
- The block emits the data vector from the **Message**
  output.
- The block emits the length of the valid data from the
  **Length** output.

If you disable this parameter, the block emits output that is the length specified
by **Maximum length for Message**.

### **Sample time (seconds)** — Frequency of calls to block `1` (default) | scalar

Specify the frequency at which the scheduler calls the UDP Receive block, in
seconds. Enter a value greater than zero. In real-time operation, setting this parameter
to a smaller value reduces the likelihood of dropped UDP messages.
## Libraries

DSP System Toolbox / Sources

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Usage notes and limitations:

- The executable generated from this block relies on prebuilt dynamic library files
  (`.dll` files) included with MATLAB. Use the `packNGo` function to package the code
  generated from this block and all the relevant files in a compressed ZIP file. Using
  this ZIP file, you can relocate, unpack, and rebuild your project in another development
  environment where MATLAB is not installed. For more details, see How To Run a Generated Executable Outside MATLAB.
- The **Local IP port** parameter is tunable in the generated code,
  but not tunable during simulation. You can control the parameter tunability in the
  generated code in several ways. One of the ways is to configure the parameter as a
  tunable field of a global structure in the generated code. Other ways include applying a
  built-in storage class or custom storage class to a `Simulink.Parameter`
  object and using this object to set the value of the block parameter. For details, see
  Create Tunable Calibration Parameter in the Generated Code (Simulink Coder).

## Version History

**Introduced in R2010a**

## Description

Receive UDP packets on a given IP port

The UDP Receive block receives UDP packets from an IP network port and saves them to its
buffer. Due to the nature of the UDP transmission protocol, the receiver is not guaranteed
to receive all the data packets that you send using the UDP Send block. With
each sample, the block outputs the contents of a single UDP packet as a data vector.

The local IP port number on which the block receives the UDP packets is tunable in the
generated code. The generated code for this block relies on prebuilt `.dll`
files. You can run this code outside the MATLAB® environment or redeploy it, but you must account for the extra
`.dll` files. The `packNGo` function creates a ZIP
file that contains the pieces required to run or rebuild this code. For more details, see
How To Run a Generated Executable Outside MATLAB.
