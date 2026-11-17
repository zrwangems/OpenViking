---
type: simulink-block
title: 'Simulation 3D Custom Pack'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation / Simulation 3D'
documentation_page: 'simulation3dcustompack'
documentation_source_path: 'simulation3dcustompack.html'
language: en
---

# Simulation 3D Custom Pack

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
- name: Engine1_Prop_T
  summary: Engine 1 propeller translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine2_T
  summary: Engine 2 translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine2_Prop_T
  summary: Engine 2 propeller translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine3_T
  summary: Engine 3 translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine3_Prop_T
  summary: Engine 3 propeller translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine4_T
  summary: Engine 4 translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine4_Prop_T
  summary: Engine 4 propeller translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine5_T
  summary: Engine 5 translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine5_Prop_T
  summary: Engine 5 propeller translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine6_T
  summary: Engine 6 translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine6_Prop_T
  summary: Engine 6 propeller translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine7_T
  summary: Engine 7 translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine7_Prop_T
  summary: Engine 7 propeller translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine8_T
  summary: Engine 8 translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine8_Prop_T
  summary: Engine 8 propeller translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine9_T
  summary: Engine 9 translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine9_Prop_T
  summary: Engine 9 propeller translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine10_T
  summary: Engine 10 translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine10_Prop_T
  summary: Engine 10 propeller translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine11_T
  summary: Engine 11 translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine11_Prop_T
  summary: Engine 11 propeller translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine12_T
  summary: Engine 12 translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine12_Prop_T
  summary: Engine 12 propeller translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine13_T
  summary: Engine 13 translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine13_Prop_T
  summary: Engine 13 propeller translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine14_T
  summary: Engine 14 translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine14_Prop_T
  summary: Engine 14 propeller translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine15_T
  summary: Engine 15 translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine15_Prop_T
  summary: Engine 15 propeller translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine16_T
  summary: Engine 16 translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine16_Prop_T
  summary: Engine 16 propeller translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Wing1_T
  summary: Wing 1 translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Wing1_Left_Flap_T
  summary: Wing 1 left flap translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Wing1_Right_Flap_T
  summary: Wing 1 right flap translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Wing1_Left_Aileron_T
  summary: Wing 1 left aileron translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Wing1_Right_Aileron_T
  summary: Wing 1 right aileron translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Wing1_Left_Spoiler_T
  summary: Wing 1 left spoiler translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Wing1_Right_Spoiler_T
  summary: Wing 1 right spoiler translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Wing2_T
  summary: Wing 2 translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Wing2_Left_Flap_T
  summary: Wing 2 left flap translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Wing2_Right_Flap_T
  summary: Wing 2 right flap translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Horizontal_Stab_T
  summary: Horizontal stab translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Left_Elevator_T
  summary: Left elevator translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Right_Elevator_T
  summary: Right elevator translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Left_Rudder_T
  summary: Left rudder translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Right_Rudder_T
  summary: Right rudder translation 1-by-3 matrix
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
- name: Nose_Gear_Door_T
  summary: Nose gear door translation 1-by-3 matrix
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
- name: Left_Gear_Door_T
  summary: Left gear door translation 1-by-3 matrix
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
- name: Right_Gear_Door_T
  summary: Right gear door translation 1-by-3 matrix
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
- name: Engine1_Prop_R
  summary: Engine 1 propeller rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine2_R
  summary: Engine 2 rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine2_Prop_R
  summary: Engine 2 propeller rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine3_R
  summary: Engine 3 rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine3_Prop_R
  summary: Engine 3 propeller rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine4_R
  summary: Engine 4 translation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine4_Prop_R
  summary: Engine 4 propeller rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine5_R
  summary: Engine 5 rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine5_Prop_R
  summary: Engine 5 propeller rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine6_R
  summary: Engine 6 rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine6_Prop_R
  summary: Engine 6 propeller rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine7_R
  summary: Engine 7 rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine7_Prop_R
  summary: Engine 7 propeller rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine8_R
  summary: Engine 8 rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine8_Prop_R
  summary: Engine 8 propeller rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine9_R
  summary: Engine 9 rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine9_Prop_R
  summary: Engine 9 propeller rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine10_R
  summary: Engine 10 rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine10_Prop_R
  summary: Engine 10 propeller rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine11_R
  summary: Engine 11 rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine11_Prop_R
  summary: Engine 11 propeller rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine12_R
  summary: Engine 12 rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine12_Prop_R
  summary: Engine 12 propeller rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine13_R
  summary: Engine 13 rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine13_Prop_R
  summary: Engine 13 propeller rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine14_R
  summary: Engine 14 rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine14_Prop_R
  summary: Engine 14 propeller rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine15_R
  summary: Engine 15 rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine15_Prop_R
  summary: Engine 15 propeller rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine16_R
  summary: Engine 16 rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Engine16_Prop_R
  summary: Engine 16 propeller rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Wing1_R
  summary: Wing 1 rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Wing1_Left_Flap_R
  summary: Wing 1 left flap rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Wing1_Right_Flap_R
  summary: Wing 1 right flap rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Wing1_Left_Aileron_R
  summary: Wing 1 left aileron rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Wing1_Right_Aileron_R
  summary: Wing 1 right aileron rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Wing1_Left_Spoiler_R
  summary: Wing 1 left spoiler rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Wing1_Right_Spoiler_R
  summary: Wing 1 right spoiler rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Wing2_R
  summary: Wing 2 rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Wing2_Left_Flap_R
  summary: Wing 2 left flap rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Wing2_Right_Flap_R
  summary: Wing 2 right flap rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Horizontal_Stab_R
  summary: Horizontal stab rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Left_Elevator_R
  summary: Left elevator rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Right_Elevator_R
  summary: Right elevator rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Left_Rudder_R
  summary: Left rudder rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Right_Rudder_R
  summary: Right rudder rotation 1-by-3 matrix
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
- name: Nose_Gear_Door_R
  summary: Nose gear door rotation 1-by-3 matrix
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
- name: Left_Gear_Door_R
  summary: Left gear door rotation 1-by-3 matrix
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
- name: Right_Gear_Door_R
  summary: Right gear door rotation 1-by-3 matrix
  direction: input
  data_types: single | double
- name: Translation
  summary: Aircraft translation 57-by-3 array
  direction: output
- name: Rotation
  summary: Aircraft rotation 57-by-3 array
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

### **Engine1\_Prop\_T** — Engine 1 propeller translation 1-by-3 matrix

Engine 1 propeller translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 1 propeller
translation** parameter.

**Data Types:** `single` | `double`

### **Engine2\_T** — Engine 2 translation 1-by-3 matrix

Engine 2 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 2 translation**
parameter.

**Data Types:** `single` | `double`

### **Engine2\_Prop\_T** — Engine 2 propeller translation 1-by-3 matrix

Engine 2 propeller translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 2 propeller
translation** parameter.

**Data Types:** `single` | `double`

### **Engine3\_T** — Engine 3 translation 1-by-3 matrix

Engine 3 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 3 translation**
parameter.

**Data Types:** `single` | `double`

### **Engine3\_Prop\_T** — Engine 3 propeller translation 1-by-3 matrix

Engine 3 propeller translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 3 propeller
translation** parameter.

**Data Types:** `single` | `double`

### **Engine4\_T** — Engine 4 translation 1-by-3 matrix

Engine 4 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 4 translation**
parameter.

**Data Types:** `single` | `double`

### **Engine4\_Prop\_T** — Engine 4 propeller translation 1-by-3 matrix

