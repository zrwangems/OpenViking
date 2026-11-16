---
type: simulink-block
title: 'Monopulse Feed'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Direction of Arrival'
documentation_page: 'monopulsefeed'
documentation_source_path: 'ref/monopulsefeed.html'
language: en
---

# Monopulse Feed

## Ports

### Input

### **X** — Input signal complex-valued *M*-by-*N* matrix

Input signal, specified as a complex-valued
*M*-by-*N* matrix, where
*M* is the number of samples or snapshots of data,
and *N* is the number of array elements. If the array
contains subarrays, then *N* is the number of
subarrays.

The size of the first dimension of the input matrix can vary to
simulate a changing signal length. A size change can occur, for example, in the case of a pulse
waveform with variable pulse repetition frequency.

**Data Types:** `double`
**Complex Number Support:** Yes

### **STEER** — Array steering direction scalar | real-valued 2-by-1 column vector

Array steering direction, specified as a scalar or real-valued 2-by-1 column vector.

- When you set the **Monopulse coverage** parameter to `Azimuth`, the steering direction is a scalar and represents the azimuth steering angle.
- When you set the **Monopulse coverage** parameter to
  `3D`, the steering direction vector has the
  form `[azimuthAngle; elevationAngle]`, where
  `azimuthAngle` is the azimuth steering angle, and
  `elevationAngle` is the elevation steering angle.

Units are in degrees. Azimuth angles lie between –180° and 180°, inclusive, and elevation
angles lie between –90° and 90°, inclusive.

**Example:** `[40;10]`

**Data Types:** `double`
### Output

### **SIGMA** — Sum-channel signal complex-valued *M*-by-1 column vector

Sum-channel signal, returned as a complex-valued
*M*-by-1 column vector, where *M* is
the number of rows of `X`.

**Data Types:** `double`
**Complex Number Support:** Yes

### **DeltaAz** — Azimuth-difference channel signal complex-valued *M*-by-1 column vector

Azimuth-difference channel signal, returned as a complex-valued
*M*-by-1 column vector, where *M*
is the number of rows of `X`.

**Data Types:** `double`
**Complex Number Support:** Yes

### **DeltaEl** — Elevation-difference channel signal complex-valued *M*-by-1 vector

Elevation difference-channel signal, returned as a complex-valued
*M*-by-1 column vector, where *M*
is the number of rows of `X`.

#### Dependencies

To enable this output port, set the **Monopulse
coverage** parameter to
`3D`.

**Data Types:** `double`
**Complex Number Support:** Yes

### **ANG** — Estimated direction of target real-valued 2-by-1 vector

Estimated direction of target, returned as a real-valued 2-by-1 vector
in the form `[azimuth,elevation]`. Units are in
degrees.

#### Dependencies

To enable this output port, select the **Output angle
estimate** check box.

**Data Types:** `double`

## Parameters

#### Main Tab

### **Signal propagation speed (m/s)** — Signal propagation speed `physconst('LightSpeed')` (default) | real-valued positive scalar

Signal propagation speed, specified as a real-valued positive scalar. The default
value of the speed of light is the value returned by
`physconst('LightSpeed')`. Units are in meters per second.

**Example:** `3e8`

**Data Types:** `double`

### **Operating frequency (Hz)** — System operating frequency `3e8` (default) | positive real scalar

System operating frequency, specified as a positive scalar. Units are in Hz.

### **Monopulse coverage** — Monopulse coverage directions `3D` (default) | `Azimuth`

Coverage directions of monopulse feed, specified as
`3D` or `Azimuth`.
When you set this parameter to `3D`, the monopulse
feed forms the sum channel and both azimuth and elevation difference
channels. When you set this parameter to `Azimuth`,
the monopulse feed forms the sum channel and the azimuth difference
channel.

### **Squint angle (degrees)** — Squint angle `10` (default) | scalar | real-valued 2-by-1 vector

Squint angle, specified as a scalar or real-valued 2-by-1 vector. The squint angle is
the separation angle between the sum beam and the beams along the azimuth and elevation directions.

- When you set the `Monopulse coverage` parameter to
  `Azimuth`, set the `Squint
  angle` parameter to a scalar.
- When you set the `Monopulse coverage` parameter to
  `3D`, you can specify the squint angle as
  either a scalar or vector. If you set the `Squint angle`
  parameter to a scalar, the squint angle is the same along both the azimuth
  and elevation directions. If you set the `Squint angle`
  parameter to a 2-by-1 vector, its elements specify the squint angle along
  the azimuth and elevation directions.

