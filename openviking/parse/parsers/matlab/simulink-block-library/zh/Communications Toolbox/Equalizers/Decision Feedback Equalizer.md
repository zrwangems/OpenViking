---
type: simulink-block
title: 'Decision Feedback Equalizer'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Equalizers'
documentation_page: 'decisionfeedbackequalizer'
documentation_source_path: 'ref/decisionfeedbackequalizer.html'
language: zh-CN
chinese_source: worker-translation
---

# Decision Feedback Equalizer

## 端口

### 输入

### **in** — 输入信号列向量

输入信号，指定为列向量。**in** 的向量长度必须等于 **Number of input samples per symbol** 参数的整数倍。有关详细信息，请参阅 Symbol Tap Spacing。

**数据类型：** `double`
**复数支持：** 是

### **Desired** — 训练符号列向量

训练符号，指定为列向量。**Desired** 的向量长度必须小于或等于输入 **in** 的长度。当 **Train** 输入端口为 `0` 时，**Desired** 输入端口被忽略。

#### 依赖关系

要启用此端口，请将 **Adaptive algorithm** 参数设置为 `LMS` 或 `RLS`。

**数据类型：** `double`
**复数支持：** 是

### **Train** — 训练均衡器标志布尔标量

训练均衡器标志，指定为 `1` 或 `0`。当此值从 `0` 变为 `1`（上升沿）时，模块开始训练。模块持续训练，直到 **Desired** 输入端口中的所有符号都被处理完毕。

#### 依赖关系

要启用此端口，请将 **Adaptive algorithm** 参数设置为 `LMS` 或 `RLS`，并选中 **Enable training control input** 参数。

**数据类型：** `Boolean`

### **Update** — 更新抽头权重标志 `1` | `0`

更新抽头权重标志，指定为 `1` 或 `0`。当此值为 `1` 时，抽头权重被更新。

#### 依赖关系

要启用此端口，请将 **Adaptive algorithm** 参数设置为 `CMA`，并将 **Source of adapt weights flag** 参数设置为 `Input port`。

**数据类型：** `Boolean`

### **Reset** — 复位均衡器标志 `1` | `0`

复位均衡器标志，指定为 `1` 或 `0`。如果 **Reset** 设置为 `1`，模块在处理输入信号之前复位抽头权重。模块执行初始训练，直到 **Desired** 输入端口中的所有符号都被处理完毕。

#### 依赖关系

要启用此端口，请选中 **Enable reset input****Enable reset input** 参数。

**数据类型：** `Boolean`
### 输出

### **Out** — 均衡后的符号列向量

均衡后的符号，返回为与输入信号 **in** 长度相同的列向量。

在您选中 **Output error signal** 或 **Output taps weights** 参数之前，此端口没有名称。

### **Err** — 误差信号列向量

误差信号，返回为与输入信号 **in** 长度相同的列向量。

#### 依赖关系

要启用此端口，请选中 **Output error signal** 参数。

### **w** — 抽头权重列向量

抽头权重，返回为 *N*Taps×1 向量，其中 *N*Taps 等于 **Number of forward taps** 和 **Number of feedback taps** 参数值之和。**w** 包含最后一次抽头权重更新后的抽头权重。

#### 依赖关系

要启用此端口，请选中 **Output taps weights** 参数。

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡中，在 **Prepare** 库中选择 **Property Inspector**。

#### 结构参数

### **Number of forward taps** — 前馈均衡器抽头数 `5`（默认）| 正整数

前馈均衡器抽头数，指定为正整数。前馈均衡器抽头数必须大于或等于 **Number of input samples per symbol** 参数的值。

### **Number of feedback taps** — 反馈均衡器抽头数 `3`（默认）| 正整数

反馈均衡器抽头数，指定为正整数。

### **Signal constellation** — 信号星座 `pskmod(0:3,4,pi/4)`（默认）| 向量

信号星座，指定为向量。默认值是使用以下代码生成的 QPSK 星座：`pskmod(0:3,4,pi/4)`。

### **Number of input samples per symbol** — 每个符号的输入采样数 `1`（默认）| 正整数

每个符号的输入采样数，指定为正整数。将此参数设置为大于 `1` 的任何数值会有效地创建分数间隔均衡器。有关详细信息，请参阅 Symbol Tap Spacing。

#### 算法参数

### **Adaptive algorithm** — 自适应算法 `LMS`（默认）| `RLS` | `CMA`

用于均衡的自适应算法，指定为以下值之一：

- `LMS` — 使用最小均方（LMS）算法更新均衡器抽头权重。
- `RLS` — 使用递归最小二乘（RLS）算法更新均衡器抽头权重。
- `CMA` — 使用恒模算法（CMA）更新均衡器抽头权重。

### **Step size** — 步长 `0.01`（默认）| 正标量

自适应算法使用的步长，指定为正标量。增大步长会缩短均衡器收敛时间，但会导致均衡器输出估计不太稳定。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Adaptive algorithm** 设置为 `LMS` 或 `CMA`。

### **Forgetting factor** — 遗忘因子 `0.99`（默认）| (0, 1] 范围内的标量

自适应算法使用的遗忘因子，指定为 (0, 1] 范围内的标量。减小遗忘因子会缩短均衡器收敛时间，但会导致均衡器输出估计不太稳定。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Adaptive algorithm** 设置为 `RLS`。

### **Initial inverse correlation matrix** — 初始逆相关矩阵 `0.1`（默认）| 标量 | 矩阵

初始逆相关矩阵，指定为标量或 *N*Taps×*N*Taps 矩阵。*N*Taps 等于 **Number of forward taps** 和 **Number of feedback taps** 参数值之和。如果将此值指定为标量 *a*，均衡器将初始逆相关矩阵设置为 *a* 倍单位矩阵：*a*(`eye`(*N*Taps))。

