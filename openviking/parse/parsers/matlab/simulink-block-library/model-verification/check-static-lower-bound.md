---
type: simulink-block
title: 'Check Static Lower Bound'
family: model-verification
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Model Verification'
documentation_page: 'checkstaticlowerbound'
---

# Check Static Lower Bound

Check that signal is greater than (or optionally equal to) static lower bound

## 中文

检查信号是否大于（或可选地等于）静态下限

### 库

Simulink / Model Verification HDL Coder / Model Verification

### 描述

Check Static Lower Bound 模块在每个时间步检查输入信号是否大于（或可选地等于）指定的下限，并在比较后执行断言。**下限** 参数定义下限。如果输入信号大于下限，则断言为 `true (1)`，模块不执行任何操作。否则，模块默认停止仿真并返回错误消息。

输入信号和边界可以是标量、向量或矩阵。输入和边界必须具有相同的数据类型。模块根据信号以不同方式将输入值与边界进行比较。

- 当将标量与向量或矩阵比较时，模块将标量与非标量输入信号或边界的每个元素进行比较。
- 当将向量或矩阵输入信号与向量或矩阵边界比较时，模块逐元素地将输入信号与边界进行比较。
- 对于输入信号和边界均为向量或矩阵的模型，输入信号和边界必须具有相同的维度。

### 端口

#### 输入

#### **Port\_1** — 输入信号与边界进行比较 标量 | 向量 | 矩阵

输入信号，根据 **下限** 参数指定的下限进行检查。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

#### 输出

#### **Port\_1** — 断言输出信号 标量

如果断言成功，则为 `true (1)`；如果断言失败，则为 `false (0)` 的输出信号。如果在配置参数窗口中，在 **数学和数据类型** 部分下，在 **高级参数** 下，选择 **将逻辑信号实现为 Boolean 数据**，则输出数据类型为 `Boolean`。否则，信号的数据类型为 `double`。

#### 依赖关系

要启用此输出端口，请选中 **输出断言信号** 参数复选框。

**数据类型：** `double` | `Boolean`

### 参数

#### **下限** — 下边界值 标量 | 向量 | 矩阵

指定输入信号可具有的幅度范围的下限。

#### 程序化使用

|  |
| --- |
| **参数：** `min` |
| **类型：** string scalar or character vector |
| **默认值：** `"0"` |

#### **包含边界** — 将下限包含在范围内 `on` (默认) | `off`

选中此复选框以使有效输入幅度的范围包含下限。

#### 程序化使用

|  |
| --- |
| **参数：** `min_included` |
| **类型：** string scalar character vector |
| **值：** `"on"` | `"off"` |
| **默认值：** `"on"` |

#### **启用断言** — 启用或禁用检查 `on` (默认) | `off`

清除此参数将禁用模块，并使模型的行为如同该模块不存在。要启用或禁用所有验证模块，而不考虑此选项的设置，请转到配置参数窗口，单击 **诊断** > **数据有效性**，展开 **高级参数** 部分，并将 **模型验证模块启用** 设置为 `Enable all` 或 `Disable all`。

#### 程序化使用

|  |
| --- |
| **参数：** `enabled` |
| **类型：** string scalar or character vector |
| **值：** `"on"` | `"off"` |
| **默认值：** `"on"` |

#### **断言失败时的仿真回调（可选）** — 断言失败时要计算的表达式 `""` (默认) | MATLAB 表达式

指定断言失败时要计算的 MATLAB® 表达式。由于该表达式在 MATLAB 工作区中计算，请在该工作区中定义表达式中使用的所有变量。

#### 依赖关系

要启用此参数，请选中 **启用断言**。

#### 程序化使用

|  |
| --- |
| **参数：** `callback` |
| **类型：** string scalar or character vector |
| **默认值：** `""` |

#### **断言失败时停止仿真** — 检查失败时是否停止仿真 `on` (默认) | `off`

选中此参数以在检查失败时停止仿真。清除此参数以显示警告并继续仿真。

#### 程序化使用

|  |
| --- |
| **参数：** `stopWhenAssertionFail` |
| **类型：** string scalar or character vector |
| **值：** `"on"` | `"off"` |
| **默认值：** `"on"` |

#### **输出断言信号** — 创建输出信号 `off` (默认) | `on`

选中此参数以启用输出端口。

#### 程序化使用

|  |
| --- |
| **参数：** `export` |
| **类型：** string scalar or character vector |
| **值：** `"on"` | `"off"` |
| **默认值：** `"off"` |

#### **选择图标类型** — 选择图标类型 `graphic` (默认) | `text`

指定模块图标的样式。`graphic` 选项在图标上显示断言条件的图形表示。`text` 选项显示表示断言条件的数学表达式。

#### 程序化使用

|  |
| --- |
| **参数：** `icon` |
| **类型：** string scalar or character vector |
| **值：** `"graphic"` | `"text"` |
| **默认值：** `"graphic"` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

