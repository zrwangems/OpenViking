---
type: simulink-block
title: 'Variable FIR Decimation'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Multirate Filters'
documentation_page: 'variablefirdecimation'
documentation_source_path: 'ref/variablefirdecimation.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable FIR Decimation

## 端口

### 输入

### **u** — 数据输入 向量 | 矩阵

将数据输入指定为大小为 *P*×*Q* 的向量或矩阵。该模块将输入信号的每一列视为一个独立通道。如果输入是二维信号，第一维表示通道长度（或帧大小），第二维表示通道数。如果输入是一维信号，则该模块将其解释为单通道。

该模块接受可变大小输入信号，即您可以在仿真期间更改每个输入通道的大小，但不能更改通道数。

当您将 **Specification** 设置为 `Output frame length` 时，输入帧长度 *P* 必须是输出帧长度 *Po* 的整数倍。*(自 R2023b 起)*

**数据类型：** `single` | `double`
**复数支持：** 是

### **M** — 抽取因子输入端口 正整数

将抽取因子 *M* 指定为最大抽取因子的整数因子的正整数。例如，如果您将 **Maximum decimation factor** 设置为 24，则抽取因子的可能值为 1、2、3、4、6、8、12 和 24。

您可以在仿真运行时调整抽取因子。有关示例，请参阅 Decimate Sinusoidal Signal with Tunable Decimation Factor。

#### 依赖关系

要启用此端口：

- 将 **Specification** 设置为 `Decimation factor`。*(自 R2023b 起)*
- 选中 **Specify decimation factor from input port** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **coeffs** — 原型滤波器系数 向量

将低通 FIR 滤波器系数按 *z* 的降幂指定为向量。

FIR 滤波器的传递函数 *H*(*z*) 由下式给出：

H(z)=b0+b1z−1+...+bNz−N，

您可以使用 DSP System Toolbox™ 滤波器设计函数（如 `designMultirateFIR`、`firnyquist`、`firgr` 或 `firceqrip`）之一生成 FIR 滤波器系数向量 **b** = [*b0*, *b1*, …, *bN*]。

基于最大抽取因子 *Mmax* 而非抽取因子 *M* 计算滤波器系数。例如，如果 *Mmax* 为 24，*M* 为 8，并且您使用 `designMultirateFIR` 作为设计函数，则使用 `designMultirateFIR(1,24)` 而非 `designMultirateFIR(1,8)` 计算滤波器系数。

为了充当有效的抗混叠滤波器，系数通常对应于归一化截止频率不大于 1/*Mmax* 的低通滤波器。要设计此类滤波器，请使用 `designMultirateFIR` 函数。

该模块在内部将所有滤波器状态初始化为零。

您可以在仿真期间更改滤波器系数，但滤波器系数的数量必须保持不变。有关示例，请参阅 Specify Filter Coefficients Through Input Port。

#### 依赖关系

要启用此端口，请将 **Numerator source** 参数设置为 `Input port`。

**数据类型：** `single` | `double`
**复数支持：** 是
### 输出

### **y** — 抽取输出 向量 | 矩阵

抽取输出，以向量或矩阵形式返回。

当您将 **Specification** 参数设置为 `Decimation factor` *(自 R2023b 起)* 时，输出信号的大小与输入信号的大小相同。但是，该模块最多计算 `ceil`(*P*/*M*)×*Q* 个输出样本，其中 *P* 是输入帧大小，*Q* 是输入通道数，*M* 是抽取因子。

如果输入是可变大小信号，则该模块输出可变大小信号以保持抽取因子。

当您将 **Specification** 参数设置为 `Output frame length` 时，输出信号的大小为 *Po*×*Q*，其中 *Po* 是您在 **Output frame length** 参数中指定的值。*(自 R2023b 起)*

如果输入是可变大小信号，则该模块相应地改变抽取因子并输出固定大小信号。*(自 R2023b 起)*

输出信号的复杂度取决于输入信号的复杂度和滤波器系数的复杂度。有关更多详细信息，请参阅此表。

| 输入信号 | 滤波器系数 | 输出信号 |
| --- | --- | --- |
| 实数 | 复数 | 复数 |
| 实数 | 实数 | 实数 |
| 复数 | 复数 | 复数 |
| 复数 | 实数 | 复数 |

**数据类型：** `single` | `double`
**复数支持：** 是

## 参数

### **Specification** — 指定控制抽取因子的模式 `Decimation factor`（默认）| `Output frame length`

