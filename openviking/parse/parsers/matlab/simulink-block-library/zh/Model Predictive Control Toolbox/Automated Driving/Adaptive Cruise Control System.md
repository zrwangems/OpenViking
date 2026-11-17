---
type: simulink-block
title: 'Adaptive Cruise Control System'
family: 'mpc'
product_id: 'mpc'
product_name: 'Model Predictive Control Toolbox'
documentation_release: R2025b
official_category: 'Automated Driving'
documentation_page: 'adaptivecruisecontrolsystem'
documentation_source_path: 'ref/adaptivecruisecontrolsystem.html'
language: zh-CN
chinese_source: worker-translation
---

# Adaptive Cruise Control System

## 端口

### 输入

### **Set velocity** — 自车速度设定值，非负标量

自车速度设定值，单位为 m/s。当没有前车时，控制器跟踪该速度。

### **Time gap** — 安全时间间隔，非负标量

前车与自车之间的安全时间间隔，单位为秒。该时间间隔用于计算最小安全跟车距离约束。有关详细信息，请参阅 Safe Following Distance。

### **Longitudinal velocity** — 自车速度，非负标量

自车速度，单位为 m/s。

### **Relative distance** — 前车与自车之间的距离，正标量

前车与自车之间的距离，单位为米。要计算该信号，请从自车位置中减去前车位置。

### **Relative velocity** — 前车与自车之间的速度差，标量

前车与自车之间的速度差，单位为米每秒。要计算该信号，请从自车速度中减去前车速度。

### **Minimum longitudinal acceleration** — 自车最小加速度，负标量

自车纵向加速度最小约束，单位为 m/s2。当最小加速度在运行时变化时，使用该输入端口。

#### 依赖关系

要启用该端口，请为 **Minimum longitudinal acceleration** 参数选择 **Use external source**。

### **Maximum longitudinal acceleration** — 自车最大加速度，正标量

自车纵向加速度最大约束，单位为 m/s2。当最大加速度在运行时变化时，使用该输入端口。

#### 依赖关系

要启用该端口，请为 **Maximum longitudinal acceleration** 参数选择 **Use external source**。

### **Enable optimization** — 控制器优化启用信号，标量

控制器优化启用信号。当该信号为：

- 非零时，控制器执行优化计算并生成 **Longitudinal acceleration** 控制信号。
- 零时，控制器不执行优化计算。在这种情况下，**Longitudinal acceleration** 输出信号保持其在优化被禁用时的值。控制器继续更新其内部状态估计。

#### 依赖关系

要启用该端口，请选择 **Use external signal to enable or disable optimization** 参数。

### **External control signal** — 施加到自车的纵向加速度，标量

施加到自车的实际纵向加速度，单位为 m/s2。控制器使用该信号来估计自车模型状态。当施加到自车的控制信号与模型预测控制器计算出的最优控制信号不匹配时，使用该输入端口。这种不匹配可能发生在以下情况，例如：

- Adaptive Cruise Control System 不是活动控制器。当控制器未激活时保持准确的状态估计，可防止控制器变为激活时控制信号出现突变。
- 加速度执行器发生故障，无法向自车提供正确的控制信号。

#### 依赖关系

要启用该端口，请选择 **Use external control signal for bumpless transfer between ACC and other controllers** 参数。
### 输出

### **Longitudinal acceleration** — 加速度控制信号，标量

由控制器生成的加速度控制信号，单位为 m/s2。

## 参数

### 参数选项卡

#### 自车模型

### **Linear model from longitudinal acceleration to longitudinal velocity** — 自车模型 `tf(1,[0.5,1,0])`（默认）| LTI 模型 | 线性 System Identification Toolbox™ 模型

从自车纵向加速度到其纵向速度的线性模型，指定为 LTI 模型或线性 System Identification Toolbox 模型。控制器通过增广自车动力学模型来创建其内部预测模型。

#### 编程使用

|  |
| --- |
| **模块参数：** `EgoModel` |
| **类型：** string, character vector |
| **默认值：** `"tf(1,[0.5,1,0])"` |

### **Initial condition for longitudinal velocity** — 自车模型的初始速度 `20`（默认）| 非负标量

自车模型的初始速度，单位为 m/s，可以与实际自车初始速度不同。

此值用于配置模型预测控制器的初始条件。有关详细信息，请参阅 Initial Conditions。

#### 编程使用

|  |
| --- |
| **模块参数：** `InitialEgoVelocity` |
| **类型：** string, character vector |
| **默认值：** `"20"` |

### **Default spacing** — 与前方车辆的最小间距 `10`（默认）| 非负标量

前方车辆与自车之间的最小间距，单位为米。此值对应于自车速度为零时自车与前方车辆之间的目标相对距离。

此值用于计算：

- 最小安全跟车距离。有关详细信息，请参阅 Safe Following Distance。
- 控制器初始条件。有关详细信息，请参阅 Initial Conditions。