Engine 4 propeller translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 4 propeller
translation** parameter.

**Data Types:** `single` | `double`

### **Engine5\_T** — Engine 5 translation 1-by-3 matrix

Engine 5 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 5 translation**
parameter.

**Data Types:** `single` | `double`

### **Engine5\_Prop\_T** — Engine 5 propeller translation 1-by-3 matrix

Engine 5 propeller translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 5 propeller
translation** parameter.

**Data Types:** `single` | `double`

### **Engine6\_T** — Engine 6 translation 1-by-3 matrix

Engine 6 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 6 translation**
parameter.

**Data Types:** `single` | `double`

### **Engine6\_Prop\_T** — Engine 6 propeller translation 1-by-3 matrix

Engine 6 propeller translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 6 propeller
translation** parameter.

**Data Types:** `single` | `double`

### **Engine7\_T** — Engine 7 translation 1-by-3 matrix

Engine 7 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 7 translation**
parameter.

**Data Types:** `single` | `double`

### **Engine7\_Prop\_T** — Engine 7 propeller translation 1-by-3 matrix

Engine 7 propeller translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 7 propeller
translation** parameter.

**Data Types:** `single` | `double`

### **Engine8\_T** — Engine 8 translation 1-by-3 matrix

Engine 8 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 8 translation**
parameter.

**Data Types:** `single` | `double`

### **Engine8\_Prop\_T** — Engine 8 propeller translation 1-by-3 matrix

Engine 8 propeller translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 8 propeller
translation** parameter.

**Data Types:** `single` | `double`

### **Engine9\_T** — Engine 9 translation 1-by-3 matrix

Engine 9 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 9 translation**
parameter.

**Data Types:** `single` | `double`

### **Engine9\_Prop\_T** — Engine 9 propeller translation 1-by-3 matrix

Engine 9 propeller translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 9 propeller
translation** parameter.

**Data Types:** `single` | `double`

### **Engine10\_T** — Engine 10 translation 1-by-3 matrix

Engine 10 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 10 translation**
parameter.

**Data Types:** `single` | `double`

### **Engine10\_Prop\_T** — Engine 10 propeller translation 1-by-3 matrix

Engine 10 propeller translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 10 propeller
translation** parameter.

**Data Types:** `single` | `double`

### **Engine11\_T** — Engine 11 translation 1-by-3 matrix

Engine 11 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 11 translation**
parameter.

**Data Types:** `single` | `double`

### **Engine11\_Prop\_T** — Engine 11 propeller translation 1-by-3 matrix

Engine 11 propeller translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 11 propeller
translation** parameter.

**Data Types:** `single` | `double`

### **Engine12\_T** — Engine 12 translation 1-by-3 matrix

Engine 12 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 12 translation**
parameter.

**Data Types:** `single` | `double`

### **Engine12\_Prop\_T** — Engine 12 propeller translation 1-by-3 matrix

Engine 12 propeller translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 12 propeller
translation** parameter.

**Data Types:** `single` | `double`

### **Engine13\_T** — Engine 13 translation 1-by-3 matrix

Engine 13 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 13 translation**
parameter.

**Data Types:** `single` | `double`

### **Engine13\_Prop\_T** — Engine 13 propeller translation 1-by-3 matrix

Engine 13 propeller translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 13 propeller
translation** parameter.

**Data Types:** `single` | `double`

### **Engine14\_T** — Engine 14 translation 1-by-3 matrix

Engine 14 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 14 translation**
parameter.

**Data Types:** `single` | `double`

### **Engine14\_Prop\_T** — Engine 14 propeller translation 1-by-3 matrix

Engine 14 propeller translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 14 propeller
translation** parameter.

**Data Types:** `single` | `double`

### **Engine15\_T** — Engine 15 translation 1-by-3 matrix

Engine 15 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 15 translation**
parameter.

**Data Types:** `single` | `double`

### **Engine15\_Prop\_T** — Engine 15 propeller translation 1-by-3 matrix

Engine 15 propeller translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 15 propeller
translation** parameter.

**Data Types:** `single` | `double`

### **Engine16\_T** — Engine 16 translation 1-by-3 matrix

Engine 16 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 16 translation**
parameter.

**Data Types:** `single` | `double`

### **Engine16\_Prop\_T** — Engine 16 propeller translation 1-by-3 matrix

Engine 16 propeller translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 16 propeller
translation** parameter.

**Data Types:** `single` | `double`

### **Wing1\_T** — Wing 1 translation 1-by-3 matrix

Wing 1 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Wing 1 translation**
parameter.

**Data Types:** `single` | `double`

### **Wing1\_Left\_Flap\_T** — Wing 1 left flap translation 1-by-3 matrix

Wing 1 left flap translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Wing 1 left flap
translation** parameter.

**Data Types:** `single` | `double`

### **Wing1\_Right\_Flap\_T** — Wing 1 right flap translation 1-by-3 matrix

Wing 1 right flap translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Wing 1 right flap
translation** parameter.

**Data Types:** `single` | `double`

### **Wing1\_Left\_Aileron\_T** — Wing 1 left aileron translation 1-by-3 matrix

Wing 1 left aileron translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Wing 1 left aileron
translation** parameter.

**Data Types:** `single` | `double`

### **Wing1\_Right\_Aileron\_T** — Wing 1 right aileron translation 1-by-3 matrix

Wing 1 right aileron translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Wing 1 right aileron
translation** parameter.

**Data Types:** `single` | `double`

### **Wing1\_Left\_Spoiler\_T** — Wing 1 left spoiler translation 1-by-3 matrix

Wing 1 left spoiler translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Wing 1 left spoiler
translation** parameter.

**Data Types:** `single` | `double`

### **Wing1\_Right\_Spoiler\_T** — Wing 1 right spoiler translation 1-by-3 matrix

Wing 1 right spoiler translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Wing 1 right spoiler
translation** parameter.

**Data Types:** `single` | `double`

### **Wing2\_T** — Wing 2 translation 1-by-3 matrix

Wing 2 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Wing 2 translation**
parameter.

**Data Types:** `single` | `double`

### **Wing2\_Left\_Flap\_T** — Wing 2 left flap translation 1-by-3 matrix

Wing 2 left flap translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Wing 2 left flap
translation** parameter.

**Data Types:** `single` | `double`

### **Wing2\_Right\_Flap\_T** — Wing 2 right flap translation 1-by-3 matrix

Wing 2 right flap translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Wing 2 right flap
translation** parameter.

**Data Types:** `single` | `double`

### **Horizontal\_Stab\_T** — Horizontal stab translation 1-by-3 matrix

Horizontal stab translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Horizontal stab translation**
parameter.

**Data Types:** `single` | `double`

### **Left\_Elevator\_T** — Left elevator translation 1-by-3 matrix

Left elevator translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Left elevator translation**
parameter.

**Data Types:** `single` | `double`

### **Right\_Elevator\_T** — Right elevator translation 1-by-3 matrix

Right elevator translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Right elevator translation**
parameter.

**Data Types:** `single` | `double`

### **Left\_Rudder\_T** — Left rudder translation 1-by-3 matrix

Left rudder translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Left rudder translation**
parameter.

**Data Types:** `single` | `double`

### **Right\_Rudder\_T** — Right rudder translation 1-by-3 matrix

Right rudder translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Right rudder translation**
parameter.

**Data Types:** `single` | `double`

### **Nose\_Gear\_T** — Nose gear translation 1-by-3 matrix

Nose gear translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Nose gear translation**
parameter.

**Data Types:** `single` | `double`

### **Nose\_Wheel\_T** — Nose wheel translation 1-by-3 matrix

Nose wheel translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Nose wheel translation**
parameter.

**Data Types:** `single` | `double`

