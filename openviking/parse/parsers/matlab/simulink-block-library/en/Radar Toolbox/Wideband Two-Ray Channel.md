---
type: simulink-block
title: 'Wideband Two-Ray Channel'
family: 'radar'
product_id: 'radar'
product_name: 'Radar Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'widebandtworaychannel'
documentation_source_path: 'ref/widebandtworaychannel.html'
language: en
---

# Wideband Two-Ray Channel

## Ports
```yaml
ports:
- name: X
  summary: Wideband input signal *M*-by-*N* complex-valued matrix | *M*-by-*2N* complex-valued matrix
  direction: input
  data_types: double
- name: Pos1
  summary: Position of signal origin 3-by-1 real-valued column vector | 3-by-*N* real-valued matrix
  direction: input
  data_types: double
- name: Pos2
  summary: Position of signal destination 3-by-1 real-valued column vector | 3-by-*N* real-valued matrix
  direction: input
  data_types: double
- name: Vel1
  summary: Velocity of signal origin 3-by-1 real-valued column vector | 3-by-*N* real-valued matrix
  direction: input
  data_types: double
- name: Vel2
  summary: Velocity of signal destination 3-by-1 real-valued column vector | 3-by-*N* real-valued matrix
  direction: input
  data_types: double
- name: Out
  summary: Propagated signal *M*-by-*N* complex-valued matrix | *M*-by-*2N* complex-valued matrix
  direction: output
```

### Input

### **X** — Wideband input signal *M*-by-*N* complex-valued matrix | *M*-by-*2N* complex-valued matrix

- Wideband nonpolarized scalar signal, specified as an

  - *M*-by-*N*
    complex-valued matrix. The quantity
    *M* is the number of samples in
    the signal and *N* is the number
    of two-ray channels. Each channel corresponds to a
    source-destination pair. Each column contains an
    identical signal that is propagated along the
    line-of-sight and reflected paths.
  - *M*-by-*2N*
    complex-valued matrix. The quantity
    *M* is the number of samples of
    the signal and *N* is the number
    of two-ray channels. Each channel corresponds to a
    source-destination pair. Each adjacent pair of
    columns represents a different channel. Within
    each pair, the first column represents the signal
    propagated along the line-of-sight path and the
    second column represents the signal propagated
    along the reflected path.

The quantity *M* is the number of samples of the
signal and *N* is the number of two-ray channels. Each
channel corresponds to a source-destination pair.

The size of the first dimension of the input matrix can vary to
simulate a changing signal length. A size change can occur, for example, in the case of a pulse
waveform with variable pulse repetition frequency.

**Example:** `[1,1;j,1;0.5,0]`

**Data Types:** `double`
**Complex Number Support:** Yes

### **Pos1** — Position of signal origin 3-by-1 real-valued column vector | 3-by-*N* real-valued matrix

Origin of the signal or signals, specified as a 3-by-1 real-valued
column vector or 3-by-*N* real-valued matrix. The
quantity *N* is the number of two-ray channels. If **Pos1** is
a column vector, it takes the form `[x;y;z]`. If **Pos1** is
a matrix, each column specifies a different signal origin and has
the form `[x;y;z]`. Position units are in meters.

**Pos1** and **Pos2** cannot
both be specified as matrices — at least one must be a 3-by-1
column vector.

**Example:** `[1000;100;500]`

**Data Types:** `double`

### **Pos2** — Position of signal destination 3-by-1 real-valued column vector | 3-by-*N* real-valued matrix

Origin of the signal or signals, specified as a 3-by-1 real-valued
column vector or 3-by-*N* real-valued matrix. The
quantity *N* is the number of two-ray channels. If **Pos2** is
a column vector, it takes the form `[x;y;z]`. If **Pos2** is
a matrix, each column specifies a different signal origin and has
the form `[x;y;z]`. Position units are in meters.

**Pos1** and **Pos2** cannot
both be specified as matrices — at least one must be a 3-by-1
column vector.

**Example:** `[-100;300;50]`

**Data Types:** `double`

### **Vel1** — Velocity of signal origin 3-by-1 real-valued column vector | 3-by-*N* real-valued matrix

Velocity of signal origin, specified as a 3-by-1 real-valued
column vector or 3-by-*N* real-valued matrix. The
dimensions of **Vel1** must match the dimensions
of **Pos1**. If **Vel1** is a column
vector, it takes the form `[Vx;Vy;Vz]`. If **Vel1** is
a 3-by-*N* matrix, each column specifies a different
origin velocity and has the form `[Vx;Vy;Vz]`. Velocity
units are in meters per second.

**Example:** `[-10;3;5]`

**Data Types:** `double`

