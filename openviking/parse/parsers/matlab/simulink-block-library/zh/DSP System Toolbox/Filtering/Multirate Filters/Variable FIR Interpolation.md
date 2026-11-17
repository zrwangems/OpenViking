---
type: simulink-block
title: 'Variable FIR Interpolation'
family: 'filtering'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Multirate Filters'
documentation_page: 'variablefirinterpolation'
documentation_source_path: 'ref/variablefirinterpolation.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable FIR Interpolation

## 端口

### 输入

### **u** — 数据输入向量 | 矩阵

将数据输入指定为大小为 *P*×*Q* 的向量或矩阵。该模块将输入信号的每一列视为独立通道。如果输入是二维信号，则第一个维度表示通道长度（或帧大小），第二个维度表示通道数。如果输入是一维信号，则该模块将其解释为单通道。

该模块接受可变大小输入信号，也就是说，您可以在仿真期间更改每个输入通道的大小，但不能更改通道数。

**数据类型：** `single` | `double`
**复数支持：** Yes

### **L** — 插值因子输入端口 正整数

将插值因子 *L* 指定为最大插值因子的整数因子的正整数。例如，如果将 **Maximum interpolation factor** 设置为 24，则插值因子的可能值为 1、2、3、4、6、8、12 和 24。

您可以在仿真运行时调整插值因子。有关示例，请参阅 Interpolate Sinusoidal Signal with Tunable Interpolation Factor。

#### 依赖关系

要启用此端口：

- 将 **Specification** 设置为 `Interpolation factor`。*（自 R2023b 起）*
- 选择 **Specify interpolation factor from input port** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **coeffs** — 原型滤波器系数 向量

指定 FIR 滤波器传递函数 *H*(*z*) 的分子系数。

H(z)=b0+b1z−1+...+bNz−N,

您可以使用 DSP System Toolbox™ 滤波器设计函数之一（例如 `designMultirateFIR`、`firnyquist`、`firgr` 或 `firceqrip`）生成 FIR 滤波器系数向量 **b** = [*b0*, *b1*, …, *bN*]。

基于最大插值因子 *Lmax* 而不是插值因子 *L* 计算滤波器系数。例如，如果 *Lmax* 为 24，*L* 为 8，并且您使用 `designMultirateFIR` 作为设计函数，则使用 `designMultirateFIR(24,1)` 而不是 `designMultirateFIR(8,1)` 计算滤波器系数。

为了作为有效的抗镜像滤波器，这些系数通常对应于归一化截止频率不大于最大插值因子倒数的低通滤波器。要设计此类滤波器，请使用 `designMultirateFIR` 函数。

该模块在内部将所有滤波器状态初始化为零。

您可以在仿真期间更改滤波器系数，但滤波器系数数量必须保持恒定。有关示例，请参阅 Specify Filter Coefficients Through Input Port。

#### 依赖关系

要启用此端口，请将 **Numerator source** 参数设置为 `Input port`。

**数据类型：** `single` | `double`
**复数支持：** Yes

### 输出

### **y** — 插值输出 向量 | 矩阵

插值输出，以向量或矩阵形式返回。

当将 **Specification** 参数设置为 `Interpolation factor` *（自 R2023b 起）* 时，输出信号的大小为 (*Lmax* × *P*)×*Q*，其中 *P* 是输入帧大小，*Q* 是输入通道数，*Lmax* 是最大插值因子。但是，该模块仅计算 (*L* × *P*)×*Q* 个样本。输出信号中的其余样本为零。

如果输入是可变大小信号，则该模块输出可变大小信号，以保持插值因子。

当将 **Specification** 参数设置为 `Output frame length` 时，输出信号的大小为 *Po*×*Q*，其中 *Po* 是您在 **Output frame length** 参数中指定的值。*（自 R2023b 起）*

如果输入是可变大小信号，则该模块会相应地改变插值因子，并输出固定大小信号。*（自 R2023b 起）*

输出信号的复/实性取决于输入信号的复/实性和滤波器系数的复/实性。有关更多详细信息，请参阅此表。

| 输入信号 | 滤波器系数 | 输出信号 |
| --- | --- | --- |
| 实数 | 复数 | 复数 |
| 实数 | 实数 | 实数 |
| 复数 | 复数 | 复数 |
| 复数 | 实数 | 复数 |

**数据类型：** `single` | `double`
**复数支持：** Yes

## 参数

