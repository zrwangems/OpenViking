---
type: simulink-block
title: 'Send net_fdm Packet to FlightGear'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation / Flight Simulator Interfaces'
documentation_page: 'sendnet_fdmpackettoflightgear'
documentation_source_path: 'sendnet_fdmpackettoflightgear.html'
language: en
---

# Send net_fdm Packet to FlightGear

## Ports
```yaml
ports:
- name: net_fdm
  summary: FlightGear net_fdm data packet scalar
  direction: input
  data_types: uint8
```

### Input

### **net\_fdm** — FlightGear `net_fdm` data packet scalar

FlightGear `net_fdm` data packet, specified as a
scalar.

**Data Types:** `uint8`
## Parameters
```yaml
parameters:
- name: Destination IP address
  summary: Destination IP address for remote computer 127.0.0.1 (default) | scalar
  group: ''
  block_parameter: DestinationIpAddress
  type: character vector
  values: scalar
  default: 127.0.0.1
- name: Destination port
  summary: Destination port for remote computer 5502 (default) | scalar
  group: ''
  block_parameter: DestinationPort
  type: character vector
  values: scalar
  default: '5502'
- name: Sample time
  summary: Sample time 1/30 (default) | scalar
  group: ''
  block_parameter: SampleTime
  type: character vector
  values: scalar
  default: 1/30
```

### **Destination IP address** — Destination IP address for remote computer `127.0.0.1` (default) | scalar

Destination IP address, specified as a scalar.

You can use one of several techniques to determine the destination IP
address, such as:

- Use 127.0.0.1 for
  the
  local computer
- Ping another computer from a Windows®
  `cmd.exe` (or UNIX® shell) prompt:

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
  returned *`IP Address`*:

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
| **Block Parameter**: `DestinationIpAddress` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `127.0.0.1` |

### **Destination port** — Destination port for remote computer 5502 (default) | scalar

Destination port, specified as a scalar

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `DestinationPort` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `5502` |

### **Sample time** — Sample time `1/30` (default) | scalar

Sample time (-1 for inherited), specified as a scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `1/30` |
## Libraries

Aerospace Blockset / Animation / Flight Simulator Interfaces

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced before R2006a**

## Description

Transmit net_fdm packet to destination IP address and port for FlightGear session

The Send net\_fdm Packet to FlightGear block transmits the
`net_fdm` packet to FlightGear on the current computer, or a remote
computer on the network. The packet is constructed using the Pack net\_fdm Packet for FlightGear block. The
destination port should be an unused port that you can use when you launch FlightGear
with the FlightGear command line flag:

```
--fdm=network,localhost,5501,5502,5503
```

This block does not produce deployable code.