#### 编程使用

|  |
| --- |
| **模块参数：** `DefaultSpacing` |
| **类型：** string, character vector |
| **默认值：** `"10"` |

### **Maximum velocity** — 最大纵向速度 `50`（默认）| 正标量

自车最大纵向速度，单位为 m/s。

#### 编程使用

|  |
| --- |
| **模块参数：** `MaxVelocity` |
| **类型：** string, character vector |
| **默认值：** `"50"` |

#### Adaptive Cruise Controller Constraints

### **Minimum longitudinal acceleration** — 自车最小加速度 `-3`（默认）| 负标量

自车纵向加速度约束最小值，单位为 m/s2。

如果最小加速度随时间变化，请通过选择 **Use external source** 将 **Minimum longitudinal acceleration** 输入端口添加到模块。

#### 编程使用

|  |
| --- |
| **模块参数：** `MinAcceleration` |
| **类型：** string, character vector |
| **默认值：** `"-3"` |

### **Maximum longitudinal acceleration** — 自车最大加速度 `2`（默认）| 非负标量

自车纵向加速度约束最大值，单位为 m/s2。

如果最大加速度随时间变化，请通过选择 **Use external source** 将 **Maximum longitudinal acceleration** 输入端口添加到模块。

#### 编程使用

|  |
| --- |
| **模块参数：** `MaxAcceleration` |
| **类型：** string, character vector |
| **默认值：** `"2"` |

#### Model Predictive Controller Settings

### **Sample time** — 控制器采样时间 `0.1`（默认）| 正标量

控制器采样时间，单位为秒。

#### 编程使用

|  |
| --- |
| **模块参数：** `Ts` |
| **类型：** string, character vector |
| **默认值：** `"0.1"` |

### **Prediction horizon** — 控制器预测时域 `10`（默认）| 正整数

控制器预测时域步数。控制器预测时间为采样时间与预测时域的乘积。

#### 编程使用

|  |
| --- |
| **模块参数：** `PredictionHorizon` |
| **类型：** string, character vector |
| **默认值：** `"30"` |

### **控制器行为** — 闭环控制器性能 `0.5`（默认）| `0` 到 `1` 之间的标量

闭环控制器性能。默认参数值提供平衡的控制器设计。指定：

- 较小的值会产生更鲁棒的控制器，控制动作更平滑。
- 较大的值会产生更激进的控制器，响应时间更快。

当您修改此参数时，更改会立即应用于控制器。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ControllerBehavior` |
| **类型：** string, character vector |
| **默认：** `"0.5"` |

### 模块选项卡

### **使用次优解** — 在指定迭代次数后应用次优解 `off`（默认）| `on`

将控制器配置为在指定的最大迭代次数后应用次优解，这保证了控制器的最坏情况执行时间。

有关详细信息，请参阅次优 QP 解。

#### 依赖关系

选择此参数后，请指定 **最大迭代次数** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `suboptimal` |
| **类型：** string, character vector |
| **默认：** `"off"` |

### **最大迭代次数** — 最大优化迭代次数 `10`（默认）| 正整数

控制器优化迭代的最大次数。

#### 依赖关系

要启用此参数，请选择 **使用次优解** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `maxiter` |
| **类型：** string, character vector |
| **默认：** `"10"` |

### **使用外部信号启用或禁用优化** — 添加用于启用优化的端口 `off`（默认）| `on`

要向模块添加 **启用优化** 输入端口，请选择此参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `optmode` |
| **类型：** string, character vector |
| **默认：** `"off"` |

### **使用外部信号在 ACC 和其他控制器之间进行无扰切换** — 添加外部控制信号输入端口 `off`（默认）| `on`

选择此参数以向模块添加 **外部控制信号** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数：** `trackmode` |
| **类型：** string, character vector |
| **默认：** `"off"` |

### **创建 ACC 子系统** — 创建自定义控制器按钮

生成自定义 ACC 子系统，您可以根据自己的应用进行修改。自定义控制器的配置数据将作为结构体导出到 MATLAB® 工作区。

您可以修改自定义控制器子系统以：

- 修改默认 MPC 设置或使用高级 MPC 功能。
- 修改默认控制器初始条件。
- 使用不同的应用设置，例如自定义安全跟车距离定义。

## 所属库

Model Predictive Control Toolbox / Automated Driving

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

使用模型预测控制器模拟自适应巡航控制

自适应巡航控制系统模块模拟自适应巡航控制（ACC）系统，该系统通过调整自车的纵向加速度来跟踪设定速度并与前车保持安全距离。该模块使用模型预测控制（MPC）在满足安全距离、速度和加速度约束的同时计算最优控制动作。

要自定义控制器，例如使用高级 MPC 功能或修改控制器初始条件，请点击 **创建 ACC 子系统**。
