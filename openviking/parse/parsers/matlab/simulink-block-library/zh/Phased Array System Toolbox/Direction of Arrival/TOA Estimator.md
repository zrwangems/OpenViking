---
type: simulink-block
title: 'TOA Estimator'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Direction of Arrival'
documentation_page: 'toaestimator'
documentation_source_path: 'ref/toaestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# TOA Estimator

## 端口

### 输入

### **X** — 信道估计矩阵 *N*×*M* 复值矩阵 | *N*×*M*×*L* 复值数组 | 1×*L* 元胞数组

信道估计矩阵，指定为 *N*×*M* 复值矩阵、*N*×*M*×*L* 复值数组或 1×*L* 元胞数组。*N*×*M* 信道估计矩阵的每一行表示一个子带上信道估计的 *M* 个采样（例如，MIMO 通信的 *M* 个空间流、雷达的 *M* 个脉冲），矩阵的每一列表示 *N* 个均匀间隔子带上信道估计的一个采样。

- 当信道估计矩阵为 *N*×*M*×*L* 数组时，数组的每一页是一个 *N*×*M* 信道估计矩阵。所有信道估计矩阵必须具有相同的大小。
- 当信道估计矩阵为 1×*L* 元胞数组时，每个元胞包含来自 *L* 个锚点之一的频域信道估计矩阵。不同锚点的信道估计矩阵大小可以不同。

**数据类型：** `single` | `double`
**复数支持：** 是

### **FreqSpacing** — 信道估计的频率间隔 `900000`

信道估计的频率间隔，指定为正标量或 1×*L* 正数值向量。如果 **FreqSpacing** 为标量，则所有 *L* 个锚点的频率间隔相同。如果 **FreqSpacing** 为 1×*L* 向量，则不同锚点的频率间隔可以不同。单位为 Hz。

**示例：** `[10e6 15e6 20e6]`

**数据类型：** `single` | `double`

### **DelayOffset** — 已知延迟偏移 标量 | 实值 1×*L* 向量

目标与每个锚点之间的已知延迟偏移，指定为标量或实值 1×*L* 向量。如果 **DelayOffset** 为标量，则来自或到达所有 *L* 个锚点的所有信号的延迟偏移相同。如果 **DelayOffset** 为 1×*L* 向量，则不同锚点的延迟偏移可以不同。**DelayOffset** 补偿所有 TOA/TDOA 估计结果 **Y**。单位为秒。

#### 依赖

要启用此端口，请选中 **Enable known delay offset input** 复选框。

**数据类型：** `single` | `double`

### **NPow** — 高斯白噪声功率 标量 | 正实值 1×*L* 向量

高斯白噪声功率，指定为标量或正实值 1×*L* 向量。如果 `npow` 为标量，则所有 *L* 个锚点的噪声功率相同。如果 **NPow** 为 1×*L* 向量，则可以对 *L* 个锚点中的每一个应用不同的噪声功率值。单位为瓦特。

**示例：** `0.4`

#### 依赖

要启用此端口，请选中 **Output variance of TOA/TDOA estimates** 复选框，然后将 **Source of noise power** 端口设置为 `'Input port'`。

**数据类型：** `single` | `double`

### **AnchorPos** — 锚点位置 *Q*×*L* 实值矩阵

锚点位置，指定为 *Q*×*L* 实值矩阵，表示 *L* 个锚点在 *Q* 维笛卡尔空间中的位置（*Q* 可以为 2 或 3）。每一列表示每个锚点在 *Q* 维笛卡尔空间中的位置。

#### 依赖

要启用此端口，请选中 **Output estimated target position** 复选框。

**数据类型：** `single` | `double`
### 输出

### **Y** — TOA 和 TDOA 估计结果 1×*L* 实值向量 | 1×(*L*-1) 实值向量

来自 *L* 个锚点处目标的到达时间（TOA）或到达时间差（TDOA）估计，输出为 1×*L* 实值向量或 1×(*L*-1) 实值向量。

- 如果 `TOA/TDOA Measurement` 参数为 `'TOA'`，**Y** 是 1×*L* 实值向量。第 `l` 个锚点处 TOA 输出的信号模型可写为 `Y(l) = min(taul)`，其中 `l = 1,2,...,L`，`taul` 是第 `l` 个锚点处接收到的多径延迟向量。
- 如果 `TOA/TDOA Measurement` 参数设置为 `'TDOA'`，**Y** 是 1×(*L*-1) 实值向量。第 (`l`-1) 个锚点处 TDOA 输出的信号模型可写为 `Y(l-1) = min(taul)-min(reftau)`，`l = 2,3,...,L`，其中 `taul` 是第 `l` 个锚点处接收到的多径延迟向量，`reftau` 是第一个锚点处接收到的多径延迟向量。

