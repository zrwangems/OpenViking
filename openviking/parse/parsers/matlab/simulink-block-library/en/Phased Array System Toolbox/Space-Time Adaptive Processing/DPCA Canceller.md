---
type: simulink-block
title: 'DPCA Canceller'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Space-Time Adaptive Processing'
documentation_page: 'dpcacanceller'
documentation_source_path: 'ref/dpcacanceller.html'
language: en
---

# DPCA Canceller

## Ports
```yaml
ports:
- name: X
  summary: Input signal *M*-by-*N*-by-*P* complex-valued matrix
  direction: input
  data_types: double
- name: Idx
  summary: Index of range cells positive integer
  direction: input
  data_types: double
- name: PRF
  summary: Pulse repetition frequency positive scalar
  direction: input
  data_types: double
- name: Ang
  summary: Targeting direction 2-by-1 real-valued vector
  direction: input
  data_types: double
- name: Dop
  summary: Targeting Doppler frequency scalar
  direction: input
  data_types: double
- name: Y
  summary: Beamformed output *M*-by-1 complex-valued vector
  direction: output
  data_types: double
- name: W
  summary: Processing weights length *N*\P* complex-valued vector
  direction: output
  data_types: double
```

### Input

### **X** — Input signal *M*-by-*N*-by-*P* complex-valued matrix

Input signal, specified as an
*M*-by-*N*-by-*P*
complex-valued array. *M* is the number of range
samples, *N* is the number of channels, and
*P* is the number of pulses.

The size of the first dimension of the input matrix can vary to
simulate a changing signal length. A size change can occur, for example, in the case of a pulse
waveform with variable pulse repetition frequency.

**Data Types:** `double`
**Complex Number Support:** Yes

### **Idx** — Index of range cells positive integer

Index of range cells to compute processing weights.

**Example:** `1`

**Data Types:** `double`

### **PRF** — Pulse repetition frequency positive scalar

Pulse repetition frequency of current pulse, specified as a positive
scalar.

#### Dependencies

To enable this port, set the **Specify PRF as**
parameter to `Input port`.

**Data Types:** `double`

### **Ang** — Targeting direction `2`-by-`1` real-valued vector

Targeting direction, specified as a
`2`-by-*1* real-valued vector. The
vector takes the form of
`[AzimuthAngle;ElevationAngle]`. Angle units are in
degrees. The azimuth angle must lie between –180° and 180°, inclusive,
and the elevation angle must lie between –90° and 90°, inclusive. Angles
are defined with respect to the local coordinate system of the
array.

#### Dependencies

To enable this port, set the **Specify direction
as** parameter to `Input port`.

**Data Types:** `double`

### **Dop** — Targeting Doppler frequency scalar

Targeting Doppler frequency of current pulse, specified as a
scalar.

#### Dependencies

This port appears when the **Output pre-Doppler
result** check box is cleared and the **Specify
targeting Doppler as** parameter is set to
`Input port`.

**Data Types:** `double`
### Output

### **Y** — Beamformed output *M*-by-1 complex-valued vector

Processing output, returned as an
*M*-by-*1* complex-valued vector.
The quantity *M* is the number of range samples in the
input port `X`.

**Data Types:** `double`
**Complex Number Support:** Yes

### **W** — Processing weights length *N*\**P* complex-valued vector

Processing weights, returned as Length
*N*\**P* complex-valued vector. The
quantity *N* is the number of channels and
*P* is the number of pulses. When the
**Specify sensor array as** parameter is set to
`Partitioned array` or `Replicated
subarray`, *N* represents the number of
subarrays. *L* is the number of desired beamforming
directions specified in the `Ang` input port or by the
**Beamforming direction (deg)** parameter. There is
one set of weights for each beamforming direction.

#### Dependencies

To enable this port, select the **Enable weights
output** check box.

