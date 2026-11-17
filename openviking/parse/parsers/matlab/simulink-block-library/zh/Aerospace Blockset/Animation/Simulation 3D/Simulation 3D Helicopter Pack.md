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
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Helicopter Pack

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
- name: Rotor1_T
  summary: 旋翼 1 平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Rotor2_T
  summary: 旋翼 2 平移 1×3 矩阵
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
- name: Left_Gear_Door1_T
  summary: 左起落架舱门 1 平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Left_Gear_Door2_T
  summary: 左起落架舱门 2 平移 1×3 矩阵
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
- name: Right_Gear_Door1_T
  summary: 右起落架舱门 1 平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Right_Gear_Door2_T
  summary: 右起落架舱门 2 平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Sensor1_T
  summary: 传感器 1 平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Sensor2_T
  summary: 传感器 2 平移 1×3 矩阵
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
- name: Rotor1_R
  summary: 旋翼 1 旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Rotor2_R
  summary: 旋翼 2 旋转 1×3 矩阵
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
- name: Left_Gear_Door1_R
  summary: 左起落架舱门 1 旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Left_Gear_Door2_R
  summary: 左起落架舱门 2 旋转 1×3 矩阵
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
- name: Right_Gear_Door1_R
  summary: 右起落架舱门 1 旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Right_Gear_Door2_R
  summary: 右起落架舱门 2 旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Sensor1_R
  summary: 传感器 1 旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Sensor2_R
  summary: 传感器 2 旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Translation
  summary: 直升机平移 19×3 数组
  direction: output
- name: Rotation
  summary: 旋翼飞行器旋转 19×3 数组
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

### **Engine2\_T** — 发动机 2 平移 1×3 矩阵

发动机 2 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 2 translation** 参数。

**数据类型：** `single` | `double`

### **Rotor1\_T** — 旋翼 1 平移 1×3 矩阵

旋翼 1 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Rotor 1 translation** 参数。

**数据类型：** `single` | `double`

### **Rotor2\_T** — 旋翼 2 平移 1×3 矩阵

旋翼 2 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Rotor 2 translation** 参数。

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

### **Nose\_Gear\_Door1\_T** — 前起落架舱门 1 平移 1×3 矩阵

前起落架舱门 1 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Nose gear door 1 translation** 复选框。

**数据类型：** `single` | `double`

### **Nose\_Gear\_Door2\_T** — 前起落架舱门 2 平移 1×3 矩阵

前起落架舱门 2 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Nose gear door 2 translation** 复选框。

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

### **Left\_Gear\_Door1\_T** — 左起落架舱门 1 平移 1×3 矩阵

左起落架舱门 1 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Left gear door 1 translation** 复选框。

**数据类型：** `single` | `double`

### **Left\_Gear\_Door2\_T** — 左起落架舱门 2 平移 1×3 矩阵

左起落架舱门 2 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Left gear door 2 translation** 复选框。

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

### **Right\_Gear\_Door1\_T** — 右起落架舱门 1 平移 1×3 矩阵

右起落架舱门 1 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Right gear door 1 translation** 复选框。

**数据类型：** `single` | `double`

### **Right\_Gear\_Door2\_T** — 右起落架舱门 2 平移 1×3 矩阵

右起落架舱门 2 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Right gear door 2 translation** 复选框。

**数据类型：** `single` | `double`

### **Sensor1\_T** — 传感器 1 平移 1×3 矩阵

传感器 1 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Sensor 1 translation** 参数。

**数据类型：** `single` | `double`

### **Sensor2\_T** — 传感器 2 平移 1×3 矩阵

传感器 2 平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Sensor 2 translation** 参数。

**数据类型：** `single` | `double`

### **Body\_R** — 机体旋转 1×3 矩阵

机体旋转，指定为 1×3 矩阵。

**数据类型：** `single` | `double`

### **Engine1\_R** — 发动机 1 旋转 1×3 矩阵

发动机 1 旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 1 rotation** 参数。

**数据类型：** `single` | `double`

### **Engine2\_R** — 发动机 2 旋转 1×3 矩阵

发动机 2 旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine 2 rotation** 参数。

**数据类型：** `single` | `double`

### **Rotor1\_R** — 旋翼 1 旋转 1×3 矩阵

旋翼 1 旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Rotor 1 rotation** 参数。

**数据类型：** `single` | `double`

### **Rotor2\_R** — 旋翼 2 旋转 1×3 矩阵

旋翼 2 旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Rotor 2 rotation** 参数。

**数据类型：** `single` | `double`

### **Nose\_Gear\_R** — 前起落架旋转 1×3 矩阵

