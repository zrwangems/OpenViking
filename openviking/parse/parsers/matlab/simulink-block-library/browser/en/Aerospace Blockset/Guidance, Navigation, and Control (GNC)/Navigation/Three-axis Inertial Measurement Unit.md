---
type: simulink-block
title: 'Three-axis Inertial Measurement Unit'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Guidance, Navigation, and Control (GNC) / Navigation'
documentation_page: 'threeaxisinertialmeasurementunit'
documentation_source_path: 'threeaxisinertialmeasurementunit.html'
language: en
---

# Three-axis Inertial Measurement Unit

## Ports

### Input

### **Ab** — Actual accelerations three-element vector

Actual accelerations in body-fixed axes, specified as a three-element vector, in the
units specified in the **Units** parameter.

**Data Types:** `double`

### **ω** — Angular rates three-element vector

Angular rates in body-fixed axes, specified as a three-element vector,
in radians per second.

**Data Types:** `double`

### **dω/dt** — Angular accelerations three-element vector

Angular accelerations in body-fixed axes, specified as a three-element
vector, in radians per second squared.

**Data Types:** `double`

### **CG** — Location of center of gravity three-element vector

Location of the center of gravity, specified as a three-element vector, in the units
specified in the **Units** parameter.

**Data Types:** `double`

### **g** — Gravity three-element vector

Gravity in body axis, specified as a three-element vector, in the units specified in the
**Units** parameter.

**Data Types:** `double`
### Output

### **Ameas** — Measured accelerations three-element vector

Measured accelerations from the accelerometer, returned as a three-element vector, in
the units specified in the **Units** parameter.

**Data Types:** `double`

### **ωmeas** — Measured angular rates three-element vector

Measured angular rates from the gyroscope, returned as a three-element vector, in
radians per second.

**Data Types:** `double`

## Parameters

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

The location of the IMU, which is also the accelerometer group location, is measured from
the zero datum (typically the nose) to aft, to the right of the vertical
centerline, and above the horizontal centerline. This measurement reference
is the same for the center of gravity input. The units are in the units
specified in the **Units** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `imu` |
| **Type**: character vector |
| **Values**: three-element vector |
| **Default**: `'[0 0 0]'` |

### **Update rate (sec)** — Update rate `0` (default) | scalar

Update rate of the accelerometer and gyroscope, specified as a double scalar, in seconds.
An update rate of 0 creates a continuous accelerometer and continuous
gyroscope. If the **Noise on** check box is selected and
the update rate is 0, the block updates the noise at a rate of 0.1.

**Tip**

If you:

- Update this parameter value to 0 (continuous)
- Configure a fixed-step solver for the model

you must also select the **Automatically handle rate
transition for data transfer** check box in the
**Solver** pane. This check box enables the
software to handle rate transitions correctly.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `i_Ts` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'0'` |

### **Second-order dynamics for accelerometer** — Second-order dynamics `on` (default) | `off`

To apply second-order dynamics to acceleration readings, select this check
box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `dtype_a` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'on'` |

### **Accelerometer natural frequency (rad/sec)** — Accelerometer natural frequency `190` (default) | scalar

Natural frequency of the accelerometer, specified as a double scalar, in radians per
second.

#### Dependencies

To enable this parameter, select **Second order dynamics for
accelerometer**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `w_a` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'190'` |

### **Accelerometer damping ratio** — Accelerometer damping ratio `0.707` (default) | scalar

Damping ratio of the accelerometer, specified as a double scalar, with no
dimensions.

#### Dependencies

To enable this parameter, select **Second order dynamics for
accelerometer**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `z_a` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'0.707'` |

### **Accelerometer scale factor and cross-coupling** — Scale factors and cross coupling `[1 0 0; 0 1 0; 0 0 1]` (default) | 3-by-3 matrix

Scale factors and cross-coupling, specified as a 3-by-3 matrix, to skew
the accelerometer from body axes and to scale accelerations along body
axes.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `a_sf_cc` |
| **Type**: character vector |
| **Values**: 3-by-3 matrix |
| **Default**: `'[1 0 0; 0 1 0; 0 0 1]'` |

### **Accelerometer measurement bias** — Accelerometer measurement bias `[0 0 0]` (default) | three-element vector

Long-term biases along the accelerometer axes, specified as a three-element vector, in
the units specified in the **Units** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `a_bias` |
| **Type**: character vector |
| **Values**: three-element vector |
| **Default**: `'[0 0 0]'` |

