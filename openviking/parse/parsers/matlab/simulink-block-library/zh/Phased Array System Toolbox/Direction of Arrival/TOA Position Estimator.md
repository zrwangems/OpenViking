---
type: simulink-block
title: 'TOA Position Estimator'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Direction of Arrival'
documentation_page: 'toapositionestimator'
documentation_source_path: 'ref/toapositionestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# TOA Position Estimator

## 端口
```yaml
ports:
- name: TOAest
  summary: 估计到达时间 1×*L* 实值向量
  direction: input
  data_types: single | double
- name: TOAVar
  summary: 估计到达时间的方差 1×*L* 实值向量
  direction: input
  data_types: single | double
- name: AnchorPos
  summary: 锚点位置 2×*L* 实值矩阵 | 3×*L* 实值矩阵
  direction: input
  data_types: single | double
- name: TgtPosEst
  summary: 估计目标位置 实值 *Q*×1 向量
  direction: output
- name: TgtPosCov
  summary: 目标位置协方差矩阵 实值半正定 *Q*×*Q* 矩阵
  direction: output
  data_types: single | double
```

### 输入

### **TOAest** — 估计到达时间 1×*L* 实值向量

锚点与单个目标之间信号的估计到达时间，指定为 1×*L* 实值向量。单位为秒。

**数据类型：** `single` | `double`

### **TOAVar** — 估计到达时间的方差 1×*L* 实值向量

锚点处估计到达时间的方差，指定为 1×*L* 实值向量。

当 `toavar` 未知时，可以将其设置为具有相同有限值的 1×*L* 向量，而不影响解 `tgtposest`。

**数据类型：** `single` | `double`

### **AnchorPos** — 锚点位置 2×*L* 实值矩阵 | 3×*L* 实值矩阵

锚点位置，指定为 2×*L* 实值矩阵或 3×*L* 实值矩阵。2×*L* 矩阵表示 2-D 笛卡尔空间中的锚点位置，而 3×*L* 矩阵表示 3-D 笛卡尔空间中的锚点位置。

**数据类型：** `single` | `double`
### 输出

### **TgtPosEst** — 估计目标位置 实值 *Q*×1 向量

估计目标位置，返回为 *Q*×1 向量，表示从 TOA 和 TDOA 测量获得的估计目标位置。单位为米。

### **TgtPosCov** — 目标位置协方差矩阵 实值半正定 *Q*×*Q* 矩阵

目标位置协方差矩阵，返回为实值半正定 *Q*×*Q* 矩阵。协方差矩阵表示根据 TOA 位置估计器的 Cramer-Rao 下界（CRLB）计算的估计目标位置协方差。计算协方差需要 `toavar` 的知识。当 `toavar` 不准确时，`tgtposcov` 也不准确。当 `toavar` 准确且较小时，`tgtposcov` 值表示 TOA 位置估计 CRLB。单位为 ㎡eters-squared。

#### 依赖

要启用此输出端口，请选中 **Output covariance of TOA position estimate** 复选框。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Signal propagation speed (m/s)
  summary: 信号传播速度 physconst("LightSpeed")（默认）| 正实标量
  group: ''
- name: Output covariance of TOA position estimate
  summary: 输出 TDOA 位置估计的协方差 false (0)（默认）| true (1)
  group: ''
- name: Simulate using
  summary: 模块仿真方法 Interpreted Execution（默认）| Code Generation
  group: ''
  block_parameter: SimulateUsing
  type: enum
  values: Interpreted Execution、Code Generation
```

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 中，在 **Simulation** 选项卡的 **Prepare** 库中，选择 **Property Inspector**。

### **Signal propagation speed (m/s)** — 信号传播速度 `physconst("LightSpeed")`（默认）| 正实标量

信号传播速度，指定为正实标量。单位为米每秒。

**示例：** `3e8`

**数据类型：** `single` | `double`

### **Output covariance of TOA position estimate** — 输出 TDOA 位置估计的协方差 `false` (0)（默认）| `true` (1)

选中 **Output covariance of TOA position estimates** 复选框以启用包含 TOA 位置协方差的 **TgtPosCov** 输出端口。

**数据类型：** `Boolean`

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或
`Code Generation`。如果您希望模块使用
MATLAB® 解释器，请选择 `Interpreted Execution`。如果您
希望模块作为编译代码运行，请选择 `Code
Generation`。编译代码需要时间进行编译，但通常运行
更快。

当您在开发和调整模型时，解释执行非常有用。模块
在 MATLAB 中运行底层 System object™。您可以快速更改和执行您的模型。当您对
结果满意时，可以使用 `Code
Generation` 运行模块。长时间仿真使用生成代码比在
解释执行中运行更快。您可以重复执行而无需重新编译，但如果您
更改任何模块参数，则模块会在执行前自动重新编译。

此表显示了 **Simulate using** 参数如何影响
整体仿真行为。

当 Simulink 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式
会覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`、`Code Generation` |
| **默认：** `Interpreted Execution` |
## 所属库

Phased Array System Toolbox / Direction of Arrival

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024b 中引入**

## 描述

根据到达时间估计和锚点位置估计目标位置

根据到达时间估计和锚点位置估计目标位置
