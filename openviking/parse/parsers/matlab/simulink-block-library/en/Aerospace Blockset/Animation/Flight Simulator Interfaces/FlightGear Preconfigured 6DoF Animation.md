---
type: simulink-block
title: 'FlightGear Preconfigured 6DoF Animation'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation / Flight Simulator Interfaces'
documentation_page: 'flightgearpreconfigured6dofanimation'
documentation_source_path: 'flightgearpreconfigured6dofanimation.html'
language: en
---

# FlightGear Preconfigured 6DoF Animation

## Ports
```yaml
ports:
- name: l,μ,h,ϕ,θ,ψ
  summary: Longitude, latitude, altitude, roll, pitch, and yaw vector
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point | enumerated | bus
```

### Input

### **l,μ,h,ϕ,θ,ψ** — Longitude, latitude, altitude, roll, pitch, and yaw vector

Longitude, latitude, altitude, roll, pitch, and yaw, in
double-precision, specified as a vector. Units are degrees west/north
for longitude and latitude, meters above mean sea level for altitude,
and radians for attitude values.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`
## Parameters
```yaml
parameters:
- name: Destination IP address
  summary: Destination IP address 127.0.0.1 (default) | scalar
  group: ''
  block_parameter: DestinationIpAddress
  type: character vector
  values: scalar
  default: '''127.0.0.1'''
- name: Destination port
  summary: Destination port scalar
  group: ''
  block_parameter: DestinationPort
  type: character vector
  values: scalar
  default: '''5502'''
- name: Sample time
  summary: Sample time 1/30 (default) | scalar
  group: ''
  block_parameter: SampleTime
  type: character vector
  values: scalar
  default: '''1/30'''
```

### **Destination IP address** — Destination IP address `127.0.0.1` (default) | scalar

Destination IP address of the machine running FlightGear software, specified as a
scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `DestinationIpAddress` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'127.0.0.1'` |

### **Destination port** — Destination port scalar

Destination port of the machine running FlightGear software, specified as a
scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `DestinationPort` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'5502'` |

### **Sample time** — Sample time 1/30 (default) | scalar

Sample time specified as a scalar (–1 for inherited).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'1/30'` |
## Libraries

Aerospace Blockset / Animation / Flight Simulator Interfaces

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced before R2006a**

## Description

Connect model to FlightGear flight simulator

The FlightGear Preconfigured 6DoF Animation
block lets you drive position and attitude values to a FlightGear
flight simulator vehicle given double-precision values for longitude
(*`l`*), latitude (*μ*),
altitude (*`h`*), roll (*ϕ*),
pitch (*θ*), and yaw (*ψ*), respectively.

The block is configured as a sim viewing device. If you generate code for your model using
Simulink®
Coder™ and connect to the running target code using external mode simulation,
Simulink software can obtain the data from the target on the fly and transmit
position and attitude data to FlightGear. For more information, see Use C/C++ S-Functions as Sim Viewing Devices in External Mode.

The Aerospace Blockset™ product supports FlightGear versions starting from v2.6. If you are using
a FlightGear version older than 2.6, the model displays a notification from the
Simulink Upgrade Advisor. Consider using the Upgrade Advisor to upgrade your
FlightGear version. For more information, see Supported FlightGear Versions.
