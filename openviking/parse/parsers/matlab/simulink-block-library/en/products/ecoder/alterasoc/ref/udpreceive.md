---
type: simulink-block
title: 'UDP Receive'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Intel SoC Devices / Modeling'
documentation_page: 'udpreceive'
documentation_source_path: 'alterasoc/ref/udpreceive.html'
language: en
---

# UDP Receive

## Ports

### Output

### **Message** — Received messages N-by-1 array

The UDP Receive block outputs the received UDP packets as an N-by-1
data vector. The **Data type for Message** and **Maximum
length for Message** parameters set the vector data type and message
length, N, respectively.

This port is unnamed while **Output variable-size signal** is
enabled.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Length** — Length of the Message vector positive scalar

This port outputs the length of the message vector signal on port
`Message`.

This port is hidden while **Output variable-size signal** is
enabled.

**Data Types:** `single`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

### **Local IP port** — Local IP port `25000` (default) | `1 .. 65535`

Enter the IP port number on your hardware board that receives UDP data
packets.

**Note**

On Linux®, to set the IP port number below 1024, run MATLAB® with root privileges. For example, at the Linux command line, enter:

```
sudo matlab
```

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `localPort` |

### **Remote IP address** — Remote IP address `'0.0.0.0'` (default) | character vector

Enter the IP address from which to accept packets. Entering a specific IP address
blocks UDP packets from other addresses. To accept packets from any IP address, enter
`'0.0.0.0'`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `remotePort` |

### **Receive buffer size (bytes)** — Receive buffer size `8192` (default) | positive integer scalar

Make the receive buffer large enough to avoid data loss caused by buffer
overflows.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `recvBufferSize` |

### **Maximum length for Message** — Maximum length for Message `255` (default) | positive integer

Enter the maximum length, in vector elements, of the data output vector. Set this
parameter to a value greater than or equal to the data size of a UDP packet. The system
truncates data that exceeds this length.

If you disable **Output variable-size signal**, the block outputs a
fixed-length output the same length as the **Maximum length for
Message**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `dims` |

### **Data type for Message** — Data type for Message `uint8` (default) | `single` | `double` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

Set the data type of the vector elements in the Message output. Match the data type
with the data input used to create the UDP packets.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `signalDatatype` |

### **Output variable-size signal** — Output variable-size signal `on` (default) | `off`

To support signals of varying length in your model, select this parameter. To
support fixed-length signals, clear this parameter. When you clear this parameter, the block:

- Emits a data vector of fixed-length, set by the **Maximum length for
  Message**, from the **Message** output.
- Emits the length of the valid data from the **Length**
  output.
- If the UDP packet contains less data than the fixed-length output, the
  difference contains invalid data.

In both cases, the block truncates data that exceeds **Maximum
length for Message**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `isVarSize` |

### **Blocking time (seconds)** — Time to wait for UDP packet `inf` (default) | positive scalar

For each sample, wait this length of time for a UDP packet before returning control
to the scheduler. This value defaults to `inf`, which indicates to wait
indefinitely.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `blockingTime` |

### **Sample time (seconds)** — Sample time `0.01` (default) | positive scalar

Specify how often the scheduler runs this block. Enter a value greater than zero. In
real-time operation, setting this option to a large value reduces the likelihood of
dropped UDP messages.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `sampletime` |

## Libraries

Embedded Coder Support Package for Intel SoC Devices

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2014b**

## Description

Receive UDP data

The UDP Receive block receives user datagram protocol (UDP) packets from an IP network
port and saves them to its buffer. With each sample, the block outputs the contents of a
single UDP packet as a data vector.
