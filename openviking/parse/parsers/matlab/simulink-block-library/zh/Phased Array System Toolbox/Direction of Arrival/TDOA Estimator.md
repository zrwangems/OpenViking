---
type: simulink-block
title: 'TDOA Estimator'
family: 'direction-of-arrival'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Direction of Arrival'
documentation_page: 'tdoaestimator'
documentation_source_path: 'ref/tdoaestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# TDOA Estimator

## 端口

### 输入

### **X** — 输入数据 *N*-by-*M*-by-*L* complex-valued 数组

接收信号矩阵，指定为 *N*-by-*M*-by-*L* complex-valued 数组。*L* 表示锚点数量。每个页面表示一个锚点的 *N*-by-*M* complex-valued 矩阵。第一页对应参考锚点。每个信号矩阵的行表示 *M* 个独立脉冲（例如雷达的慢时间样本），每列表示一个脉冲的 *N* 个快时间样本。

**数据类型：** `single` | `double`
**复数支持：** Yes

### **DelayOffset** — 延迟偏移 (sec) 标量 | 1-by-*L* 实值向量

延迟偏移，指定为标量或 1-by-*L* 实值向量，其中 *L* 是锚点数量。TDOA 估计结果 `Y` 由 `delayoffset` 调整。该偏移是每个锚点处的时钟与第一个锚点的参考时钟之间的已知延迟偏移。如果 `DelayOffset` 是标量，则所有 *L* 个锚点的延迟偏移相同。如果 `DelayOffset` 是 1-by-*L* 向量，则不同锚点的延迟偏移可以不同。单位为 seconds。

#### 依赖项

要启用 **DelayOffset** 输入端口，请选中 **Enable known delay offset input** 复选框。

**数据类型：** `single` | `double`

### **Npow** — 输入噪声功率 (W) 正标量 | 1-by-*L* 正值向量

输入噪声功率，指定为正标量或具有正值的 1-by-*L* 向量。`Npow` 表示每个锚点处的白高斯噪声功率。如果 `Npow` 是标量，则所有 *L* 个锚点的噪声功率相同。如果 `Npow` 是 1-by-*L* 向量，则相同的噪声功率值应用于 *L* 个锚点中的每一个。单位为 Watts。

此参数允许您使用输入参数 `Npow` 计算可选输出参数 `var`，

**示例：** `50`

#### 依赖项

要启用此参数，请将 **Source of noise power** 参数设置为 `'Input port'`。

**数据类型：** `single` | `double`

### 输出

### **Y** — TDOA 估计 (sec) *K*-by-(*L*-1) 实值矩阵

TDOA 估计，返回为 *K*-by-(*L*–1) 实值矩阵。*K* 是由 `NumEstimates` 属性指定的最大目标数。*L* 是产生 (*L*–1) 个锚点对的锚点数量。`Y` 的第 `l` 列表示第 `l` 个锚点对的 TDOA 估计，即第 (`l+1`) 个锚点与第一个锚点之间的时间差。

锚点对的 TDOA 通过从 GCC-PHAT TDOA 频谱中检测最多 *K* 个峰值的位置来估计。如果第 `l` 个锚点对检测到的峰值数量小于 *K*，则 `Y` 的第 `l` 列的前几个条目包含有效 TDOA 估计，而 `Y` 的第 `l` 列中剩余条目用 `NaN` 填充。单位为 seconds。

**数据类型：** `single` | `double`

### **Var** — 估计的 TDOA 方差 1-by-(*L*-1) 正值向量

估计的 TDOA 方差，返回为 1-by-(*L*-1) 正值向量。`var` 是从基于输入 `X` 和白高斯噪声功率估计 TDOA 的 Cramer-Rao 下界 (CRLB) 获得的，假设有 *K* 个目标均匀分配接收信号功率。噪声功率可通过 `NoisePower` 属性或使用 `npow` 输入参数指定。单位为 seconds-squared。

#### 依赖项

要启用此端口，请选中 **Output variance of TDOA estimates** 复选框。

