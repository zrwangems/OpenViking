---
type: simulink-block
title: 'Simulation 3D Helicopter Pack'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation / Simulation 3D'
documentation_page: 'simulation3dhelicopterpack'
documentation_source_path: 'simulation3dhelicopterpack.html'
language: en
---

# Simulation 3D Helicopter Pack

## Ports
```yaml
ports:
- name: Body_T
  summary: Body translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine1_T
  summary: Engine 1 translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine2_T
  summary: Engine 2 translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Rotor1_T
  summary: Rotor 1 translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Rotor2_T
  summary: Rotor 2 translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Nose_Gear_T
  summary: Nose gear translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Nose_Wheel_T
  summary: Nose wheel translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Nose_Gear_Door1_T
  summary: Nose gear door 1 translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Nose_Gear_Door2_T
  summary: Nose gear door 2 translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Left_Gear_T
  summary: Left gear translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Left_Wheel_T
  summary: Left wheel translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Left_Gear_Door1_T
  summary: Left gear door 1 translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Left_Gear_Door2_T
  summary: Left gear door 2 translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Right_Gear_T
  summary: Right gear translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Right_Wheel_T
  summary: Right wheel translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Right_Gear_Door1_T
  summary: Right gear door 1 translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Right_Gear_Door2_T
  summary: Right gear door 2 translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Sensor1_T
  summary: Sensor 1 translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Sensor2_T
  summary: Sensor 2 translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Body_R
  summary: Body rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine1_R
  summary: Engine 1 rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine2_R
  summary: Engine 2 rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Rotor1_R
  summary: Rotor 1 rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Rotor2_R
  summary: Rotor 2 rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Nose_Gear_R
  summary: Nose gear rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Nose_Wheel_R
  summary: Nose wheel rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Nose_Gear_Door1_R
  summary: Nose gear door 1 rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Nose_Gear_Door2_R
  summary: Nose gear door 2 rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Left_Gear_R
  summary: Left gear rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Left_Wheel_R
  summary: Left wheel rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Left_Gear_Door1_R
  summary: Left gear door 1 rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Left_Gear_Door2_R
  summary: Left gear door 2 rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Right_Gear_R
  summary: Right gear rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Right_Wheel_R
  summary: Right wheel rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Right_Gear_Door1_R
  summary: Right gear door 1 rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Right_Gear_Door2_R
  summary: Right gear door 2 rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Sensor1_R
  summary: Sensor 1 rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Sensor2_R
  summary: Sensor 2 rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Translation
  summary: Helicopter translation 19-by-3 array
  direction: output
- name: Rotation
  summary: Rotorcraft rotation 19-by-3 array
  direction: output
```

### Input

### **Body\_T** — Body translation 1-by-3 matrix

Body translation, specified as a 1-by-3 matrix.

**Data Types:** `single` | `double`

### **Engine1\_T** — Engine 1 translation 1-by-3 matrix

Engine 1 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 1 translation**
parameter.

**Data Types:** `single` | `double`

### **Engine2\_T** — Engine 2 translation 1-by-3 matrix

Engine 2 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 2 translation**
parameter.

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

### **Nose\_Gear\_T** — Nose gear translation 1-by-3 matrix

Nose gear translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Nose gear translation** parameter.

**Data Types:** `single` | `double`

### **Nose\_Wheel\_T** — Nose wheel translation 1-by-3 matrix

Nose wheel translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Nose wheel translation** parameter.

**Data Types:** `single` | `double`

### **Nose\_Gear\_Door1\_T** — Nose gear door 1 translation 1-by-3 matrix

Nose gear door 1 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Nose gear door 1
translation** check box.

**Data Types:** `single` | `double`

### **Nose\_Gear\_Door2\_T** — Nose gear door 2 translation 1-by-3 matrix

Nose gear door 2 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Nose gear door 2
translation** check box.

**Data Types:** `single` | `double`

### **Left\_Gear\_T** — Left gear translation 1-by-3 matrix

Left gear translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Left gear translation** parameter.

**Data Types:** `single` | `double`

### **Left\_Wheel\_T** — Left wheel translation 1-by-3 matrix

Left wheel translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Left wheel translation** parameter.

**Data Types:** `single` | `double`

