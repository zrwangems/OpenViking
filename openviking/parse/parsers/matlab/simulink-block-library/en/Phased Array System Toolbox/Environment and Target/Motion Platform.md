---
type: simulink-block
title: 'Motion Platform'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Environment and Target'
documentation_page: 'motionplatform'
documentation_source_path: 'ref/motionplatform.html'
language: en
---

# Motion Platform

## Ports
```yaml
ports:
- name: Ref
  summary: Reference time input scalar
  direction: input
  data_types: double
- name: Vel
  summary: Platform velocity input real-valued 3-by-*N* matrix
  direction: input
  data_types: double
- name: Acl
  summary: Platform acceleration input real-valued 3-by-*N* matrix
  direction: input
  data_types: double
- name: Pos
  summary: Platform position output real-valued 3-by-*N* matrix
  direction: output
  data_types: double
- name: Vel
  summary: Platform velocity output real-valued 3-by-*N* matrix
  direction: output
  data_types: double
- name: LAxes
  summary: Platform orientation output real-valued 3-by-3-by-*N* matrix
  direction: output
  data_types: double
```

### Input

### **Ref** — Reference time input scalar

Reference time input, specified as a scalar. Units are in
seconds.

#### Dependencies

To enable this port, set the **Source of elapsed
simulation time** parameter to `Derive from
reference input port`.

**Data Types:** `double`

### **Vel** — Platform velocity input real-valued 3-by-*N* matrix

Platform velocity, specified as a real-valued
3-by-*N* matrix where *N* is the
number of platforms to model. Units are meters per second.

#### Dependencies

To enable this port, set the **Model of object motion** parameter to
`Velocity` and the **Source of
velocity** parameter to `Input
port`.

**Data Types:** `double`

### **Acl** — Platform acceleration input real-valued 3-by-*N* matrix

Platform acceleration input, specified as a real-valued 3-by-*N* matrix
where *N* is the number of platforms to model. Units
are meters per second-squared.

#### Dependencies

To enable this port, set the **Model of object motion** parameter to
`Acceleration` and the **Source
of acceleration** parameter to `Input
port`.

**Data Types:** `double`
### Output

### **Pos** — Platform position output real-valued 3-by-*N* matrix

Current position of platform, returned as a real-valued 3-by-1 column
vector in the form of `[x;y;z]` or a real-valued
3-by-*N* matrix where *N* is the
number of platforms to model. Each column takes the form
`[x;y;z]`. Units are meters.

**Data Types:** `double`

### **Vel** — Platform velocity output real-valued 3-by-*N* matrix

Current velocity of platform, specify as a real-valued 3-by-1 column
vector in the form of `[vx;vy;vz]` or a real-valued
3-by-*N* matrix where *N* is the
number of platforms to model. Each column taking the form
`[vx;vy;vz]`. Velocity units are meters per
second.

**Data Types:** `double`

### **LAxes** — Platform orientation output real-valued 3-by-3-by-*N* matrix

Current platform orientation axes, returned as real-valued
3-by-3-by-*N* matrix where *N* is
the number of platforms to model. Each 3-by-3 submatrix is an
orthonormal matrix. This output is enabled when you set the
`OrientationAxesOutputPort` property to
`true`. The current platform axes rotate around the
normal vector to the path of the platform.

#### Dependencies

To enable this port, select the **Enable orientation axes output**
check box.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Model of object motion
  summary: Object motion model Velocity (default) | Acceleration | Custom
  group: ''
- name: Initial position (m)
  summary: Initial position of platform [0;0;0] (default)
  group: ''
- name: Initial velocity (m/s)
  summary: Initial velocity of platform [0;0;0] (default)
  group: ''
- name: Source of velocity
  summary: Source of velocity data Property (default) | Input port
  group: ''
- name: Velocity (m/s)
  summary: Current velocity of platform [0;0;0] (default)
  group: ''
- name: Source of acceleration
  summary: Source of acceleration data Property (default) | Input port
  group: ''
