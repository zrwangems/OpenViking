---
type: simulink-block
title: 'Check Custom Bounds'
family: 'sldo'
product_id: 'sldo'
product_name: 'Simulink Design Optimization'
documentation_release: R2025b
official_category: 'Model Verification'
documentation_page: 'checkcustombounds'
documentation_source_path: 'ref/checkcustombounds.html'
language: zh-CN
chinese_source: worker-translation
---

# Check Custom Bounds

## 端口

### 输入

### **Port\_1 (u)** — 要对照指定边界检查的信号 标量 | 向量 | 矩阵

在仿真期间要对照 **Amplitudes** 和 **Times** 中指定的上下边界进行检查的信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `enumerated` | `bus`
### 输出

### **Port\_1 (out)** — 输出断言信号 `1` | `0`

输出信号，指示输入信号是否处于指定断言信号的边界内。在每个时间步，输出返回为以下之一：

- 如果断言成功，即信号满足所有边界，则为 True (`1`)
- 如果断言失败，即信号违反某个边界，则为 False (`0`)

输出信号的数据类型默认为 double。要将 Simulink 模型中所有生成逻辑信号的模块的输出数据类型设置为 Boolean，请在配置参数中选择 **Implement logic signals as Boolean data**。

#### 依赖

要启用此端口，请在 **Assertion** 选项卡上选择 **Output assertion signal** 参数。

**数据类型：** `Boolean` | `double`

## 参数

### **Show Plot** — 打开绘图窗口 `button`

使用绘图查看以下内容。

- 仿真期间计算的系统特性和信号 — 在仿真模型之前点击此按钮，以查看系统特性或信号。

  您可以通过右键点击绘图并选择 **Characteristics** 来显示其他特性，例如峰值响应时间。
- 边界 — 您可以在 **Bounds** 选项卡上指定边界，或通过右键点击绘图并选择 **Bounds** > **New Bound** 来指定边界。

  您可以通过拖动边界段或右键点击绘图并选择 **Bounds** > **Edit Bound** 来修改边界。在仿真模型之前，点击 **Update Block** 以更新模块参数中的边界值。

您在绘图窗口中执行的典型任务包括：

- 通过点击 Open block parameters dialog 图标或选择 **Edit** 打开 Block Parameters 对话框。
- 通过点击 Highlight block 图标或选择 **View** > **Highlight Simulink Block** 查找绘图窗口对应的模块。此操作会使模型窗口处于活动状态并高亮显示该模块。
- 通过点击 Run 图标仿真模型。此操作还会对指定线性化输入和输出之间的模型部分进行线性化。
- 通过点击 Insert legend 图标在线性系统特性图上添加图例。

### **Show plot on block open** — 双击模块以打开绘图 `off` (默认) | `on`

当您在 Simulink 模型中双击该模块时，打开绘图窗口而不是模块参数。

如果您更愿意在绘图窗口中打开并执行任务（例如添加或修改边界），而不是在模块参数中执行，请使用此参数。如果您想从绘图窗口访问模块参数，请选择 **Edit** 或点击 Open block parameters dialog 图标。

有关绘图的更多信息，请参阅 **Show plot** 参数。

#### 程序化使用

|  |
| --- |
| **参数：** `LaunchViewOnOpen` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认：** `'off'` |

### **Response Optimization** — 打开 Response Optimizer `button`

打开 Response Optimizer，以优化模型响应，从而满足 **Bounds** 选项卡上指定的设计要求。

#### 另请参阅

- Design Optimization to Meet Step Response Requirements (GUI)
- Design Optimization to Meet Time-Domain and Frequency-Domain Requirements (GUI)

### Bounds 选项卡

### **Include upper bound in assertion** — 检查信号是否满足上界 `on`（默认）| `off`

在仿真期间检查信号是否小于或等于上界 **Times** 和 **Amplitudes** 中指定的上界。如果信号违反上界，软件将显示警告。

上界也会显示在时间图上。

当您禁用此参数时，软件将停止在仿真期间检查输入信号是否满足上界。上界段在图上也会变灰。

图上变灰的上界段

若要在图上仅查看上界和输入信号，请清除 **Enable assertion**。

#### 依赖关系

要使用此参数，请在 **Assertion** 选项卡上选择 **Enable assertion**。如果清除 **Enable assertion**，软件不会将上界用于断言，但它们仍会继续显示在图上。

#### 编程使用

