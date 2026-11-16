---
type: simulink-block
title: 'UDP Send'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / ARM Cortex-A Processors / Modeling'
documentation_page: 'udpsend'
documentation_source_path: 'armcortexa/ref/udpsend.html'
language: en
---

# UDP Send

## Ports

### Input

### **Port\_1** — Input data signal numeric vector

Input data signal, specified as a numeric vector. The block sends this data as UDP
data to the remote IP address at the remote IP port.

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

### **Remote IP address ('255.255.255.255' for broadcast)** — IP address of remote host `'255.255.255.255'` (default) | valid IP address

Specify the IP address of the remote host to which you want to send UDP data. To
broadcast the UDP message, retain the default value
`'255.255.255.255'`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `remoteURL` |

### **Remote IP port** — IP port of remote host `25000` (default) | integer from 1 to 65,535

Specify the port number of the remote host to which you want to send UDP data. The
port number must be an integer from 1 to 65,535.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `remotePort` |

### **Local IP port source** — Select local IP port source `Assign automatically` (default) | `Specify via dialog`

To enable the system automatically assign the local IP port number from which data
is sent, select `Assign automatically`. To specify the local IP
port number using the **Local IP port** parameter, select
`Specify via dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `localPortSource` |

### **Local IP port** — IP port on local host `-1` (default) | integer from 1 to 65,535

Specify the local IP port number of the application on the hardware board from which
you want to send the data. The port number can must be an integer from 1 to 65,535. The
default value, `-1` assigns any randomly available port as the local IP
port.

If the receiving host accepts UDP data from a particular port number, set this
parameter to that number.

To enable this parameter, set **Local IP port source** to
`Specify via dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `localPort` |

## Libraries

Embedded Coder Support Package for ARM Cortex-A Processors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2014b**

## Description

Send UDP data

The UDP Send block transmits user datagram protocol (UDP) data to a remote
host.
