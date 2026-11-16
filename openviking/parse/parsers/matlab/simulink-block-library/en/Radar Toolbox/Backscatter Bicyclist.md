---
type: simulink-block
title: 'Backscatter Bicyclist'
family: 'radar'
product_id: 'radar'
product_name: 'Radar Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'backscatterbicyclistblock'
documentation_source_path: 'ref/backscatterbicyclistblock.html'
language: en
---

# Backscatter Bicyclist

## Ports

### Input

### **X** — Incident radar signals complex-valued *M*-by-*N* matrix

Incident radar signals on each bicyclist scatterer, specified as a complex-valued
*M*-by-*N* matrix. *M* is the
number of samples in the signal. *N* is the number of point
scatterers on the bicyclist and is determined partly from the number of spokes in each
wheel, *N*ws. See Bicyclist Scatterer Indices for the column
representing the incident signal at each scatterer.

The size of the first dimension of the input matrix can vary to
simulate a changing signal length. A size change can occur, for example, in the case of a pulse
waveform with variable pulse repetition frequency.

**Data Types:** `double`
**Complex Number Support:** Yes

### **AngH** — Bicyclist heading `0.0` | scalar

Heading of the bicyclist, specified as a scalar. Heading is measured in the
*xy*-plane from the *x*-axis towards the
*y*-axis. Units are in degrees.

**Example:** `-34`

**Data Types:** `double`

### **Ang** — Directions of incident signals real-valued 2-by-*N* vector

Directions of incident signals on the scatterers, specified as a real-valued
2-by-*N* matrix. Each column of `Ang` specifies
the incident direction of the signal to the corresponding scatterer. Each column takes
the form of an *[AzimuthAngle;ElevationAngle]* pair. Units are in
degrees. See Bicyclist Scatterer Indices for the column
representing the incident arrival angle at each scatterer.

**Data Types:** `double`

### **Speed** — Bicyclist speed nonnegative scalar

Speed of bicyclist, specified as a nonnegative scalar. The motion model limits the
speed to 60 m/s. Units are in meters per second.

**Example:** `8`

**Data Types:** `double`

### **Coast** — Bicyclist coasting state `false` (default) | `true`

Bicyclist coasting state, specified as `false` or
`true`. This property controls the coasting of the bicyclist. If
set to `true`, the bicyclist does not pedal but the wheels are still
rotating (freewheeling). If set to `false`, the bicyclist is pedaling
and the `Gear transmission ratio` parameter determines the ratio of
wheel rotations to pedal rotations.

**Tunable:** Yes

**Data Types:** `Boolean`
### Output

### **Y** — Combined reflected radar signals complex-valued *M*-by-1 column vector

Combined reflected radar signals, returned as a complex-valued
*M*-by-1 column vector. *M* equals the number of
samples in the input signal, `X`.

**Data Types:** `double`
**Complex Number Support:** Yes

### **Pos** — Positions of scatterers real-valued 3-by-*N* matrix

Positions of scatterers, returned as a real-valued 3-by-*N*
matrix. *N* is the number of scatterers on the bicyclist. Each column
represents the Cartesian position,
[*x*;*y*;*z*], of one of the
scatterers. Units are in meters. See Bicyclist Scatterer Indices for the column
representing the position of each scatterer.

**Data Types:** `double`

### **Vel** — Velocity scatterers real-valued 3-by-*N* matrix

Velocity of scatterers, returned as a real-valued 3-by-*N*
matrix. *N* is the number of scatterers on the bicyclist. Each column
represents the Cartesian velocity,
[*vx*;*vy*;*vz*], of one of the
scatterers. Units are in meters per second. See Bicyclist Scatterer Indices for the column
representing the velocity of each scatterer.

**Data Types:** `double`

### **Ax** — Orientation of scatterers real-valued 3-by-3 matrix

Orientation axes of scatterers, returned as a real-valued 3-by-3 matrix.

**Data Types:** `double`

## Parameters

### **Number of wheel spokes** — Number of spokes per wheel `20` (default) | positive integer

Number of spokes per wheel of the bicycle, specified as a positive integer from 3
through 50, inclusive. Units are dimensionless.

**Data Types:** `double`

### **Gear transmission ratio** — Ratio of wheel rotations to pedal rotations `1.5` (default) | positive scalar

Ratio of wheel rotations to pedal rotations, specified as a positive scalar. The
gear ratio must be in the range 0.5 through 6. Units are dimensionless.

**Data Types:** `double`

### **Signal carrier frequency (Hz)** — Carrier frequency `77e9` (default) | positive scalar

Carrier frequency of narrowband incident signals, specified as a positive scalar.
Units are in Hz.

**Example:** `1e9`

**Data Types:** `double`

### **Initial position (m)** — Initial position of bicyclist `[0;0;0]` (default) | 3-by-1 real-valued vector

Initial position of the bicyclist, specified as a 3-by-1 real-valued vector in the
form of [*x*;*y*;*z*]. Units are in
meters.

**Data Types:** `double`

### **Initial heading direction (deg)** — Initial heading of bicyclist `0` (default) | scalar

Initial heading of the bicyclist, specified as a scalar. Heading is measured in the
*xy*-plane from the *x*-axis towards
*y*-axis. Units are in degrees.