- name: Acceleration (m/s^2)
  summary: Acceleration of platform [0;0;0] (default)
  group: ''
- name: Custom trajectory waypoints
  summary: Custom trajectory waypoints [ 0, 0, 0, 0, 0, 0, 0; 1, 0, 0, 0, 0, 0, 0 ] (default)
  group: ''
- name: Mechanical scanning mode
  summary: Mechanical scanning mode None (default) | Circular | Sector
  group: ''
- name: Initial scan angle (deg)
  summary: Initial scan angle of platform 0 (default)
  group: ''
- name: Azimuth scan angle span (deg)
  summary: Azimuth span [-60,60] (default)
  group: ''
- name: Azimuth scan rate (deg/s)
  summary: Azimuth scan rate 10 (default)
  group: ''
- name: Initial orientation axes
  summary: Initial orientation axes of platform eye(3) (default)
  group: ''
- name: Enable orientation axes output
  summary: Output orientation axes off (default) | on
  group: ''
- name: Source of elapsed simulation time
  summary: Source of elapsed simulation time Auto (default) | Derive from reference input port
  group: ''
- name: Inherit sample rate
  summary: Inherit sample rate from upstream blocks on (default) | off
  group: ''
- name: Sample rate (Hz)
  summary: Sampling rate of signal 1e6 (default) | positive real-valued scalar
  group: ''
- name: Simulate using
  summary: Block simulation method Interpreted Execution (default) | Code Generation
  group: ''
  block_parameter: SimulateUsing
  type: enum
  values: Interpreted Execution, Code Generation
  default: Interpreted Execution
