---
type: simulink-block
title: 'ULA Beamscan Spectrum'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Direction of Arrival'
documentation_page: 'ulabeamscanspectrum'
documentation_source_path: 'ref/ulabeamscanspectrum.html'
language: en
---

# ULA Beamscan Spectrum

## Ports
```yaml
ports:
- name: Port 1
  summary: Received signal *M*-by-*N* complex-valued matrix
  direction: input
  data_types: double
- name: Y
  summary: Beamscan spatial spectrum non-negative, real-valued column vector
  direction: output
  data_types: double
- name: Ang
  summary: Directions of arrival non-negative, real-valued column vector
  direction: output
  data_types: double
```

### Input

### **Port 1** — Received signal *M*-by-*N* complex-valued matrix

Received signal, specified as an *M*-by-*N*
complex-valued matrix. The quantity *M* is the number of sample
values (snapshots) contained in the signal and *N* is the number of
sensor elements in the array.

The size of the first dimension of the input matrix can vary to
simulate a changing signal length. A size change can occur, for example, in the case of a pulse
waveform with variable pulse repetition frequency.

**Data Types:** `double`
**Complex Number Support:** Yes
### Output

### **Y** — Beamscan spatial spectrum non-negative, real-valued column vector

Beamscan spatial spectrum, returned as a non-negative, real-valued column vector
representing the magnitude of the estimated beamscan spatial spectrum. Each entry
corresponds to an angle specified by the **Scan angles (deg)**
parameter.

**Data Types:** `double`

### **Ang** — Directions of arrival non-negative, real-valued column vector

Directions of arrival of the signals, returned as a real-valued row vector. The
direction of arrival angle is the broadside angle between the source direction and the
array axis. Angle units are in degrees. The length of the vector is the number of
signals specified by the **Number of signals** parameter. If the
object cannot identify peaks in the spectrum, it will return
`NaN`.

#### Dependencies

To enable this output port, select the **Enable DOA output**
check box.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Signal propagation speed (m/s)
  summary: Signal propagation speed physconst('LightSpeed') (default) | real-valued positive scalar
  group: ''
- name: Operating frequency (Hz)
  summary: System operating frequency 3e8 (default) | positive real scalar
  group: ''
- name: Number of bits in phase shifters
  summary: Number of phase shift quantization bits 0 (default) | nonnegative integer
  group: ''
- name: Forward-backward averaging
  summary: Enable forward-backward averaging off (default) | on
  group: ''
- name: Spatial smoothing
  summary: Enable spatial smoothing 0 (default) | non-negative integer
  group: ''
- name: Scan angles (deg)
  summary: Search angles for spectrum peaks -90:90 (default) | real-valued row vector
  group: ''
- name: Enable DOA output
  summary: Output directions of arrival through output port off (default) | on
  group: ''
- name: Number of signals
  summary: Expected number of arriving signals 1 (default) | positive integer
  group: ''
- name: Simulate using
  summary: Block simulation method Interpreted Execution (default) | Code Generation
  group: ''
  block_parameter: SimulateUsing
  type: enum
  values: Interpreted Execution, Code Generation
  default: Interpreted Execution
- name: Specify sensor array as
  summary: Method to specify array Array (no subarrays) (default) | MATLAB expression
  group: ''
- name: Expression
  summary: MATLAB expression used to create an array Phased Array System Toolbox™ array System object
  group: ''
- name: Element type
  summary: Array element types Isotropic Antenna (default) | Cosine Antenna | Custom Antenna | Omni Microphone | Custom Microphone
  group: ''
- name: Operating frequency range (Hz)
  summary: Operating frequency range of the antenna or microphone element [0,1e20] (default) | real-valued 1-by-2 row vector
  group: ''
- name: Operating frequency vector (Hz)
  summary: Operating frequency range of custom antenna or microphone elements [0,1e20] (default) | real-valued row vector
  group: ''
- name: Baffle the back of the element
  summary: Set back response of an Isotropic Antenna element or an Omni Microphone element to zero off (default) | on
  group: ''
- name: Exponent of cosine pattern
  summary: Exponents of azimuth and elevation cosine patterns [1.5 1.5] (default) | nonnegative scalar | real-valued 1-by-2
    matrix of nonnegative values
  group: ''
- name: Frequency responses (dB)
  summary: Antenna and microphone frequency response [0,0] (default) | real-valued row vector
  group: ''
- name: Input Pattern Coordinate System
  summary: Coordinate system of custom antenna pattern az-el (default) | phi-theta
  group: ''
- name: Azimuth angles (deg)
  summary: Azimuth angles of antenna radiation pattern [-180:180] (default) | real-valued row vector
  group: ''
- name: Elevation angles (deg)
  summary: Elevation angles of antenna radiation pattern [-90:90] (default) | real-valued row vector
  group: ''
- name: Phi Angles (deg)
  summary: Phi angle coordinates of custom antenna radiation pattern 0:360 | real-valued 1-by-*P* row vector
  group: ''
- name: Theta Angles (deg)
  summary: Theta angle coordinates of custom antenna radiation pattern 0:180 | real-valued 1-by-*Q* row vector
  group: ''
- name: Radiation pattern (dB)
  summary: Custom antenna radiation pattern zeros(181,361) | complex-valued matrix | complex-valued MATLAB array
  group: ''
- name: Polar pattern frequencies (Hz)
  summary: Polar pattern microphone response frequencies 1e3 (default) | real scalar | real-valued 1-by-*L* row vector
  group: ''
- name: Polar pattern angles (deg)
  summary: Polar pattern response angles [-180:180] (default) | real-valued -by-*P* row vector
  group: ''
