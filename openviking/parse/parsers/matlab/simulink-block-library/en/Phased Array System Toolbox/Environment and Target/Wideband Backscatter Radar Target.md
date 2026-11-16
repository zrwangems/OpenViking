---
type: simulink-block
title: 'Wideband Backscatter Radar Target'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Environment and Target'
documentation_page: 'widebandbackscatterradartarget'
documentation_source_path: 'ref/widebandbackscatterradartarget.html'
language: en
---

# Wideband Backscatter Radar Target

## Ports

### Input

### **X** — Wideband incident nonpolarized signal *N*-by-*1* complex-valued vector | *N*-by-*M* complex-valued matrix

Wideband incident nonpolarized signal, specified as an
*N*-by-*1* complex-valued vector
or an *N*-by-*M* complex-valued
matrix. The quantity *N* is the number of signal
samples, and *M* is the number of independent signals
reflecting off the target. Each column contains an independent signal to
be reflected from the target.

The size of the first dimension of the input matrix can vary to
simulate a changing signal length. A size change can occur, for example, in the case of a pulse
waveform with variable pulse repetition frequency.

**Data Types:** `double`
**Complex Number Support:** Yes

### **Ang** — Incident signal direction 2-by-1 real-valued column vector | 2-by-*M* real-valued column matrix

Incident signal direction, specified as a 2-by-1 real-valued column
vector or a 2-by-*M* real-valued column matrix.
*M* is the number of signals reflecting from the
target. Each column of `Ang` specifies the incident
direction of the corresponding signal in the form of an
`[AzimuthAngle;ElevationAngle]` pair. Units are
degrees. The number of columns in `Ang` must match
the number of independent signals in `X`.

**Example:** `[30;45]`

**Data Types:** `double`

### **Update** — Switch to update RCS `false` | `true`

Switch to update RCS fluctuation model values, specified as
`false` or `true`. When
`Update` is `true`, the RCS
value is updated. If `Update` is
`false`, the RCS remains unchanged.

#### Dependencies

To enable this port, set the **Fluctuation
model** drop-down menu to
`Swerling1`,
`Swerling2`,
`Swerling3`, or
`Swerling4`.
### Output

### **Port\_1** — Narrowband reflected signal 1-by-*M* complex-valued vector | *N*-by-*M* complex-valued matrix

Wideband nonpolarized signal, specified as an
1-by-*M* complex-valued vector or a
*N*-by-*M* complex-valued matrix.
Each column contains an independent signal reflected from the
target.

The quantity *N* is the number of signal samples and
*M* is the number of signals reflecting off the
target. Each column corresponds to a different reflecting angle.

The output port contains signal samples arriving at the signal
destination within the current input time frame. When the propagation
time from source to destination exceeds the current time frame duration,
the output does not contain all contributions from the input of the
current time frame.

## Parameters

### **Backscatter pattern frequency vector (Hz)** — Wideband backscatter pattern frequencies `[0,1e20]` (default) | real-valued row vector of positive values in strictly increasing order

Specify the frequencies used in the RCS matrix. The elements of this
vector must be in strictly increasing order. The target has no response
outside this frequency range. Frequencies are defined with respect to the
physical frequency band, not the baseband. Frequency units are in Hz.

**Data Types:** `double`

### **Azimuth angles (deg)** — Azimuth angles `[-180:180]` (default) | 1-by-*P* real-valued row vector | *P*-by-1 real-valued column vector

Azimuth angles used to define the angular coordinates of each column of
the matrices specified by the **RCS pattern (m^2)**
parameter. Specify the azimuth angles as a length *P*
vector. *P* must be greater than two. Angle units are in
degrees.

**Example:** `[-45:0.1:45]`

**Data Types:** `double`

### **Elevation angles (deg)** — Elevation angles `[-90:90]` (default) | 1-by-*Q* real-valued row vector | *Q*-by-1 real-valued column vector

Elevation angles used to define the angular coordinates of each row of the
matrices specified by the **RCS pattern (m^2)** parameter.
Specify the elevation angles as a length *Q* vector.
*Q* must be greater than two. Angle units are in
degrees.

**Example:** `[-30:0.1:30]`

**Data Types:** `double`

### **RCS pattern (m^2)** — Radar cross-section pattern `ones(181,361)` (default) | *Q*-by-*P* real-valued matrix | *Q*-by-*P*-by-*K* real-valued array | 1-by-*P*-by-*K* real-valued array | *K*-by-*P* real-valued matrix

Radar cross-section pattern, specified as a real-valued matrix or
array.

| Dimensions | Application |
| --- | --- |
| *Q*-by-*P* matrix | Specifies a matrix of RCS values as a function of *Q* elevation angles and *P* azimuth angles. The same RCS matrix is used for all frequencies. |
| *Q*-by-*P*-by-*K* array | Specifies an array of RCS patterns as a function of *Q* elevation angles, *P* azimuth angles, and *K* frequencies. If K = 1, the RCS pattern is equivalent to a *Q*-by-*P* matrix. |
| 1-by-*P*-by-*K* array | Specifies a matrix of RCS values as a function of *P* azimuth angles and *K* frequencies. These dimension formats apply when there is only one elevation angle. |
| *K*-by-*P* matrix |

- *Q* is the length of the vector specified by
  the **Elevation angles (deg)**
  parameter.
- *P* is the length of the vector specified by
  the **Azimuth angles (deg)** parameter.
- *K* is the number of frequencies specified by
  the **Backscatter pattern frequency vector
  (Hz)** parameter.

You can specify patterns for *L* targets by putting
*L* patterns into a cell array. All patterns must have
the same dimensions. The value of *L* must match the column
dimensions of the signals passed as input into the block. You can, however,
use one pattern to model *L* multiple targets.

RCS units are in square meters.

**Example:** `[1,2;2,1]`

**Data Types:** `double`

### **Fluctuation model** — Target fluctuation model `Nonfluctuating` (default) | `Swerling1` | `Swerling2` | `Swerling3` | `Swerling4`

Target fluctuation model, specified as
`Nonfluctuating`,
`Swerling1`,
`Swerling2`,
`Swerling3`, or
`Swerling4`. If you set this parameter to a
value other than `Nonfluctuating`, you must pass
either `true` or `false` into the
**Update**
`Update` port.

### **Propagation speed (m/s)** — Signal propagation speed `physconst('LightSpeed')` (default) | positive scalar

Signal propagation speed, specified as a real-valued positive scalar. The default
value of the speed of light is the value returned by
`physconst('LightSpeed')`.

**Data Types:** `double`

### **Operating frequency (Hz)** — Signal carrier frequency `300.0e6` (default) | positive real-valued scalar

Signal carrier frequency, specified as a positive real-valued scalar.
Units are in hertz.

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

### **Number of subbands** — Number of processing subbands `64` (default) | positive integer

Number of processing subbands, specified as a positive integer.

**Example:** `128`

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

**Introduced in R2016b**

## Description

Backscatter wideband signals from radar target

The Wideband Backscatter Radar Target block models the monostatic reflection of
nonpolarized wideband electromagnetic signals from a radar target. The target radar
cross-section (RCS) model includes four Swerling target fluctuation models and a
nonfluctuating model. You can model several targets simultaneously by specifying
multiple radar cross-section RCS matrices.
