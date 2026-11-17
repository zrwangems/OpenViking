---
type: simulink-block
title: 'Lane Keeping Assist System'
family: 'mpc'
product_id: 'mpc'
product_name: 'Model Predictive Control Toolbox'
documentation_release: R2025b
official_category: 'Automated Driving'
documentation_page: 'lanekeepingassistsystem'
documentation_source_path: 'ref/lanekeepingassistsystem.html'
language: zh-CN
chinese_source: worker-translation
---

# Lane Keeping Assist System

## 端口

### 输入

### **Curvature** — 道路曲率 标量 | 向量

道路曲率，指定为 1/*R*，其中 *R* 是曲线的半径，单位为米。

道路曲率为：

- 当道路向全局坐标系的正 Y 轴方向弯曲时为正。
- 当道路向全局坐标系的负 Y 轴方向弯曲时为负。
- 对于直道为零。

控制器将道路曲率建模为带预览的测量扰动。您可以将曲率指定为：

- 标量信号 — 指定当前控制区间的曲率。控制器在整个预测时域内使用该曲率值。
- 长度小于或等于 **Prediction Horizon** 参数的向量信号 — 指定整个预测时域内的当前和预测曲率值。如果向量的长度小于预测时域，则控制器在预测时域的剩余部分使用向量中的最终曲率值。

### **Longitudinal velocity** — 自车速度 非负标量

自车速度，单位为 m/s。

### **Lateral deviation** — 自车横向偏差 标量

自车相对于车道中心线的横向偏差，单位为米。当自车位于中心线右侧时，横向偏差 *e*1 为正；当自车位于中心线左侧时为负。

### **Relative yaw angle** — 相对于车道中心线的角度 标量

自车纵轴相对于车道中心线的角度，单位为弧度，定义为：

e2=θe−θc

其中，*θe* 是自车角度，*θc* 是中心线角度，两个角度均在全局坐标系中定义。

### **Minimum steering angle** — 最小前轮转向角 标量

最小前轮转向角约束，单位为弧度。当最小转向角在运行时变化时，使用此输入端口。

#### 依赖

要启用此端口，请选择相应的 **Use external source** 参数。

### **Maximum steering angle** — 最大前轮转向角 标量

最大前轮转向角约束，单位为弧度。当最大转向角在运行时变化时，使用此输入端口。

#### 依赖

要启用此端口，请选择相应的 **Use external source** 参数。

### **Enable optimization** — 控制器优化使能信号 标量

控制器优化使能信号。当此信号为：

- 非零时，控制器执行优化计算并生成 **Steering angle** 控制信号。
- 零时，控制器不执行优化计算。在这种情况下，**Steering angle** 输出信号保持优化禁用时的值。控制器继续更新其内部状态估计。

#### 依赖

要启用此端口，请选择 **Use external signal to enable or disable optimization** 参数。

### **External control signal** — 施加到自车的转向角 标量

施加到自车的实际转向角，单位为弧度。控制器使用此信号估计自车模型状态。当施加到自车的控制信号与模型预测控制器计算的最优控制信号不匹配时，使用此输入端口。这种不匹配可能在以下情况下发生，例如：

- Lane Keeping Assist System 不是活动控制器。当控制器不活动时保持准确的状态估计，可防止控制器变为活动时控制信号出现突变。
- 转向执行器发生故障，无法向自车提供正确的控制信号。

#### 依赖

要启用此端口，请选择 **Use external control signal for bumpless transfer between PFC and other controllers** 参数。

### **Vehicle dynamics matrix A** — 自车预测模型的状态矩阵 方阵

自车预测模型的状态矩阵。状态矩阵的行数对应于预测模型中的状态数。该矩阵必须是方阵。

由 **Vehicle dynamics matrix A**、**Vehicle dynamics matrix B** 和 **Vehicle dynamics matrix C** 定义的自车预测模型必须是最小实现。

#### 依赖关系

要启用此端口，请选择 **Use vehicle model** 参数。

### **Vehicle dynamics matrix B** — 自车预测模型的输入到状态矩阵 列向量

自车预测模型的输入到状态矩阵。此信号的行数必须与 **Vehicle dynamics matrix A** 的行数匹配。

由 **Vehicle dynamics matrix A**、**Vehicle dynamics matrix B** 和 **Vehicle dynamics matrix C** 定义的自车预测模型必须是最小实现。

#### 依赖关系

要启用此端口，请选择 **Use vehicle model** 参数。

### **Vehicle dynamics matrix C** — 自车预测模型的状态到输出矩阵 具有两行的矩阵

自车预测模型的状态到输出矩阵。此信号的列数必须与 **Vehicle dynamics matrix A** 的行数匹配。

由 **Vehicle dynamics matrix A**、**Vehicle dynamics matrix B** 和 **Vehicle dynamics matrix C** 定义的自车预测模型必须是最小实现。

#### 依赖关系

要启用此端口，请选择 **Use vehicle model** 参数。
### 输出

### **Steering angle** — 前轮转向角控制信号 标量

由控制器生成的前轮转向角控制信号，单位为弧度。前轮转向角是前轮相对于车辆纵轴的角度。转向角朝向自车横轴正方向时为正。

## 参数

### 参数选项卡

#### 自车

### **Use vehicle parameters** — 使用车辆属性定义自车模型 `on`（默认）| `off`

选择此参数可通过指定自车的属性来定义 MPC 控制器使用的自车模型。自车模型是从前轮转向角到横向速度和横摆角速度的线性模型。有关详细信息，请参阅 Ego Vehicle Predictive Model。

要定义车辆模型，请指定以下模块参数：

- **Total mass**
- **Yaw moment of inertia**
- **Longitudinal distance from center of gravity to front tires**
- **Longitudinal distance from center of gravity to rear tires**
- **Cornering stiffness of front tires**
- **Cornering stiffness of rear tires**

有关自车模型的详细信息，请参阅 Ego Vehicle Predictive Model。

选择此参数将清除 **Use vehicle model** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`ModelType` |
| **类型**：string, character vector |
| **默认值**：`"Use vehicle parameters"` |

### **Use vehicle model** — 使用状态空间矩阵定义自车模型 `off`（默认）| `on`

选择此参数可定义 MPC 控制器使用的自车模型的状态空间矩阵。该模型是从前轮转向角（单位为弧度）到横向速度（单位为米每秒）和横摆角速度（单位为弧度每秒）的线性模型。有关自车模型的详细信息，请参阅 Ego Vehicle Predictive Model。

要定义初始内部模型，请指定 **A**、**B** 和 **C** 状态空间矩阵。内部模型必须是无直接馈通的最小实现，并且 **A**、**B** 和 **C** 的维度必须一致。

通常，自车转向模型依赖于速度，因此会随时间变化。要在运行时更新内部模型，请使用 **Vehicle dynamics A**、**Vehicle dynamics B** 和 **Vehicle dynamics C** 输入端口。

选择此参数将清除 **Use vehicle parameters** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ModelType` |
| **类型：** string, character vector |
| **默认值：** `"Use vehicle parameters"` |

### **Total mass** — 自车质量 `1575`（默认）| 正标量

自车质量，单位为 kg。

#### 依赖关系

要启用此参数，请选择 **Use vehicle parameters** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `VehicleMass` |
| **类型：** string, character vector |
| **默认值：** `"1575"` |

### **Yaw moment of inertia** — 绕自车垂直轴的转动惯量 `2875`（默认）| 正标量

绕自车垂直轴的转动惯量，单位为
Kg·m2。

#### 依赖关系

要启用此参数，请选择 **Use vehicle parameters** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `VehicleYawInertia` |
| **类型：** string, character vector |
| **默认值：** `"2875"` |

### **Longitudinal distance from center of gravity to front tires** — 自车质心到前轮的距离 `1.2`（默认）| 正标量

自车质心到前轮的距离，单位为米，沿车辆纵轴测量。

#### 依赖关系

要启用此参数，请选择 **Use vehicle parameters** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LengthToFront` |
| **类型：** string, character vector |
| **默认值：** `"1.2"` |

### **Longitudinal distance from center of gravity to rear tires** — 自车质心到后轮的距离 `1.6`（默认）| 正标量

自车质心到后轮的距离，单位为米，沿车辆纵轴测量。

#### 依赖关系

要启用此参数，请选择 **Use vehicle parameters** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LengthToRear` |
| **类型：** string, character vector |
| **默认值：** `"1.6"` |

### **Cornering stiffness of front tires** — 前轮侧偏刚度 `19000`（默认）| 正标量

前轮侧偏刚度，单位为 N/rad，定义为前轮侧向力与前轮相对于车辆纵轴角度之间的关系。

#### 依赖关系

要启用此参数，请选择 **Use vehicle parameters** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FrontTireStiffness` |
| **类型：** string, character vector |
| **默认值：** `"19000"` |

### **Cornering stiffness of rear tires** — 后轮侧偏刚度 `33000`（默认）| 正标量

后轮侧偏刚度，单位为 N/rad，定义为后轮侧向力与后轮相对于车辆纵轴角度之间的关系。

#### 依赖关系

要启用此参数，请选择 **Use vehicle parameters** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `RearTireStiffness` |
| **类型：** string, character vector |
| **默认值：** `"33000"` |

### **A** — 自车预测模型的初始状态矩阵 方阵

自车预测模型的初始状态矩阵。状态矩阵中的行数
对应于预测模型中的状态数。此矩阵必须为
方阵。

由 **A**、**B** 和 **C** 定义的初始自车预测模型必须是最小实现。

通常，自车模型随时间变化。要在运行时更新状态矩阵，请使用 **Vehicle dynamics A** 输入端口。

#### 依赖关系

要启用此参数，请选择 **Use vehicle model** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `EgoModelMatrixA` |
| **类型：** string, character vector |
| **默认值：** `"[-4.4021 ,-12.4603;1.3913,-5.1868]"` |

### **B** — 自车预测模型的初始输入到状态矩阵 列向量

自车预测模型的初始输入到状态矩阵。此参数的行数必须与 **A** 的行数一致。

由 **A**、**B** 和 **C** 定义的初始自车预测模型必须是最小实现。

通常，自车模型随时间变化。要在运行时更新输入到状态矩阵，请使用 **Vehicle dynamics B** 输入端口。

#### 依赖关系

要启用此参数，请选择 **Use vehicle model** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `EgoModelMatrixB` |
| **类型：** string, character vector |
| **默认值：** `"[24.1270;15.8609]"` |

### **C** — 自车预测模型的初始状态到输出矩阵 具有两行的矩阵

自车预测模型的初始状态到输出矩阵。此参数的列数必须与 **A** 的行数一致。

由 **A**、**B** 和 **C** 定义的初始自车预测模型必须是最小实现。

通常，自车模型随时间变化。要在运行时更新状态到输出矩阵，请使用 **Vehicle dynamics C** 输入端口。

#### 依赖关系

要启用此参数，请选择 **Use vehicle model** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `EgoModelMatrixC` |
| **类型：** string, character vector |
| **默认值：** `"[1,0;0,1]"` |

### **Initial longitudinal velocity** — 自车的初始速度 `15`（默认值） | 正标量

当车道保持辅助启用时，自车模型的初始速度，单位为 m/s。此速度可以不同于实际自车的初始速度。

**注意**

非常小的初始速度，例如 `eps`，可能会为控制器被控对象模型产生非最小实现，从而导致错误。要防止此错误，请将初始速度设置为较大的值，例如 `1e-3`。

#### 编程用法

|  |
| --- |
| **模块参数：** `InitialLongVel` |
| **类型：** string, character vector |
| **默认值：** `"15"` |

### **Transport lag between model inputs and outputs** — 自车模型中的总传输延迟 `0`（默认值） | 非负标量

自车模型中的总传输延迟 *τ*，单位为秒。此延迟包括执行器、传感器和通信延迟。对于每个输入-输出通道，传输延迟近似为：

1τs+1

#### 编程用法

|  |
| --- |
| **模块参数：** `TransportLag` |
| **类型：** string, character vector |
| **默认值：** `"0"` |

#### 车道保持控制器约束

### **Minimum steering angle** — 最小前轮转向角 `-0.26`（默认值） | `-pi/2` 和 `pi/2` 之间的标量

最小前轮转向角约束，单位为弧度。

如果最小转向角随时间变化，请通过选择 **Use external source** 将 **Minimum steering angle** 输入端口添加到模块。

#### 依赖关系

此参数必须小于 **Maximum steering angle** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `MinSteering` |
| **类型：** string, character vector |
| **默认值：** `"-0.26"` |

### **Maximum steering angle** — 最大前轮转向角 `0.26`（默认值） | `-pi/2` 和 `pi/2` 之间的标量

最大前轮转向角约束，单位为弧度。

如果最大转向角随时间变化，请通过选择 **Use external source** 将 **Maximum steering angle** 输入端口添加到模块。

#### 依赖关系

此参数必须大于 **Minimum steering angle** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `MaxSteering` |
| **类型：** string, character vector |
| **默认值：** `"0.26"` |

#### 模型预测控制器设置

### **Sample time** — 控制器采样时间 `0.1`（默认值） | 正标量

控制器采样时间，单位为秒。

#### 编程用法

|  |
| --- |
| **模块参数：** `Ts` |
| **类型：** string, character vector |
| **默认值：** `"0.1"` |

### **Prediction horizon** — 控制器预测时域 `10`（默认）| 正整数

控制器预测时域步数。控制器预测时间是采样时间与预测时域的乘积。

#### 编程使用

|  |
| --- |
| **模块参数**：`PredictionHorizon` |
| **类型**：string, character vector |
| **默认值**：`"30"` |

### **Controller behavior** — 闭环控制器性能 `0.5`（默认）| `0` 到 `1` 之间的标量

闭环控制器性能。默认参数值提供平衡的控制器设计。指定：

- 较小的值会产生更鲁棒的控制器，控制动作更平滑。
- 较大的值会产生更激进的控制器，响应时间更快。

修改此参数时，更改会立即应用于控制器。

#### 编程使用

|  |
| --- |
| **模块参数**：`ControllerBehavior` |
| **类型**：string, character vector |
| **默认值**：`"0.5"` |

### Block Tab

### **Use suboptimal solution** — 在指定迭代次数后应用次优解 `off`（默认）| `on`

将控制器配置为在指定的最大迭代次数后应用次优解，这可以保证控制器的最坏情况执行时间。

有关详细信息，请参阅 Suboptimal QP Solution。

#### 依赖关系

选择此参数后，请指定 **Maximum iteration number** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`suboptimal` |
| **类型**：string, character vector |
| **默认值**：`"off"` |

### **Maximum iteration number** — 最大优化迭代次数 `10`（默认）| 正整数

控制器优化迭代的最大次数。

#### 依赖关系

要启用此参数，请选择 **Use suboptimal solution** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`maxiter` |
| **类型**：string, character vector |
| **默认值**：`"10"` |

### **Use external signal to enable or disable optimization** — 添加用于启用优化的端口 `off`（默认）| `on`

要将 **Enable optimization** 输入端口添加到模块，请选择此参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`optmode` |
| **类型**：string, character vector |
| **默认值**：`"off"` |

### **Use external signal for bumpless transfer between LKA and other controllers** — 添加外部控制信号输入端口 `off`（默认）| `on`

要将 **External control signal** 输入端口添加到模块，请选择此参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`trackmode` |
| **类型**：string, character vector |
| **默认值**：`"off"` |

### **Create LKA subsystem** — 创建自定义控制器按钮

生成自定义 LKA 子系统，您可以针对自己的应用进行修改。自定义控制器的控制器配置数据将作为结构体导出到 MATLAB® 工作区。

您可以修改自定义控制器子系统以：

- 修改默认 MPC 设置或使用高级 MPC 功能。
- 修改默认控制器初始条件。

## 所属库

Model Predictive Control Toolbox / Automated Driving

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

## 版本历史

**在 R2018a 中引入**

## 描述

使用自适应模型预测控制器模拟车道保持辅助

Lane Keeping Assist System 模块模拟车道保持辅助（LKA）系统，该系统通过调整前轮转向角，使自车沿直线或弯曲道路的中心行驶。控制器减小自车相对于车道中心线的横向偏差和相对偏航角。该模块使用自适应模型预测控制（MPC）计算最优控制动作，同时满足转向角约束。

要自定义控制器，例如使用高级 MPC 功能或修改控制器初始条件，请点击 **Create LKA subsystem**。