|  |
| --- |
| **Parameter:** `EnableUpperBound` |
| **类型**：character vector |
| **Value:** `'on'` | `'off'` |
| **默认值**：`'on'` |

### **Times** — 上界时间向量 `[0 5; 5 10]`（默认）| 二元素向量 | 两列矩阵 | 元胞数组

一个或多个上界段的时间向量，以秒为单位指定。

在 **Amplitudes** 中指定对应的幅值。

- 要指定具有一条边的单个上界，请使用二元素向量。该向量必须采用 [*Tstart* *Tend*] 的形式，其中 *Tstart* 和 *Tend* 为正有限数，且 *Tstart* < *Tend*。

  例如，要创建一个在 0 到 10 秒时间区间内幅值为 1.2 的单个上界，请为 **Times** 指定 `[0 10]`，并为 **Amplitudes** 指定 `[1.2 1.2]`。

  时间图上具有一条边的单个上界
- 要指定具有多条边的单个上界，请使用两列矩阵。该矩阵必须采用 [*T1* *T2* ; *T2* *T3* ;…; *Tn* *Tn+1*] 的形式，其中 *n* 是上界中的边数。具有多条边的单个上界是分段连续的，因此请指定这样的时间区间：下一条边从前一条边结束的同一时间开始。

  例如，要创建一个在 0–5 秒和 5–10 秒时刻具有两条边、幅值分别为 1.2 和 1 的单个上界，请为 **Times** 指定 `[0 5;5 10]`，并为 **Amplitudes** 指定 `[1.2 1.2;1 1]`。

  时间图上具有两条边的单个上界
- 要指定多个上界，请使用由二元素向量、两列矩阵或二者组成的元胞数组。也就是说，使用由多个单个上界组成的元胞数组。

  例如，要创建两个上界，分别在 0–4 秒和 6–10 秒时刻，幅值分别为 1.2 和 1，请为 **Times** 指定 `{[0 4] [6 10]}`，并为 **Amplitudes** 指定 `{[1.2 1.2] [1 1]}`。

  时间图上的两个上界

您可以从绘图窗口添加或修改开始时间和结束时间。

- 要添加新的时间向量，请右键单击图上的黄色区域并选择 **Edit**。单击 **Insert** 向 Edit Bound 对话框添加新行。在 **Time** 列中指定新上界段的开始时间和结束时间。在 **Amplitude** 列中指定对应的幅值。
- 要修改开始时间和结束时间，请拖动上界段。或者，右键单击该段，然后选择 **Edit**。在 **Time** 列中指定新的时间。

  在仿真模型之前，单击 **Update Block**。

要检查输入信号是否满足与上界时间向量对应的幅值，请同时选择 **Include upper bound in assertion** 和 **Enable assertion**。

#### 编程使用

|  |
| --- |
| **Parameter:** `UpperBoundTimes` |
| **类型**：character vector |
| **Value:** two-element vector | two-column matrix | cell array |
| **默认值**：`[0 5; 5 10]` |

### **Amplitudes** — 上界幅值 `[1.1 1.1; 1.01 1.01]`（默认）| 二元素向量 | 两列矩阵 | 元胞数组

一个或多个上界段的幅值。

在 **Times** 中指定对应的起始和结束时间。

- 要指定具有一条边的单个边界，请使用二元素向量。该向量必须为 [*A1* *A2*] 形式，其中 *A1* 和 *A2* 是时间向量对应边缘处的边界幅值。若要在整个时间区间内保持恒定幅值，请使用 *A1* = *A2*。

  例如，要在 0 到 10 秒的时间区间内创建幅值为 1.2 的单个上界，请为 **Times** 指定 `[0 10]`，并为 **Amplitudes** 指定 `[1.2 1.2]`。

  时间图上具有一条边的单个上界
- 要指定具有多条边的单个边界，请使用两列矩阵。该矩阵必须为 [*A1* *B1* ;…; *An* *Bn*] 形式，其中 *n* 是边界中的边数。若要在整个时间区间内保持恒定幅值，请使用 *Ak* = *Bk*，其中 *k* = 1,…,*n*

  例如，要创建一个在 0–5 秒和 5–10 秒时刻具有两条边、幅值分别为 1.2 和 1 的单个边界，请为 **Times** 指定 `[0 5;5 10]`，并为 **Amplitudes** 指定 `[1.2 1.2;1 1]`。

  时间图上具有两条边的单个上界
