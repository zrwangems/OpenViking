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
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Custom Pack

## 端口
```yaml
ports:
- name: Body_T
  summary: 机体平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine1_T
  summary: 发动机 1 平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine1_Prop_T
  summary: 发动机 1 螺旋桨平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine2_T
  summary: 发动机 2 平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine2_Prop_T
  summary: 发动机 2 螺旋桨平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine3_T
  summary: 发动机 3 平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine3_Prop_T
  summary: 发动机 3 螺旋桨平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine4_T
  summary: 发动机 4 平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine4_Prop_T
  summary: 发动机 4 螺旋桨平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine5_T
  summary: 发动机 5 平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine5_Prop_T
  summary: 发动机 5 螺旋桨平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine6_T
  summary: 发动机 6 平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine6_Prop_T
  summary: 发动机 6 螺旋桨平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine7_T
  summary: 发动机 7 平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine7_Prop_T
  summary: 发动机 7 螺旋桨平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine8_T
  summary: 发动机 8 平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine8_Prop_T
  summary: 发动机 8 螺旋桨平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine9_T
  summary: 发动机 9 平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine9_Prop_T
  summary: 发动机 9 螺旋桨平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine10_T
  summary: 发动机 10 平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine10_Prop_T
  summary: 发动机 10 螺旋桨平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine11_T
  summary: 发动机 11 平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine11_Prop_T
  summary: 发动机 11 螺旋桨平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine12_T
  summary: 发动机 12 平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine12_Prop_T
  summary: 发动机 12 螺旋桨平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine13_T
  summary: 发动机 13 平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine13_Prop_T
  summary: 发动机 13 螺旋桨平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine14_T
  summary: 发动机 14 平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine14_Prop_T
  summary: 发动机 14 螺旋桨平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine15_T
  summary: 发动机 15 平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine15_Prop_T
  summary: 发动机 15 螺旋桨平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine16_T
  summary: 发动机 16 平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine16_Prop_T
  summary: 发动机 16 螺旋桨平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Wing1_T
  summary: 机翼 1 平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Wing1_Left_Flap_T
  summary: 机翼 1 左襟翼平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Wing1_Right_Flap_T
  summary: 机翼 1 右襟翼平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Wing1_Left_Aileron_T
  summary: 机翼 1 左副翼平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Wing1_Right_Aileron_T
  summary: 机翼 1 右副翼平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Wing1_Left_Spoiler_T
  summary: 机翼 1 左扰流板平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Wing1_Right_Spoiler_T
  summary: 机翼 1 右扰流板平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Wing2_T
  summary: 机翼 2 平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Wing2_Left_Flap_T
  summary: 机翼 2 左襟翼平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Wing2_Right_Flap_T
  summary: 机翼 2 右襟翼平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Horizontal_Stab_T
  summary: 水平安定面平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Left_Elevator_T
  summary: 左升降舵平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Right_Elevator_T
  summary: 右升降舵平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Left_Rudder_T
  summary: 左方向舵平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Right_Rudder_T
  summary: 右方向舵平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Nose_Gear_T
  summary: 前起落架平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Nose_Wheel_T
  summary: 前轮平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Nose_Gear_Door_T
  summary: 前起落架舱门平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Left_Gear_T
  summary: 左起落架平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Left_Wheel_T
  summary: 左轮平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Left_Gear_Door_T
  summary: 左起落架舱门平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Right_Gear_T
  summary: 右起落架平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Right_Wheel_T
  summary: 右轮平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Right_Gear_Door_T
  summary: 右起落架舱门平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Body_R
  summary: 机体旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine1_R
  summary: 发动机 1 旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine1_Prop_R
  summary: 发动机 1 螺旋桨旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine2_R
  summary: 发动机 2 旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine2_Prop_R
  summary: 发动机 2 螺旋桨旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine3_R
  summary: 发动机 3 旋转 1×3 矩阵
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

### 输入

### **Body\_T** — 机体平移 1×3 矩阵

机体平移，指定为 1×3 矩阵。

**数据类型：** `single` | `double`

### **Engine1\_T** — 发动机 1 平移 1×3 矩阵

发动机 1 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 1 translation** 参数。

**数据类型：** `single` | `double`

### **Engine1\_Prop\_T** — 发动机 1 螺旋桨平移 1×3 矩阵

发动机 1 螺旋桨平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 1 propeller translation** 参数。

**数据类型：** `single` | `double`

### **Engine2\_T** — 发动机 2 平移 1×3 矩阵

发动机 2 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 2 translation** 参数。

**数据类型：** `single` | `double`

### **Engine2\_Prop\_T** — 发动机 2 螺旋桨平移 1×3 矩阵

发动机 2 螺旋桨平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 2 propeller translation** 参数。

**数据类型：** `single` | `double`

### **Engine3\_T** — 发动机 3 平移 1×3 矩阵

发动机 3 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 3 translation** 参数。

**数据类型：** `single` | `double`

### **Engine3\_Prop\_T** — 发动机 3 螺旋桨平移 1×3 矩阵

发动机 3 螺旋桨平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 3 propeller translation** 参数。

**数据类型：** `single` | `double`

### **Engine4\_T** — 发动机 4 平移 1×3 矩阵

发动机 4 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 4 translation** 参数。

**数据类型：** `single` | `double`

### **Engine4\_Prop\_T** — 发动机 4 螺旋桨平移 1×3 矩阵

发动机 4 螺旋桨平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 4 propeller translation** 参数。

**数据类型：** `single` | `double`

### **Engine5\_T** — 发动机 5 平移 1×3 矩阵

发动机 5 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 5 translation** 参数。

**数据类型：** `single` | `double`

### **Engine5\_Prop\_T** — 发动机 5 螺旋桨平移 1×3 矩阵

发动机 5 螺旋桨平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 5 propeller translation** 参数。

**数据类型：** `single` | `double`

### **Engine6\_T** — 发动机 6 平移 1×3 矩阵

发动机 6 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 6 translation** 参数。

**数据类型：** `single` | `double`

### **Engine6\_Prop\_T** — 发动机 6 螺旋桨平移 1×3 矩阵

发动机 6 螺旋桨平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 6 propeller translation** 参数。

**数据类型：** `single` | `double`

### **Engine7\_T** — 发动机 7 平移 1×3 矩阵

发动机 7 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 7 translation** 参数。

**数据类型：** `single` | `double`

### **Engine7\_Prop\_T** — 发动机 7 螺旋桨平移 1×3 矩阵

发动机 7 螺旋桨平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 7 propeller translation** 参数。

**数据类型：** `single` | `double`

### **Engine8\_T** — 发动机 8 平移 1×3 矩阵

发动机 8 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 8 translation** 参数。

**数据类型：** `single` | `double`

### **Engine8\_Prop\_T** — 发动机 8 螺旋桨平移 1×3 矩阵

发动机 8 螺旋桨平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 8 propeller translation** 参数。

**数据类型：** `single` | `double`

### **Engine9\_T** — 发动机 9 平移 1×3 矩阵

发动机 9 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 9 translation** 参数。

**数据类型：** `single` | `double`

### **Engine9\_Prop\_T** — 发动机 9 螺旋桨平移 1×3 矩阵

发动机 9 螺旋桨平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 9 propeller translation** 参数。

**数据类型：** `single` | `double`

### **Engine10\_T** — 发动机 10 平移 1×3 矩阵

发动机 10 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 10 translation** 参数。

**数据类型：** `single` | `double`

### **Engine10\_Prop\_T** — 发动机 10 螺旋桨平移 1×3 矩阵

发动机 10 螺旋桨平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 10 propeller translation** 参数。

**数据类型：** `single` | `double`

### **Engine11\_T** — 发动机 11 平移 1×3 矩阵

发动机 11 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 11 translation** 参数。

**数据类型：** `single` | `double`

### **Engine11\_Prop\_T** — 发动机 11 螺旋桨平移 1×3 矩阵

发动机 11 螺旋桨平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 11 propeller translation** 参数。

**数据类型：** `single` | `double`

### **Engine12\_T** — 发动机 12 平移 1×3 矩阵

发动机 12 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 12 translation** 参数。

**数据类型：** `single` | `double`

### **Engine12\_Prop\_T** — 发动机 12 螺旋桨平移 1×3 矩阵

发动机 12 螺旋桨平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 12 propeller translation** 参数。

**数据类型：** `single` | `double`

### **Engine13\_T** — 发动机 13 平移 1×3 矩阵

发动机 13 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 13 translation** 参数。

**数据类型：** `single` | `double`

### **Engine13\_Prop\_T** — 发动机 13 螺旋桨平移 1×3 矩阵

发动机 13 螺旋桨平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 13 propeller translation** 参数。

**数据类型：** `single` | `double`

### **Engine14\_T** — 发动机 14 平移 1×3 矩阵

发动机 14 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 14 translation** 参数。

**数据类型：** `single` | `double`

### **Engine14\_Prop\_T** — 发动机 14 螺旋桨平移 1×3 矩阵

发动机 14 螺旋桨平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 14 propeller translation** 参数。

**数据类型：** `single` | `double`

### **Engine15\_T** — 发动机 15 平移 1×3 矩阵

发动机 15 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 15 translation** 参数。

**数据类型：** `single` | `double`

### **Engine15\_Prop\_T** — 发动机 15 螺旋桨平移 1×3 矩阵

发动机 15 螺旋桨平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 15 propeller translation** 参数。

**数据类型：** `single` | `double`

### **Engine16\_T** — 发动机 16 平移 1×3 矩阵

发动机 16 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 16 translation** 参数。

**数据类型：** `single` | `double`

### **Engine16\_Prop\_T** — 发动机 16 螺旋桨平移 1×3 矩阵

发动机 16 螺旋桨平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 16 propeller translation** 参数。

**数据类型：** `single` | `double`

### **Wing1\_T** — 机翼 1 平移 1×3 矩阵

机翼 1 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Wing 1 translation** 参数。

**数据类型：** `single` | `double`

### **Wing1\_Left\_Flap\_T** — 机翼 1 左襟翼平移 1×3 矩阵

机翼 1 左襟翼平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Wing 1 left flap translation** 参数。

**数据类型：** `single` | `double`

### **Wing1\_Right\_Flap\_T** — 机翼 1 右襟翼平移 1×3 矩阵

机翼 1 右襟翼平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Wing 1 right flap translation** 参数。

**数据类型：** `single` | `double`

### **Wing1\_Left\_Aileron\_T** — 机翼 1 左副翼平移 1×3 矩阵

机翼 1 左副翼平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Wing 1 left aileron translation** 参数。

**数据类型：** `single` | `double`

### **Wing1\_Right\_Aileron\_T** — 机翼 1 右副翼平移 1×3 矩阵

机翼 1 右副翼平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Wing 1 right aileron translation** 参数。

**数据类型：** `single` | `double`

### **Wing1\_Left\_Spoiler\_T** — 机翼 1 左扰流板平移 1×3 矩阵

机翼 1 左扰流板平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Wing 1 left spoiler translation** 参数。

**数据类型：** `single` | `double`

### **Wing1\_Right\_Spoiler\_T** — 机翼 1 右扰流板平移 1×3 矩阵

机翼 1 右扰流板平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Wing 1 right spoiler translation** 参数。

**数据类型：** `single` | `double`

### **Wing2\_T** — 机翼 2 平移 1×3 矩阵

机翼 2 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Wing 2 translation** 参数。

**数据类型：** `single` | `double`

### **Wing2\_Left\_Flap\_T** — 机翼 2 左襟翼平移 1×3 矩阵

机翼 2 左襟翼平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Wing 2 left flap translation** 参数。

**数据类型：** `single` | `double`

### **Wing2\_Right\_Flap\_T** — 机翼 2 右襟翼平移 1×3 矩阵

机翼 2 右襟翼平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Wing 2 right flap translation** 参数。

**数据类型：** `single` | `double`

### **Horizontal\_Stab\_T** — 水平安定面平移 1×3 矩阵

水平安定面平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Horizontal stab translation** 参数。

**数据类型：** `single` | `double`

### **Left\_Elevator\_T** — 左升降舵平移 1×3 矩阵

左升降舵平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Left elevator translation** 参数。

**数据类型：** `single` | `double`

### **Right\_Elevator\_T** — 右升降舵平移 1×3 矩阵

右升降舵平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Right elevator translation** 参数。

**数据类型：** `single` | `double`

### **Left\_Rudder\_T** — 左方向舵平移 1×3 矩阵

左方向舵平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Left rudder translation** 参数。

**数据类型：** `single` | `double`

### **Right\_Rudder\_T** — 右方向舵平移 1×3 矩阵

右方向舵平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Right rudder translation** 参数。

**数据类型：** `single` | `double`

### **Nose\_Gear\_T** — 前起落架平移 1×3 矩阵

前起落架平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Nose gear translation** 参数。

**数据类型：** `single` | `double`

### **Nose\_Wheel\_T** — 前轮平移 1×3 矩阵

前轮平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Nose wheel translation** 参数。

**数据类型：** `single` | `double`

### **Nose\_Gear\_Door\_T** — 前起落架舱门平移 1×3 矩阵

前起落架舱门平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Nose gear door translation** 参数。

**数据类型：** `single` | `double`

### **Left\_Gear\_T** — 左起落架平移 1×3 矩阵

左起落架平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Left gear translation** 参数。

**数据类型：** `single` | `double`

### **Left\_Wheel\_T** — 左轮平移 1×3 矩阵

左轮平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Left wheel translation** 参数。

**数据类型：** `single` | `double`

### **Left\_Gear\_Door\_T** — 左起落架舱门平移 1×3 矩阵

左起落架舱门平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Left gear door translation** 参数。

**数据类型：** `single` | `double`

### **Right\_Gear\_T** — 右起落架平移 1×3 矩阵

右起落架平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Right gear translation** 参数。

**数据类型：** `single` | `double`

### **Right\_Wheel\_T** — 右轮平移 1×3 矩阵

右轮平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Right wheel translation** 参数。

**数据类型：** `single` | `double`

### **Right\_Gear\_Door\_T** — 右起落架舱门平移 1×3 矩阵

右起落架舱门平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Right gear door translation** 参数。

**数据类型：** `single` | `double`

### **Body\_R** — 机体旋转 1×3 矩阵

机体旋转，指定为 1×3 矩阵。

**数据类型：** `single` | `double`

### **Engine1\_R** — 发动机 1 旋转 1×3 矩阵

发动机 1 旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 1 rotation** 参数。

**数据类型：** `single` | `double`

### **Engine1\_Prop\_R** — 发动机 1 螺旋桨旋转 1×3 矩阵

发动机 1 螺旋桨旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 1 propeller rotation** 参数。

**数据类型：** `single` | `double`

### **Engine2\_R** — 发动机 2 旋转 1×3 矩阵

发动机 2 旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 2 rotation** 参数。

**数据类型：** `single` | `double`

### **Engine2\_Prop\_R** — 发动机 2 螺旋桨旋转 1×3 矩阵

发动机 2 螺旋桨旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 2 propeller rotation** 参数。

**数据类型：** `single` | `double`

### **Engine3\_R** — 发动机 3 旋转 1×3 矩阵

发动机 3 旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 3 rotation** 参数。

**数据类型：** `single` | `double`

### **Engine3\_Prop\_R** — Engine 3 propeller rotation 1-by-3 matrix

Engine 3 propeller rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 3 propeller rotation** 参数。

**Data Types:** `single` | `double`

### **Engine4\_R** — Engine 4 translation 1-by-3 matrix

Engine 4 translation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 4 translation** 参数。

**Data Types:** `single` | `double`

### **Engine4\_Prop\_R** — Engine 4 propeller rotation 1-by-3 matrix

Engine 4 propeller rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 4 propeller rotation** 参数。

**Data Types:** `single` | `double`

### **Engine5\_R** — Engine 5 rotation 1-by-3 matrix

Engine 5 rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 5 rotation** 参数。

**Data Types:** `single` | `double`

### **Engine5\_Prop\_R** — Engine 5 propeller rotation 1-by-3 matrix

Engine 5 propeller rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 5 propeller rotation** 参数。

**Data Types:** `single` | `double`

### **Engine6\_R** — Engine 6 rotation 1-by-3 matrix

Engine 6 rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 6 rotation** 参数。

**Data Types:** `single` | `double`

### **Engine6\_Prop\_R** — Engine 6 propeller rotation 1-by-3 matrix

Engine 6 propeller rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 6 propeller rotation** 参数。

**Data Types:** `single` | `double`

### **Engine7\_R** — Engine 7 rotation 1-by-3 matrix

Engine 7 rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 7 rotation** 参数。

**Data Types:** `single` | `double`

### **Engine7\_Prop\_R** — Engine 7 propeller rotation 1-by-3 matrix

Engine 7 propeller rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 7 propeller rotation** 参数。

**Data Types:** `single` | `double`

### **Engine8\_R** — Engine 8 rotation 1-by-3 matrix

Engine 8 rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 8 rotation** 参数。

**Data Types:** `single` | `double`

### **Engine8\_Prop\_R** — Engine 8 propeller rotation 1-by-3 matrix

Engine 8 propeller rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 8 propeller rotation** 参数。

**Data Types:** `single` | `double`

### **Engine9\_R** — Engine 9 rotation 1-by-3 matrix

Engine 9 rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 9 rotation** 参数。

**Data Types:** `single` | `double`

### **Engine9\_Prop\_R** — Engine 9 propeller rotation 1-by-3 matrix

Engine 9 propeller rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 9 propeller rotation** 参数。

**Data Types:** `single` | `double`

### **Engine10\_R** — Engine 10 rotation 1-by-3 matrix

Engine 10 rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 10 rotation** 参数。

**Data Types:** `single` | `double`

### **Engine10\_Prop\_R** — Engine 10 propeller rotation 1-by-3 matrix

Engine 10 propeller rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 10 propeller rotation** 参数。

**Data Types:** `single` | `double`

### **Engine11\_R** — Engine 11 rotation 1-by-3 matrix

Engine 11 rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 11 rotation** 参数。

**Data Types:** `single` | `double`

### **Engine11\_Prop\_R** — Engine 11 propeller rotation 1-by-3 matrix

Engine 11 propeller rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 11 propeller rotation** 参数。

**Data Types:** `single` | `double`

### **Engine12\_R** — Engine 12 rotation 1-by-3 matrix

Engine 12 rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 12 rotation** 参数。

**Data Types:** `single` | `double`

### **Engine12\_Prop\_R** — Engine 12 propeller rotation 1-by-3 matrix

Engine 12 propeller rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 12 propeller rotation** 参数。

**Data Types:** `single` | `double`

### **Engine13\_R** — Engine 13 rotation 1-by-3 matrix

Engine 13 rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 13 rotation** 参数。

**Data Types:** `single` | `double`

### **Engine13\_Prop\_R** — Engine 13 propeller rotation 1-by-3 matrix

Engine 13 propeller rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 13 propeller rotation** 参数。

**Data Types:** `single` | `double`

### **Engine14\_R** — Engine 14 rotation 1-by-3 matrix

Engine 14 rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 14 rotation** 参数。

**Data Types:** `single` | `double`

### **Engine14\_Prop\_R** — Engine 14 propeller rotation 1-by-3 matrix

Engine 14 propeller rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 14 propeller rotation** 参数。

**Data Types:** `single` | `double`

### **Engine15\_R** — Engine 15 rotation 1-by-3 matrix

Engine 15 rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 15 rotation** 参数。

**Data Types:** `single` | `double`

### **Engine15\_Prop\_R** — Engine 15 propeller rotation 1-by-3 matrix

Engine 15 propeller rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 15 propeller rotation** 参数。

**Data Types:** `single` | `double`

### **Engine16\_R** — Engine 16 rotation 1-by-3 matrix

Engine 16 rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 16 rotation** 参数。

**Data Types:** `single` | `double`

### **Engine16\_Prop\_R** — Engine 16 propeller rotation 1-by-3 matrix

Engine 16 propeller rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 16 propeller rotation** 参数。

**Data Types:** `single` | `double`

### **Wing1\_R** — Wing 1 rotation 1-by-3 matrix

Wing 1 rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Wing 1 rotation** 参数。

**Data Types:** `single` | `double`

### **Wing1\_Left\_Flap\_R** — Wing 1 left flap rotation 1-by-3 matrix

Wing 1 left flap rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Wing 1 left flap rotation** 参数。

**Data Types:** `single` | `double`

### **Wing1\_Right\_Flap\_R** — Wing 1 right flap rotation 1-by-3 matrix

Wing 1 right flap rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Wing 1 right flap rotation** 参数。

**Data Types:** `single` | `double`

### **Wing1\_Left\_Aileron\_R** — Wing 1 left aileron rotation 1-by-3 matrix

Wing 1 left aileron rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Wing 1 left aileron rotation** 参数。

**Data Types:** `single` | `double`

### **Wing1\_Right\_Aileron\_R** — Wing 1 right aileron rotation 1-by-3 matrix

Wing 1 right aileron rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Wing 1 right aileron rotation** 参数。

**Data Types:** `single` | `double`

### **Wing1\_Left\_Spoiler\_R** — Wing 1 left spoiler rotation 1-by-3 matrix

Wing 1 left spoiler rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Wing 1 left spoiler rotation** 参数。

**Data Types:** `single` | `double`

### **Wing1\_Right\_Spoiler\_R** — Wing 1 right spoiler rotation 1-by-3 matrix

Wing 1 right spoiler rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Wing 1 right spoiler rotation** 参数。

**Data Types:** `single` | `double`

### **Wing2\_R** — Wing 2 rotation 1-by-3 matrix

Wing 2 rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Wing 2 rotation** 参数。

**Data Types:** `single` | `double`

### **Wing2\_Left\_Flap\_R** — Wing 2 left flap rotation 1-by-3 matrix

Wing 2 left flap rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Wing 2 left flap rotation** 参数。

**Data Types:** `single` | `double`

### **Wing2\_Right\_Flap\_R** — Wing 2 right flap rotation 1-by-3 matrix

Wing 2 right flap rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Wing 2 right flap rotation** 参数。

**Data Types:** `single` | `double`

### **Horizontal\_Stab\_R** — Horizontal stab rotation 1-by-3 matrix

Horizontal stab rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Horizontal stab rotation** 参数。

**Data Types:** `single` | `double`

### **Left\_Elevator\_R** — Left elevator rotation 1-by-3 matrix

Left elevator rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Left elevator rotation** 参数。

**Data Types:** `single` | `double`

### **Right\_Elevator\_R** — Right elevator rotation 1-by-3 matrix

Right elevator rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Right elevator rotation** 参数。

**Data Types:** `single` | `double`

### **Left\_Rudder\_R** — Left rudder rotation 1-by-3 matrix

Left rudder rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Left rudder rotation** 参数。

**Data Types:** `single` | `double`

### **Right\_Rudder\_R** — Right rudder rotation 1-by-3 matrix

Right rudder rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Right rudder rotation** 参数。

**Data Types:** `single` | `double`

### **Nose\_Gear\_R** — Nose gear rotation 1-by-3 matrix

Nose gear rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Nose gear rotation** 参数。

**Data Types:** `single` | `double`

### **Nose\_Wheel\_R** — Nose wheel rotation 1-by-3 matrix

Nose wheel rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Nose wheel rotation** 参数。

**Data Types:** `single` | `double`

### **Nose\_Gear\_Door\_R** — Nose gear door rotation 1-by-3 matrix

Nose gear door rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Nose gear door rotation** 参数。

**Data Types:** `single` | `double`

### **Left\_Gear\_R** — Left gear rotation 1-by-3 matrix

Left gear rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Left gear rotation** 参数。

**Data Types:** `single` | `double`

### **Left\_Wheel\_R** — Left wheel rotation 1-by-3 matrix

Left wheel rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Left wheel rotation** 参数。

**Data Types:** `single` | `double`

### **Left\_Gear\_Door\_R** — Left gear door rotation 1-by-3 matrix

Left gear door rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Left gear door rotation** 参数。

**Data Types:** `single` | `double`

### **Right\_Gear\_R** — Right gear rotation 1-by-3 matrix

Right gear rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Right gear rotation** 参数。

**Data Types:** `single` | `double`

### **Right\_Wheel\_R** — Right wheel rotation 1-by-3 matrix

Right wheel rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Right wheel rotation** 参数。

**Data Types:** `single` | `double`

### **Right\_Gear\_Door\_R** — Right gear door rotation 1-by-3 matrix

Right gear door rotation，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Right gear door rotation** 参数。

**Data Types:** `single` | `double`
### 输出

### **Translation** — Aircraft translation `57`-by-`3` array

自定义飞行器的飞行器平移，返回为 `57`-by-`3` 数组。该信号包含平移 [*X*, *Y*, *Z*]，单位为米，数组的每一行对应飞行器的一个骨骼。

该平移适用于 `Custom` 类型的以下骨骼。

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

自定义飞行器的飞行器旋转，返回为 `57`-by-`3` 数组。

该旋转适用于 Translation 端口所列出的相同骨骼。

该信号包含旋转 [roll, pitch, yaw]，单位为弧度，数组的每一行对应飞行器的一个骨骼。
## 参数
```yaml
parameters:
- name: Engine 1 translation
  summary: 启用 Engine1_T 输入端口的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine1_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 1 propeller translation
  summary: 启用 Engine1_Prop_T 输入端口的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine1_Prop_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 2 translation
  summary: 启用 Engine2_T 输入端口的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine2_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 2 propeller translation
  summary: 启用 Engine2_Prop_T 输入端口的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine2_Prop_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 3 translation
  summary: 用于启用 Engine3_T 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine3_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 3 propeller translation
  summary: 用于启用 Engine3_Prop_T 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine3_Prop_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 4 translation
  summary: 用于启用 Engine4_T 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine4_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 4 propeller translation
  summary: 用于启用 Engine4_Prop_T 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine4_Prop_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 5 translation
  summary: 用于启用 Engine5_T 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine5_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 5 propeller translation
  summary: 用于启用 Engine5_Prop_T 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine5_Prop_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 6 translation
  summary: 用于启用 Engine6_T 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine6_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 6 propeller translation
  summary: 用于启用 Engine6_Prop_T 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine6_Prop_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 7 translation
  summary: 用于启用 Engine7_T 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine7_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 7 propeller translation
  summary: 用于启用 Engine7_Prop_T 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine7_Prop_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 8 translation
  summary: 用于启用 Engine8_T 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine8_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 8 propeller translation
  summary: 用于启用 Engine8_Prop_T 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine8_Prop_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 9 translation
  summary: 用于启用 Engine9_T 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine9_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 9 propeller translation
  summary: 用于启用 Engine9_Prop_T 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine9_Prop_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 10 translation
  summary: 用于启用 Engine10_T 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine10_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 10 propeller translation
  summary: 用于启用 Engine10_Prop_T 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine10_Prop_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 11 translation
  summary: 用于启用 Engine11_T 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine11_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 11 propeller translation
  summary: 用于启用 Engine11_Prop_T 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine11_Prop_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 12 translation
  summary: 用于启用 Engine12_T 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine12_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 12 propeller translation
  summary: 用于启用 Engine12_Prop_T 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine12_Prop_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 13 translation
  summary: 用于启用 Engine13_T 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine13_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 13 propeller translation
  summary: 用于启用 Engine13_Prop_T 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine13_Prop_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 14 translation
  summary: 用于启用 Engine14_T 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine14_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 14 propeller translation
  summary: 用于启用 Engine14_Prop_T 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine14_Prop_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 15 translation
  summary: 用于启用 Engine15_T 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine15_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 15 propeller translation
  summary: 用于启用 Engine15_Prop_T 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine15_Prop_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 16 translation
  summary: 用于启用 Engine16_T 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine16_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 16 propeller translation
  summary: 用于启用 Engine16_Prop_T 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine16_Prop_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 1 rotation
  summary: 用于启用 Engine1_R 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine1_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 1 propeller rotation
  summary: 用于启用 Engine1_Prop_R 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine1_Prop_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 2 rotation
  summary: 用于启用 Engine2_R 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine2_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 2 propeller rotation
  summary: 用于启用 Engine2_Prop_R 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine2_Prop_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 3 rotation
  summary: 用于启用 Engine3_R 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine3_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 3 propeller rotation
  summary: 用于启用 Engine3_Prop_R 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine3_Prop_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 4 rotation
  summary: 用于启用 Engine4_R 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine4_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 4 propeller rotation
  summary: 用于启用 Engine4_Prop_R 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine4_Prop_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 5 rotation
  summary: 用于启用 Engine5_R 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine5_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 5 propeller rotation
  summary: 用于启用 Engine5_Prop_R 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine5_Prop_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 6 rotation
  summary: 用于启用 Engine6_R 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine6_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 6 propeller rotation
  summary: 用于启用 Engine6_Prop_R 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine6_Prop_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 7 rotation
  summary: 用于启用 Engine7_R 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine7_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 7 propeller rotation
  summary: 用于启用 Engine7_Prop_R 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine7_Prop_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 8 rotation
  summary: 用于启用 Engine8_R 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine8_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 8 propeller rotation
  summary: 用于启用 Engine8_Prop_R 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine8_Prop_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 9 rotation
  summary: 用于启用 Engine9_R 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine9_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 9 propeller rotation
  summary: 用于启用 Engine9_Prop_R 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine9_Prop_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 10 rotation
  summary: 用于启用 Engine10_R 输入端的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine10_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 10 propeller rotation
  summary: 用于启用 Engine10_Prop_R 输入端口的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine10_Prop_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 11 rotation
  summary: 用于启用 Engine11_R 输入端口的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine11_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 11 propeller rotation
  summary: 用于启用 Engine11_Prop_R 输入端口的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine11_Prop_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 12 rotation
  summary: 用于启用 Engine12_R 输入端口的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine12_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 12 propeller rotation
  summary: 用于启用 Engine12_Prop_R 输入端口的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine12_Prop_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 13 rotation
  summary: 用于启用 Engine13_R 输入端口的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine13_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 13 propeller rotation
  summary: 用于启用 Engine13_Prop_R 输入端口的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine13_Prop_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 14 rotation
  summary: 用于启用 Engine14_R 输入端口的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine14_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 14 propeller rotation
  summary: 用于启用 Engine14_Prop_R 输入端口的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine14_Prop_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 15 rotation
  summary: 用于启用 Engine15_R 输入端口的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine15_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 15 propeller rotation
  summary: 用于启用 Engine15_Prop_R 输入端口的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine15_Prop_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 16 rotation
  summary: 用于启用 Engine16_R 输入端口的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine16_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 16 propeller rotation
  summary: 用于启用 Engine16_Prop_R 输入端口的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine16_Prop_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 1 translation
  summary: 用于启用 Wing1_T 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Wing1_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 1 left flap translation
  summary: 用于启用 Wing1_Left_Flap_T 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Wing1_Left_Flap_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 1 right flap translation
  summary: 用于启用 Wing1_Right_Flap_T 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Wing1_Right_Flap_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 1 left aileron translation
  summary: 用于启用 Wing1_Left_Aileron_T 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Wing1_Left_Aileron_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 1 right aileron translation
  summary: 用于启用 Wing1_Right_Aileron_T 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Wing1_Right_Aileron_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 1 left spoiler translation
  summary: 用于启用 Wing1_Left_Spoiler_T 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Wing1_Left_Spoiler_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 1 right spoiler translation
  summary: 用于启用 Wing1_Right_Spoiler_T 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Wing1_Right_Spoiler_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 2 translation
  summary: 用于启用 Wing2_T 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Wing2_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 2 left flap translation
  summary: 用于启用 Wing2_Left_Flap_T 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Wing2_Left_Flap_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 2 right flap translation
  summary: 用于启用 Wing2_Right_Flap_T 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Wing2_Right_Flap_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Horizontal stab translation
  summary: 用于启用 Horizontal_Stab_T 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Horizontal_Stab_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left elevator translation
  summary: 用于启用 Left_Elevator_T 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Left_Elevator_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right elevator translation
  summary: 用于启用 Right_Elevator_T 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Right_Elevator_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left rudder translation
  summary: 用于启用 Left_Rudder_T 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Left_Rudder_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right rudder translation
  summary: 用于启用 Right_Rudder_T 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Right_Rudder_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 1 rotation
  summary: 用于启用 Wing1_R 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Wing1_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 1 left flap rotation
  summary: 用于启用 Wing1_Left_Flap_R 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Wing1_Left_Flap_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 1 right flap rotation
  summary: 用于启用 Wing1_Right_Flap_R 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Wing1_Right_Flap_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 1 left aileron rotation
  summary: 用于启用 Wing1_Left_Aileron_R 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Wing1_Left_Aileron_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 1 right aileron rotation
  summary: 用于启用 Wing1_Right_Aileron_R 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Wing1_Right_Aileron_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 1 left spoiler rotation
  summary: 用于启用 Wing1_Left_Spoiler_R 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Wing1_Left_Spoiler_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 1 right spoiler rotation
  summary: 用于启用 Wing1_Right_Spoiler_R 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Wing1_Right_Spoiler_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 2 rotation
  summary: 用于启用 Wing2_R 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Wing2_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 2 left flap rotation
  summary: 用于启用 Wing2_Left_Flap_R 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Wing2_Left_Flap_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Wing 2 right flap rotation
  summary: 用于启用 Wing2_Right_Flap_R 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Wing2_Right_Flap_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Horizontal stab rotation
  summary: 用于启用 Horizontal_Stab_R 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Horizontal_Stab_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left elevator rotation
  summary: 用于启用 Left_Elevator_R 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Left_Elevator_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right elevator rotation
  summary: 用于启用 Right_Elevator_R 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Right_Elevator_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left rudder rotation
  summary: 用于启用 Left_Rudder_R 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Left_Rudder_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right rudder rotation
  summary: 用于启用 Right_Rudder_R 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Right_Rudder_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Nose gear translation
  summary: 用于启用 Nose_Gear_T 输入端口的选项 off（默认）| on
  group: Gear
  block_parameter: Nose_Gear_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Nose wheel translation
  summary: 用于启用 Nose_Wheel_T 输入端口的选项 off（默认）| on
  group: Gear
  block_parameter: Nose_Wheel_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Nose gear door translation
  summary: 用于启用 Nose_Gear_Door_T 输入端口的选项 off（默认）| on
  group: Gear
  block_parameter: Nose_Gear_Door_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left gear translation
  summary: 启用 Left_Gear_T 输入端的选项 off（默认）| on
  group: Gear
  block_parameter: Left_Gear_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left wheel translation
  summary: 启用 Left_Wheel_T 输入端的选项 off（默认）| on
  group: Gear
  block_parameter: Left_Wheel_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left gear door translation
  summary: 启用 Left_Gear_Door_T 输入端的选项 off（默认）| on
  group: Gear
  block_parameter: Left_Gear_Door_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right gear translation
  summary: 启用 Right_Gear_T 输入端的选项 off（默认）| on
  group: Gear
  block_parameter: Right_Gear_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right wheel translation
  summary: 启用 Right_Wheel_T 输入端的选项 off（默认）| on
  group: Gear
  block_parameter: Right_Wheel_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right gear door translation
  summary: 启用 Right_Gear_Door_T 输入端的选项 off（默认）| on
  group: Gear
  block_parameter: Right_Gear_Door_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Nose gear rotation
  summary: 启用 Nose_Gear_R 输入端的选项 off（默认）| on
  group: Gear
  block_parameter: Nose_Gear_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Nose wheel rotation
  summary: 启用 Nose_Wheel_R 输入端的选项 off（默认）| on
  group: Gear
  block_parameter: Nose_Wheel_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Nose gear door rotation
  summary: 启用 Nose_Gear_Door_R 输入端的选项 off（默认）| on
  group: Gear
  block_parameter: Nose_Gear_Door_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left gear rotation
  summary: 启用 Left_Gear_R 输入端的选项 off（默认）| on
  group: Gear
  block_parameter: Left_Gear_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left wheel rotation
  summary: 启用 Left_Wheel_R 输入端的选项 off（默认）| on
  group: Gear
  block_parameter: Left_Wheel_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left gear door rotation
  summary: 启用 Left_Gear_Door_R 输入端的选项 off（默认）| on
  group: Gear
  block_parameter: Left_Gear_Door_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right gear rotation
  summary: 启用 Right_Gear_R 输入端的选项 off（默认）| on
  group: Gear
  block_parameter: Right_Gear_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right wheel rotation
  summary: 启用 Right_Wheel_R 输入端的选项 off（默认）| on
  group: Gear
  block_parameter: Right_Wheel_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right gear door rotation
  summary: 启用 Right_Gear_Door_R 输入端的选项 off（默认）| on
  group: Gear
  block_parameter: Right_Gear_Door_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Select input coordinate frame
  summary: 输入坐标系 NED（默认）| Fixed-frame | ICRF
  group: 输入
  block_parameter: GeoRadioButton
  values: '''NED''（默认）| ''Fixed-frame'' | ''ICRF'''