### **Specification** — 指定用于控制插值因子的模式 `Interpolation factor` （默认） | `Output frame length`

*自 R2023b 起*

指定控制插值因子时所采用的模式。

当将 **Specification** 设置为：

- `Interpolation factor` –– 该模块保持您指定的插值因子。如果输入信号帧长度在仿真期间发生变化（可变大小输入信号），则输出帧长度会以保持插值因子 *L* 的方式变化。

  可变大小输入会生成可变大小输出。
- `Output frame length` –– 该模块保持您指定的输出帧长度。如果输入信号帧长度在仿真期间发生变化（可变大小输入信号），则插值因子会以保持输出帧长度 *Po* 的方式变化。

  可变大小输入会生成固定大小输出。

### **Maximum interpolation factor** — 最大插值因子 `24` （默认） | 正整数

将最大插值因子 *Lmax* 指定为正整数。您通过输入端口 **L** 指定的插值因子必须是您在此参数中指定的值的因子。

当将 **Specification** 参数设置为 `Output frame length` 时，该模块将输出帧长度视为最大插值因子 *Lmax*。*（自 R2023b 起）*

#### 依赖关系

要启用此端口，请将 **Specification** 参数设置为 `Interpolation factor`。*（自 R2023b 起）*

### **Specify interpolation factor from input port** — 从输入端口指定插值因子 `on` （默认） | `off`

当选择此参数时，可以通过输入端口 **L** 指定插值因子。当清除此参数时，可以通过 **Interpolation factor** 参数在模块对话框中指定插值因子。

#### 依赖关系

要启用此参数，请将 **Specification** 参数设置为 `Interpolation factor`。*（自 R2023b 起）*

### **Interpolation factor** — 插值因子 `24` （默认） | 正整数

将插值因子 *L* 指定为最大插值因子的整数因子的正整数。例如，如果将 **Maximum interpolation factor** 设置为 24，则 **Interpolation factor** 的可能值为 1、2、3、4、6、8、12 和 24。

您可以在仿真运行时调整插值因子。