单位为秒。

**数据类型：** `single` | `double`

### **Var** — 测量方差 1×*L* 向量 | 1×(*L*-1) 向量

- 如果 `Measurement` 为 `'TOA'`，**Var** 是 1×*L* 向量，表示估计的 TOA 方差。
- 如果 `Measurement` 属性为 `'TDOA'`，**Var** 是 1×(*L*-1) 向量，表示估计的 TDOA 方差。

单位为秒的平方。**Var** 通过 TOA/TDOA 估计器的 Cramer-Rao 下界（CRLB）获得。

#### 依赖

要启用此端口，请选中 **Output variance of TOA/TDOA estimates** 复选框，然后将 **Source of noise power** 端口设置为 `'Input port'`。

**数据类型：** `single` | `double`

### **TgtPosEst** — 目标位置估计 实值 *Q*×1 向量

估计的目标位置，输出为 *Q*×1 向量，表示从 TOA 和 TDOA 测量获得的目标位置估计。目标位置使用两步加权线性最小二乘（WLLS）算法获得，该算法近似最大似然估计算法。当 TOA 和 TDOA 估计误差较小时，该算法可达到位置估计的 CRLB。单位为米。

#### 依赖

要启用此端口，请选中 **Output estimated target position** 复选框。

**数据类型：** `single` | `double`

### **TgtPosCov** — 目标位置协方差估计 *Q*×*Q* 实正半定对称矩阵

目标位置协方差估计，输出为 *Q*×*Q* 实正半定对称矩阵。该矩阵表示使用 TOA/TDOA 测量估计的目标位置协方差。协方差通过 TOA/TDOA 位置估计的 CRLB 获得。单位为 m2。

#### 依赖

要启用此端口，请选中 **Output estimated target position** 复选框。

**数据类型：** `single` | `double`

### **TOAResp** — 基于 FFT 的 TOA 响应 *P*×*M*×*L* 矩阵 | 1×*L* 元胞数组

基于 FFT 的 TOA 响应，输出为：

如果信道估计 `X` 是 *N*×*M*×*L* 数组，`toaresp` 是 *P*×*M*×*L* 数组。

如果信道估计 `X` 是 1×*L* 元胞数组，`toaresp` 是 1×*L* 元胞数组，包含 *s* 个锚点中每个锚点的 TOA 响应。

#### 依赖

要启用此端口，请选中 **Output FFT-based TOA response** 复选框。

**数据类型：** `single` | `double`
**支持复数：** 是

### **TOAGrid** — TOA 网格 *P*×*L* 矩阵 | 1×*L* 元胞数组

到达时间网格，输出为 *P*×*L* 矩阵或 1×*L* 元胞数组。到达时间被限制在该网格上。

- 如果信道估计 `X` 是 *N*×*M*×*L* 数组，`toagrid` 返回为 *P*×*L* 矩阵，其中 *P* 是 TOA 网格样本数。
- 如果信道估计 `X` 是 1×*L* 元胞数组，`toagrid` 是 1×*L* 元胞数组，包含 *L* 个锚点中每个锚点的 TOA 网格。单位为秒。

#### 依赖关系

要启用此端口，请选中 **Output FFT-based TOA response** 复选框。

**数据类型：** `single`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### **Signal propagation speed (m/s)** — 信号传播速度 `physconst('LightSpeed')`（默认）| 实值正标量

信号传播速度，指定为实值正标量。光速的默认值是 `physconst('LightSpeed')` 返回的值。单位为米每秒。

**示例：** `3e8`

**数据类型：** `double` | `single`

### **TOA/TDOA measurement** — 测量类型 `TOA`（默认）| `TDOA`

测量类型，指定为 `TOA` 或 `TDOA`。当选择 `TOA` 时，使用 TOA 频谱分析和 TOA 定位算法来估计 TOA 测量值。当选择 `TDOA` 时，基于 TOA 测量值计算 TDOA 测量值，并使用 TDOA 定位算法。

**数据类型：** `char` | `string`

### **TOA spectrum analysis method** — 频谱分析方法 `FFT`（默认）| `MUSIC`

TOA 频谱分析方法，指定为 `FFT` 或 `MUSIC`。当选择 `FFT` 时，使用 FFT 获得 TOA 频谱。当选择 `MUSIC` 时，使用 MUSIC 超分辨率算法获得 TOA 频谱。

**数据类型：** `char` | `string`

### **Enable known delay offset input** — 启用延迟偏移输入 0（默认）| 1

选中此复选框可通过 **DelayOffset** 输入端口启用锚点与目标之间已知延迟偏移或估计延迟偏移的输入。未选中时，**DelayOffset** 输入端口被禁用，延迟偏移假定为零。

