---
type: simulink-block
title: 'Beamscan Spectrum'
family: 'radar'
product_id: 'radar'
product_name: 'Radar Toolbox'
documentation_release: R2025b
official_category: 'Signal and Data Processing / Detection, Range, Angle, and Doppler Estimation'
documentation_page: 'beamscanspectrum'
documentation_source_path: '../phased/ref/beamscanspectrum.html'
language: en
---

# Beamscan Spectrum

## Ports

### Input

### **X** — Received signal *M*-by-*N* complex-valued matrix

Received signal, specified as an *M*-by-*N*
complex-valued matrix. The quantity *M* is the length of the signal,
the number of sample values contained in the signal. The quantity *N*
is the number of sensor elements in the array.

The size of the first dimension of the input matrix can vary to
simulate a changing signal length. A size change can occur, for example, in the case of a pulse
waveform with variable pulse repetition frequency.

**Data Types:** `double`
### Output

### **Y** — Beamscan 2-D spatial spectrum non-negative real-valued *P*-by-*Q* matrix

2Magnitude of the estimated 2-D spatial spectrum, returned as a non-negative,
returned as a real-valued *P*-by-*Q* matrix. Each
entry represents the magnitude of the estimated MUSIC spatial spectrum. Each entry
corresponds to an angle specified by the **Azimuth scan angles
(deg)** and **Elevation scan angles (deg)** parameters.
*P* equals the length of the vector specified in **Azimuth
scan angles (deg)** and *Q* equals the length of the
vector specified in **Elevation scan angles (deg)**.

**Data Types:** `double`

### **Ang** — Directions of arrival non-negative, real-valued 2-by-*L* matrix

Directions of arrival of the signals, returned as a real-valued
2-by-*L* matrix. *L* is the number of signals
specified by the **Number of signals** parameter. The direction of
arrival angle is defined by the azimuth and elevation angles of the source with
respect to the array local coordinate system. The first row of the matrix contains the
azimuth angles and the second row contains the elevation angles. If the object cannot
identify peaks in the spectrum, it will return `NaN`. Angle units are
in degrees.

#### Dependencies

To enable this output port, select the **Enable DOA output**
check box.

**Data Types:** `double`

## Parameters

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

### **Azimuth scan angles (deg)** — Scan angles in azimuth direction `-180:180` (default) | real-valued vector

Scan angles in azimuthal direction, specified as a real-valued vector. The angles
must lie be between –180° and 180°, inclusive. You must specify the angles in ascending
order. Units are in degrees.

**Data Types:** `double`

### **Elevation scan angles (deg)** — Scan angles in elevation direction `-90:90` (default) | real-valued vector

Scan angles in elevation direction, specified as a real-valued vector. The angles
must lie be between –90° and 90°, inclusive. You must specify the angles in ascending
order. Units are in degrees.

**Data Types:** `double`

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
  number of elements in each row and column.

For a URA, array elements are indexed from top to bottom along the
leftmost array column, and continued to the next columns from left to right. In this
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

#### Dependencies

To enable this parameter set **Geometry** to `Conformal
Array`.

**Data Types:** `double`

### **Element normals (deg)** — Direction of conformal array element normal vectors `[0;0]` | 2-by-1 column vector | 2-by-*N* matrix

Direction of element normal vectors in a conformal array, specified as a 2-by-1 column
vector or a 2-by-*N* matrix. *N* indicates the number
of elements in the array. If the parameter value is a matrix, each column specifies the
normal direction of the corresponding element in the form
`[azimuth;elevation]` with respect to the local coordinate system.
The local coordinate system aligns the positive *x*-axis with the
direction normal to the conformal array. If the parameter value is a 2-by-1 column
vector, the same pointing direction is used for all array elements.

You can use the **Element positions (m)** and **Element
normals (deg)** parameters to represent any arrangement in which pairs of
elements differ by certain transformations. The transformations can combine translation,
azimuth rotation, and elevation rotation. However, you cannot use transformations that
require rotation about the normal direction.

To enable this parameter, set **Geometry** to `Conformal
Array`.

**Data Types:** `double`

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

Beamscan spatial spectrum estimator

The Beamscan Spectrum block estimates the 2-D spatial spectrum of incoming
narrowband signals by scanning a range of azimuth and elevation angles using a narrowband
conventional beamformer. The block optionally calculates the direction of arrival of a
specified number of signals by locating peaks of the spectrum.
