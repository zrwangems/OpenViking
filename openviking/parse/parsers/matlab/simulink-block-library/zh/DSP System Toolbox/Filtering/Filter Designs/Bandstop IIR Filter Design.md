---
type: simulink-block
title: 'Bandstop IIR Filter Design'
family: 'filtering'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Filter Designs'
documentation_page: 'bandstopiirfilterdesign'
documentation_source_path: 'ref/bandstopiirfilterdesign.html'
language: zh-CN
chinese_source: worker-translation
---

# Bandstop IIR Filter Design

## 端口

### 输入

### **N** — 滤波器阶数，偶数正整数

将滤波器阶数指定为偶数正整数。您可以在仿真期间更改通过此端口输入的滤波器阶数。

#### 依赖项

要启用此端口，请选择 **Specify filter order from input port** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Fc1** — 第一个 3-dB 截止频率，非负标量 ≤ **Fc2**

以归一化频率单位指定滤波器的第一个 3-dB 截止频率 **Fc1**，为非负标量且小于或等于第二个 3-dB 截止频率 **Fc2**。

您可以在仿真期间更改通过此端口输入的第一个 3-dB 截止频率。

#### 依赖项

要启用此端口，请选择 **Specify first 3-dB cutoff frequency from input port** 参数。

**数据类型：** `single` | `double`

### **Fc2** — 第二个 3-dB 截止频率 **Fc1** ≤ 正标量 ≤ `1`

以归一化频率单位指定滤波器的第二个 3-dB 截止频率，为正标量且大于或等于 **Fc1** 并且小于或等于 `1`。

您可以在仿真期间更改通过此端口输入的第二个 3-dB 截止频率。

#### 依赖项

要启用此端口，请选择 **Specify second 3-dB cutoff frequency from input port** 参数。

**数据类型：** `single` | `double`

### **Ap** — 通带波纹，以 dB 计，非负标量

将 Chebyshev Type I 滤波器的通带波纹指定为非负标量，以 dB 计。您可以在仿真期间更改通过此端口输入的通带波纹。

#### 依赖项

要启用此端口：

- 将 **Design method** 参数设置为 `Chebyshev Type I`。
- 选择 **Specify the passband ripple from input port** 参数。

**数据类型：** `single` | `double`

### **Ast** — 阻带衰减，以 dB 计，非负标量

将 Chebyshev Type II 滤波器的阻带衰减指定为非负标量，以 dB 计。您可以在仿真期间更改通过此端口输入的阻带衰减。

#### 依赖项

要启用此端口：

- 将 **Design method** 参数设置为 `Chebyshev Type II`。
- 选择 **Specify the stopband attenuation from input port** 参数。

**数据类型：** `single` | `double`
### 输出

### **Num** — 分子系数，*P*×3 矩阵 | *P*×5 矩阵

分子系数，以 *P*×3 矩阵（SOS 形式）或 *P*×5 矩阵（FOS 形式）返回，其中 *P* 是滤波器节的最大数量。

**SOS 形式** *(自 R2023b 起)*

当您将 **Filter cascade sections form** 设置为 `Second-order sections` 时，该模块生成 *P*×3 分子系数矩阵。

b=[b01b11b21b02b12b22⋮⋮⋮b0Pb1Pb2P]

此方程以传递函数形式表示 SOS 滤波器。

H(z)=∏k=1PHk(z)=∏k=1Pb0k+b1kz−1+b2kz−2a0k+a1kz−1+a2kz−2,

其中

- **b** 是分子系数矩阵。
- **a** 是分母系数矩阵，该模块在 **Den** 输出端口输出该矩阵。
- *k* 是行索引。

在 SOS 形式中，*P* 等于 `ceil`(*Nmax*/2)，其中 *Nmax* 是 **Filter maximum order (must be even)** 参数的值。

当实际滤波器阶数 *N* 小于最大滤波器阶数 *Nmax* 时，最后 `ceil`(*Nmax*/2) − `ceil`(*N*/2) 个节是平凡节，其系数为 [*b*0, *b*1, *b*2] = [1, 0, 0]。

**FOS 形式**

当您将 **Filter cascade sections form** 设置为 `Fourth-order sections` 时，该模块生成 *P*×5 分子系数矩阵。

