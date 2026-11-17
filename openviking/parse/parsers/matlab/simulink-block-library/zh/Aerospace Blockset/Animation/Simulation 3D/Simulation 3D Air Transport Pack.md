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
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Air Transport Pack

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
- name: Engine2_T
  summary: 发动机 2 平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine3_T
  summary: 发动机 3 平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine4_T
  summary: 发动机 4 平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Rudder_T
  summary: 方向舵平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Elevator_T
  summary: 升降舵平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Horizontal_Stab_T
  summary: 水平安定面平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Left_Aileron_T
  summary: 左副翼平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Right_Aileron_T
  summary: 右副翼平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Flaps1_T
  summary: 襟翼组 1 平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Flaps2_T
  summary: 襟翼组 2 平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Left_Spoiler_T
  summary: 左扰流板平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Right_Spoiler_T
  summary: 右扰流板平移 1×3 矩阵
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
- name: Nose_Gear_Door1_T
  summary: 前起落架舱门 1 平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Nose_Gear_Door2_T
  summary: 前起落架舱门 2 平移 1×3 矩阵
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
- name: Left_Gear_Link_T
  summary: 左起落架连杆平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Left_Gear_Door1_T
  summary: 左起落架舱门 1 平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Left_Gear_Door2_T
  summary: 左起落架舱门 2 平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Left_Gear_Door2_2_T
  summary: 左起落架舱门 2.2 平移 1×3 矩阵
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
- name: Right_Gear_Link_T
  summary: 右起落架连杆平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Right_Gear_Door1_T
  summary: 右起落架舱门 1 平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Right_Gear_Door2_T
  summary: 右起落架舱门 2 平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Right_Gear_Door2_2_T
  summary: 右起落架舱门 2.2 平移 1×3 矩阵
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
- name: Engine2_R
  summary: 发动机 2 旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine3_R
  summary: 发动机 3 旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine4_R
  summary: 发动机 4 旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Rudder_R
  summary: 方向舵旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Elevator_R
  summary: 升降舵旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Horizontal_Stab_R
  summary: 水平安定面旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Left_Aileron_R
  summary: 左副翼旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Right_Aileron_R
  summary: 右副翼旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Flaps1_R
  summary: 襟翼组 1 旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Flaps2_R
  summary: 襟翼组 2 旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Left_Spoiler_R
  summary: 左扰流板旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Right_Spoiler_R
  summary: 右扰流板旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Nose_Gear_R
  summary: 前起落架旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Nose_Wheel_R
  summary: 前轮旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Nose_Gear_Door1_R
  summary: 前起落架舱门 1 旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Nose_Gear_Door2_R
  summary: 前起落架舱门 2 旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Left_Gear_R
  summary: 左起落架旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Left_Wheel_R
  summary: 左轮旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Left_Gear_Link_R
  summary: 左起落架连杆旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Left_Gear_Door1_R
  summary: 左起落架舱门 1 旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Left_Gear_Door2_R
  summary: 左起落架舱门 2 旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Left_Gear_Door2_2_R
  summary: 左起落架舱门 2.2 旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Right_Gear_R
  summary: 右起落架旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Right_Wheel_R
  summary: 右轮旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Right_Gear_Link_R
  summary: 右起落架连杆旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Right_Gear_Door1_R
  summary: 右起落架舱门 1 旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Right_Gear_Door2_R
  summary: 右起落架舱门 2 旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Right_Gear_Door2_2_R
  summary: 右起落架舱门 2.2 旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Translation
  summary: 飞机平移 30×3 数组
  direction: output
- name: Rotation
  summary: Aircraft rotation 30×3 数组
  direction: output
