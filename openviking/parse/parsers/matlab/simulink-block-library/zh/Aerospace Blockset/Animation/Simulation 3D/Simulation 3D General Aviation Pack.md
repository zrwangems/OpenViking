---
type: simulink-block
title: 'Simulation 3D General Aviation Pack'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation / Simulation 3D'
documentation_page: 'simulation3dgeneralaviationpack'
documentation_source_path: 'simulation3dgeneralaviationpack.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D General Aviation Pack

## 端口
```yaml
ports:
- name: Body_T
  summary: 机体平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine1_T
  summary: 发动机平移 1×3 矩阵
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
- name: Left_Aileron_T
  summary: 左副翼平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Right_Aileron_T
  summary: 右副翼平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Flaps_T
  summary: 襟翼平移 1×3 矩阵
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
- name: Left_Gear_T
  summary: 左起落架平移 1×3 矩阵
  direction: input
  data_types: single | double
- name: Left_Wheel_T
  summary: 左轮平移 1×3 矩阵
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
- name: Body_R
  summary: 机体旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Engine1_R
  summary: 发动机旋转 1×3 矩阵
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
- name: Left_Aileron_R
  summary: 左副翼旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Right_Aileron_R
  summary: 右副翼旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Flaps_R
  summary: 襟翼旋转 1×3 矩阵
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
- name: Left_Gear_R
  summary: 左起落架旋转 1×3 矩阵
  direction: input
  data_types: single | double
- name: Left_Wheel_R
  summary: 左轮旋转 1×3 矩阵
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
- name: Translation
  summary: 飞机平移 15×3 数组
  direction: output
- name: Rotation
  summary: 飞机旋转 15×3 数组
  direction: output
```

### 输入

### **Body\_T** — 机体平移 1×3 矩阵

机体平移，指定为 1×3 矩阵。

**数据类型：** `single` | `double`

### **Engine1\_T** — 发动机平移 1×3 矩阵

发动机平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine translation** 参数。

**数据类型：** `single` | `double`

### **Rudder\_T** — 方向舵平移 1×3 矩阵

方向舵平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Rudder translation** 参数。

**数据类型：** `single` | `double`

### **Elevator\_T** — 升降舵平移 1×3 矩阵

升降舵平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Elevator translation** 参数。

**数据类型：** `single` | `double`

### **Left\_Aileron\_T** — 左副翼平移 1×3 矩阵

左副翼平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Left aileron translation** 参数。

**数据类型：** `single` | `double`

### **Right\_Aileron\_T** — 右副翼平移 1×3 矩阵

右副翼平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Right aileron translation** 参数。

**数据类型：** `single` | `double`

### **Flaps\_T** — 襟翼平移 1×3 矩阵

襟翼平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Flaps translation** 参数。

**数据类型：** `single` | `double`

### **Left\_Spoiler\_T** — 左扰流板平移 1×3 矩阵

左扰流板平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Left spoiler translation** 参数。

**数据类型：** `single` | `double`

### **Right\_Spoiler\_T** — 右扰流板平移 1×3 矩阵

右扰流板平移，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Right spoiler translation** 参数。

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

### **Body\_R** — 机体旋转 1×3 矩阵

机体旋转，指定为 1×3 矩阵。

**数据类型：** `single` | `double`

### **Engine1\_R** — 发动机旋转 1×3 矩阵

发动机旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine rotation** 参数。

**数据类型：** `single` | `double`

### **Rudder\_R** — 方向舵旋转 1×3 矩阵

方向舵旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Rudder rotation** 参数。

**数据类型：** `single` | `double`

### **Elevator\_R** — 升降舵旋转 1×3 矩阵

升降舵旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Elevator rotation** 参数。

**数据类型：** `single` | `double`

### **Left\_Aileron\_R** — 左副翼旋转 1×3 矩阵

左副翼旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Left aileron rotation** 参数。

**数据类型：** `single` | `double`

