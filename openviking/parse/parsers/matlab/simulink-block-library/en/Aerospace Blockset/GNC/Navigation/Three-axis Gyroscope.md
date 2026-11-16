---
type: simulink-block
title: 'Three-axis Gyroscope'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'GNC / Navigation'
documentation_page: 'threeaxisgyroscope'
documentation_source_path: 'threeaxisgyroscope.html'
language: en
---

# Three-axis Gyroscope

## Ports

### Input

### **ω** — Angular rates three-element vector

Angular rates in the body-fixed axes, specified as a three-element vector, in radians
per second.

**Data Types:** `double`

### **G's** — Accelerations three-element vector

Accelerations in the body-fixed axes, specified as a three-element vector, in Gs.

**Data Types:** `double`
### Output

### **ωmeas** — Measured angular rates three-element vector

Measured angular rates from the gyroscope, returned as a three-element
vector, in radians per second.

**Data Types:** `double`

## Parameters

### **Second order dynamics** — Second-order dynamics `on` (default) | `off`

To apply second-order dynamics to gyroscope readings, select this check
box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `dtype_g` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'on'` |

### **Natural frequency (rad/sec)** — Natural frequency `190` (default) | scalar

Natural frequency of the gyroscope, specified as a double scalar, in radians per
second.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `w_g` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'190'` |

### **Damping ratio** — Damping ratio `0.707` (default) | scalar

Damping ratio of the gyroscope, specified as a double scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `z_g` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'0.707'` |

### **Scale factors and cross-coupling** — Scale factors and cross coupling `[1 0 0; 0 1 0; 0 0 1]` (default) | 3-by-3 matrix

Scale factors and cross-coupling, specified as a 3-by-3 matrix, to skew
the gyroscope from body axes and to scale accelerations along body
axes.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `g_sf_cc` |
| **Type**: character vector |
| **Values**: 3-by-3 matrix |
| **Default**: `'[1 0 0; 0 1 0; 0 0 1]'` |

### **Measurement bias** — Measurement bias `[0 0 0]` (default) | three-element vector

Long-term biases along the gyroscope axes, specified as a three-element
vector, in radians per second.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `g_bias` |
| **Type**: character vector |
| **Values**: 3-by-3 matrix |
| **Default**: `'[0 0 0]'` |

### **G-sensitive bias** — Maximum change in rates `[0 0 0]` (default) | three-element vector

Maximum change in rates due to linear acceleration, specified as a
three-element vector, in radians per second per g-unit.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `g_sen` |
| **Type**: character vector |
| **Values**: three-element vector |
| **Default**: `'[0 0 0]'` |

### **Update rate (sec)** — Update rate `0` (default) | scalar

Update rate of the gyroscope, specified as a double scalar, in seconds. An update rate of
0 creates a continuous gyroscope. If the **Noise on** check
box is selected and the update rate is 0, the block updates the noise at a
rate of 0.1.

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
| **Block Parameter**: `g_Ts` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'0'` |

### **Noise on** — White noise `on` (default) | `off`

To apply white noise to the gyroscope readings, select this check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `g_rand` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'on'` |

### **Noise seeds** — Noise seeds `[23093 23094 23095]` (default) | three-element vector

Scalar seeds for the Gaussian noise generator for each axis of the
gyroscope, specified as a three-element vector.

#### Dependencies

To enable this parameter, select **Noise on**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `g_seeds` |
| **Type**: character vector |
| **Values**: three-element vector |
| **Default**: `'[23093 23094 23095]'` |

### **Noise power** — Noise power `[0.0001 0.0001 0.0001]` (default) | three-element vector

Height of the power spectral density (PSD) of the white noise for each
axis of the gyroscope, specified as a three-element vector, in
(rad/s)2/Hz.

#### Dependencies

To enable this parameter, select **Noise on**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `g_pow` |
| **Type**: character vector |
| **Values**: three-element vector |
| **Default**: `'[0.0001 0.0001 0.0001]'` |

### **Lower and upper output limits** — Minimum and maximum values of angular rates `[-inf -inf -inf inf inf inf]` (default) | six-element vector

Three minimum values and three maximum values of angular rates in each of gyroscope axes,
specified as a six-element vector, in radians per second.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `g_sat` |
| **Type**: character vector |
| **Values**: six-element vector |
| **Default**: `'[-inf -inf -inf inf inf inf]'` |

## Libraries

Aerospace Blockset / GNC / Navigation

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Implement three-axis gyroscope

The Three-Axis Gyroscope block implements a gyroscope on each of the three
axes. For more information on the measured body angular rates, see Algorithms.

Optionally, to apply discretizations to the block inputs and dynamics along with
nonlinearizations of the measured body angular rates, use the Saturation block.