**数据类型：** `Boolean`

### **Output variance of TOA/TDOA estimates** — 启用 TOA/TDOA 估计方差输出 0（默认）| 1

选中此复选框可通过 **Var** 输出端口启用 TOA 或 TDOA 估计方差的输出。清除此复选框则不输出估计方差。选中此复选框还会启用 **Source of noise power** 和 **Noise power (W)** 参数以及 **Npow** 输入端口。

**数据类型：** `Boolean`

### **Output FFT-based TOA response** — 启用基于 FFT 的 TOA 响应输出 `0`（默认）| `1`

选中此复选框则输出基于 FFT 的 TOA 响应。清除此复选框则不输出 TOA 响应。

#### 依赖关系

要启用此参数，请将 **TOA/TDOA Measurement** 参数设置为 **TOA**，并将 **TOA spectrum analysis method** 设置为 **FFT**。

**数据类型：** `Boolean`

### **Enable forward-backward averaging** — 启用前向-后向平均 `0`（默认）| `1`

选中此复选框以启用前向-后向平均。前向-后向平均用于减轻 MUSIC 频谱分析估计方法中使用的源协方差矩阵的秩亏缺。当信道估计的独立样本数较少时，这很有用。

#### 依赖关系

要启用此参数，请将 **TOA spectrum analysis method** 设置为 `MUSIC`。

**数据类型：** `Boolean`

### **Spatial smoothing** — 空间平滑参数 0（默认）| 非负整数

由于空间平滑导致的 TOA 估计子带数量的有效减少量，指定为非负整数。空间平滑可用于缓解 MUSIC 谱分析方法中源协方差矩阵估计的秩亏问题。当信道估计的独立样本数较少时，该技术非常有用。

如果有 *N* 个子带，且 **Spatial smoothing** 参数的值为 *K*，则形成 (*K*+1) 个最大重叠的 *N-K* 个子带。然后，为 (*K*+1) 个重叠频带上的信号估计 (*K*+1) 个协方差矩阵，并将这些 (*K*+1) 个协方差矩阵平均在一起，产生大小为 (*N*-*K*)-by-(*N*-*K*) 的空间平滑协方差矩阵。将 *K* 增加 1 会使空间平滑协方差矩阵的秩增加 1，直到达到其最大值。然而，用于 TOA 估计的有效子带数量减少 1。*K* 的最小值为 0，表示不进行空间平滑。*K* 的最大值为 *N*-2，产生 (*N*-1) 个两个子带的重叠频带。

如果 **Spatial smoothing** 是标量，则空间平滑值对所有 *L* 个锚点相同。如果 **Spatial smoothing** 是长度为 *L* 的向量，则每个空间平滑值分别应用于 *L* 个锚点中的一个。

#### 依赖关系

要启用此参数，请将 **TOA spectrum analysis method** 设置为 `MUSIC`。

**Data Types:** `single` | `double`

### **Output estimated target position** — 启用估计目标位置输出 0（默认）| 1

选中此复选框可通过 **TgtPosEst** 端口输出估计的目标位置，并通过 **TgtPosCov** 端口输出估计的目标位置协方差。选中此复选框还允许通过 **AnchorPos** 端口输入锚点位置。

**Data Types:** `Boolean`

### **Source of noise power** — 噪声功率来源 `Property`（默认）| `Input port`

指定对象如何确定用于 TOA 和 TDOA 方差估计的噪声功率值，可选 `'Property'` 或 `'Input port'`。当将 **Source of noise power** 参数设置为 `'Property'` 时，**Noise power (W)** 参数表示接收数据的噪声功率。当将 **Source of noise power** 设置为 `'Input port'` 时，通过输入 **NPow** 端口设置噪声功率。

**Example:** `Input port`

#### 依赖关系

要启用此参数，请选中 **Output estimated target position** 复选框。

**Data Types:** `char` | `string`

### **Noise power (W)** — 高斯白噪声功率 正标量（默认）| 1-by-*L* 正实数值向量

高斯白噪声功率，指定为正标量或 1-by-*L* 正实数值向量。

#### 依赖关系

要启用此参数，请选中 **Output estimated target position** 复选框，然后选择 **Source of noise power** 为 `Property`。

**Data Types:** `single` | `double`

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

在开发和调整模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真使用生成代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果更改任何模块参数，模块将在执行前自动重新编译。

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

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

## 描述

估计到达时间、到达时间差和位置

TOA Estimator 模块 Simulink® 估计多个设备的到达时间（TOA）或到达时间差（TDOA）。该模块从有源设备到多个无源锚点，或从多个有源锚点到无源设备，估计 TOA 或 TDOA。TOA 和 TDOA 基于频域信道估计进行估计。使用 TOA，该模块随后估计目标位置。
