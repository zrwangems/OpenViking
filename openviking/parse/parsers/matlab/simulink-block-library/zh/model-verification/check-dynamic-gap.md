---
type: simulink-block
title: 'Check Dynamic Gap'
family: model-verification
documentation_release: R2025b
official_category: 'Model Verification'
documentation_page: 'checkdynamicgap'
language: zh-CN
chinese_source: worker-translation
---

# Check Dynamic Gap



检查可能变化宽度的间隙是否出现在信号幅度范围内

## 库

Simulink / Model Verification HDL Coder / Model Verification

## 描述

Check Dynamic Gap 模块检查信号在每个时间步是否落在某个值范围之外，并在比较后执行断言。间隙的宽度可以随每个时间步变化。**u** 端口是被测试的输入信号。输入 **min** 和 **max** 分别指定间隙的下界和上界。如果 **u** 落在由 **min** 和 **max** 定义的间隙之外，则断言为 `true (1)`，并且模块不执行任何操作。否则，默认情况下，模块会停止仿真并返回错误消息。

输入信号可以是标量、向量或矩阵。所有三个输入信号必须具有相同的数据类型。根据信号的不同，模块将 **u** 的值与边界进行比较的方式也不同。

- 当将标量与向量或矩阵进行比较时，模块将标量信号与非标量信号的每个元素进行比较。
- 当将向量或矩阵信号与其他向量或矩阵进行比较时，模块按元素将输入与边界进行比较。
- 对于具有多个向量或矩阵输入信号的模型，这些向量或矩阵必须具有相同的维度。

## 端口

### 输入

### **max** — 动态间隙的上界 标量 | 向量 | 矩阵

用于指定间隙上界的信号。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **min** — 动态间隙的下界 标量 | 向量 | 矩阵

用于指定间隙下界的信号。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **u** — 根据间隙检查的输入信号 标量 | 向量 | 矩阵

根据由 **max** 和 **min** 指定的宽度检查间隙的输入信号。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### 输出

### **Port\_1** — 断言输出信号 标量

输出信号，如果断言成功则为 `true (1)`，如果断言失败则为 `false (0)`。如果在配置参数窗口中，在 **数学和数据类型** 部分下的 **高级参数** 中，选择 **将逻辑信号实现为布尔数据**，则输出数据类型为 `Boolean`。否则，该信号的数据类型为 `double`。

#### 依赖关系

要启用此输出端口，请选中 **输出断言信号** 参数复选框。

**数据类型：** `double` | `Boolean`

## 参数

### **启用断言** — 启用或禁用检查 `on`（默认） | `off`

清除此参数将禁用该模块，并使模型的行为如同该模块不存在。要启用或禁用所有验证模块（无论此选项的设置如何），请转到配置参数窗口，单击 **诊断** > **数据有效性**，展开 **高级参数** 部分，并将 **模型验证模块启用** 设置为 `Enable all` 或 `Disable all`。

#### 程序化使用

|  |
| --- |
| **参数：** `enabled` |
| **类型：** string scalar or character vector |
| **值：** `"on"` | `"off"` |
| **默认：** `"on"` |

### **断言失败时的仿真回调（可选）** — 断言失败时要计算的表达式 `""`（默认） | MATLAB 表达式

指定断言失败时要计算的 MATLAB® 表达式。由于该表达式在 MATLAB 工作区中计算，请在该工作区中定义表达式中使用的所有变量。

#### 依赖关系

要启用此参数，请选择 **启用断言**。

#### 程序化使用

|  |
| --- |
| **参数：** `callback` |
| **类型：** string scalar or character vector |
| **默认：** `""` |

### **断言失败时停止仿真** — 检查失败时是否停止仿真 `on`（默认） | `off`

选择此参数可在检查失败时停止仿真。清除此参数可显示警告并继续仿真。

#### 程序化使用

|  |
| --- |
| **参数：** `stopWhenAssertionFail` |
| **类型：** string scalar or character vector |
| **值：** `"on"` | `"off"` |
| **默认：** `"on"` |

### **输出断言信号** — 创建输出信号 `off`（默认） | `on`

选择此参数以启用输出端口。

#### 程序化使用

|  |
| --- |
| **参数：** `export` |
| **类型：** string scalar or character vector |
| **值：** `"on"` | `"off"` |
| **默认：** `"off"` |

### **选择图标类型** — 选择图标类型 `graphic`（默认） | `text`

指定模块图标的样式。`graphic` 选项在图标上显示断言条件的图形表示。`text` 选项显示表示断言条件的数学表达式。

#### 程序化使用

|  |
| --- |
| **参数：** `icon` |
| **类型：** string scalar or character vector |
| **值：** `"graphic"` | `"text"` |
| **默认：** `"graphic"` |

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

有关 Simulink® Coder™ 生成的代码如何处理 Model Verification 模块的信息，请参阅 Configure Model for Debugging (Simulink Coder)。

不建议用于生产代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| `No HDL` | 不要为此模块生成 HDL 代码。 |

**HDL 模块属性**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | 控制未连接逻辑的移除。默认值为 `off`，这意味着未连接逻辑不会保留在 HDL 代码中。有关更多详细信息，请参阅 PreserveUpstreamLogic (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**