当将 **Specification** 参数设置为 `Output frame length` 时，该模块将输出帧长度 *Po* 与输入帧长度 *P* 的比值视为插值因子 *L*，即 *L* = *Po*/*P*。*（自 R2023b 起）*

**可调：** Yes

#### 依赖关系

要启用此参数：

- 将 **Specification** 参数设置为 `Interpolation factor`。*（自 R2023b 起）*
- 清除 **Specify interpolation factor from input port** 参数。

### **Output frame length** — 输出帧长度 `48` （默认） | 正整数

*自 R2023b 起*

将输出帧长度 *Po* 指定为正整数。在此模式下，该模块将输出信号的帧长度保持为您在此参数中指定的值。如果输入信号帧长度在仿真期间发生变化（可变大小输入信号），则该模块的插值因子会以保持输出帧长度的方式变化。

输入帧长度必须是输出帧长度的除数。

您在此参数中指定的值确定最大插值因子 *Lmax* 和当前插值因子 *L*。有关更多详细信息，请参阅 **Maximum interpolation factor** 和 **Interpolation factor** 参数。

#### 依赖关系

要启用此参数，请将 **Specification** 参数设置为 `Output frame length`。

### **Numerator source** — FIR 滤波器系数来源 `Auto` （默认） | `Dialog parameter` | `Input port`

将 FIR 滤波器系数来源指定为以下之一：

- `Auto` –– 该模块使用 **Interpolation factor** 参数中的插值因子设计 FIR 插值器。`designMultirateFIR` 函数设计滤波器并返回该模块使用的系数。

  有关滤波器设计的更多信息，请参阅 Orfanidis [1]。
- `Dialog parameter` –– 通过模块对话框中的 **Prototype filter numerator coefficients** 参数指定滤波器系数。
- `Input port` –– 通过 **coeffs** 输入端口指定滤波器系数。

### **Prototype filter numerator coefficients** — 原型滤波器系数 `designMultirateFIR(24,1)` （默认） | 向量

指定 FIR 滤波器传递函数 *H*(*z*) 的分子系数。

H(z)=b0+b1z−1+...+bNz−N,

您可以使用 DSP System Toolbox 滤波器设计函数之一（例如 `designMultirateFIR`、`firnyquist`、`firgr` 或 `firceqrip`）生成 FIR 滤波器系数向量 **b** = [*b0*, *b1*, …, *bN*]。

基于最大插值因子 *Lmax* 而不是插值因子 *L* 计算滤波器系数。例如，如果 *Lmax* 为 24，*L* 为 8，并且您使用 `designMultirateFIR` 作为设计函数，则使用 `designMultirateFIR(24,1)` 而不是 `designMultirateFIR(8,1)` 计算滤波器系数。

为了作为有效的抗镜像滤波器，这些系数通常对应于归一化截止频率不大于最大插值因子倒数的低通滤波器。要设计此类滤波器，请使用 `designMultirateFIR` 函数。

该模块在内部将所有滤波器状态初始化为零。

您可以在仿真期间更改滤波器系数，但滤波器系数数量必须保持恒定。

#### 依赖关系

要启用此参数，请将 **Numerator source** 参数设置为 `Dialog parameter`。

**可调：** Yes

### **View Filter Response** — 查看滤波器响应按钮

单击此按钮可打开滤波器可视化器并显示可变 FIR 插值滤波器的幅值响应。响应基于您在模块对话框中选择的参数。要在滤波器可视化器运行时更新幅值响应，请修改对话框中的参数，然后单击 **Apply**。

您可以从可视化器界面配置绘图设置和信号测量。

在 **Scope** 选项卡上，**Configuration** 部分允许您修改绘图设置。单击 **Magnitude Phase** 可显示滤波器的幅值和相位响应。在 **Measurements** 选项卡上，您可以测量信号统计量、放置数据光标，并显示所选信号的峰值。

有关滤波器可视化器界面及其工具的更多详细信息，请参阅 Configure Filter Visualizer。

#### 依赖关系

当将 **Specification** 参数设置为 `Output frame length` *（自 R2023b 起）* 或将 **Numerator source** 参数设置为 `Input port` 时，无法查看滤波器响应。要查看滤波器响应，请将 **Specification** 参数设置为 `Interpolation factor` *（自 R2023b 起）*，并将 **Numerator source** 参数设置为 `Auto` 或 `Dialog parameter`。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution` （默认） | `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` –– 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` –– 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，后续仿真将重用该 C 代码。此选项需要额外的启动时间，但可提供更快的后续仿真。

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

### R2024a：**Simulate using** 参数的默认值变更

**Simulate using** 参数的默认值现在为 `Interpreted execution`。进行此更改后，该模块默认使用 MATLAB 解释器进行仿真。

### R2023b：Variable FIR Interpolation 模块可为可变大小输入信号生成固定大小输出信号

当将 **Specification** 设置为 `Output frame length` 并为 **Output frame length** 参数指定值时，Variable FIR Interpolation 模块会生成固定大小输出信号。为了在仿真期间输入帧大小发生变化（可变大小）时仍保持输出为固定大小，该模块会改变插值因子 *L*。

当将 **Specification** 设置为 `Interpolation factor` 时，您直接在模块对话框中指定插值因子。在此模式下，对于可变大小输入信号，该模块会生成可变大小输出信号。插值因子 *L* 保持恒定。

## 描述

具有可调插值因子的多相 FIR 插值

Variable FIR Interpolation 模块使用可调插值因子执行高效的多相 FIR 插值。您可以在仿真运行时，在模块对话框中或通过输入端口更新插值因子和滤波器系数。要控制插值，可以指定插值因子或输出帧长度。

当指定插值因子时，如果仿真期间输入帧长度发生变化（可变大小信号），则输出帧长度也会变化，以保持插值因子恒定。当指定输出帧长度而不是插值因子时，如果仿真期间输入帧长度发生变化（可变大小信号），则插值因子也会变化，以保持输出帧长度恒定。

从概念上讲，FIR 插值器（如示意图所示）由一个上采样器后跟一个 FIR 抗镜像滤波器组成，后者通常是理想带限插值滤波器的近似。要设计 FIR 抗镜像滤波器，请使用 `designMultirateFIR` 函数。上采样器通过在样本之间插入 *L*–1 个零，将输入的每个通道上采样到更高速率。随后的 FIR 滤波器对已上采样数据的每个通道进行滤波。所得离散时间信号的采样率是原始采样率的 *L* 倍。

FIR 插值器包含一个上采样器，后跟一个抗镜像 FIR 滤波器。

但是，实际的模块算法实现的是直接型 FIR 多相结构，这是图中所示组合系统的高效等效形式。有关更多详细信息，请参阅 Algorithms。

该模块支持 C 和 C++ 代码生成。
