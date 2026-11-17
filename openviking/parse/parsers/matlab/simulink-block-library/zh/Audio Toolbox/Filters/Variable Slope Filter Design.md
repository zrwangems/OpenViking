---
type: simulink-block
title: 'Variable Slope Filter Design'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Filters'
documentation_page: 'variableslopefilterdesign'
documentation_source_path: 'ref/variableslopefilterdesign.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable Slope Filter Design

## 端口

### 输入

### **S** — 滤波器斜率标量，范围为 [0,48]

使用此端口指定 **Filter slope** 参数的值。

#### 依赖关系

要启用此端口，请选择 **Specify slope from input port** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Fc** — 归一化截止频率标量，范围为 [0,1]

使用此端口指定 **Normalized cutoff frequency** 参数的值。

#### 依赖关系

要启用此端口，请选择 **Specify normalized cutoff frequency from input port** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **T** — 滤波器类型 `0`（低通）| `1`（高通）

使用此端口指定 **Filter type** 参数的值；`0` 对应低通滤波器，`1` 对应高通滤波器。

#### 依赖关系

要启用此端口，请选择 **Specify filter type from input port** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated`
### 输出

### **Num** — 分子滤波器系数，*N*×3 矩阵

分子滤波器系数，以 *N*×3 矩阵形式返回。*N* 是滤波器段数，取决于 **Maximum filter slope** 参数。如果 **Filter slope** 小于 **Maximum filter slope**，则模块将未使用的段设置为直通段。

#### 依赖关系

- 输出的数据类型取决于 **Output data type** 参数。
- 输出维度取决于 **Maximum filter slope** 参数。

**数据类型：** `single` | `double`

### **Den** — 分母滤波器系数，*N*×3 矩阵

分母滤波器系数，以 *N*×3 矩阵形式返回。*N* 是滤波器段数，取决于 **Maximum filter slope** 参数。更陡峭的斜率需要更多的滤波器段。如果 **Filter slope** 小于 **Maximum filter slope**，则模块将未使用的段设置为直通段。

#### 依赖关系

- 输出的数据类型取决于 **Output data type** 参数。
- 输出维度取决于 **Maximum filter slope** 参数。

**数据类型：** `single` | `double`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡中，在 **Prepare** 库中选择 **Property Inspector**。

### **Smooth tuned filter parameters** — 调谐时平滑滤波器参数 `off`（默认）| `on`

选择此参数可在调谐滤波器参数时逐渐将其更改为新值。如果清除此参数，则调谐后的参数立即切换到新值。使用 **Smoothing factor** 参数指定平滑程度。

### **Smoothing factor** — 调谐参数的平滑因子 `0.6`（默认）| 范围 [0,1) 内的标量

调谐参数的平滑因子，指定为范围 [0,1) 内的标量。当平滑因子趋近于 1 时，调谐参数更逐渐地变化到新值。平滑因子为 0 等同于不平滑。

有关平滑的详细信息，请参阅 Smoothing。

**可调谐：** 是

#### 依赖关系

要启用此参数，请选择 **Smooth tuned filter parameters** 参数。

### **Maximum filter slope** — 最大滤波器斜率（dB/octave） `12`（默认）| 范围 [0,48] 内的标量

最大滤波器斜率，以 dB/octave 为单位，指定为范围 [0,48] 内的标量。**Filter slope** 参数不能超过此值。

### **Specify slope from input port** — 使用附加输入端口指定斜率 `off`（默认）| `on`

选择此参数后，模块将添加一个附加输入端口 **S**。

### **Filter slope** — 滤波器斜率（dB/octave） `12`（默认）| 范围 [0,48] 内的标量

滤波器斜率，以 dB/octave 为单位，指定为范围 [0,48] 内的标量。模块将斜率值舍入到最接近的 6 的倍数。

**可调谐：** 是

#### 依赖关系

- 要启用此参数，请清除 **Specify slope from input port** 参数。
- 此参数的值不能超过 **Maximum filter slope** 参数的值。

### **Specify normalized cutoff frequency from input port** — 使用附加输入端口指定归一化截止频率 `off`（默认）| `on`

选择此参数后，模块将添加一个附加输入端口 **Fc**。

### **Normalized cutoff frequency** — 归一化截止频率 `0.1`（默认）| 范围 [0,1] 内的标量

滤波器的归一化截止频率，指定为范围 [0,1] 内的标量，其中 1 对应奈奎斯特频率。

**可调谐：** 是

#### 依赖关系

要启用此参数，请清除 **Specify normalized cutoff frequency from input port** 参数。

### **Specify filter type from input port** — 使用附加输入端口指定滤波器类型 `off`（默认）| `on`

选择此参数后，模块将添加一个附加输入端口 **T**。

### **Filter type** — 滤波器类型 `lowpass`（默认）| `highpass`

滤波器类型，指定为 `lowpass` 表示低通滤波器，或 `highpass` 表示高通滤波器。

### **Output data type** — 输出系数的数据类型 `double`（默认）| `single`

输出系数的数据类型，指定为 `double` 或 `single`。

### **Sample time** — 模块的采样时间 `-1`（默认）| 正标量

模块的采样时间，以秒为单位，指定为 `-1` 或正标量。将此参数设置为 `-1` 表示 Simulink 自动为您确定采样时间。您可以设置此参数以使设计模块以比滤波模块更慢的速率运行。

### **Simulate using** — 指定要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

- `Interpreted execution` —— 使用 MATLAB® 解释器仿真模型。此选项缩短启动时间，但仿真速度比 `Code generation` 慢。在此模式下，您可以调试模块的源代码。
- `Code generation` —— 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 为模块生成 C 代码。只要模型不更改，C 代码将在后续仿真中重用。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。

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

设计可调谐低通或高通滤波器系数

Variable Slope Filter Design 模块设计具有指定斜率和截止频率的低通或高通滤波器。该模块输出级联二阶节（SOS）滤波器的滤波器系数，您可以将其与 Second-Order Section Filter 模块配合使用来对音频信号进行滤波。您可以在仿真期间调谐滤波器参数。
