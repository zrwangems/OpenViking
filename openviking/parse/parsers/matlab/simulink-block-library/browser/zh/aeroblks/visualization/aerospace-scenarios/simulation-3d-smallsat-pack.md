---
type: simulink-block
title: 'Simulation 3D SmallSat Pack'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Visualization / Aerospace Scenarios'
documentation_page: 'simulation3dsmallsatpack'
documentation_source_path: 'simulation3dsmallsatpack.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D SmallSat Pack

## 端口

### 输入

### **Body\_T** — 机体平移 1×3 矩阵

机体平移，指定为 1×3 矩阵。

**数据类型：** `single` | `double`

### **Body\_R** — 机体旋转 1×3 矩阵

机体旋转，指定为 1×3 矩阵。

**数据类型：** `single` | `double`
### 输出

### **Translation** — 航天器平移 20×3 数组

SmallSat 的航天器平移，返回为 20×3 数组。该信号包含平移 [*X*, *Y*, *Z*]，以米为单位，数组的每一行对应航天器的一个骨骼。

该平移应用于 `SmallSat` 类型的以下骨骼。

| 骨骼 | 索引 |
| --- | --- |
| BODY | 1 |
| ANTENNA1 | 2 |
| ANTENNA2 | 3 |
| ANTENNA3 | 4 |
| ANTENNA4 | 5 |
| SENSOR1 | 6 |
| SENSOR2 | 7 |
| SENSOR3 | 8 |
| SENSOR4 | 9 |
| SOLAR\_ARRAY1 | 10 |
| SOLAR\_ARRAY1\_1 | 11 |
| SOLAR\_ARRAY1\_1\_1 | 12 |
| SOLAR\_ARRAY1\_1\_1\_1 | 13 |
| SOLAR\_ARRAY1\_1\_1\_1\_1 | 14 |
| SOLAR\_ARRAY2 | 15 |
| SOLAR\_ARRAY2\_2 | 16 |
| SOLAR\_ARRAY2\_2\_2 | 17 |
| SOLAR\_ARRAY2\_2\_2\_2 | 18 |
| SOLAR\_ARRAY2\_2\_2\_2\_2 | 19 |
| THRUSTER | 20 |

### **Rotation** — 航天器旋转 20×3 数组

SmallSat 的航天器旋转，返回为 20×3 数组。

该旋转应用于 Translation 端口所列的相同骨骼。

该信号包含旋转 [横滚、俯仰、偏航]，以弧度为单位，数组的每一行对应航天器的一个骨骼。

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### 传感器

### **天线 1 平移** — 用于启用 Antenna1\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Antenna1\_T** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Antenna1_T` |
| **值：** | `'off'`（默认）| `'on'` |

### **天线 1 旋转** — 用于启用 Antenna1\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Antenna1\_R** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Antenna1_R` |
| **值：** | `'off'`（默认）| `'on'` |

### **天线 2 平移** — 用于启用 Antenna2\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Antenna2\_T** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Antenna2_T` |
| **值：** | `'off'`（默认）| `'on'` |

### **天线 2 旋转** — 用于启用 Antenna2\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Antenna2\_R** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Antenna2_R` |
| **值：** | `'off'`（默认）| `'on'` |

### **天线 3 平移** — 用于启用 Antenna3\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Antenna3\_T** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Antenna3_T` |
| **值：** | `'off'`（默认）| `'on'` |

### **天线 3 旋转** — 用于启用 Antenna3\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Antenna3\_R** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Antenna3_R` |
| **值：** | `'off'`（默认）| `'on'` |

### **天线 4 平移** — 用于启用 Antenna4\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Antenna4\_T** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Antenna4_T` |
| **值：** | `'off'`（默认）| `'on'` |

### **天线 4 旋转** — 用于启用 Antenna4\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Antenna4\_R** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Antenna4_R` |
| **值：** | `'off'`（默认）| `'on'` |

### **传感器 1 平移** — 用于启用 Sensor1\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Sensor1\_T** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Sensor1_T` |
| **值：** | `'off'`（默认）| `'on'` |

### **传感器 1 旋转** — 用于启用 Sensor1\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Sensor1\_R** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Sensor1_R` |
| **值：** | `'off'`（默认）| `'on'` |

### **传感器 2 平移** — 用于启用 Sensor2\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Sensor2\_T** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Sensor2_T` |
| **值：** | `'off'`（默认）| `'on'` |