### **Nose\_Gear\_Door\_T** — Nose gear door translation 1-by-3 matrix

Nose gear door translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Nose gear door translation**
parameter.

**Data Types:** `single` | `double`

### **Left\_Gear\_T** — Left gear translation 1-by-3 matrix

Left gear translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Left gear translation**
parameter.

**Data Types:** `single` | `double`

### **Left\_Wheel\_T** — Left wheel translation 1-by-3 matrix

Left wheel translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Left wheel translation**
parameter.

**Data Types:** `single` | `double`

### **Left\_Gear\_Door\_T** — Left gear door translation 1-by-3 matrix

Left gear door translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Left gear door translation**
parameter.

**Data Types:** `single` | `double`

### **Right\_Gear\_T** — Right gear translation 1-by-3 matrix

Right gear translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Right gear translation**
parameter.

**Data Types:** `single` | `double`

### **Right\_Wheel\_T** — Right wheel translation 1-by-3 matrix

Right wheel translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Right wheel translation**
parameter.

**Data Types:** `single` | `double`

### **Right\_Gear\_Door\_T** — Right gear door translation 1-by-3 matrix

Right gear door translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Right gear door translation**
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

### **Engine1\_Prop\_R** — Engine 1 propeller rotation 1-by-3 matrix

Engine 1 propeller rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 1 propeller rotation**
parameter.

**Data Types:** `single` | `double`

### **Engine2\_R** — Engine 2 rotation 1-by-3 matrix

Engine 2 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 2 rotation**
parameter.

**Data Types:** `single` | `double`

### **Engine2\_Prop\_R** — Engine 2 propeller rotation 1-by-3 matrix

Engine 2 propeller rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 2 propeller rotation**
parameter.

**Data Types:** `single` | `double`

### **Engine3\_R** — Engine 3 rotation 1-by-3 matrix

Engine 3 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 3 rotation**
parameter.

**Data Types:** `single` | `double`

### **Engine3\_Prop\_R** — Engine 3 propeller rotation 1-by-3 matrix

Engine 3 propeller rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 3 propeller rotation**
parameter.

**Data Types:** `single` | `double`

### **Engine4\_R** — Engine 4 translation 1-by-3 matrix

Engine 4 translation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 4 translation**
parameter.

**Data Types:** `single` | `double`

### **Engine4\_Prop\_R** — Engine 4 propeller rotation 1-by-3 matrix

Engine 4 propeller rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 4 propeller rotation**
parameter.

**Data Types:** `single` | `double`

### **Engine5\_R** — Engine 5 rotation 1-by-3 matrix

Engine 5 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 5 rotation**
parameter.

**Data Types:** `single` | `double`

### **Engine5\_Prop\_R** — Engine 5 propeller rotation 1-by-3 matrix

Engine 5 propeller rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 5 propeller rotation**
parameter.

**Data Types:** `single` | `double`

### **Engine6\_R** — Engine 6 rotation 1-by-3 matrix

Engine 6 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 6 rotation**
parameter.

**Data Types:** `single` | `double`

### **Engine6\_Prop\_R** — Engine 6 propeller rotation 1-by-3 matrix

Engine 6 propeller rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 6 propeller rotation**
parameter.

**Data Types:** `single` | `double`

### **Engine7\_R** — Engine 7 rotation 1-by-3 matrix

Engine 7 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 7 rotation**
parameter.

**Data Types:** `single` | `double`

### **Engine7\_Prop\_R** — Engine 7 propeller rotation 1-by-3 matrix

Engine 7 propeller rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 7 propeller rotation**
parameter.

**Data Types:** `single` | `double`

### **Engine8\_R** — Engine 8 rotation 1-by-3 matrix

Engine 8 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 8 rotation**
parameter.

**Data Types:** `single` | `double`

### **Engine8\_Prop\_R** — Engine 8 propeller rotation 1-by-3 matrix

Engine 8 propeller rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 8 propeller rotation**
parameter.

**Data Types:** `single` | `double`

### **Engine9\_R** — Engine 9 rotation 1-by-3 matrix

Engine 9 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 9 rotation**
parameter.

**Data Types:** `single` | `double`

### **Engine9\_Prop\_R** — Engine 9 propeller rotation 1-by-3 matrix

Engine 9 propeller rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 9 propeller rotation**
parameter.

**Data Types:** `single` | `double`

### **Engine10\_R** — Engine 10 rotation 1-by-3 matrix

Engine 10 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 10 rotation**
parameter.

**Data Types:** `single` | `double`

### **Engine10\_Prop\_R** — Engine 10 propeller rotation 1-by-3 matrix

Engine 10 propeller rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 10 propeller
rotation** parameter.

**Data Types:** `single` | `double`

### **Engine11\_R** — Engine 11 rotation 1-by-3 matrix

Engine 11 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 11 rotation**
parameter.

**Data Types:** `single` | `double`

### **Engine11\_Prop\_R** — Engine 11 propeller rotation 1-by-3 matrix

Engine 11 propeller rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 11 propeller
rotation** parameter.

**Data Types:** `single` | `double`

### **Engine12\_R** — Engine 12 rotation 1-by-3 matrix

Engine 12 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 12 rotation**
parameter.

**Data Types:** `single` | `double`

### **Engine12\_Prop\_R** — Engine 12 propeller rotation 1-by-3 matrix

Engine 12 propeller rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 12 propeller
rotation** parameter.

**Data Types:** `single` | `double`

### **Engine13\_R** — Engine 13 rotation 1-by-3 matrix

Engine 13 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 13 rotation**
parameter.

**Data Types:** `single` | `double`

### **Engine13\_Prop\_R** — Engine 13 propeller rotation 1-by-3 matrix

Engine 13 propeller rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 13 propeller
rotation** parameter.

**Data Types:** `single` | `double`

### **Engine14\_R** — Engine 14 rotation 1-by-3 matrix

Engine 14 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 14 rotation**
parameter.

**Data Types:** `single` | `double`

### **Engine14\_Prop\_R** — Engine 14 propeller rotation 1-by-3 matrix

Engine 14 propeller rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 14 propeller
rotation** parameter.

**Data Types:** `single` | `double`

### **Engine15\_R** — Engine 15 rotation 1-by-3 matrix

Engine 15 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 15 rotation**
parameter.

**Data Types:** `single` | `double`

### **Engine15\_Prop\_R** — Engine 15 propeller rotation 1-by-3 matrix

Engine 15 propeller rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 15 propeller
rotation** parameter.

**Data Types:** `single` | `double`

### **Engine16\_R** — Engine 16 rotation 1-by-3 matrix

Engine 16 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 16 rotation**
parameter.

**Data Types:** `single` | `double`

### **Engine16\_Prop\_R** — Engine 16 propeller rotation 1-by-3 matrix

Engine 16 propeller rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Engine 16 propeller
rotation** parameter.

**Data Types:** `single` | `double`

### **Wing1\_R** — Wing 1 rotation 1-by-3 matrix

Wing 1 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Wing 1 rotation**
parameter.

**Data Types:** `single` | `double`

### **Wing1\_Left\_Flap\_R** — Wing 1 left flap rotation 1-by-3 matrix

Wing 1 left flap rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Wing 1 left flap rotation**
parameter.

**Data Types:** `single` | `double`

### **Wing1\_Right\_Flap\_R** — Wing 1 right flap rotation 1-by-3 matrix

Wing 1 right flap rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Wing 1 right flap rotation**
parameter.

**Data Types:** `single` | `double`

### **Wing1\_Left\_Aileron\_R** — Wing 1 left aileron rotation 1-by-3 matrix

Wing 1 left aileron rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Wing 1 left aileron
rotation** parameter.

**Data Types:** `single` | `double`

### **Wing1\_Right\_Aileron\_R** — Wing 1 right aileron rotation 1-by-3 matrix

