---
type: simulink-block
title: 'Root WSF DOA'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Direction of Arrival'
documentation_page: 'rootwsfdoa'
documentation_source_path: 'ref/rootwsfdoa.html'
language: en
---

# Root WSF DOA

## Ports
```yaml
ports:
- name: In
  summary: Input signal *M*-by-*N* complex-valued matrix
  direction: input
  data_types: single | double
- name: Ang
  summary: Estimated broadside DOA angles *P*-length row vector
  direction: output
  data_types: double
```

### Input

### **In** — Input signal *M*-by-*N* complex-valued matrix

Input signal, specified as an
*M*-by-*N* complex-valued matrix.
*M* is the number of samples in the signals. The
*N* columns of the matrix correspond to different
signals.

The size of the first dimension of the input matrix can vary to
simulate a changing signal length. A size change can occur, for example, in the case of a pulse
waveform with variable pulse repetition frequency.

**Data Types:** `single` | `double`
### Output

### **Ang** — Estimated broadside DOA angles *P*-length row vector

Estimated broadside direction-of-arrival (DOA) angles, returned as a
*P*-length row vector. Units are in degrees.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Signal propagation speed (m/s)
  summary: Signal propagation speed physconst('LightSpeed') (default) | real-valued positive scalar
  group: Main Tab
- name: Operating frequency (Hz)
  summary: System operating frequency 3e8 (default) | positive real scalar
  group: Main Tab
- name: Number of signals
  summary: Number of signals 1 (default) | positive integer scalar
  group: Main Tab
- name: Iterative method
  summary: Iterative method IMODE (default) | IQML
  group: Main Tab
- name: Maximum number of iterations
  summary: Maximum number of iterations Inf (default)
  group: Main Tab
- name: Simulate using
  summary: Block simulation method Interpreted Execution (default) | Code Generation
  group: Main Tab
  block_parameter: SimulateUsing
  type: enum
  values: Interpreted Execution, Code Generation
  default: Interpreted Execution
- name: Specify sensor array as
  summary: Method to specify array Array (no subarrays) (default) | MATLAB expression
  group: Sensor Array Tab
- name: Element type
  summary: Array element types Isotropic Antenna (default) | Cardioid Antenna | Cosine Antenna | Custom Antenna | Gaussian
    Antenna | Sinc Antenna | Omni Microphone | Custom Microphone
  group: Sensor Array Tab
- name: Operating frequency range (Hz)
  summary: Operating frequency range of the antenna or microphone element [0,1e20] (default) | real-valued 1-by-2 row vector
  group: Sensor Array Tab
- name: Baffle the back of the element
  summary: Set back response of an Isotropic Antenna element or an Omni Microphone element to zero off (default) | on
  group: Sensor Array Tab
- name: Null axis direction
  summary: Null axis direction -x (default) | +x | +y | -y | +z | -z
  group: Sensor Array Tab
- name: Exponent of cosine pattern
  summary: Exponents of azimuth and elevation cosine patterns [1.5 1.5] (default) | nonnegative scalar | real-valued 1-by-2
    matrix of nonnegative values
  group: Sensor Array Tab
- name: Operating frequency vector (Hz)
  summary: Operating frequency range of custom antenna or microphone elements [0,1e20] (default) | real-valued row vector
  group: Sensor Array Tab
- name: Frequency responses (dB)
  summary: Antenna and microphone frequency response [0,0] (default) | real-valued row vector
  group: Sensor Array Tab
- name: Input Pattern Coordinate System
  summary: Coordinate system of custom antenna pattern az-el (default) | phi-theta
  group: Sensor Array Tab
- name: Azimuth angles (deg)
  summary: Azimuth angles of antenna radiation pattern [-180:180] (default) | real-valued row vector
  group: Sensor Array Tab
- name: Elevation angles (deg)
  summary: Elevation angles of antenna radiation pattern [-90:90] (default) | real-valued row vector
  group: Sensor Array Tab
- name: Phi Angles (deg)
  summary: Phi angle coordinates of custom antenna radiation pattern 0:360 | real-valued 1-by-*P* row vector
  group: Sensor Array Tab