```

### 输入

### **Body\_T** — 机体平移 1×3 矩阵

机体平移，指定为 1×3 矩阵。

**数据类型：** `single` | `double`

### **Engine1\_T** — 发动机 1 平移 1×3 矩阵

发动机 1 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Engine 1 translation** 参数。

**数据类型：** `single` | `double`

### **Engine2\_T** — 发动机 2 平移 1×3 矩阵

发动机 2 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Engine 2 translation** 参数。

**数据类型：** `single` | `double`

### **Engine3\_T** — 发动机 3 平移 1×3 矩阵

发动机 3 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Engine 3 translation** 参数。

**数据类型：** `single` | `double`

### **Engine4\_T** — 发动机 4 平移 1×3 矩阵

发动机 4 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Engine 4 translation** 参数。

**数据类型：** `single` | `double`

### **Rudder\_T** — 方向舵平移 1×3 矩阵

方向舵平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Rudder translation** 参数。

**数据类型：** `single` | `double`

### **Elevator\_T** — 升降舵平移 1×3 矩阵

升降舵平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Elevator translation** 参数。

**数据类型：** `single` | `double`

### **Horizontal\_Stab\_T** — 水平安定面平移 1×3 矩阵

水平安定面平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Horizontal stab translation** 参数。

**数据类型：** `single` | `double`

### **Left\_Aileron\_T** — 左副翼平移 1×3 矩阵

左副翼平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Left aileron translation** 参数。

**数据类型：** `single` | `double`

### **Right\_Aileron\_T** — 右副翼平移 1×3 矩阵

右副翼平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Right aileron translation** 参数。

**数据类型：** `single` | `double`

### **Flaps1\_T** — 襟翼组 1 平移 1×3 矩阵

襟翼组 1 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Flaps set 1 translation** 参数。

**数据类型：** `single` | `double`

### **Flaps2\_T** — 襟翼组 2 平移 1×3 矩阵

襟翼组 2 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Flaps set 2 translation** 参数。

**数据类型：** `single` | `double`

### **Left\_Spoiler\_T** — 左扰流板平移 1×3 矩阵

左扰流板平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Left spoiler translation** 参数。

**数据类型：** `single` | `double`

### **Right\_Spoiler\_T** — 右扰流板平移 1×3 矩阵

右扰流板平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Right spoiler translation** 参数。

**数据类型：** `single` | `double`

### **Nose\_Gear\_T** — 前起落架平移 1×3 矩阵

前起落架平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Nose gear translation** 参数。

**数据类型：** `single` | `double`

### **Nose\_Wheel\_T** — 前轮平移 1×3 矩阵

前轮平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Nose wheel translation** 参数。

**数据类型：** `single` | `double`

### **Nose\_Gear\_Door1\_T** — 前起落架舱门 1 平移 1×3 矩阵

前起落架舱门 1 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Nose gear door 1 translation** 参数。

**数据类型：** `single` | `double`

### **Nose\_Gear\_Door2\_T** — 前起落架舱门 2 平移 1×3 矩阵

前起落架舱门 2 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Nose gear door 2 translation** 参数。

**数据类型：** `single` | `double`

### **Left\_Gear\_T** — 左起落架平移 1×3 矩阵

左起落架平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Left gear translation** 参数。

**数据类型：** `single` | `double`

### **Left\_Wheel\_T** — 左轮平移 1×3 矩阵

左轮平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Left wheel translation** 参数。

**数据类型：** `single` | `double`

### **Left\_Gear\_Link\_T** — 左起落架连杆平移 1×3 矩阵

左起落架连杆平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Left gear link translation** 参数。

**数据类型：** `single` | `double`

### **Left\_Gear\_Door1\_T** — 左起落架舱门 1 平移 1×3 矩阵

左起落架舱门 1 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Left gear door 1 translation** 参数。

**数据类型：** `single` | `double`

### **Left\_Gear\_Door2\_T** — 左起落架舱门 2 平移 1×3 矩阵

左起落架舱门 2 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Left gear door 2 translation** 参数。

**数据类型：** `single` | `double`

### **Left\_Gear\_Door2\_2\_T** — 左起落架舱门 2.2 平移 1×3 矩阵

左起落架舱门 2.2 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Left gear door 2.2 translation** 参数。

**数据类型：** `single` | `double`

### **Right\_Gear\_T** — 右起落架平移 1×3 矩阵

右起落架平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Right gear translation** 参数。

**数据类型：** `single` | `double`

### **Right\_Wheel\_T** — 右轮平移 1×3 矩阵

右轮平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Right wheel translation** 参数。

**数据类型：** `single` | `double`

### **Right\_Gear\_Link\_T** — 右起落架连杆平移 1×3 矩阵

右起落架连杆平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Right gear link translation** 参数。

**数据类型：** `single` | `double`

### **Right\_Gear\_Door1\_T** — 右起落架舱门 1 平移 1×3 矩阵

右起落架舱门 1 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Right gear door 1 translation** 参数。

**数据类型：** `single` | `double`

### **Right\_Gear\_Door2\_T** — 右起落架舱门 2 平移 1×3 矩阵

右起落架舱门 2 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Right gear door 2 translation** 参数。

**数据类型：** `single` | `double`

### **Right\_Gear\_Door2\_2\_T** — 右起落架舱门 2.2 平移 1×3 矩阵

右起落架舱门 2.2 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Right gear door 2.2 translation** 参数。

**数据类型：** `single` | `double`

### **Body\_R** — 机体旋转 1×3 矩阵

机体旋转，指定为 1×3 矩阵。

**数据类型：** `single` | `double`

### **Engine1\_R** — 发动机 1 旋转 1×3 矩阵

发动机 1 旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Engine 1 rotation** 参数。

**数据类型：** `single` | `double`

### **Engine2\_R** — 发动机 2 旋转 1×3 矩阵

发动机 2 旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Engine 2 rotation** 参数。

**数据类型：** `single` | `double`

### **Engine3\_R** — 发动机 3 旋转 1×3 矩阵

发动机 3 旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Engine 3 rotation** 参数。

**数据类型：** `single` | `double`

### **Engine4\_R** — 发动机 4 旋转 1×3 矩阵

发动机 4 旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Engine 4 rotation** 参数。

**数据类型：** `single` | `double`

### **Rudder\_R** — 方向舵旋转 1×3 矩阵

方向舵旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Rudder rotation** 参数。

**数据类型：** `single` | `double`

### **Elevator\_R** — 升降舵旋转 1×3 矩阵

升降舵旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Elevator rotation** 参数。

**数据类型：** `single` | `double`

### **Horizontal\_Stab\_R** — 水平安定面旋转 1×3 矩阵

水平安定面旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Horizontal stab rotation** 参数。

**数据类型：** `single` | `double`

### **Left\_Aileron\_R** — 左副翼旋转 1×3 矩阵

左副翼旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Left aileron rotation** 参数。

**数据类型：** `single` | `double`

### **Right\_Aileron\_R** — 右副翼旋转 1×3 矩阵

右副翼旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Right aileron rotation** 参数。

**数据类型：** `single` | `double`

### **Flaps1\_R** — 襟翼组 1 旋转 1×3 矩阵

襟翼组 1 旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Flaps set 1 rotation** 参数。

**数据类型：** `single` | `double`

### **Flaps2\_R** — 襟翼组 2 旋转 1×3 矩阵

襟翼组 2 旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Flaps set 2 rotation** 参数。

**数据类型：** `single` | `double`

### **Left\_Spoiler\_R** — 左扰流板旋转 1×3 矩阵

左扰流板旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Left spoiler rotation** 参数。

**数据类型：** `single` | `double`

### **Right\_Spoiler\_R** — 右扰流板旋转 1×3 矩阵

右扰流板旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Right spoiler rotation** 参数。

**数据类型：** `single` | `double`

### **Nose\_Gear\_R** — 前起落架旋转 1×3 矩阵

前起落架旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Nose gear rotation** 参数。

**数据类型：** `single` | `double`

### **Nose\_Wheel\_R** — 前轮旋转 1×3 矩阵

前轮旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Nose wheel rotation** 参数。

**数据类型：** `single` | `double`

### **Nose\_Gear\_Door1\_R** — 前起落架舱门 1 旋转 1×3 矩阵

前起落架舱门 1 旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Nose gear door 1 rotation** 参数。

**数据类型：** `single` | `double`

### **Nose\_Gear\_Door2\_R** — 前起落架舱门 2 旋转 1×3 矩阵

前起落架舱门 2 旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Nose gear door 2 rotation** 参数。

**数据类型：** `single` | `double`

### **Left\_Gear\_R** — 左起落架旋转 1×3 矩阵

左起落架旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Left gear rotation** 参数。

**数据类型：** `single` | `double`

### **Left\_Wheel\_R** — 左轮旋转 1×3 矩阵

左轮旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Left wheel rotation** 参数。

**数据类型：** `single` | `double`

### **Left\_Gear\_Link\_R** — 左起落架连杆旋转 1×3 矩阵

左起落架连杆旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Left gear link rotation** 参数。

**数据类型：** `single` | `double`

### **Left\_Gear\_Door1\_R** — 左起落架舱门 1 旋转 1×3 矩阵

左起落架舱门 1 旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Left gear door 1 rotation** 参数。

**数据类型：** `single` | `double`

### **Left\_Gear\_Door2\_R** — 左起落架舱门 2 旋转 1×3 矩阵

左起落架舱门 2 旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Left gear door 2 rotation** 参数。

**数据类型：** `single` | `double`

### **Left\_Gear\_Door2\_2\_R** — 左起落架舱门 2.2 旋转 1×3 矩阵

左起落架舱门 2.2 旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Left gear door 2.2 rotation** 参数。

**数据类型：** `single` | `double`

### **Right\_Gear\_R** — 右起落架旋转 1×3 矩阵

右起落架旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Right gear rotation** 参数。

**数据类型：** `single` | `double`

### **Right\_Wheel\_R** — 右轮旋转 1×3 矩阵

右轮旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Right wheel rotation** 参数。

**数据类型：** `single` | `double`

### **Right\_Gear\_Link\_R** — 右起落架连杆旋转 1×3 矩阵

右起落架连杆旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Right gear link rotation** 参数。

**数据类型：** `single` | `double`

### **Right\_Gear\_Door1\_R** — 右起落架舱门 1 旋转 1×3 矩阵

右起落架舱门 1 旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Right gear door 1 rotation** 参数。

**数据类型：** `single` | `double`

### **Right\_Gear\_Door2\_R** — 右起落架舱门 2 旋转 1×3 矩阵

右起落架舱门 2 旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Right gear door 2 rotation** 参数。

**数据类型：** `single` | `double`

### **Right\_Gear\_Door2\_2\_R** — 右起落架舱门 2.2 旋转 1×3 矩阵

右起落架舱门 2.2 旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Right gear door 2.2 rotation** 参数。

**数据类型：** `single` | `double`
### 输出

### **Translation** — 飞机平移 `30`×`3` 数组

空中运输飞机的飞机平移，以 `30`×`3` 数组形式返回。该信号包含平移 [*X*，*Y*，*Z*]，单位为米，数组的每一行对应飞机的一个骨骼。

该平移适用于 `Air transport` 类型的以下骨骼。

| 骨骼 | 索引 |
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

### **Rotation** — Aircraft rotation `30`×`3` 数组

用于 air transport aircraft 的 Aircraft rotation，返回为
`30`×`3` 数组。

该 rotation 应用于与 Translation 端口所列相同的 bones。

该信号包含 rotation [roll, pitch, yaw]，单位为弧度，数组的每一行
对应 aircraft 的一个 bone。
## 参数
```yaml
parameters:
- name: Engine 1 translation
  summary: 用于启用 Engine1_T 输入端口的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine1_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 2 translation
  summary: 用于启用 Engine2_T 输入端口的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine2_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 3 translation
  summary: 用于启用 Engine3_T 输入端口的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine3_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 4 translation
  summary: 用于启用 Engine4_T 输入端口的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine4_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 1 rotation
  summary: 用于启用 Engine1_R 输入端口的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine1_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 2 rotation
  summary: 用于启用 Engine2_R 输入端口的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine2_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 3 rotation
  summary: 用于启用 Engine3_R 输入端口的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine3_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine 4 rotation
  summary: 用于启用 Engine4_R 输入端口的选项 off（默认）| on
  group: Propulsion
  block_parameter: Engine4_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Rudder translation
  summary: 用于启用 Rudder_T 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Rudder_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Elevator translation
  summary: 用于启用 Elevator_T 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Elevator_T
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
- name: Left aileron translation
  summary: 用于启用 Left_Aileron_T 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Left_Aileron_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right aileron translation
  summary: 用于启用 Right_Aileron_T 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Right_Aileron_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Flaps set 1 translation
  summary: 用于启用 Flaps1_T 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Flaps1_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Flaps set 2 translation
  summary: 用于启用 Flaps2_T 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Flaps2_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left spoiler translation
  summary: 用于启用 Left_Spoiler_T 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Left_Spoiler_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right spoiler translation
  summary: 用于启用 Right_Spoiler_T 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Right_Spoiler_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Rudder rotation
  summary: 用于启用 Rudder_R 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Rudder_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Elevator rotation
  summary: 用于启用 Elevator_R 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Elevator_R
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
- name: Left aileron rotation
  summary: 用于启用 Left_Aileron_R 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Left_Aileron_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right aileron rotation
  summary: 用于启用 Right_Aileron_R 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Right_Aileron_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Flaps set 1 rotation
  summary: 用于启用 Flaps1_R 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Flaps1_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Flaps set 2 rotation
  summary: 用于启用 Flaps2_R 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Flaps2_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left spoiler rotation
  summary: 用于启用 Left_Spoiler_R 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Left_Spoiler_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right spoiler rotation
  summary: 用于启用 Right_Spoiler_R 输入端口的选项 off（默认）| on
  group: Controls
  block_parameter: Right_Spoiler_R
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
- name: Nose gear door 1 translation
  summary: 用于启用 Nose_Gear_Door1_T 输入端口的选项 off（默认）| on
  group: Gear
  block_parameter: Nose_Gear_Door1_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Nose gear door 2 translation
  summary: 用于启用 Nose_Gear_Door2_T 输入端口的选项 off（默认）| on
  group: Gear
  block_parameter: Nose_Gear_Door2_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left gear translation
  summary: 用于启用 Left_Gear_T 输入端口的选项 off（默认）| on
  group: Gear
  block_parameter: Left_Gear_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left wheel translation
  summary: 用于启用 Left_Wheel_T 输入端口的选项 off（默认）| on
  group: Gear
  block_parameter: Left_Wheel_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left gear link translation
  summary: 用于启用 Left_Gear_Link_T 输入端口的选项 off（默认）| on
  group: Gear
  block_parameter: Left_Gear_Link_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left gear door 1 translation
  summary: 用于启用 Left_Gear_Door1_T 输入端口的选项 off（默认）| on
  group: Gear
  block_parameter: Left_Gear_Door1_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left gear door 2 translation
  summary: 用于启用 Left_Gear_Door2_T 输入端口的选项 off（默认）| on
  group: Gear
  block_parameter: Left_Gear_Door2_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left gear door 2.2 translation
  summary: 用于启用 Left_Gear_Door2_2_T 输入端口的选项 off（默认）| on
  group: Gear
  block_parameter: Left_Gear_Door2_2_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right gear translation
  summary: 用于启用 Right_Gear_T 输入端口的选项 off（默认）| on
  group: Gear
  block_parameter: Right_Gear_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right wheel translation
  summary: 用于启用 Right_Wheel_T 输入端口的选项 off（默认）| on
  group: Gear
  block_parameter: Right_Wheel_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right gear link translation
  summary: 用于启用 Right_Gear_Link_T 输入端口的选项 off（默认）| on
  group: Gear
  block_parameter: Right_Gear_Link_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right gear door 1 translation
  summary: 用于启用 Right_Gear_Door1_T 输入端口的选项 off（默认）| on
  group: Gear
  block_parameter: Right_Gear_Door1_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right gear door 2 translation
  summary: 用于启用 Right_Gear_Door2_T 输入端口的选项 off（默认）| on
  group: Gear
  block_parameter: Right_Gear_Door2_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right gear door 2.2 translation
  summary: 用于启用 Right_Gear_Door2_2_T 输入端口的选项 off（默认）| on
  group: Gear
  block_parameter: Right_Gear_Door2_2_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Nose gear rotation
  summary: 用于启用 Nose_Gear_R 输入端口的选项 off（默认）| on
  group: Gear
  block_parameter: Nose_Gear_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Nose wheel rotation
  summary: 用于启用 Nose_Wheel_R 输入端口的选项 off（默认）| on
  group: Gear
  block_parameter: Nose_Wheel_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Nose gear door 1 rotation
  summary: 用于启用 Nose_Gear_Door1_R 输入端口的选项 off（默认）| on
  group: Gear
  block_parameter: Nose_Gear_Door1_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Nose gear door 2 rotation
  summary: 用于启用 Nose_Gear_Door2_T 输入端口的选项 off（默认）| on
  group: Gear
  block_parameter: Nose_Gear_Door2_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left gear rotation
  summary: 启用 Left_Gear_R 输入端口的选项 off（默认）| on
  group: Gear
  block_parameter: Left_Gear_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left wheel rotation
  summary: 启用 Left_Wheel_R 输入端口的选项 off（默认）| on
  group: Gear
  block_parameter: Left_Wheel_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left gear link rotation
  summary: 启用 Left_Gear_Link_R 输入端口的选项 off（默认）| on
  group: Gear
  block_parameter: Left_Gear_Link_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left gear door 1 rotation
  summary: 启用 Left_Gear_Door1_R 输入端口的选项 off（默认）| on
  group: Gear
  block_parameter: Left_Gear_Door1_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left gear door 2 rotation
  summary: 启用 Left_Gear_Door2_R 输入端口的选项 off（默认）| on
  group: Gear
  block_parameter: Left_Gear_Door2_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left gear door 2.2 rotation
  summary: 启用 Left_Gear_Door2_2_R 输入端口的选项 off（默认）| on
  group: Gear
  block_parameter: Left_Gear_Door2_2_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right gear rotation
  summary: 启用 Right_Gear_R 输入端口的选项 off（默认）| on
  group: Gear
  block_parameter: Right_Gear_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right wheel rotation
  summary: 启用 Right_Wheel_R 输入端口的选项 off（默认）| on
  group: Gear
  block_parameter: Right_Wheel_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right gear link rotation
  summary: 启用 Right_Gear_Link_R 输入端口的选项 off（默认）| on
  group: Gear
  block_parameter: Right_Gear_Link_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right gear door 1 rotation
  summary: 启用 Right_Gear_Door1_R 输入端口的选项 off（默认）| on
  group: Gear
  block_parameter: Right_Gear_Door1_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right gear door 2 rotation
  summary: 启用 Right_Gear_Door2_R 输入端口的选项 off（默认）| on
  group: Gear
  block_parameter: Right_Gear_Door2_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right gear door 2.2 rotation
  summary: 启用 Right_Gear_Door2_2_R 输入端口的选项 off（默认）| on
  group: Gear
  block_parameter: Right_Gear_Door2_2_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Select input coordinate frame
  summary: 输入坐标系 NED（默认）| Fixed-frame | ICRF
  group: 输入
  block_parameter: GeoRadioButton
  values: '''NED''（默认）| ''Fixed-frame'' | ''ICRF'''
