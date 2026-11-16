---
type: simulink-block
title: 'TOA Estimator'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Direction of Arrival'
documentation_page: 'toaestimator'
documentation_source_path: 'ref/toaestimator.html'
language: en
---

# TOA Estimator

## Ports

### Input

### **X** — Channel estimation matrices *N*-by-*M* complex-valued matrix | *N*-by-*M*-by-*L* complex-valued array | 1-by-*L* cell array

Channel estimation matrix, specified as a
*N*-by-*M* complex-valued matrix, an
*N*-by-*M*-by-*L* complex-valued
array, or a 1-by-*L* cell array. Each row of the
*N*-by-*M* channel estimation matrix represents
*M* samples (e.g., *M* spatial streams of MIMO
communication, *M* pulses of radar) of a channel estimate on one
subband, and each column of the matrix represents a sample of a channel estimate on
*N* uniformly-spaced subbands.

- When the channel estimation matrix is
  *N*-by-*M*-by-*L* array,
  each page of the array is an *N*-by-*M*
  channel estimation matrix. All channel estimation matrices must have the same
  size.
- When the channel estimation matrices is a1-by-*L* cell
  array, each cell contains a frequency-domain channel estimation matrix from one
  of the *L* anchors. The size of a channel estimation matrix can
  vary for different anchors.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **FreqSpacing** — Frequency spacings of channel estimates `900000`

Frequency spacings of channel estimates, specified as a positive scalar or as a
1-by-*L* vector of positive values. If **FreqSpacing** is
a scalar, the frequency spacing is the same for all *L* anchors. If
**FreqSpacing** is a 1-by-*L* vector, the frequency
spacing can be different for different anchors. Units are in Hz.

**Example:** `[10e6 15e6 20e6]`

**Data Types:** `single` | `double`

### **DelayOffset** — Known delay offset scalar | real-valued 1-by-*L* vector

Known delay offset between the target and each anchor, specified as a scalar or a
real-valued 1-by-*L* vector. If **DelayOffset** is a scalar,
the delay offset is the same for all signals from or to all *L*
anchors. If **DelayOffset** is a 1-by-*L* vector, the delay
offset can be different for different anchors. **DelayOffset** compensates
all TOA/TDOA estimation results, **Y**. Units are in seconds.

#### Dependencies

To enable this port, select the **Enable known delay
offset input** check box.

**Data Types:** `single` | `double`

### **NPow** — Gaussian white noise power scalar | positive real-valued 1-by-*L* vector

Gaussian white noise power, specified as scalar or positive real-valued
1-by-*L* vector. If `npow` is a scalar, the
noise power is the same for all *L* anchors. If **NPow** is
a 1-by-*L* vector, a different noise power value can be applied to
each of the *L* anchors. Units are in watts.

**Example:** `0.4`

#### Dependencies

To enable this port, select the **Output variance of TOA/TDOA
estimates** check box, and then set the **Source of noise
power** port to `'Input port'`.

**Data Types:** `single` | `double`

### **AnchorPos** — Anchor positions *Q*-by-*L* real-valued matrix

Anchor positions, specified as a *Q*-by-*L*
real-valued matrix representing the position of the *L* anchors in
the *Q*-dimensional Cartesian space (*Q* can be 2 or
3). Each column denotes the position of each anchor in the
*Q*-dimensional Cartesian space.

#### Dependencies

To enable this port, select the **Output estimated target
position** check box.

**Data Types:** `single` | `double`
### Output

### **Y** — TOA and TDOA estimation results 1-by-*L* real-valued vector | 1-by-(*L*-1) real-valued vector

Times-of-arrival (TOA) or time-differences of arrival (TDOA) estimation from a
target at *L* anchors, output as a 1-by-*L*
real-valued vector or a 1-by-(*L*-1) real-valued vector.

- If the `TOA/TDOA Measurement` parameter is
  `'TOA'`, **Y** is a 1-by-*L*
  real-valued vector. The signal model of the TOA output at the
  `l`th-anchor can be written as
  `Y(l) = min(taul)`, for `l = 1,2,...,L`,
  where `taul` is the vector of received multipath delays at the
  `l`th anchor.
- If the `TOA/TDOA Measurement` parameter is set to
  `'TDOA'`, **Y** is a 1-by-(*L*-1)
  real-valued vector. The signal model of the TDOA output at the
  (`l`-1)th anchor can be written as
  `Y(l-1) = min(taul)-min(reftau)`, `l =
  2,3,...,L`, where `taul` is the vector of received
  multipath delays at the `l`th anchor
  and `reftau` is the vector of received multipath delays at the
  first anchor.