### **传感器 2 旋转** — 用于启用 Sensor2\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Sensor2\_R** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Sensor2_R` |
| **值：** | `'off'`（默认）| `'on'` |

### **传感器 3 平移** — 用于启用 Sensor3\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Sensor3\_T** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Sensor3_T` |
| **值：** | `'off'`（默认）| `'on'` |

### **传感器 3 旋转** — 用于启用 Sensor3\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Sensor3\_R** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Sensor3_R` |
| **值：** | `'off'`（默认）| `'on'` |

### **传感器 4 平移** — 用于启用 Sensor4\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Sensor4\_T** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Sensor4_T` |
| **值：** | `'off'`（默认）| `'on'` |

### **传感器 4 旋转** — 用于启用 Sensor4\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Sensor4\_R** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Sensor4_R` |
| **值：** | `'off'`（默认）| `'on'` |

### 太阳能电池阵

### **太阳能电池阵 1 平移** — 用于启用 SolarArray1\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **SolarArray1\_T** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SolarArray1_T` |
| **值：** | `'off'`（默认）| `'on'` |

### **太阳能电池阵 1 旋转** — 用于启用 SolarArray1\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **SolarArray1\_R** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SolarArray1_R` |
| **值：** | `'off'`（默认）| `'on'` |

### **太阳能电池阵 1.1 平移** — 用于启用 SolarArray1\_1\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **SolarArray1\_1\_T** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SolarArray1_1_T` |
| **值：** | `'off'`（默认）| `'on'` |

### **太阳能电池阵 1.1 旋转** — 用于启用 SolarArray1\_1\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **SolarArray1\_1\_R** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SolarArray1_1_R` |
| **值：** | `'off'`（默认）| `'on'` |

### **太阳能电池阵 1.1.1 平移** — 用于启用 SolarArray1\_1\_1\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **SolarArray1\_1\_1\_T** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SolarArray1_1_1_T` |
| **值：** | `'off'`（默认）| `'on'` |

### **太阳能电池阵 1.1.1 旋转** — 用于启用 SolarArray1\_1\_1\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **SolarArray1\_1\_1\_R** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SolarArray1_1_1_R` |
| **值：** | `'off'`（默认）| `'on'` |

### **太阳能电池阵 1.1.1.1 平移** — 用于启用 SolarArray1\_1\_1\_1\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **SolarArray1\_1\_1\_1\_T** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SolarArray1_1_1_1_T` |
| **值：** | `'off'`（默认）| `'on'` |

### **太阳能电池阵 1.1.1.1 旋转** — 用于启用 SolarArray1\_1\_1\_1\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **SolarArray1\_1\_1\_1\_R** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SolarArray1_1_1_1_R` |
| **值：** | `'off'`（默认）| `'on'` |

### **太阳能电池阵 1.1.1.1.1 平移** — 用于启用 SolarArray1\_1\_1\_1\_1\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **SolarArray1\_1\_1\_1\_1\_T** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SolarArray1_1_1_1_1_T` |
| **值：** | `'off'`（默认）| `'on'` |

### **太阳能电池阵 1.1.1.1.1 旋转** — 用于启用 SolarArray1\_1\_1\_1\_1\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **SolarArray1\_1\_1\_1\_1\_R** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SolarArray1_1_1_1_1_R` |
| **值：** | `'off'`（默认）| `'on'` |

### **太阳能电池阵 2 平移** — 用于启用 SolarArray2\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **SolarArray2\_T** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SolarArray2_T` |
| **值：** | `'off'`（默认）| `'on'` |

### **太阳能电池阵 2 旋转** — 用于启用 SolarArray2\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **SolarArray2\_R** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SolarArray2_R` |
| **值：** | `'off'`（默认）| `'on'` |

### **太阳能电池阵 2.2 平移** — 用于启用 SolarArray2\_2\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **SolarArray2\_2\_T** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SolarArray2_2_T` |
| **值：** | `'off'`（默认）| `'on'` |

### **太阳能电池阵 2.2 旋转** — 用于启用 SolarArray2\_2\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **SolarArray2\_2\_R** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SolarArray2_2_R` |
| **值：** | `'off'`（默认）| `'on'` |

### **太阳能电池阵 2.2.2 平移** — 用于启用 SolarArray2\_2\_2\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **SolarArray2\_2\_2\_T** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SolarArray2_2_2_T` |
| **值：** | `'off'`（默认）| `'on'` |