**数据类型：** `single` | `double`

### **TDOAResp** — TDOA 响应 *P*-by-*M*-by-(*L*-1) MATLAB® 数组

TDOA 响应，输出为 *P*-by-*M*-by-(*L*-1) MATLAB 数组，其中 *P* 是 TDOA 网格样本数，*L* 是锚点数量，*M* 是独立脉冲数。

#### 依赖项

要启用此端口，请选中 **Output TDOA response and TDOA grid** 复选框。

**数据类型：** `single` | `double`

### **TDOAGrid** — TDOA 网格 实值 *P*-by-(*L*-1) 矩阵

到达时间差网格，返回为实值 *P*-by-(*L*-1) 矩阵，其中 *P* 是 TDOA 网格样本数，*L* 是锚点数量。

#### 依赖项

要启用此端口，请选中 **Output TDOA response and TDOA grid** 复选框。

**数据类型：** `single` | `double`

## 参数

要交互式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 中，在 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### **Inherit sample rate** — 从上游模块继承采样率 on (默认) | off

选择此参数以从上游模块继承采样率。否则，使用 **Sample rate (Hz)** 参数指定采样率。

**数据类型：** `Boolean`

### **Signal sample rate (Hz)** — 信号采样率 `1000000` (默认) | 实值正标量

信号采样率，指定为实值正标量。

#### 依赖项

要启用此参数，请取消选中 **Inherit sample rate** 复选框。

**数据类型：** `Boolean`

### **Maximum number of TDOA estimates** — 最大 TDOA 估计数 `1` (默认) | 正整数

最大 TDOA 估计数，指定为正整数。

**示例：** `100`

**数据类型：** `single` | `double`

### **Enable known delay offset input** — 启用已知延迟偏移输入 `false` (0) (默认) | `true` (1)

选中 **Enable known delay offset input** 复选框以启用 **DelayOffset** 输入端口。

**数据类型：** `Boolean`

### **Output variance of TDOA Estimates** — 输出 TDOA 估计方差 `false` (0) (默认) | `true` (1)

选中 **Output variance of TDOA Estimates** 复选框以启用包含 TDOA 方差的 **Var** 输出端口。

**数据类型：** `Boolean`

### **Output TDOA response and TDOA grid** — 输出 TDOA 响应和 TDOA 网格 `false` (0) (默认) | `true` (1)

选中 **Output TDOA response and TDOA grid** 复选框以启用 **TROAResp** 和 **TDOAGrid** 输出端口。

**数据类型：** `Boolean`

### **Source of noise power** — 噪声功率源 `Property` (默认) | `Input port`

噪声功率源，指定为 `Property` 或 `Input port`。

### **Noise power (W)** — 噪声功率 `1` (默认) | 正标量

噪声功率，指定为正标量。单位为 Watts。

#### 依赖项

要启用此参数，请将 **Source of noise power** 设置为 `Property`。

**数据类型：** `double` | `single`

### **Simulate using** — 模块仿真方法 `Interpreted Execution` (默认) | `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果您希望模块使用 MATLAB 解释器，请选择 `Interpreted Execution`。如果您希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间编译，但通常运行更快。

当您开发和调整模型时，解释执行很有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意时，可以使用 `Code Generation` 运行模块。长时间仿真使用生成代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果您更改任何模块参数，则模块会在执行前自动重新编译。

此表显示 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式会覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 该模块使用 MATLAB 解释器执行。 | 该模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 该模块被编译。 | 模型中的所有模块都被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`, `Code Generation` |
| **默认值：** `Interpreted Execution` |

## 所属库

Phased Array System Toolbox / Direction of Arrival

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2024b 中引入**

### R2025a：新输出端口

新增两个输出端口，用于返回到达时间差 (TDOA) 数据和 TDOA 时间网格。

## 描述

估计到达时间差

估计从有源设备到多个无源锚点的信号的 TDOA。TDOA 基于不同锚点处的时域接收信号进行估计。
