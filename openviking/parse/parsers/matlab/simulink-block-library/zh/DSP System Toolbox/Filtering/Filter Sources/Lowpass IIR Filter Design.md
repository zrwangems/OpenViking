---
type: simulink-block
title: 'Lowpass IIR Filter Design'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Filter Designs'
documentation_page: 'lowpassiirfilterdesign'
documentation_source_path: 'ref/lowpassiirfilterdesign.html'
language: zh-CN
chinese_source: worker-translation
---

# Lowpass IIR Filter Design

## 端口
```yaml
ports:
- name: N
  summary: 滤波器阶数 正整数
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64
- name: Fc
  summary: 3-dB 截止频率 正标量 ≤ 1
  direction: input
  data_types: single | double
- name: Ap
  summary: 通带波纹（dB） 正标量
  direction: input
  data_types: single | double
- name: Ast
  summary: 阻带衰减（dB） 正标量
  direction: input
  data_types: single | double
- name: Num
  summary: 分子系数 *P*×3 矩阵
  direction: output
  data_types: single | double
- name: Den
  summary: 分母系数 *P*×3 矩阵
  direction: output
  data_types: single | double
- name: g
  summary: 每个二阶节的缩放值 向量
  direction: output
  data_types: single | double
```

### 输入

### **N** — 滤波器阶数 正整数

将滤波器阶数指定为正整数。您可以在仿真期间更改通过此端口输入的滤波器阶数。

#### 依赖关系

要启用此端口，请选择 **Specify filter order from input port** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Fc** — 3-dB 截止频率 正标量 ≤ 1

以归一化频率单位将滤波器的 3-dB 截止频率指定为小于或等于 `1` 的正标量。您可以在仿真期间更改通过此端口输入的 3-dB 截止频率。

#### 依赖关系

要启用此端口，请选择 **Specify 3-dB cutoff frequency from input port** 参数。

**数据类型：** `single` | `double`

### **Ap** — 通带波纹（dB） 正标量

以 dB 为单位将 Chebyshev Type I 滤波器的通带波纹指定为正标量。您可以在仿真期间更改通过此端口输入的通带波纹。

#### 依赖关系

要启用此端口：

- 将 **Design method** 参数设置为 `Chebyshev Type I`。
- 选择 **Specify the passband ripple from input port** 参数。

**数据类型：** `single` | `double`

### **Ast** — 阻带衰减（dB） 正标量

以 dB 为单位将 Chebyshev Type II 滤波器的阻带衰减指定为正标量。您可以在仿真期间更改通过此端口输入的阻带衰减。

#### 依赖关系

要启用此端口：

- 将 **Design method** 参数设置为 `Chebyshev Type II`。
- 选择 **Specify the stopband attenuation from input port** 参数。

**数据类型：** `single` | `double`
### 输出

### **Num** — 分子系数 *P*×3 矩阵

分子系数，以 *P*×3 矩阵（SOS 形式）返回，其中 *P* 是滤波器节的最大数量。

b=[b01b11b21b02b12b22⋮⋮⋮b0Pb1Pb2P]

此方程以传递函数形式表示 SOS 滤波器。

H(z)=∏k=1PHk(z)=∏k=1Pb0k+b1kz−1+b2kz−2a0k+a1kz−1+a2kz−2,

其中

- **b** 是分子系数矩阵。
- **a** 是分母系数矩阵，模块在 **Den** 输出端口输出该矩阵。
- *k* 是行索引。

*P* 等于 `ceil`(*Nmax*/2)，其中 *Nmax* 是 **Filter maximum order** 参数的值。

当实际滤波器阶数 *N* 小于最大滤波器阶数 *Nmax* 时，最后 `ceil`(*Nmax*/2) − `ceil`(*N*/2) 节为平凡节，其系数为 [*b*0, *b*1, *b*2] = [1, 0, 0]。

当实际滤波器阶数 *N* 为奇数时，最后一个非平凡滤波器节的系数为 [*b*0, *b*1, 0] = [1, 1, 0]。

此端口的数据类型取决于 **Output data type** 参数的值。

**数据类型：** `single` | `double`

### **Den** — 分母系数 *P*×3 矩阵

分母系数，以 *P*×3 矩阵（SOS 形式）返回，其中 *P* 是滤波器节的最大数量。

a=[a01a11a21a02a12a22⋮⋮⋮a0Pa1Pa2P]

此方程以传递函数形式表示 SOS 滤波器。

H(z)=∏k=1PHk(z)=∏k=1Pb0k+b1kz−1+b2kz−2a0k+a1kz−1+a2kz−2,

其中

- **a** 是分母系数矩阵，且首项分母系数 *a*0 始终为 1。
- **b** 是分子系数矩阵，模块在 **Num** 端口输出该矩阵。
- *k* 是行索引。