Wing 1 right aileron rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Wing 1 right aileron
rotation** parameter.

**Data Types:** `single` | `double`

### **Wing1\_Left\_Spoiler\_R** — Wing 1 left spoiler rotation 1-by-3 matrix

Wing 1 left spoiler rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Wing 1 left spoiler
rotation** parameter.

**Data Types:** `single` | `double`

### **Wing1\_Right\_Spoiler\_R** — Wing 1 right spoiler rotation 1-by-3 matrix

Wing 1 right spoiler rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Wing 1 right spoiler
rotation** parameter.

**Data Types:** `single` | `double`

### **Wing2\_R** — Wing 2 rotation 1-by-3 matrix

Wing 2 rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Wing 2 rotation**
parameter.

**Data Types:** `single` | `double`

### **Wing2\_Left\_Flap\_R** — Wing 2 left flap rotation 1-by-3 matrix

Wing 2 left flap rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Wing 2 left flap rotation**
parameter.

**Data Types:** `single` | `double`

### **Wing2\_Right\_Flap\_R** — Wing 2 right flap rotation 1-by-3 matrix

Wing 2 right flap rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Wing 2 right flap rotation**
parameter.

**Data Types:** `single` | `double`

### **Horizontal\_Stab\_R** — Horizontal stab rotation 1-by-3 matrix

Horizontal stab rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Horizontal stab rotation**
parameter.

**Data Types:** `single` | `double`

### **Left\_Elevator\_R** — Left elevator rotation 1-by-3 matrix

Left elevator rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Left elevator rotation**
parameter.

**Data Types:** `single` | `double`

### **Right\_Elevator\_R** — Right elevator rotation 1-by-3 matrix

Right elevator rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Right elevator rotation**
parameter.

**Data Types:** `single` | `double`

### **Left\_Rudder\_R** — Left rudder rotation 1-by-3 matrix

Left rudder rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Left rudder rotation**
parameter.

**Data Types:** `single` | `double`

### **Right\_Rudder\_R** — Right rudder rotation 1-by-3 matrix

Right rudder rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Right rudder rotation**
parameter.

**Data Types:** `single` | `double`

### **Nose\_Gear\_R** — Nose gear rotation 1-by-3 matrix

Nose gear rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Nose gear rotation**
parameter.

**Data Types:** `single` | `double`

### **Nose\_Wheel\_R** — Nose wheel rotation 1-by-3 matrix

Nose wheel rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Nose wheel rotation**
parameter.

**Data Types:** `single` | `double`

### **Nose\_Gear\_Door\_R** — Nose gear door rotation 1-by-3 matrix

Nose gear door rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Nose gear door rotation**
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

To enable this port, select the **Left wheel rotation**
parameter.

**Data Types:** `single` | `double`

### **Left\_Gear\_Door\_R** — Left gear door rotation 1-by-3 matrix

Left gear door rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Left gear door rotation**
parameter.

**Data Types:** `single` | `double`

### **Right\_Gear\_R** — Right gear rotation 1-by-3 matrix

Right gear rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Right gear rotation**
parameter.

**Data Types:** `single` | `double`

### **Right\_Wheel\_R** — Right wheel rotation 1-by-3 matrix

Right wheel rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Right wheel rotation**
parameter.

**Data Types:** `single` | `double`

### **Right\_Gear\_Door\_R** — Right gear door rotation 1-by-3 matrix

Right gear door rotation, specified as a 1-by-3 matrix.

#### Dependencies

To enable this port, select the **Right gear door rotation**
parameter.

**Data Types:** `single` | `double`
### Output

### **Translation** — Aircraft translation `57`-by-`3` array

Aircraft translation for custom aircraft, returned as an
`57`-by-`3` array. The signal contains translation
[*X*, *Y*, *Z*], in meters, with
one row of the array for each bone of the aircraft.

The translation applies to these bones of the `Custom`
type.

| Bone | Index |
| --- | --- |
| `BODY` | 1 |
| `ENGINE1` | 2 |
| `ENGINE1_PROP` | 3 |
| `ENGINE2` | 4 |
| `ENGINE2_PROP` | 5 |
| `ENGINE3` | 6 |
| `ENGINE3_PROP` | 7 |
| `ENGINE4` | 8 |
| `ENGINE4_PROP` | 9 |
| `ENGINE5` | 10 |
| `ENGINE5_PROP` | 11 |
| `ENGINE6` | 12 |
| `ENGINE6_PROP` | 13 |
| `ENGINE7` | 14 |
| `ENGINE7_PROP` | 15 |
| `ENGINE8` | 16 |
| `ENGINE8_PROP` | 17 |
| `ENGINE9` | 18 |
| `ENGINE9_PROP` | 19 |
| `ENGINE10` | 20 |
| `ENGINE10_PROP` | 21 |
| `ENGINE11` | 22 |
| `ENGINE11_PROP` | 23 |
| `ENGINE12` | 24 |
| `ENGINE12_PROP` | 25 |
| `ENGINE13` | 26 |
| `ENGINE13_PROP` | 27 |
| `ENGINE14` | 28 |
| `ENGINE14_PROP` | 29 |
| `ENGINE15` | 30 |
| `ENGINE15_PROP` | 31 |
| `ENGINE16` | 32 |
| `ENGINE16_PROP` | 33 |
| `WING1` | 34 |
| `WING1_LEFT_FLAP` | 35 |
| `WING1_RIGHT_FLAP` | 36 |
| `WING1_LEFT_AILERON` | 37 |
| `WING1_RIGHT_AILERON` | 38 |
| `WING1_LEFT_SPOILER` | 39 |
| `WING1_RIGHT_SPOILER` | 40 |
| `WING2` | 41 |
| `WING2_LEFT_FLAP` | 42 |
| `WING2_RIGHT_FLAP` | 43 |
| `HORIZONTAL_STABILIZER` | 44 |
| `LEFT_ELEVATOR` | 45 |
| `RIGHT_ELEVATOR` | 46 |
| `LEFT_RUDDER` | 47 |
| `RIGHT_RUDDER` | 48 |
| `NOSE_GEAR` | 49 |
| `NOSE_WHEEL` | 50 |
| `NOSE_GEAR_DOOR` | 51 |
| `LEFT_GEAR` | 52 |
| `LEFT_WHEEL` | 53 |
| `LEFT_GEAR_DOOR` | 54 |
| `RIGHT_GEAR` | 55 |
| `RIGHT_WHEEL` | 56 |
| `RIGHT_GEAR_DOOR` | 57 |

### **Rotation** — Aircraft rotation `57`-by-`3` array

