---
type: simulink-block
title: 'Three-axis Inertial Measurement Unit'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Sensors'
documentation_page: 'threeaxisinertialmeasurementunit'
documentation_source_path: 'ref/threeaxisinertialmeasurementunit.html'
language: en
---

# Three-axis Inertial Measurement Unit

## Ports

### Input

### **A\_b** — Actual accelerations three-element vector

Actual accelerations in body-fixed axes, specified as a three-element vector, in
selected units.

**Data Types:** `double`

### **w** — Angular rates three-element vector

Angular rates in body-fixed axes, specified as a three-element vector, in radians
per second.

**Data Types:** `double`

### **w\_dot** — Angular accelerations three-element vector

Angular accelerations in body-fixed axes, specified as a three-element vector, in
radians per second squared.

**Data Types:** `double`

### **CG** — Location of center of gravity three-element vector

Location of the center of gravity, specified as a three-element vector, in
selected units.

**Data Types:** `double`

### **g** — Gravity three-element vector

Gravity in body axis, specified as a three-element vector, in selected
units.

**Data Types:** `double`
### Output

### **A\_meas** — Measured accelerations three-element vector

Measured accelerations from the accelerometer, specified as a three-element
vector, in selected units.

**Data Types:** `double`

### **w\_meas** — Measured angular rates three-element vector

Measured angular rates from the gyroscope, specified as a three-element vector, in
radians per second.

**Data Types:** `double`

## Parameters

#### Main

### **Units** — Units `Metric (MKS)` (default) | `English`

Input and output units, specified as:

| Units | Acceleration | Length |
| --- | --- | --- |
| `Metric (MKS)` | Meters per second squared | Meters |
| `English` (British Imperial) | Feet per second squared | Feet |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `units` |
| **Type**: character vector |
| **Values**: `'Metric (MKS)'` | `'English'` |
| **Default**: `'Metric (MKS)'` |

### **IMU location** — IMU location `[0 0 0]` (default) | three-element vector

The location of the IMU, which is also the accelerometer group location, from the
vehicle center of gravity, along the vehicle-fixed axis. This measurement reference is
the same for the center of gravity input. The units are in selected length units.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `imu` |
| **Type**: character vector |
| **Values**: three-element vector |
| **Default**: `'[0 0 0]'` |

### **Update rate** — Update rate `0` (default) | real, double scalar

Update rate of the accelerometer and gyroscope, specified as a real, double scalar,
in seconds. An update rate of 0 creates a continuous accelerometer and continuous
gyroscope. If you select the **Noise on** parameter and the update rate
is 0, the block updates the noise at a rate of 0.1.

**Tip**

If you:

- Update this parameter value to 0 (continuous)
- Configure a fixed-step solver for the model

you must also select the **Automatically handle rate transition for data
transfer** check box in the **Solver** pane. This check
box enables the software to handle rate transitions correctly.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `a_Ts` |
| **Type**: character vector |
| **Values**: real, double scalar |
| **Default**: `'0'` |

#### Accelerometer

### **Second order dynamics for accelerometer** — Second-order dynamics `on` (default) | `off`

To apply second-order dynamics to acceleration readings, select this check
box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `dtype_a` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'on'` |

### **Accelerometer natural frequency (rad/sec)** — Accelerometer natural frequency `190` (default) | real, double scalar

Natural frequency of the accelerometer, specified as a real, double scalar, in
radians per second.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `w_a` |
| **Type**: character vector |
| **Values**: real, double scalar |
| **Default**: `'190'` |

#### Dependencies

To enable this parameter, select **Second order dynamics for
accelerometer**.

### **Accelerometer damping ratio** — Accelerometer damping ratio `0.707` (default) | real, double scalar

Damping ratio of the accelerometer, specified as a real, double scalar, with no
dimensions.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `z_a` |
| **Type**: character vector |
| **Values**: real, double scalar |
| **Default**: `'0.707'` |

#### Dependencies

To enable this parameter, select **Second order dynamics for
accelerometer**.

### **Accelerometer scale factor and cross-coupling** — Scale factor and cross coupling `[1 0 0; 0 1 0; 0 0 1]` (default) | 3-by-3 matrix

Scale factor and cross-coupling, specified as a 3-by-3 matrix, to skew the
accelerometer from body axes and to scale accelerations along body axes.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `a_sf_cc` |
| **Type**: character vector |
| **Values**: 3-by-3 matrix |
| **Default**: `'[1 0 0; 0 1 0; 0 0 1]'` |

### **Accelerometer measurement bias** — Accelerometer measurement bias `[0 0 0]` (default) | three-element vector

Long-term biases along the accelerometer axes, specified as a three-element vector,
in selected acceleration units.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `a_bias` |
| **Type**: character vector |
| **Values**: three-element vector |
| **Default**: `'[0 0 0]'` |

### **Accelerometer upper and lower limits** — Minimum and maximum values of acceleration `[-inf -inf -inf inf inf inf]` (default) | six-element vector

Three minimum values and three maximum values of acceleration in each of
accelerometer axes, specified as a six-element vector, in selected acceleration
units.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `a_sat` |
| **Type**: character vector |
| **Values**: six-element vector |
| **Default**: `'[-inf -inf -inf inf inf inf]'` |

#### Gyroscope

### **Second-order dynamics for gyro** — Gyroscope second-order dynamics `on` (default) | `off`

To apply second-order dynamics to gyroscope readings, select this check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `dtype_g` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'on'` |