### **Accelerometer upper and lower limits** — Minimum and maximum values of acceleration `[-inf -inf -inf inf inf inf]` (default) | six-element vector

Three minimum values and three maximum values of acceleration in each of accelerometer
axes, specified as a six-element vector, in units specified in the
**Units** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `a_sat` |
| **Type**: character vector |
| **Values**: six-element vector |
| **Default**: `'[-inf -inf -inf inf inf inf]'` |

### **Second-order dynamics for gyro** — Gyroscope second-order dynamics `on` (default) | `off`

To apply second-order dynamics to gyroscope readings, select this check
box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `dtype_g` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'on'` |

### **Gyro natural frequency (rad/sec)** — Gyroscope natural frequency `190` (default) | scalar

Natural frequency of the gyroscope, specified as a double scalar, in radians per
second.

#### Dependencies

To enable this parameter, select **Second-order dynamics for
gyro**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `w_g` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'190'` |

### **Gyro damping ratio** — Gyroscope damping ratio `0.707` (default) | scalar

Damping ratio of the gyroscope, specified as a double scalar.

#### Dependencies

To enable this parameter, select **Second-order dynamics for
gyro**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `z_g` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'0.707'` |

### **Gyro scale factors and cross-coupling** — Gyroscope scale factors and cross-coupling `[1 0 0; 0 1 0; 0 0 1]` (default) | 3-by-3 matrix

Gyroscope scale factors and cross-coupling, specified as a 3-by-3 matrix,
to skew the gyroscope from body axes and to scale angular rates along body
axes.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `g_sf_cc` |
| **Type**: character vector |
| **Values**: 3-by-3 matrix |
| **Default**: `'[1 0 0; 0 1 0; 0 0 1]'` |

### **Gyro measurement bias** — Gyroscope measurement bias `[0 0 0]` (default) | three-element vector

Long-term biases along the gyroscope axes, specified a three-element
vector, in radians per second.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `g_bias` |
| **Type**: character vector |
| **Values**: three-element vector |
| **Default**: `'[0 0 0]'` |

### **G-sensitive bias** — Maximum change in rates `[0 0 0]` (default) | three-element vector

Maximum change in rates due to linear acceleration, specified as a
three-element vector, in radians per second per g-unit.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `g_sens` |
| **Type**: character vector |
| **Values**: three-element vector |
| **Default**: `'[0 0 0]'` |

### **Gyro upper and lower limits** — Minimum and maximum values of angular rates `[-inf -inf -inf inf inf inf]` (default) | six-element vector

Three minimum values and three maximum values of angular rates in each of
the gyroscope axes, specified as a six-element vector, in radians per
second.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `g_sat` |
| **Type**: character vector |
| **Values**: six-element vector |
| **Default**: `'[-inf -inf -inf inf inf inf]'` |

### **Noise on** — White noise `on` (default) | `off`

To apply white noise to acceleration and gyroscope readings, select this
check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `i_rand` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'on'` |

### **Noise seeds** — Noise seeds `[23093 23094 23095 23096 23097 23098]` (default) | six-element vector

Scalar seeds for the Gaussian noise generator for each axis of the
accelerometer and gyroscope, specified as a six-element vector.

#### Dependencies

To enable this parameter, select **Noise on**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `i_seeds` |
| **Type**: character vector |
| **Values**: six-element vector |
| **Default**: `'[23093 23094 23095 23096 23097 23098]'` |

### **Noise power** — Noise power `[0.001 0.001 0.001 0.0001 0.0001 0.0001]` (default) | six-element vector

Height of the power spectral density (PSD) of the white noise for each
axis of the accelerometer and gyroscope, specified as a six-element vector,
in:

- (m/s2)/Hz when
  **Units** is set to `Metric
  (MKS)`
- (ft/s2)/Hz when
  **Units** is set to
  `English`

#### Dependencies

To enable this parameter, select **Noise on**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `i_pow` |
| **Type**: character vector |
| **Values**: six-element vector |
| **Default**: `'[0.001 0.001 0.001 0.0001 0.0001 0.0001]'` |

## Libraries

Aerospace Blockset / GNC / Navigation

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Implement three-axis inertial measurement unit (IMU)

The Three-Axis Inertial Measurement Unit block implements an
inertial measurement unit (IMU) containing a three-axis accelerometer and a three-axis
gyroscope.

For a description of the equations and application of errors, see Three-axis Accelerometer and Three-axis Gyroscope.

The Three-axis Inertial Measurement Unit block icon displays the input
and output units selected from the **Units** parameter.
