---
type: simulink-block
title: 'Range-Angle Position Estimator'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Direction of Arrival'
documentation_page: 'rangeanglepositionestimator'
documentation_source_path: 'ref/rangeanglepositionestimator.html'
language: en
---

# Range-Angle Position Estimator

## Ports

### Input

### **RngEst** — range measurement (meters) real-valued 1-by-*K* vector | real-valued *J*-by-*L* matrix

Bistatic range or range-sum measurements, specified as a real-valued
1-by-*K* vector or real-valued
*J*-by-*L* matrix.

- When **RngEst** is a real-valued 1-by-*K* vector,
  the measurement represents bistatic range or range-sum measurements measured at
  one transmit anchor and one receive anchor for *K*
  targets.
- When **RngEst** is a real-valued
  *J*-by-*L* matrix, the measurement
  represents bistatic range or range-sum measurements measured at
  *J* transmit anchors and *L* receive
  anchors.

Units are in meters.

**Example:** `[1000 2000]`

**Data Types:** `single` | `double`

### **AngEst** — angle-of-arrival estimate (degrees) real-valued 1-by-*L* row vector | real-valued 2-by-*L* matrix

- When **RngEst** is a real-valued
  *J*-by-*L* matrix, `angest`
  should be a real-valued length-*L* row vector or
  2-by-*L* matrix. When **AngEst** is a row vector, it
  represents the azimuth angles measured at *L* receive anchors.
  When **AngEst** is a matrix, its first row represents the azimuth angle
  and its second row represents the elevation angle measured at *L*
  receive anchors.
- When **RngEst** is a real-valued 1-by-*K* vector,
  **AngEst** should be a real-valued *K*-element row
  vector or 2-by-*K* matrix.

**Example:** `[10 20]`

**Data Types:** `single` | `double`

### **RngVar** — range variance (meters-squared) `[]` (default) | positive real-valued *J*-by-*L* matrix | positive real-valued length-*K* row vector

Range variance, specified as an empty matrix or positive real-valued
*J*-by-*L* matrix or positive real-valued
length-*K* row vector. When **RngVar** is empty, the
variance estimates are unknown and are set to be unity for all targets.

- When **RngVar** is a *J*-by-*L*, it
  represents the variance of the bistatic range or range-sum estimates of a target
  measured at *J*-*L* anchor pairs. When
  **RngVar** is empty, the variance estimates are unknown and are set to
  unit for all anchor pairs. Units are in meters-squared.
- When **RngVar** is a length-K vector, it represents is the variance
  of bistatic range or range sum estimation of *K* targets measured
  at one anchor pair.

**Example:** `[10 15]`

#### Dependencies

To enable this port, select **Enable known variance input**
check box.

**Data Types:** `single` | `double`

### **AngVar** — angle variance (degrees-squared) `[]` | real-valued 1-by-*L* row vector | real-valued 2-by-*L* matrix

Angle measurement variances, specified as empty, real-valued
1-by-*L* row vector, or positive real-valued
2-by-*L* matrix. When **AngVar** is a vector, it
represents the azimuth angle variance estimates of a target measured at
*L* receive anchors. When **AngVar** is a matrix, it
represents the angle variance estimates of a target measured at *L*
receive anchors. When **AngVar** is empty, the variance estimates are unknown
and are set unity all *L* receive anchors. When the measurements are
accurate, we can set the corresponding variance to be empty.

**Example:** `[.10 .15]`

#### Dependencies

To enable this port, select **Enable known variance input**
check box.

**Data Types:** `single` | `double`

### **AnchorPos** — Anchor positions (meters) real-valued *Q*-by-*J* matrix

Anchor positions, specified as a real-valued
*Q*-by-*J* matrix. *J* is the
number of anchors. Each column represents the position of a different anchor.
Positions may be two or three dimensional. For two dimensional positions,
*Q=2* and for three dimensional positions, *Q=3*.
The *j*th column of
`txpos` denotes the position of the
*j*th transmitter in
*Q*-dimensional Cartesian space. Units are in meters.

**Example:** `[20 31 –16; 13 64 –44]`

**Data Types:** `single` | `double`
### Output

### **TgtPosEst** — Target position estimate (meters) real-valued *Q*-by-1 vector

Target position estimate, returned as a real-valued *Q*-by-1
vector or real-valued *Q*-by-*K* matrix,
representing the estimated *K* target positions. Units are in
meters.

**Data Types:** `single` | `double`

### **TgtPosCov** — Estimated target position covariance (meters-squared) real-valued *Q*-by-*Q* matrix | real-valued *Q*-by-*Q*-by-*K* array

When the input contains *JL* anchor pairs with one target, the
`tgtposcov` is a *Q*-by-*Q*
matrix, which is a real positive semi-definite symmetric matrix representing the
estimated target position covariance. When the input contains 1 anchor pair with
*K* targets, the `tgtposcov` is a
*Q*-by-*Q*-by-*K* array, where
each page is a real-valued positive semi-definite symmetric matrix, representing the
estimated target position covariance. Units are in meters-squared.

#### Dependencies

To enable this port, select the **Output covariances of position
estimates** check box.

**Data Types:** `single` | `double`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Enable known variance input** — Enable known variance input on (default) | off

Select this check box to allow input from the **RngVar** and
**AngVar** ports.

**Data Types:** `Boolean`

### **Output covariances of position estimates** — Output covariances of position estimates off (default) | on

Select this check box to output position covariance estimates from the
**TgtPosCov** port.

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

Estimate target positions using range-angle measurements

The Range-Angle Position Estimator block estimates target positions using
range-angle measurements.