有关 Simulink® Coder™ 生成的代码如何处理 Model Verification 模块的信息，请参阅 Configure Model for Debugging (Simulink Coder)。

不推荐用于生产代码。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| `No HDL` | 不为该模块生成 HDL 代码。 |

**HDL 模块属性**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | 控制未连接逻辑的移除。默认值为 `off`，这意味着未连接逻辑不会保留在 HDL 代码中。有关更多详细信息，请参阅 PreserveUpstreamLogic (HDL Coder)。 |

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史

**在 R2006a 之前引入**

## Libraries

Simulink / Model Verification HDL Coder / Model Verification

## Description

The Check Static Lower Bound block checks if an input signal is greater than
(or optionally equal to) a specified lower bound at each time step and executes an
assertion after comparison. The **Lower bound** parameter defines the
lower bound. If the input signal is greater than the lower bound, the assertion is
`true (1)` and the block does nothing. If not, the block halts the
simulation and returns an error message by default.

The input signal and bound can be scalars, vectors, or matrices. The input and the
bound must be the same data type. The block compares the value of the input to the bound
differently depending on the signal.

- When comparing scalars to vectors or matrices, the block compares the
  scalar to each element of the non-scalar input signal or bound.
- When comparing a vector or matrix input signal to a vector or matrix
  bound, the block compares the input signal to the bound
  element-by-element.
- For models with an input signal and bound that are both vectors or
  matrices, the input signal and bound must have the same dimensions.

## Ports

### Input

### **Port\_1** — Input signal checked against bound scalar | vector | matrix

Input signal checked against the lower bound specified by the
**Lower bound** parameter.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
### Output

### **Port\_1** — Assertion output signal scalar

Output signal that is `true (1)` if the assertion
succeeds and `false (0)` if the assertion fails. If, in
the Configuration Parameters window, in the **Math and Data
Types** section, under **Advanced
parameters**, you select **Implement logic signals
as Boolean data**, then the output data type is
`Boolean`. Otherwise, the data type of the signal
is `double`.

#### Dependencies

To enable this output port, select the **Output assertion signal**
parameter check box.

**Data Types:** `double` | `Boolean`

## Parameters

### **Lower bound** — Lower boundary value scalar | vector | matrix

Specify the lower bound on the range of amplitudes that the input signal
can have.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `min` |
| **Type:** string scalar or character vector |
| **Default:** `"0"` |

### **Inclusive boundary** — Include the lower bound in range `on` (default) | `off`

Select this check box to make the range of valid input amplitudes include
the lower bound.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `min_included` |
| **Type:** string scalar character vector |
| **Values:** `"on"` | `"off"` |
| **Default:** `"on"` |

### **Enable assertion** — Enable or disable check `on` (default) | `off`

Clearing this parameter disables the block and causes the model to behave as if the
block does not exist. To enable or disable all verification blocks, regardless of the
setting of this option, go to the Configuration Parameters window, click **Diagnostics** > **Data Validity**, expand the **Advanced parameters** section, and set
**Model Verification block enabling** to `Enable
all` or `Disable all`.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `enabled` |
| **Type:** string scalar or character vector |
| **Values:** `"on"` | `"off"` |
| **Default:** `"on"` |

### **Simulation callback when assertion fails (optional)** — Expression to evaluate when assertion fails `""` (default) | MATLAB expression

Specify a MATLAB® expression to evaluate when the assertion fails. Because the expression is
evaluated in the MATLAB workspace, define all variables used in the expression in that
workspace.

#### Dependencies

To enable this parameter, select **Enable assertion**.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `callback` |
| **Type:** string scalar or character vector |
| **Default:** `""` |

### **Stop simulation when assertion fails** — Whether to stop simulation when check fails `on` (default) | `off`

Select this parameter to stop the simulation when the check fails. Clear this
parameter to display a warning and continue the simulation.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `stopWhenAssertionFail` |
| **Type:** string scalar or character vector |
| **Values:** `"on"` | `"off"` |
| **Default:** `"on"` |

### **Output assertion signal** — Create output signal `off` (default) | `on`

Select this parameter to enable the output port.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `export` |
| **Type:** string scalar or character vector |
| **Values:** `"on"` | `"off"` |
| **Default:** `"off"` |

### **Select icon type** — Select icon type `graphic` (default) | `text`

Specify the style of the block icon. The `graphic` option displays a
graphical representation of the assertion condition on the icon. The
`text` option displays a mathematical expression that represents
the assertion condition.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `icon` |
| **Type:** string scalar or character vector |
| **Values:** `"graphic"` | `"text"` |
| **Default:** `"graphic"` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

For information about how Simulink®
Coder™ generated code handles Model Verification blocks, see Configure Model for Debugging (Simulink Coder).

Not recommended for production code.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

| Architecture | Description |
| --- | --- |
| `No HDL` | Do not generate HDL code for this block. |

**HDL Block Properties**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | Control the removal of unconnected logic. The default is `off`, which means unconnected logic is not preserved in HDL code. For more details, see PreserveUpstreamLogic (HDL Coder). |

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
