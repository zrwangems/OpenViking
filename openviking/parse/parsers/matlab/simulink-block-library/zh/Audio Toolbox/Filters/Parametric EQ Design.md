---
type: simulink-block
title: 'Parametric Equalizer Design'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Filters'
documentation_page: 'parametricequalizerdesign'
documentation_source_path: 'ref/parametricequalizerdesign.html'
language: zh-CN
chinese_source: worker-translation
---

# Parametric Equalizer Design

## 端口

### 输入

### **N** — 滤波器阶数 正偶整数

使用此端口指定 **Filter order** 参数的值。

#### 依赖关系

要启用此端口，请选择 **Specify filter order from input port** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **G** — 增益 (dB) 实数标量

使用此端口指定 **Gain (dB)** 参数的值。

#### 依赖关系

要启用此端口，请选择 **Specify gain from input port** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Fc** — 归一化中心频率 范围为 [0,1] 的标量

使用此端口指定 **Normalized center frequency** 参数的值。

#### 依赖关系

要启用此端口，请选择 **Specify normalized center frequency from input port** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **BW** — 归一化带宽 范围为 [0,1] 的标量

使用此端口指定 **Normalized bandwidth** 参数的值。

#### 依赖关系

要启用此端口，请选择 **Specify normalized bandwidth from input port** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
### 输出

### **Num** — 分子滤波器系数矩阵

分子滤波器系数，以矩阵形式返回。

- 对于 SOS 滤波器，该模块将系数以 *N*×3 矩阵形式返回。
- 对于 FOS 滤波器，该模块将系数以 *N*×5 矩阵形式返回。

*N* 是滤波器节数，取决于 **Maximum filter order** 参数。如果 **Filter order** 小于 **Maximum filter order**，则该模块将未使用的节设置为直通节。

#### 依赖关系

- 输出的数据类型取决于 **Output data type** 参数。
- 输出维度取决于 **Maximum filter order** 和 **Filter cascade sections form** 参数。

**数据类型：** `single` | `double`

### **Den** — 分母滤波器系数矩阵

分母滤波器系数，以矩阵形式返回。

- 对于 SOS 滤波器，该模块将系数以 *N*×3 矩阵形式返回。
- 对于 FOS 滤波器，该模块将系数以 *N*×5 矩阵形式返回。

*N* 是滤波器节数，取决于 **Maximum filter order** 参数。如果 **Filter order** 小于 **Maximum filter order**，则该模块将未使用的节设置为直通节。

#### 依赖关系

- 输出的数据类型取决于 **Output data type** 参数。
- 输出维度取决于 **Maximum filter order** 和 **Filter cascade sections form** 参数。

**数据类型：** `single` | `double`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### **Smooth tuned filter parameters** — 调谐时平滑滤波器参数 `off`（默认）| `on`

选择此参数可在调谐滤波器参数时逐渐将其更改为新值。如果清除此参数，则调谐的参数会立即切换到新值。使用 **Smoothing factor** 参数指定平滑程度。

### **Smoothing factor** — 调谐参数的平滑因子 `0.6`（默认）| 范围为 [0,1) 的标量

调谐参数的平滑因子，指定为范围 [0,1) 内的标量。当平滑因子接近 1 时，调谐参数会更逐渐地更改为新值。平滑因子为 0 等同于不平滑。

有关平滑的详细信息，请参阅 Smoothing。

**可调谐：** 是

#### 依赖关系

要启用此参数，请选择 **Smooth tuned filter parameters** 参数。

### **Maximum filter order** — 最大滤波器阶数 `2`（默认）| 正偶整数

所设计系数的最大滤波器阶数，指定为正偶整数。**Filter order** 参数不能超过此值。

### **Specify filter order from input port** — 使用附加输入端口指定滤波器阶数 `off`（默认）| `on`

选择此参数后，会向该模块添加一个附加输入端口 **N**。

### **Filter order** — 滤波器阶数 `2`（默认）| 正偶整数

所设计系数的滤波器阶数，指定为正偶整数。

**可调谐：** 是

#### 依赖关系

- 要启用此参数，请清除 **Specify filter order from input port** 参数。
- 此参数的值不能超过 **Maximum filter order**。

### **Specify gain from input port** — 使用附加输入端口指定增益 `off`（默认）| `on`

选择此参数后，会向该模块添加一个附加输入端口 **G**。使用此端口指定滤波器的增益。

### **Gain (dB)** — 增益 (dB) `0`（默认）| 实数标量

滤波器的增益，以 dB 为单位，指定为实数标量。

**可调谐：** 是

#### 依赖关系

要启用此参数，请清除 **Specify gain from input port** 参数。

### **Specify normalized center frequency from input port** — 使用附加输入端口指定归一化中心频率 `off`（默认）| `on`

选择此参数后，会向该模块添加一个附加输入端口 **Fc**。

### **Normalized center frequency** — 归一化中心频率 `0.2`（默认）| 范围为 [0,1] 的标量

滤波器的归一化中心频率，指定为范围 [0,1] 内的标量，其中 1 对应于奈奎斯特频率。

**可调谐：** 是

#### 依赖关系

要启用此参数，请清除 **Specify normalized center frequency from input port** 参数。

### **Specify normalized bandwidth from input port** — 使用附加输入端口指定归一化带宽 `off`（默认）| `on`

选择此参数后，会向该模块添加一个附加输入端口 **BW**。

### **Normalized bandwidth** — 归一化带宽 `0.1`（默认）| 范围为 [0,1] 的标量

滤波器的归一化带宽，指定为范围 [0,1] 内的标量，其中 1 对应于奈奎斯特频率。

归一化带宽在增益/2 dB 处测量。如果增益设置为 `-Inf`（陷波滤波器），则归一化带宽在 3 dB 衰减点处测量：10×log10(0.5)。

要将倍频程带宽转换为归一化带宽，请计算相关的 *Q* 因子为

Q=2(octave bandwidth)2(octave bandwidth)−1 .

然后转换为带宽

bandwidth=centerFreqQ .

#### 依赖关系

要启用此参数，请清除 **Specify normalized bandwidth from input port** 参数。

**可调谐：** 是

### **Filter cascade sections form** — 级联滤波器节的形式 `Second-order sections`（默认）| `Fourth-order sections`

级联滤波器节的形式，对于 SOS 滤波器指定为 `Second-order sections`，对于 FOS 滤波器指定为 `Fourth-order sections`。

### **Output data type** — 输出系数的数据类型 `double`（默认）| `single`

输出系数的数据类型，指定为 `double` 或 `single`。

### **Sample time** — 模块的采样时间 `-1`（默认）| 正标量

模块的采样时间，以秒为单位，指定为 `-1` 或正标量。将此参数设置为 `-1` 表示 Simulink 会自动为您确定采样时间。您可以设置此参数以使设计模块以比滤波模块更慢的速率运行。

### **Simulate using** — 指定要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

- `Interpreted execution` –– 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但仿真速度比 `Code generation` 慢。在此模式下，您可以调试模块的源代码。
- `Code generation` –– 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，C 代码就会在后续仿真中重用。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。

## 所属库

Audio Toolbox / Filters

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

## 描述

设计可调谐参数均衡器系数

Parametric Equalizer Design 模块设计具有指定滤波器阶数、增益、中心频率和带宽的参数均衡器。该模块输出级联二阶节 (SOS) 或四阶节 (FOS) 滤波器的滤波器系数，您可以将其与 Second-Order Section Filter 或 Fourth-Order Section Filter 模块一起使用来对音频信号进行滤波。您可以在仿真期间调谐滤波器参数。