Aircraft rotation for custom aircraft, returned as an
`57`-by-`3` array.

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
- name: Engine 1 propeller translation
  summary: Option to enable Engine1_Prop_T input port off (default) | on
  group: Propulsion
  block_parameter: Engine1_Prop_T
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
- name: Engine 2 propeller translation
  summary: Option to enable Engine2_Prop_T input port off (default) | on
  group: Propulsion
  block_parameter: Engine2_Prop_T
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
- name: Engine 3 propeller translation
  summary: Option to enable Engine3_Prop_T input port off (default) | on
  group: Propulsion
  block_parameter: Engine3_Prop_T
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
- name: Engine 4 propeller translation
  summary: Option to enable Engine4_Prop_T input port off (default) | on
  group: Propulsion
  block_parameter: Engine4_Prop_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 5 translation
  summary: Option to enable Engine5_T input port off (default) | on
  group: Propulsion
  block_parameter: Engine5_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 5 propeller translation
  summary: Option to enable Engine5_Prop_T input port off (default) | on
  group: Propulsion
  block_parameter: Engine5_Prop_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 6 translation
  summary: Option to enable Engine6_T input port off (default) | on
  group: Propulsion
  block_parameter: Engine6_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 6 propeller translation
  summary: Option to enable Engine6_Prop_T input port off (default) | on
  group: Propulsion
  block_parameter: Engine6_Prop_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 7 translation
  summary: Option to enable Engine7_T input port off (default) | on
  group: Propulsion
  block_parameter: Engine7_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 7 propeller translation
  summary: Option to enable Engine7_Prop_T input port off (default) | on
  group: Propulsion
  block_parameter: Engine7_Prop_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 8 translation
  summary: Option to enable Engine8_T input port off (default) | on
  group: Propulsion
  block_parameter: Engine8_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 8 propeller translation
  summary: Option to enable Engine8_Prop_T input port off (default) | on
  group: Propulsion
  block_parameter: Engine8_Prop_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 9 translation
  summary: Option to enable Engine9_T input port off (default) | on
  group: Propulsion
  block_parameter: Engine9_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 9 propeller translation
  summary: Option to enable Engine9_Prop_T input port off (default) | on
  group: Propulsion
  block_parameter: Engine9_Prop_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 10 translation
  summary: Option to enable Engine10_T input port off (default) | on
  group: Propulsion
  block_parameter: Engine10_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 10 propeller translation
  summary: Option to enable Engine10_Prop_T input port off (default) | on
  group: Propulsion
  block_parameter: Engine10_Prop_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 11 translation
  summary: Option to enable Engine11_T input port off (default) | on
  group: Propulsion
  block_parameter: Engine11_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 11 propeller translation
  summary: Option to enable Engine11_Prop_T input port off (default) | on
  group: Propulsion
  block_parameter: Engine11_Prop_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 12 translation
  summary: Option to enable Engine12_T input port off (default) | on
  group: Propulsion
  block_parameter: Engine12_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 12 propeller translation
  summary: Option to enable Engine12_Prop_T input port off (default) | on
  group: Propulsion
  block_parameter: Engine12_Prop_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 13 translation
  summary: Option to enable Engine13_T input port off (default) | on
  group: Propulsion
  block_parameter: Engine13_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 13 propeller translation
  summary: Option to enable Engine13_Prop_T input port off (default) | on
  group: Propulsion
  block_parameter: Engine13_Prop_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 14 translation
  summary: Option to enable Engine14_T input port off (default) | on
  group: Propulsion
  block_parameter: Engine14_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 14 propeller translation
  summary: Option to enable Engine14_Prop_T input port off (default) | on
  group: Propulsion
  block_parameter: Engine14_Prop_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 15 translation
  summary: Option to enable Engine15_T input port off (default) | on
  group: Propulsion
  block_parameter: Engine15_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 15 propeller translation
  summary: Option to enable Engine15_Prop_T input port off (default) | on
  group: Propulsion
  block_parameter: Engine15_Prop_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 16 translation
  summary: Option to enable Engine16_T input port off (default) | on
  group: Propulsion
  block_parameter: Engine16_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 16 propeller translation
  summary: Option to enable Engine16_Prop_T input port off (default) | on
  group: Propulsion
  block_parameter: Engine16_Prop_T
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
- name: Engine 1 propeller rotation
  summary: Option to enable Engine1_Prop_R input port off (default) | on
  group: Propulsion
  block_parameter: Engine1_Prop_R
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
- name: Engine 2 propeller rotation
  summary: Option to enable Engine2_Prop_R input port off (default) | on
  group: Propulsion
  block_parameter: Engine2_Prop_R
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
- name: Engine 3 propeller rotation
  summary: Option to enable Engine3_Prop_R input port off (default) | on
  group: Propulsion
  block_parameter: Engine3_Prop_R
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
- name: Engine 4 propeller rotation
  summary: Option to enable Engine4_Prop_R input port off (default) | on
  group: Propulsion
  block_parameter: Engine4_Prop_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 5 rotation
  summary: Option to enable Engine5_R input port off (default) | on
  group: Propulsion
  block_parameter: Engine5_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 5 propeller rotation
  summary: Option to enable Engine5_Prop_R input port off (default) | on
  group: Propulsion
  block_parameter: Engine5_Prop_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 6 rotation
  summary: Option to enable Engine6_R input port off (default) | on
  group: Propulsion
  block_parameter: Engine6_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 6 propeller rotation
  summary: Option to enable Engine6_Prop_R input port off (default) | on
  group: Propulsion
  block_parameter: Engine6_Prop_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 7 rotation
  summary: Option to enable Engine7_R input port off (default) | on
  group: Propulsion
  block_parameter: Engine7_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 7 propeller rotation
  summary: Option to enable Engine7_Prop_R input port off (default) | on
  group: Propulsion
  block_parameter: Engine7_Prop_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 8 rotation
  summary: Option to enable Engine8_R input port off (default) | on
  group: Propulsion
  block_parameter: Engine8_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 8 propeller rotation
  summary: Option to enable Engine8_Prop_R input port off (default) | on
  group: Propulsion
  block_parameter: Engine8_Prop_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 9 rotation
  summary: Option to enable Engine9_R input port off (default) | on
  group: Propulsion
  block_parameter: Engine9_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 9 propeller rotation
  summary: Option to enable Engine9_Prop_R input port off (default) | on
  group: Propulsion
  block_parameter: Engine9_Prop_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 10 rotation
  summary: Option to enable Engine10_R input port off (default) | on
  group: Propulsion
  block_parameter: Engine10_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 10 propeller rotation
  summary: Option to enable Engine10_Prop_R input port off (default) | on
  group: Propulsion
  block_parameter: Engine10_Prop_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 11 rotation
  summary: Option to enable Engine11_R input port off (default) | on
  group: Propulsion
  block_parameter: Engine11_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 11 propeller rotation
  summary: Option to enable Engine11_Prop_R input port off (default) | on
  group: Propulsion
  block_parameter: Engine11_Prop_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 12 rotation
  summary: Option to enable Engine12_R input port off (default) | on
  group: Propulsion
  block_parameter: Engine12_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 12 propeller rotation
  summary: Option to enable Engine12_Prop_R input port off (default) | on
  group: Propulsion
  block_parameter: Engine12_Prop_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 13 rotation
  summary: Option to enable Engine13_R input port off (default) | on
  group: Propulsion
  block_parameter: Engine13_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 13 propeller rotation
  summary: Option to enable Engine13_Prop_R input port off (default) | on
  group: Propulsion
  block_parameter: Engine13_Prop_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 14 rotation
  summary: Option to enable Engine14_R input port off (default) | on
  group: Propulsion
  block_parameter: Engine14_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 14 propeller rotation
  summary: Option to enable Engine14_Prop_R input port off (default) | on
  group: Propulsion
  block_parameter: Engine14_Prop_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 15 rotation
  summary: Option to enable Engine15_R input port off (default) | on
  group: Propulsion
  block_parameter: Engine15_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 15 propeller rotation
  summary: Option to enable Engine15_Prop_R input port off (default) | on
  group: Propulsion
  block_parameter: Engine15_Prop_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 16 rotation
  summary: Option to enable Engine16_R input port off (default) | on
  group: Propulsion
  block_parameter: Engine16_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 16 propeller rotation
  summary: Option to enable Engine16_Prop_R input port off (default) | on
  group: Propulsion
  block_parameter: Engine16_Prop_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 1 translation
  summary: Option to enable Wing1_T input port off (default) | on
  group: Controls
  block_parameter: Wing1_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 1 left flap translation
  summary: Option to enable Wing1_Left_Flap_T input port off (default) | on
  group: Controls
  block_parameter: Wing1_Left_Flap_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 1 right flap translation
  summary: Option to enable Wing1_Right_Flap_T input port off (default) | on
  group: Controls
  block_parameter: Wing1_Right_Flap_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 1 left aileron translation
  summary: Option to enable Wing1_Left_Aileron_T input port off (default) | on
  group: Controls
  block_parameter: Wing1_Left_Aileron_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 1 right aileron translation
  summary: Option to enable Wing1_Right_Aileron_T input port off (default) | on
  group: Controls
  block_parameter: Wing1_Right_Aileron_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 1 left spoiler translation
  summary: Option to enable Wing1_Left_Spoiler_T input port off (default) | on
  group: Controls
  block_parameter: Wing1_Left_Spoiler_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 1 right spoiler translation
  summary: Option to enable Wing1_Right_Spoiler_T input port off (default) | on
  group: Controls
  block_parameter: Wing1_Right_Spoiler_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 2 translation
  summary: Option to enable Wing2_T input port off (default) | on
  group: Controls
  block_parameter: Wing2_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 2 left flap translation
  summary: Option to enable Wing2_Left_Flap_T input port off (default) | on
  group: Controls
  block_parameter: Wing2_Left_Flap_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 2 right flap translation
  summary: Option to enable Wing2_Right_Flap_T input port off (default) | on
  group: Controls
  block_parameter: Wing2_Right_Flap_T
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
- name: Left elevator translation
  summary: Option to enable Left_Elevator_T input port off (default) | on
  group: Controls
  block_parameter: Left_Elevator_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right elevator translation
  summary: Option to enable Right_Elevator_T input port off (default) | on
  group: Controls
  block_parameter: Right_Elevator_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left rudder translation
  summary: Option to enable Left_Rudder_T input port off (default) | on
  group: Controls
  block_parameter: Left_Rudder_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right rudder translation
  summary: Option to enable Right_Rudder_T input port off (default) | on
  group: Controls
  block_parameter: Right_Rudder_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 1 rotation
  summary: Option to enable Wing1_R input port off (default) | on
  group: Controls
  block_parameter: Wing1_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 1 left flap rotation
  summary: Option to enable Wing1_Left_Flap_R input port off (default) | on
  group: Controls
  block_parameter: Wing1_Left_Flap_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 1 right flap rotation
  summary: Option to enable Wing1_Right_Flap_R input port off (default) | on
  group: Controls
  block_parameter: Wing1_Right_Flap_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 1 left aileron rotation
  summary: Option to enable Wing1_Left_Aileron_R input port off (default) | on
  group: Controls
  block_parameter: Wing1_Left_Aileron_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 1 right aileron rotation
  summary: Option to enable Wing1_Right_Aileron_R input port off (default) | on
  group: Controls
  block_parameter: Wing1_Right_Aileron_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 1 left spoiler rotation
  summary: Option to enable Wing1_Left_Spoiler_R input port off (default) | on
  group: Controls
  block_parameter: Wing1_Left_Spoiler_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 1 right spoiler rotation
  summary: Option to enable Wing1_Right_Spoiler_R input port off (default) | on
  group: Controls
  block_parameter: Wing1_Right_Spoiler_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 2 rotation
  summary: Option to enable Wing2_R input port off (default) | on
  group: Controls
  block_parameter: Wing2_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 2 left flap rotation
  summary: Option to enable Wing2_Left_Flap_R input port off (default) | on
  group: Controls
  block_parameter: Wing2_Left_Flap_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 2 right flap rotation
  summary: Option to enable Wing2_Right_Flap_R input port off (default) | on
  group: Controls
  block_parameter: Wing2_Right_Flap_R
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
- name: Left elevator rotation
  summary: Option to enable Left_Elevator_R input port off (default) | on
  group: Controls
  block_parameter: Left_Elevator_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right elevator rotation
  summary: Option to enable Right_Elevator_R input port off (default) | on
  group: Controls
  block_parameter: Right_Elevator_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left rudder rotation
  summary: Option to enable Left_Rudder_R input port off (default) | on
  group: Controls
  block_parameter: Left_Rudder_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right rudder rotation
  summary: Option to enable Right_Rudder_R input port off (default) | on
  group: Controls
  block_parameter: Right_Rudder_R
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
- name: Nose gear door translation
  summary: Option to enable Nose_Gear_Door_T input port off (default) | on
  group: Gear
  block_parameter: Nose_Gear_Door_T
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
- name: Left gear door translation
  summary: Option to enable Left_Gear_Door_T input port off (default) | on
  group: Gear
  block_parameter: Left_Gear_Door_T
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
- name: Right gear door translation
  summary: Option to enable Right_Gear_Door_T input port off (default) | on
  group: Gear
  block_parameter: Right_Gear_Door_T
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
- name: Nose gear door rotation
  summary: Option to enable Nose_Gear_Door_R input port off (default) | on
  group: Gear
  block_parameter: Nose_Gear_Door_R
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
- name: Left gear door rotation
  summary: Option to enable Left_Gear_Door_R input port off (default) | on
  group: Gear
  block_parameter: Left_Gear_Door_R
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
- name: Right gear door rotation
  summary: Option to enable Right_Gear_Door_R input port off (default) | on
  group: Gear
  block_parameter: Right_Gear_Door_R
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