**Data Types:** `double`

### **Initial bicyclist speed (m/s)** — Initial speed of bicyclist `4` (default) | nonnegative scalar

Initial speed of bicyclist, specified as a nonnegative scalar. The motion model
limits the speed to a maximum of 60 m/s (216 kph). Units are in meters per
second.

**Tunable:** Yes

**Data Types:** `double`

### **Propagation speed (m/s)** — Signal propagation speed `physconst('LightSpeed')` (default) | positive scalar

Signal propagation speed, specified as a real-valued positive scalar. The default
value of the speed of light is the value returned by
`physconst('LightSpeed')`.

**Data Types:** `double`

### **RCS pattern** — Source of RCS pattern `Auto` (default) | `Property`

Source of the RCS pattern, specified as either `Auto` or
`Property`. When you specify `Auto`,
the pattern is a 1-by-361 matrix containing values derived from radar measurements taken
at 77 GHz.

### **Azimuth angles (deg)** — Azimuth angles `[-180:180]` (default) | 1-by-*P* real-valued row vector | *P*-by-1 real-valued column vector

Azimuth angles used to define the angular coordinates of each column of the matrix
specified by the **Radar cross section pattern (square meters)**
parameter. Specify the azimuth angles as a length *P* vector.
*P* must be greater than two. Angle units are in degrees.

**Example:** `[-45:0.1:45]`

#### Dependencies

To enable this parameter, set the **RCS pattern** parameter to
`Property`.

**Data Types:** `double`

### **Elevation angles (deg)** — Elevation angles `[-90:90]` (default) | 1-by-*Q* real-valued row vector | *Q*-by-1 real-valued column vector

Elevation angles used to define the angular coordinates of each row of the matrix
specified by the **Radar cross section pattern (square meters)**
parameter. Specify the elevation angles as a length *Q* vector.
*Q* must be greater than two. Angle units are in degrees.

#### Dependencies

To enable this parameter, set the **RCS pattern** parameter to
`Property`.

**Data Types:** `double`

### **Radar cross section pattern (square meters)** — Radar cross-section pattern 1-by-361 real-valued matrix (default) | *Q*-by-*P* real-valued matrix | 1-by-*P* real-valued vector

Radar cross-section (RCS) pattern as a function of elevation and azimuth angle,
specified as a *Q*-by-*P* real-valued matrix or a
1-by-*P* real-valued vector. *Q* is the length of
the vector defined by the `ElevationAngles` property.
*P* is the length of the vector defined by the
`AzimuthAngles` property. Units are in square meters.

You can also specify the pattern as a 1-by-*P* real-valued vector
of azimuth angles for one elevation.

The default value of this property is a 1-by-361 matrix containing values derived
from radar measurements taken at 77 GHz found in
`backscatterBicyclist.defaultRCSPattern`.

#### Dependencies

To enable this parameter, set the **RCS pattern** parameter to
`Property`.

**Data Types:** `double`

### **Simulate using** — Block simulation method `Interpreted Execution` (default) | `Code Generation`

Block simulation, specified as `Interpreted Execution` or
`Code Generation`. If you want your block to use the
MATLAB® interpreter, choose `Interpreted Execution`. If
you want your block to run as compiled code, choose `Code
Generation`. Compiled code requires time to compile but usually runs
faster.

Interpreted execution is useful when you are developing and tuning a model. The
block runs the underlying System object™ in MATLAB. You can change and execute your model quickly. When you are satisfied
with your results, you can then run the block using `Code
Generation`. Long simulations usually run faster as compiled code than
interpreted execution. You can run repeated executions without recompiling, but if you
change any block parameters, then the block automatically recompiles before
execution.

This table shows how the **Simulate using** parameter affects the
overall simulation behavior.

When the Simulink model is in `Accelerator` mode, the block mode specified
using **Simulate using** overrides the simulation mode.

**Acceleration Modes**

|  |  |  |  |
| --- | --- | --- | --- |
| **Block Simulation** | **Simulation Behavior** | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | The block executes using the MATLAB interpreter. | The block executes using the MATLAB interpreter. | Creates a standalone executable from the model. |
| `Code Generation` | The block is compiled. | All blocks in the model are compiled. |

For more information, see Choosing a Simulation Mode (Simulink).

## Libraries

Radar Toolbox

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

## Description

Backscatter signals from bicyclist

The Backscatter Bicyclist block simulates backscattered radar signals reflected from a
moving bicyclist. The bicyclist consists of the bicycle and its rider. The object models the
motion of the bicyclist and computes the sum of all reflected signals from multiple discrete
scatterers on the bicyclist. The model ignores internal occlusions within the bicyclist. The
reflected signals are computed using a multi-scatterer model developed from a 77-GHz radar
system.

Scatterers are located on five major bicyclist components:

- bicycle frame and rider
- bicycle pedals
- upper and lower legs of the rider
- front wheel
- back wheel

Excluding the wheels, there are 114 scatterers on the bicyclist. The wheels
contain scatterers on the rim and spokes. The number of scatterers on the wheels depends on
the number of spokes per wheel, which can be specified using the
`NumWheelSpokes` property.
