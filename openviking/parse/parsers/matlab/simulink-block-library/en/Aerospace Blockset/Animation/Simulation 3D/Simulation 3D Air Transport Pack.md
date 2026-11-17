---
type: simulink-block
title: 'Simulation 3D Air Transport Pack'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation / Simulation 3D'
documentation_page: 'simulation3dairtransportpack'
documentation_source_path: 'simulation3dairtransportpack.html'
language: en
---

# Simulation 3D Air Transport Pack

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
- name: Engine3_T
  summary: Engine 3 translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine4_T
  summary: Engine 4 translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Rudder_T
  summary: Rudder translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Elevator_T
  summary: Elevator translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Horizontal_Stab_T
  summary: Horizontal stab translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Left_Aileron_T
  summary: Left aileron translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Right_Aileron_T
  summary: Right aileron translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Flaps1_T
  summary: Flaps set 1 translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Flaps2_T
  summary: Flaps set 2 translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Left_Spoiler_T
  summary: Left spoiler translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Right_Spoiler_T
  summary: Right spoiler translation 1-by-3 matrix
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
- name: Left_Gear_Link_T
  summary: Left gear link translation 1-by-3 matrix
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
- name: Left_Gear_Door2_2_T
  summary: Left gear door 2.2 translation 1-by-3 matrix
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
- name: Right_Gear_Link_T
  summary: Right gear link translation 1-by-3 matrix
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
- name: Right_Gear_Door2_2_T
  summary: Right gear door 2.2 translation 1-by-3 matrix
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
- name: Engine3_R
  summary: Engine 3 rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine4_R
  summary: Engine 4 rotation 1-by-3 matrix
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
- name: Horizontal_Stab_R
  summary: Horizontal stab rotation 1-by-3 matrix
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
- name: Flaps1_R
  summary: Flaps set 1 rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Flaps2_R
  summary: Flaps set 2 rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Left_Spoiler_R
  summary: Left spoiler rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Right_Spoiler_R
  summary: Right spoiler rotation 1-by-3 matrix
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
- name: Left_Gear_Link_R
  summary: Left gear link rotation 1-by-3 matrix
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
- name: Left_Gear_Door2_2_R
  summary: Left gear door 2.2 rotation 1-by-3 matrix
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
- name: Right_Gear_Link_R
  summary: Right gear link rotation 1-by-3 matrix
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
- name: Right_Gear_Door2_2_R
  summary: Right gear door 2.2 rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Translation
  summary: Aircraft translation 30-by-3 array
  direction: output
- name: Rotation
  summary: Aircraft rotation 30-by-3 array
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

### **Engine3\_T** — Engine 3 translation 1-by-3 matrix

Engine 3 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 3 translation**
parameter.

**Data Types:** `single` | `double`

### **Engine4\_T** — Engine 4 translation 1-by-3 matrix

Engine 4 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 4 translation**
parameter.

**Data Types:** `single` | `double`

### **Rudder\_T** — Rudder translation 1-by-3 matrix

Rudder translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Rudder translation** parameter.

**Data Types:** `single` | `double`

### **Elevator\_T** — Elevator translation 1-by-3 matrix

Elevator translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Elevator translation** parameter.

**Data Types:** `single` | `double`

### **Horizontal\_Stab\_T** — Horizontal stab translation 1-by-3 matrix

Horizontal stab translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Horizontal stab translation**
parameter.

**Data Types:** `single` | `double`

### **Left\_Aileron\_T** — Left aileron translation 1-by-3 matrix

Left aileron translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Left aileron translation**
parameter.

**Data Types:** `single` | `double`

### **Right\_Aileron\_T** — Right aileron translation 1-by-3 matrix

Right aileron translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Right aileron translation**
parameter.

**Data Types:** `single` | `double`

### **Flaps1\_T** — Flaps set 1 translation 1-by-3 matrix

Flaps set 1 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Flaps set 1 translation**
parameter.

**Data Types:** `single` | `double`

### **Flaps2\_T** — Flaps set 2 translation 1-by-3 matrix

Flaps set 2 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Flaps set 2 translation**
parameter.

**Data Types:** `single` | `double`