- 要指定多个边界，请使用由二元素向量、两列矩阵或两者组成的元胞数组。也就是说，使用由多个单个边界组成的元胞数组。

  例如，要创建两个分别在 0–4 秒和 6–10 秒时刻、幅值分别为 1.2 和 1 的边界，请为 **Times** 指定 `{[0 4] [6 10]}`，并为 **Amplitudes** 指定 `{[1.2 1.2] [1 1]}`。

  时间图上的两个上界

您可以从绘图窗口添加或修改幅值。

- 要添加新的幅值，请右键点击绘图并选择 **Edit**。点击 **Insert** 向 Edit Bound 对话框添加新行。在 **Amplitude** 列中指定新边界段的起始和结束幅值。在 **Time** 列中指定对应的起始和结束时间。
- 要修改起始和结束幅值，请拖动边界段。或者，右键点击该段，然后选择 **Edit**。在 **Amplitude** 列中指定新的幅值。

  在仿真模型之前，点击 **Update Block**。

要检查输入信号是否满足上幅值边界，请同时选择 **Include upper bound in assertion** 和 **Enable assertion**。

#### 编程使用

|  |
| --- |
| **Parameter:** `UpperBoundAmplitudes` |
| **类型**：character vector |
| **Value:** two-element vector | two-column matrix | cell array |
| **默认值**：`[1.1 1.1; 1.01 1.01]` |

### **Include lower bound in assertion** — 检查信号是否满足下界 `off`（默认）| `on`

在仿真期间检查信号是否大于或等于在下界 **Times** 和 **Amplitudes** 中指定的下界。如果信号违反下界，软件将显示警告。

这些边界也会显示在时间图上。

当此参数被禁用时，下界将被禁用，软件在仿真期间停止检查是否满足这些边界。边界段也会在图上变灰。

图上变灰的下界段

要仅在图上查看边界和输入信号，请清除 **Enable assertion**。

#### 依赖关系

要使用此参数，请在 **Assertion** 选项卡上选择 **Enable assertion**。如果清除 **Enable assertion**，软件不会将这些边界用于断言，但它们仍会继续显示在图上。

#### 编程使用

|  |
| --- |
| **Parameter:** `EnableLowerBound` |
| **类型**：character vector |
| **Value:** `'on'` | `'off'` |
| **默认值**：`'off'` |

### **Times** — 下界时间向量 `[]`（默认）| 二元素向量 | 二列矩阵 | 元胞数组

一个或多个下界段的时间向量，以秒为单位指定。

在 **Amplitudes** 中指定对应的幅值。

- 要指定具有一条边的单个边界，请使用二元素向量。该向量必须采用 [*Tstart* *Tend*] 的形式，其中 *Tstart* 和 *Tend* 为正有限数，且 *Tstart* < *Tend*。

  例如，要在 0 到 10 秒的时间区间内创建幅值为 0.8 的单个下界，请为 **Times** 指定 `[0 10]`，并为 **Amplitudes** 指定 `[0.8 0.8]`。

  时间图上的单边单个下界
- 要指定具有多条边的单个边界，请使用二列矩阵。该矩阵必须采用 [*T1* *T2* ; *T2* *T3* ;…; *Tn* *Tn+1*] 的形式，其中 *n* 是边界中的边数。具有多条边的单个边界是分段连续的，请指定时间区间，使下一条边在前一条边结束的同一时间开始。

  例如，要创建一个在 0–5 秒和 5–10 秒两个时间处具有两条边、幅值分别为 0.8 和 0.98 的单个边界，请为 **Times** 指定 `[0 5;5 10]`，并为 **Amplitudes** 指定 `[0.8 0.8;0.98 0.98]`。

  时间图上的双边单个下界
- 要指定多个边界，请使用由二元素向量、二列矩阵或两者组成的元胞数组。也就是说，使用由多个单个边界组成的元胞数组。

  例如，要创建两个边界，分别在 0–4 秒和 6–10 秒时间处，幅值分别为 0.8 和 0.98，请为 **Times** 指定 `{[0 4] [6 10]}`，并为 **Amplitudes** 指定 `{[0.8 0.8] [0.98 0.98]}`。

  时间图上的两个下界

您可以从绘图窗口添加或修改开始和结束时间。

- 要添加新的时间向量，请右键单击绘图上的黄色区域，然后选择 **Edit**。单击 **Insert** 向 Edit Bound 对话框添加新行。在 **Time** 列中指定新边界段的开始和结束时间。在 **Amplitude** 列中指定对应的幅值。
- 要修改开始和结束时间，请拖动边界段。或者，右键单击该段，然后选择 **Edit**。在 **Time** 列中指定新的时间。

  在仿真模型之前，单击 **Update Block**。

