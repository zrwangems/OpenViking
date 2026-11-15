---
type: simulink-block
title: 'Wideband LOS Channel'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Waveform Design and Signal Synthesis / Signal Propagation and Targets'
documentation_page: 'widebandloschannelblock'
documentation_source_path: 'ref/widebandloschannelblock.html'
language: en
---

# Wideband LOS Channel

## Ports

### Input

### **X** — Radiated signal complex-valued *M*-by-1 vector | complex-valued *M*-by-*N* matrix

Radiated signal, specified as a complex-valued
*M*-by-1 vector or complex-valued
*M*-by-*N* matrix.
*M* is the length of the signal and
*N* is the number of array elements (or subarrays
when subarrays are supported).

**Dimensions of X**

| Dimension | Signal |
| --- | --- |
| *M*-by-1 vector | The same signal is radiated from all array elements (or all subarrays when subarrays are supported). |
| `M-by-N matrix` | Each column corresponds to the signal radiated by the corresponding array element (or corresponding subarrays when subarrays are supported). |

The size of the first dimension of the input matrix can vary to
simulate a changing signal length. A size change can occur, for example, in the case of a pulse
waveform with variable pulse repetition frequency.

**Data Types:** `double`
**Complex Number Support:** Yes

### **Pos1** — Position of signal origin 3-by-1 real-valued column vector | 3-by-*N* real-valued matrix

Position of signal origin, specified as a real-valued 3-by-1 column vector or a
3-by-*N* real-valued matrix. The quantity
*N* is the number of source positions. Examples of
source positions include transmitters, array element positions or
subarray positions. Position units are in meters.

If **Pos1** is a column vector, it takes the form
`[x;y;z]`. If **Pos1** is a matrix, each column specifies a different signal
origin and has the form `[x;y;z]`.

If **Pos1** has more than one column, **Pos2** can have only one column. You cannot specify both **Pos1** and **Pos2** as matrices.

**Example:** `[1000;100;500]`

**Data Types:** `double`

### **Pos2** — Signal destination 3-by-1 real-valued column vector | 3-by-*N* real-valued matrix

Position of signal destination, specified as a real-valued 3-by-1 column vector or a
3-by-*N* real-valued matrix. The quantity
*N* is the number of destinations such as array
element positions or subarray positions. Position units are in
meters.

If **Pos2** is a column vector, it takes the form
`[x;y;z]`. If **Pos2** is a matrix, each column specifies a different signal
destination. Each row takes the form `[x;y;z]`.
Position units are in meters.

If **Pos2** has more than one column, **Pos1** can have only one column. You cannot specify both **Pos2** and **Pos1** as matrices.

**Example:** `[1000;100;500]`

**Data Types:** `double`

### **Vel1** — Source velocity 3-by-1 real-valued column vector | 3-by-*N* real-valued matrix | *N*-by-3 real-valued matrix

Source velocity, specified as a real-valued vector or matrix having
the same size as **Pos1**.

**Example:** `[20;20;50]`

**Data Types:** `double`

### **Vel2** — Destination velocity 3-by-1 real-valued column vector | 3-by-*N* real-valued matrix | *N*-by-3 real-valued matrix

Destination velocity, specified as a real-valued vector or matrix
having the same size as **Pos2**.

**Example:** `[0;0;100]`

**Data Types:** `double`
### Output

### **Port\_1** — Propagated signal complex-valued *M*-by-1 vector | complex-valued *M*-by-*N* matrix

Propagated signal, returned as a complex-valued *M*-by-1 vector or
complex-valued *M*-by-*N* matrix.
**Port\_1** has the same size as the input port **X**. *M* is the length of the signal and
*N* is the number of signals.

**Data Types:** `double`

## Parameters

### **Propagation speed (m/s)** — Signal propagation speed `physconst('LightSpeed')` (default) | positive scalar

Signal propagation speed, specified as a real-valued positive scalar. The default
value of the speed of light is the value returned by
`physconst('LightSpeed')`.

**Data Types:** `double`

### **Signal carrier frequency (Hz)** — Signal carrier frequency `3e8` (default) | positive scalar

Signal carrier frequency, specified as a positive scalar. Units are in Hz.

**Data Types:** `double`

### **Number of subbands** — Number of processing subbands `64` (default) | positive integer

Number of processing subbands, specified as a positive integer.

**Example:** `128`

### **Specify atmospheric parameters** — Enable atmospheric attenuation model off (default) | on

Select this check box to enable atmospheric attenuation modeling.

### **Temperature (degrees Celsius)** — Ambient temperature `15` | real-valued scalar

Specify the ambient atmospheric temperature as a real-valued scalar. Units
are degrees Celsius.

#### Dependencies

This parameter appears when you select the **Specify
atmospheric parameters** check box.

### **Dry air pressure (Pa)** — Atmospheric dry air pressure `101325` | positive real-valued scalar

Specify the atmospheric dry air pressure as a positive real-valued scalar.
Units are Pascals (Pa). The value 101325 for this property corresponds to
one standard atmosphere.

#### Dependencies

This parameter appears when you select the **Specify
atmospheric parameters** check box.

### **Water vapour density (g/m^3)** — Atmospheric water vapor density `7.5` | positive real-valued scalar

Specify the atmospheric water vapor density as a positive real-valued
scalar. Units are gm/m3.

#### Dependencies

This parameter appears when you select the **Specify
atmospheric parameters** check box.

### **Liquid water density (g/m^3)** — Liquid water density `0` | non-negative real-valued scalar

Specify the liquid water density of fog or clouds as a non-negative
real-valued scalar. Units are gm/m3. Typical
values for liquid water density are 0.05 for medium fog and 0.5 for thick
fog.

#### Dependencies

This parameter appears when you select the **Specify
atmospheric parameters** check box.

### **Rain rate (mm/hr)** — Rainfall rate `0` | non-negative real-valued scalar

Specify the rainfall rate as a non-negative real-valued scalar. Units are
in mm/hour.

#### Dependencies

This parameter appears when you select the **Specify
atmospheric parameters** check box.

### **Perform two-way propagation** — Enable two-way propagation off (default) | on

Select this check box to perform round-trip propagation between the origin
and destination. Otherwise the block performs one-way propagation from the
origin to the destination.

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

Wideband line-of-sight propagation channel

The Wideband LOS Channel block propagates signals from one point in space to multiple points or from multiple points back to one point via line-of-sight (LOS) channels. The block models propagation time, free-space propagation loss, Doppler shift, and atmospheric as well as weather loss. The block assumes that the propagation speed is much greater than the object's speed in which case the stop-and-hop model is valid.

When propagating a signal in an LOS channel to an object and back, you can use a single
block to compute a two-way LOS channel propagation delay or two blocks to a perform
one-way propagation delays in each direction. Because the LOS channel propagation delay
is not necessarily an integer multiple of the sampling interval, it may turn out that
the total round trip delay in samples when you use a two-way propagation block differs
from the delay in samples when you use two one-way propagation blocks. For this reason,
it is recommended that, when possible, you use a single two-way propagation
block.
