---
type: simulink-block
title: 'Simulation 3D CubeSat Pack'
family: 'animation'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation / Simulation 3D'
documentation_page: 'simulation3dcubesatpack'
documentation_source_path: 'simulation3dcubesatpack.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D CubeSat Pack

## 端口

### 输入

### **Body\_T** — 机体平移 1×3 矩阵

机体平移，指定为 1×3 矩阵。

**数据类型：** `single` | `double`

### **Body\_R** — 机体旋转 1×3 矩阵

机体旋转，指定为 1×3 矩阵。

**数据类型：** `single` | `double`
### 输出

### **Translation** — 航天器平移 10×3 数组

CubeSat 的航天器平移，返回为 10×3 数组。该信号包含平移 [*X*, *Y*, *Z*]，单位为 meters，数组的每一行对应航天器的一个骨骼。

平移适用于 `CubeSat` 类型的以下骨骼。

| 骨骼 | 索引 |
| --- | --- |
| BODY | 1 |
| ANTENNA1 | 2 |
| ANTENNA2 | 3 |
| ANTENNA3 | 4 |
| SENSOR | 5 |
| SOLAR\_ARRAY1 | 6 |
| SOLAR\_ARRAY1\_1 | 7 |
| SOLAR\_ARRAY2 | 8 |
| SOLAR\_ARRAY2\_2 | 9 |
| THRUSTER | 10 |

### **Rotation** — 航天器旋转 10×3 数组

CubeSat 的航天器旋转，返回为 10×3 数组。

旋转适用于 Translation 端口列出的相同骨骼。

该信号包含旋转 [roll, pitch, yaw]，单位为 radians，数组的每一行对应航天器的一个骨骼。

## 参数

要交互式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **属性检查器**。

### 传感器

### **天线 1 平移** — 用于启用 Antenna1\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Antenna1\_T** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Antenna1_T` |
| **值：** | `'off'`（默认） | `'on'` |

### **天线 1 旋转** — 用于启用 Antenna1\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Antenna1\_R** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Antenna1_R` |
| **值：** | `'off'`（默认） | `'on'` |

### **天线 2 平移** — 用于启用 Antenna2\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Antenna2\_T** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Antenna2_T` |
| **值：** | `'off'`（默认） | `'on'` |

### **天线 2 旋转** — 用于启用 Antenna2\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Antenna2\_R** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Antenna2_R` |
| **值：** | `'off'`（默认） | `'on'` |

### **天线 3 平移** — 用于启用 Antenna3\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Antenna3\_T** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Antenna3_T` |
| **值：** | `'off'`（默认） | `'on'` |

### **天线 3 旋转** — 用于启用 Antenna3\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Antenna3\_R** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Antenna3_R` |
| **值：** | `'off'`（默认） | `'on'` |

### **传感器平移** — 用于启用 Sensor\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Sensor\_T** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Sensor_T` |
| **值：** | `'off'`（默认） | `'on'` |

### **传感器旋转** — 用于启用 Sensor\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Sensor\_R** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Sensor_R` |
| **值：** | `'off'`（默认） | `'on'` |

### 太阳能阵列

### **太阳能阵列 1 平移** — 用于启用 SolarArray1\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **SolarArray1\_T** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SolarArray1_T` |
| **值：** | `'off'`（默认） | `'on'` |

### **太阳能阵列 1 旋转** — 用于启用 SolarArray1\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **SolarArray1\_R** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SolarArray1_R` |
| **值：** | `'off'`（默认） | `'on'` |

### **太阳能阵列 1.1 平移** — 用于启用 SolarArray1\_1\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **SolarArray1\_1\_T** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SolarArray1_1_T` |
| **值：** | `'off'`（默认） | `'on'` |

### **太阳能阵列 1.1 旋转** — 用于启用 SolarArray1\_1\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **SolarArray1\_1\_R** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SolarArray1_1_R` |
| **值：** | `'off'`（默认） | `'on'` |

### **太阳能阵列 2 平移** — 用于启用 SolarArray2\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **SolarArray2\_T** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SolarArray2_T` |
| **值：** | `'off'`（默认） | `'on'` |

### **太阳能阵列 2 旋转** — 用于启用 SolarArray2\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **SolarArray2\_R** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SolarArray2_R` |
| **值：** | `'off'`（默认） | `'on'` |

### **太阳能阵列 2.2 平移** — 用于启用 SolarArray2\_2\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **SolarArray2\_2\_T** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SolarArray2_2_T` |
| **值：** | `'off'`（默认） | `'on'` |

### **太阳能阵列 2.2 旋转** — 用于启用 SolarArray2\_2\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **SolarArray2\_2\_R** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SolarArray2_2_R` |
| **值：** | `'off'`（默认） | `'on'` |

### 推进器

### **推进器平移** — 用于启用 Thruster\_T 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Thruster\_T** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Thruster_T` |
| **值：** | `'off'`（默认） | `'on'` |

### **推进器旋转** — 用于启用 Thruster\_R 输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **Thruster\_R** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Thruster_R` |
| **值：** | `'off'`（默认） | `'on'` |

### 输入

### **选择输入坐标系** — 输入坐标系 `NED`（默认）| `Fixed-frame` | `ICRF`

选择输入坐标系，以相对于北东地（NED）、固定坐标系（Fixed-frame）或国际天球参考系（ICRF）定位航空航天飞行器。

如果模型包含关联的 Simulation 3D Scene Configuration 模块，则 Simulation 3D CubeSat Pack 模块使用 Simulation 3D Scene Configuration 的坐标系。在这种情况下，**选择输入坐标系** 可能会被禁用。有关 Simulation 3D CubeSat Pack 模块坐标系的详细信息，请参阅算法。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `GeoRadioButton` |
| **值：** | `'NED'`（默认） | `'Fixed-frame'` | `'ICRF'` |

## 所属库

Aerospace Blockset / Animation / Simulation 3D

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024a 中引入**

### R2025a：Simulation 3D CubeSat Pack 模块现在与 Simulation 3D Scene Configuration 模块同步坐标系

Simulation 3D CubeSat Pack 模块有以下更改：

- **地理空间** 选项卡已重命名为 **输入** 选项卡。
- 在 **输入** 选项卡上，**选择输入坐标系** 窗格现在包含以下坐标系按钮：

  - **Fixed-frame** — 固定坐标系。选择此坐标系时，注释 `Fixed-frame` 会显示在 pack 模块图标下方。
  - **ICRF** — 国际天球参考系坐标系。选择此坐标系时，注释 `ICRF` 会显示在 pack 模块图标下方。
  - **NED** — 北东地坐标系。选择此坐标系时，注释 `NED` 会显示在 pack 模块图标下方。

  如果模型包含 Simulation 3D pack 模块和关联的 Simulation 3D Scene Configuration 模块，则 Simulation 3D CubeSat Pack 的 **输入** 选项卡选项可能会被禁用。在这种情况下，Simulation 3D CubeSat Pack 会与 Simulation 3D Scene Configuration 模块同步坐标系。
- 坐标系在模块下方显示为注释。
- **Enable geospatial correction** 和 **Direction of x-axis (degrees clockwise from north)** 参数已被移除。

## 描述

为 CubeSat 创建平移和旋转输入矩阵

Simulation 3D CubeSat Pack 模块为 **类型** 设置为 `CubeSat` 的 Simulation 3D Spacecraft 模块创建平移和旋转信息。使用 Simulation 3D CubeSat Pack 模块向 Simulation 3D Spacecraft 模块的 **Translation** 和 **Rotation** 输入端口提供平移和旋转信息。
