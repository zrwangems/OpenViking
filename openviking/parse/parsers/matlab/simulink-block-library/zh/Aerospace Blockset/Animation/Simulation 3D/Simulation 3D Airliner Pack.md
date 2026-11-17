---
type: simulink-block
title: 'Simulation 3D Airliner Pack'
family: 'animation'
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

### **Body\_T** — 机体平移 1-by-3 矩阵

机体平移，指定为 1-by-3 矩阵。

**数据类型：** `single` | `double`

### **Body\_R** — 机体旋转 1-by-3 矩阵

机体旋转，指定为 1-by-3 矩阵。

**数据类型：** `single` | `double`

### **Left\_Engine\_R** — 左发动机旋转 1-by-3 矩阵

左发动机旋转，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **左发动机旋转** 参数。

**数据类型：** `single` | `double`

### **Right\_Engine\_R** — 右发动机旋转 1-by-3 矩阵

右发动机旋转，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **右发动机旋转** 参数。

**数据类型：** `single` | `double`

### **Rudder\_R** — 方向舵旋转 1-by-3 矩阵

方向舵旋转，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **方向舵旋转** 参数。

**数据类型：** `single` | `double`

### **Elevator\_R** — 升降舵旋转 1-by-3 矩阵

升降舵旋转，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **升降舵旋转** 参数。

**数据类型：** `single` | `double`

### **Left\_Aileron\_R** — 左副翼旋转 1-by-3 矩阵

左副翼旋转，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **左副翼旋转** 参数。

**数据类型：** `single` | `double`

### **Right\_Aileron\_R** — 右副翼旋转 1-by-3 矩阵

右副翼旋转，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **右副翼旋转** 参数。

**数据类型：** `single` | `double`

### **Flaps\_R** — 襟翼旋转 1-by-3 矩阵

襟翼旋转，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **襟翼旋转** 参数。

**数据类型：** `single` | `double`

### **Nose\_Wheel\_Strut\_R** — 前轮支柱旋转 1-by-3 矩阵

前轮支柱旋转，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **前轮支柱旋转** 参数。

**数据类型：** `single` | `double`

### **Nose\_Wheel\_R** — 前轮旋转 1-by-3 矩阵

前轮旋转，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **前轮旋转** 参数。

**数据类型：** `single` | `double`

### **Left\_Wheel\_R** — 左轮旋转 1-by-3 矩阵

左轮旋转，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **左轮旋转** 参数。

**数据类型：** `single` | `double`

### **Right\_Wheel\_R** — 右轮旋转 1-by-3 矩阵

右轮旋转，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **右轮旋转** 参数。

**数据类型：** `single` | `double`

### 输出

### **Translation** — 飞机平移 `12`-by-`3` 数组

通用客机的飞机平移，返回为 `12`-by-`3` 数组。该信号包含平移 [*X*, *Y*, *Z*]，单位为 meters，数组的每一行对应飞机的一个骨骼。

该平移应用于 `Airliner` 类型的以下骨骼。

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

### **Rotation** — 飞机和机轮旋转 `12`-by-`3` 数组

通用客机的飞机和机轮旋转，返回为 `12`-by-`3` 数组。

该旋转应用于 Translation 端口中列出的相同骨骼。

该信号包含旋转 [roll, pitch, yaw]，单位为 radians，数组的每一行对应飞机的一个骨骼。

## 参数

### 推进

### **左发动机旋转** — 用于启用 Left\_Engine\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Engine\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Left_Engine_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **右发动机旋转** — 用于启用 Right\_Engine\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Engine\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Right_Engine_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### 控制

### **方向舵旋转** — 用于启用 Rudder\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Rudder\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Rudder_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **升降舵旋转** — 用于启用 Elevator\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Elevator\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Elevator_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **左副翼旋转** — 用于启用 Left\_Aileron\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Aileron\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Left_Aileron_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **右副翼旋转** — 用于启用 Right\_Aileron\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Aileron\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Right_Aileron_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **襟翼旋转** — 用于启用 Flaps\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Flaps\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Flaps_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### 起落架

### **前轮支柱旋转** — 用于启用 Nose\_Wheel\_Strut\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Nose\_Wheel\_Strut\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Nose_Wheel_Strut_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **前轮旋转** — 用于启用 Nose\_Wheel\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Nose\_Wheel\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Nose_Wheel_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **左轮旋转** — 用于启用 Left\_Wheel\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Left\_Wheel\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Left_Wheel_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **右轮旋转** — 用于启用 Right\_Wheel\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Right\_Wheel\_R** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Right_Wheel_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### 输入

### **选择输入坐标系** — 输入坐标系 `NED`（默认）| `Fixed-frame` | `ICRF`

选择输入坐标系，以相对于 north-east-down (NED)、fixed-frame (Fixed-frame) 或 International Celestial Reference Frame (ICRF) 定位航空航天器。

如果模型包含关联的 Simulation 3D Scene Configuration 模块，则 Simulation 3D Airliner Pack 模块使用 Simulation 3D Scene Configuration 的坐标系。在这种情况下，**选择输入坐标系** 可能会被禁用。有关 Simulation 3D Airliner Pack 模块坐标系的详细信息，请参阅 Algorithms。

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

### R2025a：Simulation 3D Airliner Pack 模块现在与 Simulation 3D Scene Configuration 模块同步坐标系

Simulation 3D Airliner Pack 模块有以下更改：

- **Geospatial** 选项卡已重命名为 **Input** 选项卡。
- 在 **Input** 选项卡上，**选择输入坐标系** 窗格现在包含以下坐标系按钮：

  - **Fixed-frame** — Fixed-frame 坐标系。选择此坐标系后，注释 `Fixed-frame` 会出现在 pack 模块图标下。
  - **ICRF** — International Celestial Reference Frame 坐标系。选择此坐标系后，注释 `ICRF` 会出现在 pack 模块图标下。
  - **NED** — North-east-down 坐标系。选择此坐标系后，注释 `NED` 会出现在 pack 模块图标下。

  如果模型包含 Simulation 3D pack 模块和关联的 Simulation 3D Scene Configuration 模块，则 Simulation 3D Airliner Pack 的 **Input** 选项卡选项可能会被禁用。在这种情况下，Simulation 3D Airliner Pack 会与 Simulation 3D Scene Configuration 模块同步坐标系。
- 坐标系显示为模块下方的注释。
- **启用地理空间校正** 和 **x 轴方向（degrees clockwise from north）** 参数已被移除。

### R2024a：Simulation 3D Airliner Pack 模块现在支持 Earth-centered Earth-fixed (ECEF) 输入坐标系

为平移输入启用 ECEF 坐标系，Simulation 3D Airliner Pack 模块已更新。在 Simulation 3D Scene Configuration 模块中，将这些参数与 **Use Earth center as origin (ECEF)** 参数一起使用。

- **选择输入坐标系**

  - **ECEF** — ECEF 输入坐标系。选择此坐标系后，注释 `Origin: Earth center (ECEF)` 会出现在 pack 模块图标下。
  - **NED** — NED 坐标系。在 R2024a 之前，NED 是唯一支持的坐标系。
- **x 轴方向（degrees clockwise from north）** — *x* 轴的方向。当您选中 **启用地理空间校正** 复选框时，此参数启用。

## 描述

生成通用客机的平移和旋转信息

Simulation 3D Airliner Pack 模块为 **Type** 设置为 `Airliner` 的 Simulation 3D Aircraft 模块创建平移和旋转信息。使用 Simulation 3D Airliner Pack 模块将平移和旋转信息提供给 Simulation 3D Aircraft 模块的 **Translation** 和 **Rotation** 输入端口。
