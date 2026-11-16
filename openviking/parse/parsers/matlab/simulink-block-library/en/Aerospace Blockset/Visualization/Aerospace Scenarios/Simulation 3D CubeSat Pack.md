---
type: simulink-block
title: 'Simulation 3D CubeSat Pack'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Visualization / Aerospace Scenarios'
documentation_page: 'simulation3dcubesatpack'
documentation_source_path: 'simulation3dcubesatpack.html'
language: en
---

# Simulation 3D CubeSat Pack

## Ports

### Input

### **Body\_T** — Body translation 1-by-3 matrix

Body translation, specified as a 1-by-3 matrix.

**Data Types:** `single` | `double`

### **Body\_R** — Body rotation 1-by-3 matrix

Body rotation, specified as a 1-by-3 matrix.

**Data Types:** `single` | `double`
### Output

### **Translation** — Spacecraft translation 10-by-3 array

Spacecraft translation for CubeSat, returned as an 10-by-3 array. The signal
contains translation [*X*, *Y*,
*Z*], in meters, with one row of the array for each bone of the
spacecraft.

The translation applies to these bones of the `CubeSat`
type.

| Bone | Index |
| --- | --- |
| BODY | 1 |
| ANTENNA1 | 2 |
| ANTENNA2 | 3 |
| ANTENNA3 | 4 |
| SENSOR | 5 |
| SOLAR\_ARRAY1 | 6 |
| SOLAR\_ARRAY1\_1 | 7 |
| SOLAR\_ARRAY2 | 8 |
| SOLAR\_ARRAY2\_2 | 9 |
| THRUSTER | 10 |

### **Rotation** — Spacecraft rotation 10-by-3 array

Spacecraft rotation for CubeSat, returned as an 10-by-3 array.

The rotation applies to the same bones as listed for the Translation port.

The signal contains the rotation [roll, pitch, yaw], in radians, with one row of
the array for each bone of the spacecraft.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Sensors

### **Antenna 1 translation** — Option to enable Antenna1\_T input port `off` (default) | `on`

Select this parameter to enable the **Antenna1\_T** input port.

#### Programmatic Use

To set the block parameter value programmatically, use the `set_param` function.

To get the block parameter value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Antenna1_T` |
| **Values:** | `'off'` (default) | `'on'` |

### **Antenna 1 rotation** — Option to enable Antenna1\_R input port `off` (default) | `on`

Select this parameter to enable the **Antenna1\_R** input port.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Antenna1_R` |
| **Values:** | `'off'` (default) | `'on'` |

### **Antenna 2 translation** — Option to enable Antenna2\_T input port `off` (default) | `on`

Select this parameter to enable the **Antenna2\_T** input port.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Antenna2_T` |
| **Values:** | `'off'` (default) | `'on'` |

### **Antenna 2 rotation** — Option to enable Antenna2\_R input port `off` (default) | `on`

Select this parameter to enable the **Antenna2\_R** input port.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Antenna2_R` |
| **Values:** | `'off'` (default) | `'on'` |

### **Antenna 3 translation** — Option to enable Antenna3\_T input port `off` (default) | `on`

Select this parameter to enable the **Antenna3\_T** input port.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Antenna3_T` |
| **Values:** | `'off'` (default) | `'on'` |

### **Antenna 3 rotation** — Option to enable Antenna3\_R input port `off` (default) | `on`

Select this parameter to enable the **Antenna3\_R** input port.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Antenna3_R` |
| **Values:** | `'off'` (default) | `'on'` |

### **Sensor translation** — Option to enable Sensor\_T input port `off` (default) | `on`

Select this parameter to enable the **Sensor\_T** input port.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Sensor_T` |
| **Values:** | `'off'` (default) | `'on'` |

### **Sensor rotation** — Option to enable Sensor\_R input port `off` (default) | `on`

Select this parameter to enable the **Sensor\_R** input port.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Sensor_R` |
| **Values:** | `'off'` (default) | `'on'` |

### Solar Arrays

### **Solar array 1 translation** — Option to enable SolarArray1\_T input port `off` (default) | `on`