前起落架旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Nose gear rotation** 参数。

**数据类型：** `single` | `double`

### **Nose\_Wheel\_R** — 前轮旋转 1×3 矩阵

前轮旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Nose wheel rotation** 参数。

**数据类型：** `single` | `double`

### **Nose\_Gear\_Door1\_R** — 前起落架舱门 1 旋转 1×3 矩阵

前起落架舱门 1 旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Nose gear door 1 rotation** 复选框。

**数据类型：** `single` | `double`

### **Nose\_Gear\_Door2\_R** — 前起落架舱门 2 旋转 1×3 矩阵

前起落架舱门 2 旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Nose gear door 2 rotation** 复选框。

**数据类型：** `single` | `double`

### **Left\_Gear\_R** — 左起落架旋转 1×3 矩阵

左起落架旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Left gear rotation** 参数。

**数据类型：** `single` | `double`

### **Left\_Wheel\_R** — 左轮旋转 1×3 矩阵

左轮旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Left wheel rotation** 参数。

**数据类型：** `single` | `double`

### **Left\_Gear\_Door1\_R** — 左起落架舱门 1 旋转 1×3 矩阵

左起落架舱门 1 旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Left gear door 1 rotation** 复选框。

**数据类型：** `single` | `double`

### **Left\_Gear\_Door2\_R** — 左起落架舱门 2 旋转 1×3 矩阵

左起落架舱门 2 旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Left gear door 2 rotation** 复选框。

**数据类型：** `single` | `double`

### **Right\_Gear\_R** — 右起落架旋转 1×3 矩阵

右起落架旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Right gear rotation** 参数。

**数据类型：** `single` | `double`

### **Right\_Wheel\_R** — 右轮旋转 1×3 矩阵

右轮旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Right wheel rotation** 参数。

**数据类型：** `single` | `double`

### **Right\_Gear\_Door1\_R** — 右起落架舱门 1 旋转 1×3 矩阵

右起落架舱门 1 旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Right gear door 1 rotation** 复选框。

**数据类型：** `single` | `double`

### **Right\_Gear\_Door2\_R** — 右起落架舱门 2 旋转 1×3 矩阵

右起落架舱门 2 旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选中 **Right gear door 2 rotation** 复选框。

**数据类型：** `single` | `double`

### **Sensor1\_R** — 传感器 1 旋转 1×3 矩阵

传感器 1 旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Sensor 1 rotation** 参数。

**数据类型：** `single` | `double`

### **Sensor2\_R** — 传感器 2 旋转 1×3 矩阵

传感器 2 旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Sensor 2 rotation** 参数。

**数据类型：** `single` | `double`
### 输出

### **Translation** — 直升机平移 `19`×`3` 数组

直升机旋翼飞行器的直升机平移，以 `19`×`3` 数组形式返回。该信号包含平移 [*X*, *Y*, *Z*]，单位为米，数组的每一行对应旋翼飞行器的一个骨骼。

该平移适用于 `Helicopter` 类型的以下骨骼。

| 骨骼 | 索引 |
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

### **Rotation** — 旋翼飞行器旋转 `19`×`3` 数组

直升机旋翼飞行器的旋翼飞行器旋转，以 `19`×`3` 数组形式返回。

该旋转适用于 Translation 端口所列出的相同骨骼。

