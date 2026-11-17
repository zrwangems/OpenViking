---
type: simulink-block
title: 'Lane Change'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / Drive Cycle and Maneuvers'
documentation_page: 'lanechange'
documentation_source_path: 'ref/lanechange.html'
language: zh-CN
chinese_source: worker-translation
---

# Lane Change

## 端口

### 输入

### **xdot** — 车辆纵向速度标量

在车体坐标系下的车辆纵向速度，指定为标量，单位为 m/s。

**数据类型：** `double`

### **X** — 车辆质心纵向位置标量

在全局坐标系下的车辆质心纵向位置，指定为标量，单位为 m。

**数据类型：** `double`

### **Y** — 车辆质心横向位置标量

在全局坐标系下的车辆质心横向位置，指定为标量，单位为 m。

**数据类型：** `double`

### **psi** — 车辆横摆角标量

相对于全局坐标系的车辆横摆角，指定为标量，单位为 m。

**数据类型：** `double`
### 输出

### **DrvRef** — 驾驶员参考数据总线

驾驶员参考数据，以包含以下模块值的总线形式返回。

| 信号 | 描述 | 单位 |
| --- | --- | --- |
| `LngRef` | 纵向参考速度 | m/s |
| `LtrRef` | 横向参考位移 | m |
| `XRef` | 车辆全局纵向参考位置 | m |
| `YRef` | 车辆全局横向参考位置 | m |
| `PhiRef` | 车辆全局横摆参考位置 | rad |
| `CurvRef` | 参考路径曲率 | 1/m |
| `CurvGradRef` | 参考路径曲率梯度 | 1/m^2 |

**数据类型：** `bus`

### **DrvCmd** — 驾驶员指令数据总线

驾驶员指令数据，以包含以下模块值的总线形式返回。

| 信号 | | 描述 | 单位 |
| --- | --- | --- | --- |
| `SteerCmd` | `EnblSteerCmd` | 用于覆盖驾驶员模型转向指令的布尔信号 | one |
| `SteerCmd` | 方向盘转角 | one |
| `SteerZero` | 当值为 `true` 时，用于将驾驶员模型转向指令覆盖为零的布尔信号 | one |
| `SteerHld` | 当为 `true` 时，用于保持当前驾驶员模型转向输出的布尔信号 | one |
| `AccelCmd` | `EnblAccelCmd` | 用于覆盖驾驶员模型加速指令的布尔信号 | one |
| `AccelCmd` | 归一化加速踏板输入 | one |
| `AccelHld` | 当为 `true` 时，用于保持当前驾驶员模型加速输出的布尔信号 | one |
| `AccelZero` | 当值为 `true` 时，用于将驾驶员模型加速指令覆盖为零的布尔信号 | one |
| `DecelCmd` | `EnblDecelCmd` | 用于覆盖驾驶员模型减速指令的布尔信号 | one |
| `DecelCmd` | 归一化减速踏板或制动输入 | one |
| `DecelHld` | 当为 `true` 时，用于保持当前驾驶员模型减速输出的布尔信号 | one |
| `DecelZero` | 当值为 `true` 时，用于将驾驶员模型减速指令覆盖为零的布尔信号 | one |
| `HndBrkCmd` | 归一化手刹或驻车制动输入 | one |
| `TransCmd` | `TransModeCmd` | 用于指定变速器模式的指令 | one |
| `GearCmd` | 用于指定手动挡位编号或自动变速器换挡杆位置的指令 | one |
| `UpShiftCmd` | 升挡指令 | one |
| `DwnShiftCmd` | 降挡指令 | one |
| `ClutchCmd` | 手动变速器的归一化离合器分离指令 | one |

**注意**

默认情况下，`TransCmd` 总线不会被主动使用。使用 Bus Assignment 模块覆盖 `TransCmd` 总线，以自定义和扩展场景。

Bus Assignment 模块覆盖 Lane Change 模块的 TransModeCmd 输出的框图。

**数据类型：** `bus`

### **Info** — 信息数据总线

