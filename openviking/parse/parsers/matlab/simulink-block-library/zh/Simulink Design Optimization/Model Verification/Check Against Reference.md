---
type: simulink-block
title: 'Check Against Reference'
family: 'sldo'
product_id: 'sldo'
product_name: 'Simulink Design Optimization'
documentation_release: R2025b
official_category: 'Model Verification'
documentation_page: 'checkagainstreference'
documentation_source_path: 'ref/checkagainstreference.html'
language: zh-CN
chinese_source: worker-translation
---

# Check Against Reference

## 端口
```yaml
ports:
- name: Port_1 (u)
  summary: 要对照指定参考信号检查的信号 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point | enumerated
    | bus
- name: Port_1 (out)
  summary: 输出断言信号 1 | 0
  direction: output
  data_types: Boolean | double
```

### 输入

### **Port\_1 (u)** — 要对照指定参考信号检查的信号 标量 | 向量 | 矩阵

在仿真期间要对照 **Amplitudes** 和 **Times** 中指定的参考信号进行检查的信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `enumerated` | `bus`
### 输出

### **Port\_1 (out)** — 输出断言信号 `1` | `0`

输出信号，指示输入信号是否在指定断言信号的边界内。在每个时间步，输出返回为以下之一：

- 如果断言成功，即输入信号满足所有边界，则为 True (`1`)
- 如果断言失败，即信号违反某个边界，则为 False (`0`)

输出信号的数据类型默认为 double。要将 Simulink 模型中所有生成逻辑信号的模块的输出数据类型设置为 Boolean，请在配置参数中选择 Implement logic signals as Boolean data。

#### 依赖

要启用此端口，请在 **Assertion** 选项卡上选择 **Output assertion signal** 参数。

**数据类型：** `Boolean` | `double`
## 参数
```yaml
parameters:
- name: Show Plot
  summary: 打开绘图窗口 button
  group: ''
- name: Show plot on block open
  summary: 双击模块以打开绘图 off (默认) | on
  group: ''
  block_parameter: LaunchViewOnOpen
  type: 字符向量
  values: '''on'' | ''off'''
- name: Response Optimization
  summary: 打开 Response Optimizer button
  group: ''
- name: 在断言中包含参考信号跟踪
  summary: 检查信号是否跟踪参考信号 on（默认）| off
  group: Bounds 选项卡
  block_parameter: EnableReferenceBound
  type: 字符向量
  values: '''on'' | ''off'''
- name: Times
  summary: 时间向量 linspace(0,10)（默认）| 正值向量 | MATLAB 表达式
  group: Bounds 选项卡
  block_parameter: ReferenceTimes
  type: 向量
  values: 正值向量 | MATLAB 表达式
- name: Amplitudes
  summary: 参考信号幅值 1-exp(-linspace(0,10)/2)（默认）| 向量 | MATLAB 表达式
  group: Bounds 选项卡
  block_parameter: ReferenceAmplitudes
  type: 向量
  values: 向量 | MATLAB 表达式
- name: Absolute tolerance
  summary: 信号的绝对容差 eps^(1/3)（默认）| 正实数标量
  group: Bounds 选项卡
  block_parameter: AbsTolerance
  type: 标量
  values: 正实数标量
- name: Relative tolerance
  summary: 信号相对容差 0.01（默认）| 正实数标量
  group: Bounds 选项卡
  block_parameter: RelTolerance
  type: scalar
  values: positive real scalar
  default: '0.01'
- name: Enable assertion
  summary: 启用或禁用检查 on（默认）| off
  group: Assertion Tab
  block_parameter: enabled
  type: character vector
  values: '''on'' | ''off'''
  default: '''on'''
- name: Simulation callback when assertion fails (optional)
  summary: 断言失败时要求值的表达式 ''（默认）| MATLAB 表达式
  group: Assertion Tab
  block_parameter: callback
  type: character vector
  values: MATLAB expression
  default: ''''''
- name: Stop simulation when assertion fails
  summary: 断言失败时停止仿真 off（默认）| on
  group: Assertion Tab
  block_parameter: stopWhenAssertionFail
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: 输出断言信号
  summary: 创建输出信号 off（默认）| on
  group: Assertion Tab
  block_parameter: export
  type: 字符向量
  values: '''on'' | ''off'''
```

