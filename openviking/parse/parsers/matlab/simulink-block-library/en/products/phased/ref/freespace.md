---
type: simulink-block
title: 'Free Space'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Waveform Design and Signal Synthesis / Signal Propagation and Targets'
documentation_page: 'freespace'
documentation_source_path: 'ref/freespace.html'
language: en
---

# Free Space

## Ports

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
the dimension specified in the signal into the port
`X`. If `Pos1` is a column
vector, it takes the form `[x; y; z]`. If
`Pos1` is a matrix, each column specifies a
different signal origin and has the form `[x; y; z]`.
`Pos1` and `Pos2` cannot both
be specified as matrices — at least one must be a 3-by-1 column
vector. Position units are meters.

**Data Types:** `double`

### **Pos2** — Signal destination 3-by-1 real-valued column vector | 3-by-*N* real-valued matrix

Signal destination, specified as a 3-by-1 real-valued column vector or
3-by-*N* real-valued matrix. The quantity
*N* is the number of propagated signals and equals
the dimension specified in the signal into the port
`X`. If `Pos2` is a column
vector, it takes the form `[x; y; z]`. If
`Pos2` is a matrix, each column specifies a
different signal origin and has the form `[x; y; z]`.
`Pos2` and `Pos1` cannot both
be specified as matrices — at least one must be a 3-by-1 column
vector. Position units are meters.

**Data Types:** `double`

### **Vel1** — Signal origin velocity 3-by-1 real-valued column vector | 3-by-*N* real-valued matrix

Signal origin velocity, specified as a 3-by-1 real-valued column
vector or 3-by-*N* real-valued matrix. The quantity
*N* is the number of propagated signals and equals
the dimension specified in the signal into the port
`X`. If `Vel1` is a column
vector, it takes the form `[Vx; Vy; zV]`. If
`Vel1` is a matrix, each column specifies a
different signal origin and has the form `[Vx; Vy;
Vz]`. `Vel1` and `Vel2`
cannot both be specified as matrices — at least one must be a
3-by-1 column vector. Position units are meters.

**Data Types:** `double`

### **Vel2** — Signal destination velocity 3-by-1 real-valued column vector | 3-by-*N* real-valued matrix

Signal destination velocity, specified as a 3-by-1 real-valued column
vector or 3-by-*N* real-valued matrix. The quantity
*N* is the number of propagated signals and equals
the dimension specified in the signal into the port
`X`. If `Vel2` is a column
vector, it takes the form `[Vx; Vy; zV]`. If
`Vel2` is a matrix, each column specifies a
different signal origin and has the form `[Vx; Vy;
Vz]`. `Vel2` and `Vel1`
cannot both be specified as matrices — at least one must be a
3-by-1 column vector. Position units are meters.

**Data Types:** `double`
### Output

### **Port\_1** — Propagated narrowband signal *M*-element complex-valued column vector, *M*-by-*N* complex-valued matrix.

Propagated signal, returned as a *M*-element
complex-valued column vector,
*M*-by-*N* complex-valued
matrix.

If `X` is a column vector or matrix,
`Y` is also a column vector or matrix with the
same dimensions.

The output `Y` contains signal samples arriving at
the signal destination within the current time frame. The current time
frame is defined as the time spanned by the current input. Whenever it
takes longer than the current time frame for the signal to propagate
from the origin to the destination, the output contains no contribution
from the input of the current time frame.

## Parameters

### **Propagation speed (m/s)** — Signal propagation speed `physconst('LightSpeed')` (default) | positive scalar

Signal propagation speed, specified as a real-valued positive scalar. The default
value of the speed of light is the value returned by
`physconst('LightSpeed')`.

**Data Types:** `double`

### **Signal carrier frequency (Hz)** — Signal carrier frequency `3e8` (default) | positive scalar

Signal carrier frequency, specified as a positive scalar. Units are in Hz.

**Data Types:** `double`

### **Perform two-way propagation** — Perform two-way propagation off (default) | on

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

### **Maximum one-way propagation distance (m)** — Maximum one-way propagation distance `10e3` (default)

The maximum distance, in meters, between the origin and the destination as
a positive scalar. Amplitudes of any signals that propagate beyond this
distance will be set to zero.

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

**Introduced in R2014b**

## Description

Free space environment

The Free Space Channel block propagates a signal from one point to another in
space. The block models propagation time, free space propagation loss and Doppler shift.
The block assumes that the propagation speed is much greater than the target or array
speed in which case the stop-and-hop model is valid.

When propagating a signal in free-space to an object and back, you have the choice of either using a single block to compute a two-way free space propagation delay or two blocks to perform one-way propagation delays in each direction. Because the free-space propagation delay is not necessarily an integer multiple of the sampling interval, it may turn out that the total round trip delay in samples when you use a two-way propagation block differs from the delay in samples when you use two one-way propagation blocks. For this reason, it is recommended that, when possible, you use a single two-way propagation block.