**Data Types:** `double`
**Complex Number Support:** Yes
## Parameters
```yaml
parameters:
- name: Signal propagation speed (m/s)
  summary: Signal propagation speed physconst('LightSpeed') (default) | real-valued positive scalar
  group: ''
- name: Operating frequency (Hz)
  summary: System operating frequency 3e8 (default) | positive real scalar
  group: ''
- name: Specify PRF as
  summary: Source of PRF value Property (default) | Input port
  group: ''
- name: Pulse repetition frequency (Hz)
  summary: Pulse repetition frequency 1 (default) | positive scalar
  group: ''
- name: Specify direction as
  summary: Specify source of targeting directions Property (default) | Input port
  group: ''
- name: Receiving mainlobe direction (deg)
  summary: Pointing direction of main lobe of array [0;0] (default) | real-valued 2-by-1 vector
  group: ''
- name: Number of bits in phase shifters
  summary: Number of phase shift quantization bits 0 (default) | nonnegative integer
  group: ''
- name: Specify targeting Doppler as
  summary: Source of targeting Doppler Property (default) | Input port
  group: ''
- name: Targeting Doppler (Hz)
  summary: Targeting Doppler of STAP processor 0 (default) | scalar
  group: ''
- name: Enable weights output
  summary: Option to output beamformer weights off (default) | on
  group: ''
- name: Output pre-Doppler result
  summary: Output results before Doppler filtering on (default) | off
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
- name: Magnitude pattern (dB)
  summary: Magnitude of combined antenna radiation pattern zeros(181,361) (default) | real-valued *Q*-by-*P* matrix | real-valued
    *Q*-by-*P*-by-*L* array
  group: ''
- name: Phase pattern (deg)
  summary: Custom antenna radiation phase pattern zeros(181,361) (default) | real-valued *Q*-by-*P* matrix | real-valued *Q*-by-*P*-by-*L*
    array
  group: ''
- name: MatchArrayNormal
  summary: Rotate antenna element to array normal on (default) | off
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
- name: Specify sensor array as
  summary: Type of array Array (no subarrays) (default) | MATLAB expression
  group: Array Parameters
- name: Number of elements
  summary: Number of array elements in U 2 (default) | positive integer greater than or equal to two
  group: Array Parameters
- name: Element spacing
  summary: Distance between ULA elements 0.5 (default) | positive scalar
  group: Array Parameters
- name: Array axis
  summary: Linear axis direction of ULA y (default) | x | z
  group: Array Parameters
- name: Taper
  summary: ULA array taper 1 (default) | complex-valued vector
  group: Array Parameters
- name: Expression
  summary: MATLAB expression used to create an array Phased Array System Toolbox array System object
  group: Array Parameters
```

#### Main Tab

### **Signal propagation speed (m/s)** — Signal propagation speed `physconst('LightSpeed')` (default) | real-valued positive scalar

Signal propagation speed, specified as a real-valued positive scalar. The default
value of the speed of light is the value returned by
`physconst('LightSpeed')`. Units are in meters per second.

**Example:** `3e8`

**Data Types:** `double`

### **Operating frequency (Hz)** — System operating frequency `3e8` (default) | positive real scalar

System operating frequency, specified as a positive scalar. Units are in Hz.

### **Specify PRF as** — Source of PRF value `Property` (default) | `Input port`

Source of PRF value, specified as `Property` or
`Input port`. When set to
`Property`, the **Pulse repetition frequency
(Hz)** parameter sets the PRF. When set to `Input
port`, pass in the PRF using the `PRF` input
port.

### **Pulse repetition frequency (Hz)** — Pulse repetition frequency `1` (default) | positive scalar

Pulse repetition frequency, PRF, specified as a positive scalar. Units are in Hertz.
Set this parameter to the same value set in any `Waveform` library
block used in the simulation.

#### Dependencies

To enable this parameter, set the **Specify PRF as** parameter to
`Property`.

### **Specify direction as** — Specify source of targeting directions `Property` (default) | `Input port`

Specify whether the targeting direction for the STAP processor block comes from a block
parameter or from the `ANG` input port. Values of this parameter
are

|  |  |
| --- | --- |
| `Property` | - For the ADPCA Canceller and   DPCA Canceller blocks, targeting   direction is specified using **Receiving   mainlobe direction (deg)**. - For the SMI Beamformer block,   targeting direction is specified using   **Targeting direction**.  These parameters appear only when the **Specify direction as** parameter is set to `Property`. |
| `Input port` | Enter the targeting directions using the `Ang` input port. This port appears only when **Specify direction as** is set to `Input port`. |

### **Receiving mainlobe direction (deg)** — Pointing direction of main lobe of array `[0;0]` (default) | real-valued 2-by-1 vector

