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

### **u** — 数据输入向量 | 矩阵

指定数据输入为大小为 *P*×*Q* 的向量或矩阵。该模块将输入信号的每一列视为单独通道。如果输入是二维信号，第一个维度表示通道长度（或帧大小），第二个维度表示通道数。如果输入是一维信号，则该模块将其解释为单通道。

该模块接受可变大小输入信号，即可以在仿真期间更改每个输入通道的大小，但不能更改通道数。

当将 **Specification** 设置为 `Output frame length` 时，输入帧长度 *P* 必须是输出帧长度 *Po* 的整数倍。*(自 R2023b 起)*

**数据类型：** `single` | `double`
**复数支持：** Yes

### **M** — 抽取因子输入端口 正整数

指定抽取因子 *M* 为正整数，且为最大抽取因子的整数因子。例如，如果将 **Maximum decimation factor** 设置为 24，则抽取因子的可能值为 1、2、3、4、6、8、12 和 24。

可以在仿真运行时调整抽取因子。有关示例，请参阅使用可调抽取因子对正弦信号进行抽取。

#### 依赖关系

要启用此端口：

- 将 **Specification** 设置为 `Decimation factor`。*(自 R2023b 起)*
- 选择 **Specify decimation factor from input port** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **coeffs** — 原型滤波器系数 向量

以降幂 *z* 指定低通 FIR 滤波器系数为向量。

FIR 滤波器的传递函数 *H*(*z*) 由下式给出：

H(z)=b0+b1z−1+...+bNz−N,

可以使用 DSP System Toolbox™ 滤波器设计函数之一（如 `designMultirateFIR`、`firnyquist`、`firgr` 或 `firceqrip`）生成 FIR 滤波器系数向量，**b** = [*b0*, *b1*, …, *bN*]。

基于最大抽取因子 *Mmax* 而不是抽取因子 *M* 计算滤波器系数。例如，如果 *Mmax* 为 24 且 *M* 为 8，并且使用 `designMultirateFIR` 作为设计函数，则使用 `designMultirateFIR(1,24)` 而不是 `designMultirateFIR(1,8)` 计算滤波器系数。

为了充当有效的抗混叠滤波器，系数通常对应于归一化截止频率不大于 1/*Mmax* 的低通滤波器。要设计此类滤波器，请使用 `designMultirateFIR` 函数。

该模块在内部将所有滤波器状态初始化为零。

可以在仿真期间更改滤波器系数，但滤波器系数的数量必须保持不变。有关示例，请参阅通过输入端口指定滤波器系数。

#### 依赖关系

要启用此端口，请将 **Numerator source** 参数设置为 `Input port`。

**数据类型：** `single` | `double`
**复数支持：** Yes

### 输出

### **y** — 抽取输出 向量 | 矩阵

抽取输出，以向量或矩阵形式返回。

当将 **Specification** 参数设置为 `Decimation factor` *(自 R2023b 起)* 时，输出信号的大小与输入信号的大小相同。但是，该模块最多计算 `ceil`(*P*/*M*)×*Q* 个输出样本，其中 *P* 是输入帧大小，*Q* 是输入通道数，*M* 是抽取因子。

如果输入是可变大小信号，则该模块输出可变大小信号，以保持抽取因子。

当将 **Specification** 参数设置为 `Output frame length` 时，输出信号的大小为 *Po*×*Q*，其中 *Po* 是在 **Output frame length** 参数中指定的值。*(自 R2023b 起)*

如果输入是可变大小信号，则该模块相应地改变抽取因子，并输出固定大小信号。*(自 R2023b 起)*

输出信号的复数性取决于输入信号的复数性和滤波器系数的复数性。有关更多详细信息，请参阅下表。

| 输入信号 | 滤波器系数 | 输出信号 |
| --- | --- | --- |
| Real | Complex | Complex |
| Real | Real | Real |
| Complex | Complex | Complex |
| Complex | Real | Complex |

**数据类型：** `single` | `double`
**复数支持：** Yes

## 参数

### **Specification** — 指定控制抽取因子的模式 `Decimation factor`（默认）| `Output frame length`

*自 R2023b 起*

指定控制抽取因子的模式。

当将 **Specification** 设置为：