### **Left\_Spoiler\_T** — Left spoiler translation 1-by-3 matrix

Left spoiler translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Left spoiler translation**
parameter.

**Data Types:** `single` | `double`

### **Right\_Spoiler\_T** — Right spoiler translation 1-by-3 matrix

Right spoiler translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Right spoiler translation**
parameter.

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
translation** parameter.

**Data Types:** `single` | `double`

### **Nose\_Gear\_Door2\_T** — Nose gear door 2 translation 1-by-3 matrix

Nose gear door 2 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Nose gear door 2
translation** parameter.

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

### **Left\_Gear\_Link\_T** — Left gear link translation 1-by-3 matrix

Left gear link translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Left gear link translation**
parameter.

**Data Types:** `single` | `double`

### **Left\_Gear\_Door1\_T** — Left gear door 1 translation 1-by-3 matrix

Left gear door 1 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Left gear door 1
translation** parameter.

**Data Types:** `single` | `double`

### **Left\_Gear\_Door2\_T** — Left gear door 2 translation 1-by-3 matrix

Left gear door 2 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Left gear door 2
translation** parameter.

**Data Types:** `single` | `double`

### **Left\_Gear\_Door2\_2\_T** — Left gear door 2.2 translation 1-by-3 matrix

Left gear door 2.2 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Left gear door 2.2
translation** parameter.

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

### **Right\_Gear\_Link\_T** — Right gear link translation 1-by-3 matrix

Right gear link translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Right gear link translation**
parameter.

**Data Types:** `single` | `double`

### **Right\_Gear\_Door1\_T** — Right gear door 1 translation 1-by-3 matrix

Right gear door 1 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Right gear door 1
translation** parameter.

**Data Types:** `single` | `double`

### **Right\_Gear\_Door2\_T** — Right gear door 2 translation 1-by-3 matrix

Right gear door 2 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Right gear door 2
translation** parameter.

**Data Types:** `single` | `double`

### **Right\_Gear\_Door2\_2\_T** — Right gear door 2.2 translation 1-by-3 matrix

Right gear door 2.2 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Right gear door 2.2
translation** parameter.

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

### **Engine3\_R** — Engine 3 rotation 1-by-3 matrix

Engine 3 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 3 rotation**
parameter.

**Data Types:** `single` | `double`

### **Engine4\_R** — Engine 4 rotation 1-by-3 matrix

Engine 4 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 4 rotation**
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

### **Horizontal\_Stab\_R** — Horizontal stab rotation 1-by-3 matrix

Horizontal stab rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Horizontal stab rotation**
parameter.

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

### **Flaps1\_R** — Flaps set 1 rotation 1-by-3 matrix

Flaps set 1 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Flaps set 1 rotation**
parameter.

**Data Types:** `single` | `double`

### **Flaps2\_R** — Flaps set 2 rotation 1-by-3 matrix

Flaps set 2 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Flaps set 2 rotation**
parameter.

**Data Types:** `single` | `double`

### **Left\_Spoiler\_R** — Left spoiler rotation 1-by-3 matrix

Left spoiler rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Left spoiler rotation** parameter.

**Data Types:** `single` | `double`

### **Right\_Spoiler\_R** — Right spoiler rotation 1-by-3 matrix

Right spoiler rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Right spoiler rotation** parameter.

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
parameter.

**Data Types:** `single` | `double`

### **Nose\_Gear\_Door2\_R** — Nose gear door 2 rotation 1-by-3 matrix

Nose gear door 2 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Nose gear door 2 rotation**
parameter.

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

### **Left\_Gear\_Link\_R** — Left gear link rotation 1-by-3 matrix

Left gear link rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Left gear link rotation**
parameter.

**Data Types:** `single` | `double`

### **Left\_Gear\_Door1\_R** — Left gear door 1 rotation 1-by-3 matrix

Left gear door 1 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Left gear door 1 rotation**
parameter.

**Data Types:** `single` | `double`

### **Left\_Gear\_Door2\_R** — Left gear door 2 rotation 1-by-3 matrix

Left gear door 2 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Left gear door 2 rotation**
parameter.

**Data Types:** `single` | `double`

### **Left\_Gear\_Door2\_2\_R** — Left gear door 2.2 rotation 1-by-3 matrix

