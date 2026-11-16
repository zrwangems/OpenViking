---
type: simulink-block
title: 'Simulation 3D Sky Hogg Pack'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation / Simulation 3D'
documentation_page: 'simulation3dskyhoggpack'
documentation_source_path: 'simulation3dskyhoggpack.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Sky Hogg Pack

## 端口

### 输入

### **Body\_T** — 机体平移 1×3 矩阵

机体平移，指定为 1×3 矩阵。

**数据类型：** `single` | `double`

### **Body\_R** — 机体旋转 1×3 矩阵

机体旋转，指定为 1×3 矩阵。

**数据类型：** `single` | `double`

### **Propeller\_R** — 螺旋桨旋转 1×3 矩阵

螺旋桨旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **螺旋桨** 参数。

**数据类型：** `single` | `double`

### **Rudder\_R** — 方向舵旋转 1×3 矩阵

方向舵旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **方向舵旋转** 参数。

**数据类型：** `single` | `double`

### **Elevator\_R** — 升降舵旋转 1×3 矩阵

升降舵旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **升降舵旋转** 参数。

**数据类型：** `single` | `double`

### **Left\_Aileron\_R** — 左副翼旋转 1×3 矩阵

左副翼旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **左副翼旋转** 参数。

**数据类型：** `single` | `double`

### **Right\_Aileron\_R** — 右副翼旋转 1×3 矩阵

右副翼旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **右副翼旋转** 参数。

**数据类型：** `single` | `double`

### **Flaps\_R** — 襟翼旋转 1×3 矩阵

襟翼旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **襟翼旋转** 参数。

**数据类型：** `single` | `double`

### **Nose\_Wheel\_Strut\_R** — 前轮支柱旋转 1×3 矩阵

前轮支柱旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **前轮支柱旋转** 参数。

**数据类型：** `single` | `double`

### **Nose\_Wheel\_R** — 前轮旋转 1×3 矩阵

前轮旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **前轮旋转** 参数。

**数据类型：** `single` | `double`

### **Left\_Wheel\_R** — 左轮旋转 1×3 矩阵

左轮旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **左轮旋转** 参数。

**数据类型：** `single` | `double`

### **Right\_Wheel\_R** — 右轮旋转 1×3 矩阵

右轮旋转，指定为 1×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **右轮旋转** 参数。

**数据类型：** `single` | `double`
### 输出

### **Translation** — 飞行器平移 `11`×`3` 数组

Sky Hogg 的飞行器平移，返回为 `11`×`3` 数组。该信号包含平移
[*X*, *Y*, *Z*]，单位为米，数组的每一行对应飞行器的一个骨骼。

平移适用于 `Sky Hogg` 类型的以下骨骼。

| 骨骼 | 索引 |
| --- | --- |
| BODY | 1 |
| PROPELLER | 2 |
| RUDDER | 3 |
| ELEVATOR | 4 |
| LEFT\_AILERON | 5 |
| RIGHT\_AILERON | 6 |
| FLAPS | 7 |
| NOSE\_WHEEL\_STRUT | 8 |
| NOSE\_WHEEL | 9 |
| LEFT\_WHEEL | 10 |
| RIGHT\_WHEEL | 11 |

### **Rotation** — 飞行器旋转 `11`×`3` 数组

Sky Hogg 飞行器的飞行器旋转，返回为 `11`×`3` 数组。

旋转适用于 Translation 端口列出的相同骨骼。

该信号包含旋转 [roll, pitch, yaw]，单位为弧度，数组的每一行对应飞行器的一个骨骼。

## 参数

### 推进

### **螺旋桨旋转** — 用于启用 Propeller\_R 输入端口的选项 `off`（默认） | `on`

选择此参数以启用 **Propeller\_R** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Propeller_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### 控制

### **方向舵旋转** — 用于启用 Rudder\_R 输入端口的选项 `off`（默认） | `on`

选择此参数以启用 **Rudder\_R** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Rudder_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **升降舵旋转** — 用于启用 Elevator\_R 输入端口的选项 `off`（默认） | `on`

选择此参数以启用 **Elevator\_R** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Elevator_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **左副翼旋转** — 用于启用 Left\_Aileron\_R 输入端口的选项 `off`（默认） | `on`

选择此参数以启用 **Left\_Aileron\_R** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Left_Aileron_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **右副翼旋转** — 用于启用 Right\_Aileron\_R 输入端口的选项 `off`（默认） | `on`

