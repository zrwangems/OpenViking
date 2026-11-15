---
type: simulink-block
title: 'TOA Estimator'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Detection, Range and Doppler Estimation / Localization'
documentation_page: 'toaestimator'
documentation_source_path: 'ref/toaestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# TOA Estimator

## 端口

### 输入

### **X** — 信道估计矩阵 *N*-by-*M* 复值矩阵 | *N*-by-*M*-by-*L* 复值数组 | 1-by-*L* 元胞数组

信道估计矩阵，指定为
*N*-by-*M* 复值矩阵、
*N*-by-*M*-by-*L* 复值
数组或 1-by-*L* 元胞数组。*N*-by-*M* 信道估计矩阵的每一行表示
一个子带上的信道估计的 *M* 个样本（例如，MIMO
通信的 *M* 个空间流、雷达的 *M* 个脉冲），矩阵的每一列表示
*N* 个均匀间隔子带上的信道估计的一个样本。

- 当信道估计矩阵是
  *N*-by-*M*-by-*L* 数组时，
  数组的每一页是一个 *N*-by-*M*
  信道估计矩阵。所有信道估计矩阵必须具有相同
  大小。
- 当信道估计矩阵是 1-by-*L* 元胞
  数组时，每个元胞包含来自 *L* 个锚点之一的
  频域信道估计矩阵。对于不同锚点，信道估计矩阵的大小
  可以不同。

**数据类型:** `single` | `double`
**复数支持:** Yes

### **FreqSpacing** — 信道估计的频率间隔 `900000`

信道估计的频率间隔，指定为正标量或
1-by-*L* 正值向量。如果 **FreqSpacing** 是
标量，则所有 *L* 个锚点的频率间隔相同。如果
**FreqSpacing** 是 1-by-*L* 向量，则不同锚点的频率
间隔可以不同。单位是 Hz。

**示例:** `[10e6 15e6 20e6]`

**数据类型:** `single` | `double`

### **DelayOffset** — 已知延迟偏移 标量 | 实值 1-by-*L* 向量

目标与每个锚点之间的已知延迟偏移，指定为标量或
实值 1-by-*L* 向量。如果 **DelayOffset** 是标量，
则来自或到达所有 *L* 个锚点的所有信号的延迟偏移相同。如果
**DelayOffset** 是 1-by-*L* 向量，则不同锚点的延迟
偏移可以不同。**DelayOffset** 补偿
所有 TOA/TDOA 估计结果 **Y**。单位是 seconds。

#### 依赖关系

要启用此端口，请选中 **启用已知延迟偏移输入** 复选框。

**数据类型:** `single` | `double`

### **NPow** — 高斯白噪声功率 标量 | 正实值 1-by-*L* 向量

高斯白噪声功率，指定为标量或正实值
1-by-*L* 向量。如果 `npow` 是标量，
则所有 *L* 个锚点的噪声功率相同。如果 **NPow** 是
1-by-*L* 向量，则可以对 *L* 个锚点中的每一个应用不同的噪声功率值。单位是 watts。

**示例:** `0.4`

#### 依赖关系

要启用此端口，请选中 **输出 TOA/TDOA 估计的方差** 复选框，然后将 **噪声功率源** 端口设置为 `'Input port'`。

**数据类型:** `single` | `double`

### **AnchorPos** — 锚点位置 *Q*-by-*L* 实值矩阵

锚点位置，指定为 *Q*-by-*L*
实值矩阵，表示 *L* 个锚点在
*Q* 维笛卡尔空间中的位置（*Q* 可以为 2 或
3）。每一列表示每个锚点在
*Q* 维笛卡尔空间中的位置。

#### 依赖关系

要启用此端口，请选中 **输出估计的目标位置** 复选框。

**数据类型:** `single` | `double`

### 输出

### **Y** — TOA 和 TDOA 估计结果 1-by-*L* 实值向量 | 1-by-(*L*-1) 实值向量

