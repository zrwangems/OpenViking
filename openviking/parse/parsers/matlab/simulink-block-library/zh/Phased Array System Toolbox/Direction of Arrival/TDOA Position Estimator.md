---
type: simulink-block
title: 'TDOA Position Estimator'
family: 'phased'
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

### **TDOAEst** — 估计的到达时间差（秒），(*L*–1) 元实值向量

信号在锚点对之间相对于第一个锚点与目标的估计到达时间差，指定为 (*L*–1) 元实值向量。*L* 是锚点的数量。单位为秒。

**数据类型：** `single` | `double`

### **TDOAVar** — 估计的到达时间差方差（秒的平方），(*L*–1) 元实值向量

信号在锚点对之间相对于第一个锚点与目标的估计到达时间差方差，指定为 (*L*–1) 元实值向量。*L* 是锚点的数量。单位为秒的平方。

**数据类型：** `single` | `double`

### **AnchorPos** — 锚点位置（米），2×*L* 实值矩阵 | 3×*L* 实值矩阵

锚点位置，指定为 2×*L* 实值矩阵或 3×*L* 实值矩阵。2×*L* 矩阵表示二维笛卡尔空间中的锚点位置，而 3×*L* 矩阵表示三维笛卡尔空间中的锚点位置。单位为米。

**数据类型：** `single` | `double`
### 输出

### **TgtPosEst** — 目标位置估计，实值 *Q*×1 向量

估计的目标位置，返回为 *Q*×1 向量，表示从 TDOA 测量获得的估计目标位置。单位为米。

**数据类型：** `single` | `double`

### **TgtPosCov** — 目标位置协方差矩阵，实值半正定 *Q*×*Q* 矩阵

目标位置协方差矩阵，返回为实值半正定 *Q*×*Q* 矩阵。协方差矩阵表示从 TOA 位置估计器的 Cramer-Rao 下界（CRLB）计算得到的估计目标位置协方差。计算协方差需要已知 `toavar`。当 `toavar` 不准确时，`tgtposcov` 也不准确。当 `toavar` 准确且较小时，`tgtposcov` 值表示 TOA 位置估计的 CRLB。单位为平方米。

#### 依赖关系

要启用此输出端口，请选中 **Output covariance of TDOA position estimate** 复选框。

**数据类型：** `single` | `double`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡中，在 **Prepare** 库中选择 **Property Inspector**。

### **Signal propagation speed (m/s)** — 信号传播速度 `physconst("LightSpeed")`（默认）| 正实标量

信号传播速度，指定为正实标量。单位为米每秒。

**示例：** `3e8`

### **Output covariances of TDOA position estimates** — 输出 TDOA 位置估计的协方差 `false` (0)（默认）| `true` (1)

选中 **Output covariances of TDOA position estimates** 复选框以启用包含 TDOA 位置协方差的 **TgtPosCov** 输出端口。

**数据类型：** `Boolean`

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

当您开发和调整模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意时，可以使用 `Code Generation` 运行模块。长时间仿真使用生成代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果更改任何模块参数，模块将在执行前自动重新编译。

下表显示了 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`SimulateUsing` |
| **类型**：enum |
| **值**：`Interpreted Execution`, `Code Generation` |
| **默认值**：`Interpreted Execution` |

## 所属库

Phased Array System Toolbox / Direction of Arrival

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024b 中引入**

## 描述

根据到达时间差估计目标位置

根据到达时间差（TDOA）测量值和锚点位置估计目标位置。该模块还估计到达时间差测量值的方差。