- `Decimation factor` —— 该模块保持指定的抽取因子。如果输入信号帧长度在仿真期间变化（可变大小输入信号），则输出帧长度会以保持抽取因子 *M* 的方式变化。

  可变大小输入生成可变大小输出。
- `Output frame length` —— 该模块保持指定的输出帧长度。如果输入信号帧长度在仿真期间变化（可变大小输入信号），则抽取因子会以保持输出帧长度 *Po* 的方式变化。

  可变大小输入生成固定大小输出。

### **Maximum decimation factor** — 最大抽取因子 `24`（默认）| 正整数

指定最大抽取因子 *Mmax* 为正整数。通过输入端口 **M** 指定的抽取因子必须是此参数中指定的值的因子。

当将 **Specification** 参数设置为 `Output frame length` 时，该模块将输入帧长度视为最大抽取因子 *Mmax*。*(自 R2023b 起)*

#### 依赖关系

要启用此端口，请将 **Specification** 参数设置为 `Decimation factor`。*(自 R2023b 起)*

### **Specify decimation factor from input port** — 从输入端口指定抽取因子 `on`（默认）| `off`

选择此参数后，可以通过输入端口 **M** 指定抽取因子。清除此参数后，可以通过 **Decimation factor** 参数在模块对话框中指定抽取因子。

#### 依赖关系

要启用此参数，请将 **Specification** 参数设置为 `Decimation factor`。*(自 R2023b 起)*

### **Decimation factor** — 抽取因子 `24`（默认）| 正整数

指定抽取因子 *M* 为正整数，且为最大抽取因子 *Mmax* 的整数因子。例如，如果将 **Maximum decimation factor** 设置为 24，则 **Decimation factor** 的可能值为 1、2、3、4、6、8、12 和 24。

可以在仿真运行时调整抽取因子。

