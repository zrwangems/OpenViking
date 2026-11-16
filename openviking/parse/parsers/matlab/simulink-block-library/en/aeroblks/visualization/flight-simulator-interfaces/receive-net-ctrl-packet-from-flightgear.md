---
type: simulink-block
title: 'Receive net_ctrl Packet from FlightGear'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Visualization / Flight Simulator Interfaces'
documentation_page: 'receivenet_ctrlpacketfromflightgear'
documentation_source_path: 'receivenet_ctrlpacketfromflightgear.html'
language: en
---

# Receive net_ctrl Packet from FlightGear

## Ports

### Output

### **net\_ctrl** — Controls information from FlightGear 744-by-1 vector

Controls information from FlightGear, returned as a 744-by-1 vector.

**Data Types:** `uint8`

### **Rx bytes** — Received FlightGear packet size `0` | `744`

Received FlightGear packet size, specified as a scalar.

- 0, if no data is received
- Size of the packet (744) in bytes.

#### Dependencies

This port is enabled by the **Enable received flag
port** check box.

**Data Types:** `double`

## Parameters

### **Origin IP address** — Origin IP address `127.0.0.1` (default) | scalar

Enter a valid IP address as a dot-decimal string. This IP address must be the address of
the computer from which FlightGear is run, for example,
`10.10.10.3`.

You can also use a MATLAB expression that returns a valid IP address as a character
vector. If FlightGear is run on the local computer, leave the default value
of `127.0.0.1` (localhost).

To determine the source IP address, you can use one of several techniques,
such as:

- Use 127.0.0.1 for the local computer (localhost).
- Ping another computer from a Windows®
  `cmd.exe` (or Linux® shell) prompt:

  ```
  C:\> ping andyspc

  Pinging andyspc [144.213.175.92] with 32 bytes of data:

  Reply from 144.213.175.92: bytes=32 time=30ms TTL=253
  Reply from 144.213.175.92: bytes=32 time=20ms TTL=253
  Reply from 144.213.175.92: bytes=32 time=20ms TTL=253
  Reply from 144.213.175.92: bytes=32 time=20ms TTL=253

  Ping statistics for 144.213.175.92:
      Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
  Approximate round trip times in milli-seconds:
      Minimum = 20ms, Maximum =  30ms, Average =  22ms
  ```
- On a Windows machine, type `ipconfig` and use the
  returned IP address:

  ```
  H:\>ipconfig

  Windows IP Configuration

  Ethernet adapter Local Area Connection:

          Connection-specific DNS Suffix  . :
          IP Address. . . . . . . . . . . . : 192.168.42.178
          Subnet Mask . . . . . . . . . . . : 255.255.255.0
          Default Gateway . . . . . . . . . : 192.168.42.254
  ```

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ReceiveAddress` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'127.0.0.1'` |

### **Origin port** — Origin port 5505 (default)

UDP port that the block accepts data from. The sender sends data to the port specified in
this parameter. This value must match the **Origin port**
parameter of the Generate Run Script block.
It must be a unique port number that no other application on the computer
uses. The site,
`https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers`,
lists commonly known UDP port numbers. To identify UDP port numbers already
in use on your computer, type:

```
netstat -a -p UDP
```

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ReceivePort` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'5505'` |

### **Sample time** — Sample time 1/30 (default) | scalar

Specify the sample time (-1 for inherited).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'1/30'` |

### **Enable received flag port** — Enable received flag output port `off` (default) | `on`

Enable a received flag output port. Use this check box to determine if a
FlightGear network packet has been received.

#### Dependencies

Selecting this check box enables the **Rx bytes**
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `packetFlag` |
| **Type**: character vector |
| **Values:**`'off' | 'on'` |
| **Default**: `'off'` |

## Libraries

Aerospace Blockset / Animation / Flight Simulator Interfaces

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2012a**

## Description

Receive net_ctrl packet from FlightGear

The Receive net\_ctrl Packet from FlightGear block receives a
network control and environment data packet, `net_ctrl`, from the
simulation of a Simulink® model in the FlightGear simulator, or from a FlightGear session. This data
packet is compatible with a particular version of FlightGear flight simulator. This
block supports all signals supported by the FlightGear `net_ctrl` data
packet. The block arranges the signals into multiple groups. The block inserts zeros for
packet values that are part of inactive signal groups.

The Aerospace Blockset™ product supports FlightGear versions starting from v2.6. If you are using
a FlightGear version older than 2.6, the model displays a notification from the
Simulink Upgrade Advisor. Consider using the Upgrade Advisor to upgrade your
FlightGear version. For more information, see Supported FlightGear Versions.

If you run a model that contains this block in Rapid Accelerator mode, the block produces
zeros (`0`s) and it does not produce deployable code. In Accelerator
mode, the block works as expected.

For details on signals and signal groups, see Output.