### **Left\_Gear\_Door1\_T** — Left gear door 1 translation 1-by-3 matrix

Left gear door 1 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Left gear door 1
translation** check box.

**Data Types:** `single` | `double`

### **Left\_Gear\_Door2\_T** — Left gear door 2 translation 1-by-3 matrix

Left gear door 2 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Left gear door 2
translation** check box.

**Data Types:** `single` | `double`

### **Right\_Gear\_T** — Right gear translation 1-by-3 matrix

Right gear translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Right gear translation** parameter.

**Data Types:** `single` | `double`

### **Right\_Wheel\_T** — Right wheel translation 1-by-3 matrix

Right wheel translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Right wheel translation** parameter.

**Data Types:** `single` | `double`

### **Right\_Gear\_Door1\_T** — Right gear door 1 translation 1-by-3 matrix

Right gear door 1 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Right gear door 1
translation** check box.

**Data Types:** `single` | `double`

### **Right\_Gear\_Door2\_T** — Right gear door 2 translation 1-by-3 matrix

Right gear door 2 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Right gear door 2
translation** check box.

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

### **Engine1\_R** — Engine 1 rotation 1-by-3 matrix

Engine 1 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 1 rotation**
parameter.

**Data Types:** `single` | `double`

### **Engine2\_R** — Engine 2 rotation 1-by-3 matrix

Engine 2 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 2 rotation**
parameter.

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

### **Nose\_Gear\_R** — Nose gear rotation 1-by-3 matrix

Nose gear rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Nose gear rotation** parameter.

**Data Types:** `single` | `double`

### **Nose\_Wheel\_R** — Nose wheel rotation 1-by-3 matrix

Nose wheel rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Nose wheel rotation** parameter.

**Data Types:** `single` | `double`

### **Nose\_Gear\_Door1\_R** — Nose gear door 1 rotation 1-by-3 matrix

Nose gear door 1 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Nose gear door 1 rotation**
check box.

**Data Types:** `single` | `double`

### **Nose\_Gear\_Door2\_R** — Nose gear door 2 rotation 1-by-3 matrix

Nose gear door 2 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Nose gear door 2 rotation**
check box.

**Data Types:** `single` | `double`

### **Left\_Gear\_R** — Left gear rotation 1-by-3 matrix

Left gear rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Left gear rotation**
parameter.

**Data Types:** `single` | `double`

### **Left\_Wheel\_R** — Left wheel rotation 1-by-3 matrix

Left wheel rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Left wheel rotation** parameter.

**Data Types:** `single` | `double`

### **Left\_Gear\_Door1\_R** — Left gear door 1 rotation 1-by-3 matrix

Left gear door 1 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Left gear door 1 rotation**
check box.

**Data Types:** `single` | `double`

### **Left\_Gear\_Door2\_R** — Left gear door 2 rotation 1-by-3 matrix

Left gear door 2 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Left gear door 2 rotation**
check box.

**Data Types:** `single` | `double`

### **Right\_Gear\_R** — Right gear rotation 1-by-3 matrix

Right gear rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Right gear rotation** parameter.

**Data Types:** `single` | `double`

### **Right\_Wheel\_R** — Right wheel rotation 1-by-3 matrix

Right wheel rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Right wheel rotation**
parameter.

**Data Types:** `single` | `double`

### **Right\_Gear\_Door1\_R** — Right gear door 1 rotation 1-by-3 matrix

Right gear door 1 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Right gear door 1 rotation**
check box.

**Data Types:** `single` | `double`

### **Right\_Gear\_Door2\_R** — Right gear door 2 rotation 1-by-3 matrix

Right gear door 2 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Right gear door 2 rotation**
check box.

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

### **Translation** — Helicopter translation `19`-by-`3` array

Helicopter translation for helicopter rotorcraft, returned as an
`19`-by-`3` array. The signal contains translation
[*X*, *Y*, *Z*], in meters, with
one row of the array for each bone of the rotorcraft.

The translation applies to these bones of the
`Helicopter` type.

