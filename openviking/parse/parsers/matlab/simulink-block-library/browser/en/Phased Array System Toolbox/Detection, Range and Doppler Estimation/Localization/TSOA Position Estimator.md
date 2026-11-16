---
type: simulink-block
title: 'TSOA Position Estimator'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Detection, Range and Doppler Estimation / Localization'
documentation_page: 'tsoapositionestimator'
documentation_source_path: 'ref/tsoapositionestimator.html'
language: en
---

# TSOA Position Estimator

## Ports

### Input

### **TSOAEst** — Time-sum of arrival estimates (sec) real-valued *J*-by-*L*-by-*K* array

Time-sum of arrival estimates, input as a real-valued
*J*-by-*L*-by-*K* array, where
*J* is the number of transmitting anchors, *L* is
the number of receiving anchors, and *K* is the number of TSOA
groups. Each page represents a TSOA group corresponding to the TSOAs measured at the
*JL* anchor pairs for a potential target. In each page, the element
in the *j*th row and
*l*th column of
`TSOAEst` represents the estimated TSOA from the
*j*th transmit anchor to the
*l*th receive anchor. When the actual
values of `TSOAVar` are unknown, `TSOAVar` is
typically chosen to be a matrix with each element chosen to be the same real positive
value. This value does not impact affect the solution
`tgtposest`.Units are in seconds.

**Data Types:** `single` | `double`

### **TSOAVar** — TSOA estimation variance (seconds-squared) real-valued *J*-by-*L* matrix | real-valued *J*-by-*L*-by-*K* array

TSOA estimation variance, input as a real-valued
*J*-by-*L* matrix or real-valued
*J*-by-*L*-by-*K* array.
Representing the variance of TSOA estimation variance for the *JL*
anchor pairs. When `TSOAVsr` is a matrix, the variance estimates
for *JL* anchor pairs are the same for all *K* TSOA
groups. When `TSOAVar` is an array, the variance estimates for
*JL* anchor pairs are different for different TSOA groups. Units
are in seconds-squared.

**Data Types:** `single` | `double`

### **TxPos** — Transmitting anchor positions (meters) real-valued *Q*-by-*J* matrix

Transmitting anchor positions, input as a real-valued
*Q*-by-*J* matrix. *J* is the
number of transmitting anchors. Each column represents the position of a different
anchor. Positions may be two or three dimensional. For two dimensional positions,
*Q*=2 and for three dimensional positions, *Q*=3.
The *j*th column of
`txpos` denotes the position of the
*j*th transmitter in
*Q*-dimensional Cartesian space. Units are in meters.

**Example:** `[20 31 –16; 13 64 –44]`

**Data Types:** `single` | `double`

### **RxPos** — Receiving anchor positions (meters) real-valued *Q*-by-*L* matrix

Receiving anchor positions, input as a real-valued
*Q*-by-*L* matrix. *L* is the
number of receiving anchors. Each column represents the position of a different
anchor. Positions may be two or three dimensional. For two dimensional positions,
*Q=2* and for three dimensional positions, *Q=3*.
The *l*th column of
`rxpos` denotes the position of the
*l*th receiver in
*Q*-dimensional Cartesian space. Units are in meters.

**Example:** `[20 31 –16; 13 64 –44]`

**Data Types:** `single` | `double`
### Output

### **TgtPosEst** — Target position estimate real-valued *Q*-by-1 vector

Estimated target positions, returned as a *Q*-by-1 vector
representing the estimated target position obtained from TSOA measurements. Units are
in meters.

**Data Types:** `single` | `double`

### **TgtPosCov** — Target position covariance matrix real-valued positive semi-definite *Q*-by-*Q* matrix

Target position covariance matrix, returned as a real-valued positive
semi-definite *Q*-by-*Q* matrix. The covariance
matrix represents the estimated target position covariance calculated from the
Cramer-Rao lower bound (CRLB) of the TSOA position estimator. Calculating the
covariance requires the knowledge of `TSOAVar`. When
`TSOAVar` is inaccurate, `TgtPosCov` is also
inaccurate. When `TSOAVar` is accurate and small, the
`TgtPosCov` value represents the TSOA position estimate CRLB.
Units are in meters-squared.

#### Dependencies

To enable this output port, select the **Output covariance of TSOA
position estimate** check box.

**Data Types:** `single` | `double`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Signal propagation speed (m/s)** — Signal propagation speed `physconst("LightSpeed")` (default) | positive real scalar

Signal propagation speed, specified as a positive real scalar. Units are in meters
per second.

**Example:** `3e8`

**Data Types:** `double`

### **Output covariances of TSOA position estimates (meters-squared)** — Output covariance of TSOA position estimates `false` (0) (default) | `true` (1)

Select the **Output covariances of TSOA position estimates**
check box to enable the **TgtPosCov** output port containing the TSOA position
covariances. Units are meters-squared.

**Data Types:** `Boolean`

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

**Introduced in R2025a**

## Description

Estimate target position from time-sum of arrival

Estimate target position from time-sum-of-arrival (TSOA) measurements and anchor
positions. The block also estimates the variance of the time-sum of arrival
measurements.
