---
type: simulink-block
title: 'MIMO FIR Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Filter Implementations'
documentation_page: 'mimofirfilter'
documentation_source_path: 'ref/mimofirfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# MIMO FIR Filter

## 端口

### 输入

### **x** — 数据输入向量 | 矩阵

将数据输入指定为大小为 *L*×*T* 的向量或矩阵。此模块支持可变大小输入信号，也就是说，您可以在仿真期间更改输入帧大小（行数）。但是，通道数（列数）必须保持不变。

在您将 **Numerator source** 设置为 `Input port` 之前，此端口没有名称。

**数据类型：** `single` | `double`
**复数支持：** Yes

### **Num** — 时域 FIR 滤波器系数行向量 | 矩阵

将时域 FIR 滤波器系数指定为行向量或矩阵输入。有关滤波器系数的更多信息，请参阅 **Numerator** 参数说明。

如果分子输入是行向量，则数据输入通道数必须为 1。

#### 依赖项

要启用此端口，请将 **Numerator source** 设置为 `Input port`。

**数据类型：** `single` | `double`
**复数支持：** Yes

### 输出

### **y** — 滤波后输出向量 | 矩阵 | 3-D 数组

滤波后输出，以向量、矩阵或 3-D 数组形式返回。

当滤波器数量 *F* 大于 1 并且您：

- 选择 **Sum filtered output contributions from all input channels** 参数时，模块会将来自每个输入通道的滤波后输出相加，生成一个 *L*×*R* 输出矩阵，其中 *L* 是输入帧大小（输入行数），*R* 是输出通道数。*R* 等于 *F*/(*T* × *P*)，其中 *F* 是滤波器数量，*T* 是输入通道数，*P* 是您在 **Number of propagation paths** 参数中指定的值。
- 清除 **Sum filtered output contributions from all input channels** 参数时，模块不会对所有输入通道的滤波后输出贡献求和。输出是 *L*×*R*×*T* 数组。`y(:,j,k)` 指的是对于第 *j* 个输出通道，来自第 *k* 个输入通道的输出。例如，`y(:,3,2)` 表示来自第二个输入通道的第三个输出通道上的输出。

有关模块如何计算输出的更多信息，请参阅使用多个传播路径对 MIMO 系统建模。

输出与输入信号具有相同的数据类型和复数/实数属性。

**数据类型：** `single` | `double`
**复数支持：** Yes

## 参数

要交互式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 中，在 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### **Numerator source** — FIR 滤波器系数的来源 `Property`（默认） | `Input port`

将 FIR 滤波器系数的来源指定为以下之一：

- `Property` –– 通过 **Numerator** 参数指定滤波器系数。
- `Input port` –– 通过 **Num** 输入端口指定滤波器系数。

### **Numerator** — 时域 FIR 滤波器系数 [`0.5 0.5`;`0.75 0.25`]（默认） | 行向量 | 矩阵

将时域 FIR 滤波器系数指定为大小为 *F*×*NumLen* 的行向量（单个滤波器）或矩阵（多个滤波器），其中 *F* 是滤波器数量，*NumLen* 是滤波器长度。如果 *F* 大于 1，则其值必须是输入通道数（列数）*T* 与您通过 `NumPaths` 属性指定的路径数 *P* 的乘积的倍数。该倍数决定输出通道数 *R*，且等于 *F*/(*T* × *P*)。

系数值可以在仿真期间更改，但分子的大小必须保持不变。

**可调：** Yes

#### 依赖项

要启用此参数，请将 **Numerator source** 设置为 `Property`。

**数据类型：** `single` | `double`
**复数支持：** Yes

### **Number of propagation paths** — 每对输入和输出通道之间的传播路径数 `1`（默认） | 正整数

将每对输入和输出通道之间的传播路径数 *P* 指定为正整数。每条路径由一个唯一的滤波器表示。当您将路径数指定为大于 `1` 时，该滤波器对多径传播进行建模。模块会对每对输入和输出通道之间所有路径的滤波后输出贡献求和。

有关示例，请参阅通过多个传播路径对输入信号进行滤波。

#### 依赖项

要启用此参数，滤波器数量 *F* 必须大于 1。

**数据类型：** `single` | `double`

### **Sum filtered output contributions from all input channels** — 对所有输入通道的滤波后输出贡献求和的选项 `on`（默认） | `off`

选择此参数可对所有输入通道的滤波后输出贡献求和。模块会将来自每个输入通道的滤波后输出相加，生成一个 *L*×*R* 输出矩阵，其中 *L* 是输入帧大小（输入行数），*R* 是输出通道数。*R* 等于 *F*/(*T* × *P*)，其中 *F* 是滤波器数量，*T* 是输入通道数，*P* 是您在 **Number of propagation paths** 参数中指定的值。

当您清除此参数时，模块不会对所有输入通道的滤波后输出贡献求和。输出是 *L*×*R*×*T* 数组。

有关模块如何基于此参数的值计算输出的更多信息，请参阅使用多个传播路径对 MIMO 系统建模。

#### 依赖项

要启用此参数，滤波器数量 *F* 必须大于 1。

**数据类型：** `Boolean`

### **View Filter Response** — View Filter Response 按钮

单击此按钮会打开滤波器可视化工具，并显示您在分子矩阵中指定的滤波器的幅值响应。该响应基于您在模块对话框中选定的参数。要在滤波器可视化工具运行时更新幅值响应，请修改对话框中的参数，然后单击 **Apply**。

您可以从可视化工具的界面配置绘图设置和信号测量。

在滤波器可视化工具 toolstrip 的 **Scope** 选项卡上，**Configuration** 部分允许您修改绘图设置。在 **Measurements** 选项卡上，您可以放置数据光标并显示所选信号的峰值。

有关滤波器可视化工具界面及其工具的更多详细信息，请参阅配置滤波器可视化工具。

#### 依赖项

要启用此按钮，请将 **Numerator source** 设置为 `Property`。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认） | `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` –– 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` –– 使用生成的 C 代码仿真模型。第一次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，后续仿真会重用该 C 代码。此选项需要额外的启动时间，但可提供更快的后续仿真。

## 所属库

DSP System Toolbox / Filtering / Filter Implementations

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

**在 R2025a 中引入**

## 描述

通过多径 MIMO FIR 滤波器对输入信号进行滤波

MIMO FIR Filter 模块对包含多个时域 FIR 滤波器的多输入多输出 (MIMO) 系统进行建模。该模块执行时域滤波，其中滤波操作涉及输入通道与特定路径上的 FIR 滤波器之间的卷积。您可以直接使用 **Numerator** 参数或通过 **Num** 输入端口指定多个滤波器的系数。

使用 **Number of propagation paths** 参数，您可以指定每对输入和输出通道之间的路径数。每条路径包含一个长度相同的单时域 FIR 滤波器。模块会对来自每条路径的滤波后输出求和。此外，根据 **Sum filtered output contributions from all input channels** 参数的设置，模块会将这些滤波后输出贡献相加或串联。有关更多信息，请参阅使用多个传播路径对 MIMO 系统建模。

输出信号中的通道数取决于滤波器数量、每对输入和输出通道之间的路径数以及输入通道数。有关更多详细信息，请参阅 `y` 参数说明。

Frequency-Domain FIR Filter 模块也支持对 MIMO 和多径系统进行建模。该模块在频域中实现滤波。通常，时域滤波对于较小的脉冲响应更高效，而频域滤波对于较长的脉冲响应更高效。