| Bone | Index |
| --- | --- |
| BODY | 1 |
| ENGINE1 | 2 |
| ENGINE2 | 3 |
| ROTOR1 | 4 |
| ROTOR2 | 5 |
| NOSE\_GEAR | 6 |
| NOSE\_WHEEL | 7 |
| NOSE\_GEAR\_DOOR1 | 8 |
| NOSE\_GEAR\_DOOR2 | 9 |
| LEFT\_GEAR | 10 |
| LEFT\_WHEEL | 11 |
| LEFT\_GEAR\_DOOR1 | 12 |
| LEFT\_GEAR\_DOOR2 | 13 |
| RIGHT\_GEAR | 14 |
| RIGHT\_WHEEL | 15 |
| RIGHT\_GEAR\_DOOR1 | 16 |
| RIGHT\_GEAR\_DOOR2 | 17 |
| SENSOR1 | 18 |
| SENSOR2 | 19 |

### **Rotation** — Rotorcraft rotation `19`-by-`3` array

Rotorcraft rotation for helicopter rotorcraft, returned as an
`19`-by-`3` array.

The rotation applies to the same bones as listed for the Translation port.

The signal contains the rotation [roll, pitch, yaw], in radians, with one row of
the array for each bone of the rotorcraft.
## Parameters
```yaml
parameters:
- name: Engine 1 translation
  summary: Option to enable Engine1_T input port off (default) | on
  group: Propulsion
  block_parameter: Engine1_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 2 translation
  summary: Option to enable Engine2_T input port off (default) | on
  group: Propulsion
  block_parameter: Engine2_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Rotor 1 translation
  summary: Option to enable Rotor1_T input port off (default) | on
  group: Propulsion
  block_parameter: Rotor1_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Rotor 2 translation
  summary: Option to enable Rotor2_T input port off (default) | on
  group: Propulsion
  block_parameter: Rotor2_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 1 rotation
  summary: Option to enable Engine1_R input port off (default) | on
  group: Propulsion
  block_parameter: Engine1_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 2 rotation
  summary: Option to enable Engine2_R input port off (default) | on
  group: Propulsion
  block_parameter: Engine2_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Rotor 1 rotation
  summary: Option to enable Rotor1_R input port off (default) | on
  group: Propulsion
  block_parameter: Rotor1_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Rotor 2 rotation
  summary: Option to enable Rotor2_R input port off (default) | on
  group: Propulsion
  block_parameter: Rotor2_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Nose gear translation
  summary: Option to enable Nose_Gear_T input port off (default) | on
  group: Gear
  block_parameter: Nose_Gear_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Nose wheel translation
  summary: Option to enable Nose_Wheel_T input port off (default) | on
  group: Gear
  block_parameter: Nose_Wheel_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Nose gear door 1 translation
  summary: Option to enable Nose_Gear_Door1_T input port off (default) | on
  group: Gear
  block_parameter: Nose_Gear_Door1_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Nose gear door 2 translation
  summary: Option to enable Nose_Gear_Door2_T input port off (default) | on
  group: Gear
  block_parameter: Nose_Gear_Door2_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left gear translation
  summary: Option to enable Left_Gear_T input port off (default) | on
  group: Gear
  block_parameter: Left_Gear_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left wheel translation
  summary: Option to enable Left_Wheel_T input port off (default) | on
  group: Gear
  block_parameter: Left_Wheel_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left gear door 1 translation
  summary: Option to enable Left_Gear_Door1_T input port off (default) | on
  group: Gear
  block_parameter: Left_Gear_Door1_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left gear door 2 translation
  summary: Option to enable Left_Gear_Door2_T input port off (default) | on
  group: Gear
  block_parameter: Left_Gear_Door2_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right gear translation
  summary: Option to enable Right_Gear_T input port off (default) | on
  group: Gear
  block_parameter: Right_Gear_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right wheel translation
  summary: Option to enable Right_Wheel_T input port off (default) | on
  group: Gear
  block_parameter: Right_Wheel_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right gear door 1 translation
  summary: Option to enable Right_Gear_Door1_T input port off (default) | on
  group: Gear
  block_parameter: Right_Gear_Door1_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right gear door 2 translation
  summary: Option to enable Right_Gear_Door2_T input port off (default) | on
  group: Gear
  block_parameter: Right_Gear_Door2_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Nose gear rotation
  summary: Option to enable Nose_Gear_R input port off (default) | on
  group: Gear
  block_parameter: Nose_Gear_R
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
- name: Nose gear door 1 rotation
  summary: Option to enable Nose_Gear_Door1_R input port off (default) | on
  group: Gear
  block_parameter: Nose_Gear_Door1_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Nose gear door 2 rotation
  summary: Option to enable Nose_Gear_Door2_R input port off (default) | on
  group: Gear
  block_parameter: Nose_Gear_Door2_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left gear rotation
  summary: Option to enable Left_Gear_R input port off (default) | on
  group: Gear
  block_parameter: Left_Gear_R
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
- name: Left gear door 1 rotation
  summary: Option to enable Left_Gear_Door1_R input port off (default) | on
  group: Gear
  block_parameter: Left_Gear_Door1_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left gear door 2 rotation
  summary: Option to enable Left_Gear_Door2_R input port off (default) | on
  group: Gear
  block_parameter: Left_Gear_Door2_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right gear rotation
  summary: Option to enable Right_Gear_R input port off (default) | on
  group: Gear
  block_parameter: Right_Gear_R
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
- name: Right gear door 1 rotation
  summary: Option to enable Right_Gear_Door1_R input port off (default) | on
  group: Gear
  block_parameter: Right_Gear_Door1_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right gear door 2 rotation
  summary: Option to enable Right_Gear_Door2_R input port off (default) | on
  group: Gear
  block_parameter: Right_Gear_Door2_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Sensor 1 translation
  summary: Option to enable Sensor1_T input port off (default) | on
  group: Sensors
  block_parameter: Sensor1_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Sensor 2 translation
  summary: Option to enable Sensor2_T input port off (default) | on
  group: Sensors
  block_parameter: Sensor2_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Sensor 1 rotation
  summary: Option to enable Sensor1_R input port off (default) | on
  group: Sensors
  block_parameter: Sensor1_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Sensor 2 rotation
  summary: Option to enable Sensor2_R input port off (default) | on
  group: Sensors
  block_parameter: Sensor2_R
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

### **Engine 1 translation** — Option to enable Engine1\_T input port `off` (default) | `on`

Select this parameter to enable the **Engine1\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine1_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 2 translation** — Option to enable Engine2\_T input port `off` (default) | `on`

Select this parameter to enable the **Engine2\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine2_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

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

### **Engine 1 rotation** — Option to enable Engine1\_R input port `off` (default) | `on`

Select this parameter to enable the **Engine1\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine1_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 2 rotation** — Option to enable Engine2\_R input port `off` (default) | `on`

Select this parameter to enable the **Engine2\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine2_R` |
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