来自 *L* 个锚点处目标的
到达时间（TOA）或到达时间差（TDOA）估计，输出为 1-by-*L*
实值向量或 1-by-(*L*-1) 实值向量。

- 如果 `TOA/TDOA Measurement` 参数是
  `'TOA'`，则 **Y** 是 1-by-*L*
  实值向量。第
  `l` 个锚点处 TOA 输出的信号模型可以写为
  `Y(l) = min(taul)`，对于 `l = 1,2,...,L`，
  其中 `taul` 是第
  `l` 个锚点处接收到的多径延迟向量。
- 如果 `TOA/TDOA Measurement` 参数设置为
  `'TDOA'`，则 **Y** 是 1-by-(*L*-1)
  实值向量。第
  (`l`-1) 个锚点处 TDOA 输出的信号模型可以写为
  `Y(l-1) = min(taul)-min(reftau)`，`l =
  2,3,...,L`，其中 `taul` 是第 `l` 个锚点处接收到的
  多径延迟向量
  且 `reftau` 是第一个锚点处接收到的多径延迟向量。

单位是 seconds。

**数据类型:** `single` | `double`

### **Var** — 测量方差 1-by-*L* 向量 | 1-by-(*L*-1) 向量

- 如果 `Measurement` 是 `'TOA'`，
  则 **Var** 是 1-by-*L* 向量，表示
  估计的 TOA 方差。
- 如果 `Measurement` 属性是
  `'TDOA'`，则 **Var** 是 1-by-(*L*-1)
  向量，表示估计的 TDOA 方差。

单位是 seconds-squared。**Var** 通过
TOA/TDOA 估计器的 Cramer-Rao 下界（CRLB）获得。

#### 依赖关系

要启用此端口，请选中 **输出 TOA/TDOA 估计的方差** 复选框，然后将 **噪声功率源** 端口设置为 `'Input port'`。

**数据类型:** `single` | `double`

### **TgtPosEst** — 目标位置估计 实值 *Q*-by-1 向量

估计的目标位置，输出为 *Q*-by-1 向量，
表示从 TOA 和 TDOA 测量获得的估计目标位置。
目标位置使用两步加权线性最小二乘（WLLS）
算法获得，该算法近似最大似然估计算法。当 TOA 和 TDOA 估计误差
较小时，该算法可以达到位置估计 CRLB。单位是 meters。

#### 依赖关系

要启用此端口，请选中 **输出估计的目标位置** 复选框。

**数据类型:** `single` | `double`

### **TgtPosCov** — 目标位置协方差估计 *Q*-by-*Q* 实正半定对称矩阵

目标位置协方差估计，输出为
*Q*-by-*Q* 实正半定对称
矩阵。该矩阵表示使用 TOA/TDOA
测量估计的目标位置协方差。协方差从 TOA/TDOA 位置
估计的 CRLB 获得。单位是 m2。

#### 依赖关系

要启用此端口，请选中 **输出估计的目标位置** 复选框。

**数据类型:** `single` | `double`

### **TOAResp** — 基于 FFT 的 TOA 响应 *P*-by-*M*-by-*L* 矩阵 | 1-by-*L* 元胞数组

基于 FFT 的 TOA 响应，输出为：

如果信道估计 `X` 是
*N*-by-*M*-by-*L* 数组，
则 `toaresp` 是
*P*-by-*M*-by-*L* 数组。

如果信道估计 `X` 是 1-by-*L* 元胞
数组，则 `toaresp` 是 1-by-*L* 元胞数组，
包含 *s* 个锚点中每个锚点的 TOA 响应。

#### 依赖关系

要启用此端口，请选中 **输出基于 FFT 的 TOA 响应** 复选框。

**数据类型:** `single` | `double`
**复数支持:** Yes

### **TOAGrid** — TOA 网格 *P*-by-*L* 矩阵 | 1-by-*L* 元胞数组

到达时间网格，输出为 *P*-by-*L*
矩阵或 1-by-*L* 元胞数组。到达时间被限制到
此网格。