Units are in seconds.

**Data Types:** `single` | `double`

### **Var** — Measurement variance 1-by-*L* vector | 1-by-(*L*-1) vector

- If the `Measurement` is `'TOA'`,
  **Var** is a 1-by-*L* vector representing the
  estimated TOA variance.
- If the `Measurement` property is
  `'TDOA'`, **Var** is a 1-by-(*L*-1)
  vector representing the estimated TDOA variance.

Units are in seconds-squared. **Var** is obtained through the
Cramer-Rao lower bound (CRLB) of the TOA/TDOA estimator.

#### Dependencies

To enable this port, select the **Output variance of TOA/TDOA
estimates** check box, and then set the **Source of noise
power** port to `'Input port'`.

**Data Types:** `single` | `double`

### **TgtPosEst** — Target position estimate real-valued *Q*-by-1 vector

Estimated target positions, output as a *Q*-by-1 vector
representing the estimated target position obtained from TOA and TDOA measurements.
Target positions are obtained using a two-step weighted linear least squares (WLLS)
algorithm that approximates a maximum-likelihood estimation algorithm The algorithm
can achieve the position estimation CRLB when the TOA and TDOA estimation errors are
small. Units are in meters.

#### Dependencies

To enable this port, select the **Output estimated target
position** check box.

**Data Types:** `single` | `double`

### **TgtPosCov** — Target position covariance estimates *Q*-by-*Q* real positive semi-definite symmetric matrix

Target position covariance estimates, output as a
*Q*-by-*Q* real positive semi-definite symmetric
matrix. The matrix represents the estimated target position covariance using TOA/TDOA
measurements. The covariance is obtained from the CRLB of the TOA/TDOA position
estimate. Units are m2.

#### Dependencies

To enable this port, select the **Output estimated target
position** check box.

**Data Types:** `single` | `double`

### **TOAResp** — FFT-based TOA response *P*-by-*M*-by-*L* matrix | 1-by-*L* cell array

FFT-based TOA response, output as:

If the channel estimate `X` is an
*N*-by-*M*-by-*L* array,
`toaresp` is a
*P*-by-*M*-by-*L* array.

If the channel estimate `X` is a 1-by-*L* cell
array, `toaresp` is a 1-by-*L* cell array,
containing the TOA response for each of the *s* anchors.

#### Dependencies

To enable this port, select the **Output FFT-based TOA
response** check box.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **TOAGrid** — TOA grid *P*-by-*L* matrix | 1-by-*L* cell array

Times of arrival grid, output as *P*-by-*L*
matrix or a 1-by-*L* cell array. Times of arrival are restricted to
this grid.

- If the channel estimate `X` is a
  *N*-by-*M*-by-*L* array,
  `toagrid` is returned as a
  *P*-by-*L* matrix, where
  *P* is the number of TOA grid samples.
- If the channel estimate `X` is a
  1-by-*L* cell array, `toagrid` is a
  1-by-*L* cell array, containing the TOA grid for each of the
  *L* anchors. Units are in seconds.

#### Dependencies

To enable this port, select the **Output FFT-based TOA
response** check box.

**Data Types:** `single`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Signal propagation speed (m/s)** — Signal propagation speed `physconst('LightSpeed')` (default) | real-valued positive scalar

Signal propagation speed, specified as a real-valued positive scalar. The default
value of the speed of light is the value returned by
`physconst('LightSpeed')`. Units are in meters per second.

**Example:** `3e8`

**Data Types:** `double` | `single`

### **TOA/TDOA measurement** — Measurement type `TOA` (default) | `TDOA`

Measurement type, specified as `TOA` or
`TDOA`. When `TOA` is chosen, TOA
measurements are estimated using TOA spectrum analysis and a TOA positioning algorithm.
When `TDOA` is chosen, TDOA measurements are calculated based
on TOA measurements and a TDOA positioning algorithm is used.

**Data Types:** `char` | `string`

### **TOA spectrum analysis method** — Spectrum analysis method `FFT` (default) | `MUSIC`

TOA spectrum analysis method, specified as `FFT` or
`MUSIC`. When `FFT` is chosen, an
FFT is used to obtain the TOA spectrum. When `MUSIC` is chosen,
a MUSIC super-resolution algorithm is used to obtain the TOA spectrum.

**Data Types:** `char` | `string`

### **Enable known delay offset input** — Enable input of delay offsets 0 (default) | 1

Select this check box to enable input of known delay offsets or estimated delay
offsets between anchors and a target using the **DelayOffset** input port. When
not selected, the **DelayOffset** input port is disabled and delay offsets are
assumed to be zero.