选择此参数以启用 **Right\_Aileron\_R** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Right_Aileron_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **襟翼旋转** — 用于启用 Flaps\_R 输入端口的选项 `off`（默认） | `on`

选择此参数以启用 **Flaps\_R** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Flaps_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### 起落架

### **前轮支柱旋转** — 用于启用 Nose\_Wheel\_Strut\_R 输入端口的选项 `off`（默认） | `on`

选择此参数以启用 **Nose\_Wheel\_Strut\_R** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Nose_Wheel_Strut_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **前轮旋转** — 用于启用 Nose\_Wheel\_R 输入端口的选项 `off`（默认） | `on`

选择此参数以启用 **Nose\_Wheel\_R** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Nose_Wheel_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **左轮旋转** — 用于启用 Left\_Wheel\_R 输入端口的选项 `off`（默认） | `on`

选择此参数以启用 **Left\_Wheel\_R** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Left_Wheel_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **右轮旋转** — 用于启用 Right\_Wheel\_R 输入端口的选项 `off`（默认） | `on`

选择此参数以启用 **Right\_Wheel\_R** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Right_Wheel_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### 输入

### **选择输入坐标系** — 输入坐标系 `NED`（默认） | `Fixed-frame` | `ICRF`

选择输入坐标系，以相对于北-东-下 (NED)、固定坐标系 (`Fixed-frame`) 或国际天球参考系 (ICRF) 定位航空航天器。

如果模型包含关联的 Simulation 3D Scene Configuration 模块，则 Simulation 3D Sky Hogg Pack 模块使用 Simulation 3D Scene Configuration 的坐标系。在这种情况下，**选择输入坐标系** 可能会被禁用。有关 Simulation 3D Sky Hogg Pack 模块坐标系的详细信息，请参阅算法。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |
| --- |
| **参数：** | `GeoRadioButton` |
| **值：** | `'NED'`（默认） | `'Fixed-frame'` | `'ICRF'` |

## 所属库

Aerospace Blockset / Animation / Simulation 3D

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023b 中引入**

### R2025a：Simulation 3D Sky Hogg Pack 模块现在与 Simulation 3D Scene Configuration 模块同步坐标系

Simulation 3D Sky Hogg Pack 模块有以下更改：

- **地理空间** 选项卡已重命名为 **输入** 选项卡。
- 在 **输入** 选项卡上，**选择输入坐标系** 窗格现在包含以下坐标系按钮：

  - **Fixed-frame** — 固定坐标系。选择此坐标系后，注释 `Fixed-frame` 会显示在 pack 模块图标下方。
  - **ICRF** — 国际天球参考系。选择此坐标系后，注释 `ICRF` 会显示在 pack 模块图标下方。
  - **NED** — 北-东-下坐标系。选择此坐标系后，注释 `NED` 会显示在 pack 模块图标下方。

  如果模型包含 Simulation 3D pack 模块和关联的 Simulation 3D Scene Configuration 模块，则 Simulation 3D Sky Hogg Pack 的 **输入** 选项卡选项可能会被禁用。在这种情况下，Simulation 3D Sky Hogg Pack 会与 Simulation 3D Scene Configuration 模块同步坐标系。
- 坐标系会作为注释显示在模块下方。
- **启用地理空间校正** 和 **x 轴方向（从北顺时针方向的度数）** 参数已被移除。

### R2024a：Simulation 3D Sky Hogg Pack 模块现在支持地心地球固定 (ECEF) 输入坐标系

为启用于平移输入的 ECEF 坐标系，Simulation 3D Sky Hogg Pack 模块已更新。将这些参数与 Simulation 3D Scene Configuration 模块中的 **使用地心作为原点 (ECEF)** 参数一起使用。

- **选择输入坐标系**

  - **ECEF** — ECEF 输入坐标系。选择此坐标系后，注释 `Origin: Earth center (ECEF)` 会显示在 pack 模块图标下方。
  - **NED** — NED 坐标系。在 R2024a 之前，NED 是唯一支持的坐标系。
- **x 轴方向（从北顺时针方向的度数）** — *x* 轴的方向。当您选择 **启用地理空间校正** 复选框时，此参数会启用。

## 描述

生成 Sky Hogg 的平移和旋转信息

Simulation 3D Sky Hogg Pack 模块为 **类型** 设置为 `Sky Hogg` 的 Simulation 3D Aircraft 模块创建平移和旋转信息。使用 Simulation 3D Sky Hogg Pack 模块向 Simulation 3D Aircraft 模块的 **Translation** 和 **Rotation** 输入端口提供平移和旋转信息。
