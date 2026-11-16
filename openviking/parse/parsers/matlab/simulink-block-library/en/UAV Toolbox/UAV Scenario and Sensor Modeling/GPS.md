---
type: simulink-block
title: 'GPS'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Scenario and Sensor Modeling'
documentation_page: 'gps'
documentation_source_path: 'ref/gps.html'
language: en
---

# GPS

## Ports

### Input

### **Position** — Position of GPS receiver in navigation coordinate system matrix

Specify the input position of the GPS receiver in the navigation coordinate system
as a real, finite *N*-by-3 matrix. *N* is the number
of samples in the current frame. The format of the matrix rows differs depending on
the value of the **Position input format** parameter.

- If the value of the **Position input format** parameter is
  `Local`, specify each row of the
  **Position** as Cartesian coordinates in meters with respect
  to the local navigation reference frame, specified by the **Reference
  frame** parameter, with the origin specified by the **Reference
  location** parameter.
- If the value of the **Position input format** parameter is
  `Geodetic`, specify each row of the
  **Position** input as geodetic coordinates of the form
  `[latitude longitude altitude]`. The values of
  `latitude` and `longitude` are in degrees.
  `Altitude` is the height above the WGS84 ellipsoid model in
  meters.

**Data Types:** `single` | `double`

### **Velocity** — Velocity in local navigation coordinate system (m/s) matrix

Specify the input velocity of the GPS receiver in the navigation coordinate system
in meters per second as a real, finite *N*-by-3 matrix.
*N* is the number of samples in the current frame. The format of
the matrix rows differs depending on the value of the **Position input format** parameter.

- If the value of the **Position input format** parameter is
  `Local`, specify each row of the
  **Velocity** with respect to the local navigation reference
  frame (NED or ENU), specified by the **Reference
  frame** parameter, with the origin specified by the **Reference
  location** parameter.
- If the value of the **Position input format** parameter is
  `Geodetic`, specify each row of the
  **Velocity** with respect to the navigation reference frame
  (NED or ENU), specified by the **Reference frame** parameter,
  with the origin specified by **Position**.

**Data Types:** `single` | `double`
### Output

### **LLA** — Position in LLA coordinate system matrix

Position of the GPS receiver in the geodetic latitude, longitude, and altitude
(LLA) coordinate system, returned as a real, finite *N*-by-3 array.
Latitude and longitude are in degrees with North and East being positive. Altitude is
in meters.

*N* is the number of samples in the current frame.

**Data Types:** `single` | `double`

### **Velocity** — Velocity in local navigation coordinate system (m/s) matrix

Velocity of the GPS receiver in the local navigation coordinate system in meters
per second, returned as a real, finite *N*-by-3 matrix.
*N* is the number of samples in the current frame. The format of
the matrix rows differs depending on the value of the **Position input format** parameter.

- If the value of the **Position input format** parameter is
  `Local`, the **Velocity** output is with
  respect to the local navigation reference frame (NED or ENU), specified by the
  **Reference
  frame** parameter, with the origin specified by the **Reference
  location** parameter.
- If the value of the **Position input format** parameter is
  `Geodetic`, the **Velocity** output is with
  respect to the navigation reference frame (NED or ENU), specified by the
  **Reference frame** parameter, with the origin specified by
  **LLA**.

**Data Types:** `single` | `double`

### **Groundspeed** — Magnitude of horizontal velocity in local navigation coordinate system (m/s) vector

Magnitude of the horizontal velocity of the GPS receiver in the local navigation
coordinate system in meters per second, returned as a real, finite
*N*-element column vector.

*N* is the number of samples in the current frame.

**Data Types:** `single` | `double`

### **Course** — Direction of horizontal velocity in local navigation coordinate system (°) vector

Direction of the horizontal velocity of the GPS receiver in the local navigation
coordinate system, in degrees, returned as a real, finite *N*-element
column vector of values from 0 to 360. North corresponds to 0 degrees and East
corresponds to 90 degrees.