要检查输入信号是否满足与下界时间向量对应的幅值，请同时选择 **Include lower bound in assertion** 和 **Enable assertion**。

#### 编程使用

|  |
| --- |
| **Parameter:** `LowerBoundTimes` |
| **类型**：character vector |
| **Value:** two-element vector | two-column matrix | cell array |
| **默认值**：`[]` |

### **Amplitudes** — 下界幅值 `[]`（默认）| 二元素向量 | 两列矩阵 | 元胞数组

一个或多个下界段的幅值。

在 **Times** 中指定对应的开始和结束时间。

- 要指定具有一条边的单个边界，请使用二元素向量。该向量必须采用 [*A1* *A2*] 的形式，其中 *A1* 和 *A2* 是时间向量对应边处的边界幅值。若要在整个时间区间内保持恒定幅值，请使用 *A1* = *A2*。

  例如，要在 0 到 10 秒的时间区间内创建幅值为 0.8 的单个下界，请为 **Times** 指定 `[0 10]`，并为 **Amplitudes** 指定 `[0.8 0.8]`。

  时间图上具有一条边的单个下界
- 要指定具有多条边的单个边界，请使用两列矩阵。该矩阵必须采用 [*A1* *B1* ;…; *An* *Bn*] 的形式，其中 *n* 是边界中的边数。若要在整个时间区间内保持恒定幅值，请使用 *Ak* = *Bk*，其中 *k* = 1,…,*n*

  例如，要创建一个在 0–5 秒和 5–10 秒处具有两条边、幅值分别为 0.8 和 0.98 的单个边界，请为 **Times** 指定 `[0 5;5 10]`，并为 **Amplitudes** 指定 `[0.8 0.8;0.98 0.98]`。

  时间图上具有两条边的单个下界
- 要指定多个边界，请使用由二元素向量、两列矩阵或二者组成的元胞数组。也就是说，使用由多个单个边界组成的元胞数组。

  例如，要创建两个边界，时间分别为 0–4 秒和 6–10 秒，幅值分别为 0.8 和 0.98，请为 **Times** 指定 `{[0 4] [6 10]}`，并为 **Amplitudes** 指定 `{[0.8 0.8] [0.98 0.98]}`。

  时间图上的两个下界

您可以从绘图窗口添加或修改幅值。

- 要添加新的幅值，请右键点击绘图并选择 **Edit**。点击 **Insert** 向 Edit Bound 对话框添加新行。在 **Amplitude** 列中指定新边界段的起始和结束幅值。在 **Time** 列中指定对应的开始和结束时间。
- 要修改起始和结束幅值，请拖动边界段。或者，右键点击该段，然后选择 **Edit**。在 **Amplitude** 列中指定新的幅值。

  在仿真模型之前点击 **Update Block**。

要检查输入信号是否满足下幅值边界，请同时选择 **Include lower bound in assertion** 和 **Enable assertion**。

#### 编程使用

|  |
| --- |
| **Parameter:** `LowerBoundAmplitudes` |
| **类型**：character vector |
| **Value:** two-element vector | two-column matrix | cell array |
| **默认值**：`[]` |

### **Enable zero-crossing detection** — 在边界边处评估模型 `on`（默认）| `off`

确保软件对模型进行仿真，以在边界边处产生输出。在边界边处对模型进行仿真可防止仿真求解器遗漏信号在其边处满足该边界的断言。

显示模型仿真时间点的图

有关详细信息，请参阅 Zero-Crossing Detection。

#### 编程使用

|  |
| --- |
| **Parameter:** `ZeroCross` |
| **类型**：character vector |
| **Value:** `'on'` | `'off'` |
| **默认值**：`'on'` |

### Assertion Tab

### **Enable assertion** — 启用或禁用检查 `on`（默认）| `off`

使模块能够检查在**边界**选项卡中指定并包含用于断言的边界在仿真期间是否得到满足。如果边界未得到满足，则断言失败。MATLAB 命令提示符处会出现一条报告断言失败的警告。

如果断言失败，您可以选择指定模块：

- 执行在**断言失败时的仿真回调（可选）**中指定的 MATLAB 表达式。
- 通过选择**断言失败时停止仿真**来停止仿真并返回错误消息。

如果您未指定任何边界，则此参数无效。

当您禁用此参数时，模块不再检查输入信号是否满足指定的边界。模块图标也会更新以指示断言已禁用。