### **Engine 1 propeller translation** — Option to enable Engine1\_Prop\_T input port `off` (default) | `on`

Select this parameter to enable the **Engine1\_Prop\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine1_Prop_T` |
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

### **Engine 2 propeller translation** — Option to enable Engine2\_Prop\_T input port `off` (default) | `on`

Select this parameter to enable the **Engine2\_Prop\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine2_Prop_T` |
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

### **Engine 3 propeller translation** — Option to enable Engine3\_Prop\_T input port `off` (default) | `on`

Select this parameter to enable the **Engine3\_Prop\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine3_Prop_T` |
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

### **Engine 4 propeller translation** — Option to enable Engine4\_Prop\_T input port `off` (default) | `on`

Select this parameter to enable the **Engine4\_Prop\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine4_Prop_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 5 translation** — Option to enable Engine5\_T input port `off` (default) | `on`

Select this parameter to enable the **Engine5\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine5_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 5 propeller translation** — Option to enable Engine5\_Prop\_T input port `off` (default) | `on`

Select this parameter to enable the **Engine5\_Prop\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine5_Prop_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 6 translation** — Option to enable Engine6\_T input port `off` (default) | `on`

Select this parameter to enable the **Engine6\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine6_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 6 propeller translation** — Option to enable Engine6\_Prop\_T input port `off` (default) | `on`

Select this parameter to enable the **Engine6\_Prop\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine6_Prop_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 7 translation** — Option to enable Engine7\_T input port `off` (default) | `on`

Select this parameter to enable the **Engine7\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine7_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 7 propeller translation** — Option to enable Engine7\_Prop\_T input port `off` (default) | `on`

Select this parameter to enable the **Engine7\_Prop\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine7_Prop_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 8 translation** — Option to enable Engine8\_T input port `off` (default) | `on`

Select this parameter to enable the **Engine8\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine8_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 8 propeller translation** — Option to enable Engine8\_Prop\_T input port `off` (default) | `on`

Select this parameter to enable the **Engine8\_Prop\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine8_Prop_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 9 translation** — Option to enable Engine9\_T input port `off` (default) | `on`

Select this parameter to enable the **Engine9\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine9_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 9 propeller translation** — Option to enable Engine9\_Prop\_T input port `off` (default) | `on`

Select this parameter to enable the **Engine9\_Prop\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine9_Prop_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 10 translation** — Option to enable Engine10\_T input port `off` (default) | `on`

Select this parameter to enable the **Engine10\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine10_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 10 propeller translation** — Option to enable Engine10\_Prop\_T input port `off` (default) | `on`

Select this parameter to enable the **Engine10\_Prop\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine10_Prop_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 11 translation** — Option to enable Engine11\_T input port `off` (default) | `on`

Select this parameter to enable the **Engine11\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine11_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 11 propeller translation** — Option to enable Engine11\_Prop\_T input port `off` (default) | `on`

Select this parameter to enable the **Engine11\_Prop\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine11_Prop_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 12 translation** — Option to enable Engine12\_T input port `off` (default) | `on`

Select this parameter to enable the **Engine12\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine12_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 12 propeller translation** — Option to enable Engine12\_Prop\_T input port `off` (default) | `on`

Select this parameter to enable the **Engine12\_Prop\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine12_Prop_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 13 translation** — Option to enable Engine13\_T input port `off` (default) | `on`

Select this parameter to enable the **Engine13\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine13_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 13 propeller translation** — Option to enable Engine13\_Prop\_T input port `off` (default) | `on`

Select this parameter to enable the **Engine13\_Prop\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine13_Prop_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 14 translation** — Option to enable Engine14\_T input port `off` (default) | `on`

Select this parameter to enable the **Engine14\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine14_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 14 propeller translation** — Option to enable Engine14\_Prop\_T input port `off` (default) | `on`

Select this parameter to enable the **Engine14\_Prop\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine14_Prop_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 15 translation** — Option to enable Engine15\_T input port `off` (default) | `on`

Select this parameter to enable the **Engine15\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine15_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 15 propeller translation** — Option to enable Engine15\_Prop\_T input port `off` (default) | `on`

Select this parameter to enable the **Engine15\_Prop\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine15_Prop_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 16 translation** — Option to enable Engine16\_T input port `off` (default) | `on`

Select this parameter to enable the **Engine16\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine16_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 16 propeller translation** — Option to enable Engine16\_Prop\_T input port `off` (default) | `on`

Select this parameter to enable the **Engine16\_Prop\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine16_Prop_T` |
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

