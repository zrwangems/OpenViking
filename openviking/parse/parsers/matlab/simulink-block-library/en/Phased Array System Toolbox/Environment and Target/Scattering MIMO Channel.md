---
type: simulink-block
title: 'Scattering MIMO Channel'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Environment and Target'
documentation_page: 'scatteringmimochannel'
documentation_source_path: 'ref/scatteringmimochannel.html'
language: en
---

# Scattering MIMO Channel

## Ports

### Input

### **X** — Transmitted narrowband signal *M*-by-*Nt* complex-valued matrix

The transmitted narrowband signal, specified as an *M*-by-*Nt* complex-valued
matrix. The quantity *M* is the number of samples
in the signal, and *Nt* is
the number of transmitting array elements. Each column represents
the signal transmitted by the corresponding array element.

**Example:** `[1,1;j,1;0.5,0]`

The size of the first dimension of the input matrix can vary to
simulate a changing signal length. A size change can occur, for example, in the case of a pulse
waveform with variable pulse repetition frequency.

#### Dependencies

To enable this port, set the **Polarization configuration**
parameter to `None` or
`Combined`.

**Data Types:** `double`
**Complex Number Support:** Yes

### **XH** — Transmitted narrowband H-polarization signal *M*-by-*Nt* complex-valued matrix

Transmitted narrowband *H*-polarization signal, specified as an
*M*-by-*Nt* complex-valued
matrix. The quantity *M* is the number of samples in the signal, and
*Nt* is the number of transmitting array
elements. Each column represents the signal transmitted by the corresponding array
element.

The size of the first dimension of the input matrix can vary to
simulate a changing signal length. A size change can occur, for example, in the case of a pulse
waveform with variable pulse repetition frequency.

**Example:** `[1,1;j,1;0.5,0]`

#### Dependencies

To enable this port, set the **Polarization configuration**
parameter to `Dual`.

**Data Types:** `double`
**Complex Number Support:** Yes

### **XV** — Transmitted narrowband V-polarization signal *M*-by-*Nt* complex-valued matrix

Transmitted narrowband *V*-polarization signal, specified as an
*M*-by-*Nt* complex-valued
matrix. The quantity *M* is the number of samples in the signal, and
*Nt* is the number of transmitting array
elements. Each column represents the signal transmitted by the corresponding array
element.

The size of the first dimension of the input matrix can vary to
simulate a changing signal length. A size change can occur, for example, in the case of a pulse
waveform with variable pulse repetition frequency.

#### Dependencies

To enable this port, set the **Polarization configuration**
parameter to `Dual`.

**Data Types:** `double`
**Complex Number Support:** Yes

### **TxPos** — Position of transmitting antenna array 3-by-1 real-valued column vector

Position of transmitting antenna array, specified as a 3-by-1
real-valued column vector taking the form `[x;y;z]`.
The vector elements correspond to the *x*, *y*,
and *z* positions of the array. Units are in meters.

#### Dependencies

To enable this port, set the **Source of transmit array
motion** parameter to `Input port`.

**Data Types:** `double`

### **TxVel** — Velocity of transmitting antenna array 3-by-1 real-valued column vector

Velocity of transmitting antenna array, specified as a 3-by-1
real-valued column vector taking the form `[vx;vy;vz]`.
The vector elements correspond to the *x*, *y*,
and *z* velocities of the array. Units are in meters
per second.

#### Dependencies

To enable this port, set the **Source of transmit array
motion** parameter to `Input port`.

**Data Types:** `double`

### **TxAxes** — Axes orientation of transmitting antenna array 3-by-3 real orthonormal matrix

Axes orientation of transmitting antenna array, specified as
a 3-by-3 real orthonormal matrix. The matrix defines the orientation
of the array local coordinate system with respect to the global coordinates.
Matrix columns correspond to the directions of the *x*, *y*,
and *z* axes of the local coordinate system. Units
are dimensionless.

#### Dependencies

To enable this port, set the **Source of transmit array
motion** parameter to `Input port`.

**Data Types:** `double`

