---
type: simulink-block
title: 'Simulation 3D Spacecraft'
family: 'animation'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation / Simulation 3D'
documentation_page: 'simulation3dspacecraft'
documentation_source_path: 'simulation3dspacecraft.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Spacecraft

## 端口

### 输入

### **Translation** — 航天器平移 10×3 数组 | 20×3 数组

航天器平移，指定为：

- 10×3 数组 — 航天器 **Type** 为 `CubeSat`。
- 20×3 数组 — 航天器 **Type** 为 `SmallSat`。

该信号包含平移 [*X*, *Y*, *Z*]，以 meters 为单位，数组的每一行对应航天器的一个骨骼。

平移应用于 `CubeSat` 类型的以下骨骼。

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

平移应用于 `SmallSat` 类型的以下骨骼。

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

**数据类型：** `single` | `double`

### **Rotation** — 航天器旋转 10×3 数组 | 20×3 数组

航天器旋转，指定为：

- 10×3 数组 — 航天器 **Type** 为 `CubeSat`。
- 20×3 数组 — 航天器 **Type** 为 `SmallSat`。

旋转应用于为 Translation 端口列出的相同骨骼。

该信号包含旋转 [roll, pitch, yaw]，以 radians 为单位，数组的每一行对应航天器的一个骨骼。

**数据类型：** `single` | `double`

### **Scale** — 网格缩放 `[1 1 1]`（默认）| 1×3 数组

网格缩放，指定为 1×3 数组。

#### 依赖关系

要启用此端口，请将 **Scale source** 参数设置为 `Port`。

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink Toolstrip 中，在 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### **Type** — 航天器类型 `CubeSat`（默认）| `SmallSat`

航天器类型，指定为 `CubeSat` 或 `SmallSat`。

#### 依赖关系

要设置此参数，请将 **Initial translation** 和 **Initial rotation** 参数设置为匹配的数组大小。未能适当设置这些数组大小会导致错误。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Mesh` |
| **值：** | `CubeSat`（默认）| `SmallSat` |

**示例：** `CubeSat`

### **Path to CubeSat mesh** — CubeSat 网格路径 `/MathWorksAerospaceContent/Vehicles/Spacecraft/CubeSat/Mesh/SK_CubeSat.SK_CubeSat`（默认）| character vector

CubeSat 网格路径，指定为 character vector。要创建自定义航空航天网格，请参阅 Prepare Custom Aircraft Mesh for the Unreal Editor。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `CubeSat`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `MeshPath` |
| **值：** | `/MathWorksAerospaceContent/Vehicles/Spacecraft/CubeSat/Mesh/SK_CubeSat.SK_CubeSat` | character vector |

**示例：** `/MathWorksAerospaceContent/Vehicles/Spacecraft/CubeSat/Mesh/SK_CubeSat.SK_CubeSat`

### **Path to SmallSat mesh** — SmallSat 网格路径 `/MathWorksAerospaceContent/Vehicles/Spacecraft/SmallSat/Mesh/SK_SmallSat.SK_SmallSat`（默认）| character vector

SmallSat 网格路径，指定为 character vector。要创建自定义航空航天网格，请参阅 Prepare Custom Aircraft Mesh for the Unreal Editor。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `SmallSat`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `MeshPathSmall` |
| **值：** | `/MathWorksAerospaceContent/Vehicles/Spacecraft/SmallSat/Mesh/SK_SmallSat.SK_SmallSat` | character vector |

**示例：** `/MathWorksAerospaceContent/Vehicles/Spacecraft/SmallSat/Mesh/SK_SmallSat.SK_SmallSat`

### **Name** — 航天器名称 `SimulinkVehicle1`（默认）| character vector

航天器名称，指定为 character vector。默认情况下，当你在模型中使用 Simulation 3D Spacecraft 模块时，该模块会将 **Name** 参数设置为 `SimulinkVehicleX`。`X` 的值取决于模型中其他 Simulation 3D 模块的数量。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ActorName` |
| **值：** | `SimulinkVehicle1`（默认）| character vector |

**示例：** `SimulinkVehicle1`

### **Initial translation (m)** — 航天器的初始平移 `zeros(10,3)`（默认）| 10×3 数组 | 20×3 数组

航天器的初始平移，指定为 10×3 数组或 20×3 数组。

#### 依赖关系