带叉的模块图标

在 Simulink 模型中，在配置参数中，**模型验证模块启用**参数允许您启用或禁用模型中的所有模型验证模块，而不管此选项在模块中的设置如何。

#### 编程使用

|  |
| --- |
| **Parameter:** `enabled` |
| **类型**：character vector |
| **Value:** `'on'` | `'off'` |
| **默认值**：`'on'` |

### **Simulation callback when assertion fails (optional)** — 断言失败时要计算的表达式 `''`（默认）| MATLAB 表达式

断言失败时要执行的 MATLAB 表达式。

由于该表达式在 MATLAB 工作区中计算，因此请先在工作区中定义表达式中使用的所有变量。

#### 依赖关系

要启用此参数，请选择**启用断言**。

#### 编程使用

|  |
| --- |
| **Parameter:** `callback` |
| **类型**：character vector |
| **Value:** MATLAB expression |
| **默认值**：`''` |

### **Stop simulation when assertion fails** — 断言失败时停止仿真 `off`（默认）| `on`

当信号在仿真期间违反**边界**选项卡中指定的边界时，即断言失败时，停止仿真。

如果您从 Simulink 模型窗口运行仿真，则会打开“仿真诊断”窗口以显示错误消息。模型中发生边界违反的模块会高亮显示。

由于选择此选项会在断言失败时立即停止仿真，因此软件不会报告仿真期间可能稍后发生的断言失败。如果您想报告*所有*断言失败，请不要选择此选项。

#### 依赖关系

要启用此参数，请选择**启用断言**。

#### 编程使用

|  |
| --- |
| **Parameter:** `stopWhenAssertionFail` |
| **类型**：character vector |
| **Value:** `'on'` | `'off'` |
| **默认值**：`'off'` |

### **Output assertion signal** — 创建输出信号 `off`（默认）| `on`

输出一个布尔信号，该信号在每个时间步为：

- 如果断言成功，即输入信号满足所有边界，则为 true（`1`）
- 如果断言失败，即输入信号违反某个边界，则为 false（`0`）

输出信号的数据类型默认是 double。要将 Simulink 模型中所有生成逻辑信号的模块的输出数据类型设置为 Boolean，请在配置参数中选择 Implement logic signals as Boolean data。

选择此参数会向模块添加一个输出端口，您可以将其连接到模型中的任何模块。

使用此参数可设计复杂的断言逻辑。有关示例，请参阅 Verify Model Using Simulink Control Design and Simulink Verification Blocks (Simulink Control Design)。

#### 编程使用

|  |
| --- |
| **Parameter:** `export` |
| **类型**：character vector |
| **Value:** `'on'` | `'off'` |
| **默认值**：`'off'` |

## 所属库

Simulink Design Optimization / Model Verification Simulink Design Optimization / Signal Constraints

## 模块特性

Not documented in R2025b.

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

仅当启用 **Output assertion signal** 参数时，代码生成才可用。

## 版本历史

**在 R2011b 中引入**

## 描述

检查模型信号在仿真期间是否满足边界

检查信号在仿真期间是否满足指定的上下界。

- 如果信号满足所有边界，该模块不执行任何操作。
- 如果信号不满足某个边界，MATLAB® 命令窗口中将出现警告消息。您还可以指定该模块：

  - 计算 MATLAB 表达式。
  - 停止仿真并返回错误消息。

在仿真期间，该模块还可以返回一个逻辑断言信号。

- 如果信号满足所有边界，断言信号为 true
  (`1`)。
- 如果信号不满足某个边界，断言信号为 false
  (`0`)。

使用该模块，您可以创建：

- 具有一条边的单个边界
- 具有多条边的单个边界
- 多个边界

您可以将 Check Custom Bounds 模块添加到多个信号，以检查它们是否满足边界。您还可以在时间图上绘制边界，以图形方式验证信号是否满足边界。

该模块以及 Model Verification 库中的其他模块用于测试信号是否保持在指定的时域特性边界内。当模型未违反任何边界时，您可以通过清除断言选项来禁用该模块。如果您修改了模型，可以重新启用断言，以确保您的更改不会导致模型违反边界。

如果信号不满足边界，您可以优化模型参数以满足边界。如果您拥有 Simulink® Control Design™ 软件，可以添加频域边界（例如 Bode 幅值），并优化模型响应以满足时域和频域要求。

该模块可用于所有仿真模式下的信号监视，但仅可在 `Normal` 或 `Accelerator` 仿真模式下用于响应优化。