### **RxPos** — Position of receiving antenna array 3-by-1 real-valued column vector

Position of receiving antenna array, specified as a 3-by-1 real-valued
column vector taking the form `[x;y;z]`. The vector
elements correspond to the *x*, *y*,
and *z* positions of the array. Units are in meters.

#### Dependencies

To enable this port, set the **Source of receive array
motion** parameter to `Input port`.

**Data Types:** `double`

### **RxVel** — Velocity of receiving antenna array 3-by-1 real-valued column vector

Velocity of receiving antenna array, specified as a 3-by-1 real-valued
column vector taking the form `[vx;vy;vz]`. The vector
elements correspond to the *x*, *y*,
and *z* velocities of the array. Units are in meters
per second.

#### Dependencies

To enable this port, set the **Source of receive array
motion** parameter to `Input port`.

**Data Types:** `double`

### **RxAxes** — Axes orientation of receiving antenna array 3-by-3 real orthonormal matrix

Axes orientation of receiving antenna array, specified as a
3-by-3 real orthonormal matrix. The matrix defines the orientation
of the array local coordinate system with respect to the global coordinates.
Matrix columns correspond to the directions of the *x*, *y*,
and *z* axes of the local coordinate system. Units
are dimensionless.

#### Dependencies

To enable this port, set the **Source of receive array
motion** parameter to `Input port`.

**Data Types:** `double`

### **ScatPos** — Positions of scatterers 3-by-*Ns* real-valued matrix

Position of scatterers, specified as a 3-by-*Ns* real-valued
matrix. Each column of the matrix takes the form `[x;y;z]`,
containing the *x*, *y*, and *z* positions
of a scatterer. Units are in meters.

#### Dependencies

To enable this port, set the **Scatterer specification** parameter
to `Input port`.

**Data Types:** `double`

### **ScatVel** — Velocities of scatterers 3-by-*Ns* real-valued matrix

Velocities of scatterers, specified as a 3-by-*Ns* real-valued
matrix. Each matrix column has the form `[vx;vy;vz]`,
containing the *x*, *y*, and *z* velocities
of a scatterer. Units are in meters per second.

#### Dependencies

To enable this port, set the **Scatterer specification** parameter
to `Input port`.

**Data Types:** `double`

### **ScatCoef** — Scattering coefficients 1-by-*Ns* complex-valued row vector

Scattering coefficients, specified as a 1-by-*Ns* complex-valued
row vector. Each vector element specifies the scattering coefficient
of the corresponding scatterer. Units are dimensionless.

#### Dependencies

To enable this port, set the **Scatterer specification** parameter
to `Input port`.

**Data Types:** `double`
**Complex Number Support:** Yes
### Output

### **Y** — Received narrowband signal *M*-by-*Nr* complex-valued matrix

Received narrowband signal, returned as an *M*-by-*Nr* complex-valued
matrix. The quantity *M* is the number of samples
in the signal, and *Nr* is
the number of receiving array elements. Each column represents the
signal received by the corresponding array element.

#### Dependencies

To enable this port, set the **Polarization configuration**
parameter to `None` or
`Combined`.

**Data Types:** `double`
**Complex Number Support:** Yes

### **YH** — Received narrowband H-polarization signal complex-valued *M*-by-*Nr* matrix

Received narrowband *H*-polarization signal, returned as a
complex-valued *M*-by-*Nr*
matrix. *M* is the number of samples in the signal, and
*Nr* is the number of receiving array
elements. Each column represents the signal received by the corresponding array
element.

#### Dependencies

To enable this port, set the **Polarization configuration**
parameter to `Dual`.

**Data Types:** `double`
**Complex Number Support:** Yes

### **YV** — Received narrowband V-polarization signal complex-valued *M*-by-*Nr* matrix

Received narrowband *V*-polarization signal, returned as a
complex-valued *M*-by-*Nr*
matrix. *M* is the number of samples in the signal, and
*Nr* is the number of receiving array
elements. Each column represents the signal received by the corresponding array
element.

#### Dependencies