### **Engine 1 propeller rotation** — Option to enable Engine1\_Prop\_R input port `off` (default) | `on`

Select this parameter to enable the **Engine1\_Prop\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine1_Prop_R` |
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

### **Engine 2 propeller rotation** — Option to enable Engine2\_Prop\_R input port `off` (default) | `on`

Select this parameter to enable the **Engine2\_Prop\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine2_Prop_R` |
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

### **Engine 3 propeller rotation** — Option to enable Engine3\_Prop\_R input port `off` (default) | `on`

Select this parameter to enable the **Engine3\_Prop\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine3_Prop_R` |
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

### **Engine 4 propeller rotation** — Option to enable Engine4\_Prop\_R input port `off` (default) | `on`

Select this parameter to enable the **Engine4\_Prop\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine4_Prop_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 5 rotation** — Option to enable Engine5\_R input port `off` (default) | `on`

Select this parameter to enable the **Engine5\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine5_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 5 propeller rotation** — Option to enable Engine5\_Prop\_R input port `off` (default) | `on`

Select this parameter to enable the **Engine5\_Prop\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine5_Prop_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 6 rotation** — Option to enable Engine6\_R input port `off` (default) | `on`

Select this parameter to enable the **Engine6\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine6_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 6 propeller rotation** — Option to enable Engine6\_Prop\_R input port `off` (default) | `on`

Select this parameter to enable the **Engine6\_Prop\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine6_Prop_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 7 rotation** — Option to enable Engine7\_R input port `off` (default) | `on`

Select this parameter to enable the **Engine7\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine7_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 7 propeller rotation** — Option to enable Engine7\_Prop\_R input port `off` (default) | `on`

Select this parameter to enable the **Engine7\_Prop\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine7_Prop_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 8 rotation** — Option to enable Engine8\_R input port `off` (default) | `on`

Select this parameter to enable the **Engine8\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine8_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 8 propeller rotation** — Option to enable Engine8\_Prop\_R input port `off` (default) | `on`

Select this parameter to enable the **Engine8\_Prop\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine8_Prop_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 9 rotation** — Option to enable Engine9\_R input port `off` (default) | `on`

Select this parameter to enable the **Engine9\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine9_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 9 propeller rotation** — Option to enable Engine9\_Prop\_R input port `off` (default) | `on`

Select this parameter to enable the **Engine9\_Prop\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine9_Prop_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 10 rotation** — Option to enable Engine10\_R input port `off` (default) | `on`

Select this parameter to enable the **Engine10\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine10_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 10 propeller rotation** — Option to enable Engine10\_Prop\_R input port `off` (default) | `on`

Select this parameter to enable the **Engine10\_Prop\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine10_Prop_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 11 rotation** — Option to enable Engine11\_R input port `off` (default) | `on`

Select this parameter to enable the **Engine11\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine11_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 11 propeller rotation** — Option to enable Engine11\_Prop\_R input port `off` (default) | `on`

Select this parameter to enable the **Engine11\_Prop\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine11_Prop_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 12 rotation** — Option to enable Engine12\_R input port `off` (default) | `on`

Select this parameter to enable the **Engine12\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine12_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 12 propeller rotation** — Option to enable Engine12\_Prop\_R input port `off` (default) | `on`

Select this parameter to enable the **Engine12\_Prop\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine12_Prop_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 13 rotation** — Option to enable Engine13\_R input port `off` (default) | `on`

Select this parameter to enable the **Engine13\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine13_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 13 propeller rotation** — Option to enable Engine13\_Prop\_R input port `off` (default) | `on`

Select this parameter to enable the **Engine13\_Prop\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine13_Prop_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 14 rotation** — Option to enable Engine14\_R input port `off` (default) | `on`

Select this parameter to enable the **Engine14\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine14_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 14 propeller rotation** — Option to enable Engine14\_Prop\_R input port `off` (default) | `on`

Select this parameter to enable the **Engine14\_Prop\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine14_Prop_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 15 rotation** — Option to enable Engine15\_R input port `off` (default) | `on`

Select this parameter to enable the **Engine15\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine15_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 15 propeller rotation** — Option to enable Engine15\_Prop\_R input port `off` (default) | `on`

Select this parameter to enable the **Engine15\_Prop\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine15_Prop_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 16 rotation** — Option to enable Engine16\_R input port `off` (default) | `on`

Select this parameter to enable the **Engine16\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine16_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Engine 16 propeller rotation** — Option to enable Engine16\_Prop\_R input port `off` (default) | `on`

Select this parameter to enable the **Engine16\_Prop\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Engine16_Prop_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### Controls

### **Wing 1 translation** — Option to enable Wing1\_T input port `off` (default) | `on`

Select this parameter to enable the **Wing1\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Wing1_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Wing 1 left flap translation** — Option to enable Wing1\_Left\_Flap\_T input port `off` (default) | `on`

Select this parameter to enable the **Wing1\_Left\_Flap\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Wing1_Left_Flap_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Wing 1 right flap translation** — Option to enable Wing1\_Right\_Flap\_T input port `off` (default) | `on`

Select this parameter to enable the **Wing1\_Right\_Flap\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Wing1_Right_Flap_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Wing 1 left aileron translation** — Option to enable Wing1\_Left\_Aileron\_T input port `off` (default) | `on`

Select this parameter to enable the **Wing1\_Left\_Aileron\_T**
input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Wing1_Left_Aileron_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Wing 1 right aileron translation** — Option to enable Wing1\_Right\_Aileron\_T input port `off` (default) | `on`

Select this parameter to enable the **Wing1\_Right\_Aileron\_T**
input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Wing1_Right_Aileron_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Wing 1 left spoiler translation** — Option to enable Wing1\_Left\_Spoiler\_T input port `off` (default) | `on`

Select this parameter to enable the **Wing1\_Left\_Spoiler\_T**
input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Wing1_Left_Spoiler_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Wing 1 right spoiler translation** — Option to enable Wing1\_Right\_Spoiler\_T input port `off` (default) | `on`

Select this parameter to enable the **Wing1\_Right\_Spoiler\_T**
input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Wing1_Right_Spoiler_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Wing 2 translation** — Option to enable Wing2\_T input port `off` (default) | `on`

Select this parameter to enable the **Wing2\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Wing2_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Wing 2 left flap translation** — Option to enable Wing2\_Left\_Flap\_T input port `off` (default) | `on`

Select this parameter to enable the **Wing2\_Left\_Flap\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Wing2_Left_Flap_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Wing 2 right flap translation** — Option to enable Wing2\_Right\_Flap\_T input port `off` (default) | `on`

Select this parameter to enable the **Wing2\_Right\_Flap\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Wing2_Right_Flap_T` |
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