Select this parameter to enable the **SolarArray1\_T** input port.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SolarArray1_T` |
| **Values:** | `'off'` (default) | `'on'` |

### **Solar array 1 rotation** — Option to enable SolarArray1\_R input port `off` (default) | `on`

Select this parameter to enable the **SolarArray1\_R** input port.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SolarArray1_R` |
| **Values:** | `'off'` (default) | `'on'` |

### **Solar array 1.1 translation** — Option to enable SolarArray1\_1\_T input port `off` (default) | `on`

Select this parameter to enable the **SolarArray1\_1\_T** input port.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SolarArray1_1_T` |
| **Values:** | `'off'` (default) | `'on'` |

### **Solar array 1.1 rotation** — Option to enable SolarArray1\_1\_R input port `off` (default) | `on`

Select this parameter to enable the **SolarArray1\_1\_R** input port.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SolarArray1_1_R` |
| **Values:** | `'off'` (default) | `'on'` |

### **Solar array 2 translation** — Option to enable SolarArray2\_T input port `off` (default) | `on`

Select this parameter to enable the **SolarArray2\_T** input port.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SolarArray2_T` |
| **Values:** | `'off'` (default) | `'on'` |

### **Solar array 2 rotation** — Option to enable SolarArray2\_R input port `off` (default) | `on`

Select this parameter to enable the **SolarArray2\_R** input port.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SolarArray2_R` |
| **Values:** | `'off'` (default) | `'on'` |

### **Solar array 2.2 translation** — Option to enable SolarArray2\_2\_T input port `off` (default) | `on`

Select this parameter to enable the **SolarArray2\_2\_T** input port.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SolarArray2_2_T` |
| **Values:** | `'off'` (default) | `'on'` |

### **Solar array 2.2 rotation** — Option to enable SolarArray2\_2\_R input port `off` (default) | `on`

Select this parameter to enable the **SolarArray2\_2\_R** input port.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SolarArray2_2_R` |
| **Values:** | `'off'` (default) | `'on'` |

### Thrusters

### **Thruster translation** — Option to enable Thruster\_T input port `off` (default) | `on`

Select this parameter to enable the **Thruster\_T** input port.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Thruster_T` |
| **Values:** | `'off'` (default) | `'on'` |

### **Thruster rotation** — Option to enable Thruster\_R input port `off` (default) | `on`

Select this parameter to enable the **Thruster\_R** input port.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Thruster_R` |
| **Values:** | `'off'` (default) | `'on'` |

### Input

### **Select input coordinate frame** — Input coordinate frame `NED` (default) | `Fixed-frame` | `ICRF`

Select the input coordinate frame to position aerospace vehicles with respect to
north-east-down (NED), fixed-frame (Fixed-frame), or International Celestial Reference
Frame (ICRF).

If the model contains an associated Simulation 3D Scene
Configuration block, Simulation 3D CubeSat Pack block uses the coordinate
frame of the Simulation 3D Scene Configuration. In this case, the
**Select input coordinate frame** might be disabled. For more
information about the Simulation 3D CubeSat Pack block coordinate frame, see Algorithms.

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

**Introduced in R2024a**

### R2025a: Simulation 3D CubeSat Pack block now synchronizes coordinate frame with Simulation 3D Scene Configuration block

The Simulation 3D CubeSat Pack block has these changes:

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
  Simulation 3D CubeSat Pack might be disabled. In this case, the
  Simulation 3D CubeSat Pack synchronizes coordinate systems with the
  Simulation 3D Scene Configuration block.
- The coordinate system displays as an annotation under the block.
- The **Enable geospatial correction** and **Direction of x-axis (degrees clockwise from north)** parameters have been removed.

## Description

Create translation and rotation input matrices for CubeSat

The Simulation 3D CubeSat Pack block creates translation and rotation
information for the Simulation 3D
Spacecraft block with **Type** set to
`CubeSat`. Use the Simulation 3D CubeSat Pack block
to provide translation and rotation information to the **Translation** and
**Rotation** input ports of the Simulation 3D Spacecraft
block.
