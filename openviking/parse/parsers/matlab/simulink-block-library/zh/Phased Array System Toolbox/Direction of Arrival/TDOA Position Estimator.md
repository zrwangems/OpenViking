---
type: simulink-block
title: 'TDOA Position Estimator'
family: 'direction-of-arrival'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Direction of Arrival'
documentation_page: 'tdoapositionestimator'
documentation_source_path: 'ref/tdoapositionestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# TDOA Position Estimator

## 端口

### 输入

### **TDOAEst** — 估计的到达时间差 (sec) (*L*–1) 元素实值向量

估计信号在锚点对之间相对于第一个锚点和目标的到达时间差，指定为 (*L*–1) 元素实值向量。*L* 是锚点数量。单位为 seconds。

**数据类型：** `single` | `double`

### **TDOAVar** — 估计的到达时间差方差 (seconds-squared) (*L*–1) 元素实值向量

估计信号在锚点对之间相对于第一个锚点和目标的到达时间差方差，指定为 (*L*–1) 元素实值向量。*L* 是锚点数量。单位为 seconds-squared。

**数据类型：** `single` | `double`

### **AnchorPos** — 锚点位置 (meters) 2-by-*L* 实值矩阵 | 3-by-*L* 实值矩阵

锚点位置，指定为 2-by-*L* 实值矩阵或 3-by-*L* 实值矩阵。2-by-*L* 矩阵表示 2-D 笛卡尔空间中的锚点位置，而 3-by-*L* 矩阵表示 3-D 笛卡尔空间中的锚点位置。单位为 meters。

**数据类型：** `single` | `double`

### 输出

### **TgtPosEst** — 目标位置估计 实值 *Q*-by-1 向量

估计的目标位置，以 *Q*-by-1 向量形式返回，表示根据 TDOA 测量值获得的估计目标位置。单位为 meters。

**数据类型：** `single` | `double`

### **TgtPosCov** — 目标位置协方差矩阵 实值半正定 *Q*-by-*Q* 矩阵

目标位置协方差矩阵，以实值半正定 *Q*-by-*Q* 矩阵形式返回。该协方差矩阵表示根据 TOA 位置估计器的 Cramer-Rao 下界 (CRLB) 计算得到的估计目标位置协方差。计算协方差需要知道 `toavar`。当 `toavar` 不准确时，`tgtposcov` 也不准确。当 `toavar` 准确且很小时，`tgtposcov` 值表示 TOA 位置估计 CRLB。单位为 ㎡eters-squared。

#### 依赖项

要启用此输出端口，请选中 **TDOA 位置估计的输出协方差** 复选框。

**数据类型：** `single` | `double`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 的 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### **信号传播速度 (m/s)** — 信号传播速度 `physconst("LightSpeed")`（默认）| 正实数标量

信号传播速度，指定为正实数标量。单位为 meters per second。

**示例：** `3e8`

### **TDOA 位置估计的输出协方差** — 输出 TDOA 位置估计的协方差 `false` (0)（默认）| `true` (1)

选中 **TDOA 位置估计的输出协方差** 复选框以启用包含 TDOA 位置协方差的 **TgtPosCov** 输出端口。

**数据类型：** `Boolean`

### **仿真方式** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间编译，但通常运行更快。

当开发和调整模型时，解释执行很有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真使用生成代码比解释执行运行更快。可以重复执行而无需重新编译，但如果更改任何模块参数，模块会在执行前自动重新编译。

此表显示 **仿真方式** 参数如何影响整体仿真行为。

当 Simulink 模型处于 `Accelerator` 模式时，使用 **仿真方式** 指定的模块模式会覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都会被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`, `Code Generation` |
| **默认：** `Interpreted Execution` |

## 所属库

Phased Array System Toolbox / Direction of Arrival

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**R2024b 中引入**

## 描述

根据到达时间差估计目标位置

根据到达时间差 (TDOA) 测量值和锚点位置估计目标位置。该模块还估计到达时间差测量值的方差。