该信号包含旋转 [roll, pitch, yaw]，单位为弧度，数组的每一行对应旋翼飞行器的一个骨骼。
## 参数
```yaml
parameters:
- name: Engine 1 translation
  summary: 启用 Engine1_T 输入端口的选项 off（默认）| on
  group: 推进
  block_parameter: Engine1_T
  type: 字符向量
  values: '''on'' | ''off'''
- name: Engine 2 translation
  summary: 启用 Engine2_T 输入端口的选项 off（默认）| on
  group: 推进
  block_parameter: Engine2_T
  type: 字符向量
  values: '''on'' | ''off'''
- name: Rotor 1 translation
  summary: 启用 Rotor1_T 输入端口的选项 off（默认）| on
  group: 推进
  block_parameter: Rotor1_T
  type: 字符向量
  values: '''on'' | ''off'''
- name: Rotor 2 translation
  summary: 启用 Rotor2_T 输入端口的选项 off（默认）| on
  group: 推进
  block_parameter: Rotor2_T
  type: 字符向量
  values: '''on'' | ''off'''
- name: Engine 1 rotation
  summary: 启用 Engine1_R 输入端口的选项 off（默认）| on
  group: 推进
  block_parameter: Engine1_R
  type: 字符向量
  values: '''on'' | ''off'''
- name: Engine 2 rotation
  summary: 启用 Engine2_R 输入端口的选项 off（默认）| on
  group: 推进
  block_parameter: Engine2_R
  type: 字符向量
  values: '''on'' | ''off'''
- name: Rotor 1 rotation
  summary: 启用 Rotor1_R 输入端口的选项 off（默认）| on
  group: 推进
  block_parameter: Rotor1_R
  type: 字符向量
  values: '''on'' | ''off'''
- name: Rotor 2 rotation
  summary: 启用 Rotor2_R 输入端口的选项 off（默认）| on
  group: 推进
  block_parameter: Rotor2_R
  type: 字符向量
  values: '''on'' | ''off'''
- name: Nose gear translation
  summary: 启用 Nose_Gear_T 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Nose_Gear_T
  type: 字符向量
  values: '''on'' | ''off'''
- name: Nose wheel translation
  summary: 启用 Nose_Wheel_T 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Nose_Wheel_T
  type: 字符向量
  values: '''on'' | ''off'''
- name: Nose gear door 1 translation
  summary: 启用 Nose_Gear_Door1_T 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Nose_Gear_Door1_T
  type: 字符向量
  values: '''on'' | ''off'''
- name: Nose gear door 2 translation
  summary: 启用 Nose_Gear_Door2_T 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Nose_Gear_Door2_T
  type: 字符向量
  values: '''on'' | ''off'''
- name: Left gear translation
  summary: 启用 Left_Gear_T 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Left_Gear_T
  type: 字符向量
  values: '''on'' | ''off'''
- name: Left wheel translation
  summary: 启用 Left_Wheel_T 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Left_Wheel_T
  type: 字符向量
  values: '''on'' | ''off'''
- name: Left gear door 1 translation
  summary: 启用 Left_Gear_Door1_T 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Left_Gear_Door1_T
  type: 字符向量
  values: '''on'' | ''off'''
- name: Left gear door 2 translation
  summary: 启用 Left_Gear_Door2_T 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Left_Gear_Door2_T
  type: 字符向量
  values: '''on'' | ''off'''
- name: Right gear translation
  summary: 启用 Right_Gear_T 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Right_Gear_T
  type: 字符向量
  values: '''on'' | ''off'''
- name: 右轮平移
  summary: 启用 Right_Wheel_T 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Right_Wheel_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: 右起落架舱门 1 平移
  summary: 启用 Right_Gear_Door1_T 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Right_Gear_Door1_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: 右起落架舱门 2 平移
  summary: 启用 Right_Gear_Door2_T 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Right_Gear_Door2_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: 前起落架旋转
  summary: 启用 Nose_Gear_R 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Nose_Gear_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: 前轮旋转
  summary: 启用 Nose_Wheel_R 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Nose_Wheel_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: 前起落架舱门 1 旋转
  summary: 启用 Nose_Gear_Door1_R 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Nose_Gear_Door1_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: 前起落架舱门 2 旋转
  summary: 启用 Nose_Gear_Door2_R 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Nose_Gear_Door2_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: 左起落架旋转
  summary: 启用 Left_Gear_R 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Left_Gear_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: 左轮旋转
  summary: 启用 Left_Wheel_R 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Left_Wheel_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: 左起落架舱门 1 旋转
  summary: 启用 Left_Gear_Door1_R 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Left_Gear_Door1_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: 左起落架舱门 2 旋转
  summary: 启用 Left_Gear_Door2_R 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Left_Gear_Door2_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: 右起落架旋转
  summary: 启用 Right_Gear_R 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Right_Gear_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: 右轮旋转
  summary: 启用 Right_Wheel_R 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Right_Wheel_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: 右起落架舱门 1 旋转
  summary: 启用 Right_Gear_Door1_R 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Right_Gear_Door1_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: 右起落架舱门 2 旋转
  summary: 启用 Right_Gear_Door2_R 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Right_Gear_Door2_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: 传感器 1 平移
  summary: 启用 Sensor1_T 输入端口的选项 off（默认）| on
  group: 传感器
  block_parameter: Sensor1_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: 传感器 2 平移
  summary: 启用 Sensor2_T 输入端口的选项 off（默认）| on
  group: 传感器
  block_parameter: Sensor2_T
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: 传感器 1 旋转
  summary: 启用 Sensor1_R 输入端口的选项 off（默认）| on
  group: 传感器
  block_parameter: Sensor1_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: 传感器 2 旋转
  summary: 启用 Sensor2_R 输入端口的选项 off（默认）| on
  group: 传感器
  block_parameter: Sensor2_R
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: 选择输入坐标系
  summary: 输入坐标系 NED（默认）| Fixed-frame | ICRF
  group: 输入
  block_parameter: GeoRadioButton
  values: '''NED''（默认）| ''Fixed-frame'' | ''ICRF'''
```