```

### Propulsion

### **Engine 1 translation** — 用于启用 Engine1\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Engine1\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Engine1_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 2 translation** — 用于启用 Engine2\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Engine2\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Engine2_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 3 translation** — 用于启用 Engine3\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Engine3\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Engine3_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 4 translation** — 用于启用 Engine4\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Engine4\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Engine4_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 1 rotation** — 用于启用 Engine1\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Engine1\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Engine1_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 2 rotation** — 用于启用 Engine2\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Engine2\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Engine2_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 3 rotation** — 用于启用 Engine3\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Engine3\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Engine3_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine 4 rotation** — 用于启用 Engine4\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Engine4\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Engine4_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### Controls

### **Rudder translation** — 用于启用 Rudder\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Rudder\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Rudder_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Elevator translation** — 用于启用 Elevator\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Elevator\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Elevator_T` |
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

### **Left aileron translation** — 用于启用 Left\_Aileron\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Aileron\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Left_Aileron_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right aileron translation** — 用于启用 Right\_Aileron\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Aileron\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Right_Aileron_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Flaps set 1 translation** — 用于启用 Flaps1\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Flaps1\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Flaps1_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Flaps set 2 translation** — 用于启用 Flaps2\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Flaps2\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Flaps2_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Left spoiler translation** — 用于启用 Left\_Spoiler\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Spoiler\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Left_Spoiler_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right spoiler translation** — 用于启用 Right\_Spoiler\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Spoiler\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Right_Spoiler_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Rudder rotation** — 用于启用 Rudder\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Rudder\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Rudder_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Elevator rotation** — 用于启用 Elevator\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Elevator\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Elevator_R` |
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