b=[b01b11b21b31b41b02b12b22b32b42⋮⋮⋮⋱⋮b0Pb1Pb2Pb3Pb4P]

此方程以传递函数形式表示 FOS 滤波器。

H(z)=∏k=1PHk(z)=∏k=1Pb0k+b1kz−1+b2kz−2+b3kz−3+b4kz−4a0k+a1kz−1+a2kz−2+a3kz−3+a4kz−4

在 FOS 形式中，*P* 等于 `ceil`(*Nmax*/4)。

当实际滤波器阶数 *N* 小于最大滤波器阶数 *Nmax* 时，最后 `ceil`(*Nmax*/4) − `ceil`(*N*/4) 个节是平凡节，其系数为 [*b*0, *b*1, *b*2, *b*3, *b*4] = [1, 0, 0, 0, 0]。

此端口的数据类型取决于 **Output data type** 参数的值。

**数据类型：** `single` | `double`

### **Den** — 分母系数，*P*×5 矩阵

分母系数，以 *P*×3 矩阵（SOS 形式）或 *P*×5 矩阵（FOS 形式）返回，其中 *P* 是滤波器节的最大数量。

**SOS 形式** *(自 R2023b 起)*

当您将 **Filter cascade sections form** 设置为 `Second-order sections` 时，该模块生成 *P*×3 分母系数矩阵。

a=[a01a11a21a02a12a22⋮⋮⋮a0Pa1Pa2P]

此方程以传递函数形式表示 SOS 滤波器。

H(z)=∏k=1PHk(z)=∏k=1Pb0k+b1kz−1+b2kz−2a0k+a1kz−1+a2kz−2,

其中

- **a** 是分母系数矩阵，并且前导分母系数 *a*0 始终为 1。
- **b** 是分子系数矩阵，该模块在 **Num** 端口输出该矩阵。
- *k* 是行索引。

在 SOS 形式中，*P* 等于 `ceil`(*Nmax*/2)，其中 *Nmax* 是 **Filter maximum order (must be even)** 参数的值。

当实际滤波器阶数 *N* 小于最大滤波器阶数 *Nmax* 时，最后 `ceil`(*Nmax*/2) − `ceil`(*N*/2) 个节是平凡节，其系数为 [*a*0, *a*1, *a*2] = [1, 0, 0]。

**FOS 形式**

当您将 **Filter cascade sections form** 设置为 `Fourth-order sections` 时，该模块生成 *P*×5 分母系数矩阵。

a=[a01a11a21a31a41a02a12a22a32a42⋮⋮⋮⋱⋮a0Pa1Pa2Pa3Pa4P]

此方程以传递函数形式表示 FOS 滤波器。

H(z)=∏k=1PHk(z)=∏k=1Pb0k+b1kz−1+b2kz−2+b3kz−3+b4kz−4a0k+a1kz−1+a2kz−2+a3kz−3+a4kz−4

在 FOS 形式中，*P* 等于 `ceil`(*Nmax*/4)。

前导分母系数 *a*0 始终为 1。

当实际滤波器阶数 *N* 小于最大滤波器阶数 *Nmax* 时，最后 `ceil`(*Nmax*/4) − `ceil`(*N*/4) 个节是平凡节，其系数为 [*a*0, *a*1, *a*2, *a*3, *a*4] = [1, 0, 0, 0, 0]。

此端口的数据类型取决于 **Output data type** 参数的值。

**数据类型：** `single` | `double`

### **g** — 每个二阶节的缩放值，向量

*自 R2023b 起*

每个二阶节的缩放值，以包含 *P* + 1 个元素的向量返回，其中 *P* 是滤波器节的最大数量，等于 `ceil`(*Nmax*/2)，其中 *Nmax* 是 **Filter maximum order (must be even)** 参数的值。

**可调：** 是

#### 依赖项

要启用此端口：

- 将 **Filter cascade sections form** 设置为 `Second-order sections`。
- 选择 **Design has scale values** 参数。

**数据类型：** `single` | `double`

## 参数

### **Smooth tuned filter parameters** — 平滑可调滤波器参数 `off`（默认） | `on`

*自 R2024a 起*