**Example:** `[20;5]`

### **Output angle estimate** — Enable angle estimate output `off` (default) | `on`

Select this check box to output an estimate of the target direction angle
using the `ANG` output port.

### **Generate Monopulse Tracker** — Create Monopulse estimator block button

Click this button to create a Monopulse Estimate block
based on the parameters in this block.

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

### **Specify sensor array as** — Method to specify array `Array (no subarrays)` (default) | `Partitioned array` | `Replicated subarray` | `MATLAB expression`

Method to specify array, specified as `Array (no subarrays)`
or `MATLAB expression`.

- `Array (no subarrays)` — use the block
  parameters to specify the array.
- `Partitioned array` — use the block
  parameters to specify the array.
- `Replicated subarray` — use the block
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

#### Array Parameters

### **Geometry** — Array geometry `ULA` (default) | `URA` | `UCA` | `Conformal Array`

Array geometry, specified as one of

- `ULA` — Uniform linear array
- `URA` — Uniform rectangular array
- `UCA` — Uniform circular array
- `Conformal Array` — arbitrary element
  positions

### **Number of elements** — Number of array elements `2` for ULA arrays and `5` for UCA arrays (default) | integer greater than or equal to 2

The number of array elements for ULA or UCA arrays, specified as an integer greater
than or equal to 2.

When you set **Specify sensor array as** to `Replicated
subarray`, this parameter applies to each subarray.

#### Dependencies

To enable this parameter, set **Geometry** to
`ULA` or `UCA`.

### **Element spacing (m)** — Spacing between array elements `0.5` for ULA arrays and `[0.5,0.5]` for URA arrays (default) | positive scalar for ULA or URA arrays | 2-element vector of positive values for URA arrays

Spacing between adjacent array elements:

- ULA — specify the spacing between two adjacent elements in the
  array as a positive scalar.
- URA — specify the spacing as a positive scalar or a 1-by-2 vector
  of positive values. If **Element spacing (m)** is a scalar,
  the row and column spacings are equal. If **Element spacing
  (m)** is a vector, the vector has the form
  `[SpacingBetweenArrayRows,SpacingBetweenArrayColumns]`.
- When you set **Specify sensor array as** to
  `Replicated subarray`, this parameter applies to each
  subarray.

#### Dependencies

To enable this parameter, set **Geometry** to
`ULA` or `URA`.

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

### **Array size** — Dimensions of URA array `[2,2]` (default) | positive integer | 1-by-2 vector of positive integers

Dimensions of a URA array, specified as a positive integer or 1-by-2 vector of
positive integers.

- If **Array size** is a 1-by-2 vector, the vector has the
  form `[NumberOfArrayRows,NumberOfArrayColumns]`.
- If **Array size** is an integer, the array has the same
  number of rows and columns.
- When you set **Specify sensor array as** to
  `Replicated subarray`, this parameter applies to each
  subarray.

For a URA, array elements are indexed from top to bottom along the
leftmost column, and then continue to the next columns from left to right. In this
figure, the **Array size** value of `[3,2]` creates an
array having three rows and two columns.

#### Dependencies

To enable this parameter, set **Geometry** to
`URA`.

### **Element lattice** — Lattice of URA element positions `Rectangular` (default) | `Triangular`

Lattice of URA element positions, specified as `Rectangular`
or `Triangular`.

- `Rectangular` — Aligns all the elements in
  row and column directions.
- `Triangular` — Shifts the even-row
  elements of a rectangular lattice toward the positive row-axis direction.
  The displacement is one-half the element spacing along the row
  dimension.

#### Dependencies

To enable this parameter, set **Geometry** to
`URA`.

### **Array normal** — Array normal direction `x` for URA arrays or `z` for UCA arrays (default) | `y`

Array normal direction, specified as
`x`,
`y`, or
`z`.

Elements of planar arrays lie in a plane orthogonal to the
selected array normal direction. Element boresight
directions point along the array normal
direction.

| Array Normal Parameter Value | Element Positions and Boresight Directions |
| --- | --- |
| `x` | Array elements lie in the *yz*-plane. All element boresight vectors point along the *x*-axis. |
| `y` | Array elements lie in the *zx*-plane. All element boresight vectors point along the *y*-axis. |
| `z` | Array elements lie in the *xy*-plane. All element boresight vectors point along the *z*-axis. |