*N* is the number of samples in the current frame.

**Data Types:** `single` | `double`

## Parameters

### **Reference frame** — Reference frame `NED` (default) | `ENU`

Specify the reference frame as `NED` (North-East-Down) or
`ENU`(East-North-Up).

### **Position input format** — Position coordinate input format `Local` (default) | `Geodetic`

Specify the position coordinate input format as `Local` or
`Geodetic`.

- If you set this parameter to `Local`, then the input to the
  **Position**
  port must be in the form of Cartesian coordinates with respect to the local
  navigation frame, specified by the **Reference Frame** parameter,
  with the origin fixed and defined by the **Reference location**
  parameter. The input to the **Velocity**
  input port must also be with respect to this local navigation frame.
- If you set this parameter to `Geodetic`, then the input to
  the **Position** port must be geodetic coordinates in
  `[latitude longitude altitude]`. The input to the
  **Velocity** input port must also be with respect to the
  navigation frame specified by the **Reference frame** parameter,
  with the origin corresponding to the **Position** port.

### **Reference location** — Origin of local navigation reference frame `[0,0,0]` (default) | three-element vector

Specify the origin of the local reference frame as a three-element row vector in
geodetic coordinates `[latitude longitude altitude]`, where
`altitude` is the height above the reference ellipsoid model WGS84.
The reference location values are in degrees, degrees, and meters, respectively. The
degree format is decimal degrees (DD).

#### Dependencies

To enable this parameter, set the **Position input
format** parameter to `Local`.

### **Horizontal position accuracy** — Horizontal position accuracy (m) `1.6` (default) | nonnegative real scaler

Specify horizontal position accuracy as a nonnegative real scalar in meters. The
horizontal position accuracy specifies the standard deviation of the noise in the
horizontal position measurement. Increasing this value adds noise to the measurement,
decreasing its accuracy.

**Tunable:** Yes

### **Vertical position accuracy** — Vertical position accuracy (m) `3` (default) | nonnegative real scaler

Specify vertical position accuracy as a nonnegative real scalar in meters. The
vertical position accuracy specifies the standard deviation of the noise in the vertical
position measurement. Increasing this value adds noise to the measurement, decreasing
its accuracy.

**Tunable:** Yes

### **Velocity accuracy** — Velocity accuracy (m/s) `0.1` (default) | nonnegative real scalar

Specify velocity accuracy per second as a nonnegative real scalar in meters. The
velocity accuracy specifies the standard deviation of the noise in the velocity
measurement. Increasing this value adds noise to the measurement, decreasing its
accuracy.

**Tunable:** Yes

### **Decay factor** — Global position noise decay factor `0.999` (default) | scalar in range [0, 1]

Specify the global position noise decay factor as a numeric scalar in the range [0,
1]. A decay factor of `0` models the global position noise as a white
noise process. A decay factor of 1 models the global position noise as a random walk
process.

**Tunable:** Yes

### **Seed** — Initial seed `67` (default) | nonnegative integer

Specify the initial seed of an mt19937ar random number generator algorithm as a
nonnegative integer.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Select the type of simulation to run from these options:

- `Interpreted execution` — Simulate the model
  using the MATLAB® interpreter. For more information, see Interpreted Execution vs. Code Generation (Simulink).
- `Code generation` — Simulate the model using generated
  C code. The first time you run a simulation, Simulink® generates C code for the block. The C code is reused for subsequent
  simulations, as long as the model does not change.

## Libraries

UAV Toolbox / UAV Scenario and Sensor Modeling Navigation Toolbox / Multisensor Positioning / Sensor Models Sensor Fusion and Tracking Toolbox / Multisensor Positioning / Sensor Models

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021b**

## Description

Simulate GPS sensor readings with noise

The block outputs noise-corrupted GPS measurements based on the input position and
velocity in the local coordinate frame or geodetic frame. It uses the WGS84 earth model to
convert local coordinates to latitude-longitude-altitude LLA coordinates.