### 推进

### **Engine 1 translation** — 启用 Engine1\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Engine1\_T** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Engine1_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认**：`'off'` |

### **Engine 2 translation** — 启用 Engine2\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Engine2\_T** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Engine2_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认**：`'off'` |

### **Rotor 1 translation** — 启用 Rotor1\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Rotor1\_T** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Rotor1_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认**：`'off'` |

### **Rotor 2 translation** — 启用 Rotor2\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Rotor2\_T** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Rotor2_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认**：`'off'` |

### **Engine 1 rotation** — 启用 Engine1\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Engine1\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Engine1_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认**：`'off'` |

### **Engine 2 rotation** — 启用 Engine2\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Engine2\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Engine2_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认**：`'off'` |

### **Rotor 1 rotation** — 启用 Rotor1\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Rotor1\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Rotor1_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认**：`'off'` |

### **Rotor 2 rotation** — 启用 Rotor2\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Rotor2\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Rotor2_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认**：`'off'` |

### 起落架

### **Nose gear translation** — 启用 Nose\_Gear\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Nose\_Gear\_T** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Nose_Gear_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认**：`'off'` |

### **Nose wheel translation** — 启用 Nose\_Wheel\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Nose\_Wheel\_T** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Nose_Wheel_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认**：`'off'` |

### **Nose gear door 1 translation** — 启用 Nose\_Gear\_Door1\_T 输入端口的选项 `off`（默认）| `on`

选中此复选框以启用 **Nose\_Gear\_Door1\_T** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Nose_Gear_Door1_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认**：`'off'` |

### **Nose gear door 2 translation** — 启用 Nose\_Gear\_Door2\_T 输入端口的选项 `off`（默认）| `on`

选中此复选框以启用 **Nose\_Gear\_Door2\_T** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Nose_Gear_Door2_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认**：`'off'` |

### **Left gear translation** — 启用 Left\_Gear\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Gear\_T** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Left_Gear_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认**：`'off'` |

### **Left wheel translation** — 启用 Left\_Wheel\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Wheel\_T** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Left_Wheel_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认**：`'off'` |

### **Left gear door 1 translation** — 启用 Left\_Gear\_Door1\_T 输入端口的选项 `off`（默认）| `on`

选中此复选框以启用 **Left\_Gear\_Door1\_T** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Left_Gear_Door1_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认**：`'off'` |

### **Left gear door 2 translation** — 启用 Left\_Gear\_Door2\_T 输入端口的选项 `off`（默认）| `on`

选中此复选框以启用 **Left\_Gear\_Door2\_T** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Left_Gear_Door2_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认**：`'off'` |

### **Right gear translation** — 启用 Right\_Gear\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Gear\_T** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Right_Gear_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认**：`'off'` |

### **右轮平移** — 启用 Right\_Wheel\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Wheel\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Right_Wheel_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **右起落架舱门 1 平移** — 启用 Right\_Gear\_Door1\_T 输入端口的选项 `off`（默认）| `on`

选中此复选框以启用 **Right\_Gear\_Door1\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Right_Gear_Door1_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **右起落架舱门 2 平移** — 启用 Right\_Gear\_Door2\_T 输入端口的选项 `off`（默认）| `on`

选中此复选框以启用 **Right\_Gear\_Door2\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Right_Gear_Door2_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **前起落架旋转** — 启用 Nose\_Gear\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Nose\_Gear\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Nose_Gear_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **前轮旋转** — 启用 Nose\_Wheel\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Nose\_Wheel\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Nose_Wheel_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **前起落架舱门 1 旋转** — 启用 Nose\_Gear\_Door1\_R 输入端口的选项 `off`（默认）| `on`

选中此复选框以启用 **Nose\_Gear\_Door1\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Nose_Gear_Door1_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **前起落架舱门 2 旋转** — 启用 Nose\_Gear\_Door2\_R 输入端口的选项 `off`（默认）| `on`

选中此复选框以启用 **Nose\_Gear\_Door2\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Nose_Gear_Door2_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **左起落架旋转** — 启用 Left\_Gear\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Gear\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Left_Gear_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **左轮旋转** — 启用 Left\_Wheel\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Wheel\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Left_Wheel_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **左起落架舱门 1 旋转** — 启用 Left\_Gear\_Door1\_R 输入端口的选项 `off`（默认）| `on`