- 如果信道估计 `X` 是
  *N*-by-*M*-by-*L* 数组，
  则 `toagrid` 返回为
  *P*-by-*L* 矩阵，其中
  *P* 是 TOA 网格样本的数量。
- 如果信道估计 `X` 是
  1-by-*L* 元胞数组，则 `toagrid` 是
  1-by-*L* 元胞数组，包含 *L* 个锚点中每个锚点的
  TOA 网格。单位是 seconds。

#### 依赖关系

要启用此端口，请选中 **输出基于 FFT 的 TOA 响应** 复选框。

**数据类型:** `single`

## 参数

要交互式编辑模块参数，请使用
Property Inspector。在 Simulink Toolstrip 上，在 **Simulation** 选项卡的
**Prepare** 库中，选择 **Property
Inspector**。

### **信号传播速度 (m/s)** — 信号传播速度 `physconst('LightSpeed')` (默认) | 实值正标量

信号传播速度，指定为实值正标量。光速的默认
值是由
`physconst('LightSpeed')` 返回的值。单位是 meters per second。

**示例:** `3e8`

**数据类型:** `double` | `single`

### **TOA/TDOA 测量** — 测量类型 `TOA` (默认) | `TDOA`

测量类型，指定为 `TOA` 或
`TDOA`。选择 `TOA` 时，使用 TOA 频谱分析和 TOA 定位算法
估计 TOA 测量。选择 `TDOA` 时，基于 TOA 测量计算 TDOA
测量，并使用 TDOA 定位算法。

**数据类型:** `char` | `string`

### **TOA 频谱分析方法** — 频谱分析方法 `FFT` (默认) | `MUSIC`

TOA 频谱分析方法，指定为 `FFT` 或
`MUSIC`。选择 `FFT` 时，使用
FFT 获得 TOA 频谱。选择 `MUSIC` 时，
使用 MUSIC 超分辨率算法获得 TOA 频谱。

**数据类型:** `char` | `string`

### **启用已知延迟偏移输入** — 启用延迟偏移输入 0 (默认) | 1

选中此复选框以启用使用 **DelayOffset** 输入端口输入锚点与目标之间的已知延迟偏移或估计延迟偏移。未
选中时，**DelayOffset** 输入端口被禁用，并假定延迟偏移
为零。

**数据类型:** `Boolean`

### **输出 TOA/TDOA 估计的方差** — 启用输出 TOA/TDOA 估计的方差 0 (默认) | 1

选中此复选框以启用使用 **Var** 输出端口输出 TOA 或 TDOA 估计的方差。清除此复选框则不输出估计的
方差。选中此复选框还会启用 **噪声功率源** 和 **噪声功率 (W)** 参数以及
**Npow** 输入端口。

**数据类型:** `Boolean`

### **输出基于 FFT 的 TOA 响应** — 启用输出基于 FFT 的 TOA 响应 `0` (默认) | `1`

选中此复选框以输出基于 FFT 的 TOA 响应。清除此复选框则不
输出 TOA 响应。

#### 依赖关系

要启用此参数，请将 **TOA/TDOA 测量** 参数设置为 **TOA**，并将 **TOA 频谱分析方法** 设置为 **FFT**。

**数据类型:** `Boolean`

### **启用前向-后向平均** — 启用前向-后向平均 `0` (默认) | `1`

选中此复选框以启用前向-后向平均。前向-后向
平均用于减轻 MUSIC 频谱分析估计方法中使用的
源协方差矩阵的秩不足。当信道估计的独立样本数量较小时，
这很有用。

#### 依赖关系

要启用此参数，请将 **TOA 频谱分析方法** 设置为 `MUSIC`。

**数据类型:** `Boolean`

### **空间平滑** — 空间平滑参数 0 (默认) | 非负整数

由于空间平滑导致的 TOA 估计子带数量的有效减少，指定为非负整数。空间平滑可用于减轻
MUSIC 频谱分析方法的源协方差矩阵估计中的秩不足问题。当信道估计的独立样本数量较小时，此技术很有用。