当您选中此复选框时，该模块通过使用中间参数值反复设计滤波器，逐步更新可调滤波器参数（如滤波器阶数、截止频率、通带波纹和阻带衰减），直到参数达到所需值。此过程称为参数平滑。有关详细信息，请参阅 Parameter Smoothing。

当您清除此复选框时，该模块立即使用新参数值重新设计滤波器。

### **Smoothing factor** — 平滑因子 `0.6`（默认） | 小于 1 的非负标量

*自 R2024a 起*

将平滑因子 *α* 指定为小于 1 的非负标量。当 *α* = 0 时，不发生平滑。随着 *α* 接近 1，平滑操作的数量以及因此滤波器重新设计的数量会增加。

**可调：** 是

#### 依赖项

要启用此参数，请选择 **Smooth tuned filter parameters** 参数。

### **Design method** — 滤波器设计方法 `Butterworth`（默认） | `Chebyshev Type I` | `Chebyshev Type II`

将滤波器设计方法指定为以下之一：

- `Butterworth`
- `Chebyshev Type I`
- `Chebyshev Type II`

### **Specify filter order from input port** — 从输入端口指定滤波器阶数的标志 `off`（默认） | `on`

选择此参数以从输入端口 **N** 指定滤波器阶数。当您清除此参数时，您可以在模块对话框中使用 **Filter order (must be even)** 参数指定滤波器阶数。

### **Filter order (must be even)** — 滤波器阶数 `6`（默认） | 偶数正整数

将滤波器阶数指定为小于或等于 **Filter maximum order (must be even)** 参数值的偶数正整数。

**可调：** 是

#### 依赖项

要启用此参数，请清除 **Specify filter order from input port** 参数。

### **Filter maximum order (must be even)** — 滤波器最大阶数 `10`（默认） | 偶数正整数

将滤波器的最大阶数指定为偶数正整数。您在 **Filter order (must be even)** 参数中指定的值必须小于或等于您在 **Filter maximum order (must be even)** 参数中指定的值。

### **Design has scale values** — 指定滤波器是否为每个节具有缩放值 `off`（默认） | `on`

*自 R2023b 起*

指定滤波器是否为每个节具有缩放值。当您选择此参数时，该模块通过 **g** 输出端口输出缩放值。

#### 依赖项

要启用此参数，请将 **Filter cascade sections form** 设置为 `Second-order sections`。

### **Specify first 3-dB cutoff frequency from input port** — 从输入端口指定第一个 3-dB 截止频率的标志 `off`（默认） | `on`

选择此参数以从输入端口 **Fc1** 指定第一个 3-dB 滤波器截止频率。当您清除此参数时，您可以在模块对话框中使用 **First 3-dB cutoff frequency** 参数指定第一个 3-dB 截止频率。

### **First 3-dB cutoff frequency** — 第一个 3-dB 截止频率 `0.25`（默认） | 正标量

以归一化频率单位将滤波器的第一个 3-dB 截止频率指定为小于或等于第二个 3-dB 截止频率的正标量。

**可调：** 是

#### 依赖项

要启用此参数，请清除 **Specify first 3-dB cutoff frequency from input port** 参数。

### **Specify second 3-dB cutoff frequency from input port** — 从输入端口指定第二个 3-dB 截止频率的标志 `off`（默认） | `on`

选择此参数以从输入端口 **Fc2** 指定第二个 3-dB 滤波器截止频率。当您清除此参数时，您可以在模块对话框中使用 **Second 3-dB cutoff frequency** 参数指定第二个 3-dB 截止频率。

### **Second 3-dB cutoff frequency** — 第二个 3-dB 截止频率 `0.75`（默认） | 正标量

以归一化频率单位将滤波器的第二个 3-dB 截止频率指定为大于或等于第一个 3-dB 截止频率且小于或等于 `1` 的正标量。

**可调：** 是

#### 依赖项

要启用此参数，请清除 **Specify second 3-dB cutoff frequency from input port** 参数。

### **Specify the passband ripple from input port** — 从输入端口指定通带波纹的标志 `off`（默认） | `on`

选择此参数以从输入端口 **Ap** 指定通带波纹。当您清除此参数时，您可以在模块对话框中使用 **Passband ripple (dB)** 参数指定通带波纹。

