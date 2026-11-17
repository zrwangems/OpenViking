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
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Airliner Pack

## 端口

### 输入

### **Body\_T** — 机体平移 1×3 矩阵

机体平移，指定为 1×3 矩阵。

**数据类型：** `single` | `double`

### **Body\_R** — 机体旋转 1×3 矩阵

机体旋转，指定为 1×3 矩阵。

**数据类型：** `single` | `double`

### **Left\_Engine\_R** — 左发动机旋转 1×3 矩阵

左发动机旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Left engine rotation** 参数。

**数据类型：** `single` | `double`

### **Right\_Engine\_R** — 右发动机旋转 1×3 矩阵

右发动机旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Right engine rotation** 参数。

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

### **Nose\_Wheel\_Strut\_R** — 前轮支柱旋转 1×3 矩阵

前轮支柱旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Nose wheel strut rotation** 参数。

**数据类型：** `single` | `double`

### **Nose\_Wheel\_R** — 前轮旋转 1×3 矩阵

前轮旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Nose wheel rotation** 参数。

**数据类型：** `single` | `double`

### **Left\_Wheel\_R** — 左轮旋转 1×3 矩阵

左轮旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Left wheel rotation** 参数。

**数据类型：** `single` | `double`

### **Right\_Wheel\_R** — 右轮旋转 1×3 矩阵

右轮旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Right wheel rotation** 参数。

**数据类型：** `single` | `double`
### 输出

### **Translation** — 飞行器平移 `12`×`3` 数组

通用客机飞行器的飞行器平移，以 `12`×`3` 数组形式返回。该信号包含平移 [*X*，*Y*，*Z*]，单位为米，数组的每一行对应飞行器的一个骨骼。

该平移适用于 `Airliner` 类型的以下骨骼。

| 骨骼 | 索引 |
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

### **Rotation** — 飞行器和机轮旋转 `12`×`3` 数组

通用客机的飞行器和机轮旋转，以 `12`×`3` 数组形式返回。

该旋转适用于 Translation 端口所列出的相同骨骼。

该信号包含旋转 [roll，pitch，yaw]，单位为弧度，数组的每一行对应飞行器的一个骨骼。

## 参数

### 推进

### **Left engine rotation** — 启用 Left\_Engine\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Engine\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Left_Engine_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right engine rotation** — 启用 Right\_Engine\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Engine\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Right_Engine_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### 控制

### **Rudder rotation** — 启用 Rudder\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Rudder\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Rudder_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Elevator rotation** — 启用 Elevator\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Elevator\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Elevator_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Left aileron rotation** — 启用 Left\_Aileron\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Aileron\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Left_Aileron_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right aileron rotation** — 启用 Right\_Aileron\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Aileron\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Right_Aileron_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Flaps rotation** — 启用 Flaps\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Flaps\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Flaps_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### 起落架

### **Nose wheel strut rotation** — 启用 Nose\_Wheel\_Strut\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Nose\_Wheel\_Strut\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Nose_Wheel_Strut_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Nose wheel rotation** — 启用 Nose\_Wheel\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Nose\_Wheel\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Nose_Wheel_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Left wheel rotation** — 启用 Left\_Wheel\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Wheel\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Left_Wheel_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Right wheel rotation** — 启用 Right\_Wheel\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Wheel\_R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`Right_Wheel_R` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### 输入

### **Select input coordinate frame** — 输入坐标系 `NED`（默认）| `Fixed-frame` | `ICRF`

选择输入坐标系，以相对于北-东-地（NED）、固定坐标系（Fixed-frame）或国际天球参考系（ICRF）来定位航空航天飞行器。

如果模型包含关联的 Simulation 3D Scene Configuration 模块，则 Simulation 3D Airliner Pack 模块使用 Simulation 3D Scene Configuration 的坐标系。在这种情况下，**Select input coordinate frame** 可能被禁用。有关 Simulation 3D Airliner Pack 模块坐标系的详细信息，请参阅算法。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

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

### R2025a：Simulation 3D Airliner Pack 模块现在与 Simulation 3D Scene Configuration 模块同步坐标系

Simulation 3D Airliner Pack 模块有以下变更：

- **Geospatial** 选项卡已重命名为 **Input** 选项卡。
- 在 **Input** 选项卡上，**Select input coordinate frame** 窗格现在包含以下坐标系按钮：

  - **Fixed-frame** — 固定坐标系。当您选择此坐标系时，注释 `Fixed-frame` 会出现在 pack 模块图标下方。
  - **ICRF** — 国际天球参考系坐标系。当您选择此坐标系时，注释 `ICRF` 会出现在 pack 模块图标下方。
  - **NED** — 北-东-地坐标系。当您选择此坐标系时，注释 `NED` 会出现在 pack 模块图标下方。

  如果模型包含 Simulation 3D pack 模块和关联的 Simulation 3D Scene Configuration 模块，则 Simulation 3D Airliner Pack 的 **Input** 选项卡选项可能被禁用。在这种情况下，Simulation 3D Airliner Pack 会与 Simulation 3D Scene Configuration 模块同步坐标系。
- 坐标系显示为模块下方的注释。
- **Enable geospatial correction** 和 **Direction of x-axis (degrees clockwise from north)** 参数已被移除。

### R2024a：Simulation 3D Airliner Pack 模块现在支持地心地球固定（ECEF）输入坐标系

为了支持用于平移输入的 ECEF 坐标系，Simulation 3D Airliner Pack 模块已更新。将这些参数与 Simulation 3D Scene Configuration 模块中的 **Use Earth center as origin (ECEF)** 参数一起使用。

- **选择输入坐标系**

  - **ECEF** — ECEF 输入坐标系。当您选择此坐标系时，注释 `Origin: Earth center (ECEF)` 会出现在 pack 模块图标下方。
  - **NED** — NED 坐标系。在 R2024a 之前，NED 是唯一支持的坐标系。
- **Direction of x-axis (degrees clockwise from north)** — *x* 轴的方向。当您选中 **Enable geospatial correction** 复选框时，此参数启用。

## 描述

为通用客机生成平移和旋转信息

Simulation 3D Airliner Pack 模块为 **Type** 设置为 `Airliner` 的 Simulation 3D Aircraft 模块创建平移和旋转信息。使用 Simulation 3D Airliner Pack 模块为 Simulation 3D Aircraft 模块的 **Translation** 和 **Rotation** 输入端口提供平移和旋转信息。