### **Show Plot** — 打开绘图窗口 `button`

使用绘图查看以下内容。

- 仿真期间计算的系统特性和信号 — 在仿真模型之前点击此按钮以查看系统特性或信号。

  您可以通过右键点击绘图并选择 **Characteristics** 来显示其他特性，例如峰值响应时间。
- 边界 — 您可以在 **Bounds** 选项卡上指定边界，或通过右键点击绘图并选择 **Bounds** > **New Bound** 来指定边界。

  您可以通过拖动边界段或右键点击绘图并选择 **Bounds** > **Edit Bound** 来修改边界。在仿真模型之前，点击 **Update Block** 以更新模块参数中的边界值。

您在绘图窗口中执行的典型任务包括：

- 通过点击 Open block parameters dialog 图标或选择 **Edit** 打开 Block Parameters 对话框。
- 通过点击 Highlight block 图标或选择 **View** > **Highlight Simulink Block** 找到绘图窗口对应的模块。此操作会使模型窗口处于活动状态并高亮显示该模块。
- 通过点击 Run 图标仿真模型。此操作还会对指定的线性化输入和输出之间的模型部分进行线性化。
- 通过点击 Insert legend 图标在线性系统特性图上添加图例。

### **Show plot on block open** — 双击模块以打开绘图 `off` (默认) | `on`

当您在 Simulink 模型中双击该模块时，打开绘图窗口而不是模块参数。

如果您希望在绘图窗口中打开并执行任务（例如添加或修改边界）而不是在模块参数中执行，请使用此参数。如果您想从绘图窗口访问模块参数，请选择 **Edit** 或点击 Open block parameters dialog 图标。

有关绘图的更多信息，请参阅 **Show plot** 参数。

#### 编程使用

|  |
| --- |
| **参数：** `LaunchViewOnOpen` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认：** `'off'` |

### **Response Optimization** — 打开 Response Optimizer `button`

打开 Response Optimizer 以优化模型响应，使其满足 **Bounds** 选项卡上指定的设计要求。

#### 另请参阅

- Design Optimization to Meet Step Response Requirements (GUI)
- Design Optimization to Meet Time-Domain and Frequency-Domain Requirements (GUI)

### Bounds 选项卡

### **在断言中包含参考信号跟踪** — 检查信号是否跟踪参考信号 `on`（默认）| `off`

检查模块的输入信号在仿真期间是否跟踪 **Amplitudes** 和 **Times** 中指定的参考信号。如果信号未跟踪参考信号，软件将显示警告。

- 禁用此参数时，软件在仿真期间停止检查输入信号是否跟踪参考信号。
- 若要在图上仅查看参考信号，请禁用 **Enable assertion**。

如果选择 **Show plot**，参考信号将显示在时间图上，如图所示。

参考信号的时间图

#### 依赖关系

要使用此参数，请在模块参数中选择 **Enable assertion**。当 **Enable assertion** 被禁用时，软件不会将参考信号用于断言，但参考信号仍会显示在图上。

#### 编程使用

|  |
| --- |
| **参数：** `EnableReferenceBound` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认：** `'on'` |

### **Times** — 时间向量 `linspace(0,10)`（默认）| 正值向量 | MATLAB 表达式

参考信号的时间向量，以秒为单位，指定为单调递增的正值向量。您也可以指定一个求值结果为向量的 MATLAB 表达式。使用 **Amplitudes** 参数指定对应的幅值。**Times** 向量必须与 **Amplitudes** 向量具有相同的维度。

#### 编程使用

|  |
| --- |
| **参数：** `ReferenceTimes` |
| **类型：** 向量 |
| **值：** 正值向量 | MATLAB 表达式 |
| **默认：** `linspace(0,10)` |