信息数据，以包含以下模块值的总线形式返回。

| 信号 | 描述 | 单位 |
| --- | --- | --- |
| `LeftBnd` | 左侧车道边界 | m |
| `RightBnd` | 右侧车道边界 | m |
| `LtrlRef` | 横向参考位移 | m |
| `XRef` | 车辆全局纵向参考位置 | m |
| `YRef` | 车辆全局横向参考位置 | m |

#### 依赖关系

要启用此参数，请选择 **Output info bus**。

**数据类型：** `bus`

## 参数

要交互式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡中，在 **Prepare** 库中选择 **Property Inspector**。

### **Lane change type, changeType** — 要执行的换道类型 `Double lane change (ISO 3888-1)`（默认）| `Obstacle avoidance (ISO 3888-2)` | `Obstacle avoidance truck-trailer (SAE J2179)`

要执行的换道类型 [[1],[2],[3],[4]]。

使用 **Lane change type, changeType** 参数选择所需的换道类型。

| 操作 | 换道类型设置 |
| --- | --- |
| 模拟双移线。该模块保持加速度恒定。 | `Double lane change (ISO 3888-1)` |
| 模拟带避障的换道。该模块指令零加速度。 | `Obstacle avoidance (ISO 3888-2)` |
| 模拟卡车-挂车带避障的换道。该模块不覆盖加速度指令。 | `Obstacle truck-trailer (SAE J2179)` |

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `changeType` |
| **值：** | `Double lane change (ISO 3888-1)`（默认）| `Obstacle avoidance (ISO 3888-2)` | `Obstacle avoidance truck-trailer (SAE J2179)` |
| **数据类型：** | `character vector` |

### **Maneuver start time, tStart [s]** — 开始时间 `3`（默认）| 正标量