Left gear door 2.2 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Left gear door 2.2 rotation**
parameter.

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

### **Right\_Gear\_Link\_R** — Right gear link rotation 1-by-3 matrix

Right gear link rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Right gear link rotation**
parameter.

**Data Types:** `single` | `double`

### **Right\_Gear\_Door1\_R** — Right gear door 1 rotation 1-by-3 matrix

Right gear door 1 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Right gear door 1 rotation**
parameter.

**Data Types:** `single` | `double`

### **Right\_Gear\_Door2\_R** — Right gear door 2 rotation 1-by-3 matrix

Right gear door 2 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Right gear door 2 rotation**
parameter.

**Data Types:** `single` | `double`

### **Right\_Gear\_Door2\_2\_R** — Right gear door 2.2 rotation 1-by-3 matrix

Right gear door 2.2 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Right gear door 2.2
rotation** parameter.

**Data Types:** `single` | `double`
### Output

### **Translation** — Aircraft translation `30`-by-`3` array

Aircraft translation for air transport aircraft, returned as a
`30`-by-`3` array. The signal contains translation
[*X*, *Y*, *Z*], in meters, with
one row of the array for each bone of the aircraft.

The translation applies to these bones of the `Air
transport` type.

| Bone | Index |
| --- | --- |
| BODY | 1 |
| ENGINE1 | 2 |
| ENGINE2 | 3 |
| ENGINE3 | 4 |
| ENGINE4 | 5 |
| RUDDER | 6 |
| ELEVATOR | 7 |
| HORIZONTAL\_STAB | 8 |
| LEFT\_AILERON | 9 |
| RIGHT\_AILERON | 10 |
| FLAPS1 | 11 |
| FLAPS2 | 12 |
| LEFT\_SPOILER | 13 |
| RIGHT\_SPOILER | 14 |
| NOSE\_GEAR | 15 |
| NOSE\_WHEEL | 16 |
| NOSE\_GEAR\_DOOR1 | 17 |
| NOSE\_GEAR\_DOOR2 | 18 |
| LEFT\_GEAR | 19 |
| LEFT\_WHEEL | 20 |
| LEFT\_GEAR\_LINK | 21 |
| LEFT\_GEAR\_DOOR1 | 22 |
| LEFT\_GEAR\_DOOR2 | 23 |
| LEFT\_GEAR\_DOOR2\_2 | 24 |
| RIGHT\_GEAR | 25 |
| RIGHT\_WHEEL | 26 |
| RIGHT\_GEAR\_LINK | 27 |
| RIGHT\_GEAR\_DOOR1 | 28 |
| RIGHT\_GEAR\_DOOR2 | 29 |
| RIGHT\_GEAR\_DOOR2\_2 | 30 |

### **Rotation** — Aircraft rotation `30`-by-`3` array

Aircraft rotation for air transport aircraft, returned as a
`30`-by-`3` array.

The rotation applies to the same bones as listed for the Translation port.