### **Right\_Aileron\_R** — 右副翼旋转 1×3 矩阵

右副翼旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Right aileron rotation** 参数。

**数据类型：** `single` | `double`

### **Flaps\_R** — 襟翼旋转 1×3 矩阵

襟翼旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Flaps rotation** 参数。

**数据类型：** `single` | `double`

### **Left\_Spoiler\_R** — 左扰流板旋转 1×3 矩阵

左扰流板旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Left spoiler rotation** 参数。

**数据类型：** `single` | `double`

### **Right\_Spoiler\_R** — 右扰流板旋转 1×3 矩阵

右扰流板旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Right spoiler rotation** 参数。

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
### 输出

### **Translation** — 飞机平移 `15`×`3` 数组

通用航空飞机的飞机平移，以 `15`×`3` 数组形式返回。该信号包含平移 [*X*, *Y*, *Z*]，单位为米，数组的每一行对应飞机的一个骨骼。

该平移适用于 `General Aviation` 类型的以下骨骼。

| 骨骼 | 索引 |
| --- | --- |
| BODY | 1 |
| ENGINE1 | 2 |
| RUDDER | 3 |
| ELEVATOR | 4 |
| LEFT\_AILERON | 5 |
| RIGHT\_AILERON | 6 |
| FLAPS | 7 |
| LEFT\_SPOILER | 8 |
| RIGHT\_SPOILER | 9 |
| NOSE\_GEAR | 10 |
| NOSE\_WHEEL | 11 |
| LEFT\_GEAR | 12 |
| LEFT\_WHEEL | 13 |
| RIGHT\_GEAR | 14 |
| RIGHT\_WHEEL | 15 |

### **Rotation** — 飞机旋转 `15`×`3` 数组

通用航空飞机的飞机旋转，以 `15`×`3` 数组形式返回：

该旋转适用于 Translation 端口所列出的相同骨骼。

该信号包含旋转 [roll, pitch, yaw]，单位为弧度，数组的每一行对应飞机的一个骨骼。
## 参数
```yaml
parameters:
- name: Engine translation
  summary: 启用 Engine1_T 输入端口的选项 off（默认）| on
  group: 推进
  block_parameter: Engine1_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Engine rotation
  summary: 启用 Engine1_R 输入端口的选项 off（默认）| on
  group: 推进
  block_parameter: Engine1_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Rudder translation
  summary: 启用 Rudder_T 输入端口的选项 off（默认）| on
  group: 控制
  block_parameter: Rudder_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Elevator translation
  summary: 启用 Elevator_T 输入端口的选项 off（默认）| on
  group: 控制
  block_parameter: Elevator_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left aileron translation
  summary: 启用 Left_Aileron_T 输入端口的选项 off（默认）| on
  group: 控制
  block_parameter: Left_Aileron_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right aileron translation
  summary: 启用 Right_Aileron_T 输入端口的选项 off（默认）| on
  group: 控制
  block_parameter: Right_Aileron_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Flaps translation
  summary: 启用 Flaps_T 输入端口的选项 off（默认）| on
  group: 控制
  block_parameter: Flaps_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left spoiler translation
  summary: 启用 Left_Spoiler_T 输入端口的选项 off（默认）| on
  group: 控制
  block_parameter: Left_Spoiler_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right spoiler translation
  summary: 启用 Right_Spoiler_T 输入端口的选项 off（默认）| on
  group: 控制
  block_parameter: Right_Spoiler_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Rudder rotation
  summary: 启用 Rudder_R 输入端口的选项 off（默认）| on
  group: 控制
  block_parameter: Rudder_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Elevator rotation
  summary: 启用 Elevator_R 输入端口的选项 off（默认）| on
  group: 控制
  block_parameter: Elevator_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left aileron rotation
  summary: 启用 Left_Aileron_R 输入端口的选项 off（默认）| on
  group: 控制
  block_parameter: Left_Aileron_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right aileron rotation
  summary: 启用 Right_Aileron_R 输入端口的选项 off（默认）| on
  group: 控制
  block_parameter: Right_Aileron_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Flaps rotation
  summary: 启用 Flaps_R 输入端口的选项 off（默认）| on
  group: 控制
  block_parameter: Flaps_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left spoiler rotation
  summary: 启用 Left_Spoiler_R 输入端口的选项 off（默认）| on
  group: 控制
  block_parameter: Left_Spoiler_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right spoiler rotation
  summary: 启用 Right_Spoiler_R 输入端口的选项 off（默认）| on
  group: 控制
  block_parameter: Right_Spoiler_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Nose gear translation
  summary: 启用 Nose_Gear_T 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Nose_Gear_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Nose wheel translation
  summary: 启用 Nose_Wheel_T 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Nose_Wheel_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left gear translation
  summary: 启用 Left_Gear_T 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Left_Gear_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left wheel translation
  summary: 启用 Left_Wheel_T 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Left_Wheel_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right gear translation
  summary: 启用 Right_Gear_T 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Right_Gear_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right wheel translation
  summary: 启用 Right_Wheel_T 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Right_Wheel_T
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Nose gear rotation
  summary: 启用 Nose_Gear_R 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Nose_Gear_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Nose wheel rotation
  summary: 启用 Nose_Wheel_R 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Nose_Wheel_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left gear rotation
  summary: 用于启用 Left_Gear_R 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Left_Gear_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Left wheel rotation
  summary: 用于启用 Left_Wheel_R 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Left_Wheel_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right gear rotation
  summary: 用于启用 Right_Gear_R 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Right_Gear_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Right wheel rotation
  summary: 用于启用 Right_Wheel_R 输入端口的选项 off（默认）| on
  group: 起落架
  block_parameter: Right_Wheel_R
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Select input coordinate frame
  summary: 输入坐标系 NED（默认）| Fixed-frame | ICRF
  group: 输入
  block_parameter: GeoRadioButton
  values: '''NED''（默认）| ''Fixed-frame'' | ''ICRF'''
```

