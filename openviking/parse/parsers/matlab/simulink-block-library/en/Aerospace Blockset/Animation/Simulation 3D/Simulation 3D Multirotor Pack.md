---
type: simulink-block
title: 'Simulation 3D Multirotor Pack'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation / Simulation 3D'
documentation_page: 'simulation3dmultirotorpack'
documentation_source_path: 'simulation3dmultirotorpack.html'
language: en
---

# Simulation 3D Multirotor Pack

## Ports

### Input

### **Body\_T** — Body translation 1-by-3 matrix

Body translation, specified as a 1-by-3 matrix.

**Data Types:** `single` | `double`

### **Rotor1\_T** — Rotor 1 translation 1-by-3 matrix

Rotor 1 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Rotor 1 translation** parameter.

**Data Types:** `single` | `double`

### **Rotor2\_T** — Rotor 2 translation 1-by-3 matrix

Rotor 2 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Rotor 2 translation** parameter.

**Data Types:** `single` | `double`

### **Rotor3\_T** — Rotor 3 translation 1-by-3 matrix

Rotor 3 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Rotor 3 translation** parameter.

**Data Types:** `single` | `double`

### **Rotor4\_T** — Rotor 4 translation 1-by-3 matrix

Rotor 4 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Rotor 4 translation** parameter.

**Data Types:** `single` | `double`

### **Rotor5\_T** — Rotor 5 translation 1-by-3 matrix

Rotor 5 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Rotor 5 translation** parameter.

**Data Types:** `single` | `double`

### **Rotor6\_T** — Rotor 6 translation 1-by-3 matrix

Rotor 6 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Rotor 6 translation** parameter.

**Data Types:** `single` | `double`

### **Rotor7\_T** — Rotor 7 translation 1-by-3 matrix

Rotor 7 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Rotor 7 translation** parameter.

**Data Types:** `single` | `double`

### **Rotor8\_T** — Rotor 8 translation 1-by-3 matrix

Rotor 8 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Rotor 8 translation** parameter.

**Data Types:** `single` | `double`

### **Sensor1\_T** — Sensor 1 translation 1-by-3 matrix

Sensor 1 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Sensor 1 translation**
parameter.

**Data Types:** `single` | `double`

### **Sensor2\_T** — Sensor 2 translation 1-by-3 matrix

Sensor 2 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Sensor 2 translation**
parameter.

**Data Types:** `single` | `double`

### **Body\_R** — Body rotation 1-by-3 matrix

Body rotation, specified as a 1-by-3 matrix.

**Data Types:** `single` | `double`

### **Rotor1\_R** — Rotor 1 rotation 1-by-3 matrix

Rotor 1 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Rotor 1 rotation** parameter.

**Data Types:** `single` | `double`

### **Rotor2\_R** — Rotor 2 rotation 1-by-3 matrix

Rotor 2 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Rotor 2 rotation** parameter.

**Data Types:** `single` | `double`

### **Rotor3\_R** — Rotor 3 rotation 1-by-3 matrix

Rotor 3 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Rotor 3 rotation** parameter.

**Data Types:** `single` | `double`

### **Rotor4\_R** — Rotor 4 rotation 1-by-3 matrix

Rotor 4 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Rotor 4 rotation** parameter.

**Data Types:** `single` | `double`

### **Rotor5\_R** — Rotor 5 rotation 1-by-3 matrix

Rotor 5 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Rotor 5 rotation** parameter.

**Data Types:** `single` | `double`

### **Rotor6\_R** — Rotor 6 rotation 1-by-3 matrix

Rotor 6 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Rotor 6 rotation** parameter.

**Data Types:** `single` | `double`

### **Rotor7\_R** — Rotor 7 rotation 1-by-3 matrix

Rotor 7 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Rotor 7 rotation** parameter.

**Data Types:** `single` | `double`

### **Rotor8\_R** — Rotor 8 rotation 1-by-3 matrix

Rotor 8 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Rotor 8 rotation** parameter.