```

### Propulsion

### **Engine 1 translation** — 启用 Engine1\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Engine1\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Engine1_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 1 propeller translation** — 启用 Engine1\_Prop\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Engine1\_Prop\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Engine1_Prop_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 2 translation** — 启用 Engine2\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Engine2\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Engine2_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 2 propeller translation** — 启用 Engine2\_Prop\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Engine2\_Prop\_T** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine2_Prop_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 3 translation** — 用于启用 Engine3\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine3\_T** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine3_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 3 propeller translation** — 用于启用 Engine3\_Prop\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine3\_Prop\_T** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine3_Prop_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 4 translation** — 用于启用 Engine4\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine4\_T** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine4_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 4 propeller translation** — 用于启用 Engine4\_Prop\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine4\_Prop\_T** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine4_Prop_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 5 translation** — 用于启用 Engine5\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine5\_T** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine5_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 5 propeller translation** — 用于启用 Engine5\_Prop\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine5\_Prop\_T** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine5_Prop_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 6 translation** — 用于启用 Engine6\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine6\_T** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine6_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 6 propeller translation** — 用于启用 Engine6\_Prop\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine6\_Prop\_T** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine6_Prop_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 7 translation** — 用于启用 Engine7\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine7\_T** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine7_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 7 propeller translation** — 用于启用 Engine7\_Prop\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine7\_Prop\_T** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine7_Prop_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 8 translation** — 用于启用 Engine8\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine8\_T** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine8_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 8 propeller translation** — 用于启用 Engine8\_Prop\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine8\_Prop\_T** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine8_Prop_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 9 translation** — 用于启用 Engine9\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine9\_T** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine9_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 9 propeller translation** — 用于启用 Engine9\_Prop\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine9\_Prop\_T** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine9_Prop_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 10 translation** — 用于启用 Engine10\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine10\_T** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine10_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 10 propeller translation** — 用于启用 Engine10\_Prop\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine10\_Prop\_T** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine10_Prop_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 11 translation** — 用于启用 Engine11\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine11\_T** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine11_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 11 propeller translation** — 用于启用 Engine11\_Prop\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine11\_Prop\_T** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine11_Prop_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 12 translation** — 用于启用 Engine12\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine12\_T** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine12_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 12 propeller translation** — 用于启用 Engine12\_Prop\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine12\_Prop\_T** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine12_Prop_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 13 translation** — 用于启用 Engine13\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine13\_T** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine13_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 13 propeller translation** — 用于启用 Engine13\_Prop\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine13\_Prop\_T** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine13_Prop_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 14 translation** — 用于启用 Engine14\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine14\_T** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine14_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 14 propeller translation** — 用于启用 Engine14\_Prop\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine14\_Prop\_T** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine14_Prop_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 15 translation** — 用于启用 Engine15\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine15\_T** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine15_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 15 propeller translation** — 用于启用 Engine15\_Prop\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine15\_Prop\_T** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine15_Prop_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 16 translation** — 用于启用 Engine16\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine16\_T** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine16_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 16 propeller translation** — 用于启用 Engine16\_Prop\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine16\_Prop\_T** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine16_Prop_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 1 rotation** — 用于启用 Engine1\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine1\_R** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine1_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 1 propeller rotation** — 用于启用 Engine1\_Prop\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine1\_Prop\_R** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine1_Prop_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 2 rotation** — 用于启用 Engine2\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine2\_R** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine2_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 2 propeller rotation** — 用于启用 Engine2\_Prop\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine2\_Prop\_R** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine2_Prop_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 3 rotation** — 用于启用 Engine3\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine3\_R** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine3_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 3 propeller rotation** — 用于启用 Engine3\_Prop\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine3\_Prop\_R** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine3_Prop_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 4 rotation** — 用于启用 Engine4\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine4\_R** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine4_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 4 propeller rotation** — 用于启用 Engine4\_Prop\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine4\_Prop\_R** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine4_Prop_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 5 rotation** — 用于启用 Engine5\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine5\_R** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine5_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 5 propeller rotation** — 用于启用 Engine5\_Prop\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine5\_Prop\_R** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine5_Prop_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 6 rotation** — 用于启用 Engine6\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine6\_R** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine6_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 6 propeller rotation** — 用于启用 Engine6\_Prop\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine6\_Prop\_R** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine6_Prop_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 7 rotation** — 用于启用 Engine7\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine7\_R** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine7_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 7 propeller rotation** — 用于启用 Engine7\_Prop\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine7\_Prop\_R** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine7_Prop_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 8 rotation** — 用于启用 Engine8\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine8\_R** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine8_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 8 propeller rotation** — 用于启用 Engine8\_Prop\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine8\_Prop\_R** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine8_Prop_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 9 rotation** — 用于启用 Engine9\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine9\_R** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine9_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 9 propeller rotation** — 用于启用 Engine9\_Prop\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine9\_Prop\_R** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine9_Prop_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 10 rotation** — 用于启用 Engine10\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Engine10\_R** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine10_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 10 propeller rotation** — 用于启用 Engine10\_Prop\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Engine10\_Prop\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Engine10_Prop_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 11 rotation** — 用于启用 Engine11\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Engine11\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Engine11_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 11 propeller rotation** — 用于启用 Engine11\_Prop\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Engine11\_Prop\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Engine11_Prop_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 12 rotation** — 用于启用 Engine12\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Engine12\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Engine12_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 12 propeller rotation** — 用于启用 Engine12\_Prop\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Engine12\_Prop\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Engine12_Prop_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 13 rotation** — 用于启用 Engine13\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Engine13\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Engine13_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 13 propeller rotation** — 用于启用 Engine13\_Prop\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Engine13\_Prop\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Engine13_Prop_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 14 rotation** — 用于启用 Engine14\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Engine14\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Engine14_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 14 propeller rotation** — 用于启用 Engine14\_Prop\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Engine14\_Prop\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Engine14_Prop_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 15 rotation** — 用于启用 Engine15\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Engine15\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Engine15_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 15 propeller rotation** — 用于启用 Engine15\_Prop\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Engine15\_Prop\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Engine15_Prop_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 16 rotation** — 用于启用 Engine16\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Engine16\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Engine16_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 16 propeller rotation** — 用于启用 Engine16\_Prop\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Engine16\_Prop\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Engine16_Prop_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### Controls

### **Wing 1 translation** — 用于启用 Wing1\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Wing1\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Wing1_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Wing 1 left flap translation** — 用于启用 Wing1\_Left\_Flap\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Wing1\_Left\_Flap\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Wing1_Left_Flap_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Wing 1 right flap translation** — 用于启用 Wing1\_Right\_Flap\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Wing1\_Right\_Flap\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Wing1_Right_Flap_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Wing 1 left aileron translation** — 用于启用 Wing1\_Left\_Aileron\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Wing1\_Left\_Aileron\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Wing1_Left_Aileron_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Wing 1 right aileron translation** — 用于启用 Wing1\_Right\_Aileron\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Wing1\_Right\_Aileron\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Wing1_Right_Aileron_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Wing 1 left spoiler translation** — 用于启用 Wing1\_Left\_Spoiler\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Wing1\_Left\_Spoiler\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Wing1_Left_Spoiler_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Wing 1 right spoiler translation** — 用于启用 Wing1\_Right\_Spoiler\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Wing1\_Right\_Spoiler\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Wing1_Right_Spoiler_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Wing 2 translation** — 用于启用 Wing2\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Wing2\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Wing2_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Wing 2 left flap translation** — 用于启用 Wing2\_Left\_Flap\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Wing2\_Left\_Flap\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Wing2_Left_Flap_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Wing 2 right flap translation** — 用于启用 Wing2\_Right\_Flap\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Wing2\_Right\_Flap\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Wing2_Right_Flap_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Horizontal stab translation** — 用于启用 Horizontal\_Stab\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Horizontal\_Stab\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Horizontal_Stab_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Left elevator translation** — 用于启用 Left\_Elevator\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Elevator\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Left_Elevator_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right elevator translation** — 用于启用 Right\_Elevator\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Elevator\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Right_Elevator_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Left rudder translation** — 用于启用 Left\_Rudder\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Rudder\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Left_Rudder_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right rudder translation** — 用于启用 Right\_Rudder\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Rudder\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Right_Rudder_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Wing 1 rotation** — 用于启用 Wing1\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Wing1\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Wing1_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Wing 1 left flap rotation** — 用于启用 Wing1\_Left\_Flap\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Wing1\_Left\_Flap\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Wing1_Left_Flap_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Wing 1 right flap rotation** — 用于启用 Wing1\_Right\_Flap\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Wing1\_Right\_Flap\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Wing1_Right_Flap_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Wing 1 left aileron rotation** — 用于启用 Wing1\_Left\_Aileron\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Wing1\_Left\_Aileron\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Wing1_Left_Aileron_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Wing 1 right aileron rotation** — 用于启用 Wing1\_Right\_Aileron\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Wing1\_Right\_Aileron\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Wing1_Right_Aileron_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Wing 1 left spoiler rotation** — 用于启用 Wing1\_Left\_Spoiler\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Wing1\_Left\_Spoiler\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Wing1_Left_Spoiler_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Wing 1 right spoiler rotation** — 用于启用 Wing1\_Right\_Spoiler\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Wing1\_Right\_Spoiler\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Wing1_Right_Spoiler_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Wing 2 rotation** — 用于启用 Wing2\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Wing2\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Wing2_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Wing 2 left flap rotation** — 用于启用 Wing2\_Left\_Flap\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Wing2\_Left\_Flap\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Wing2_Left_Flap_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Wing 2 right flap rotation** — 用于启用 Wing2\_Right\_Flap\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Wing2\_Right\_Flap\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Wing2_Right_Flap_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Horizontal stab rotation** — 用于启用 Horizontal\_Stab\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Horizontal\_Stab\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Horizontal_Stab_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Left elevator rotation** — 用于启用 Left\_Elevator\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Elevator\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Left_Elevator_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right elevator rotation** — 用于启用 Right\_Elevator\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Elevator\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Right_Elevator_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Left rudder rotation** — 用于启用 Left\_Rudder\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Rudder\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Left_Rudder_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right rudder rotation** — 用于启用 Right\_Rudder\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Rudder\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Right_Rudder_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### Gear

### **Nose gear translation** — 用于启用 Nose\_Gear\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Nose\_Gear\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Nose_Gear_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Nose wheel translation** — 用于启用 Nose\_Wheel\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Nose\_Wheel\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Nose_Wheel_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Nose gear door translation** — 用于启用 Nose\_Gear\_Door\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Nose\_Gear\_Door\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Nose_Gear_Door_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Left gear translation** — 启用 Left\_Gear\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Gear\_T** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Left_Gear_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Left wheel translation** — 启用 Left\_Wheel\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Wheel\_T** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Left_Wheel_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Left gear door translation** — 启用 Left\_Gear\_Door\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Gear\_Door\_T** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Left_Gear_Door_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right gear translation** — 启用 Right\_Gear\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Gear\_T** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Right_Gear_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right wheel translation** — 启用 Right\_Wheel\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Wheel\_T** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Right_Wheel_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right gear door translation** — 启用 Right\_Gear\_Door\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Gear\_Door\_T** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Right_Gear_Door_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Nose gear rotation** — 启用 Nose\_Gear\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Nose\_Gear\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Nose_Gear_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Nose wheel rotation** — 启用 Nose\_Wheel\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Nose\_Wheel\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Nose_Wheel_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Nose gear door rotation** — 启用 Nose\_Gear\_Door\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Nose\_Gear\_Door\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Nose_Gear_Door_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Left gear rotation** — 启用 Left\_Gear\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Gear\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Left_Gear_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Left wheel rotation** — 启用 Left\_Wheel\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Wheel\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Left_Wheel_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Left gear door rotation** — 启用 Left\_Gear\_Door\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Gear\_Door\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Left_Gear_Door_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right gear rotation** — 启用 Right\_Gear\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Gear\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Right_Gear_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right wheel rotation** — 启用 Right\_Wheel\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Wheel\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Right_Wheel_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right gear door rotation** — 启用 Right\_Gear\_Door\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Gear\_Door\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Right_Gear_Door_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### 输入

### **Select input coordinate frame** — 输入坐标系 `NED`（默认）| `Fixed-frame` | `ICRF`

选择输入坐标系，以相对于北-东-地（NED）、固定坐标系（Fixed-frame）或国际天球参考系（ICRF）来定位航空航天器。

如果模型中包含关联的 Simulation 3D Scene Configuration 模块，Simulation 3D Custom Pack 模块将使用 Simulation 3D Scene Configuration 的坐标系。在这种情况下，**Select input coordinate frame** 可能被禁用。有关 Simulation 3D Custom Pack 模块坐标系的更多信息，请参阅算法。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `GeoRadioButton` |
| **值：** | `'NED'`（默认）| `'Fixed-frame'` | `'ICRF'` |
## 所属库

Aerospace Blockset / Animation / Simulation 3D

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023b 中引入**

### R2025a：Simulation 3D Custom Pack 模块现在与 Simulation 3D Scene Configuration 模块同步坐标系

Simulation 3D Custom Pack 模块有以下变更：

- **Geospatial** 选项卡已重命名为 **Input** 选项卡。
- 在 **Input** 选项卡上，**Select input coordinate frame** 窗格现在包含以下坐标系按钮：

  - **Fixed-frame** — 固定坐标系。当您选择此坐标系时，注释 `Fixed-frame` 将显示在载具模块图标下方。
  - **ICRF** — 国际天球参考系坐标系。当您选择此坐标系时，注释 `ICRF` 将显示在载具模块图标下方。
  - **NED** — 北-东-地坐标系。当您选择此坐标系时，注释 `NED` 将显示在载具模块图标下方。

  如果模型中包含 Simulation 3D 载具模块以及关联的 Simulation 3D Scene Configuration 模块，Simulation 3D Custom Pack 的 **Input** 选项卡选项可能被禁用。在这种情况下，Simulation 3D Custom Pack 将与 Simulation 3D Scene Configuration 模块同步坐标系。
- 坐标系将作为注释显示在模块下方。
- **Enable geospatial correction** 和 **Direction of x-axis (degrees clockwise from north)** 参数已被移除。

### R2024a：Simulation 3D Custom Pack 模块现在支持地心地图（ECEF）输入坐标系

为了支持用于平移输入的 ECEF 坐标系，Simulation 3D Custom Pack 模块已更新。请将这些参数与 Simulation 3D Scene Configuration 模块中的 **Use Earth center as origin (ECEF)** 参数一起使用。

- **选择输入坐标系**

  - **ECEF** — ECEF 输入坐标系。当您选择此坐标系时，注释 `Origin: Earth center (ECEF)` 将显示在载具模块图标下方。
  - **NED** — NED 坐标系。在 R2024a 之前，NED 是唯一支持的坐标系。
- **Direction of x-axis (degrees clockwise from north)** — *x* 轴方向。当您选中 **Enable geospatial correction** 复选框时，此参数启用。

## 描述

为自定义飞行器生成平移和旋转信息

Simulation 3D Custom Pack 模块为 **Type** 设置为 `Custom` 的 Simulation 3D Aircraft 模块创建平移和旋转信息。使用 Simulation 3D Custom Pack 模块将平移和旋转信息提供给 Simulation 3D Aircraft 模块的 **Translation** 和 **Rotation** 输入端口。