The signal contains the rotation [roll, pitch, yaw], in radians, with one row of
the array for each bone of the aircraft.
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
- name: Engine 3 translation
  summary: Option to enable Engine3_T input port off (default) | on
  group: Propulsion
  block_parameter: Engine3_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 4 translation
  summary: Option to enable Engine4_T input port off (default) | on
  group: Propulsion
  block_parameter: Engine4_T
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
- name: Engine 3 rotation
  summary: Option to enable Engine3_R input port off (default) | on
  group: Propulsion
  block_parameter: Engine3_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 4 rotation
  summary: Option to enable Engine4_R input port off (default) | on
  group: Propulsion
  block_parameter: Engine4_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Rudder translation
  summary: Option to enable Rudder_T input port off (default) | on
  group: Controls
  block_parameter: Rudder_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Elevator translation
  summary: Option to enable Elevator_T input port off (default) | on
  group: Controls
  block_parameter: Elevator_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Horizontal stab translation
  summary: Option to enable Horizontal_Stab_T input port off (default) | on
  group: Controls
  block_parameter: Horizontal_Stab_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left aileron translation
  summary: Option to enable Left_Aileron_T input port off (default) | on
  group: Controls
  block_parameter: Left_Aileron_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right aileron translation
  summary: Option to enable Right_Aileron_T input port off (default) | on
  group: Controls
  block_parameter: Right_Aileron_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Flaps set 1 translation
  summary: Option to enable Flaps1_T input port off (default) | on
  group: Controls
  block_parameter: Flaps1_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Flaps set 2 translation
  summary: Option to enable Flaps2_T input port off (default) | on
  group: Controls
  block_parameter: Flaps2_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left spoiler translation
  summary: Option to enable Left_Spoiler_T input port off (default) | on
  group: Controls
  block_parameter: Left_Spoiler_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right spoiler translation
  summary: Option to enable Right_Spoiler_T input port off (default) | on
  group: Controls
  block_parameter: Right_Spoiler_T
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
- name: Horizontal stab rotation
  summary: Option to enable Horizontal_Stab_R input port off (default) | on
  group: Controls
  block_parameter: Horizontal_Stab_R
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
- name: Flaps set 1 rotation
  summary: Option to enable Flaps1_R input port off (default) | on
  group: Controls
  block_parameter: Flaps1_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Flaps set 2 rotation
  summary: Option to enable Flaps2_R input port off (default) | on
  group: Controls
  block_parameter: Flaps2_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left spoiler rotation
  summary: Option to enable Left_Spoiler_R input port off (default) | on
  group: Controls
  block_parameter: Left_Spoiler_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right spoiler rotation
  summary: Option to enable Right_Spoiler_R input port off (default) | on
  group: Controls
  block_parameter: Right_Spoiler_R
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
- name: Left gear link translation
  summary: Option to enable Left_Gear_Link_T input port off (default) | on
  group: Gear
  block_parameter: Left_Gear_Link_T
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
- name: Left gear door 2.2 translation
  summary: Option to enable Left_Gear_Door2_2_T input port off (default) | on
  group: Gear
  block_parameter: Left_Gear_Door2_2_T
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
- name: Right gear link translation
  summary: Option to enable Right_Gear_Link_T input port off (default) | on
  group: Gear
  block_parameter: Right_Gear_Link_T
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
- name: Right gear door 2.2 translation
  summary: Option to enable Right_Gear_Door2_2_T input port off (default) | on
  group: Gear
  block_parameter: Right_Gear_Door2_2_T
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
  summary: Option to enable Nose_Gear_Door2_T input port off (default) | on
  group: Gear
  block_parameter: Nose_Gear_Door2_T
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
- name: Left gear link rotation
  summary: Option to enable Left_Gear_Link_R input port off (default) | on
  group: Gear
  block_parameter: Left_Gear_Link_R
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
- name: Left gear door 2.2 rotation
  summary: Option to enable Left_Gear_Door2_2_R input port off (default) | on
  group: Gear
  block_parameter: Left_Gear_Door2_2_R
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
- name: Right gear link rotation
  summary: Option to enable Right_Gear_Link_R input port off (default) | on
  group: Gear
  block_parameter: Right_Gear_Link_R
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
- name: Right gear door 2.2 rotation
  summary: Option to enable Right_Gear_Door2_2_R input port off (default) | on
  group: Gear
  block_parameter: Right_Gear_Door2_2_R
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

### **Engine 3 translation** — Option to enable Engine3\_T input port `off` (default) | `on`

Select this parameter to enable the **Engine3\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine3_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 4 translation** — Option to enable Engine4\_T input port `off` (default) | `on`