- name: Polar pattern (dB)
  summary: Custom microphone polar response zeros(1,361) (default) | real-valued *L*-by-*P* matrix
  group: ''
- name: Number of elements
  summary: Number of array elements in U 2 (default) | positive integer greater than or equal to two
  group: ''
- name: Element spacing
  summary: Distance between ULA elements 0.5 (default) | positive scalar
  group: ''
- name: Array axis
  summary: Linear axis direction of ULA y (default) | x | z
  group: ''
- name: Taper
  summary: Array element tapers 1 (default) | complex scalar | complex-valued row vector
  group: ''
```

### **Signal propagation speed (m/s)** — Signal propagation speed `physconst('LightSpeed')` (default) | real-valued positive scalar

Signal propagation speed, specified as a real-valued positive scalar. The default
value of the speed of light is the value returned by
`physconst('LightSpeed')`. Units are in meters per second.

**Example:** `3e8`

**Data Types:** `double`

### **Operating frequency (Hz)** — System operating frequency `3e8` (default) | positive real scalar

System operating frequency, specified as a positive scalar. Units are in Hz.

### **Number of bits in phase shifters** — Number of phase shift quantization bits `0` (default) | nonnegative integer

The number of bits used to quantize the phase shift component of beamformer or
steering vector weights. Specify the number of bits as a non-negative integer. A value
of zero indicates that no quantization is performed.

### **Forward-backward averaging** — Enable forward-backward averaging off (default) | on

Select this parameter to use forward-backward averaging to estimate the covariance
matrix for sensor arrays with a conjugate symmetric array manifold structure.

### **Spatial smoothing** — Enable spatial smoothing `0` (default) | non-negative integer

Specify the amount of averaging used by spatial smoothing to estimate the covariance
matrix as a nonnegative integer. Each increase in smoothing handles one extra coherent
source, but reduces the effective number of elements by one. The maximum value of this
parameter is *N – 2*, where *N* is the number of
sensors in the ULA.

### **Scan angles (deg)** — Search angles for spectrum peaks `-90:90` (default) | real-valued row vector

Specify the scan angles in degrees as a real-valued row vector. The angles are array
broadside angles and must lie between –90° and 90°, inclusive. You must specify the
angles in increasing order.

### **Enable DOA output** — Output directions of arrival through output port off (default) | on

Select this parameter to output the signals directions of arrival (DOA)
through the **Ang** output port.

### **Number of signals** — Expected number of arriving signals `1` (default) | positive integer

Specify the expected number of signals for DOA estimation as a positive scalar
integer.

#### Dependencies

To enable this parameter, select the **Enable DOA output** check
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

#### Sensor Array Tab

### **Specify sensor array as** — Method to specify array `Array (no subarrays)` (default) | `MATLAB expression`

Method to specify array, specified as `Array (no subarrays)`
or `MATLAB expression`.

- `Array (no subarrays)` — use the block
  parameters to specify the array.
- `MATLAB expression` — create the array
  using a MATLAB expression.

### **Expression** — MATLAB expression used to create an array Phased Array System Toolbox™ array System object

MATLAB expression used to create an array, specified as a valid Phased Array System Toolbox array System object.

**Example:** `phased.URA('Size',[5,3])`

#### Dependencies

To enable this parameter, set **Specify sensor array as** to
`MATLAB expression`.

#### Element Parameters

### **Element type** — Array element types `Isotropic Antenna` (default) | `Cosine Antenna` | `Custom Antenna` | `Omni Microphone` | `Custom Microphone`

Antenna or microphone type, specified as one of the following:

- `Isotropic Antenna`
- `Cosine Antenna`
- `Custom Antenna`
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

### **Radiation pattern (dB)** — Custom antenna radiation pattern `zeros(181,361)` | complex-valued matrix | complex-valued MATLAB array

Magnitude of the combined polarized antenna radiation pattern,
specified as a *Q*-by-*P* matrix
or a *Q*-by-*P*-by-*L* array.
The value of *Q* must equal the value of *Q* specified
by **Elevation angles (deg)**. The value of *P* must
equal the value of *P* specified by **Azimuth
angles (deg)**. The value of *L* must equal
the value of *L* specified by **Operating
frequency vector (Hz)**.

#### Dependencies

To enable this parameter, set **Element type** to `Custom
Antenna`.

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

#### Array Parameters

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

Linear axis direction of ULA, specified as `y`, `x`,
or `z`. Then, all ULA array elements are
uniformly spaced along this axis in the local array coordinate system.

### **Taper** — Array element tapers 1 (default) | complex scalar | complex-valued row vector

Specify element tapering as a complex-valued scalar or a
complex-valued 1-by-*N* row vector. In this
vector, *N* represents the number of elements
in the array.

Also known as *element weights*, tapers multiply
the array element responses. Tapers modify both amplitude and
phase of the response to reduce side lobes or steer the main
response axis.

If **Taper** is a scalar, the same weight is applied
to each element. If **Taper** is a vector, a
weight from the vector is applied to the corresponding sensor
element. The number of weights must match the number of elements
of the array.

**Data Types:** `double`
## Libraries

Phased Array System Toolbox / Direction of Arrival

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Beamscan spatial spectrum estimator for ULA

The ULA Beamscan Spectrum block estimates the spatial spectrum of incoming
narrowband signals by scanning a region of broadside angles using a narrowband conventional
beamformer applied to a uniform linear array. The block optionally calculates the direction of
arrival of a specified number of signals by estimating peaks of the spectrum.