To enable this port, set the **Polarization configuration**
parameter to `Dual`.

**Data Types:** `double`
**Complex Number Support:** Yes

### **CS** — Channel response *Nt*-by-*Nr*-by-*Ns* complex-valued MATLAB® array

Channel response, returned as an *Nt*-by-*Nr*-by-*Ns* complex-valued MATLAB array. *Nt* is
the number of transmitting array elements. *Nr* is
the number of receiving array elements. *Ns* is
the number of scatterers. Each page of the array corresponds to the
channel response matrix for a specific scatterer.

#### Dependencies

To enable this port, select the **Output channel response** check box.

**Data Types:** `double`
**Complex Number Support:** Yes

### **Tau** — Path delays 1-by-*Ns* real-valued vector

Path delays, returned as a 1-by-*Ns* real-valued
vector. *Ns* is the number
of scatterers. Each element corresponds to the path time delay from
the transmitting array phase center to the scatterer and then to the
receiving array phase center.

#### Dependencies

To enable this port, select the **Output channel response** checkbox.

**Data Types:** `double`

## Parameters

#### Main Tab

### **Propagation speed (m/s)** — Signal propagation speed `physconst('LightSpeed')` (default) | positive scalar

Signal propagation speed, specified as a real-valued positive scalar. The default
value of the speed of light is the value returned by
`physconst('LightSpeed')`.

**Data Types:** `double`

### **Signal carrier frequency (Hz)** — Signal carrier frequency `3e8` (default) | positive scalar

Signal carrier frequency, specified as a positive scalar. Units are in Hz.

**Data Types:** `double`

### **Polarization configuration** — Polarization configuration `None` (default) | `Combined` | `Dual`

Polarization configuration, specified as `None`,
`Combined`, or `Dual`. When you set
this parameter to `None`, the output field is considered a
scalar field. When you set this parameter to `None`, the
radiated fields are polarized and are interpreted as a single signal in the sensor's
inherent polarization. When you set this parameter to `Dual`,
the *H* and *V* polarization components of the
radiated field are independent signals.

**Data Types:** `char`

### **Specify atmospheric parameters** — Enable atmospheric attenuation model off (default) | on

Select this parameter to enable to add signal attenuation caused by atmospheric gases,
rain, fog, or clouds. When you select this parameter, the **Temperature (degrees
Celsius)**, **Dry air pressure (Pa)**, **Water
vapour density (g/m^3)**, **Liquid water density
(g/m^3)**, and **Rain rate (mm/hr)** parameters appear in the
dialog box.

**Data Types:** `Boolean`

### **Temperature (degrees Celsius)** — Ambient temperature `15` (default) | real-valued scalar

Ambient temperature, specified as a real-valued scalar. Units are in degrees
Celsius.

#### Dependencies

To enable this parameter, select the **Specify atmospheric
parameters** checkbox.

**Data Types:** `double`

### **Dry air pressure (Pa)** — Atmospheric dry air pressure `101.325e3` (default) | positive real-valued scalar

Atmospheric dry air pressure, specified as a positive real-valued scalar. Units are in
pascals (Pa). The default value of this parameter corresponds to one standard
atmosphere.

#### Dependencies

To enable this parameter, select the **Specify atmospheric
parameters** checkbox.

**Data Types:** `double`

### **Water vapour density (g/m^3)** — Atmospheric water vapor density `7.5` (default) | positive real-valued scalar

Atmospheric water vapor density, specified as a positive real-valued scalar. Units are
in g/m3.

#### Dependencies

To enable this parameter, select the **Specify atmospheric
parameters** checkbox.

**Data Types:** `datetime`

### **Liquid water density (g/m^3)** — Liquid water density `0.0` (default) | nonnegative real-valued scalar

Liquid water density of fog or clouds, specified as a nonnegative real-valued scalar.
Units are in g/m3. Typical values for liquid water density
are 0.05 for medium fog and 0.5 for thick fog.

#### Dependencies

To enable this parameter, select the **Specify atmospheric
parameters** checkbox.