Select this parameter to enable the **Engine4\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine4_T` |
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

### **Engine 3 rotation** — Option to enable Engine3\_R input port `off` (default) | `on`

Select this parameter to enable the **Engine3\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine3_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 4 rotation** — Option to enable Engine4\_R input port `off` (default) | `on`

Select this parameter to enable the **Engine4\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine4_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### Controls

### **Rudder translation** — Option to enable Rudder\_T input port `off` (default) | `on`

Select this parameter to enable the **Rudder\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Rudder_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Elevator translation** — Option to enable Elevator\_T input port `off` (default) | `on`

Select this parameter to enable the **Elevator\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Elevator_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Horizontal stab translation** — Option to enable Horizontal\_Stab\_T input port `off` (default) | `on`

Select this parameter to enable the **Horizontal\_Stab\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Horizontal_Stab_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Left aileron translation** — Option to enable Left\_Aileron\_T input port `off` (default) | `on`

Select this parameter to enable the **Left\_Aileron\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Left_Aileron_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Right aileron translation** — Option to enable Right\_Aileron\_T input port `off` (default) | `on`

Select this parameter to enable the **Right\_Aileron\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Right_Aileron_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Flaps set 1 translation** — Option to enable Flaps1\_T input port `off` (default) | `on`

Select this parameter to enable the **Flaps1\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Flaps1_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Flaps set 2 translation** — Option to enable Flaps2\_T input port `off` (default) | `on`

Select this parameter to enable the **Flaps2\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Flaps2_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Left spoiler translation** — Option to enable Left\_Spoiler\_T input port `off` (default) | `on`

Select this parameter to enable the **Left\_Spoiler\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Left_Spoiler_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Right spoiler translation** — Option to enable Right\_Spoiler\_T input port `off` (default) | `on`

Select this parameter to enable the **Right\_Spoiler\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Right_Spoiler_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

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

### **Horizontal stab rotation** — Option to enable Horizontal\_Stab\_R input port `off` (default) | `on`

Select this parameter to enable the **Horizontal\_Stab\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Horizontal_Stab_R` |
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

### **Flaps set 1 rotation** — Option to enable Flaps1\_R input port `off` (default) | `on`

Select this parameter to enable the **Flaps1\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Flaps1_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Flaps set 2 rotation** — Option to enable Flaps2\_R input port `off` (default) | `on`

Select this parameter to enable the **Flaps2\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Flaps2_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Left spoiler rotation** — Option to enable Left\_Spoiler\_R input port `off` (default) | `on`

Select this parameter to enable the **Left\_Spoiler\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Left_Spoiler_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Right spoiler rotation** — Option to enable Right\_Spoiler\_R input port `off` (default) | `on`

Select this parameter to enable the **Right\_Spoiler\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Right_Spoiler_R` |
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

Select this parameter to enable the **Nose\_Gear\_Door1\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Nose_Gear_Door1_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Nose gear door 2 translation** — Option to enable Nose\_Gear\_Door2\_T input port `off` (default) | `on`

Select this parameter to enable the **Nose\_Gear\_Door2\_T** input
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

### **Left gear link translation** — Option to enable Left\_Gear\_Link\_T input port `off` (default) | `on`

Select this parameter to enable the **Left\_Gear\_Link\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Left_Gear_Link_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Left gear door 1 translation** — Option to enable Left\_Gear\_Door1\_T input port `off` (default) | `on`

Select this parameter to enable the **Left\_Gear\_Door1\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Left_Gear_Door1_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Left gear door 2 translation** — Option to enable Left\_Gear\_Door2\_T input port `off` (default) | `on`

Select this parameter to enable the **Left\_Gear\_Door2\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Left_Gear_Door2_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Left gear door 2.2 translation** — Option to enable Left\_Gear\_Door2\_2\_T input port `off` (default) | `on`

Select this parameter to enable the **Left\_Gear\_Door2\_2\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Left_Gear_Door2_2_T` |
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

### **Right gear link translation** — Option to enable Right\_Gear\_Link\_T input port `off` (default) | `on`

Select this parameter to enable the **Right\_Gear\_Link\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Right_Gear_Link_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Right gear door 1 translation** — Option to enable Right\_Gear\_Door1\_T input port `off` (default) | `on`

Select this parameter to enable the **Right\_Gear\_Door1\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Right_Gear_Door1_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Right gear door 2 translation** — Option to enable Right\_Gear\_Door2\_T input port `off` (default) | `on`

Select this parameter to enable the **Right\_Gear\_Door2\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Right_Gear_Door2_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Right gear door 2.2 translation** — Option to enable Right\_Gear\_Door2\_2\_T input port `off` (default) | `on`

Select this parameter to enable the **Right\_Gear\_Door2\_2\_T**
input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Right_Gear_Door2_2_T` |
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

Select this parameter to enable the **Nose\_Gear\_Door1\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Nose_Gear_Door1_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Nose gear door 2 rotation** — Option to enable Nose\_Gear\_Door2\_T input port `off` (default) | `on`

Select this parameter to enable the **Nose\_Gear\_Door2\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Nose_Gear_Door2_T` |
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