### **Left aileron rotation** — 用于启用 Left\_Aileron\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Aileron\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Left_Aileron_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right aileron rotation** — 用于启用 Right\_Aileron\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Aileron\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Right_Aileron_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Flaps set 1 rotation** — 用于启用 Flaps1\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Flaps1\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Flaps1_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Flaps set 2 rotation** — 用于启用 Flaps2\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Flaps2\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Flaps2_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Left spoiler rotation** — 用于启用 Left\_Spoiler\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Spoiler\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Left_Spoiler_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right spoiler rotation** — 用于启用 Right\_Spoiler\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Spoiler\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Right_Spoiler_R` |
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

### **Nose gear door 1 translation** — 用于启用 Nose\_Gear\_Door1\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Nose\_Gear\_Door1\_T** 输入
端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Nose_Gear_Door1_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Nose gear door 2 translation** — 用于启用 Nose\_Gear\_Door2\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Nose\_Gear\_Door2\_T** 输入
端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Nose_Gear_Door2_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Left gear translation** — 用于启用 Left\_Gear\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Gear\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Left_Gear_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Left wheel translation** — 用于启用 Left\_Wheel\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Wheel\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Left_Wheel_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Left gear link translation** — 用于启用 Left\_Gear\_Link\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Gear\_Link\_T** 输入
端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Left_Gear_Link_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Left gear door 1 translation** — 用于启用 Left\_Gear\_Door1\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Gear\_Door1\_T** 输入
端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Left_Gear_Door1_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Left gear door 2 translation** — 用于启用 Left\_Gear\_Door2\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Gear\_Door2\_T** 输入
端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Left_Gear_Door2_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Left gear door 2.2 translation** — 用于启用 Left\_Gear\_Door2\_2\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Gear\_Door2\_2\_T** 输入
端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Left_Gear_Door2_2_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right gear translation** — 用于启用 Right\_Gear\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Gear\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Right_Gear_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right wheel translation** — 用于启用 Right\_Wheel\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Wheel\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Right_Wheel_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right gear link translation** — 用于启用 Right\_Gear\_Link\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Gear\_Link\_T** 输入
端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Right_Gear_Link_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right gear door 1 translation** — 用于启用 Right\_Gear\_Door1\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Gear\_Door1\_T** 输入
端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Right_Gear_Door1_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right gear door 2 translation** — 用于启用 Right\_Gear\_Door2\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Gear\_Door2\_T** 输入
端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Right_Gear_Door2_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right gear door 2.2 translation** — 用于启用 Right\_Gear\_Door2\_2\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Gear\_Door2\_2\_T**
输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Right_Gear_Door2_2_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Nose gear rotation** — 用于启用 Nose\_Gear\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Nose\_Gear\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Nose_Gear_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Nose wheel rotation** — 用于启用 Nose\_Wheel\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Nose\_Wheel\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Nose_Wheel_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Nose gear door 1 rotation** — 用于启用 Nose\_Gear\_Door1\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Nose\_Gear\_Door1\_R** 输入
端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Nose_Gear_Door1_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Nose gear door 2 rotation** — 用于启用 Nose\_Gear\_Door2\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Nose\_Gear\_Door2\_T** 输入
端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Nose_Gear_Door2_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Left gear rotation** — 启用 Left\_Gear\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Gear\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Left_Gear_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Left wheel rotation** — 启用 Left\_Wheel\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Wheel\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Left_Wheel_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Left gear link rotation** — 启用 Left\_Gear\_Link\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Gear\_Link\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Left_Gear_Link_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Left gear door 1 rotation** — 启用 Left\_Gear\_Door1\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Gear\_Door1\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Left_Gear_Door1_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Left gear door 2 rotation** — 启用 Left\_Gear\_Door2\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Gear\_Door2\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Left_Gear_Door2_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Left gear door 2.2 rotation** — 启用 Left\_Gear\_Door2\_2\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Gear\_Door2\_2\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Left_Gear_Door2_2_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right gear rotation** — 启用 Right\_Gear\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Gear\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Right_Gear_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right wheel rotation** — 启用 Right\_Wheel\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Wheel\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Right_Wheel_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right gear link rotation** — 启用 Right\_Gear\_Link\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Gear\_Link\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Right_Gear_Link_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right gear door 1 rotation** — 启用 Right\_Gear\_Door1\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Gear\_Door1\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Right_Gear_Door1_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right gear door 2 rotation** — 启用 Right\_Gear\_Door2\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Gear\_Door2\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Right_Gear_Door2_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right gear door 2.2 rotation** — 启用 Right\_Gear\_Door2\_2\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Gear\_Door2\_2\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Right_Gear_Door2_2_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### 输入