### **太阳能电池阵 2.2.2 旋转** — 用于启用 SolarArray2\_2\_2\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **SolarArray2\_2\_2\_R** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SolarArray2_2_2_R` |
| **值：** | `'off'`（默认）| `'on'` |

### **太阳能电池阵 2.2.2.2 平移** — 用于启用 SolarArray2\_2\_2\_2\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **SolarArray2\_2\_2\_2\_T** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SolarArray2_2_2_2_T` |
| **值：** | `'off'`（默认）| `'on'` |

### **太阳能电池阵 2.2.2.2 旋转** — 用于启用 SolarArray2\_2\_2\_2\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **SolarArray2\_2\_2\_2\_R** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SolarArray2_2_2_2_R` |
| **值：** | `'off'`（默认）| `'on'` |

### **太阳能电池阵 2.2.2.2.2 平移** — 用于启用 SolarArray2\_2\_2\_2\_2\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **SolarArray2\_2\_2\_2\_2\_T** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SolarArray2_2_2_2_2_T` |
| **值：** | `'off'`（默认）| `'on'` |

### **太阳能电池阵 2.2.2.2.2 旋转** — 用于启用 SolarArray2\_2\_2\_2\_2\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **SolarArray2\_2\_2\_2\_2\_R** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SolarArray2_2_2_2_2_R` |
| **值：** | `'off'`（默认）| `'on'` |

### 推进器

### **推进器平移** — 用于启用 Thruster\_T 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Thruster\_T** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Thruster_T` |
| **值：** | `'off'`（默认）| `'on'` |

### **推进器旋转** — 用于启用 Thruster\_R 输入端的选项 `off`（默认）| `on`

选择此参数以启用 **Thruster\_R** 输入端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Thruster_R` |
| **值：** | `'off'`（默认）| `'on'` |

### 输入

### **选择输入坐标系** — 输入坐标系 `NED`（默认）| `Fixed-frame` | `ICRF`

选择输入坐标系，以相对于北-东-下 (NED)、固定坐标系 (Fixed-frame) 或国际天球参考框架 (ICRF) 定位航空航天器。

如果模型包含关联的 Simulation 3D Scene Configuration 模块，Simulation 3D SmallSat Pack 模块使用 Simulation 3D Scene Configuration 的坐标系。在这种情况下，**选择输入坐标系** 可能会被禁用。有关 Simulation 3D SmallSat Pack 模块坐标系的详细信息，请参阅算法。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `GeoRadioButton` |
| **值：** | `'NED'`（默认）| `'Fixed-frame'` | `'ICRF'` |

## 所属库

Aerospace Blockset / Animation / Simulation 3D

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2024a 中引入**

### R2025a：Simulation 3D SmallSat Pack 模块现在与 Simulation 3D Scene Configuration 模块同步坐标系

Simulation 3D SmallSat Pack 模块具有以下更改：

- **地理空间** 选项卡已重命名为 **输入** 选项卡。
- 在 **输入** 选项卡上，**选择输入坐标系** 窗格现在包含这些坐标系按钮：

  - **Fixed-frame** — Fixed-frame 坐标系。选择此坐标系后，注释 `Fixed-frame` 会出现在 pack 模块图标下方。
  - **ICRF** — International Celestial Reference Frame 坐标系。选择此坐标系后，注释 `ICRF` 会出现在 pack 模块图标下方。
  - **NED** — North-east-down 坐标系。选择此坐标系后，注释 `NED` 会出现在 pack 模块图标下方。

  如果模型包含 Simulation 3D pack 模块和关联的 Simulation 3D Scene Configuration 模块，则 Simulation 3D SmallSat Pack 的 **输入** 选项卡选项可能会被禁用。在这种情况下，Simulation 3D SmallSat Pack 会与 Simulation 3D Scene Configuration 模块同步坐标系。
- 坐标系显示为模块下方的注释。
- **启用地理空间校正** 和 **x 轴方向（从北顺时针的度数）** 参数已被移除。

## 描述

为 SmallSat 创建平移和旋转输入矩阵

Simulation 3D SmallSat Pack 模块为 **Type** 设置为 `SmallSat` 的 Simulation 3D Spacecraft 模块创建平移和旋转信息。使用 Simulation 3D SmallSat Pack 模块将平移和旋转信息提供给 Simulation 3D Spacecraft 模块的 **Translation** 和 **Rotation** 输入端口。