#### Dependencies

To enable this parameter, set
**Geometry** to
`URA` or
`UCA`.

### **Radius of UCA (m)** — UCA array radius 0.5 (default) | positive scalar

Radius of UCA array, specified as a positive scalar.

#### Dependencies

To enable this parameter, set **Geometry** to
`UCA`.

### **Element positions (m)** — Positions of conformal array elements `[0;0;0]` (default) | 3-by-*N*matrix of real values

Positions of the elements in a conformal array, specified as a
3-by-*N* matrix of real values, where *N* is the
number of elements in the conformal array. Each column of this matrix represents the
position `[x;y;z]`of an array element in the array local coordinate
system. The origin of the local coordinate system is *(0,0,0)*. Units
are in meters.

When you set **Specify sensor array as** to `Replicated
subarray`, this parameter applies to each subarray.

#### Dependencies

To enable this parameter set **Geometry** to `Conformal
Array`.

### **Element normals (deg)** — Direction of conformal array element normal vectors `[0;0]` | 2-by-1 column vector | 2-by-*N* matrix

Direction of element normal vectors in a conformal array, specified as a 2-by-1 column
vector or a 2-by-*N* matrix. *N* indicates the number
of elements in the array. For a matrix, each column specifies the normal direction of
the corresponding element in the form `[azimuth;elevation]` with
respect to the local coordinate system. The local coordinate system aligns the positive
*x*-axis with the direction normal to the conformal array. If the
parameter value is a 2-by-1 column vector, the same pointing direction is used for all
array elements.

When you set **Specify sensor array as** to `Replicated
subarray`, this parameter applies to each subarray.

You can use the **Element positions (m)** and **Element
normals (deg)** parameters to represent any arrangement in which pairs of
elements differ by certain transformations. The transformations can combine translation,
azimuth rotation, and elevation rotation. However, you cannot use transformations that
require rotation about the normal direction.

#### Dependencies

To enable this parameter, set **Geometry** to
`Conformal Array`.

### **Taper** — Array element tapers 1 (default) | complex-valued scalar | complex-valued row vector

Element tapering, specified as a complex-valued scalar or a
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

When you set **Specify sensor array as** to
`Replicated subarray`, this
parameter applies to each subarray.

### **Subarray definition matrix** — Define elements belonging to subarrays logical matrix

Specify the subarray selection as an *M*-by-*N*
matrix. *M* is the number of subarrays and *N* is the
total number of elements in the array. Each row of the matrix represents a subarray and
each entry in the row indicates when an element belongs to the subarray. When the entry
is zero, the element does not belong the subarray. A nonzero entry represents a
complex-valued weight applied to the corresponding element. Each row must contain at
least one nonzero entry.

The phase center of each subarray lies at the subarray geometric center. The subarray
geometric center depends on the **Subarray definition matrix** and
**Geometry** parameters.

#### Dependencies

To enable this parameter, set **Specify sensor array as** to
`Partitioned array`.

### **Subarray steering method** — Specify subarray steering method `None` (default) | `Phase` | `Time`

Subarray steering method, specified as one of

- `None`
- `Phase`
- `Time`
- `Custom`

Selecting `Phase` or `Time` opens the
`Steer` input port on the Narrowband Receive Array,
Narrowband Transmit Array, Wideband Receive Array,
Wideband Transmit Array blocks, Constant Gamma
Clutter, and GPU Constant Gamma Clutter blocks.

Selecting `Custom` opens the `WS` input port on the
Narrowband Receive Array, Narrowband Transmit Array,
Wideband Receive Array, Wideband Transmit Array
blocks, Constant Gamma Clutter, and GPU Constant Gamma
Clutter blocks.

#### Dependencies

To enable this parameter, set **Specify sensor array as** to
`Partitioned array` or `Replicated
subarray`.

### **Phase shifter frequency (Hz)** — Subarray phase shifting frequency `3.0e8` (default) | positive real-valued scalar

Operating frequency of subarray steering phase shifters, specified as a positive
real-valued scalar. Units are Hz.

#### Dependencies

To enable this parameter, set **Sensor array** to
`Partitioned array` or `Replicated subarray`
and set **Subarray steering method** to
`Phase`.

### **Number of bits in phase shifters** — Subarray steering phase shift quantization bits `0` (default) | non-negative integer