### **Amplitudes** — 参考信号幅值 `1-exp(-linspace(0,10)/2)`（默认）| 向量 | MATLAB 表达式

参考信号的幅值，指定为与 **Times** 中指定的时间向量对应的实数有限向量。您也可以指定一个求值结果为向量的 MATLAB 表达式。**Amplitudes** 向量必须与 **Times (seconds)** 向量具有相同的维度。

#### 编程使用

|  |
| --- |
| **参数：** `ReferenceAmplitudes` |
| **类型：** 向量 |
| **值：** 向量 | MATLAB 表达式 |
| **默认：** `1-exp(-linspace(0,10)/2)` |

### **Absolute tolerance** — 信号的绝对容差 `eps^(1/3)`（默认）| 正实数标量

用于在输入信号接近参考信号时确定边界的绝对容差，指定为正实数标量。在仿真期间，信号必须保持在参考信号各自的上限和下限范围内，由下式给出

*y*u = (1 +
*RelTol*)*y*r
+ *AbsTol*

*y*l = (1 –
*RelTol*)*y*r
– *AbsTol*

其中：

- *y*r 是某一时刻参考信号的值。
- *y*u 是对应于该时间点的容差上限。
- *y*l 是对应于该时间点的容差下限。
- *RelTol* 设置每个时间步输入信号与参考信号幅值之间的相对容差。要设置 *RelTol*，请使用 **Relative tolerance** 参数。
- *AbsTol* 设置每个时间步输入信号与参考信号幅值之间的绝对容差。要设置 *AbsTol*，请使用 **Absolute tolerance** 参数。

如果信号违反这些限制，模块将触发断言。

#### 编程使用

|  |
| --- |
| **参数：** `AbsTolerance` |
| **类型：** 标量 |
| **值：** 正实数标量 |
| **默认：** `eps^(1/3)` |

### **Relative tolerance** — 信号相对容差 `0.01`（默认）| 正实数标量

用于在输入信号接近参考信号时确定边界的相对容差，指定为正实数标量。在仿真期间，信号必须保持在参考信号的上限和下限范围内，由下式给出

*y*u = (1 +
*RelTol*)*y*r
+ *AbsTol*

*y*l = (1 –
*RelTol*)*y*r
– *AbsTol*

其中：

- *y*r 是某一时刻参考信号的值。
- *y*u 是容差上限。
- *y*l 是容差下限。
- *RelTol* 设置每个时间步输入信号与参考信号幅度之间的相对容差。要设置 *RelTol*，请使用 **Relative tolerance** 参数。
- *AbsTol* 设置每个时间步输入信号与参考信号幅度之间的绝对容差。要设置 *AbsTol*，请使用 **Absolute tolerance** 参数。

如果信号违反这些限制，模块将触发断言。

#### 编程使用

|  |
| --- |
| **Parameter:** `RelTolerance` |
| **类型**：scalar |
| **Value:** positive real scalar |
| **默认值**：`0.01` |

### Assertion Tab

### **Enable assertion** — 启用或禁用检查 `on`（默认）| `off`

启用模块以检查在 **Bounds** 选项卡中指定并包含用于断言的边界在仿真期间是否得到满足。如果边界未满足，断言将失败。MATLAB 命令提示符处将出现报告断言失败的警告。

如果断言失败，您可以选择指定模块：

- 执行在 **Simulation callback when assertion fails (optional)** 中指定的 MATLAB 表达式。
- 通过选择 **Stop simulation when assertion fails** 停止仿真并返回错误消息。

如果您未指定任何边界，此参数无效。

当您禁用此参数时，模块不再检查输入信号是否满足指定的边界。模块图标也会更新以指示断言已禁用。

带叉的模块图标

在 Simulink 模型中，在 Configuration Parameters 中，**Model Verification block enabling** 参数允许您启用或禁用模型中的所有模型验证模块，而不管模块中此选项的设置如何。

#### 编程使用

|  |
| --- |
| **Parameter:** `enabled` |
| **类型**：character vector |
| **Value:** `'on'` | `'off'` |
| **默认值**：`'on'` |