此参数必须与你在 **Type** 中设置的航天器类型匹配。未能适当设置这些数组大小会导致错误。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Translation` |
| **值：** | `zeros(10,3)`（默认）| 10×3 数组 | 20×3 数组 |
| **数据类型：** | `single` | `double` |

**示例：** `zeros(10,3)`

### **Initial rotation (rad)** — 航天器的初始旋转 `zeros(10,3)`（默认）| 10×3 数组 | 20×3 数组

航天器的初始旋转，指定为 10×3 或 20×3 数组。

#### 依赖关系

此参数必须与你在 **Type** 中设置的航天器类型匹配。未能适当设置这些数组大小会导致错误。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Rotation` |
| **值：** | `zeros(10,3)`（默认）| 10×3 数组 | 20×3 数组 |
| **数据类型：** | `single` | `double` |

**示例：** `zeros(10,3)`

### **Scale source** — 缩放源 `Dialog`（默认）| `Port`

缩放源，指定为 `Dialog` 或 `Port`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ScaleInputPort` |
| **值：** | `Dialog`（默认）| `Port` |

**示例：** `Dialog`

### **Initial scale** — 初始网格缩放 `[1 1 1]`（默认）| 1×3 数组

初始网格缩放，指定为 1×3 数组。

#### 依赖关系

要启用此参数，请将 **Scale source** 设置为 `Port`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `InitialScale` |
| **值：** | `[1 1 1]`（默认）| 1×3 数组 |
| **数据类型：** | `single` | `double` |

**示例：** `[1 1 1]`

### **Scale** — 网格缩放 `[1 1 1]`（默认）| 1×3 数组

网格缩放，指定为 1×3 数组。

#### 依赖关系

要启用此参数，请将 **Scale source** 设置为 `Dialog`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Scale` |
| **值：** | `[1 1 1]`（默认）| 1×3 数组 |
| **数据类型：** | `single` | `double` |

**示例：** `[1 1 1]`

### **Sample time** — 采样时间 `0.02`（默认）| real scalar

采样时间，*Ts*。图形帧率是采样时间的倒数。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `'-1'`（默认）| real scalar |

**示例：** `'-1'`

## 所属库

Aerospace Blockset / Animation / Simulation 3D

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024a 中引入**

### R2024b：Simulation 3D Environment：为 Simulation 3D Spacecraft 缩放网格

现在，你可以使用 **Scale** 参数或 **Scale** 端口更改 Simulation 3D Spacecraft 模块的网格大小。默认缩放是 1×3 向量 `[1 1 1]`。

要启用这些参数或端口，请使用 **Scale source** 参数。

- `Dialog` — 启用 **Scale** 参数。
- `Port` — 启用 **Scale** 端口和 **Initial scale** 参数。

## 描述

在 3D 环境中实现航天器

**注意**

使用 Simulation 3D Spacecraft 模块对模型进行仿真需要 Simulink® 3D Animation™。

Simulation 3D Spacecraft 模块使用平移和旋转在 3D 可视化环境中实现航天器，以放置航天器。

要使用此模块，你的模型必须包含 Simulation 3D Scene Configuration 模块。如果将 Simulation 3D Spacecraft 模块的 **Sample time** 参数设置为 `-1`，则该模块使用 Simulation 3D Scene Configuration 模块中指定的采样时间。

该模块输入使用航天器北-东-下（NED）*右手*（RH）*笛卡尔*坐标系。

- *X* 轴 — 沿航天器纵轴，指向正前方
- *Y* 轴 — 沿航天器横轴，指向右侧
- *Z* 轴 — 指向下方

有关详细信息，请参阅 Fundamental Coordinate System Concepts。

**提示**

验证 Simulation 3D Spacecraft 模块在 Simulation 3D Scene Configuration 模块之前执行。这样，Simulation 3D Spacecraft 模块会在 Unreal Engine® 3D 可视化环境接收数据之前准备好信号数据。要检查模块执行顺序，请右键单击每个模块并选择 **Properties**。在 **General** 选项卡上，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Spacecraft — `-1`

有关执行顺序的详细信息，请参阅 Control and Display Execution Order。

### 骨架、骨骼和网格

Unreal Engine 使用*骨架*、*骨骼*和*网格*来定义 3D 模型。骨架由一组骨骼组成。网格是骨架的外层覆盖物。航天器部件是链接到骨骼的网格区段，例如天线或推进器。有关详细信息，请参阅 https://docs.unrealengine.com/4.27/AnimatingObjects/SkeletalMeshAnimation/Skeleton/。

有关 Simulation 3D Space block 平移输入数组如何连接到航天器类型的详细信息，请参阅 Algorithms。
