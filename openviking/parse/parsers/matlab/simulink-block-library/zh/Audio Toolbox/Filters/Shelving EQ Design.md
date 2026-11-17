---
type: simulink-block
title: 'Shelving Equalizer Design'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Filters'
documentation_page: 'shelvingequalizerdesign'
documentation_source_path: 'ref/shelvingequalizerdesign.html'
language: zh-CN
chinese_source: worker-translation
---

# Shelving Equalizer Design

## 端口

### 输入

### **G** — 峰值增益 (dB) 实数标量

使用此端口指定 **Peak gain (dB)** 参数的值。

#### 依赖关系

要启用此端口，请选择 **Specify peak gain from input port** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **S** — 斜率系数 正标量

使用此端口指定 **Slope coefficient** 参数的值。

#### 依赖关系

要启用此端口，请选择 **Specify slope coefficient from input port** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Fc** — 归一化截止频率 [0,1] 范围内的标量

使用此端口指定 **Normalized cutoff frequency** 参数的值。

#### 依赖关系

要启用此端口，请选择 **Specify normalized cutoff frequency from input port** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **T** — 滤波器类型 `0`（低架）| `1`（高架）

使用此端口指定 **Filter type** 参数的值；`0` 对应低架均衡器，`1` 对应高架均衡器。

#### 依赖关系

要启用此端口，请选择 **Specify filter type from input port** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated`
### 输出

### **Num** — 分子滤波器系数 三元素行向量

所设计 SOS 滤波器的分子滤波器系数，以三元素行向量形式返回。

#### 依赖关系

输出的数据类型取决于 **Output data type** 参数。

**数据类型：** `single` | `double`

### **Den** — 分母滤波器系数 三元素行向量

所设计 SOS 滤波器的分母滤波器系数，以三元素行向量形式返回。

#### 依赖关系

输出的数据类型取决于 **Output data type** 参数。

**数据类型：** `single` | `double`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### **Smooth tuned filter parameters** — 调谐时平滑滤波器参数 `off`（默认）| `on`

选择此参数可在调谐滤波器参数时逐渐将其更改为新值。如果清除此参数，则调谐后的参数会立即切换到新值。使用 **Smoothing factor** 参数指定平滑程度。

### **Smoothing factor** — 调谐参数的平滑因子 `0.6`（默认）| [0,1) 范围内的标量

调谐参数的平滑因子，指定为 [0,1) 范围内的标量。当平滑因子接近 1 时，调谐后的参数会更逐渐地更改为新值。平滑因子为 0 等同于不平滑。

有关平滑的详细信息，请参阅 Smoothing。

**可调谐：** 是

#### 依赖关系

要启用此参数，请选择 **Smooth tuned filter parameters** 参数。

### **Specify peak gain from input port** — 使用附加输入端口指定增益 `off`（默认）| `on`

选择此参数后，模块中会添加一个附加输入端口 **G**。使用此端口指定滤波器的增益。

### **Peak gain (dB)** — 峰值增益 (dB) `0`（默认）| 实数标量

滤波器的峰值增益，以 dB 为单位，指定为实数标量。增益指定滤波器对输入信号频谱的提升量（如果增益为正）或衰减量（如果增益为负）。

**可调谐：** 是

#### 依赖关系

要启用此参数，请清除 **Specify peak gain from input port** 参数。

### **Specify slope coefficient from input port** — 使用附加输入端口指定斜率系数 `off`（默认）| `on`

选择此参数后，模块中会添加一个附加输入端口 **S**。使用此端口指定滤波器的斜率。

### **Slope coefficient** — 斜率系数 `1.5`（默认）| 正标量

滤波器的斜率系数，指定为正标量。斜率控制滤波器响应中过渡带的宽度。

**可调谐：** 是

#### 依赖关系

要启用此参数，请清除 **Specify slope coefficient from input port** 参数。

### **Specify normalized cutoff frequency from input port** — 使用附加输入端口指定归一化截止频率 `off`（默认）| `on`

选择此参数后，模块中会添加一个附加输入端口 **Fc**。

### **Normalized cutoff frequency** — 归一化截止频率 `0.1`（默认）| [0,1] 范围内的标量

滤波器的归一化截止频率，指定为 [0,1] 范围内的标量，其中 1 对应奈奎斯特频率。截止频率指定滤波器峰值增益一半处的频率，即 *G*/2 dB，其中 *G* 是峰值增益。

**可调谐：** 是

#### 依赖关系

要启用此参数，请清除 **Specify normalized cutoff frequency from input port** 参数。

### **Specify filter type from input port** — 使用附加输入端口指定滤波器类型 `off`（默认）| `on`

选择此参数后，模块中会添加一个附加输入端口 **T**。

### **Filter type** — 架式均衡器的类型 `low`（默认）| `high`

架式均衡器的类型，指定为 `low` 表示低架均衡器，或 `high` 表示高架均衡器。

- 低架均衡器提升或衰减截止频率以下的频谱。
- 高架均衡器提升或衰减截止频率以上的频谱。

### **Output data type** — 输出系数的数据类型 `double`（默认）| `single`

输出系数的数据类型，指定为 `double` 或 `single`。

### **Sample time** — 模块的采样时间 `-1`（默认）| 正标量

模块的采样时间，以秒为单位，指定为 `-1` 或正标量。将此参数设置为 `-1` 表示 Simulink 会自动为您确定采样时间。您可以设置此参数以使设计模块以比滤波模块更慢的速率运行。

### **Simulate using** — 指定要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

- `Interpreted execution` —— 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但仿真速度比 `Code generation` 慢。在此模式下，您可以调试模块的源代码。
- `Code generation` —— 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为模块生成 C 代码。只要模型不更改，C 代码就会在后续仿真中重用。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。

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

设计可调谐架式均衡器系数

Shelving Equalizer Design 模块设计具有指定增益、斜率和截止频率的架式均衡器。您可以选择设计低架或高架均衡器。该模块输出二阶节 (SOS) 滤波器的系数，您可以将其与 Second-Order Section Filter 模块一起使用来对音频信号进行滤波。您可以在仿真期间调谐滤波器参数。
