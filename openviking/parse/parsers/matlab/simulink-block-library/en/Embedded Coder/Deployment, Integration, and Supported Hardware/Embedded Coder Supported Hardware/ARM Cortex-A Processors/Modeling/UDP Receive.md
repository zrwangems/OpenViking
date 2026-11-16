---
type: simulink-block
title: 'UDP Receive'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / ARM Cortex-A Processors / Modeling'
documentation_page: 'udpreceive'
documentation_source_path: 'armcortexa/ref/udpreceive.html'
language: en
---

# UDP Receive

## Ports

### Output

### **Port\_1** — UDP data received numeric vector

UDP data received from remote host, returned as a numeric vector. Set the data
type of this output by using the **Data type for Message**
parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

### **Local IP port** — IP Port on remote host `25000` (default) | `1 .. 65535`

Specify the local IP port number of the application on the hardware board on which
you want to receive UDP packets. The port number must be an integer from 1 to
65,535.

**Note**

On Linux®, to set the local IP port number below 1024, run MATLAB® with root privileges. For example, at the Linux command line, enter:

```
sudo matlab
```

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `localPort` |

### **Remote IP address ('0.0.0.0' to accept all)** — Remote IP address to listen `'0.0.0.0'` (default) | valid IP address

Specify the IP address from which the block accepts UDP packets. Entering a specific
IP address blocks, UDP packets from other addresses. To accept packets from all IP
addresses,use default value `'0.0.0.0'`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `remoteURL` |

### **Receive buffer size (bytes)** — Maximum number of data bytes in received data `8192` (default) | positive integer

Specify the size of the buffer size in which you want to store the received UDP
packets. Specify the receive buffer size to be large enough to avoid data loss caused by
buffer overflows.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `recvBufferSize` |

### **Maximum length for Message** — Maximum length of output UDP data `255` (default) | positive integer

Specify the maximum length of the output UDP data. This value must be greater than
or equal to the data size of a UDP packet. The system truncates any data that exceeds
this length.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `dims` |

### **Data type for Message** — Data type of output data `uint8` (default) | `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

Select the data type of the output UDP data. This data type must be the same as the
data type of UDP message sent by the remote host.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `signalDataType` |

### **Output variable-size signal** — Enable or disable variable output signal size `off` (default) | `on`

Select the **Output variable-size signal** if your model supports
signals for varying length. In this case:

- The output vector varies in length, depending on the amount of data in the UDP
  data received.
- The block emits the data vector from a single unlabeled output.

Clear the **Output variable-size signal** if your model does not
support signals of varying length. In this case:

- The block emits a fixed-length output of the same length as the
  **Maximum length for Message**.
- If the UDP packet contains less data than the fixed-length output, the
  difference contains invalid data.
- The **Data type for length** parameter is enabled.

In both cases, the block truncates data that exceeds **Maximum length for
Message**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `isVarSize` |

### **Blocking time (seconds)** — Time to wait for UDP packet `inf` (default) | nonnegative scalar

Specify the duration of wait time for a UDP packet at each sample before returning
control to the scheduler.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `blockingTime` |

### **Sample time (seconds)** — Sample time `1` (default) | positive scalar

Specify how often the scheduler runs this block. Setting this parameter to a large
value reduces the likelihood of dropped UDP messages.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `sampletime` |

## Libraries

Embedded Coder Support Package for ARM Cortex-A Processors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2014b**

## Description

Receive UDP data

The UDP Receive block receives user datagram protocol (UDP) data from a
remote host. The block reads available UDP data from the socket buffer and outputs the data as
a vector.
