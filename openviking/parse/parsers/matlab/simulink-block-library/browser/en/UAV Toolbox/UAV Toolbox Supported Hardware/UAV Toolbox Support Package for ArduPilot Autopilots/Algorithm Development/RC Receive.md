---
type: simulink-block
title: 'RC Receive'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for ArduPilot Autopilots / Algorithm Development'
documentation_page: 'rcreceive'
documentation_source_path: 'ardupilot/ref/rcreceive.html'
language: en
---

# RC Receive

## Ports

### Output

### **Failsafe** — Failsafe status scalar

The RC Receive block outputs the failsafe status by default. If the RC
transmitter turns off or loses signal during operation, the failsafe output
switches to `1`. Use this output to trigger safety mechanisms
in your model.

**Data Types:** `double`

### **Ch *`x`* Raw** — Raw data from the specified RC channel vector

Raw data for each selected channel. When you enable normalization, it
adjusts the output values using the specified trim and deadzone
settings.

**Data Types:** `double`

### **Mode** — Current flight mode scalar

The block outputs the flight mode index (starting from 0) based on your
Mission Planner configuration. This value indicates the current mapped flight
mode.

#### Dependencies

To enable this port, select the **Output flight mode**
parameter.

**Data Types:** `uint8`

### **RSSI** — Radio signal strength scalar

The block outputs the radio signal strength from the RC transmitter. Use
this value in your model for monitoring or implementing safety
mechanisms.

#### Dependencies

To enable this port, select the **Output radio signal strength
indicator(RSSI)** parameter.

**Data Types:** `int32`

### **Arm** — Status of vehicle arming scalar

The block outputs `1` when armed, `0` when
disarmed.

#### Dependencies

To enable this port, select the **Output arming status**
parameter.

**Data Types:** `uint8`

### **Estop** — Emergency stop status scalar

The block outputs a signal that indicates whether the motor emergency stop
has been triggered.

#### Dependencies

To enable this port, select the **Output motor emergency stop
status** parameter.

**Data Types:** `uint8`

## Parameters

#### Channels tab

### **Channel Selection** — Channels for raw data channels

Select which RC channels you want to read from your transmitter. Add or remove
channels using the interface. The block displays `Ch
x Raw` outputs based on your selections
in this parameter list. You can add a maximum of `16`
channels.

### **Normalize output for channels using trim and deadzone** — Apply trim and deadzone to raw RC data `off` (default) | `on`

Select this parameter to normalize the outputs for the selected channels using
the specified trim and deadzone settings.

### **Sample time** — Interval at which the block reads values `-1` (default)

The time interval at which the block retrieves values from the ArduPilot
autopilot.

#### Advanced tab

### **Output flight mode** — Enable output port for flight mode off (default) | on

Select this parameter to enable the **Port** output port . To
view information on the mapping of flight modes to channel values, see Flight Mode Mapping.

### **Output radio signal strenght indicator(RSSI)** — Enable output port for RSSI off (default) | on

Select this parameter to enable the **RSSI** output port
.

### **Output arming status** — Enable output port for arming status off (default) | on

Select this parameter to enable the **Arm** output port
.

### **Output motor emergency stop status** — Enable output port for motor emergency stop status off (default) | on

Select this parameter to enable the **Estop** output
port.

## Libraries

UAV Toolbox Support Package for ArduPilot Autopilots / Peripheral Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2025b**

## Description

Reads radio control channel data

The RC Receive block acquires raw input data from selected channels of an
RC transmitter. The block provides options to apply trim and deadzone adjustments for
output normalization. Additionally, the block can output auxiliary information such as
flight mode, radio signal strength indicator (RSSI), arming status, and motor emergency
stop status.