#### 依赖关系

要启用此参数，请将 **Adaptive algorithm** 设置为 `RLS`。

#### 控制参数

### **Reference tap** — 参考抽头 `3`（默认）| 正整数

参考抽头，指定为小于或等于 **Number of forward taps** 参数值的正整数。均衡器使用参考抽头位置来跟踪信道的主要能量。

### **Input signal delay (samples)** — 输入信号延迟 `0`（默认）| 非负整数

输入信号延迟（以采样为单位），相对于均衡器的复位时间，指定为非负整数。如果输入信号是长度大于 1 的向量，则输入延迟相对于输入向量的起始位置。如果输入信号是标量，则输入延迟相对于模块的第一次调用以及 **Reset** 输入端口切换为 `1` 后模块的第一次调用。

#### 依赖关系

要启用此参数，请将 **Adaptive algorithm** 设置为 `LMS` 或 `RLS`。

### **Source of adapt weights flag** — 自适应抽头权重请求的来源 `Property`（默认）| `Input port`

自适应抽头权重请求的来源，指定为以下值之一：

- `Property` — 指定此值以使用 **Adaptive algorithm** 参数来控制模块何时自适应抽头权重。
- `Input port` — 指定此值以使用 **Update** 输入端口来控制模块何时自适应抽头权重。

#### 依赖关系

要启用此参数，请将 **Adaptive algorithm** 设置为 `CMA`。

### **Adapt tap weights** — 自适应抽头权重 `on`（默认）| `off`

选中此参数以自适应更新均衡器抽头权重。如果清除此参数，模块保持均衡器抽头权重不变。

#### 依赖关系

要启用此参数，请将 **Adaptive algorithm** 设置为 `CMA`，并将 **Source of adapt weights flag** 设置为 `Property`。

### **Initial tap weights source** — 初始抽头权重的来源 `Auto`（默认）| `Property`

初始抽头权重的来源，指定为以下值之一：

- `Auto` — 将抽头权重初始化为算法特定的默认值，如 **Initial weights** 参数中所述。
- `Property` — 使用 **Initial weights** 参数值初始化抽头权重。

### **Initial weights** — 初始抽头权重 `0` 或 `[0;0;1;0;0]`（默认）| 标量 | 列向量

自适应算法使用的初始抽头权重，指定为标量或 *N*Taps×1 向量。*N*Taps 等于 **Number of forward taps** 和 **Number of feedback taps** 参数值之和。当 **Adaptive algorithm** 参数设置为 `LMS` 或 `RLS` 时，默认值为 `0`。当 **Adaptive algorithm** 参数设置为 `CMA` 时，默认值为 `[0;0;1;0;0]`。

如果将 **Initial weights** 指定为向量，则向量长度必须为 *N*Taps。如果将 **Initial weights** 指定为标量，均衡器使用标量扩展创建长度为 *N*Taps 的向量，所有值都设置为 **Initial weights**。

#### 依赖关系

要启用此参数，请将 **Initial tap weights source** 设置为 `Property`。

### **Tap weight update period (symbols)** — 抽头权重更新周期 `1`（默认）| 正整数

抽头权重更新周期（以符号为单位），指定为正整数。均衡器在处理此数量的符号后更新抽头权重。

### **Enable training control input** — 启用训练控制输入 `off`（默认）| `on`

选中此参数以启用输入端口 **Train**。如果清除此参数，模块在初始抽头训练后不会重新进入训练模式。

#### 依赖关系

要启用此参数，请将 **Adaptive algorithm** 设置为 `LMS` 或 `RLS`。

### **Update tap weights when not training** — 非训练时更新抽头权重 `on`（默认）| `off`

选中此参数以使用决策导向模式更新均衡器抽头权重。如果清除此参数，模块在训练后保持均衡器抽头权重不变。

#### 依赖关系

要启用此参数，请将 **Adaptive algorithm** 设置为 `LMS` 或 `RLS`。

### **Enable reset input** — 启用复位输入 `off`（默认）| `on`

选中此参数以启用输入端口 **Reset**。如果清除此参数，模块在处理输入信号之前不会复位抽头权重。

### **Info** — 判决反馈均衡器信息按钮

选择 **Info** 以显示适用于所应用设置的判决反馈均衡器信息。

#### 诊断参数

### **Output error signal** — 启用误差信号输出 `off`（默认）| `on`

选中此参数以启用包含均衡器误差信号的输出端口 **Err**。

### **Output taps weights** — 启用抽头权重输出 `off`（默认）| `on`

选中此参数以启用包含最后一次抽头权重更新后的抽头权重的输出端口 **w**。

### **Simulate using** — 要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

要运行的仿真类型，指定为 `Code generation` 或 `Interpreted execution`。

- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 为模块生成 C 代码。除非模型发生变化，否则模型在后续仿真中重用 C 代码。此选项需要额外的启动时间，但后续仿真的速度快于 `Interpreted execution` 选项。
- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项缩短启动时间，但后续仿真的速度慢于 `Code generation` 选项。在此模式下，您可以调试模块的源代码。

有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。

## 所属库

Communications Toolbox / Equalizers

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

## 描述

使用判决反馈滤波对调制信号进行均衡

Decision Feedback Equalizer 模块使用带有加权求和的判决反馈滤波器抽头延迟线，对通过色散信道传输的调制信号进行均衡。该模块使用建模为有限输入响应（FIR）滤波器的信道估计，处理输入帧并输出估计信号。

此图标显示了为使用 LMS 或 RLS 自适应算法的配置启用了所有端口的模块。

此图标显示了为使用 CMA 自适应算法的配置启用了所有端口的模块。