机动开始时间，单位为 s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tStart` |
| **值：** | `3`（默认）| 正标量 |
| **数据类型：** | `double` |

### **Inertial longitudinal position of gate extrance, XGate [m]** — 门入口起点的全局纵向位置 `176`（默认）| 标量

门入口起点的全局纵向位置，单位为 m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `XGate` |
| **值：** | `176`（默认）| 标量 |
| **数据类型：** | `double` |

### **Longitudinal entrance velocity setpoint, velRef** — 目标速度 `35`（默认）| 正标量

目标速度。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `velRef` |
| **值：** | `35`（默认）| 正标量 |
| **数据类型：** | `double` |

### **Longitudinal entrance velocity setpoint units, velRefUnit []** — 单位 `mph`（默认）

目标速度的单位。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `velRefUnit` |
| **值：** | `mph`（默认）| 字符向量 |
| **数据类型：** | `character vector` |

### **Distance after target speed to begin reference, xStart [m]** — 纵向偏移 `2`（默认）| 标量

用于偏移标称路径的纵向偏移，单位为 m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `xStart` |
| **值：** | `2`（默认）| 标量 |
| **数据类型：** | `double` |

### **Vehicle width, vehWidth [m]** — 标称车辆宽度 `2`（默认）| 正标量

标称车辆宽度，单位为 m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `vehWidth` |
| **值：** | `2`（默认） | 正标量 |
| **数据类型：** | `double` |

### **横向偏移，nomLatOffset [m]** — 标称横向偏移 `0`（默认） | 标量

标称横向偏移，单位为 m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `nomLatOffset` |
| **值：** | `0`（默认） | 标量 |
| **数据类型：** | `double` |

### **横向参考位置断点，latRefbp [m]** — 纵向路径断点 1×*n* 向量（默认）

与横向参考点 **latRef** 对应的纵向路径断点，指定为 1×*n* 向量，单位为 m。

#### 依赖关系

要启用此参数，请将 **换道类型，changeType** 设置为以下类型之一：

- `Double lane change (ISO 3888-1)`
- `Obstacle avoidance (ISO 3888-2)`

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `latRefbp` |
| **值：** | 1×7 向量（默认） |
| **数据类型：** | `double` |

### **横向参考数据，latRef [m]** — 横向路径参考点 1×7 向量（默认）

与路径纵向断点 **latRefbp** 对应的横向路径参考点，指定为 1×7 向量，单位为 m。

#### 依赖关系

要启用此参数，请将 **换道类型，changeType** 设置为以下类型之一：

- `Double lane change (ISO 3888-1)`
- `Obstacle avoidance (ISO 3888-2)`

#### 依赖关系

要启用此参数，请选择 **使用参考数据**。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `latRef` |
| **值：** | 1×7 向量（默认） |
| **数据类型：** | `double` |

### **使用参考数据** — 使用参考数据的选项 `on`（默认） | `off`

选择此参数以使用参考数据。

#### 依赖关系

要启用此参数，请将 **换道类型，changeType** 设置为以下类型之一：

- `Double lane change (ISO 3888-1)`
- `Obstacle avoidance (ISO 3888-2)`

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `centerSwitch` |
| **值：** | `on`（默认） | `off` |
| **数据类型：** | `character vector` |

### **驶出路线时停止仿真** — 驶出路线时停止仿真的选项 `off`（默认） | `on`

选择此参数以在驶出路线时停止仿真。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `xSimStop` |
| **值：** | `off`（默认） | `on` |
| **数据类型：** | `character vector` |

### **输出信息总线** — 输出信息总线的选项 `off`（默认） | `on`

选择此参数以输出信息总线。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `extInfo` |
| **值：** | `off`（默认） | `on` |
| **数据类型：** | `character vector` |

### **Instantiate 3D cones (Simulation 3D Scene Configuration required)** — 实例化 3D 锥桶的选项 `off`（默认）| `on`

选择此参数以实例化 3D 锥桶。需要 Simulation 3D Scene Configuration 模块。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `use3DCones` |
| **值**：| `off`（默认）| `on` |
| **Data Types:** | `character vector` |

### **Show Maneuver Plot** — 可视化机动按钮的选项

点击 **Show Maneuver Plot** 以可视化由 **Lane change type, changeType** 指定的机动。

## 所属库

Vehicle Dynamics Blockset / Vehicle Scenarios / Drive Cycle and Maneuvers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

要进行 ERT 构建，在将 **System target file** 指定为 `ert.tlc` 后，您必须在 **Simulation Target** 窗格的 **Advanced parameters** 部分中选择 **Dynamic memory allocation in MATLAB functions (Simulink)** 参数。

## 版本历史

**在 R2024b 中引入**

### R2025a：额外的换道类型

从 R2025a 开始，您可以模拟测试机动以评估卡车-挂车避障的性能。要模拟此机动，请将 **Lane change type, changeType** 设置为 `Obstacle avoidance truck-trailer (SAE J2179)`。

## 描述

生成执行换道机动的命令

Lane Change 模块生成执行换道机动的命令，并在车辆达到目标纵向速度后，根据所选机动调整加速度命令。然后，该模块根据纵向位移生成横向参考轨迹。该模块还根据指定的赛道宽度生成指示左车道边界和右车道边界的信号。

使用 **Lane change type, changeType** 参数选择所需的换道类型。

| 操作 | 换道类型设置 |
| --- | --- |
| 模拟双车道变更。该模块保持加速度恒定。 | `Double lane change (ISO 3888-1)` |
| 模拟带避障的换道。该模块命令零加速度。 | `Obstacle avoidance (ISO 3888-2)` |
| 模拟卡车-挂车带避障的换道。该模块不覆盖加速度命令。 | `Obstacle truck-trailer (SAE J2179)` |

您必须将模型中车辆的初始纵向位置设置为距门合理的距离，并指定以下模块参数，以确保车辆在到达门之前达到目标速度：

- **Inertial longitudinal position of gate entrance, XGate [m]**
- **Longitudinal entrance velocity setpoint, velRef**
- **Distance after target speed to begin reference, xStart [m]**

**注意**

有关双车道变更参考应用中使用的参考生成器模块的信息，请参阅 Reference Generator。