*P* 等于 `ceil`(*Nmax*/2)，其中 *Nmax* 是 **Filter maximum order** 参数的值。

当实际滤波器阶数 *N* 小于最大滤波器阶数 *Nmax* 时，最后 `ceil`(*Nmax*/2) − `ceil`(*N*/2) 节为平凡节，其系数为 [*a*0, *a*1, *a*2] = [1, 0, 0]。

当实际滤波器阶数 *N* 为奇数时，最后一个非平凡滤波器节的系数为 [1, *a*1, 0] = [1, 1, 0]。

此端口的数据类型取决于 **Output data type** 参数的值。

**数据类型：** `single` | `double`

### **g** — 每个二阶节的缩放值 向量

每个二阶节的缩放值，以包含 *P* + 1 个元素的向量返回，其中 *P* 是滤波器节的最大数量，等于 `ceil`(*Nmax*/2)，其中 *Nmax* 是 **Filter maximum order** 参数的值。

**可调：** 是

#### 依赖关系

要启用此端口，请选择 **Design has scale values** 参数。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Smooth tuned filter parameters
  summary: 平滑可调滤波器参数 off（默认）| on
  group: ''
- name: Smoothing factor
  summary: 平滑因子 0.6（默认）| 小于 1 的非负标量
  group: ''
- name: Design method
  summary: 滤波器设计方法 Butterworth（默认）| Chebyshev Type I | Chebyshev Type II
  group: ''
- name: Specify filter order from input port
  summary: 从输入端口指定滤波器阶数的标志 off（默认）| on
  group: ''
- name: Filter order
  summary: 滤波器阶数 6（默认）| 正整数
  group: ''
- name: Filter maximum order
  summary: 滤波器最大阶数 10（默认）| 正整数
  group: ''
- name: Design has scale values
  summary: 指定滤波器是否为每个节具有缩放值 off（默认）| on
  group: ''
- name: Specify 3-dB cutoff frequency from input port
  summary: 从输入端口指定 3-dB 截止频率的标志 off（默认）| on
  group: ''
- name: 3-dB cutoff frequency
  summary: 3-dB 截止频率 0.25（默认）| 正标量 ≤ 1
  group: ''
- name: Specify the passband ripple from input port
  summary: 从输入端口指定通带波纹的标志 off（默认）| on
  group: ''
- name: Passband ripple (dB)
  summary: 通带波纹（dB） 1（默认）| 正标量
  group: ''
- name: Specify the stopband attenuation from input port
  summary: 从输入端口指定阻带衰减的标志 off（默认）| on
  group: ''
- name: Stopband attenuation (dB)
  summary: 阻带衰减（dB） 60（默认）| 正标量
  group: ''
- name: Sample time
  summary: 采样时间（秒） -1（默认）| 正标量 | Inf
  group: ''
- name: Output data type
  summary: 滤波器系数的数据类型 double（默认）| single
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Interpreted execution（默认）| Code generation
  group: ''
