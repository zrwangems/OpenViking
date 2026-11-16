---
type: simulink-block
title: 'TDOA Estimator'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Direction of Arrival'
documentation_page: 'tdoaestimator'
documentation_source_path: 'ref/tdoaestimator.html'
language: en
---

# TDOA Estimator

## Ports

### Input

### **X** — Input data *N*-by-*M*-by-*L*complex-valued array

Received signal matrices, specified as an
*N*-by-*M*-by-*L* complex-valued
array. *L* represents the number of anchors. Each page represents an
*N*-by-*M* complex-valued matrix for one anchor.
The first page corresponds to the reference anchor. The rows of each signal matrix
represent *M* independent pulses (such as slow-time samples of a
radar) and each column represents *N* fast-time samples of a
pulse.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **DelayOffset** — Delay offset (sec) scalar | 1-by-*L* real-valued vector

Delay offset, specified as a scalar or as a 1-by-*L* real-valued
vector where *L* is the number of anchors. The TDOA estimation result
`Y` is adjusted by `delayoffset`. The offset
is the known delay offset between the clock at each anchor and the reference clock for
the first anchor. If `DelayOffset` is a scalar, the delay offset is
the same for all *L* anchors. If `DelayOffset` is
a 1-by-*L* vector, the delay offset can be different for different
anchors. Units are in seconds.

#### Dependencies

To enable the **DelayOffset** input port, select the **Enable
known delay offset input** check box.

**Data Types:** `single` | `double`

### **Npow** — Input noise power (W) positive scalar | 1-by-*L* vector of positive values

Input noise power, specified as a positive scalar or a 1-by-*L*
vector with positive values. `Npow` represents the white Gaussian
noise power at each anchor. If `Npow` is a scalar, the noise power
is the same for all *L* anchors. If `Npow` is a
1-by-*L* vector, the same noise power value is applied to each of
the *L* anchors. Units are in Watts.

This argument lets you calculate the optional output argument
`var` using the input argument `Npow`,

**Example:** `50`

#### Dependencies

To enable this argument, set the **Source of noise power**
parameter to `'Input port'`.

**Data Types:** `single` | `double`
### Output

### **Y** — TDOA estimates (sec) *K*-by-(*L*-1) real-valued matrix

TDOA estimates, returned as a *K*-by-(*L*–1)
real-valued matrix. *K* is the maximum number of targets specified by
the `NumEstimates` property. *L* is the number of
anchors producing (*L*–1) anchor pairs. The
`l`th column of `Y`
represents the TDOA estimates for the
`l`th anchor pair which is the time
difference between (`l+1`)-th anchor and
the first anchor.

The TDOA for an anchor pair is estimated by detecting the locations of up to
*K* peaks from the GCC-PHAT TDOA spectrum. If the number of
detected peaks for the `l`th anchor pair
is less than *K*, the first entries of the
`l`th column of `Y`
contain the valid TDOA estimates, and the remaining entries in the
`l`th column of `Y`
are filled with `NaN`. Units are in seconds.

**Data Types:** `single` | `double`

### **Var** — Estimated TDOA variance 1-by-(*L*-1) positive-value vector

Estimated TDOA variance, returned as a 1-by-(*L*-1)
positive-valued vector. `var` is obtained from the Cramer-Rao lower
bound (CRLB) of estimating TDOA based on the input `X` and the
white Gaussian noise power, assuming there are *K* targets equally
splitting received signal power. The noise power can be specified either by the
`NoisePower` property or using the `npow`
input argument.. Units are seconds-squared.

#### Dependencies

To enable this port, select the **Output variance of TDOA
estimates** check box.

**Data Types:** `single` | `double`

### **TDOAResp** — TDOA response *P*-by-*M*-by-(*L*-1) MATLAB® array

TDOA response, output as a
*P*-by-*M*-by-(*L*-1) MATLAB array where *P* is the number of TDOA grid samples,
*L* is the number of anchors, and *M* is number of
independent pulses.

#### Dependencies

To enable this port, select the **Output TDOA response and TDOA
grid** check box.

**Data Types:** `single` | `double`

### **TDOAGrid** — TDOA grid real-valued *P*-by-(*L*-1) matrix

Time-difference of arrival grid, returned as a real-valued
*P*-by-(*L*-1) matrix, where *P*
is the number of TDOA grid samples and *L* is the number of
anchors.

#### Dependencies

To enable this port, select the **Output TDOA response and TDOA
grid** check box.

**Data Types:** `single` | `double`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Inherit sample rate** — Inherit sample rate from upstream blocks on (default) | off

Select this parameter to inherit the sample rate from upstream blocks. Otherwise,
specify the sample rate using the **Sample rate (Hz)**
parameter.

**Data Types:** `Boolean`

### **Signal sample rate (Hz)** — Signal sampling rate `1000000` (default) | real-valued positive scalar

Signal sample rate, specified as a real-valued positive scalar.

#### Dependencies

To enable this parameter, deselect the **Inherit sample rate**
check box.

**Data Types:** `Boolean`

### **Maximum number of TDOA estimates** — Maximum number of TDOA estimates `1` (default) | positive integer

Maximum number of TDOA estimates, specified as a positive integer.

**Example:** `100`

**Data Types:** `single` | `double`

### **Enable known delay offset input** — Enable known delay offset input `false` (0) (default) | `true` (1)

Select the **Enable known delay offset input** check box to
enable the **DelayOffset** input port.

**Data Types:** `Boolean`

### **Output variance of TDOA Estimates** — Output variance of TDOA estimates `false` (0) (default) | `true` (1)

Select the **Output variance of TDOA Estimates** check box to
enable the **Var** output port containing the TDOA variances.

**Data Types:** `Boolean`

### **Output TDOA response and TDOA grid** — Output TDOA response and TDOA grid `false` (0) (default) | `true` (1)

Select the **Output TDOA response and TDOA grid** check box to
enable the **TROAResp** and **TDOAGrid** output ports.

**Data Types:** `Boolean`

### **Source of noise power** — Source of noise power `Property` (default) | `Input port`

Source of noise power, specified as `Property` or `Input
port`.

### **Noise power (W)** — Noise power `1` (default) | positive scalar

Noise power, specified as a positive scalar. Units are Watts.

#### Dependencies

To enable this parameter, set the **Source of noise power** to
`Property`.

**Data Types:** `double` | `single`

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

When the Simulink model is in `Accelerator` mode, the block mode specified
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

Phased Array System Toolbox / Direction of Arrival

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024b**

### R2025a: New output ports

Two new output ports are added to return time-difference of arrival (TDOA) data and the
TDOA time grid.

## Description

Estimate time-difference of arrival

Estimate TDOA of signals from active devices to multiple passive anchors. The TDOA's are
estimated based on time-domain received signals at different anchors.
