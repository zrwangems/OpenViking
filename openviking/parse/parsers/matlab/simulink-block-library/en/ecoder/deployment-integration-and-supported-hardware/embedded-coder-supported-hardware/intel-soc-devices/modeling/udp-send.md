---
type: simulink-block
title: 'UDP Send'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Intel SoC Devices / Modeling'
documentation_page: 'udpsend'
documentation_source_path: 'alterasoc/ref/udpsend.html'
language: en
---

# UDP Send

## Ports

### Input

### **Port\_1** — Input data signal N-by-1 array

Input signal of messages to be sent to the remote IP address and port.

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

### **IP address** — IP address `'255.255.255.255'` (default) | character vector

Specify the IP address to which the block sends the message. To broadcast the UDP
message, retain the default value `'255.255.255.255'`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `localURL` |

### **Remote IP port** — Remote IP port `25000` (default) | 1–65535

Specify the IP port where the block sends the message.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `remotePort` |

### **Local IP port source** — Local IP port source `Assign automatically` (default) | `Specify via dialog`

To let the system automatically assign the port number, select `Assign
automatically`. To specify the IP port number using the **Local
IP port** parameter, select `Specify via
dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `localPortSource` |

### **Local IP port** — Local IP port `-1` (default) | `1 .. 65535`

Specify the IP port number from which the block sends the message. If the receiving
address expects messages from a particular port number, enter that number here.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `localPort` |

## Libraries

Embedded Coder Support Package for Intel SoC Devices

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2014b**

## Description

Send UDP message

The UDP Send block transmits an input vector as a user datagram protocol
(UDP) message over an IP network port.
