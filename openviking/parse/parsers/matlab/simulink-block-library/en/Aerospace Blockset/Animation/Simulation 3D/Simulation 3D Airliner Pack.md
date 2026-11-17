---
type: simulink-block
title: 'Simulation 3D Airliner Pack'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation / Simulation 3D'
documentation_page: 'simulation3dairlinerpack'
documentation_source_path: 'simulation3dairlinerpack.html'
language: en
---

# Simulation 3D Airliner Pack

## Ports
```yaml
ports:
- name: Body_T
  summary: Body translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Body_R
  summary: Body rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Left_Engine_R
  summary: Left engine rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Right_Engine_R
  summary: Right engine rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Rudder_R
  summary: Rudder rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Elevator_R
  summary: Elevator rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Left_Aileron_R
  summary: Left aileron rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Right_Aileron_R
  summary: Right aileron rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Flaps_R
  summary: Flaps rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Nose_Wheel_Strut_R
  summary: Nose wheel strut rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Nose_Wheel_R
  summary: Nose wheel rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Left_Wheel_R
  summary: Left wheel rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Right_Wheel_R
  summary: Right wheel rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Translation
  summary: Aircraft translation 12-by-3 array
  direction: output
- name: Rotation
  summary: Aircraft and wheel rotation 12-by-3 array
  direction: output
```

### Input

### **Body\_T** — Body translation 1-by-3 matrix

Body translation, specified as a 1-by-3 matrix.

**Data Types:** `single` | `double`

### **Body\_R** — Body rotation 1-by-3 matrix

Body rotation, specified as a 1-by-3 matrix.

**Data Types:** `single` | `double`

### **Left\_Engine\_R** — Left engine rotation 1-by-3 matrix

Left engine rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Left engine rotation**
parameter.

**Data Types:** `single` | `double`

### **Right\_Engine\_R** — Right engine rotation 1-by-3 matrix

Right engine rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Right engine rotation**
parameter.

**Data Types:** `single` | `double`

### **Rudder\_R** — Rudder rotation 1-by-3 matrix

Rudder rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Rudder rotation** parameter.

**Data Types:** `single` | `double`

### **Elevator\_R** — Elevator rotation 1-by-3 matrix

Elevator rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Elevator rotation** parameter.

**Data Types:** `single` | `double`

### **Left\_Aileron\_R** — Left aileron rotation 1-by-3 matrix

Left aileron rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Left aileron rotation** parameter.

**Data Types:** `single` | `double`

### **Right\_Aileron\_R** — Right aileron rotation 1-by-3 matrix

Right aileron rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Right aileron rotation** parameter.

**Data Types:** `single` | `double`

### **Flaps\_R** — Flaps rotation 1-by-3 matrix

Flaps rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Flaps rotation** parameter.

**Data Types:** `single` | `double`

### **Nose\_Wheel\_Strut\_R** — Nose wheel strut rotation 1-by-3 matrix

Nose wheel strut rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Nose wheel strut rotation**
parameter.

**Data Types:** `single` | `double`

### **Nose\_Wheel\_R** — Nose wheel rotation 1-by-3 matrix

Nose wheel rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Nose wheel rotation** parameter.

**Data Types:** `single` | `double`

### **Left\_Wheel\_R** — Left wheel rotation 1-by-3 matrix

Left wheel rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Left wheel rotation** parameter.

**Data Types:** `single` | `double`

### **Right\_Wheel\_R** — Right wheel rotation 1-by-3 matrix

Right wheel rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Right wheel rotation**
parameter.

**Data Types:** `single` | `double`
### Output

### **Translation** — Aircraft translation `12`-by-`3` array

Aircraft translation for generic airliner aircraft, returned as a
`12`-by-`3` array. The signal contains translation
[*X*, *Y*, *Z*], in meters, with
one row of the array for each bone of the aircraft.

The translation applies to these bones of the `Airliner`
type.

| Bone | Index |
| --- | --- |
| BODY | 1 |
| LEFT\_ENGINE | 2 |
| RIGHT\_ENGINE | 3 |
| RUDDER | 4 |
| ELEVATOR | 5 |
| LEFT\_AILERON | 6 |
| RIGHT\_AILERON | 7 |
| FLAPS | 8 |
| NOSE\_WHEEL\_STRUT | 9 |
| NOSE\_WHEEL | 10 |
| LEFT\_WHEEL | 11 |
| RIGHT\_WHEEL | 12 |

### **Rotation** — Aircraft and wheel rotation `12`-by-`3` array

Aircraft and wheel rotation for generic airliner, returned as a
`12`-by-`3` array.

The rotation applies to the same bones as listed for the Translation port.