```

### **Model of object motion** — Object motion model `Velocity` (default) | `Acceleration` | `Custom`

Specify the object motion model as `Velocity`,
`Acceleration`, or
`Custom`. When you set this parameter to
`Velocity`, the platform follows a constant
velocity trajectory during each simulation step. When you set this parameter
to `Acceleration`, the platform follows a constant
acceleration trajectory during each simulation step. When you set the
parameter to `Custom`, the platform motion follows
a sequence of waypoints specified by the **Custom trajectory
waypoints** parameter. The object performs a piecewise cubic
interpolation on the waypoints to derive the position and velocity at each
time step.

### **Initial position (m)** — Initial position of platform `[0;0;0]` (default)

Specify the initial position of the platform in meters as a
3-by-*N* matrix where each column represents the
initial position of a platform in the form `[x;y;z]`. The
quantity *N* is the number of platforms.

### **Initial velocity (m/s)** — Initial velocity of platform `[0;0;0]` (default)

Specify the initial velocity of the platform in m/s as a
3-by-*N* matrix where each column represents the
initial velocity of a platform in the form `[vx;vy;vz]`.
The quantity *N* is the number of platforms.

#### Dependencies

This parameter appears only when you set the **Source of
velocity** or the **Source of
acceleration** parameters to `Input
port`.

### **Source of velocity** — Source of velocity data `Property` (default) | `Input port`

This parameter appears only when you set the **Model of object
motion** parameter to `Velocity`.
Then, you must supply velocity data for the model. Specify the
**Source of velocity** data as either coming from a
`Property` or an `Input
port`.

| **Source of velocity** | Use these model parameters or ports |
| --- | --- |
| **Property** | **Initial position (m)** parameter  **Velocity (m/s)** parameter |
| `Input port` | **Initial position (m)** parameter  **Initial velocity (m/s)** parameter  `Vel` input port |

#### Dependencies

This parameter appears only when you set the **Model of object
motion** parameter to
`Velocity`.

### **Velocity (m/s)** — Current velocity of platform `[0;0;0]` (default)

Specify the current velocity of the platforms in m/s as a
3-by-*N* matrix where each column represents the
current velocity of a platform in the form
`[vx;vy;vz]`.

#### Dependencies

This parameter appears only when you set the **Model of object
motion** parameter to `Velocity`
and set the **Source of velocity** parameter to
`Property`.

### **Source of acceleration** — Source of acceleration data `Property` (default) | `Input port`

This parameter appears only when you set the **Model of object
motion** parameter to `Acceleration`.
Then, you must supply acceleration values for the model. Specify the
**Source of acceleration** data as either coming from a
`Property` or an `Input
port`.

| Source of acceleration | Use these model parameters or ports |
| --- | --- |
| `Property` | **Initial Position (m)** parameter  **Initial Velocity (m/s)** parameter  **Acceleration (m/s^2)** parameter |
| `Input port` | **Initial Position (m)** parameter  **Initial Velocity (m/s)** parameter  `Acl` input port |

#### Dependencies

This parameter appears only when you set the **Model of object
motion** parameter to
`Acceleration`.

### **Acceleration (m/s^2)** — Acceleration of platform `[0;0;0]` (default)

Specify the current acceleration of the platforms in m/s^2 as a
3-by-*N* matrix where each column represents the
current acceleration of a platform in the form
`[ax;ay;az]`.

#### Dependencies

This parameter appears when you set the **Model of object
motion** parameter to
`Acceleration` and set the **Source
of acceleration** parameter to
`Property`.

### **Custom trajectory waypoints** — Custom trajectory waypoints `[ 0, 0, 0, 0, 0, 0, 0; 1, 0, 0, 0, 0, 0, 0 ]` (default)

Custom trajectory waypoints, specified as a real-valued
*M*-by-*L* matrix, or
*M*-by-*L*-by-*N*
array. *M* is the number of waypoints. *L*
is either 4 or 7.

- When *L* is 4, the first column indicates the
  times at which the platform position is measured. Columns 2 - 4
  are position measurements in x, y, and z coordinates. The
  velocity is derived from the position measurements.
- When *L* is 7, columns 5 - 7 in the matrix
  are velocity measurements in x, y, and z coordinates.

When you set the **Custom trajectory
waypoints** parameter to a three-dimensional array, the number
of pages, *N*, represent the number of platforms. Time
units are in seconds, position units are in meters, and velocity units are
in meters per second.

#### Dependencies

To enable this property, set the **Model of object
motion** property to
`Custom`.

### **Mechanical scanning mode** — Mechanical scanning mode `None` (default) | `Circular` | `Sector`

Mechanical scan mode for platform, specified as
`None`, `Circular`, or
`Sector`, where `None`
is the default. When you set the **Mechanical scanning
mode** parameter to `Circular`, the
platform scan clockwise 360 degrees continuously in the azimuthal direction
of the platform orientation axes. When you set the **Mechanical
scanning mode** parameter to `Sector`,
the platform scans clockwise in the azimuthal direction in the platform
orientation axes within a range specified by the **Azimuth scan
angle span (deg)** parameter. When the platform scan reaches
the span limits, the scan reverses direction and scans back to the other
scan limit. Scanning happens within the orientation axes of the
platform.

### **Initial scan angle (deg)** — Initial scan angle of platform `0` (default)

Initial scan angle of platform, specified as a 1-by-*N*
vector where *N* is the number of platforms. The scanning
occurs in the local coordinate system of the platform. The **Initial
orientation axes** parameter specifies the original local
coordinate system. At the start of the simulation, the orientation axes
specified by the **Initial orientation axes** are rotated
by the angle specified in the
`InitialScanAngle`**Initial scan angle
(deg)** parameter. The default value is zero. Units are in
degrees.

#### Dependencies

This parameter applies when you set the **Mechanical scanning
mode** parameter to `Circular` or
`Sector`.

### **Azimuth scan angle span (deg)** — Azimuth span `[-60,60]` (default)

Specify the azimuth angle span as an *N*-by-2 matrix
where *N* is the number of platforms. Each row of the
matrix specifies the scan range of the corresponding platform in the form
`[ScanAngleLowerBound ScanAngleHigherBound]`. The
default value is `[-60 60]`. Units are in degrees.

#### Dependencies

To enable this parameter, set the **Mechanical scanning
mode** parameter to
`Sector`.

### **Azimuth scan rate (deg/s)** — Azimuth scan rate `10` (default)

Specify the azimuth scan rate as a 1-by-*N* vector where
*N* is the number of platforms. Each entry in the
vector is the azimuth scan rate for the corresponding platform. The default
value is 10 degrees/second. Units are in degrees/second.

#### Dependencies

To enable this parameter, set the **Mechanical scanning
mode** parameter to `Circular` or
`Sector`.

### **Initial orientation axes** — Initial orientation axes of platform `eye(3)` (default)

Specify the three axes that define the initial local
*(x,y,z)* coordinate system at the platform as a
3-by-3-by-*N* matrix. Each column of the matrix
represents an axis of the local coordinate system. The three axes must be
orthonormal.

### **Enable orientation axes output** — Output orientation axes off (default) | on

Select this check box to obtain the instantaneous orientation axes of the
platform via the output port `LAxes`. The port appears only
when the check box is selected.

### **Source of elapsed simulation time** — Source of elapsed simulation time `Auto` (default) | `Derive from reference input port`

Specify the source for elapsed simulation time as
`Auto` or `Derive from reference
input port`. When you choose
`Auto`, the block computes the elapsed time.
When you choose `Derive from reference input port`,
the block uses the time duration of a reference signal passed into the
`Ref` input port.

### **Inherit sample rate** — Inherit sample rate from upstream blocks on (default) | off

Select this parameter to inherit the sample rate from upstream blocks. Otherwise,
specify the sample rate using the **Sample rate (Hz)**
parameter.

**Data Types:** `Boolean`

### **Sample rate (Hz)** — Sampling rate of signal `1e6` (default) | positive real-valued scalar

Specify the signal sampling rate as a positive scalar. Units are in Hz.

#### Dependencies

To enable this parameter, clear the **Inherit sample rate** check
box.

**Data Types:** `double`

### **Simulate using** — Block simulation method `Interpreted Execution` (default) | `Code Generation`

Block simulation, specified as `Interpreted Execution` or
`Code Generation`. If you want your block to use the
MATLAB® interpreter, choose `Interpreted Execution`. If
you want your block to run as compiled code, choose `Code
Generation`. Compiled code requires time to compile but usually runs
faster.

Interpreted execution is useful when you are developing and tuning a model. The block
runs the underlying System object™ in MATLAB. You can change and execute your model quickly. When you are satisfied
with your results, you can then run the block using `Code
Generation`. Long simulations run faster with generated code than in
interpreted execution. You can run repeated executions without recompiling, but if you
change any block parameters, then the block automatically recompiles before
execution.

This table shows how the **Simulate using** parameter affects the
overall simulation behavior.

When the Simulink® model is in `Accelerator` mode, the block mode specified
using **Simulate using** overrides the simulation mode.

**Acceleration Modes**

|  |  |  |  |
| --- | --- | --- | --- |
| Block Simulation | Simulation Behavior | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | The block executes using the MATLAB interpreter. | The block executes using the MATLAB interpreter. | Creates a standalone executable from the model. |
| `Code Generation` | The block is compiled. | All blocks in the model are compiled. |

For more information, see Choosing a Simulation Mode (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SimulateUsing` |
| **Type:** enum |
| **Values:** `Interpreted Execution`, `Code Generation` |
| **Default:** `Interpreted Execution` |
## Libraries

Phased Array System Toolbox / Environment and Target

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Motion platform

The Motion Platform block models the motion of multiple platforms such as airplanes, ground vehicles, and/or receiving and transmitting sensors arrays, determining their positions and velocities. The platforms move along trajectories determined by initial positions and velocities, according to which motion model you choose — the velocity or acceleration model. The platform positions and velocities are updated at each simulation step. In addition, you can specify initial orientations for the platforms and obtain orientation updates.