#### 依赖项

要启用此参数，请将 **Design method** 参数设置为 `Chebyshev Type I`。

### **Passband ripple (dB)** — 通带波纹，以 dB 计 `1`（默认） | 正标量

将 Chebyshev Type I 滤波器的通带波纹指定为正标量，以 dB 计。

**可调：** 是

#### 依赖项

要启用此参数：

- 将 **Design method** 参数设置为 `Chebyshev Type I`。
- 清除 **Specify the passband ripple from input port** 参数。

### **Specify the stopband attenuation from input port** — 从输入端口指定阻带衰减的标志 `off`（默认） | `on`

选择此参数以从输入端口 **Ast** 指定阻带衰减。当您清除此参数时，您可以在模块对话框中使用 **Stopband attenuation (dB)** 参数指定阻带衰减。

#### 依赖项

要启用此参数，请将 **Design method** 参数设置为 `Chebyshev Type II`。

### **Stopband attenuation (dB)** — 阻带衰减，以 dB 计 `60`（默认） | 正标量

将 Chebyshev Type II 滤波器的阻带衰减指定为正标量，以 dB 计。

**可调：** 是

#### 依赖项

要启用此参数：

- 将 **Design method** 参数设置为 `Chebyshev Type II`。
- 清除 **Specify the stopband attenuation from input port** 参数。

### **Sample time** — 采样时间（seconds） `-1`（默认） | 正标量 | `Inf`

将采样时间指定为 `-1`（继承）、`Inf`（常量采样时间）或正标量。此参数决定模块在仿真期间何时产生输出并更新其内部状态。有关更多详细信息，请参阅 What Is Sample Time? (Simulink)。

### **Filter cascade sections form** — 滤波器级联节的形式 `Fourth-order sections`（默认） | `Second-order sections`

*自 R2023b 起*

将滤波器级联节的形式指定为以下之一：

- `Fourth-order sections` –– 该模块生成 *P*×5 滤波器系数矩阵。
- `Second-order sections` –– 该模块生成 *P*×3 滤波器系数矩阵。

### **Output data type** — 滤波器系数的数据类型 `double`（默认） | `single`

指定该模块通过 **Num** 和 **Den** 端口输出的滤波器系数的数据类型。您可以将数据类型设置为 `double` 或 `single`。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认） | `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` –– 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` –– 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，C 代码就会在后续仿真中重用。此选项需要额外的启动时间，但可提供更快的后续仿真。

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

**R2023a 中引入**

### R2024a：**Simulate using** 参数默认值的更改

**Simulate using** 参数的默认值现在为 `Interpreted execution`。通过此更改，该模块默认使用 MATLAB 解释器进行仿真。

### R2024a：Tunable Bandstop IIR Filter 模块已重命名

Tunable Bandstop IIR Filter 已重命名为 Bandstop IIR Filter Design 模块。

### R2024a：支持平滑可调滤波器参数

当可调滤波器参数（如滤波器阶数、截止频率、通带波纹和阻带衰减）在仿真期间发生变化时，该模块可以平滑这些参数，直到参数达到所需值。有关详细信息，请参阅 Parameter Smoothing。

### R2023b：Tunable Bandstop IIR Filter 模块以二阶节形式生成系数

从 R2023b 开始，Tunable Bandstop IIR Filter 模块以 SOS 或 FOS 形式生成滤波器系数。您可以使用新的 **Filter cascade sections form** 参数指定该形式。

当您将 **Filter cascade sections form** 设置为 `Second-order sections` 并选择 **Design has scale values** 时，该模块通过 **g** 端口输出缩放值。

## 描述

设计具有可调滤波器规格的带阻 IIR 滤波器

使用 Bandstop IIR Filter Design 模块，通过 Butterworth、Chebyshev Type I 和 Chebyshev Type II 设计方法设计带阻 IIR 滤波器。您可以在仿真期间调整滤波器设计规格，如滤波器阶数、3-dB 截止频率、通带波纹和阻带衰减。当这些参数的值发生变化时，该模块会重新设计滤波器，并以二阶节 (SOS) 形式 *(自 R2023b 起)* 或四阶节 (FOS) 形式输出分子和分母系数。
