---
type: simulink-block
title: 'Battery'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'battery'
documentation_source_path: 'px4/ref/battery.html'
language: en
---

# Battery

## Ports

### Output

### **Status** — Status of the received uORB data `0` | `1`

The Status output indicates if the `battery_status uORB` message
was received during a previous time step or not. A value of `0`
indicates that the uORB data at the outputs is the latest, and a value of
`1` indicates that the uORB data was received during the previous
time step.

This output can be used to trigger subsystems for processing new messages received
in the uORB network.

**Data Types:** `Boolean`

### **Voltage** — Voltage of battery scalar (volts)

The output voltage of battery, as read from the battery\_status uORB topic.

**Data Types:** `single`

### **Current** — The output current that the battery is delivering scalar (amperes)

The output current, as read from the battery\_status uORB topic.

**Data Types:** `single`

### **Percentage** — Percentage of battery life remaining scalar

The percentage of battery life remaining, as read from the battery\_status uORB
topic.

**Data Types:** `single`

### **Warning** — Battery warning status scalar

The battery warning status, as read from the battery\_status uORB topic.

| Status | Description |
| --- | --- |
| 0 | No battery low voltage warning active |
| 1 | Warning of low voltage |
| 2 | Critical voltage, return / abort immediately |
| 3 | Immediate landing required |
| 4 | The battery has failed completely |

**Data Types:** `uint8`

### **Timestamp** — Timestamp of the received uORB data time

The timestamp of the battery\_status uORB topic read from the uORB network.

**Data Types:** `double`

## Parameters

#### Main tab

### **Voltage** — Enable voltage value as one of the outputs `on` (default) | `off`

### **Current** — Enable current value as one of the outputs `off` (default) | `on`

### **Battery percentage** — Enable battery percentage as one of the outputs `on` (default) | `off`

### **Battery status warning** — Enable battery status warning as one of the outputs `off` (default) | `on`

### **Timestamp** — Enable timestamp value as one of the outputs `off` (default) | `on`

### **Sample time** — Interval at which the block reads values `1/250` (default) | any non-negative value that is a multiple of 1/250 | -1

Enter the time interval at which the block reads values from the uORB
network.

When you set this parameter to `-1`, Simulink® determines the best sample time for the block based on the block context
within the model.

#### Advanced Tab

### **Wait until data received** — Wait until requested data is available off (default) | on

- When you select this option, the read operation runs in Blocking Mode. The read
  operation is blocked while waiting for the requested data to be available. When
  waiting for the data, the **Status** port displays same values from
  the previous time step. When the data become available, the block outputs the
  selected values, and the **Status** port changes to
  `0`.

  A task overrun occurs if the target hardware is still waiting for the data to be
  available when the next read operation is scheduled to begin.

  To fix overruns, increase the time step by using the **Sample
  time** parameter.
- When you clear this option, the read operation runs in Non-Blocking Mode. In
  this mode, the block does not wait for the requested data to be available.

### **Timeout in seconds** — Time to wait until the data is received `1e-3` (default) | (0, 2^32/1000]

Specify the amount of time that the block waits for the data during each time step,
if the **Wait until data received** parameter is selected. If timeout
occurs, the read operation is aborted.

#### Dependencies

This parameter appears only when you select the **Wait until data
received** parameter.

## Libraries

UAV Toolbox Support Package for PX4 Autopilots / PX4 Sensor Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Read battery_status uORB topic and obtain details about the battery's state

The Battery block reads the `battery_status uORB` topic
and outputs the details about the state of the battery connected to PX4 flight controller. The
block also outputs the timestamp.

On each simulation step, the block checks if a new message is available on the
battery\_status topic. If a new message is available, the block retrieves the message and
converts it to the output values. If a new message is not available, the outputs are based on
the last received uORB message. If a message has not been received since the start of the
simulation, the outputs are zeroes.

During Normal mode simulation, the block outputs zeroes.

During Connected I/O simulation, this block reads data from the peripherals of the
hardware.