**Data Types:** `Boolean`

### **Output variance of TOA/TDOA estimates** — Enable output variance of TOA/TDOA estimates 0 (default) | 1

Select this check box to enable the output of variances of the TOA or TDOA estimates
using the **Var** output port. Clear this check box to not output the estimated
variances. Selecting this check box also enables the **Source of noise
power** and **Noise power (W)** parameters and the
**Npow** input port.

**Data Types:** `Boolean`

### **Output FFT-based TOA response** — Enable output of FFT-based TOA response `0` (default) | `1`

Select this check box output and FFT-based TOA response. Clear this check box to not
output the TOA response.

#### Dependencies

To enable this parameter, set the **TOA/TDOA Measurement**
parameter to **TOA** and set the **TOA spectrum analysis
method** to **FFT**.

**Data Types:** `Boolean`

### **Enable forward-backward averaging** — Enable forward-backward averaging `0` (default) | `1`

Select this check box to enable forward-backward averaging. Forward-backward
averaging is used to mitigate rank deficiency in the source covariance matrix used in
the MUSIC spectrum analysis estimation method. This is useful when the number of
independent samples of the channel estimate is small.

#### Dependencies

To enable this parameter, set the **TOA spectrum analysis
method** to `MUSIC`.

**Data Types:** `Boolean`

### **Spatial smoothing** — Spatial smoothing parameter 0 (default) | nonnegative integer

Effective reduction in the number of subbands for TOA estimation due to spatial
smoothing, specified as a nonnegative integer. Spatial smoothing can be used to mitigate
the rank deficiency issue in the source covariance matrix estimation of the MUSIC
spectrum analysis method. This technique is useful when the number of independent
samples of channel estimate is small.

If there are *N* subbands and the value of the **Spatial
smoothing** parameter is *K*, then (*K*+1)
maximally overlapped bands of *N-K* subbands are formed. Then,
(*K*+1) covariance matrices are estimated for signals on the
(*K*+1) overlapped bands and these (*K*+1)
covariance matrices are averaged together to produce a spatially smoothed covariance
matrix of size
(*N*-*K*)-by-(*N*-*K*).
Incrementing *K* by 1 increases the rank of the spatially smoothed
covariance matrix by 1 until the range reaches its maximum. However, the effective
number of subbands for TOA estimation is reduced by 1. The minimum value of
*K* is 0 which result in no spatial smoothing. The maximum value of
*K* is *N*-2, resulting in (*N*-1)
overlapped bands of two subbands.

If **Spatial smoothing** is a scalar, the spatial smoothing value
is the same for all *L* anchors. If **Spatial
smoothing** is a length-*L* vector, each spatial smoothing
value is applied to one of the *L* anchors.

#### Dependencies

To enable this parameter, set the **TOA spectrum analysis
method** to `MUSIC`.

**Data Types:** `single` | `double`

### **Output estimated target position** — Enable output of estimated target position 0 (default) | 1

Select this check box to enable output of estimated target positions using the
**TgtPosEst** port and the estimated target position covariances using the
**TgtPosCov** port. Selecting this check box also allows input of anchor
positions using the **AnchorPos** port.

**Data Types:** `Boolean`

### **Source of noise power** — Source of noise power `Property` (default) | `Input port`

Specify how the object determines the noise power values used for TOA and TDOA
variance estimation as `'Property'` or `'Input port'`.
When you set **Source of noise power** parameter to
`'Property'`, the **Noise power (W)** parameter
then represents the noise power of the received data. When you set **Source of
noise power** to `'Input port'`, then set the noise power
through the input **NPow** port.

**Example:** `Input port`

#### Dependencies

To enable this parameter, select the **Output estimated target
position** check box.

**Data Types:** `char` | `string`

### **Noise power (W)** — Gaussian white noise power positive scalar (default) | 1-by-*L* real-valued vector of positive values

Gaussian white noise power, specified as a positive scalar or
1-by-*L* real-valued vector of positive values.

#### Dependencies

To enable this parameter, select the **Output estimated target
position** check box and then select **Source of noise
power** as `Property`.

**Data Types:** `single` | `double`

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

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024a**

## Description

Estimate time of arrival, time-difference of arrival, and position

The TOA Estimator block Simulink® estimates time-of-arrival (TOA) or time-difference of arrival (TDOA) at multiple
devices. The block estimates TOA or TDOA from an active device to multiple passive anchors or
from multiple active anchors to a passive device. TOA and TDOA are estimated based on a
frequency-domain channel estimation. Using TOA, the block then estimates target
position.
