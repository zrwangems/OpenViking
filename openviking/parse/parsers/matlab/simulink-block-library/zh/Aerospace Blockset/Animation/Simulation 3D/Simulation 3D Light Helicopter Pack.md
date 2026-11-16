---
type: simulink-block
title: 'Simulation 3D Light Helicopter Pack'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation / Simulation 3D'
documentation_page: 'simulation3dlighthelicopterpack'
documentation_source_path: 'simulation3dlighthelicopterpack.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Light Helicopter Pack

## 端口

### 输入

### **Body\_T** — Body translation 1-by-3 matrix

机体平移，指定为 1-by-3 矩阵。

**数据类型：** `single` | `double`

### **Engine\_T** — Engine translation 1-by-3 matrix

发动机平移，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine translation** 参数。

**数据类型：** `single` | `double`

### **Rotor1\_T** — Rotor 1 translation 1-by-3 matrix

旋翼 1 平移，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Rotor 1 translation** 参数。

**数据类型：** `single` | `double`

### **Rotor2\_T** — Rotor 2 translation 1-by-3 matrix

旋翼 2 平移，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Rotor 2 translation** 参数。

**数据类型：** `single` | `double`

### **Sensor1\_T** — Sensor 1 translation 1-by-3 matrix

传感器 1 平移，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Sensor 1 translation** 参数。

**数据类型：** `single` | `double`

### **Sensor2\_T** — Sensor 2 translation 1-by-3 matrix

传感器 2 平移，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Sensor 2 translation** 参数。

**数据类型：** `single` | `double`

### **Body\_R** — Body rotation 1-by-3 matrix

机体旋转，指定为 1-by-3 矩阵。

**数据类型：** `single` | `double`

### **Engine\_R** — Engine rotation 1-by-3 matrix

发动机旋转，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Engine rotation** 参数。

**数据类型：** `single` | `double`

### **Rotor1\_R** — Rotor 1 rotation 1-by-3 matrix

旋翼 1 旋转，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Rotor 1 rotation** 参数。

**数据类型：** `single` | `double`

### **Rotor2\_R** — Rotor 2 rotation 1-by-3 matrix

旋翼 2 旋转，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Rotor 2 rotation** 参数。

**数据类型：** `single` | `double`

### **Sensor1\_R** — Sensor 1 rotation 1-by-3 matrix

传感器 1 旋转，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Sensor 1 rotation** 参数。

**数据类型：** `single` | `double`

### **Sensor2\_R** — Sensor 2 rotation 1-by-3 matrix

传感器 2 旋转，指定为 1-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Sensor 2 rotation** 参数。

**数据类型：** `single` | `double`

### 输出

### **Translation** — Light helicopter translation `6`-by-`3` array

轻型直升机的旋翼航空器平移，返回为 `6`-by-`3` 数组。该信号包含平移 [*X*, *Y*, *Z*]，以 meters 为单位，数组的每一行对应旋翼航空器的一个骨骼。

该平移适用于 `Light helicopter` 类型的以下骨骼。

| 骨骼 | 索引 |
| --- | --- |
| BODY | 1 |
| ENGINE | 2 |
| ROTOR1 | 3 |
| ROTOR2 | 4 |
| SENSOR1 | 5 |
| SENSOR2 | 6 |

### **Rotation** — Rotorcraft rotation `6`-by-`3` array

轻型直升机的旋翼航空器旋转，返回为 `6`-by-`3` 数组。

该旋转适用于 Translation 端口下列出的相同骨骼。

该信号包含旋转 [roll, pitch, yaw]，以 radians 为单位，数组的每一行对应旋翼航空器的一个骨骼。

## 参数

### 推进系统

### **Engine translation** — 用于启用 Engine\_T 输入端口的选项 `off` (默认) | `on`

选择此参数以启用 **Engine\_T** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Rotor 1 translation** — 用于启用 Rotor1\_T 输入端口的选项 `off` (默认) | `on`

选择此参数以启用 **Rotor1\_T** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Rotor1_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Rotor 2 translation** — 用于启用 Rotor2\_T 输入端口的选项 `off` (默认) | `on`

选择此参数以启用 **Rotor2\_T** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Rotor2_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Engine rotation** — 用于启用 Engine\_R 输入端口的选项 `off` (默认) | `on`

选择此参数以启用 **Engine\_R** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Engine_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Rotor 1 rotation** — 用于启用 Rotor1\_R 输入端口的选项 `off` (默认) | `on`