### **Vel2** — Velocity of signal destination 3-by-1 real-valued column vector | 3-by-*N* real-valued matrix

Velocity of signal origin, specified as a 3-by-1 real-valued
column vector or 3-by-*N* real-valued matrix. The
dimensions of **Vel2** must match the dimensions
of **Pos2**. If **Vel2** is a column
vector, it takes the form `[Vx;Vy;Vz]`. If **Vel2** is
a 3-by-*N* matrix, each column specifies a different
origin velocity and has the form `[Vx;Vy;Vz]`. Velocity
units are in meters per second.

**Example:** `[-1000;300;550]`

**Data Types:** `double`
### Output

### **Out** — Propagated signal *M*-by-*N* complex-valued matrix | *M*-by-*2N* complex-valued matrix

- *M*-by-*N* complex-valued
  matrix. To return this format, set the `CombinedRaysOutput` property
  to `true`. Each matrix column contains the coherently
  combined signals from the line-of-sight path and the reflected path.
- *M*-by-*2N* complex-valued
  matrix. To return this format set the `CombinedRaysOutput` property
  to `false`. Alternate columns of the matrix contain
  the signals from the line-of-sight path and the reflected path.

The output **Out** contains signal samples
arriving at the signal destination within the current input time frame.
Whenever it takes longer than the current time frame for the signal
to propagate from the origin to the destination, the output may not
contain all contributions from the input of the current time frame.
The remaining output will appear in the next execution of the block.
## Parameters
```yaml
parameters:
- name: Signal propagation speed (m/s)
  summary: Signal propagation speed physconst('LightSpeed') (default) | real-valued positive scalar
  group: ''
- name: Signal carrier frequency (Hz)
  summary: Signal carrier frequency 300e6 (default) | positive real-valued scalar
  group: ''
- name: Number of subbands
  summary: Number of processing subbands 64 (default) | positive integer
  group: ''
- name: Specify atmospheric parameters
  summary: Enable atmospheric attenuation model off (default) | on
  group: ''
- name: Temperature (degrees Celsius)
  summary: Ambient temperature 15 (default) | real-valued scalar
  group: ''
- name: Dry air pressure (Pa)
  summary: Atmospheric dry air pressure 101.325e3 (default) | positive real-valued scalar
  group: ''
- name: Water vapour density (g/m^3)
  summary: Atmospheric water vapor density 7.5 (default) | positive real-valued scalar
  group: ''
- name: Liquid water density (g/m^3)
  summary: Liquid water density 0.0 (default) | nonnegative real-valued scalar
  group: ''
- name: Rain rate (mm/hr)
  summary: Rainfall rate 0.0 (default) | non-negative real-valued scalar
  group: ''
- name: Inherit sample rate
  summary: Inherit sample rate from upstream blocks on (default) | off
  group: ''
- name: Sample rate (Hz)
  summary: Sampling rate of signal 1e6 (default) | positive real-valued scalar
  group: ''
- name: Ground reflection coefficient
  summary: Ground reflection coefficient -1 (default) | complex-valued scalar | complex-valued 1-by-*N* row vector
  group: ''
- name: Combine two rays at output
  summary: Option to combine two rays at output on (default) | off
  group: ''
- name: Maximum one-way propagation distance (m)
  summary: Maximum one-way propagation distance 10.0e3 (default) | positive real-valued scalar
  group: ''
- name: Simulate using
  summary: Block simulation method Interpreted Execution (default) | Code Generation
  group: ''
```

### **Signal propagation speed (m/s)** — Signal propagation speed `physconst('LightSpeed')` (default) | real-valued positive scalar

Signal propagation speed, specified as a real-valued positive scalar. The default value of the
speed of light is the value returned by `physconst('LightSpeed')`.
Units are in meters per second.

**Example:** `3e8`

**Data Types:** `double`

### **Signal carrier frequency (Hz)** — Signal carrier frequency `300e6` (default) | positive real-valued scalar

Signal carrier frequency, specified as a positive real-valued
scalar. Units are in hertz.

**Data Types:** `double`

### **Number of subbands** — Number of processing subbands `64` (default) | positive integer

Number of processing subbands, specified as a positive integer.

**Example:** `128`

### **Specify atmospheric parameters** — Enable atmospheric attenuation model off (default) | on

Select this parameter to enable to add signal attenuation caused
by atmospheric gases, rain, fog, or clouds. When you select this parameter,
the **Temperature (degrees Celsius)**, **Dry
air pressure (Pa)**, **Water vapour density (g/m^3)**, **Liquid
water density (g/m^3)**, and **Rain rate (mm/hr)** parameters
appear in the dialog box.

**Data Types:** `Boolean`

### **Temperature (degrees Celsius)** — Ambient temperature `15` (default) | real-valued scalar