### **Gyro natural frequency (rad/sec)** — Gyroscope natural frequency `190` (default) | real, double scalar

Natural frequency of the gyroscope, specified as a real, double scalar, in radians
per second.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `w_g` |
| **Type**: character vector |
| **Values**: real, double scalar |
| **Default**: `'190'` |

#### Dependencies

To enable this parameter, select **Second-order dynamics for
gyro**.

### **Gyro damping ratio** — Gyroscope damping ratio `0.707` (default) | real, double scalar

Damping ratio of the gyroscope, specified as a real, double scalar, with no
dimensions.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `z_g` |
| **Type**: character vector |
| **Values**: real, double scalar |
| **Default**: `'0.707'` |

#### Dependencies

To enable this parameter, select **Second-order dynamics for
gyro**.

### **Gyro scale factors and cross-coupling** — Gyroscope scale factors and cross-coupling `[1 0 0; 0 1 0; 0 0 1]` (default) | 3-by-3 matrix

Gyroscope scale factors and cross-coupling, specified as a 3-by-3 matrix, to skew
the gyroscope from body axes and to scale angular rates along body axes.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `g_sf_cc` |
| **Type**: character vector |
| **Values**: 3-by-3 matrix |
| **Default**: `'[1 0 0; 0 1 0; 0 0 1]'` |

### **Gyro measurement bias** — Gyroscope measurement bias `[0 0 0]` (default) | three-element vector

Long-term biases along the gyroscope axes, specified as three-element vector, in
radians per second.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `g_bias` |
| **Type**: character vector |
| **Values**: three-element vector |
| **Default**: `'[0 0 0]'` |

### **G-sensitive bias** — Maximum change in rates `[0 0 0]` (default) | three-element vector

Maximum change in rates due to linear acceleration, specified as a three-element
vector, in radians per second per g-unit.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `g_sens` |
| **Type**: character vector |
| **Values**: three-element vector |
| **Default**: `'[0 0 0]'` |

### **Gyro upper and lower limits** — Minimum and maximum values of angular rates `[-inf -inf -inf inf inf inf]` (default) | six-element vector

Three minimum values and three maximum values of angular rates in each of the
gyroscope axes, specified as a six-element vector, in radians per second.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `g_sat` |
| **Type**: character vector |
| **Values**: six-element vector |
| **Default**: `'[-inf -inf -inf inf inf inf]'` |

#### Noise

### **Noise on** — White noise `on` (default) | `off`

To apply white noise to acceleration and gyroscope readings, select this check
box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `a_rand` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'on'` |

### **Noise seeds** — Noise seeds `[23093 23094 23095 23096 23097 23098]` (default) | six-element vector

Scalar seeds for the Gaussian noise generator for each axis of the accelerometer and
gyroscope, specified as a six-element vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `a_seeds` |
| **Type**: character vector |
| **Values**: six-element vector |
| **Default**: `'[23093 23094 23095 23096 23097 23098]'` |

#### Dependencies

To enable this parameter, select **Noise on**.

### **Noise power** — Noise power `[0.001 0.001 0.001 0.0001 0.0001 0.0001]` (default) | six-element vector

Height of the power spectral density (PSD) of the white noise for each axis of the
accelerometer and gyroscope, specified as a six-element vector, in:

- (m/s2)/Hz for `Metric (MKS)`
- (ft/s2)/Hz for `English`

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `a_pow` |
| **Type**: character vector |
| **Values**: six-element vector |
| **Default**: `'[0.001 0.001 0.001 0.0001 0.0001 0.0001]'` |

#### Dependencies

To enable this parameter, select **Noise on**.

## Libraries

Vehicle Dynamics Blockset / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Implement three-axis inertial measurement unit (IMU)

The Three-Axis Inertial Measurement Unit block implements an inertial
measurement unit (IMU) containing a three-axis accelerometer and a three-axis
gyroscope.

For a description of the equations and application of errors, see Three-axis Accelerometer (Aerospace Blockset) and
Three-axis Gyroscope (Aerospace Blockset).
