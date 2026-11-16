---
type: simulink-block
title: 'Vehicle Attitude'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'vehicleattitude'
documentation_source_path: 'px4/ref/vehicleattitude.html'
language: en
---

# Vehicle Attitude

## Ports

### Output

### **Status** — Status of the received uORB data `0` | `1`

The Status output indicates if the vehicle\_odometry uORB message was received
during a previous time step or not. A value of `0` indicates that the
uORB data at the outputs is the latest, and a value of `1` indicates
that the uORB data was not updated during the previous time step.

This output can be used to trigger subsystems for processing new messages received
in the uORB network.

**Data Types:** `Boolean`

### **Roll rate** — Bias corrected angular velocity about x-axis scalar | rad/s

The bias corrected angular velocity about x-axis, as read from the
vehicle\_odometry uORB topic.

**Data Types:** `single`

### **Pitch rate** — Bias corrected angular velocity about y-axis scalar | rad/s

The bias corrected angular velocity about y-axis, as read from the
vehicle\_odometry uORB topic.

**Data Types:** `single`

### **Yaw rate** — Bias corrected angular velocity about z-axis scalar | rad/s

The bias corrected angular velocity about z-axis, as read from the
vehicle\_odometry uORB topic.

**Data Types:** `single`

### **Quaternion** — Attitude of the vehicle on which the PX4 flight controller is mounted, in quaternion form 1-by-4 array

The attitude of the vehicle on which the PX4 flight controller is mounted, in
quaternion form, as read from the vehicle\_odometry uORB topic.

**Data Types:** `single`

### **Timestamp** — Timestamp of the received uORB data time in microseconds

Represents the time (since the PX4® system start) when the vehicle\_odometry topic was last updated.

**Data Types:** `double`

## Parameters

#### Main tab

### **Roll** — Enable roll value as one of the outputs `off` (default) | `on`

### **Pitch** — Enable pitch value as one of the outputs `off` (default) | `on`

### **Yaw** — Enable yaw value as one of the outputs `off` (default) | `on`

### **Quaternion** — Enable quaternion value as one of the outputs `on` (default) | `off`

### **Timestamp** — Enable timestamp value as one of the outputs `off` (default) | `on`

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

Read vehicle_odometry uORB topic and obtain attitude measurements

The Vehicle Attitude block reads the vehicle\_odometry uORB topic and
outputs the attitude measurements from the Pixhawk® hardware. The block outputs the vehicle attitude in both roll, pitch, and yaw,
and quaternion (NED) form.

On each simulation step, the block checks if a new message is available on the
vehicle\_odometry topic. If a new message is available, the block retrieves the message and
outputs it, and the timestamp is updated. If a new message is not available, the block outputs
the last updated uORB message and the timestamp is not updated. If a message has not been
received since the start of the simulation, the outputs are zeroes.

During Normal mode simulation, the block outputs zeroes.

During Connected I/O simulation, this block reads data from the peripherals of the
hardware.