如果有 *N* 个子带，且 **空间平滑** 参数的值为 *K*，则形成 (*K*+1) 个最大重叠的 *N-K* 子带频带。然后，
对 (*K*+1) 个重叠频带上的信号估计 (*K*+1) 个协方差矩阵，并将这些 (*K*+1)
个协方差矩阵一起平均，以产生大小为
(*N*-*K*)-by-(*N*-*K*) 的空间平滑协方差矩阵。
将 *K* 增加 1 会使空间平滑协方差矩阵的秩增加 1，直到范围达到其最大值。但是，用于 TOA 估计的有效
子带数量减少 1。*K* 的最小值为 0，这导致无空间平滑。*K* 的最大值为 *N*-2，导致 (*N*-1)
个由两个子带组成的重叠频带。

如果 **空间平滑** 是标量，则所有 *L* 个锚点的空间平滑值相同。如果 **空间平滑** 是长度-*L* 向量，则每个空间平滑值应用于 *L* 个锚点之一。

#### 依赖关系

要启用此参数，请将 **TOA 频谱分析方法** 设置为 `MUSIC`。

**数据类型:** `single` | `double`

### **输出估计的目标位置** — 启用输出估计的目标位置 0 (默认) | 1

选中此复选框以启用使用 **TgtPosEst** 端口输出估计的目标位置，以及使用 **TgtPosCov** 端口输出估计的目标位置协方差。选中此复选框还允许使用 **AnchorPos** 端口输入锚点位置。

**数据类型:** `Boolean`

### **噪声功率源** — 噪声功率源 `Property` (默认) | `Input port`

指定对象如何确定用于 TOA 和 TDOA 方差估计的噪声功率值，指定为 `'Property'` 或 `'Input port'`。
当将 **噪声功率源** 参数设置为
`'Property'` 时，**噪声功率 (W)** 参数
表示接收数据的噪声功率。当将 **噪声功率源** 设置为 `'Input port'` 时，通过输入 **NPow** 端口设置噪声功率。

**示例:** `Input port`

#### 依赖关系

要启用此参数，请选中 **输出估计的目标位置** 复选框。

**数据类型:** `char` | `string`

### **噪声功率 (W)** — 高斯白噪声功率 正标量 (默认) | 1-by-*L* 正值实值向量

高斯白噪声功率，指定为正标量或
1-by-*L* 正值实值向量。

#### 依赖关系

要启用此参数，请选中 **输出估计的目标位置** 复选框，然后选择 **噪声功率源** 为 `Property`。

**数据类型:** `single` | `double`

### **仿真使用** — 模块仿真方法 `Interpreted Execution` (默认) | `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或
`Code Generation`。如果希望模块使用
MATLAB® 解释器，请选择 `Interpreted Execution`。如果
希望模块作为编译代码运行，请选择 `Code
Generation`。编译代码需要时间编译，但通常运行
更快。

在开发和调整模型时，解释执行很有用。模块
在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您
对结果满意时，随后可以使用 `Code
Generation` 运行模块。长时间仿真的运行速度在使用生成代码时比在
解释执行中更快。您可以重复执行而无需重新编译，但如果
更改任何模块参数，则模块会在执行前自动重新编译。

此表显示 **仿真使用** 参数如何影响
整体仿真行为。

当 Simulink 模型处于 `Accelerator` 模式时，使用 **仿真使用** 指定的模块模式
会覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块均被编译。 |

有关更多信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数:** `SimulateUsing` |
| **类型:** enum |
| **值:** `Interpreted Execution`, `Code Generation` |
| **默认值:** `Interpreted Execution` |

## 所属库

Phased Array System Toolbox / Direction of Arrival

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

## 描述

估计到达时间、到达时间差和位置

TOA Estimator 模块 Simulink® 估计多个设备处的到达时间（TOA）或到达时间差（TDOA）。该模块估计从一个主动设备到多个被动锚点，或从多个主动锚点到一个被动设备的 TOA 或 TDOA。TOA 和 TDOA 基于频域信道估计进行估计。利用 TOA，该模块随后估计目标位置。