Ambient temperature, specified as a real-valued scalar. Units
are in degrees Celsius.

#### Dependencies

To enable this parameter, select the **Specify atmospheric parameters** check
box.

**Data Types:** `double`

### **Dry air pressure (Pa)** — Atmospheric dry air pressure `101.325e3` (default) | positive real-valued scalar

Atmospheric dry air pressure, specified as a positive real-valued
scalar. Units are in pascals (Pa). The default value of this parameter
corresponds to one standard atmosphere.

#### Dependencies

To enable this parameter, select the **Specify atmospheric parameters** check
box.

**Data Types:** `double`

### **Water vapour density (g/m^3)** — Atmospheric water vapor density `7.5` (default) | positive real-valued scalar

Atmospheric water vapor density, specified as a positive real-valued
scalar. Units are in g/m3.

#### Dependencies

To enable this parameter, select the **Specify atmospheric parameters** check
box.

**Data Types:** `double`

### **Liquid water density (g/m^3)** — Liquid water density `0.0` (default) | nonnegative real-valued scalar

Liquid water density of fog or clouds, specified as a nonnegative
real-valued scalar. Units are in g/m3.
Typical values for liquid water density are 0.05 for medium fog and
0.5 for thick fog.

#### Dependencies

To enable this parameter, select the **Specify atmospheric parameters** check
box.

**Data Types:** `double`

### **Rain rate (mm/hr)** — Rainfall rate `0.0` (default) | non-negative real-valued scalar

Rainfall rate, specified as a nonnegative real-valued scalar.
Units are in mm/hr.

#### Dependencies

To enable this parameter, select the **Specify atmospheric parameters** check
box.

**Data Types:** `double`

### **Inherit sample rate** — Inherit sample rate from upstream blocks on (default) | off

Select this parameter to inherit the sample rate from upstream
blocks. Otherwise, specify the sample rate using the **Sample
rate (Hz)** parameter.

**Data Types:** `Boolean`

### **Sample rate (Hz)** — Sampling rate of signal `1e6` (default) | positive real-valued scalar

Specify the signal sampling rate as a positive scalar. Units
are in Hz.

#### Dependencies

To enable this parameter, clear the **Inherit sample rate** check box.

**Data Types:** `double`

### **Ground reflection coefficient** — Ground reflection coefficient -1 (default) | complex-valued scalar | complex-valued 1-by-*N* row vector

Ground reflection coefficient for the field at the reflection point, specified as a
complex-valued scalar or a complex-valued 1-by-*N* row vector.
Coefficients have an absolute value less than or equal to one. The quantity
*N* is the number of two-ray channels. Units are
dimensionless.

**Example:** `-0.5`

### **Combine two rays at output** — Option to combine two rays at output on (default) | off

Select this parameter to combine the two rays at channel output. Combining
the two rays coherently adds the line-of-sight propagated signal and the
reflected path signal to form the output signal. You can use this mode when
you do not need to include the directional gain of an antenna or array in
your simulation.

**Example:** on

### **Maximum one-way propagation distance (m)** — Maximum one-way propagation distance `10.0e3` (default) | positive real-valued scalar

Maximum one-way propagation distance, specified as a real-valued positive scalar.
Units are in meters. Any signal that propagates more than the maximum one-way distance
is ignored. The maximum distance must be greater than or equal to the largest
position-to-position distance.

**Example:** `5000.0`

### **Simulate using** — Block simulation method `Interpreted Execution` (default) | `Code Generation`

Block simulation, specified as `Interpreted Execution` or `Code
Generation`. If you want your block to use the MATLAB® interpreter,
choose `Interpreted Execution`. If you want
your block to run as compiled code, choose `Code Generation`.
Compiled code requires time to compile but usually runs faster.

Interpreted execution is useful when you are developing and tuning a model. The block runs the
underlying System object™ in MATLAB. You can change and execute your model quickly. When you are satisfied
with your results, you can then run the block using `Code
Generation`. Long simulations run faster with generated code than in
interpreted execution. You can run repeated executions without recompiling, but if you
change any block parameters, then the block automatically recompiles before
execution.

This table shows how the **Simulate using** parameter affects the overall
simulation behavior.

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
## Libraries

Radar Toolbox

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

## Description

Wideband two-ray channel environment

The Wideband Two-Ray Channel block propagates
wideband signals from one point in space to multiple points or from
multiple points back to one point via both the direct path and the
ground reflection path. The block propagates wideband signals by (1)
decomposing them into subbands, (2) propagating subbands independently,
and (3) recombining the propagated subbands. The block models propagation
time, propagation loss, and Doppler shift. The block assumes that
the propagation speed is much greater than the object's speed in which
case the stop-and-hop model is valid.