Subarray steering phase shift quantization bits, specified as a non-negative integer.
A value of zero indicates that no quantization is performed.

#### Dependencies

To enable this parameter, set **Sensor array** to
`Partitioned array` or `Replicated subarray`
and set **Subarray steering method** to
`Phase`.

### **Subarrays layout** — Subarray position specification `Rectangular` (default) | `Custom`

Specify the layout of replicated subarrays as `Rectangular` or
`Custom`.

- When you set this parameter to `Rectangular`, use the
  **Grid size** and **Grid spacing**
  parameters to place the subarrays.
- When you set this parameter to `Custom`, use the
  **Subarray positions (m)** and **Subarray
  normals** parameters to place the subarrays.

#### Dependencies

To enable this parameter, set **Sensor array** to
`Replicated subarray`

### **Grid size** — Dimensions of rectangular subarray grid `[1,2]` (default)

Rectangular subarray grid size, specified as a single positive
integer, or a 1-by-2 row vector of positive integers.

If **Grid size** is an integer scalar, the array has
an equal number of subarrays in each row and column. If
**Grid size** is a 1-by-2 vector of
the form `[NumberOfRows, NumberOfColumns]`, the
first entry is the number of subarrays along each column. The
second entry is the number of subarrays in each row. A row is
along the local *y*-axis, and a column is along
the local *z*-axis. The figure here shows how
you can replicate a 3-by-2 URA subarray using a **Grid
size** of `[1,2]`.

#### Dependencies

To enable this parameter, set **Sensor
array** to `Replicated
subarray` and **Subarrays
layout** to
`Rectangular`.

### **Grid spacing (m)** — Spacing between subarrays on rectangular grid `Auto` (default) | positive real-valued scalar | 1-by-2 vector of positive real-values

The rectangular grid spacing of subarrays, specified as a positive, real-valued
scalar, a 1-by-2 row vector of positive, real-values, or `Auto`. Units
are in meters.

- If **Grid spacing** is a scalar, the spacing along the row
  and the spacing along the column is the same.
- If **Grid spacing** is a 1-by-2 row vector, the vector has
  the form `[SpacingBetweenRows,SpacingBetweenColumn]`. The first
  entry specifies the spacing between rows along a column. The second entry
  specifies the spacing between columns along a row.
- If **Grid spacing** is set to `Auto`,
  replication preserves the element spacing of the subarray for both rows and
  columns while building the full array. This option is available only when you
  specify **Geometry** as `ULA` or
  `URA`.

#### Dependencies

To enable this parameter, set **Sensor array** to
`Replicated subarray` and **Subarrays layout**
to `Rectangular`.

### **Subarray positions (m)** — Positions of subarrays `[0,0;0.5,0.5;0,0]` (default) | 3-by-*N* real-valued matrix

Positions of the subarrays in the custom grid, specified as a real
3-by-*N* matrix, where *N* is the number of
subarrays in the array. Each column of the matrix represents the position of a single
subarray in the array local coordinate system. The coordinates are expressed in the form
`[x; y; z]`. Units are in meters.

#### Dependencies

To enable this parameter, set **Sensor array** to
`Replicated subarray` and **Subarrays layout**
to `Custom`.

### **Subarray normals** — Direction of subarray normal vectors `[0,0;0,0]` (default) | 2-by-*N* real matrix

Specify the normal directions of the subarrays in the array. This parameter value is a
2-by-*N* matrix, where *N* is the number of
subarrays in the array. Each column of the matrix specifies the normal direction of the
corresponding subarray, in the form `[azimuth;elevation]`. Angle units
are in degrees. Angles are defined with respect to the local coordinate system.

You can use the **Subarray positions** and **Subarray
normals** parameters to represent any arrangement in which pairs of
subarrays differ by certain transformations. The transformations can combine
translation, azimuth rotation, and elevation rotation. However, you cannot use
transformations that require rotation about the normal.

#### Dependencies

To enable this parameter, set the **Sensor array** parameter to
`Replicated subarray` and the **Subarrays
layout** to `Custom`.

## Libraries

Phased Array System Toolbox / Direction of Arrival

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Create monopulse sum and difference channels

The Monopulse Feed block forms the sum and difference channels used for
amplitude monopulse directing finding. Sum and difference channels are derived from
signals received by an array. You can feed these channels into the Monopulse
Estimator block.