The signal contains the rotation [roll, pitch, yaw], in radians, with one row of
the array for each bone of the aircraft.
## Parameters
```yaml
parameters:
- name: Left engine rotation
  summary: Option to enable Left_Engine_R input port off (default) | on
  group: Propulsion
  block_parameter: Left_Engine_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right engine rotation
  summary: Option to enable Right_Engine_R input port off (default) | on
  group: Propulsion
  block_parameter: Right_Engine_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Rudder rotation
  summary: Option to enable Rudder_R input port off (default) | on
  group: Controls
  block_parameter: Rudder_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Elevator rotation
  summary: Option to enable Elevator_R input port off (default) | on
  group: Controls
  block_parameter: Elevator_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left aileron rotation
  summary: Option to enable Left_Aileron_R input port off (default) | on
  group: Controls
  block_parameter: Left_Aileron_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right aileron rotation
  summary: Option to enable Right_Aileron_R input port off (default) | on
  group: Controls
  block_parameter: Right_Aileron_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Flaps rotation
  summary: Option to enable Flaps_R input port off (default) | on
  group: Controls
  block_parameter: Flaps_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Nose wheel strut rotation
  summary: Option to enable Nose_Wheel_Strut_R input port off (default) | on
  group: Gear
  block_parameter: Nose_Wheel_Strut_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Nose wheel rotation
  summary: Option to enable Nose_Wheel_R input port off (default) | on
  group: Gear
  block_parameter: Nose_Wheel_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left wheel rotation
  summary: Option to enable Left_Wheel_R input port off (default) | on
  group: Gear
  block_parameter: Left_Wheel_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right wheel rotation
  summary: Option to enable Right_Wheel_R input port off (default) | on
  group: Gear
  block_parameter: Right_Wheel_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Select input coordinate frame
  summary: Input coordinate frame NED (default) | Fixed-frame | ICRF
  group: Input
  block_parameter: GeoRadioButton
  values: '''NED'' (default) | ''Fixed-frame'' | ''ICRF'''
```

### Propulsion

### **Left engine rotation** — Option to enable Left\_Engine\_R input port `off` (default) | `on`

Select this parameter to enable the **Left\_Engine\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Left_Engine_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Right engine rotation** — Option to enable Right\_Engine\_R input port `off` (default) | `on`

Select this parameter to enable the **Right\_Engine\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Right_Engine_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### Controls

### **Rudder rotation** — Option to enable Rudder\_R input port `off` (default) | `on`

Select this parameter to enable the **Rudder\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Rudder_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Elevator rotation** — Option to enable Elevator\_R input port `off` (default) | `on`

Select this parameter to enable the **Elevator\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Elevator_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Left aileron rotation** — Option to enable Left\_Aileron\_R input port `off` (default) | `on`

Select this parameter to enable the **Left\_Aileron\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Left_Aileron_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Right aileron rotation** — Option to enable Right\_Aileron\_R input port `off` (default) | `on`

Select this parameter to enable the **Right\_Aileron\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Right_Aileron_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Flaps rotation** — Option to enable Flaps\_R input port `off` (default) | `on`

Select this parameter to enable the **Flaps\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Flaps_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### Gear

### **Nose wheel strut rotation** — Option to enable Nose\_Wheel\_Strut\_R input port `off` (default) | `on`

Select this parameter to enable the **Nose\_Wheel\_Strut\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Nose_Wheel_Strut_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Nose wheel rotation** — Option to enable Nose\_Wheel\_R input port `off` (default) | `on`

Select this parameter to enable the **Nose\_Wheel\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Nose_Wheel_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Left wheel rotation** — Option to enable Left\_Wheel\_R input port `off` (default) | `on`

Select this parameter to enable the **Left\_Wheel\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Left_Wheel_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Right wheel rotation** — Option to enable Right\_Wheel\_R input port `off` (default) | `on`

Select this parameter to enable the **Right\_Wheel\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Right_Wheel_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### Input

### **Select input coordinate frame** — Input coordinate frame `NED` (default) | `Fixed-frame` | `ICRF`

Select the input coordinate frame to position aerospace vehicles with respect to
north-east-down (NED), fixed-frame (Fixed-frame), or International Celestial Reference
Frame (ICRF).

If the model contains an associated Simulation 3D Scene
Configuration block, Simulation 3D Airliner Pack block uses the coordinate
frame of the Simulation 3D Scene Configuration. In this case, the
**Select input coordinate frame** might be disabled. For more
information about the Simulation 3D Airliner Pack block coordinate frame, see Algorithms.

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

### R2025a: Simulation 3D Airliner Pack block now synchronizes coordinate frame with Simulation 3D Scene Configuration block

The Simulation 3D Airliner Pack block has these changes:

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
  Simulation 3D Airliner Pack might be disabled. In this case, the
  Simulation 3D Airliner Pack synchronizes coordinate systems with the
  Simulation 3D Scene Configuration block.
- The coordinate system displays as an annotation under the block.
- The **Enable geospatial correction** and **Direction of x-axis (degrees clockwise from north)** parameters have been removed.

### R2024a: Simulation 3D Airliner Pack Block Now Supports Earth-centered Earth-fixed (ECEF) Input Coordinate Frame

To enable ECEF coordinate systems for translation input, the Simulation 3D Airliner Pack block
has been updated. Use these parameters with the **Use Earth center as origin
(ECEF)** parameter in the Simulation 3D Scene
Configuration block.

- **Select input coordinate frame**

  - **ECEF** — ECEF input coordinate frame. When you select this coordinate frame, the annotation `Origin: Earth center (ECEF)` appears under the pack block icons.
  - **NED** — NED coordinate frame. Prior to R2024a, NED was the only supported coordinate frame.
- **Direction of x-axis (degrees clockwise from north)** — Direction of the *x*-axis. This parameter is enabled when you select the **Enable geospatial correction** check box.

## Description

Generate translation and rotation information for generic airliner

The Simulation 3D Airliner Pack block creates translation and rotation
information for the Simulation 3D Aircraft block with **Type**
set to `Airliner`. Use the Simulation 3D Airliner Pack
block to provide translation and rotation information to the **Translation**
and **Rotation** input ports of the Simulation 3D Aircraft
block.