### **Simulation callback when assertion fails (optional)** — 断言失败时要求值的表达式 `''`（默认）| MATLAB 表达式

断言失败时要执行的 MATLAB 表达式。

由于该表达式在 MATLAB 工作区中求值，请先在工作区中定义表达式中使用的所有变量。

#### 依赖关系

要启用此参数，请选择 **Enable assertion**。

#### 编程使用

|  |
| --- |
| **Parameter:** `callback` |
| **类型**：character vector |
| **Value:** MATLAB expression |
| **默认值**：`''` |

### **Stop simulation when assertion fails** — 断言失败时停止仿真 `off`（默认）| `on`

当输入信号在仿真期间违反 **Bounds** 选项卡中指定的边界时，即断言失败时，停止仿真。

如果您从 Simulink 模型窗口运行仿真，Simulation Diagnostics 窗口将打开以显示错误消息。模型中发生边界违反的模块将被高亮显示。

由于选择此选项会在断言失败时立即停止仿真，软件不会报告仿真期间可能稍后发生的断言失败。如果您想报告*所有*断言失败，请不要选择此选项。

#### 依赖关系

要启用此参数，请选择 **Enable assertion**。

#### 编程使用

|  |
| --- |
| **Parameter:** `stopWhenAssertionFail` |
| **类型**：character vector |
| **Value:** `'on'` | `'off'` |
| **默认值**：`'off'` |

### **输出断言信号** — 创建输出信号 `off`（默认）| `on`

输出一个布尔信号，在每个时间步为：

- 如果断言成功，即为 True（`1`），也就是说，
  输入信号满足所有边界
- 如果断言失败，即为 False（`0`），也就是说，
  输入信号违反某个边界

默认情况下，输出信号的数据类型为 double。要将 Simulink 模型中所有生成逻辑信号的模块的输出数据类型设置为 Boolean，请在配置参数中选择“将逻辑信号实现为布尔数据”。

选择此参数会为模块添加一个输出端口，您可以将其连接到模型中的任何模块。

使用此参数可设计复杂的断言逻辑。有关示例，请参阅 Verify Model Using Simulink Control Design and Simulink Verification Blocks (Simulink Control Design)。

#### 程序化使用

|  |
| --- |
| **参数：** `export` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认：** `'off'` |
## 所属库

Simulink Design Optimization / Model Verification Simulink Design Optimization / Signal Constraints

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

仅当启用 **输出断言信号** 参数时，代码生成才可用。

## 版本历史

**在 R2011b 中引入**

## 描述

在仿真期间检查模型信号是否跟踪参考信号

在仿真期间检查信号是否保持在参考信号的容差边界内。

- 如果信号满足所有边界，模块不执行任何操作。
- 如果信号不满足某个边界，MATLAB® 命令窗口中会出现警告消息。您还可以指定模块：

  - 计算 MATLAB 表达式。
  - 停止仿真并返回错误消息。

在仿真期间，模块还可以返回逻辑断言信号。

- 如果信号满足所有边界，断言信号为 true
  （`1`）。
- 如果信号不满足某个边界，断言信号为 false
  （`0`）。

您可以将 Check Against Reference 模块添加到多个信号，以检查它们是否跟踪参考信号。您还可以在时间图上绘制参考信号，以图形方式验证信号跟踪。

此模块以及 Model Verification 库中的其他模块用于测试信号是否保持在指定的时域特性边界内。当模型未违反任何边界时，您可以通过清除断言选项来禁用该模块。如果修改模型，您可以重新启用断言，以确保您的更改不会导致模型违反边界。

如果信号不满足边界，您可以优化模型参数以满足边界。如果您拥有 Simulink® Control Design™ 软件，则可以添加频域边界，例如 Bode 幅值，并优化模型响应以满足时域和频域要求。

该模块可用于所有仿真模式下的信号监视，但仅可在 `Normal` 或 `Accelerator` 仿真模式下用于响应优化。