*自 R2023b 起*

指定控制抽取因子的模式。

当您将 **Specification** 设置为：

- `Decimation factor` —— 该模块保持您指定的抽取因子。如果输入信号帧长度在仿真期间发生变化（可变大小输入信号），则输出帧长度以保持抽取因子 *M* 的方式变化。

  可变大小输入生成可变大小输出。
- `Output frame length` —— 该模块保持您指定的输出帧长度。如果输入信号帧长度在仿真期间发生变化（可变大小输入信号），则抽取因子以保持输出帧长度 *Po* 的方式变化。

  可变大小输入生成固定大小输出。

### **Maximum decimation factor** — 最大抽取因子 `24`（默认）| 正整数

将最大抽取因子 *Mmax* 指定为正整数。您通过输入端口 **M** 指定的抽取因子必须是您在此参数中指定的值的因子。

当您将 **Specification** 参数设置为 `Output frame length` 时，该模块将输入帧长度视为最大抽取因子 *Mmax*。*(自 R2023b 起)*

#### 依赖关系

要启用此端口，请将 **Specification** 参数设置为 `Decimation factor`。*(自 R2023b 起)*

### **Specify decimation factor from input port** — 从输入端口指定抽取因子 `on`（默认）| `off`

当您选中此参数时，您可以通过输入端口 **M** 指定抽取因子。当您清除此参数时，您可以在模块对话框中通过 **Decimation factor** 参数指定抽取因子。

#### 依赖关系

要启用此参数，请将 **Specification** 参数设置为 `Decimation factor`。*(自 R2023b 起)*

### **Decimation factor** — 抽取因子 `24`（默认）| 正整数

将抽取因子 *M* 指定为最大抽取因子 *Mmax* 的整数因子的正整数。例如，如果您将 **Maximum decimation factor** 设置为 24，则 **Decimation factor** 的可能值为 1、2、3、4、6、8、12 和 24。

您可以在仿真运行时调整抽取因子。

