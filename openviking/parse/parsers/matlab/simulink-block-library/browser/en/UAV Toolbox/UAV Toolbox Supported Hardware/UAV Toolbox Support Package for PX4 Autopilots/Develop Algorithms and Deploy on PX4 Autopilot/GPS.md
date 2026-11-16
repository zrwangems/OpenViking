---
type: simulink-block
title: 'GPS'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'gps'
documentation_source_path: 'px4/ref/gps.html'
language: en
---

# GPS

## Ports

### Output

### **Status** — Status of the received uORB data `0` | `1`

The Status output indicates if the vehicle\_gps\_position uORB message was received
during a previous time step or not. A value of `0` indicates that the
uORB data at the outputs is the latest, and a value of `1` indicates
that the uORB data was not updated during the previous time step.

This output can be used to trigger subsystems for processing new messages received
in the uORB network.

**Data Types:** `Boolean`

### **Latitude** — Latitude of the PX4 Autopilot scalar | 1e-7 degrees

The latitude coordinate based on the current position of the GPS receiver
connected to PX4 Autopilot, as read from the vehicle\_gps\_position uORB topic.

**Data Types:** `int32`

### **Longitude** — Longitude of the PX4 Autopilot scalar | 1e-7 degrees

The longitude coordinate based on the current position of the GPS receiver
connected to PX4 Autopilot, as read from the vehicle\_gps\_position uORB topic.

**Data Types:** `int32`

### **Altitude(MSL)** — Altitude of the PX4 Autopilot above Mean Sea Level (MSL) scalar | millimeters

The altitude coordinate based on the current position of the GPS receiver above
Mean Sea Level, as read from the vehicle\_gps\_position uORB topic.

**Data Types:** `int32`

### **Speed** — Ground speed of the PX4 Autopilot scalar | meters/sec

The ground speed coordinate from the GPS receiver connected to PX4 Autopilot, as
read from the vehicle\_gps\_position uORB topic.

#### Dependencies

This output appears only if you have selected the **Ground speed
(m/s)** parameter.

**Data Types:** `float32`

### **Course** — Course of the PX4 Autopilot over ground scalar | radians

The course over ground (not the heading, but the direction of movement) value
within (-π to π), based on the direction of movement of the GPS receiver connected to
PX4 Autopilot, as read from the vehicle\_gps\_position uORB topic.

#### Dependencies

This output appears only if you have selected the **Course
(rad)** parameter.

**Data Types:** `float32`

### **Fix Type** — Fix type of the GPS receiver scalar

The type of signal or technique being used by the GPS receiver to determine the
location, as read from the vehicle\_gps\_position uORB topic. The following table
represents the values for this signal:

| Value | Type of Fix |
| --- | --- |
| 0-1 | No fix |
| 2 | 2D fix |
| 3 | 3D fix |
| 4 | RTCM code differential |
| 5 | Real-Time Kinematic, float |
| 6 | Real-Time Kinematic, fixed |
| 8 | Extrapolated. Some applications will not use the value of this field unless it is at least two, so always correctly fill in the fix. |

#### Dependencies

This output appears only if you have selected the **GPS fix
type** parameter.

**Data Types:** `uint8`

### **Num Sats** — Number of satellites used for global positioning scalar

The number of satellites used by the GPS receiver to determine the GPS
coordinates, as read from the vehicle\_gps\_position uORB topic.

#### Dependencies

This output appears only if you have selected the **Number of
satellites** parameter.

**Data Types:** `uint8`

### **UTC Time** — UTC timestamp in Unix time obtained from the GPS receiver UTC (in microseconds)

UTC timestamp in Unix time (in microseconds) obtained from the GPS receiver, as
read from the vehicle\_gps\_position uORB topic. The value might be unavailable right
after cold start, indicated by a value of 0.

#### Dependencies

This output appears only if you have selected the **Unix timestamp UTC
(us)** parameter.

**Data Types:** `uint64`

### **DOP** — Horizontal and vertical dilution of precisions used by the GPS receiver 2-by-1 vector