Specify the direction of the main lobe of the receiving sensor array as a
real-valued 2-by-1 vector. The direction is specified in the format of
`[AzimuthAngle; ElevationAngle]`. The azimuth angle
should be between –180° and 180° and the elevation angle should be between
–90° and 90°.

**Example:** `[100;-45]`

#### Dependencies

To enable this parameter, set **Specify direction
as** to `Property`.

### **Number of bits in phase shifters** — Number of phase shift quantization bits `0` (default) | nonnegative integer

The number of bits used to quantize the phase shift component of beamformer or
steering vector weights. Specify the number of bits as a non-negative integer. A value
of zero indicates that no quantization is performed.

### **Specify targeting Doppler as** — Source of targeting Doppler `Property` (default) | `Input port`

Specify whether targeting Doppler values for the STAP processor comes from the
**Targeting Doppler (Hz)** parameter of this block or using the
`DOP` input port. For the ADPCA Canceller and
DPCA Canceller blocks, the **Specify targeting Doppler
as** parameter appears only when the **Output pre-Doppler
result** check box is cleared. Values of this parameter are

|  |  |
| --- | --- |
| `Property` | Specify targeting Doppler values using the **Targeting Doppler** parameter of the block. The **Targeting Doppler** parameter appears only when **Specify targeting Doppler as** is set to `Property`. |
| `Input port` | Specify targeting Doppler values using the `Dop` input port. This port appears only when **Specify targeting Doppler as** is set to `Input port`. |

### **Targeting Doppler (Hz)** — Targeting Doppler of STAP processor `0` (default) | scalar

Targeting Doppler of STAP processor, specified as a scalar.

#### Dependencies

- To enable this parameter for the SMI Beamformer block,
  set **Specify targeting Doppler as** to
  `Property`.
- To enable this parameter for the ADPCA Canceller and
  DPCA Canceller blocks, first clear the
  **Output pre-Doppler result** check box. Then set
  the **Specify targeting Doppler as** parameter to
  `Property`.

### **Enable weights output** — Option to output beamformer weights off (default) | on

Select this check box to obtain the beamformer weights from the output port,
`W`.

### **Output pre-Doppler result** — Output results before Doppler filtering on (default) | off

Select this check box to output the results before Doppler filtering.
Clear this check box to output the processing result after Doppler
filtering. Selecting this check box will remove the **Specify
targeting Doppler as** and **Targeting Doppler
(Hz)** parameters.

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

#### Sensor Arrays Tab

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

### **MatchArrayNormal** — Rotate antenna element to array normal `on` (default) | `off`

Select this check box to rotate the antenna element pattern to align with the array normal. When not selected, the element pattern is not rotated.

When the antenna is used in an antenna array and the **Input Pattern Coordinate System** parameter is `az-el`, selecting this check box rotates the pattern so that the *x*-axis of the element coordinate system points along the array normal. Not selecting uses the element pattern without the rotation.

When the antenna is used in an antenna array and **Input Pattern Coordinate System** is set to `phi-theta`, selecting this check box rotates the pattern so that the *z*-axis of the element coordinate system points along the array normal.

Use the parameter in conjunction with the **Array normal** parameter of the `URA` and `UCA` arrays.

#### Dependencies

To enable this parameter, set **Element type** to `Custom Antenna`.

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

### Array Parameters

### **Specify sensor array as** — Type of array `Array (no subarrays)` (default) | `MATLAB expression`

Specify a ULA sensor array directly or by using a MATLAB expression.

**Types**

|  |
| --- |
| `Array (no subarrays)` |
| `MATLAB expression` |

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

### **Expression** — MATLAB expression used to create an array Phased Array System Toolbox array System object

MATLAB expression used to create a ULA array, specified as a valid Phased Array System Toolbox array System object.

**Example:** `phased.ULA('NumElements',13)`

#### Dependencies

To enable this parameter, set **Specify sensor array as** to
`MATLAB expression`.
## Libraries

Phased Array System Toolbox / Space-Time Adaptive Processing

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Displaced phase center array (DPCA) pulse canceller for a uniform linear array

The DPCA Canceller block filters clutter impinging on a uniform linear
array using a displaced phase center array pulse canceller.
