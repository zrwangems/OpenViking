---
type: simulink-block
title: 'Check Step Response Characteristics'
family: 'sldo'
product_id: 'sldo'
product_name: 'Simulink Design Optimization'
documentation_release: R2025b
official_category: 'Model Verification'
documentation_page: 'checkstepresponsecharacteristics'
documentation_source_path: 'ref/checkstepresponsecharacteristics.html'
language: zh-CN
chinese_source: worker-translation
---

# Check Step Response Characteristics

## 端口
```yaml
ports:
- name: Port_1 (u)
  summary: 要对照指定边界检查的信号 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point | enumerated
    | bus
- name: Port_1 (out)
  summary: 输出断言信号 1 | 0
  direction: output
  data_types: Boolean | double
```

### 输入

### **Port\_1 (u)** — 要对照指定边界检查的信号 标量 | 向量 | 矩阵

在仿真期间要对照指定阶跃响应特性进行检查的信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `enumerated` | `bus`
### 输出

### **Port\_1 (out)** — 输出断言信号 `1` | `0`

输出信号，指示输入信号是否在指定断言信号的边界内。在每个时间步，输出返回为以下之一：

- 如果断言成功，即信号满足所有边界，则为 True (`1`)
- 如果断言失败，即信号违反某个边界，则为 False (`0`)

输出信号的数据类型默认为 double。要将 Simulink 模型中所有生成逻辑信号的模块的输出数据类型设置为 Boolean，请在配置参数中选择 **Implement logic signals as Boolean data**。

#### 依赖关系

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
- name: Include step response bound in assertion
  summary: 检查信号是否满足阶跃响应边界 on（默认）| off
  group: Bounds 选项卡
  block_parameter: EnableStepResponseBound
  type: character vector
  values: '''on'' | ''off'''
  default: '''on'''
- name: Step time
  summary: 阶跃响应边界开始的时间 0（默认）| 非负标量
  group: Bounds 选项卡
  block_parameter: StepTime
  type: character vector
  values: 非负标量
  default: '0'
- name: Initial value
  summary: 阶跃前的信号值 0（默认）| 标量
  group: Bounds 选项卡
  block_parameter: InitialValue
  type: character vector
  values: 标量
  default: '0'
- name: Final value
  summary: 阶跃后的信号值 1（默认）| 标量
  group: Bounds 选项卡
  block_parameter: FinalValue
  type: character vector
  values: 标量
  default: '1'
- name: Rise time
  summary: 达到阶跃范围指定百分比所需的时间 5（默认）| 正标量
  group: Bounds 选项卡
  block_parameter: RiseTime
  type: character vector
  values: positive scalar
  default: '5'
- name: '% Rise'
  summary: 上升时间的阶跃范围值百分比 80（默认）| 0–100 范围内的标量
  group: Bounds 选项卡
  block_parameter: PercentRise
  type: character vector
  values: scalar in range 0–100
  default: '80'
- name: Settling time (seconds)
  summary: 达到稳定范围所需的时间 7（默认）| 正标量
  group: Bounds 选项卡
  block_parameter: SettlingTime
  type: character vector
  values: positive scalar
  default: '7'
- name: '% Settling'
  summary: 最终值周围的稳定范围 1（默认）| 0–100 范围内的标量
  group: Bounds 选项卡
  block_parameter: PercentSettling
  type: character vector
  values: scalar in range 0–100
  default: '1'
- name: '% Overshoot'
  summary: 信号可以超出最终值的量 10（默认）| 范围 0–100 的标量
  group: Bounds 选项卡
  block_parameter: PercentOvershoot
  type: character vector
  values: scalar in range 0–100
  default: '10'
- name: '% Undershoot'
  summary: 信号可以低于初始值的量 1（默认）| 范围 0–100 的标量
  group: Bounds 选项卡
  block_parameter: PercentUndershoot
  type: character vector
  values: scalar in range 0–100
  default: '1'
- name: Enable zero-crossing detection
  summary: 在边界边缘处评估模型 on（默认）| off
  group: Bounds 选项卡
  block_parameter: ZeroCross
  type: character vector
  values: '''on'' | ''off'''
  default: '''on'''
- name: Enable assertion
  summary: 启用或禁用检查 on（默认）| off
  group: Assertion Tab
  block_parameter: enabled
  type: character vector
  values: '''on'' | ''off'''
  default: '''on'''
- name: Simulation callback when assertion fails (optional)
  summary: 断言失败时要计算的表达式 ''（默认）| MATLAB 表达式
  group: Assertion Tab
  block_parameter: callback
  type: 字符向量
  values: MATLAB 表达式
- name: Stop simulation when assertion fails
  summary: 断言失败时停止仿真 off（默认）| on
  group: Assertion Tab
  block_parameter: stopWhenAssertionFail
  type: 字符向量
  values: '''on'' | ''off'''