The horizontal and vertical dilution of precisions (DOP) used by the GPS receiver,
as read from the vehicle\_gps\_position uORB topic.

#### Dependencies

This output appears only if you have selected the **Dilution of
precision** parameter.

**Data Types:** `float32`

### **NED velocity** — North, east, and down velocity of the PX4 Autopilot 3-by-1 vector | meters/sec

The north, east, and down velocity measured by the GPS receiver connected to the
PX4 Autopilot, as read from the vehicle\_gps\_position uORB topic.

#### Dependencies

This output appears only if you have selected the **NED
velocity** parameter.

**Data Types:** `float32`

### **Altitude(Ellipsoid)** — Altitude of the PX4 Autopilot above Ellipsoid scalar | millimeters

The altitude coordinate based on the current position of the GPS receiver based on
ellipsoidal model (1e-3 meters above Ellipsoid), as read from the vehicle\_gps\_position
uORB topic.

#### Dependencies

This output appears only if you have selected the **Altitude above
Ellipsoid** parameter.

**Data Types:** `int32`

### **Jamming ind** — Jamming indicator of the GPS receiver scalar

The jamming indicator value of the GPS receiver, which indicates if jamming of
signals is occurring or not, as read from the vehicle\_gps\_position uORB topic.

#### Dependencies

This output appears only if you have selected the **Jamming
indicator** parameter.

**Data Types:** `int32`

### **Timestamp** — Timestamp of the received uORB data since system start microseconds

Represents the time since the PX4 system start when the vehicle\_gps\_position uORB
topic was last updated.

#### Dependencies

This output appears only if you have selected the **PX4 timestamp
(us)** parameter.

**Data Types:** `uint64`

## Parameters

#### Main tab

### **Latitude (1e-7 degrees)** — Enable latitude value as one of the outputs `on` (default) | `off`

### **Longitude (1e-7 degrees)** — Enable longitude value as one of the outputs `on` (default) | `off`

### **Alititude above MSL (mm)** — Enable altitude (above MSL) as one of the outputs `off` (default) | `on`

### **Ground speed (m/s)** — Enable ground speed value as one of the outputs `off` (default) | `on`

### **Course (rad)** — Enable course value as one of the outputs `off` (default) | `on`

### **GPS fix type** — Enable GPS fix type value as one of the outputs `off` (default) | `on`

### **Number of satellites** — Enable number of satellites as one of the outputs `off` (default) | `on`

### **Unix timestamp UTC (us)** — Enable UTC timestamp value as one of the outputs `off` (default) | `on`

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

### **Dilution of precision** — Enable dilution of precision value as one of the outputs `off` (default) | `on`

### **NED velocity** — Enable NED velocity value as one of the outputs `off` (default) | `on`

### **Altitude above Ellipsoid** — Enable altitude above ellipsoid value as one of the outputs `off` (default) | `on`

### **Jamming indicator** — Enable jamming indicator value as one of the outputs `off` (default) | `on`

### **PX4 timestamp (us)** — Enable PX4 timestamp value as one of the outputs `off` (default) | `on`

## Libraries

UAV Toolbox Support Package for PX4 Autopilots / PX4 Sensor Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020a**

## Description

Read vehicle_gps_position uORB topic and obtain GPS coordinates

The GPS block reads the vehicle\_gps\_position uORB topic and outputs the GPS
coordinates of the GPS receiver connected to the PX4 Autopilot. The block outputs latitude,
longitude and altitude, by default, and it also provides the option to add more outputs that
are based on the GPS coordinates.

On each simulation step, the block checks if a new message is available on the
vehicle\_gps\_position topic. If a new message is available, the block retrieves the message and
outputs it, and the timestamp is updated. If a new message is not available, the block outputs
the last updated uORB message and the timestamp is not updated. If a message has not been
received since the start of the simulation, the outputs are zeroes.

During Normal mode simulation, the block outputs zeroes.

During Connected I/O simulation, this block reads data from the peripherals of the
hardware.