**Data Types:** `single` | `double`

### **Sensor1\_R** — Sensor 1 rotation 1-by-3 matrix

Sensor 1 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Sensor 1 rotation**
parameter.

**Data Types:** `single` | `double`

### **Sensor2\_R** — Sensor 2 rotation 1-by-3 matrix

Sensor 2 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Sensor 2 rotation** parameter.

**Data Types:** `single` | `double`
### Output

### **Translation** — Multirotor translation `11`-by-`3` array

Rotorcraft translation for multirotor, returned as an
`11`-by-`3` array. The signal contains translation
[*X*, *Y*, *Z*], in meters, with
one row of the array for each bone of the rotorcraft.

The translation applies to these bones of the
`Multirotor` type.

| Bone | Index |
| --- | --- |
| BODY | 1 |
| ROTOR1 | 2 |
| ROTOR2 | 3 |
| ROTOR3 | 4 |
| ROTOR4 | 5 |
| ROTOR5 | 6 |
| ROTOR6 | 7 |
| ROTOR7 | 8 |
| ROTOR8 | 9 |
| SENSOR1 | 10 |
| SENSOR2 | 11 |

### **Rotation** — Rotorcraft rotation `11`-by-`3` array

Rotorcraft rotation for multirotor, returned as an
`11`-by-`3` array:

The rotation applies to the same bones as listed for the Translation port.

The signal contains the rotation [roll, pitch, yaw], in radians, with one row of
the array for each bone of the rotorcraft.

## Parameters

### Propulsion

### **Rotor 1 translation** — Option to enable Rotor1\_T input port `off` (default) | `on`

Select this parameter to enable the **Rotor1\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Rotor1_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Rotor 2 translation** — Option to enable Rotor2\_T input port `off` (default) | `on`

Select this parameter to enable the **Rotor2\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Rotor2_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Rotor 3 translation** — Option to enable Rotor3\_T input port `off` (default) | `on`

Select this parameter to enable the **Rotor3\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Rotor3_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Rotor 4 translation** — Option to enable Rotor4\_T input port `off` (default) | `on`

Select this parameter to enable the **Rotor4\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Rotor4_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Rotor 5 translation** — Option to enable Rotor5\_T input port `off` (default) | `on`

Select this parameter to enable the **Rotor5\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Rotor5_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Rotor 6 translation** — Option to enable Rotor6\_T input port `off` (default) | `on`

Select this parameter to enable the **Rotor6\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Rotor6_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Rotor 7 translation** — Option to enable Rotor7\_T input port `off` (default) | `on`

Select this parameter to enable the **Rotor7\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Rotor7_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Rotor 8 translation** — Option to enable Rotor8\_T input port `off` (default) | `on`

Select this parameter to enable the **Rotor8\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Rotor8_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Rotor 1 rotation** — Option to enable Rotor1\_R input port `off` (default) | `on`

Select this parameter to enable the **Rotor1\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Rotor1_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Rotor 2 rotation** — Option to enable Rotor2\_R input port `off` (default) | `on`

Select this parameter to enable the **Rotor2\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Rotor2_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Rotor 3 rotation** — Option to enable Rotor3\_R input port `off` (default) | `on`

Select this parameter to enable the **Rotor3\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Rotor3_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Rotor 4 rotation** — Option to enable Rotor4\_R input port `off` (default) | `on`

Select this parameter to enable the **Rotor4\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Rotor4_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Rotor 5 rotation** — Option to enable Rotor5\_R input port `off` (default) | `on`

Select this parameter to enable the **Rotor5\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Rotor5_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Rotor 6 rotation** — Option to enable Rotor6\_R input port `off` (default) | `on`

Select this parameter to enable the **Rotor6\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Rotor6_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Rotor 7 rotation** — Option to enable Rotor7\_R input port `off` (default) | `on`

Select this parameter to enable the **Rotor7\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Rotor7_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Rotor 8 rotation** — Option to enable Rotor8\_R input port `off` (default) | `on`

