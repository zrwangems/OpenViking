---
type: simulink-block
title: 'Bistatic Position Estimator'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Direction of Arrival'
documentation_page: 'bistaticpositionestimator'
documentation_source_path: 'ref/bistaticpositionestimator.html'
language: en
---

# Bistatic Position Estimator

## Ports

### Input

### **RngEst** — Range measurement (meters) real-valued 1-by-*K* vector | real-valued *J*-by-*L* matrix

Bistatic range or range-sum measurements, specified as a real-valued
*1*-by-*K* vector or real-valued
*J*-by-*L* matrix.

- When **RngEst** is a real-valued
  *J*-by-*L* matrix, the measurement
  represents bistatic range or range-sum measurements measured at
  *J* transmit anchors and *L* receive
  anchors.
- When **RngEst** is a real-valued 1-by-*K* vector,
  the measurement represents bistatic range or range-sum measurements measured at
  one transmit anchor and one receive anchors for *K*
  targets.

Units are in meters.

**Example:** `[1000 2000]`

**Data Types:** `single` | `double`

### **AngEst** — Angle-of-arrival estimate (degrees) real-valued 1-by-*L* row vector | real-valued 2-by-*L* matrix

- When **RngEst** is a real-valued
  *J*-by-*L* matrix, **AngEst** should
  be a real-valued length-*L* row vector or
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

### **RngVar** — Range variance (meters-squared) positive real-valued *J*-by-*L* matrix | positive real-valued length-*K* row vector

Range variance, specified as a positive real-valued
*J*-by-*L* matrix or positive real-valued
length-*K* row vector. When **RngVar** is empty, the
variance estimates are unknown and are set to be unity for all targets.

- When **RngVar** is a *J*-by-*L*, it
  represents the variance of the bistatic range or range-sum estimates of a target
  measured at *J*-*L* anchor pairs. When
  **RngVar** is empty, the variance estimates are unknown and are set to
  unity for all anchor pairs. Units are in meters-squared.
- When **RngVar** is a length-K vector, it represents the variance of
  bistatic range or range sum estimation of *K* targets measured at
  one anchor pair.

**Example:** `[10 15]`

#### Dependencies

To enable this port, select **Enable known variance input**
check box.

**Data Types:** `single` | `double`

### **AngVar** — Angle variance (degrees-squared) real-valued 1-by-*L* row vector | real-valued 2-by-*L* matrix

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

### **TxPos** — Transmitting anchor positions (meters) real-valued *Q*-by-*J* matrix

Transmitting anchor positions, specified as a real-valued
*Q*-by-*J* matrix. *J* is the
number of transmitting anchors. Each column represents the position of a different
anchor. Positions may be two or three dimensional. For two dimensional positions,
*Q=2* and for three dimensional positions, *Q=3*.
The *j*th column of **TxPos**
denotes the position of the *j*th
transmitter in *Q*-dimensional Cartesian space. Units are in
meters.

**Example:** `[20 31 –16; 13 64 –44]`

**Data Types:** `single` | `double`

### **RxPos** — Receiving anchor positions (meters) real-valued *Q*-by-*L* matrix

Receiving anchor positions, specified as a real-valued
*Q*-by-*L* matrix. *L* is the
number of receiving anchors. Each column represents the position of a different
anchor. Positions may be two or three dimensional. For two dimensional positions,
*Q*=2 and for three dimensional positions, *Q*=3.
The *l*th column of **RxPos**
denotes the position of the *l*th receiver
in *Q*-dimensional Cartesian space. Units are in meters.

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

### **Range Measurement** — Range measurement type **Bistatic range** (default) | **Range sum**

Range measurement type, specified as **Bistatic range** or
**Range sum**. The bistatic range is the range sum subtracted by the
baseline range. When **Bistatic range** is chosen, the target position
estimation uses bistatic range and AOA measurements. When **Range sum**
chosen, the target position estimation uses range-sum and AOA measurements.

### **Enable known variance input** — Enable known variance inputs on (default) | off

Select this check box to allow input from the **RngVar** and
**AngVar** ports.

### **Output covariances of position estimates** — Output covariances of position estimates off (default) | on

Select this check box to output position covariance estimates from the
**TgtPosCov** port.

**Data Types:** `single` | `double`

## Libraries

Phased Array System Toolbox / Direction of Arrival

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2025a**

## Description

Estimate targets positions using bistatic range and angle measurements

The Bistatic Position Estimator block estimates target positions from
bistatic range or range-sum measurements with known anchor positions.