- name: Output assertion signal
  summary: 创建输出信号 off（默认）| on
  group: Assertion Tab
  block_parameter: export
  type: 字符向量
  values: '''on'' | ''off'''
```

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

如果您希望在绘图窗口中而不是模块参数中打开并执行任务（例如添加或修改边界），请使用此参数。如果您想从绘图窗口访问模块参数，请选择 **Edit** 或点击 Open block parameters dialog 图标。

有关绘图的详细信息，请参阅 **Show plot** 参数。

#### 编程用法

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

### **Include step response bound in assertion** — 检查信号是否满足阶跃响应边界 `on`（默认）| `off`

检查信号是否满足 **Bounds** 选项卡上指定的*所有*阶跃响应特性。如果信号违反指定的阶跃响应特性，软件将显示警告。

要在图上查看指定的阶跃响应边界，请点击 **Show Plot**。

图上显示的指定阶跃响应边界

默认情况下，线段表示以下阶跃响应要求：

- 幅值大于或等于 –0.01，直到上升时间为 5 秒，用于 1% 下冲
- 幅值大于或等于 0.8，在 5 到 7 秒之间，用于 80% 上升
- 幅值小于或等于 1.1，直到稳定时间为 7 秒，用于 10% 超调
- 幅值在 0.99 到 1.01 之间，超过稳定时间后，用于 1% 稳定

当您禁用此参数时，软件在仿真期间停止检查输入信号是否满足这些边界。边界线段也会在图上变灰。

图上变灰的边界线段

要仅在图上查看边界和输入信号，请清除 **Enable assertion**。

#### 依赖关系

要使用此参数，请在 **Assertion** 选项卡上选择 **Enable assertion**。如果清除 **Enable assertion**，软件不会将这些边界用于断言，但它们仍会继续显示在图上。

#### 编程使用

|  |
| --- |
| **Parameter:** `EnableStepResponseBound` |
| **类型**：character vector |
| **Value:** `'on'` | `'off'` |
| **默认值**：`'on'` |

### **Step time** — 阶跃响应边界开始的时间 `0`（默认）| 非负标量

阶跃响应边界开始的时间，以秒为单位，指定为有限、实数、非负标量。

要从绘图窗口修改阶跃时间值，请拖动相应的边界线段。或者，右键点击该线段，然后选择 **Edit**。在 **Step time** 中指定新值。在仿真模型之前点击 **Update Block**。

要检查输入信号是否满足阶跃时间值，请同时选择 **Include step response bound in assertion** 和 **Enable assertion**。

#### 编程使用

|  |
| --- |
| **Parameter:** `StepTime` |
| **类型**：character vector |
| **Value:** 非负标量 |
| **默认值**：`0` |

### **Initial value** — 阶跃前的信号值 `0`（默认）| 标量

阶跃发生前的信号值，指定为不等于 **Final value** 参数的有限实数标量。

要从绘图窗口修改初始值，请拖动相应的边界线段。或者，右键点击该线段，然后选择 **Edit**。在 **Initial value** 中指定新值。在仿真模型之前点击 **Update Block**。

要检查输入信号是否满足初始值，请同时选择 **Include step response bound in assertion** 和 **Enable assertion**。

#### 编程使用

|  |
| --- |
| **Parameter:** `InitialValue` |
| **类型**：character vector |
| **Value:** 标量 |
| **默认值**：`0` |

### **Final value** — 阶跃后的信号值 `1`（默认）| 标量

阶跃发生后的信号值，指定为不等于 **Initial value** 参数的有限实数标量。

要从绘图窗口修改最终值，请拖动相应的边界线段。或者，右键点击该线段，然后选择 **Edit**。在 **Final value** 中指定新值。您必须在仿真模型之前点击 **Update Block**。

要检查输入信号是否满足最终值，请同时选择 **Include step response bound in assertion** 和 **Enable assertion**。

#### 编程使用

|  |
| --- |
| **Parameter:** `FinalValue` |
| **类型**：character vector |
| **Value:** 标量 |
| **默认值**：`1` |

### **Rise time** — 达到阶跃范围指定百分比所需的时间 `5`（默认）| 正标量

信号达到 **% Rise** 中指定的阶跃范围百分比（**Final value** – **Initial value**）所需的时间，以秒为单位，指定为小于 **Settling time** 参数的有限、正、实标量。

要从绘图窗口修改上升时间，请拖动相应的边界段。或者，右键单击该段，然后选择 **Edit**。在 **Rise time** 中指定新值。在仿真模型之前单击 **Update Block**。

要检查输入信号是否满足上升时间值，请同时选择 **Include step response bound in assertion** 和 **Enable assertion**。

#### 编程使用

|  |
| --- |
| **Parameter:** `RiseTime` |
| **类型**：character vector |
| **Value:** positive scalar |
| **默认值**：`5` |

### **% Rise** — 上升时间的阶跃范围值百分比 `80`（默认）| 0–100 范围内的标量

与 **Rise time** 一起用于定义整体上升时间特性的阶跃范围值百分比，指定为 0–100 范围内的实有限标量，且小于 100 – **% Settling**。

要从绘图窗口修改上升百分比，请拖动相应的边界段。或者，右键单击该段，然后选择 **Edit**。在 **% Rise** 中指定新值。在仿真模型之前单击 **Update Block**。

要检查输入信号是否满足上升百分比值，请同时选择 **Include step response bound in assertion** 和 **Enable assertion**。

#### 编程使用

|  |
| --- |
| **Parameter:** `PercentRise` |
| **类型**：character vector |
| **Value:** scalar in range 0–100 |
| **默认值**：`80` |

### **Settling time (seconds)** — 达到稳定范围所需的时间 `7`（默认）| 正标量

信号在最终值附近的指定范围内稳定所需的时间，以秒为单位，指定为大于 **Rise time** 的有限正实标量。该稳定范围定义为最终值加上或减去稳定范围值。在 **% Settling** 参数中指定稳定范围。

要从绘图窗口修改稳定时间，请拖动相应的边界段。或者，右键单击该段，然后选择 **Edit**。在 **Settling time** 中指定新值。在仿真模型之前单击 **Update Block**。

要检查输入信号是否满足稳定时间值，请同时选择 **Include step response bound in assertion** 和 **Enable assertion**。

#### 编程使用

|  |
| --- |
| **Parameter:** `SettlingTime` |
| **类型**：character vector |
| **Value:** positive scalar |
| **默认值**：`7` |

### **% Settling** — 最终值周围的稳定范围 `1`（默认）| 0–100 范围内的标量

定义 **Settling time** 特性稳定范围的阶跃范围值（**Final value** – **Initial value**）百分比，指定为 0–100 范围内的实有限标量。指定的值应小于 100 – **% Rise** 和 **% Overshoot**。

要从绘图窗口修改稳定百分比，请拖动相应的边界段。或者，右键单击该段，然后选择 **Edit**。在 **% Settling** 中指定新值。在仿真模型之前单击 **Update Block**。

要检查输入信号是否满足稳定百分比值，请同时选择 **Include step response bound in assertion** 和 **Enable assertion**。

#### 编程使用

|  |
| --- |
| **Parameter:** `PercentSettling` |
| **类型**：character vector |
| **Value:** scalar in range 0–100 |
| **默认值**：`1` |

### **% Overshoot** — 信号可以超出最终值的量 `10`（默认）| 范围 0–100 的标量

信号在稳定之前可以超出最终值的量，指定为 0–100 范围内的正实数标量，且大于 **% Settling**。该量以阶跃范围的百分比指定。阶跃范围是最终值与初始值之间的差值。

要从绘图窗口修改超调百分比，请拖动相应的边界段。或者，右键单击该段，然后选择 **Edit**。在 **% Overshoot** 中指定新值。在仿真模型之前单击 **Update Block**。

要检查输入信号是否满足超调百分比值，请同时选择 **Include step response bound in assertion** 和 **Enable assertion**。

#### 编程使用

|  |
| --- |
| **Parameter:** `PercentOvershoot` |
| **类型**：character vector |
| **Value:** scalar in range 0–100 |
| **默认值**：`10` |

### **% Undershoot** — 信号可以低于初始值的量 `1`（默认）| 范围 0–100 的标量

信号在上升之前可以低于初始值的量，指定为 0–100 范围内的正实数标量。该量以阶跃范围的百分比指定。阶跃范围是最终值与初始值之间的差值。

要从绘图窗口修改下冲百分比，请拖动相应的边界段。或者，右键单击该段，然后选择 **Edit**。在 **% Undershoot** 中指定新值。在仿真模型之前单击 **Update Block**。

要检查输入信号是否满足下冲百分比值，请同时选择 **Include step response bound in assertion** 和 **Enable assertion**。

#### 编程使用

|  |
| --- |
| **Parameter:** `PercentUndershoot` |
| **类型**：character vector |
| **Value:** scalar in range 0–100 |
| **默认值**：`1` |

### **Enable zero-crossing detection** — 在边界边缘处评估模型 `on`（默认）| `off`

确保软件对模型进行仿真以在边界边缘处产生输出。在边界边缘处对模型进行仿真可防止仿真求解器遗漏信号在其边缘处满足该边界的断言。

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

启用该模块以检查在 **Bounds** 选项卡上指定并包含用于断言的边界在仿真期间是否得到满足。如果边界未得到满足，则断言失败。报告断言失败的警告会出现在 MATLAB 命令提示符处。

如果断言失败，您可以选择指定该模块：

- 执行 MATLAB 表达式，在 **Simulation callback when assertion fails (optional)** 中指定。
- 通过选择 **Stop simulation when assertion fails** 停止仿真并返回错误消息。

如果您未指定任何边界，则此参数无效。

当您禁用此参数时，该模块不再检查输入信号是否满足指定的边界。模块图标也会更新以指示断言已禁用。

带叉的模块图标

在 Simulink 模型中，在 Configuration Parameters 中，**Model Verification block enabling** 参数允许您启用或禁用模型中的所有模型验证模块，而不管该模块中此选项的设置如何。

#### 编程使用

|  |
| --- |
| **Parameter:** `enabled` |
| **类型**：character vector |
| **Value:** `'on'` | `'off'` |
| **默认值**：`'on'` |

### **Simulation callback when assertion fails (optional)** — 断言失败时要计算的表达式 `''`（默认）| MATLAB 表达式

断言失败时要执行的 MATLAB 表达式。

由于该表达式在 MATLAB 工作区中计算，请先在工作区中定义表达式中使用的所有变量。

#### 依赖关系

要启用此参数，请选择 **Enable assertion**。

#### 编程使用

|  |
| --- |
| **参数：** `callback` |
| **类型：** 字符向量 |
| **值：** MATLAB 表达式 |
| **默认：** `''` |

### **Stop simulation when assertion fails** — 断言失败时停止仿真 `off`（默认）| `on`

当输入信号在仿真期间违反 **Bounds** 选项卡上指定的边界时，即断言失败时，停止仿真。

如果从 Simulink 模型窗口运行仿真，将打开 Simulation Diagnostics 窗口以显示错误消息。模型中发生边界违反的模块会高亮显示。

由于选择此选项会在断言失败时立即停止仿真，因此软件不会报告仿真期间稍后可能发生的断言失败。如果要报告*所有*断言失败，请不要选择此选项。

#### 依赖关系

要启用此参数，请选择 **Enable assertion**。

#### 编程使用

|  |
| --- |
| **参数：** `stopWhenAssertionFail` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认：** `'off'` |

### **Output assertion signal** — 创建输出信号 `off`（默认）| `on`

输出一个布尔信号，在每个时间步为：

- 如果断言成功，即输入信号满足所有边界，则为 true（`1`）
- 如果断言失败，即输入信号违反边界，则为 false（`0`）

输出信号的数据类型默认是 double。要将 Simulink 模型中所有生成逻辑信号的模块的输出数据类型设置为 Boolean，请在 Configuration Parameters 中选择 Implement logic signals as Boolean data。

选择此参数会向模块添加一个输出端口，您可以将其连接到模型中的任何模块。

使用此参数设计复杂的断言逻辑。有关示例，请参阅 Verify Model Using Simulink Control Design and Simulink Verification Blocks (Simulink Control Design)。

#### 编程使用

|  |
| --- |
| **参数：** `export` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认：** `'off'` |
## 所属库

Simulink Design Optimization / Model Verification Simulink Design Optimization / Signal Constraints

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

仅当启用 **Output assertion signal** 参数时，代码生成才可用。

## 版本历史

**在 R2011b 中引入**

## 描述

在仿真期间检查模型信号是否满足阶跃响应边界

在仿真期间检查信号是否满足阶跃响应边界。

- 如果信号满足所有边界，则该模块不执行任何操作。
- 如果信号不满足某个边界，MATLAB® 命令窗口中将显示警告消息。您还可以指定该模块：

  - 计算 MATLAB 表达式。
  - 停止仿真并返回错误消息。

在仿真期间，该模块还可以返回一个逻辑断言信号。

- 如果信号满足所有边界，则断言信号为 true
  (`1`)。
- 如果信号不满足某个边界，则断言信号为 false
  (`0`)。

您可以将 Check Step Response Characteristics 模块添加到多个信号，以检查它们是否满足边界。您还可以在时间图上绘制边界，以图形方式验证信号是否满足边界。

该模块与 Model Verification 库中的其他模块用于测试信号是否保持在指定的时域特性边界内。当模型未违反任何边界时，您可以通过清除断言选项来禁用该模块。如果您修改了模型，可以重新启用断言，以确保您的更改不会导致模型违反边界。

如果信号不满足边界，您可以优化模型参数以满足边界。如果您拥有 Simulink®
Control Design™ 软件，您可以添加频域边界（例如 Bode 幅值），并优化模型响应以满足时域和频域要求。

该模块可用于所有仿真模式下的信号监测，但仅可在
`Normal` 或 `Accelerator` 仿真模式下用于响应优化。