```

### **Smooth tuned filter parameters** — 平滑可调滤波器参数 `off`（默认）| `on`

*自 R2024a 起*

当您选中此复选框时，模块通过使用参数的中间值反复设计滤波器，直到参数达到所需值，从而逐步更新可调滤波器参数，如滤波器阶数、截止频率、通带波纹和阻带衰减。此过程称为参数平滑。有关详细信息，请参阅 Parameter Smoothing。

当您清除此复选框时，模块立即使用新参数值重新设计滤波器。

### **Smoothing factor** — 平滑因子 0.6（默认）| 小于 1 的非负标量

*自 R2024a 起*

将平滑因子 *α* 指定为小于 1 的非负标量。当 *α* = 0 时，不发生平滑。当 *α* 趋近于 1 时，平滑操作次数以及随之而来的滤波器重新设计次数增加。

**可调：** 是

#### 依赖关系

要启用此参数，请选择 **Smooth tuned filter parameters** 参数。

### **Design method** — 滤波器设计方法 `Butterworth`（默认）| `Chebyshev Type I` | `Chebyshev Type II`

将滤波器设计方法指定为以下之一：

- `Butterworth`
- `Chebyshev Type I`
- `Chebyshev Type II`

### **Specify filter order from input port** — 从输入端口指定滤波器阶数的标志 `off`（默认）| `on`

选择此参数以从输入端口 **N** 指定滤波器阶数。当您清除此参数时，可以使用 **Filter order** 参数在模块对话框中指定滤波器阶数。

### **Filter order** — 滤波器阶数 `6`（默认）| 正整数

将滤波器阶数指定为小于或等于 **Filter maximum order** 参数值的正整数。

**可调：** 是

#### 依赖关系

要启用此参数，请清除 **Specify filter order from input port** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Filter maximum order** — 滤波器最大阶数 `10`（默认）| 正整数

将滤波器的最大阶数指定为正整数。您在 **Filter order** 参数中指定的值必须小于或等于您在 **Filter maximum order** 参数中指定的值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Design has scale values** — 指定滤波器是否为每个节具有缩放值 `off`（默认）| `on`

指定滤波器是否为每个节具有缩放值。当您选择此参数时，模块通过 **g** 输出端口输出缩放值。

### **Specify 3-dB cutoff frequency from input port** — 从输入端口指定 3-dB 截止频率的标志 `off`（默认）| `on`

选择此参数以从输入端口 **Fc** 指定 3-dB 滤波器截止频率。当您清除此参数时，可以使用 **3-dB cutoff frequency** 参数在模块对话框中指定截止频率。

### **3-dB cutoff frequency** — 3-dB 截止频率 `0.25`（默认）| 正标量 ≤ 1

以归一化频率单位将滤波器的 3-dB 截止频率指定为小于或等于 `1` 的正标量。

**可调：** 是

#### 依赖关系

要启用此参数，请清除 **Specify 3-dB cutoff frequency from input port** 参数。

**数据类型：** `single` | `double`

### **Specify the passband ripple from input port** — 从输入端口指定通带波纹的标志 `off`（默认）| `on`

选择此参数以从输入端口 **Ap** 指定通带波纹。当您清除此参数时，可以使用 **Passband ripple (dB)** 参数在模块对话框中指定通带波纹。

#### 依赖关系

要启用此参数，请将 **Design method** 参数设置为 `Chebyshev Type I`。

### **Passband ripple (dB)** — 通带波纹（dB） `1`（默认）| 正标量

以 dB 为单位将 Chebyshev Type I 滤波器的通带波纹指定为正标量。

**可调：** 是

#### 依赖关系

要启用此参数：

- 将 **Design method** 参数设置为 `Chebyshev Type I`。
- 清除 **Specify the passband ripple from input port** 参数。

**数据类型：** `single` | `double`

### **Specify the stopband attenuation from input port** — 从输入端口指定阻带衰减的标志 `off`（默认）| `on`

选择此参数以从输入端口 **Ast** 指定阻带衰减。当您清除此参数时，可以使用 **Stopband attenuation (dB)** 参数在模块对话框中指定阻带衰减。

#### 依赖关系

要启用此参数，请将 **Design method** 参数设置为 `Chebyshev Type II`。

### **Stopband attenuation (dB)** — 阻带衰减（dB） `60`（默认）| 正标量

以 dB 为单位将 Chebyshev Type II 滤波器的阻带衰减指定为正标量。

**可调：** 是

#### 依赖关系

要启用此参数：

- 将 **Design method** 参数设置为 `Chebyshev Type II`。
- 清除 **Specify the stopband attenuation from input port** 参数。

**数据类型：** `single` | `double`

### **Sample time** — 采样时间（秒） `-1`（默认）| 正标量 | `Inf`

将采样时间指定为 `-1`（继承）、`Inf`（常量采样时间）或正标量。此参数确定模块在仿真期间何时产生输出并更新其内部状态。有关更多详细信息，请参阅 What Is Sample Time? (Simulink)。

**数据类型：** `single` | `double`

### **Output data type** — 滤波器系数的数据类型 `double`（默认）| `single`

指定模块通过 **Num** 和 **Den** 端口输出的滤波器系数的数据类型。您可以将数据类型设置为 `double` 或 `single`。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` —— 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` —— 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，C 代码将在后续仿真中重用。此选项需要额外的启动时间，但可提供更快的后续仿真。
## 所属库

DSP System Toolbox / Filtering / Filter Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

从此模块生成代码时，您可以在生成的代码中调整滤波器设计规格。

## 版本历史

**在 R2023b 中引入**

### R2024a：**Simulate using** 参数默认值变更

**Simulate using** 参数的默认值现在为 `Interpreted execution`。通过此变更，模块默认使用 MATLAB 解释器进行仿真。

### R2024a：Tunable Lowpass IIR Filter 模块已重命名

Tunable Lowpass IIR Filter 已重命名为 Lowpass IIR Filter Design 模块。

### R2024a：支持平滑可调滤波器参数

当可调滤波器参数（如滤波器阶数、截止频率、通带波纹和阻带衰减）在仿真期间发生变化时，模块可以平滑这些参数，直到参数达到所需值。有关详细信息，请参阅 Parameter Smoothing。

## 描述

设计具有可调滤波器规格的低通 IIR 滤波器

使用 Lowpass IIR Filter Design 模块，通过 Butterworth、Chebyshev Type I 和 Chebyshev Type II 设计方法设计低通 IIR 滤波器。您可以在仿真期间调整滤波器设计规格，如滤波器阶数、3-dB 截止频率、通带波纹和阻带衰减。当这些参数的值发生变化时，模块会重新设计滤波器，并以二阶节（SOS）形式输出分子和分母系数。