### 推进

### **Engine translation** — 启用 Engine1\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Engine1\_T** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Engine1_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine rotation** — 启用 Engine1\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Engine1\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Engine1_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### 控制

### **Rudder translation** — 启用 Rudder\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Rudder\_T** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Rudder_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Elevator translation** — 启用 Elevator\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Elevator\_T** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Elevator_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Left aileron translation** — 启用 Left\_Aileron\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Aileron\_T** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Left_Aileron_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right aileron translation** — 启用 Right\_Aileron\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Aileron\_T** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Right_Aileron_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Flaps translation** — 启用 Flaps\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Flaps\_T** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Flaps_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Left spoiler translation** — 启用 Left\_Spoiler\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Spoiler\_T** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Left_Spoiler_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right spoiler translation** — 启用 Right\_Spoiler\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Spoiler\_T** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Right_Spoiler_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Rudder rotation** — 启用 Rudder\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Rudder\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Rudder_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Elevator rotation** — 启用 Elevator\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Elevator\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Elevator_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Left aileron rotation** — 启用 Left\_Aileron\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Aileron\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Left_Aileron_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right aileron rotation** — 启用 Right\_Aileron\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Aileron\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Right_Aileron_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Flaps rotation** — 启用 Flaps\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Flaps\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Flaps_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Left spoiler rotation** — 启用 Left\_Spoiler\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Spoiler\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Left_Spoiler_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right spoiler rotation** — 启用 Right\_Spoiler\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Spoiler\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Right_Spoiler_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### 起落架

