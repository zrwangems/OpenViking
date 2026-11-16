---
type: simulink-block
title: 'TDOA Position Estimator'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Direction of Arrival'
documentation_page: 'tdoapositionestimator'
documentation_source_path: 'ref/tdoapositionestimator.html'
language: en
---

# TDOA Position Estimator

## Ports

### Input

### **TDOAEst** — Estimated time-difference of arrival (sec) (*L*–1)-element real-valued vector

Estimated time-difference of arrival of signals between anchor pairs with respect
to the first anchor and target, specified as an (*L*–1)-element
real-valued vector. *L* is the number of anchors. Units are in
seconds.

**Data Types:** `single` | `double`

### **TDOAVar** — Estimated variances of time-differences of arrival (seconds-squared) (*L*–1)-element real-valued vector

Estimated variances of time-difference of arrival of signals between anchor pairs
with respect to the first anchor and target, specified as an
(*L*–1)-element real-valued vector. *L* is the
number of anchors. Units are in seconds-squared.

**Data Types:** `single` | `double`

### **AnchorPos** — Anchor positions (meters) 2-by-*L* real-valued matrix | 3-by-*L* real-valued matrix

Anchor positions, specified as 2-by-*L* real-valued matrix or
3-by-*L* real-valued matrix. A 2-by-*L* matrix
represents the anchor positions in 2-D Cartesian space, while a
3-by-*L* matrix represents the anchor positions in 3-D Cartesian
space. Units are in meters.

**Data Types:** `single` | `double`
### Output

### **TgtPosEst** — Target position estimate real-valued *Q*-by-1 vector

Estimated target positions, returned as a *Q*-by-1 vector
representing the estimated target position obtained from TDOA measurements. Units are
in meters.

**Data Types:** `single` | `double`

### **TgtPosCov** — Target position covariance matrix real-valued positive semi-definite *Q*-by-*Q* matrix

Target position covariance matrix, returned as a real-valued positive
semi-definite *Q*-by-*Q* matrix. The covariance
matrix represents the estimated target position covariance calculated from the
Cramer-Rao lower bound (CRLB) of the TOA position estimator. Calculating the
covariance requires the knowledge of `toavar`. When
`toavar` is inaccurate, `tgtposcov` is also
inaccurate. When `toavar` is accurate and small, the
`tgtposcov` value represents the TOA position estimate CRLB.
Units are in ㎡eters-squared.

#### Dependencies

To enable this output port, select the **Output covariance of TDOA
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

### **Output covariances of TDOA position estimates** — Output covariance of TDOA position estimates `false` (0) (default) | `true` (1)

Select the **Output covariances of TDOA position estimates**
check box to enable the **TgtPosCov** output port containing the TDOA position
covariances.

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

Not documented in R2025b.

## Version History

**Introduced in R2024b**

## Description

Estimate target position from time-difference of arrival

Estimate target position from time-difference-of-arrival (TDOA) measurements and anchor
positions. The block also estimates the variance of the time-difference of arrival
measurements.