选择此参数以启用 **Rotor1\_R** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Rotor1_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Rotor 2 rotation** — 用于启用 Rotor2\_R 输入端口的选项 `off` (默认) | `on`

选择此参数以启用 **Rotor2\_R** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Rotor2_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### 传感器

### **Sensor 1 translation** — 用于启用 Sensor1\_T 输入端口的选项 `off` (默认) | `on`

选择此参数以启用 **Sensor1\_T** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Sensor1_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Sensor 2 translation** — 用于启用 Sensor2\_T 输入端口的选项 `off` (默认) | `on`

选择此参数以启用 **Sensor2\_T** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Sensor2_T` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Sensor 1 rotation** — 用于启用 Sensor1\_R 输入端口的选项 `off` (默认) | `on`

选择此参数以启用 **Sensor1\_R** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Sensor1_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Sensor 2 rotation** — 用于启用 Sensor2\_R 输入端口的选项 `off` (默认) | `on`

选择此参数以启用 **Sensor2\_R** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Sensor2_R` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### 输入

### **Select input coordinate frame** — 输入坐标系 `NED` (默认) | `Fixed-frame` | `ICRF`

选择输入坐标系，以相对于 north-east-down (NED)、fixed-frame (Fixed-frame) 或 International Celestial Reference Frame (ICRF) 定位航空航天器。

如果模型包含关联的 Simulation 3D Scene Configuration 模块，则 Simulation 3D Light Helicopter Pack 模块使用 Simulation 3D Scene Configuration 的坐标系。在这种情况下，**Select input coordinate frame** 可能被禁用。有关 Simulation 3D Light Helicopter Pack 模块坐标系的详细信息，请参阅 Algorithms。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `GeoRadioButton` |
| **值：** | `'NED'` (默认) | `'Fixed-frame'` | `'ICRF'` |

## 所属库

Aerospace Blockset / Animation / Simulation 3D

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**R2023b 中引入**

### R2025a: Simulation 3D Light Helicopter Pack 模块现在与 Simulation 3D Scene Configuration 模块同步坐标系

Simulation 3D Light Helicopter Pack 模块具有以下更改：

- **Geospatial** 选项卡已重命名为 **Input** 选项卡。
- 在 **Input** 选项卡上，**Select input coordinate frame** 窗格现在包含以下坐标系按钮：

  - **Fixed-frame** — Fixed-frame 坐标系。选择此坐标系时，注释 `Fixed-frame` 会出现在 pack 模块图标下方。
  - **ICRF** — International Celestial Reference Frame 坐标系。选择此坐标系时，注释 `ICRF` 会出现在 pack 模块图标下方。
  - **NED** — North-east-down 坐标系。选择此坐标系时，注释 `NED` 会出现在 pack 模块图标下方。

  如果模型包含 Simulation 3D pack 模块和关联的 Simulation 3D Scene Configuration 模块，则 Simulation 3D Light Helicopter Pack 的 **Input** 选项卡选项可能被禁用。在这种情况下，Simulation 3D Light Helicopter Pack 会与 Simulation 3D Scene Configuration 模块同步坐标系。
- 坐标系在模块下方显示为注释。
- **Enable geospatial correction** 和 **Direction of x-axis (degrees clockwise from north)** 参数已被移除。

### R2024a: Simulation 3D Light Helicopter Pack 模块现在支持 Earth-centered Earth-fixed (ECEF) 输入坐标系

为了为平移输入启用 ECEF 坐标系，Simulation 3D Light Helicopter Pack 模块已更新。将这些参数与 Simulation 3D Scene Configuration 模块中的 **Use Earth center as origin (ECEF)** 参数一起使用。

- **Select input coordinate frame**

  - **ECEF** — ECEF 输入坐标系。选择此坐标系时，注释 `Origin: Earth center (ECEF)` 会出现在 pack 模块图标下方。
  - **NED** — NED 坐标系。在 R2024a 之前，NED 是唯一支持的坐标系。
- **Direction of x-axis (degrees clockwise from north)** — *x* 轴方向。当您选择 **Enable geospatial correction** 复选框时，会启用此参数。

## 描述

生成轻型直升机的平移和旋转信息

Simulation 3D Light Helicopter Pack 模块为 **Type** 设置为 `Light helicopter` 的 Simulation 3D Rotorcraft 模块创建平移和旋转信息。使用 Simulation 3D Light Helicopter Pack 模块将平移和旋转信息提供给 Simulation 3D Rotorcraft 模块的 **Translation** 和 **Rotation** 输入端口。