### **Nose gear translation** — 启用 Nose\_Gear\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Nose\_Gear\_T** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Nose_Gear_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Nose wheel translation** — 启用 Nose\_Wheel\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Nose\_Wheel\_T** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Nose_Wheel_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Left gear translation** — 启用 Left\_Gear\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Gear\_T** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Left_Gear_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Left wheel translation** — 启用 Left\_Wheel\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Wheel\_T** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Left_Wheel_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right gear translation** — 启用 Right\_Gear\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Gear\_T** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Right_Gear_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right wheel translation** — 启用 Right\_Wheel\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Wheel\_T** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Right_Wheel_T` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Nose gear rotation** — 启用 Nose\_Gear\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Nose\_Gear\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Nose_Gear_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Nose wheel rotation** — 启用 Nose\_Wheel\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Nose\_Wheel\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Nose_Wheel_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Left gear rotation** — 用于启用 Left\_Gear\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Gear\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Left_Gear_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Left wheel rotation** — 用于启用 Left\_Wheel\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Wheel\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Left_Wheel_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right gear rotation** — 用于启用 Right\_Gear\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Gear\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Right_Gear_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right wheel rotation** — 用于启用 Right\_Wheel\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Wheel\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Right_Wheel_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### 输入

### **Select input coordinate frame** — 输入坐标系 `NED`（默认）| `Fixed-frame` | `ICRF`

选择输入坐标系，以相对于北-东-地（NED）、固定坐标系（Fixed-frame）或国际天球参考框架（ICRF）来定位航空航天器。

如果模型中包含关联的 Simulation 3D Scene Configuration 模块，则 Simulation 3D General Aviation Pack 模块使用 Simulation 3D Scene Configuration 的坐标系。在这种情况下，**Select input coordinate frame** 可能被禁用。有关 Simulation 3D General Aviation Pack 模块坐标系的更多信息，请参阅算法。

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

### R2025a：Simulation 3D General Aviation Pack 模块现在与 Simulation 3D Scene Configuration 模块同步坐标系

Simulation 3D General Aviation Pack 模块有以下变更：

- **Geospatial** 选项卡已重命名为 **Input** 选项卡。
- 在 **Input** 选项卡上，**Select input coordinate frame** 窗格现在包含以下坐标系按钮：

  - **Fixed-frame** — 固定坐标系。选择此坐标系时，注释 `Fixed-frame` 会显示在载具模块图标下方。
  - **ICRF** — 国际天球参考框架坐标系。选择此坐标系时，注释 `ICRF` 会显示在载具模块图标下方。
  - **NED** — 北-东-地坐标系。选择此坐标系时，注释 `NED` 会显示在载具模块图标下方。

  如果模型中包含 Simulation 3D 载具模块以及关联的 Simulation 3D Scene Configuration 模块，则 Simulation 3D General Aviation Pack 的 **Input** 选项卡选项可能被禁用。在这种情况下，Simulation 3D General Aviation Pack 会与 Simulation 3D Scene Configuration 模块同步坐标系。
- 坐标系显示为模块下方的注释。
- **Enable geospatial correction** 和 **Direction of x-axis (degrees clockwise from north)** 参数已被移除。

### R2024a：Simulation 3D General Aviation Pack 模块现在支持地心地球固定（ECEF）输入坐标系

为支持用于平移输入的 ECEF 坐标系，Simulation 3D General Aviation Pack 模块已更新。请将这些参数与 Simulation 3D Scene Configuration 模块中的 **Use Earth center as origin (ECEF)** 参数一起使用。

- **选择输入坐标系**

  - **ECEF** — ECEF 输入坐标系。选择此坐标系时，注释 `Origin: Earth center (ECEF)` 会显示在载具模块图标下方。
  - **NED** — NED 坐标系。在 R2024a 之前，NED 是唯一受支持的坐标系。
- **Direction of x-axis (degrees clockwise from north)** — *x* 轴方向。当您选中 **Enable geospatial correction** 复选框时，此参数启用。

## 描述

为通用航空器生成平移和旋转信息

Simulation 3D General Aviation Pack 模块为 **Type** 设置为 `General aviation` 的 Simulation 3D Aircraft 模块创建平移和旋转信息。使用 Simulation 3D General Aviation Pack 模块向 Simulation 3D Aircraft 模块的 **Translation** 和 **Rotation** 输入端口提供平移和旋转信息。