- name: Theta Angles (deg)
  summary: Theta angle coordinates of custom antenna radiation pattern 0:180 | real-valued 1-by-*Q* row vector
  group: Sensor Array Tab
- name: Magnitude pattern (dB)
  summary: Magnitude of combined antenna radiation pattern zeros(181,361) (default) | real-valued *Q*-by-*P* matrix | real-valued
    *Q*-by-*P*-by-*L* array
  group: Sensor Array Tab
- name: Phase pattern (deg)
  summary: Custom antenna radiation phase pattern zeros(181,361) (default) | real-valued *Q*-by-*P* matrix | real-valued *Q*-by-*P*-by-*L*
    array
  group: Sensor Array Tab
- name: Align element normal with array normal
  summary: Align element normal with array normal on (default) | off
  group: Sensor Array Tab
- name: Radiation pattern beamwidth (deg)
  summary: Radiation pattern beamwidth [10,10] (default)
  group: Sensor Array Tab
- name: Polar pattern frequencies (Hz)
  summary: Polar pattern microphone response frequencies 1e3 (default) | real scalar | real-valued 1-by-*L* row vector
  group: Sensor Array Tab
- name: Polar pattern angles (deg)
  summary: Polar pattern response angles [-180:180] (default) | real-valued -by-*P* row vector
  group: Sensor Array Tab
- name: Polar pattern (dB)
  summary: Custom microphone polar response zeros(1,361) (default) | real-valued *L*-by-*P* matrix
  group: Sensor Array Tab
- name: Number of elements
  summary: Number of array elements in U 2 (default) | positive integer greater than or equal to two
  group: Sensor Array Tab
- name: Element spacing
  summary: Distance between ULA elements 0.5 (default) | positive scalar
  group: Sensor Array Tab
- name: Array axis
  summary: Linear axis direction of ULA y (default) | x | z
  group: Sensor Array Tab
- name: Taper
  summary: ULA array taper 1 (default) | complex-valued vector
  group: Sensor Array Tab
- name: Expression
  summary: MATLAB expression used to create an array Phased Array System Toolbox™ array System object
  group: Sensor Array Tab