### Gear

### **Nose gear translation** — Option to enable Nose\_Gear\_T input port `off` (default) | `on`

Select this parameter to enable the **Nose\_Gear\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Nose_Gear_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Nose wheel translation** — Option to enable Nose\_Wheel\_T input port `off` (default) | `on`

Select this parameter to enable the **Nose\_Wheel\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Nose_Wheel_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Nose gear door 1 translation** — Option to enable Nose\_Gear\_Door1\_T input port `off` (default) | `on`

Select this check box to enable the **Nose\_Gear\_Door1\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Nose_Gear_Door1_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Nose gear door 2 translation** — Option to enable Nose\_Gear\_Door2\_T input port `off` (default) | `on`

Select this check box to enable the **Nose\_Gear\_Door2\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Nose_Gear_Door2_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Left gear translation** — Option to enable Left\_Gear\_T input port `off` (default) | `on`

Select this parameter to enable the **Left\_Gear\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Left_Gear_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Left wheel translation** — Option to enable Left\_Wheel\_T input port `off` (default) | `on`

Select this parameter to enable the **Left\_Wheel\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Left_Wheel_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Left gear door 1 translation** — Option to enable Left\_Gear\_Door1\_T input port `off` (default) | `on`

Select this check box to enable the **Left\_Gear\_Door1\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Left_Gear_Door1_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Left gear door 2 translation** — Option to enable Left\_Gear\_Door2\_T input port `off` (default) | `on`

Select this check box to enable the **Left\_Gear\_Door2\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Left_Gear_Door2_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Right gear translation** — Option to enable Right\_Gear\_T input port `off` (default) | `on`

Select this parameter to enable the **Right\_Gear\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Right_Gear_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Right wheel translation** — Option to enable Right\_Wheel\_T input port `off` (default) | `on`