**Data Types:** `double`

### **Rain rate (mm/hr)** — Rainfall rate `0.0` (default) | non-negative real-valued scalar

Rainfall rate, specified as a nonnegative real-valued scalar. Units are in
mm/hr.

#### Dependencies

To enable this parameter, select the **Specify atmospheric
parameters** checkbox.

**Data Types:** `double`

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

### **Simulate direct path propagation** — Enable propagation along direct path off (default) | on

Select this check box to enable signal propagation along the
line-of-sight direct path from the transmitting array to the receiving
array with no scattering.

**Data Types:** `Boolean`

### **Maximum delay (s)** — Maximum signal delay `10e-6` (default) | positive scalar

The maximum signal delay, specified as a positive scalar. Delays
greater than this value are ignored.

**Data Types:** `double`

### **Output channel response** — Enable output of channel response off (default) | on

Select this checkbox to output the channel response and time
delay via the output ports `CS` and `Tau`.

**Data Types:** `Boolean`

### **Simulate using** — Block simulation method `Interpreted Execution` (default) | `Code Generation`

Block simulation, specified as `Interpreted Execution` or
`Code Generation`. If you want your block to use the
MATLAB interpreter, choose `Interpreted Execution`. If
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

#### Transmit and Receive Array Tabs

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

#### Motion Tab

### **Source of transmit array motion** — Specify the source of the transmitting array motion parameters `Property` (default) | `Input port`

Source of transmitting array motion parameters, specified as `Property` or `Input
port`.

- When you select `Property`,
  specify the array location and orientation using the **Position
  of the transmit array (m)** and **Orientation of
  the transmit array** parameters. The array is stationary.
- When you select `Input port`,
  specify the array location, velocity, and orientation using the `TxPos`, `TxVel`,
  and `TxAxes` input ports of the block.

**Data Types:** `char`

### **Position of the transmit array (m)** — Position of transmitting array `[0;0;0]` (default) | real-valued 3-by-1 vector

The position of the transmitting array phase center, specified
as a real-valued, 3-by-1 vector in Cartesian form `[x;y;z]` with
respect to the global coordinate system. Units are in meters.

#### Dependencies

To enable this parameter, set the **Source of transmit
array motion** parameter to `Property`.

**Data Types:** `double`

### **Orientation of the transmit array** — Set the orientation of transmitting array axes `eye(3,3)` (default) | real-valued 3-by-3 orthonormal matrix

The orientation of transmitting array, specified as a real-valued,
3-by-3 orthonormal matrix. The matrix specifies the directions of
the three axes that define the local coordinate system of the array
with respect to the global coordinate system. The columns of the array
correspond to the *x*, *y*, and *z* axes,
respectively.

#### Dependencies

To enable this parameter, set the **Source of transmit
array motion** parameter to `Property`.

**Data Types:** `double`

### **Source of receive array motion** — Specify the source of the receiving array motion parameters `Property` (default) | `Input port`

Source of receiving array motion parameters, specified as `Property` or `Input
port`.

- When you select `Property`,
  specify the array location and orientation using the **Position
  of the receive array (m)** and **Orientation of the
  receive array** parameters. The array is stationary.
- When you select `Input port`,
  specify the array location, velocity, and orientation using the `RxPos`, `RxVel`,
  and `RxAxes` input ports of the block.

**Data Types:** `char`

### **Position of the receive array (m)** — Position of receiving array `[physconst('LightSpeed' )/1e5; 0;0]` (default) | real-valued 3-by-1 vector

The position of the receiving array phase center, specified
as a real-valued, 3-by-1 vector in Cartesian form `[x;y;z]` with
respect to the global coordinate system. Units are in meters.

#### Dependencies

To enable this parameter, set the **Source of receive
array motion** parameter to `Property`.

**Data Types:** `double`

### **Orientation of the receive array** — Set the orientation of receiving array axes `eye(3,3)` (default) | real-valued 3-by-3 orthonormal matrix