当将 **Specification** 参数设置为 `Output frame length` 时，该模块将输入帧长度 *P* 与输出帧长度 *Po* 之比视为抽取因子 *M*，即 *M* = *P*/*Po*。*(自 R2023b 起)*

**可调：** Yes

#### 依赖关系

要启用此参数：

- 将 **Specification** 参数设置为 `Decimation factor`。*(自 R2023b 起)*
- 清除 **Specify decimation factor from input port** 参数。

### **Output frame length** — 输出帧长度 `48`（默认）| 正整数

*自 R2023b 起*

指定输出帧长度 *Po* 为正整数。在此模式下，该模块将输出信号的帧长度保持为此参数中指定的值。如果输入信号帧长度在仿真期间变化（可变大小输入信号），则该模块的抽取因子会以保持输出帧长度的方式变化。

输入帧长度必须是输出帧长度的整数倍。

在此参数中指定的值决定当前抽取因子 *M*。有关更多详细信息，请参阅 **Decimation factor** 参数。

#### 依赖关系

要启用此参数，请将 **Specification** 参数设置为 `Output frame length`。

### **Numerator source** — FIR 滤波器系数来源 `Auto`（默认）| `Dialog parameter` | `Input port`

将 FIR 滤波器系数来源指定为以下之一：

- `Auto` —— 该模块使用 `designMultirateFIR` 函数设计 FIR 抽取器。此函数设计滤波器并返回该模块使用的系数。

  有关滤波器设计的更多信息，请参阅 Orfanidis [1]。
- `Dialog parameter` —— 通过模块对话框中的 **Prototype filter numerator coefficients** 参数指定滤波器系数。
- `Input port` —— 通过 **coeffs** 输入端口指定滤波器系数。

### **Prototype filter numerator coefficients** — 原型低通 FIR 滤波器系数 `designMultirateFIR(1,24)`（默认）| 向量

以降幂 *z* 指定原型低通 FIR 滤波器系数为向量。默认情况下，`designMultirateFIR(1,24)` 使用最大抽取因子 *Mmax* 为 24 计算滤波器系数。

FIR 滤波器的传递函数 *H*(*z*) 由下式给出：

H(z)=b0+b1z−1+...+bNz−N,

可以使用 DSP System Toolbox 滤波器设计函数之一（如 `designMultirateFIR`、`firnyquist`、`firgr` 或 `firceqrip`）生成 FIR 滤波器系数向量，**b** = [*b0*, *b1*, …, *bN*]。

基于最大抽取因子 *Mmax* 而不是抽取因子 *M* 计算滤波器系数。例如，如果 *Mmax* 为 24 且 *M* 为 8，并且使用 `designMultirateFIR` 作为设计函数，则使用 `designMultirateFIR(1,24)` 而不是 `designMultirateFIR(1,8)` 计算滤波器系数。

为了充当有效的抗混叠滤波器，系数通常对应于归一化截止频率不大于 1/*Mmax* 的低通滤波器。要设计此类滤波器，请使用 `designMultirateFIR` 函数。

该模块在内部将所有滤波器状态初始化为零。

#### 依赖关系

要启用此参数，请将 **Numerator source** 参数设置为 `Dialog parameter`。

**可调：** Yes

### **View Filter Response** — 查看滤波器响应 按钮

单击此按钮可打开滤波器可视化工具，并显示可变 FIR 抽取滤波器的幅值响应。该响应基于在模块对话框中选择的参数。要在动态滤波器可视化工具运行时更新幅值响应，请修改对话框中的参数并单击 **Apply**。

可以从可视化工具界面配置绘图设置和信号测量。

在 **Scope** 选项卡上，**Configuration** 部分允许修改绘图设置。单击 **Magnitude Phase** 可显示滤波器的幅值和相位响应。在 **Measurements** 选项卡上，可以测量信号统计信息、放置数据光标，并显示所选信号的峰值。

有关滤波器可视化工具界面及其工具的更多详细信息，请参阅配置滤波器可视化工具。

#### 依赖关系

当将 **Specification** 参数设置为 `Output frame length` *(自 R2023b 起)* 或将 **Numerator source** 参数设置为 `Input port` 时，无法查看滤波器响应。要查看滤波器响应，请将 **Specification** 参数设置为 `Decimation factor` *(自 R2023b 起)*，并将 **Numerator source** 参数设置为 `Auto` 或 `Dialog parameter`。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

指定要运行的仿真类型。可以将此参数设置为：

- `Interpreted execution` —— 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` —— 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，后续仿真将重用该 C 代码。此选项需要额外的启动时间，但后续仿真更快。

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

当将 **Specification** 设置为 `Output frame length` 并为 **Output frame length** 参数指定值时，Variable FIR Decimation 模块会生成固定大小输出信号。为了在输入帧大小在仿真期间变化（可变大小）时仍保持输出固定大小，该模块会改变抽取因子 *M*。

当将 **Specification** 设置为 `Decimation factor` 时，可直接在模块对话框中指定抽取因子。在此模式下，对于可变大小输入信号，该模块生成可变大小输出信号。抽取因子 *M* 保持不变。

## 描述

具有可调抽取因子的多相 FIR 抽取

Variable FIR Decimation 模块使用可调抽取因子执行高效的多相 FIR 抽取。可以在仿真运行时更新模块对话框中的抽取因子和滤波器系数，或通过输入端口更新它们。要控制抽取，可以指定抽取因子或输出帧长度。

当指定抽取因子时，如果输入帧长度在仿真期间变化（可变大小信号），则输出帧长度也会变化，以保持抽取因子恒定。当指定输出帧长度而不是抽取因子时，如果输入帧长度在仿真期间变化（可变大小信号），则抽取因子也会变化，以保持输出帧长度恒定。

从概念上讲，FIR 抽取器（如示意图所示）由抗混叠 FIR 滤波器后接下采样器组成。要设计 FIR 抗混叠滤波器，请使用 `designMultirateFIR` 函数。

FIR 滤波器使用直接型 FIR 滤波器对输入每个通道中的数据进行滤波。随后的下采样器通过对滤波后数据的每个通道每 *M* 个样本取一个样本，并丢弃随后的 *M* – 1 个样本，来对每个通道进行下采样。*M* 是抽取因子的值。生成的离散时间信号的采样率是原始采样率的 1/*M*。

FIR 抽取器包含抗混叠 FIR 滤波器后接下采样器。

请注意，实际模块算法实现直接型 FIR 多相结构，这是图中所示组合系统的高效等效形式。有关更多详细信息，请参阅算法。

该模块支持 C 和 C++ 代码生成。
