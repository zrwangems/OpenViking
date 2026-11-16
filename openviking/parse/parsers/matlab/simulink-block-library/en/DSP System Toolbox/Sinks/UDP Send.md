---
type: simulink-block
title: 'UDP Send'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'udpsend'
documentation_source_path: 'ref/udpsend.html'
language: en
---

# UDP Send

## Ports

### Input

### **Input** — Input data vector vector

Specify the input data vector that the block transmits as a UDP packet.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
**Complex Number Support:** Yes

## Parameters

### **Remote IP address ('255.255.255.255' for broadcast)** — IP address from which to accept UDP packets `'127.0.0.1'` (default) | IP address | string

Specify the IP address or host name to which to send UDP packets. If you specify a
host name, specify it as a string. To broadcast a UDP packet, specify
`'255.255.255.255'`.

### **Remote IP port** — Number of remote IP port 25000 (default) | scalar in the range [1, 65535]

Specify the IP port number to which to send UDP packets. This parameter is tunable
in the generated code but is not tunable during simulation.

On Linux®, to set the IP port number below 1024, run MATLAB with root privileges. For example, at the Linux command line, enter `sudo matlab`.

### **Local IP port source** — Source of local IP port `Automatically determine` (default) | `Specify via dialog`

Specify whether the block uses a local port number that the system assigns or that
you specify by using the **Local IP port** parameter. For the system to
assign the port number, select `Automatically determine`. If
the receiving address expects UDP packets from a specific port number, select
`Specify via dialog` and specify the port number by using the
**Local IP port** parameter.

### **Local IP port** — Number of local IP port -1 (default) | scalar in the range [1, 65535]

Specify the IP port number from which the block sends UDP packets. Use this
parameter when the receiving address expects messages from a specific port
number.

#### Parameter Dependencies

To enable this parameter, set **Local IP port source**  to
`Specify via dialog`.

### **Send buffer size (bytes)** — Size of buffer that sends UDP packets 8192 (default) | scalar in the range [1, 67108864]

Specify the size of the buffer, in bytes, that sends the UDP packets. Make the
buffer large enough to avoid data loss caused by buffer overflows.

## Libraries

DSP System Toolbox / Sinks

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Usage notes and limitations:

- The executable generated from this block relies on prebuilt dynamic library files
  (`.dll` files) included with MATLAB. Use the `packNGo` function to package the code
  generated from this block and all the relevant files in a compressed ZIP file. Using
  this ZIP file, you can relocate, unpack, and rebuild your project in another development
  environment where MATLAB is not installed. For more details, see How To Run a Generated Executable Outside MATLAB.
- The **Remote IP port** parameter is tunable in the generated code,
  but not tunable during simulation. You can control the parameter tunability in the
  generated code through several ways. One of the ways is to configure the parameter as a
  tunable field of a global structure in the generated code. Other ways include applying a
  built-in storage class or custom storage class to a `Simulink.Parameter`
  object and using this object to set the value of the block parameter. For details, see
  Create Tunable Calibration Parameter in the Generated Code (Simulink Coder).

## Version History

**Introduced in R2010a**

## Description

Send UDP message

The UDP Send block sends data packets over the network using the User
Datagram Protocol (UDP). UDP is a simple message-based connectionless protocol and does not
have an end-to-end connection. The protocol sends data packets in one direction from source
to destination without verifying the readiness of the receiver. The protocol has no
handshaking mechanism. The data packets can get dropped for several reasons. There is no
acknowledgement, retransmission, or timeout in UDP. However, UDP is a very simple
transmission protocol and is suitable for time-sensitive applications where dropping packets
is preferable to waiting for packets delayed due to retransmission.

The UDP Send block transmits an input data vector as a UDP packet to a
remote IP network port. The remote IP port number to which the block sends the UDP packets
is tunable in the generated code.

Some Simulink® blocks and `.exe` files built from models that contain those
blocks require shared libraries, such as `.dll` files on Windows®. The UDP Send block requires the
`networkdevice.dll` library file. To meet this requirement, follow the
example on the `packNGo` (Simulink Coder) function page to package the code
files for your model. The resulting compressed folder contains the `.dll`
files that the model requires, including `networkdevice.dll`. To run this
type of `.exe` file outside of a MATLAB® environment, place the required `.dll` files in the same
folder as the `.exe` file or place them in a folder on the Windows system path. For more details, see How To Run a Generated Executable Outside MATLAB.