### **Left elevator translation** — Option to enable Left\_Elevator\_T input port `off` (default) | `on`

Select this parameter to enable the **Left\_Elevator\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Left_Elevator_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Right elevator translation** — Option to enable Right\_Elevator\_T input port `off` (default) | `on`

Select this parameter to enable the **Right\_Elevator\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Right_Elevator_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Left rudder translation** — Option to enable Left\_Rudder\_T input port `off` (default) | `on`

Select this parameter to enable the **Left\_Rudder\_T** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Left_Rudder_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Right rudder translation** — Option to enable Right\_Rudder\_T input port `off` (default) | `on`

Select this parameter to enable the **Right\_Rudder\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Right_Rudder_T` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Wing 1 rotation** — Option to enable Wing1\_R input port `off` (default) | `on`

Select this parameter to enable the **Wing1\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Wing1_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Wing 1 left flap rotation** — Option to enable Wing1\_Left\_Flap\_R input port `off` (default) | `on`

Select this parameter to enable the **Wing1\_Left\_Flap\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Wing1_Left_Flap_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Wing 1 right flap rotation** — Option to enable Wing1\_Right\_Flap\_R input port `off` (default) | `on`

Select this parameter to enable the **Wing1\_Right\_Flap\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Wing1_Right_Flap_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Wing 1 left aileron rotation** — Option to enable Wing1\_Left\_Aileron\_R input port `off` (default) | `on`

Select this parameter to enable the **Wing1\_Left\_Aileron\_R**
input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Wing1_Left_Aileron_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Wing 1 right aileron rotation** — Option to enable Wing1\_Right\_Aileron\_R input port `off` (default) | `on`

Select this parameter to enable the **Wing1\_Right\_Aileron\_R**
input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Wing1_Right_Aileron_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Wing 1 left spoiler rotation** — Option to enable Wing1\_Left\_Spoiler\_R input port `off` (default) | `on`

Select this parameter to enable the **Wing1\_Left\_Spoiler\_R**
input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Wing1_Left_Spoiler_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Wing 1 right spoiler rotation** — Option to enable Wing1\_Right\_Spoiler\_R input port `off` (default) | `on`

Select this parameter to enable the **Wing1\_Right\_Spoiler\_R**
input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Wing1_Right_Spoiler_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Wing 2 rotation** — Option to enable Wing2\_R input port `off` (default) | `on`

Select this parameter to enable the **Wing2\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Wing2_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Wing 2 left flap rotation** — Option to enable Wing2\_Left\_Flap\_R input port `off` (default) | `on`

Select this parameter to enable the **Wing2\_Left\_Flap\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Wing2_Left_Flap_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Wing 2 right flap rotation** — Option to enable Wing2\_Right\_Flap\_R input port `off` (default) | `on`

Select this parameter to enable the **Wing2\_Right\_Flap\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Wing2_Right_Flap_R` |
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

### **Left elevator rotation** — Option to enable Left\_Elevator\_R input port `off` (default) | `on`

Select this parameter to enable the **Left\_Elevator\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Left_Elevator_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Right elevator rotation** — Option to enable Right\_Elevator\_R input port `off` (default) | `on`

Select this parameter to enable the **Right\_Elevator\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Right_Elevator_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Left rudder rotation** — Option to enable Left\_Rudder\_R input port `off` (default) | `on`

Select this parameter to enable the **Left\_Rudder\_R** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Left_Rudder_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Right rudder rotation** — Option to enable Right\_Rudder\_R input port `off` (default) | `on`

Select this parameter to enable the **Right\_Rudder\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Right_Rudder_R` |
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

### **Nose gear door translation** — Option to enable Nose\_Gear\_Door\_T input port `off` (default) | `on`

Select this parameter to enable the **Nose\_Gear\_Door\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Nose_Gear_Door_T` |
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

### **Left gear door translation** — Option to enable Left\_Gear\_Door\_T input port `off` (default) | `on`

Select this parameter to enable the **Left\_Gear\_Door\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Left_Gear_Door_T` |
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

### **Right gear door translation** — Option to enable Right\_Gear\_Door\_T input port `off` (default) | `on`

Select this parameter to enable the **Right\_Gear\_Door\_T** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Right_Gear_Door_T` |
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

### **Nose gear door rotation** — Option to enable Nose\_Gear\_Door\_R input port `off` (default) | `on`

Select this parameter to enable the **Nose\_Gear\_Door\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Nose_Gear_Door_R` |
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

### **Left gear door rotation** — Option to enable Left\_Gear\_Door\_R input port `off` (default) | `on`

Select this parameter to enable the **Left\_Gear\_Door\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Left_Gear_Door_R` |
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

### **Right gear door rotation** — Option to enable Right\_Gear\_Door\_R input port `off` (default) | `on`

Select this parameter to enable the **Right\_Gear\_Door\_R** input
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Right_Gear_Door_R` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### Input

### **Select input coordinate frame** — Input coordinate frame `NED` (default) | `Fixed-frame` | `ICRF`

Select the input coordinate frame to position aerospace vehicles with respect to
north-east-down (NED), fixed-frame (Fixed-frame), or International Celestial Reference
Frame (ICRF).

If the model contains an associated Simulation 3D Scene
Configuration block, Simulation 3D Custom Pack block uses the coordinate
frame of the Simulation 3D Scene Configuration. In this case, the
**Select input coordinate frame** might be disabled. For more
information about the Simulation 3D Custom Pack block coordinate frame, see Algorithms.

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

### R2025a: Simulation 3D Custom Pack block now synchronizes coordinate frame with Simulation 3D Scene Configuration block

The Simulation 3D Custom Pack block has these changes:

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
  Simulation 3D Custom Pack might be disabled. In this case, the
  Simulation 3D Custom Pack synchronizes coordinate systems with the
  Simulation 3D Scene Configuration block.
- The coordinate system displays as an annotation under the block.
- The **Enable geospatial correction** and **Direction of x-axis (degrees clockwise from north)** parameters have been removed.

### R2024a: Simulation 3D Custom Pack Block Now Supports Earth-centered Earth-fixed (ECEF) Input Coordinate Frame

To enable ECEF coordinate systems for translation input, the Simulation 3D Custom Pack block
has been updated. Use these parameters with the **Use Earth center as origin
(ECEF)** parameter in the Simulation 3D Scene
Configuration block.

- **Select input coordinate frame**

  - **ECEF** — ECEF input coordinate frame. When you select this coordinate frame, the annotation `Origin: Earth center (ECEF)` appears under the pack block icons.
  - **NED** — NED coordinate frame. Prior to R2024a, NED was the only supported coordinate frame.
- **Direction of x-axis (degrees clockwise from north)** — Direction of the *x*-axis. This parameter is enabled when you select the **Enable geospatial correction** check box.

## Description

Generate translation and rotation information for custom aircraft

The Simulation 3D Custom Pack block creates translation and rotation
information for the Simulation 3D Aircraft block with **Type**
set to `Custom`. Use the Simulation 3D Custom Pack
block to provide translation and rotation information to the **Translation**
and **Rotation** input ports of the Simulation 3D Aircraft
block.