### **Select input coordinate frame** — 输入坐标系 `NED`（默认）| `Fixed-frame` | `ICRF`

选择输入坐标系，以相对于北-东-地（NED）、固定坐标系（Fixed-frame）或国际天球参考系（ICRF）来定位航空航天器。

如果模型中包含关联的 Simulation 3D Scene Configuration 模块，则 Simulation 3D Air Transport Pack 模块使用 Simulation 3D Scene Configuration 的坐标系。在这种情况下，**Select input coordinate frame** 可能被禁用。有关 Simulation 3D Air Transport Pack 模块坐标系的详细信息，请参阅 Algorithms。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter：** | `GeoRadioButton` |
| **值**：| `'NED'`（默认）| `'Fixed-frame'` | `'ICRF'` |
## 所属库

Aerospace Blockset / Animation / Simulation 3D

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023b 中引入**

### R2025a：Simulation 3D Air Transport Pack 模块现在与 Simulation 3D Scene Configuration 模块同步坐标系

Simulation 3D Air Transport Pack 模块有以下变更：

- **Geospatial** 选项卡已重命名为 **Input** 选项卡。
- 在 **Input** 选项卡上，**Select input coordinate frame** 窗格现在包含以下坐标系按钮：

  - **Fixed-frame** — 固定坐标系。当您选择此坐标系时，注释 `Fixed-frame` 会显示在载具模块图标下方。
  - **ICRF** — 国际天球参考系坐标系。当您选择此坐标系时，注释 `ICRF` 会显示在载具模块图标下方。
  - **NED** — 北-东-地坐标系。当您选择此坐标系时，注释 `NED` 会显示在载具模块图标下方。

  如果模型中包含 Simulation 3D 载具模块以及关联的 Simulation 3D Scene Configuration 模块，则 Simulation 3D Air Transport Pack 的 **Input** 选项卡选项可能被禁用。在这种情况下，Simulation 3D Air Transport Pack 会与 Simulation 3D Scene Configuration 模块同步坐标系。