Select this parameter to enable the **Rotor8\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Rotor8_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### Sensors

### **Sensor 1 translation** — Option to enable Sensor1\_T input port `off` (default) | `on`

Select this parameter to enable the **Sensor1\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Sensor1_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Sensor 2 translation** — Option to enable Sensor2\_T input port `off` (default) | `on`

Select this parameter to enable the **Sensor2\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Sensor2_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Sensor 1 rotation** — Option to enable Sensor1\_R input port `off` (default) | `on`

Select this parameter to enable the **Sensor1\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Sensor1_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Sensor 2 rotation** — Option to enable Sensor2\_R input port `off` (default) | `on`

Select this parameter to enable the **Sensor2\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Sensor2_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### Input

### **Select input coordinate frame** — Input coordinate frame `NED` (default) | `Fixed-frame` | `ICRF`

Select the input coordinate frame to position aerospace vehicles with respect to
north-east-down (NED), fixed-frame (Fixed-frame), or International Celestial Reference
Frame (ICRF).

If the model contains an associated Simulation 3D Scene
Configuration block, Simulation 3D Multirotor Pack block uses the coordinate
frame of the Simulation 3D Scene Configuration. In this case, the
**Select input coordinate frame** might be disabled. For more
information about the Simulation 3D Multirotor Pack block coordinate frame, see Algorithms.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `GeoRadioButton` |
| **Values:** | `'NED'` (default) | `'Fixed-frame'` | `'ICRF'` |

## Libraries

Aerospace Blockset / Animation / Simulation 3D

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023b**

### R2025a: Simulation 3D Multirotor Pack block now synchronizes coordinate frame with Simulation 3D Scene Configuration block

The Simulation 3D Multirotor Pack block has these changes:

- The **Geospatial** tab was renamed to **Input** tab.
- On the **Input** tab, the **Select input coordinate frame** pane now contains these coordinate frame buttons:

  - **Fixed-frame** — Fixed-frame coordinate frame. When
    you select this coordinate frame, the annotation
    `Fixed-frame` appears under the pack block
    icons.
  - **ICRF** — International Celestial Reference Frame coordinate frame. When you select this coordinate frame, the annotation `ICRF` appears under the pack block icons.
  - **NED** — North-east-down coordinate frame. When you select this coordinate frame, the annotation `NED` appears under the pack block icons.

  If a model contains a Simulation 3D pack block and an associated Simulation 3D Scene
  Configuration block, the **Input** tab options of
  Simulation 3D Multirotor Pack might be disabled. In this case, the
  Simulation 3D Multirotor Pack synchronizes coordinate systems with the
  Simulation 3D Scene Configuration block.
- The coordinate system displays as an annotation under the block.
- The **Enable geospatial correction** and **Direction of x-axis (degrees clockwise from north)** parameters have been removed.

### R2024a: Simulation 3D Multirotor Pack Block Now Supports Earth-centered Earth-fixed (ECEF) Input Coordinate Frame

To enable ECEF coordinate systems for translation input, the Simulation 3D Multirotor Pack block
has been updated. Use these parameters with the **Use Earth center as origin
(ECEF)** parameter in the Simulation 3D Scene
Configuration block.

- **Select input coordinate frame**

  - **ECEF** — ECEF input coordinate frame. When you select this coordinate frame, the annotation `Origin: Earth center (ECEF)` appears under the pack block icons.
  - **NED** — NED coordinate frame. Prior to R2024a, NED was the only supported coordinate frame.
- **Direction of x-axis (degrees clockwise from north)** — Direction of the *x*-axis. This parameter is enabled when you select the **Enable geospatial correction** check box.

## Description

Generate translation and rotation information for multirotor rotorcraft

The Simulation 3D Multirotor Pack block creates translation and rotation
information for the Simulation 3D Rotorcraft block with
**Type** set to `Multirotor`. Use the
Simulation 3D Multirotor Pack block to provide translation and rotation
information to the **Translation** and **Rotation** input
ports of the Simulation 3D Rotorcraft block.
