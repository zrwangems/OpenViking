---
type: simulink-block
title: 'Magnetometer'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'magnetometer'
documentation_source_path: 'px4/ref/magnetometer.html'
language: en
---

# Magnetometer

## Ports

### Output

### **Status** — Status of the received uORB data `0` | `1`

The Status output indicates if the sensor\_mag uORB message was received during a
previous time step or not. A value of `0` indicates that the uORB
data at the outputs is the latest, and a value of `1` indicates that
the uORB data was received during the previous time step.

This output can be used to trigger subsystems for processing new messages received
in the uORB network.

**Data Types:** `Boolean`

### **X** — Magnetic field along the x-axis scalar | gauss

The magnetic field along the x-axis of the PX4 Autopilot board, as read from the
sensor\_mag uORB topic.

**Data Types:** `single`

### **Y** — Magnetic field along the y-axis scalar | gauss

The magnetic field along the y-axis of the PX4 Autopilot board, as read from the
sensor\_mag uORB topic.

**Data Types:** `single`

### **Z** — Magnetic field along the z-axis scalar | gauss

The magnetic field along the z-axis of the PX4 Autopilot board, as read from the
sensor\_mag uORB topic.

**Data Types:** `single`

### **Timestamp** — Timestamp of the received uORB data time

Represents the time (since the PX4 system start) when the sensor\_mag uORB topic
was last updated.

**Data Types:** `double`

To see more output options for the sensor\_mag uorb topic, use the PX4 uORB Read block, subscribe to the
topic, and select other output options.

## Parameters

#### Main tab

### **Timestamp** — Enable timestamp value as one of the outputs `off` (default) | `on`

Select this parameter to output the timestamp.

### **Sample time** — Interval at which the block reads values `1/250` (default) | any non-negative value that is a multiple of 1/250 | -1

Enter the time interval at which the block reads values from the uORB
network.

When you set this parameter to `-1`, Simulink® determines the best sample time for the block based on the block context
within the model.

#### Advanced Tab

### **Wait until data received** — Wait until requested data is available off (default) | on

- When you select this option, the read operation runs in Blocking Mode. The read
  operation is blocked while waiting for the requested data to be available. When the
  data is available, the block outputs the selected values, and the
  **Status** port is set to `0`.

  The board waits for the message in Blocking Mode for the time mentioned in the
  `Timeout in seconds`. If the data is not received before the
  timeout, then the Status port outputs 1 and the block outputs the last received
  value.

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

Read sensor_mag uORB topic and obtain three dimensional magnetic field

The Magnetometer block reads the sensor\_mag uORB topic and outputs the
magnetic field of the PX4 Autopilot board along the x, y and z axis. The block also outputs
the timestamp.

On each simulation step, the block checks if a new message is available on the sensor\_mag
topic. If a new message is available, the block retrieves the message and outputs it, and the
timestamp is updated. If a new message is not available, the block outputs the last updated
uORB message and the timestamp is not updated. If a message has not been received since the
start of the simulation, the outputs are zeroes.

During Normal mode simulation, the block outputs zeroes.

During Connected I/O simulation, this block reads data from the peripherals of the
hardware.
