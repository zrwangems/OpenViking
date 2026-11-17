---
type: simulink-block
title: 'LOS Channel'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Environment and Target'
documentation_page: 'loschannel'
documentation_source_path: 'ref/loschannel.html'
language: en
---

# LOS Channel

## Ports
```yaml
ports:
- name: X
  summary: Narrowband signal *M*-element complex-valued column vector, *M*-by-*N* complex-valued matrix.
  direction: input
- name: Pos1
  summary: Signal origin 3-by-1 real-valued column vector | 3-by-*N* real-valued matrix
  direction: input
  data_types: double
- name: Pos2
  summary: Signal destination 3-by-1 real-valued column vector | 3-by-*N* real-valued matrix
  direction: input
  data_types: double
- name: Vel1
  summary: Signal origin velocity 3-by-1 real-valued column vector | 3-by-*N* real-valued matrix
  direction: input
  data_types: double
- name: Vel2
  summary: Signal destination velocity 3-by-1 real-valued column vector | 3-by-*N* real-valued matrix
  direction: input
  data_types: double
- name: Port_1
  summary: Propagated narrowband signal *M*-element complex-valued column vector, *M*-by-*N* complex-valued matrix.
  direction: output
```

### Input

### **X** — Narrowband signal *M*-element complex-valued column vector, *M*-by-*N* complex-valued matrix.

Narrowband signal, specified as an *M*-element
complex-valued column vector or
*M*-by-*N* complex-valued matrix.
The quantity *M* is the number of sample values of the
signal and *N* is the number of signals to propagate.
When you specify *N* signals, you need to specify
*N* signal origins or *N* signal
destinations.

The size of the first dimension of the input matrix can vary to
simulate a changing signal length. A size change can occur, for example, in the case of a pulse
waveform with variable pulse repetition frequency.

### **Pos1** — Signal origin 3-by-1 real-valued column vector | 3-by-*N* real-valued matrix

Signal origin, specified as a 3-by-1 real-valued column vector or
3-by-*N* real-valued matrix. The quantity
*N* is the number of propagated signals and equals
the dimension specified in the signal input port `X`.
If `Pos1` is a column vector, it takes the form
`[x; y; z]`. If `Pos1` is a
matrix, each column specifies a different signal origin and has the form
`[x; y; z]`. `Pos1` and
`Pos2` cannot both be specified as matrices
— at least one must be a 3-by-1 column vector. Position units are
meters.

**Data Types:** `double`

### **Pos2** — Signal destination 3-by-1 real-valued column vector | 3-by-*N* real-valued matrix

Signal destination, specified as a 3-by-1 real-valued column vector or
3-by-*N* real-valued matrix. The quantity
*N* is the number of propagated signals and equals
the dimension specified in the signal in the input port
`X`. If `Pos2` is a column
vector, it takes the form `[x; y; z]`. If
`Pos2` is a matrix, each column specifies a
different signal origin and has the form `[x; y; z]`.
`Pos2` and `Pos1` cannot both
be specified as matrices — at least one must be a 3-by-1 column
vector. Position units are meters.

**Data Types:** `double`

### **Vel1** — Signal origin velocity 3-by-1 real-valued column vector | 3-by-*N* real-valued matrix

Signal origin velocity, specified as a 3-by-1 real-valued column vector or
3-by-*N* real-valued matrix. The quantity
*N* is the number of propagated signals and equals
the dimension specified in the signal into the port
`X`. If `Vel1` is a column
vector, it takes the form `[Vx; Vy; zV]`. If
`Vel1` is a matrix, each column specifies a
different signal origin and has the form `[Vx; Vy;
Vz]`. The dimensions of `Vel1` must agree
with the dimensions of `Pos1`.
`Vel1` and `Vel2` cannot both
be specified as matrices — at least one must be a 3-by-1 column
vector. Position units are meters.

**Data Types:** `double`

### **Vel2** — Signal destination velocity 3-by-1 real-valued column vector | 3-by-*N* real-valued matrix