The orientation of receiving array, specified as a real-valued,
3-by-3 orthonormal matrix. The matrix specifies the directions of
the three axes that define the local coordinate system of the array
with respect to the global coordinate system. The columns of the array
correspond to the *x*, *y*, and *z* axes,
respectively.

#### Dependencies

To enable this parameter, set the **Source of receive
array motion** parameter to `Property`.

**Data Types:** `double`

### **Scatterer specification** — Specify source of scatterer parameters `Auto` (default) | `Property` | `Input port`

The source of scatterer parameters, specified as `Auto`, `Property`,
or `Input port`.

- When you set this parameter to `Auto`,
  all scatterer positions and coefficients are randomly generated. Scatterer
  velocities are zero. The generated positions are contained within
  the region set by the **Boundary of scatterer positions** parameter.
  Set the number of scatterers using the **Number of scatterers** parameter.
- When you set this property to `Property`,
  set the scatterer positions using the **Positions of scatterers
  (m)** parameter. Set the scattering coefficients using the **Scattering
  coefficients** parameter. Scatterer velocities are zero.
- When you set this parameter to `Input
  port`, you specify the scatterer positions, velocities,
  and scattering coefficients using the `ScatPos`, `ScatVel`,
  and `ScatCoef` block input ports.

**Data Types:** `char`

### **Number of scatterers** — Number of scatterers `1` (default) | nonnegative integer

The number of scatterers, specified as a nonnegative integer.

#### Dependencies

To enable this property, set the **Scatterer specification** parameter
to `Auto`.

**Data Types:** `double`

### **Boundary of scatterer positions** — Constrain scatterer positions within a boundary `[0,1000]` (default) | 1-by-2 real-valued vector | 3-by-2 real-valued matrix

The boundary scatterer positions, specified as a 1-by-2 real-valued
row vector or a 3-by-2 real-valued matrix. If the boundary is a 1-by-2
row vector, the vector contains the minimum and maximum, `[minbdry
maxbdry]`, for all three dimensions. If the boundary is a
3-by-2 matrix, the matrix specifies boundaries in all three dimensions
in the form `[x_minbdry x_maxbdry;y_minbdry y_maxbdry; z_minbdry
z_maxbdry]`.

#### Dependencies

To enable this property, set the **Scatterer specification** parameter
to `Auto`.

**Data Types:** `double`

### **Positions of scatterers (m)** — Positions of scatterers `[physconst('LightSpeed' )*5e-6;0;0]` (default) | real-valued 3-by-*Ns* matrix

The positions of the scatterers, specified as real-valued 3-by-*Ns* matrix. *Ns* is
the number of scatterers. Each column represents a different scatterer
and has the Cartesian form `[x;y;z]` with respect
to the global coordinate system. Units are in meters.

#### Dependencies

To enable this property, set the **Scatterer specification** parameter
to `Property`.

**Data Types:** `double`

### **ScattererCoefficient** — Scattering coefficients `1` (default) | complex-valued 1-by-*Ns* matrix

Scattering coefficients, specified as a complex-valued 1-by-*Ns* vector. *Ns* is
the number of scatterers. Units are dimensionless.

#### Dependencies

To enable this property, set the **Scatterer specification** parameter
to `Property`.

**Data Types:** `double`
**Complex Number Support:** Yes

## Libraries

Phased Array System Toolbox / Environment and Target

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017a**

## Description

Scattering MIMO propagation channel

The Scattering MIMO Channel models a 3-D multipath
propagation channel in which radiated signals from a transmitting
array are reflected from multiple scatters back towards a receiving
array. In this channel, propagation paths are direct paths (line-of-sight)
from point to point. The block models range-dependent time delay,
gain, Doppler shift, phase change, and atmospheric loss due to gases,
rain, fog, and clouds. You can optionally propagate a signal via a
direct path from transmitter to receiver.

The attenuation models for atmospheric gases and rain are valid
for electromagnetic signals in the frequency range 1–1000 GHz
but the attenuation model for fog and clouds is valid for only 10–1000
GHz. Outside these frequency ranges, the object uses the nearest valid
value.