```

### Main Tab

### **Signal propagation speed (m/s)** — Signal propagation speed `physconst('LightSpeed')` (default) | real-valued positive scalar

Signal propagation speed, specified as a real-valued positive scalar. The default
value of the speed of light is the value returned by
`physconst('LightSpeed')`. Units are in meters per second.

**Example:** `3e8`

**Data Types:** `double`

### **Operating frequency (Hz)** — System operating frequency `3e8` (default) | positive real scalar

System operating frequency, specified as a positive scalar. Units are in Hz.

### **Number of signals** — Number of signals `1` (default) | positive integer scalar

Specify the number of signals as a positive integer scalar.

### **Iterative method** — Iterative method `IMODE` (default) | `IQML`

Specify the iterative method as one of
`IMODE` or
`IQML`.

### **Maximum number of iterations** — Maximum number of iterations `Inf` (default)

Specify the maximum number of iterations as a positive integer or
`Inf`.

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

### Sensor Array Tab

### **Specify sensor array as** — Method to specify array `Array (no subarrays)` (default) | `MATLAB expression`

Method to specify array, specified as `Array (no subarrays)`
or `MATLAB expression`.

- `Array (no subarrays)` — use the block
  parameters to specify the array.
- `MATLAB expression` — create the array
  using a MATLAB expression.

#### Element Parameters

### **Element type** — Array element types `Isotropic Antenna` (default) | `Cardioid Antenna` | `Cosine Antenna` | `Custom Antenna` | `Gaussian Antenna` | `Sinc Antenna` | `Omni Microphone` | `Custom Microphone`

Antenna or microphone type, specified as one of the following:

- `Isotropic Antenna`
- `Cardioid Antenna`
- `Cosine Antenna`
- `Custom Antenna`
- `Gaussian Antenna`
- `Sinc Antenna`
- `Omni Microphone`
- `Custom Microphone`

### **Operating frequency range (Hz)** — Operating frequency range of the antenna or microphone element `[0,1e20]` (default) | real-valued 1-by-2 row vector

Specify the operating frequency range of the antenna or microphone element as a 1-by-2
row vector in the form `[LowerBound,UpperBound]`. The element has no
response outside this frequency range. Frequency units are in Hz.

#### Dependencies

To enable this parameter, set **Element type** to
`Isotropic Antenna`, `Cosine Antenna`, or
`Omni Microphone`.

### **Baffle the back of the element** — Set back response of an `Isotropic Antenna` element or an `Omni Microphone` element to zero off (default) | on

Select this check box to baffle the back response of
the element. When back baffled, the responses at
all azimuth angles beyond ±90° from
broadside are set to zero. The broadside direction
is defined as 0° azimuth angle and 0° elevation
angle.

#### Dependencies

To enable this check box, set
**Element type** to
`Isotropic Antenna` or
`Omni Microphone`.

### **Null axis direction** — Null axis direction `-x` (default) | `+x` | `+y` | `-y` | `+z` | `-z`

#### Dependencies

To enable this parameter, set **Element type** to `Cardioid Antenna`.

### **Exponent of cosine pattern** — Exponents of azimuth and elevation cosine patterns `[1.5 1.5]` (default) | nonnegative scalar | real-valued 1-by-2 matrix of nonnegative values

Specify the exponents of the cosine pattern as a nonnegative scalar or
a real-valued 1-by-2 matrix of nonnegative values. When
**Exponent of cosine pattern** is a
1-by-2 vector, the first element is the exponent in the azimuth
direction and the second element is the exponent in the
elevation direction. When you set this parameter to a scalar,
both the azimuth direction and elevation direction cosine
patterns are raised to the same power.

#### Dependencies

To enable this parameter, set **Element
type** to `Cosine
Antenna`.

### **Operating frequency vector (Hz)** — Operating frequency range of custom antenna or microphone elements `[0,1e20]` (default) | real-valued row vector

Specify the frequencies at which to set antenna and microphone frequency responses as
a 1-by-*L* row vector of increasing real values. The antenna or
microphone element has no response outside the frequency range specified by the minimum
and maximum elements of this vector. Frequency units are in Hz.

#### Dependencies

To enable this parameter, set **Element type** to `Custom
Antenna` or `Custom Microphone`. Use
**Frequency responses (dB)** to set the responses at these
frequencies.

### **Frequency responses (dB)** — Antenna and microphone frequency response `[0,0]` (default) | real-valued row vector

Frequency response of a custom antenna or custom
microphone for the frequencies defined by the
**Operating frequency vector
(Hz)** parameter. The dimensions of
**Frequency responses (dB)** must
match the dimensions of the vector specified by
the **Operating frequency vector
(Hz)** parameter.

#### Dependencies

To enable this parameter, set
**Element type** to
`Custom Antenna` or
`Custom
Microphone`.

### **Input Pattern Coordinate System** — Coordinate system of custom antenna pattern `az-el` (default) | `phi-theta`

Coordinate system of custom antenna pattern, specified
`az-el` or `phi-theta`. When you
specify `az-el`, use the **Azimuth angles
(deg)** and **Elevations angles (deg)** parameters to
specify the coordinates of the pattern points. When you specify
`phi-theta`, use the **Phi angles (deg)**
and **Theta angles (deg)** parameters to specify the coordinates of the
pattern points.

#### Dependencies

To enable this parameter, set **Element type** to
`Custom Antenna`.

### **Azimuth angles (deg)** — Azimuth angles of antenna radiation pattern `[-180:180]` (default) | real-valued row vector

Specify the azimuth angles at which to calculate the antenna radiation pattern
as a 1-by-*P* row vector. *P* must be
greater than 2. Azimuth angles must lie between –180° and 180°,
inclusive, and be in strictly increasing order.

#### Dependencies

To enable this parameter, set the **Element type**
parameter to `Custom Antenna` and the
**Input Pattern Coordinate System**
parameter to `az-el`.

### **Elevation angles (deg)** — Elevation angles of antenna radiation pattern `[-90:90]` (default) | real-valued row vector

Specify the elevation angles at which to compute the radiation pattern as a
1-by-*Q* vector. *Q* must be
greater than 2. Angle units are in degrees. Elevation angles must lie
between –90° and 90°, inclusive, and be in strictly increasing
order.

#### Dependencies

To enable this parameter, set the **Element type**
parameter to `Custom Antenna` and the
**Input Pattern Coordinate System**
parameter to `az-el`.

### **Phi Angles (deg)** — Phi angle coordinates of custom antenna radiation pattern `0:360` | real-valued 1-by-*P* row vector

Phi angles of points at which to specify the antenna radiation pattern, specify as a
real-valued 1-by-*P* row vector. *P* must be greater
than 2. Angle units are in degrees. Phi angles must lie between 0° and 360° and be in
strictly increasing order.

#### Dependencies

To enable this parameter, set the **Element type** parameter to
`Custom Antenna` and the **Input Pattern Coordinate
System** parameter to `phi-theta`.

### **Theta Angles (deg)** — Theta angle coordinates of custom antenna radiation pattern `0:180` | real-valued 1-by-*Q* row vector

Theta angles of points at which to specify the antenna radiation pattern, specify as a
real-valued 1-by-*Q* row vector. *Q* must be greater
than 2. Angle units are in degrees. Theta angles must lie between 0° and 360° and be in
strictly increasing order.

#### Dependencies

To enable this parameter, set the **Element type** parameter to
`Custom Antenna` and the **Input Pattern Coordinate
System** parameter to `phi-theta`.

### **Magnitude pattern (dB)** — Magnitude of combined antenna radiation pattern `zeros(181,361)` (default) | real-valued *Q*-by-*P* matrix | real-valued *Q*-by-*P*-by-*L* array

Magnitude of the combined antenna radiation pattern, specified as a
*Q*-by-*P* matrix or a
*Q*-by-*P*-by-*L* array.

- When the **Input Pattern Coordinate System** parameter is
  set to `az-el`, *Q* equals the
  length of the vector specified by the **Elevation angles
  (deg)** parameter and *P* equals the length of
  the vector specified by the **Azimuth angles (deg)**
  parameter.
- When the **Input Pattern Coordinate System** parameter is
  set to `phi-theta`, *Q* equals the
  length of the vector specified by the **Theta Angles
  (deg)** parameter and *P* equals the length of
  the vector specified by the **Phi Angles (deg)**
  parameter.

The quantity *L* equals the length of the
**Operating frequency vector (Hz)**.

- If this parameter is a *Q*-by-*P*
  matrix, the same pattern is applied to *all* frequencies
  specified in the **Operating frequency vector (Hz)**
  parameter.
- If the value is a
  *Q*-by-*P*-by-*L*
  array, each *Q*-by-*P* page of the array
  specifies a pattern for the *corresponding* frequency
  specified in the **Operating frequency vector (Hz)**
  parameter.

#### Dependencies

To enable this parameter, set **Element type** to
`Custom Antenna`.

### **Phase pattern (deg)** — Custom antenna radiation phase pattern `zeros(181,361)` (default) | real-valued *Q*-by-*P* matrix | real-valued *Q*-by-*P*-by-*L* array

Phase of the combined antenna radiation pattern, specified as a
*Q*-by-*P* matrix or a
*Q*-by-*P*-by-*L* array.

- When the **Input Pattern Coordinate System** parameter is
  set to `az-el`, *Q* equals the
  length of the vector specified by the **Elevation angles
  (deg)** parameter and *P* equals the length of
  the vector specified by the **Azimuth angles (deg)**
  parameter.
- When the **Input Pattern Coordinate System** parameter is
  set to `phi-theta`, *Q* equals the
  length of the vector specified by the **Theta Angles
  (deg)** parameter and *P* equals the length of
  the vector specified by the **Phi Angles (deg)**
  parameter.

The quantity *L* equals the length of the
**Operating frequency vector (Hz)**.

- If this parameter is a *Q*-by-*P*
  matrix, the same pattern is applied to *all* frequencies
  specified in the **Operating frequency vector (Hz)**
  parameter.
- If the value is a
  *Q*-by-*P*-by-*L*
  array, each *Q*-by-*P* page of the array
  specifies a pattern for the *corresponding* frequency
  specified in the **Operating frequency vector (**

#### Dependencies

To enable this parameter, set **Element type** to
`Custom Antenna`.

### **Align element normal with array normal** — Align element normal with array normal on (default) | off

#### Dependencies

This parameter is enabled when **Element type** is set to
`Custom Antenna`.

### **Radiation pattern beamwidth (deg)** — Radiation pattern beamwidth `[10,10]` (default)

#### Dependencies

This parameter is enabled when **Element type** is set to `Gaussian Antenna`.

### **Polar pattern frequencies (Hz)** — Polar pattern microphone response frequencies 1e3 (default) | real scalar | real-valued 1-by-*L* row vector

Polar pattern microphone response frequencies, specified as a real scalar, or a
real-valued, 1-by-*L* vector. The response frequencies lie within the
frequency range specified by the **Operating frequency vector (Hz)**
vector.

#### Dependencies

To enable this parameter, set **Element type** set to
`Custom Microphone`.

### **Polar pattern angles (deg)** — Polar pattern response angles `[-180:180]` (default) | real-valued -by-*P* row vector

Specify the polar pattern response angles, as a 1-by-*P* vector. The
angles are measured from the central pickup axis of the microphone and must be between
–180° and 180°, inclusive.

#### Dependencies

To enable this parameter, set **Element type** to
`Custom Microphone`.

### **Polar pattern (dB)** — Custom microphone polar response `zeros(1,361)` (default) | real-valued *L*-by-*P* matrix

Specify the magnitude of the custom microphone element polar patterns as an
*L*-by-*P* matrix. *L* is the
number of frequencies specified in **Polar pattern frequencies (Hz)**.
*P* is the number of angles specified in **Polar pattern
angles (deg)**. Each row of the matrix represents the magnitude of the
polar pattern measured at the corresponding frequency specified in **Polar
pattern frequencies (Hz)** and all angles specified in **Polar
pattern angles (deg)**. The pattern is measured in the azimuth plane. In
the azimuth plane, the elevation angle is 0° and the central pickup axis is 0°
degrees azimuth and 0° degrees elevation. The polar pattern is symmetric around the
central axis. You can construct the microphone response pattern in 3-D space from the
polar pattern.

#### Dependencies

To enable this parameter, set **Element type** to
`Custom Microphone`.

#### ULA Parameters

### **Number of elements** — Number of array elements in U `2` (default) | positive integer greater than or equal to two

The number of array elements for ULA arrays, specified as an integer greater than or
equal to two.

**Example:** `11`

**Data Types:** `double`

### **Element spacing** — Distance between ULA elements `0.5` (default) | positive scalar

Distance between adjacent ULA elements, specified as a positive scalar. Units are in
meters.

**Example:** `1.5`

### **Array axis** — Linear axis direction of ULA `y` (default) | `x` | `z`

Linear axis direction of ULA, specified as `y`,
`x`, or `z`. All ULA array
elements are uniformly spaced along this axis in the local array coordinate
system.

#### Dependencies

- To enable this parameter, set **Geometry** to
  `ULA`.
- This parameter is also enabled when the block only supports ULA
  arrays.

### **Taper** — ULA array taper `1` (default) | complex-valued vector

Tapers, also known as *element weights*, are applied to sensor
elements in the array. Tapers are used to modify both the amplitude and phase of the
transmitted or received data.

Specify element tapering as a complex-valued scalar or a complex-valued
1-by-*N* row vector. In this vector, *N*
represents the number of elements in the array. If **Taper** is a
scalar, the same weight is applied to each element. If **Taper** is a
vector, a weight from the vector is applied to the corresponding sensor element. A
weight must be applied to each element in the sensor array.

**Example:** [0.5;1;0.5]

**Data Types:** `double`
**Complex Number Support:** Yes

### **Expression** — MATLAB expression used to create an array Phased Array System Toolbox™ array System object

MATLAB expression used to create a ULA array, specified as a valid Phased Array System Toolbox array System object.

**Example:** `phased.ULA('NumElements',13)`

#### Dependencies

To enable this parameter, set **Specify sensor array as** to
`MATLAB expression`.
## Libraries

Phased Array System Toolbox / Direction of Arrival

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Root weighted subspace fitting (WSF) direction of arrival (DOA) estimator for ULA

The Root WSF DOA block estimates the direction of arrival of a specified
number of narrowband signals incident on a uniform linear array (ULA) using the
root-weighted subspace fitting (RootWSF) algorithm.