- 坐标系显示为模块下方的注释。
- **Enable geospatial correction** 和 **Direction of x-axis (degrees clockwise from north)** 参数已被移除。

### R2024a：Simulation 3D Air Transport Pack 模块现在支持地心地球固定（ECEF）输入坐标系

为支持用于平移输入的 ECEF 坐标系，Simulation 3D Air Transport Pack 模块已更新。请将这些参数与 Simulation 3D Scene Configuration 模块中的 **Use Earth center as origin (ECEF)** 参数一起使用。

- **选择输入坐标系**

  - **ECEF** — ECEF 输入坐标系。当您选择此坐标系时，注释 `Origin: Earth center (ECEF)` 会显示在载具模块图标下方。
  - **NED** — NED 坐标系。在 R2024a 之前，NED 是唯一受支持的坐标系。
- **Direction of x-axis (degrees clockwise from north)** — *x* 轴方向。当您选中 **Enable geospatial correction** 复选框时，此参数启用。

## 描述

为空中运输航空器生成平移和旋转信息

Simulation 3D Air Transport Pack 模块为 **Type** 设置为 `Air transport` 的 Simulation 3D Aircraft 模块创建平移和旋转信息。使用 Simulation 3D Air Transport Pack 模块向 Simulation 3D Aircraft 模块的 **Translation** 和 **Rotation** 输入端口提供平移和旋转信息。
