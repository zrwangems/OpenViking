---
type: simulink-block
title: 'MAVLink Bridge Sink'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'mavlinkbridgesink'
documentation_source_path: 'px4/ref/mavlinkbridgesink.html'
language: en
---

# MAVLink Bridge Sink

## Ports

### Input

### **Data** — MAVLink data stream vector

This port takes MAVLink data stream (uint8) as input.

**Data Types:** `unit8`

## Parameters

### **Serial Port** — Port for connecting the Pixhawk board `Select a port` (default) | `COM1` | `COM3` | `Specify manually`

Select a serial port for connecting to the Pixhawk board. If the required ports are not available in the list, select
`Specify manually` and enter the serial port in the
**Serial Port (specify manually)** field.

**Note**

You must select / specify the same serial port in MAVLink Bridge
Source and MAVLink Bridge Sink blocks.

### **Source Ports** — Port for enabling data routing `'UDP','127.0.0.1','14550'` (default)

Click **Add** to add the source UDP/TCP connections for data
routing. The existing connections (`'UDP','127.0.0.1','14550'`)
are used for connecting to QGC.

**Note**

The MAVLink bridge block utilizes the following local port settings:

- Local Port for Ground Control Stations:
  `14570`
- Local Port for Onboard Connection: `14580`

## Libraries

px4MAVLinkBridgelib

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022a**

## Description

Write MAVLink data to the Pixhawk board

The MAVLink Bridge Sink block reads the MAVLink data from the source
UDP/TCP ports, merges it with input data and writes to Pixhawk® hardware connected to Serial port.

To access the block, open the block library by entering the following command in the
MATLAB® Command
window.

```
px4MAVLinkBridgelib
```

The MAVLink Bridge Sink and MAVLink Bridge Source blocks
provides a way to route MAVLink data stream from Pixhawk hardware to the mission planning software QGroundControl(QGC), On-board
computer hardware, Simulink Plant, and vice versa in HITL workflow. For more information,
see MAVLink Connectivity for QGC, On-board Computer and Simulink Plant.
