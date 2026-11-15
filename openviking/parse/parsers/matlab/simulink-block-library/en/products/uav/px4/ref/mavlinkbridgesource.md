---
type: simulink-block
title: 'MAVLink Bridge Source'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'mavlinkbridgesource'
documentation_source_path: 'px4/ref/mavlinkbridgesource.html'
language: en
---

# MAVLink Bridge Source

## Ports

### Output

### **Data** — MAVLink data stream vector

This port outputs the MAVLink data stream.

**Data Types:** `uint8`

### **Length** — Length of the data stream scalar

This port outputs the length of the data stream for the current time
setup.

**Data Types:** `uint16`

## Parameters

### **Serial Port** — Port for connecting the Pixhawk board `Select a port` (default) | `COM1` | `COM3` | `Specify manually`

Select a serial port to connect to the Pixhawk board. If the required ports are not available in the list, select
`Specify manually` and enter the serial port in the
**Serial Port (specify manually)** field.

### **Max Data Length** — Maximum output data stream length `1024` (default) | `any non-negative value`

Enter the maximum output data stream length.

### **Destination Ports** — Port for enabling data routing `'UDP','127.0.0.1','14550'` (default)

Click **Add** to add the destination UDP/TCP connections for
data routing. The existing connections
(`'UDP','127.0.0.1','14550'`) are used for connecting to
QGC.

**Note**

The MAVLink bridge block utilizes the following local port settings:

- Local Port for Ground Control Stations:
  `14570`
- Local Port for Onboard Connection: `14580`

### **Sample time** — Interval between outputs `0.01` (default) | any nonnegative integer that is a multiple of 0,001 | `-1`

Specify the time interval at which the block reads values from the serial
connections and routes it to the added UDP/TCP connections.

## Libraries

px4MAVLinkBridgelib

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022a**

## Description

Read MAVLink data from the Pixhawk board

The MAVLink Bridge Source block reads MAVLink data stream from the
Pixhawk® board connected to the serial port and routes it to the Simulink® plant model and the configured UDP/TCP objects. This block allows you to
configure Serial, UDP, and TCP connections.

To access the block, open the block library by entering the following command in the
MATLAB® Command
window.

```
px4MAVLinkBridgelib
```

The MAVLink Bridge Source and MAVLink Bridge Sink blocks
provides a way to route MAVLink data stream from Pixhawk hardware to the mission planning software QGroundControl(QGC), On-board
computer hardware, Simulink Plant, and vice versa in HITL workflow. For more information,
see MAVLink Connectivity for QGC, On-board Computer and Simulink Plant.