Signal destination velocity, specified as a 3-by-1 real-valued column vector or
3-by-*N* real-valued matrix. The quantity
*N* is the number of propagated signals and equals
the dimension specified in the signal into the port
`X`. If `Vel2` is a column
vector, it takes the form `[Vx; Vy; zV]`. If
`Vel2` is a matrix, each column specifies a
different signal origin and has the form `[Vx; Vy;
Vz]`. The dimensions of `Vel2` must agree
with the dimensions of `Pos2`.
`Vel2` and `Vel1` cannot both
be specified as matrices — at least one must be a 3-by-1 column
vector. Position units are meters.

**Data Types:** `double`
### Output

### **Port\_1** — Propagated narrowband signal *M*-element complex-valued column vector, *M*-by-*N* complex-valued matrix.

Propagated signal, returned as a *M*-element complex-valued column
vector, *M*-by-*N* complex-valued
matrix. `Y` will have the same dimensions as
`X`.

The output `Y` contains signal samples arriving at
the signal destination within the current time frame. The current time
frame is defined as the time spanned by the current input. Whenever it
takes longer than the current time frame for the signal to propagate
from the origin to the destination, the output contains no contribution
from the input of the current time frame.
## Parameters
```yaml
parameters:
- name: Propagation speed (m/s)
  summary: Signal propagation speed physconst('LightSpeed') (default) | positive scalar
  group: ''
- name: Signal carrier frequency (Hz)
  summary: Signal carrier frequency 3e8 (default) | positive scalar
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
- name: Perform two-way propagation
  summary: Enable two-way propagation off (default) | on
  group: ''
- name: Inherit sample rate
  summary: Inherit sample rate from upstream blocks on (default) | off
  group: ''
- name: Sample rate (Hz)
  summary: Sampling rate of signal 1e6 (default) | positive real-valued scalar
  group: ''
- name: Maximum one-way propagation distance (m)
  summary: Maximum one-way propagation distance 10e3 (default) | positive real-valued scalar
  group: ''
- name: Simulate using
  summary: Block simulation method Interpreted Execution (default) | Code Generation
  group: ''
  block_parameter: SimulateUsing
  type: enum
  values: Interpreted Execution, Code Generation
  default: Interpreted Execution
```

### **Propagation speed (m/s)** — Signal propagation speed `physconst('LightSpeed')` (default) | positive scalar

Signal propagation speed, specified as a real-valued positive scalar. The default
value of the speed of light is the value returned by
`physconst('LightSpeed')`.

**Data Types:** `double`

### **Signal carrier frequency (Hz)** — Signal carrier frequency `3e8` (default) | positive scalar

Signal carrier frequency, specified as a positive scalar. Units are in Hz.

**Data Types:** `double`

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

### **Perform two-way propagation** — Enable two-way propagation `off` (default) | `on`

Select this check box to perform round-trip propagation between the origin and destination. Otherwise the block performs one-way propagation from the origin to the destination.

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

### **Maximum one-way propagation distance (m)** — Maximum one-way propagation distance `10e3` (default) | positive real-valued scalar

Specify the maximum distance between the signal origin and the destination as a positive scalar. Units are in meters. Amplitudes of any signals that propagate beyond this distance will be set to zero.

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

**Introduced in R2016a**

## Description

Narrowband line-of-sight propagation channel

The LOS Channel block propagates signals from a point in space to another
point in space by line-of-sight (LOS) channels. The block can also propagate signals
from one point to multiple points or from multiple points back to one point. The block
models propagation time, free-space propagation loss, Doppler shift, and atmospheric as
well as weather loss. The block assumes that the propagation speed is much greater than
the object speed in which case the stop-and-hop model is valid.

When propagating a signal in an LOS channel to an object and back, you can use a single
block to compute two-way LOS channel propagation delays or two blocks to perform two
one-way propagation delays in each direction. Because the LOS channel propagation delay
is not necessarily an integer multiple of the sampling interval, it can turn out that
the total round trip delay in samples when you use a two-way propagation block differs
from the delay in samples when you use two one-way propagation blocks. For this reason,
it is recommended that, when possible, you use a single two-way propagation
block.