选中此复选框以启用 **Left\_Gear\_Door1\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Left_Gear_Door1_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **左起落架舱门 2 旋转** — 启用 Left\_Gear\_Door2\_R 输入端口的选项 `off`（默认）| `on`

选中此复选框以启用 **Left\_Gear\_Door2\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Left_Gear_Door2_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **右起落架旋转** — 启用 Right\_Gear\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Gear\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Right_Gear_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **右轮旋转** — 启用 Right\_Wheel\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Wheel\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Right_Wheel_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **右起落架舱门 1 旋转** — 启用 Right\_Gear\_Door1\_R 输入端口的选项 `off`（默认）| `on`

选中此复选框以启用 **Right\_Gear\_Door1\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Right_Gear_Door1_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **右起落架舱门 2 旋转** — 启用 Right\_Gear\_Door2\_R 输入端口的选项 `off`（默认）| `on`

选中此复选框以启用 **Right\_Gear\_Door2\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Right_Gear_Door2_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### 传感器

### **传感器 1 平移** — 启用 Sensor1\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Sensor1\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Sensor1_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **传感器 2 平移** — 启用 Sensor2\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Sensor2\_T** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Sensor2_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **传感器 1 旋转** — 启用 Sensor1\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Sensor1\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Sensor1_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **传感器 2 旋转** — 启用 Sensor2\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Sensor2\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Sensor2_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### 输入

### **选择输入坐标系** — 输入坐标系 `NED`（默认）| `Fixed-frame` | `ICRF`

选择输入坐标系，以相对于北-东-地（NED）、固定坐标系（Fixed-frame）或国际天球参考系（ICRF）来定位航空航天器。

如果模型中包含关联的 Simulation 3D Scene Configuration 模块，则 Simulation 3D Helicopter Pack 模块使用 Simulation 3D Scene Configuration 的坐标系。在这种情况下，**选择输入坐标系** 可能被禁用。有关 Simulation 3D Helicopter Pack 模块坐标系的更多信息，请参阅算法。

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

### R2025a：Simulation 3D Helicopter Pack 模块现在与 Simulation 3D Scene Configuration 模块同步坐标系

Simulation 3D Helicopter Pack 模块有以下变更：

- **Geospatial** 选项卡已重命名为 **Input** 选项卡。
- 在 **Input** 选项卡上，**Select input coordinate frame** 窗格现在包含以下坐标系按钮：

  - **Fixed-frame** — 固定坐标系。当您选择此坐标系时，注释 `Fixed-frame` 会显示在 pack 模块图标下方。
  - **ICRF** — 国际天球参考系坐标系。当您选择此坐标系时，注释 `ICRF` 会显示在 pack 模块图标下方。
  - **NED** — 北-东-地坐标系。当您选择此坐标系时，注释 `NED` 会显示在 pack 模块图标下方。

  如果模型中包含 Simulation 3D pack 模块和关联的 Simulation 3D Scene Configuration 模块，则 Simulation 3D Helicopter Pack 的 **Input** 选项卡选项可能被禁用。在这种情况下，Simulation 3D Helicopter Pack 会与 Simulation 3D Scene Configuration 模块同步坐标系。
- 坐标系显示为模块下方的注释。
- **Enable geospatial correction** 和 **Direction of x-axis (degrees clockwise from north)** 参数已被移除。

### R2024a：Simulation 3D Helicopter Pack 模块现在支持地心地球固定（ECEF）输入坐标系

为了支持用于平移输入的 ECEF 坐标系，Simulation 3D Helicopter Pack 模块已更新。将这些参数与 Simulation 3D Scene Configuration 模块中的 **Use Earth center as origin (ECEF)** 参数一起使用。

- **选择输入坐标系**

  - **ECEF** — ECEF 输入坐标系。当您选择此坐标系时，注释 `Origin: Earth center (ECEF)` 会显示在 pack 模块图标下方。
  - **NED** — NED 坐标系。在 R2024a 之前，NED 是唯一支持的坐标系。
- **Direction of x-axis (degrees clockwise from north)** — *x* 轴方向。当您选中 **Enable geospatial correction** 复选框时，此参数启用。

## 描述

生成直升机的平移和旋转信息

Simulation 3D Helicopter Pack 模块为 **Type** 设置为 `Helicopter` 的 Simulation 3D Rotorcraft 模块创建平移和旋转信息。使用 Simulation 3D Helicopter Pack 模块向 Simulation 3D Rotorcraft 模块的 **Translation** 和 **Rotation** 输入端口提供平移和旋转信息。