Select this parameter to enable the **Right\_Wheel\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Right_Wheel_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Right gear door 1 translation** — Option to enable Right\_Gear\_Door1\_T input port `off` (default) | `on`

Select this check box to enable the **Right\_Gear\_Door1\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Right_Gear_Door1_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Right gear door 2 translation** — Option to enable Right\_Gear\_Door2\_T input port `off` (default) | `on`

Select this check box to enable the **Right\_Gear\_Door2\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Right_Gear_Door2_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Nose gear rotation** — Option to enable Nose\_Gear\_R input port `off` (default) | `on`

Select this parameter to enable the **Nose\_Gear\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Nose_Gear_R` |
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

### **Nose gear door 1 rotation** — Option to enable Nose\_Gear\_Door1\_R input port `off` (default) | `on`

Select this check box to enable the **Nose\_Gear\_Door1\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Nose_Gear_Door1_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Nose gear door 2 rotation** — Option to enable Nose\_Gear\_Door2\_R input port `off` (default) | `on`

Select this check box to enable the **Nose\_Gear\_Door2\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Nose_Gear_Door2_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Left gear rotation** — Option to enable Left\_Gear\_R input port `off` (default) | `on`

Select this parameter to enable the **Left\_Gear\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Left_Gear_R` |
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

### **Left gear door 1 rotation** — Option to enable Left\_Gear\_Door1\_R input port `off` (default) | `on`

Select this check box to enable the **Left\_Gear\_Door1\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Left_Gear_Door1_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Left gear door 2 rotation** — Option to enable Left\_Gear\_Door2\_R input port `off` (default) | `on`

Select this check box to enable the **Left\_Gear\_Door2\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Left_Gear_Door2_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Right gear rotation** — Option to enable Right\_Gear\_R input port `off` (default) | `on`

Select this parameter to enable the **Right\_Gear\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Right_Gear_R` |
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

### **Right gear door 1 rotation** — Option to enable Right\_Gear\_Door1\_R input port `off` (default) | `on`

Select this check box to enable the **Right\_Gear\_Door1\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Right_Gear_Door1_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Right gear door 2 rotation** — Option to enable Right\_Gear\_Door2\_R input port `off` (default) | `on`

Select this check box to enable the **Right\_Gear\_Door2\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Right_Gear_Door2_R` |
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
Configuration block, Simulation 3D Helicopter Pack block uses the coordinate
frame of the Simulation 3D Scene Configuration. In this case, the
**Select input coordinate frame** might be disabled. For more
information about the Simulation 3D Helicopter Pack block coordinate frame, see Algorithms.

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

### R2025a: Simulation 3D Helicopter Pack block now synchronizes coordinate frame with Simulation 3D Scene Configuration block

The Simulation 3D Helicopter Pack block has these changes:

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
  Simulation 3D Helicopter Pack might be disabled. In this case, the
  Simulation 3D Helicopter Pack synchronizes coordinate systems with the
  Simulation 3D Scene Configuration block.
- The coordinate system displays as an annotation under the block.
- The **Enable geospatial correction** and **Direction of x-axis (degrees clockwise from north)** parameters have been removed.

### R2024a: Simulation 3D Helicopter Pack Block Now Supports Earth-centered Earth-fixed (ECEF) Input Coordinate Frame

To enable ECEF coordinate systems for translation input, the Simulation 3D Helicopter Pack block
has been updated. Use these parameters with the **Use Earth center as origin
(ECEF)** parameter in the Simulation 3D Scene
Configuration block.

- **Select input coordinate frame**

  - **ECEF** — ECEF input coordinate frame. When you select this coordinate frame, the annotation `Origin: Earth center (ECEF)` appears under the pack block icons.
  - **NED** — NED coordinate frame. Prior to R2024a, NED was the only supported coordinate frame.
- **Direction of x-axis (degrees clockwise from north)** — Direction of the *x*-axis. This parameter is enabled when you select the **Enable geospatial correction** check box.

## Description

Generate translation and rotation information for helicopter

The Simulation 3D Helicopter Pack block creates translation and rotation
information for the Simulation 3D Rotorcraft block with
**Type** set to `Helicopter`. Use the
Simulation 3D Helicopter Pack block to provide translation and rotation
information to the **Translation** and **Rotation** input
ports of the Simulation 3D Rotorcraft block.