### **Left gear link rotation** — Option to enable Left\_Gear\_Link\_R input port `off` (default) | `on`

Select this parameter to enable the **Left\_Gear\_Link\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Left_Gear_Link_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Left gear door 1 rotation** — Option to enable Left\_Gear\_Door1\_R input port `off` (default) | `on`

Select this parameter to enable the **Left\_Gear\_Door1\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Left_Gear_Door1_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Left gear door 2 rotation** — Option to enable Left\_Gear\_Door2\_R input port `off` (default) | `on`

Select this parameter to enable the **Left\_Gear\_Door2\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Left_Gear_Door2_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Left gear door 2.2 rotation** — Option to enable Left\_Gear\_Door2\_2\_R input port `off` (default) | `on`

Select this parameter to enable the **Left\_Gear\_Door2\_2\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Left_Gear_Door2_2_R` |
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

### **Right gear link rotation** — Option to enable Right\_Gear\_Link\_R input port `off` (default) | `on`

Select this parameter to enable the **Right\_Gear\_Link\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Right_Gear_Link_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Right gear door 1 rotation** — Option to enable Right\_Gear\_Door1\_R input port `off` (default) | `on`

Select this parameter to enable the **Right\_Gear\_Door1\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Right_Gear_Door1_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Right gear door 2 rotation** — Option to enable Right\_Gear\_Door2\_R input port `off` (default) | `on`

Select this parameter to enable the **Right\_Gear\_Door2\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Right_Gear_Door2_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Right gear door 2.2 rotation** — Option to enable Right\_Gear\_Door2\_2\_R input port `off` (default) | `on`

Select this parameter to enable the **Right\_Gear\_Door2\_2\_R**
input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Right_Gear_Door2_2_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### Input

### **Select input coordinate frame** — Input coordinate frame `NED` (default) | `Fixed-frame` | `ICRF`

Select the input coordinate frame to position aerospace vehicles with respect to
north-east-down (NED), fixed-frame (Fixed-frame), or International Celestial Reference
Frame (ICRF).

If the model contains an associated Simulation 3D Scene
Configuration block, Simulation 3D Air Transport Pack block uses the coordinate
frame of the Simulation 3D Scene Configuration. In this case, the
**Select input coordinate frame** might be disabled. For more
information about the Simulation 3D Air Transport Pack block coordinate frame, see Algorithms.

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

### R2025a: Simulation 3D Air Transport Pack block now synchronizes coordinate frame with Simulation 3D Scene Configuration block

The Simulation 3D Air Transport Pack block has these changes:

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
  Simulation 3D Air Transport Pack might be disabled. In this case, the
  Simulation 3D Air Transport Pack synchronizes coordinate systems with the
  Simulation 3D Scene Configuration block.
- The coordinate system displays as an annotation under the block.
- The **Enable geospatial correction** and **Direction of x-axis (degrees clockwise from north)** parameters have been removed.

### R2024a: Simulation 3D Air Transport Pack Block Now Supports Earth-centered Earth-fixed (ECEF) Input Coordinate Frame

To enable ECEF coordinate systems for translation input, the Simulation 3D Air Transport Pack block
has been updated. Use these parameters with the **Use Earth center as origin
(ECEF)** parameter in the Simulation 3D Scene
Configuration block.

- **Select input coordinate frame**

  - **ECEF** — ECEF input coordinate frame. When you select this coordinate frame, the annotation `Origin: Earth center (ECEF)` appears under the pack block icons.
  - **NED** — NED coordinate frame. Prior to R2024a, NED was the only supported coordinate frame.
- **Direction of x-axis (degrees clockwise from north)** — Direction of the *x*-axis. This parameter is enabled when you select the **Enable geospatial correction** check box.

## Description

Generate translation and rotation information for air transport aircraft

The Simulation 3D Air Transport Pack block creates translation and rotation
information for the Simulation 3D Aircraft block with **Type**
set to `Air transport`. Use the Simulation 3D Air Transport
Pack block to provide translation and rotation information to the
**Translation** and **Rotation** input ports of the
Simulation 3D Aircraft block.