当您将 **Specification** 参数设置为 `Output frame length` 时，该模块将输入帧长度 *P* 与输出帧长度 *Po* 的比值视为抽取因子 *M*，即 *M* = *P*/*Po*。*(自 R2023b 起)*

**可调：** 是

#### 依赖关系

要启用此参数：

- 将 **Specification** 参数设置为 `Decimation factor`。*(自 R2023b 起)*
- 清除 **Specify decimation factor from input port** 参数。

### **Output frame length** — 输出帧长度 `48`（默认）| 正整数

*自 R2023b 起*

将输出帧长度 *Po* 指定为正整数。在此模式下，该模块将输出信号的帧长度保持为您在此参数中指定的值。如果输入信号帧长度在仿真期间发生变化（可变大小输入信号），则该模块的抽取因子以保持输出帧长度的方式变化。

输入帧长度必须是输出帧长度的整数倍。

您在此参数中指定的值决定当前抽取因子 *M*。有关更多详细信息，请参阅 **Decimation factor** 参数。

#### 依赖关系

要启用此参数，请将 **Specification** 参数设置为 `Output frame length`。

### **Numerator source** — FIR 滤波器系数来源 `Auto`（默认）| `Dialog parameter` | `Input port`

将 FIR 滤波器系数来源指定为以下之一：

- `Auto` —— 该模块使用 `designMultirateFIR` 函数设计 FIR 抽取器。此函数设计滤波器并返回该模块使用的系数。

  有关滤波器设计的更多信息，请参阅 Orfanidis [1]。
- `Dialog parameter` —— 通过模块对话框中的 **Prototype filter numerator coefficients** 参数指定滤波器系数。
- `Input port` —— 通过 **coeffs** 输入端口指定滤波器系数。

### **Prototype filter numerator coefficients** — 原型低通 FIR 滤波器系数 `designMultirateFIR(1,24)`（默认）| 向量

将原型低通 FIR 滤波器系数按 *z* 的降幂指定为向量。默认情况下，`designMultirateFIR(1,24)` 使用最大抽取因子 *Mmax* 为 24 计算滤波器系数。

FIR 滤波器的传递函数 *H*(*z*) 由下式给出：

H(z)=b0+b1z−1+...+bNz−N，

您可以使用 DSP System Toolbox 滤波器设计函数（如 `designMultirateFIR`、`firnyquist`、`firgr` 或 `firceqrip`）之一生成 FIR 滤波器系数向量 **b** = [*b0*, *b1*, …, *bN*]。

基于最大抽取因子 *Mmax* 而非抽取因子 *M* 计算滤波器系数。例如，如果 *Mmax* 为 24，*M* 为 8，并且您使用 `designMultirateFIR` 作为设计函数，则使用 `designMultirateFIR(1,24)` 而非 `designMultirateFIR(1,8)` 计算滤波器系数。

为了充当有效的抗混叠滤波器，系数通常对应于归一化截止频率不大于 1/*Mmax* 的低通滤波器。要设计此类滤波器，请使用 `designMultirateFIR` 函数。

该模块在内部将所有滤波器状态初始化为零。

#### 依赖关系

要启用此参数，请将 **Numerator source** 参数设置为 `Dialog parameter`。

**可调：** 是

### **View Filter Response** — 查看滤波器响应 按钮

点击此按钮可打开滤波器可视化器并显示可变 FIR 抽取滤波器的幅值响应。响应基于您在模块对话框中选择的参数。要在动态滤波器可视化器运行时更新幅值响应，请修改对话框中的参数并点击 **Apply**。

您可以从可视化器界面配置绘图设置和信号测量。

在 **Scope** 选项卡上，**Configuration** 部分允许您修改绘图设置。点击 **Magnitude Phase** 可显示滤波器的幅值和相位响应。在 **Measurements** 选项卡上，您可以测量信号统计量、放置数据光标并显示所选信号的峰值。

有关滤波器可视化器界面及其工具的更多详细信息，请参阅 Configure Filter Visualizer。

#### 依赖关系

当您将 **Specification** 参数设置为 `Output frame length` *(自 R2023b 起)* 或将 **Numerator source** 参数设置为 `Input port` 时，您无法查看滤波器响应。要查看滤波器响应，请将 **Specification** 参数设置为 `Decimation factor` *(自 R2023b 起)*，并将 **Numerator source** 参数设置为 `Auto` 或 `Dialog parameter`。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` —— 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` —— 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不更改，C 代码就会在后续仿真中重用。此选项需要额外的启动时间，但可提供更快的后续仿真。

## 所属库

DSP System Toolbox / Filtering / Multirate Filters

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

### R2024a：**Simulate using** 参数默认值变更

**Simulate using** 参数的默认值现在为 `Interpreted execution`。通过此更改，该模块默认使用 MATLAB 解释器进行仿真。

### R2023b：Variable FIR Decimation 模块可为可变大小输入信号生成固定大小输出信号

当您将 **Specification** 设置为 `Output frame length` 并为 **Output frame length** 参数指定值时，Variable FIR Decimation 模块生成固定大小输出信号。为了在仿真期间输入帧大小发生变化（可变大小）时仍保持输出的固定大小，该模块改变抽取因子 *M*。

当您将 **Specification** 设置为 `Decimation factor` 时，您直接在模块对话框中指定抽取因子。在此模式下，对于可变大小输入信号，该模块生成可变大小输出信号。抽取因子 *M* 保持不变。

## 描述

具有可调抽取因子的多相 FIR 抽取

Variable FIR Decimation 模块执行具有可调抽取因子的高效多相 FIR 抽取。您可以在仿真运行时在模块对话框中或通过输入端口更新抽取因子和滤波器系数。要控制抽取，您可以指定抽取因子或输出帧长度。

当您指定抽取因子时，如果输入帧长度在仿真期间发生变化（可变大小信号），则输出帧长度也会变化以保持抽取因子恒定。当您指定输出帧长度而非抽取因子时，如果输入帧长度在仿真期间发生变化（可变大小信号），则抽取因子也会变化以保持输出帧长度恒定。

从概念上讲，FIR 抽取器（如示意图所示）由抗混叠 FIR 滤波器后接降采样器组成。要设计 FIR 抗混叠滤波器，请使用 `designMultirateFIR` 函数。

FIR 滤波器使用直接型 FIR 滤波器对输入每个通道中的数据进行滤波。随后的降采样器通过对滤波后数据的每个通道取每第 *M* 个样本并丢弃随后的 *M* – 1 个样本来进行降采样。*M* 是抽取因子的值。所得离散时间信号的采样率为原始采样率的 1/*M*。

FIR 抽取器包含抗混叠 FIR 滤波器后接降采样器。

请注意，实际模块算法实现的是直接型 FIR 多相结构，它是图中所示组合系统的高效等价形式。有关更多详细信息，请参阅 Algorithms。

该模块支持 C 和 C++ 代码生成。
