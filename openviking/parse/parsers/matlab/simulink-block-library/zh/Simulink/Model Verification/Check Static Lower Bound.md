---
type: simulink-block
title: 'Check Static Lower Bound'
family: 'model-verification'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Model Verification'
documentation_page: 'checkstaticlowerbound'
documentation_source_path: 'slref/checkstaticlowerbound.html'
language: zh-CN
chinese_source: worker-translation
---

# Check Static Lower Bound

## 端口

### 输入

### **Port\_1** — Input signal checked against bound scalar | vector | matrix

输入信号，根据 **下限** 参数指定的下限进行检查。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### 输出

### **Port\_1** — Assertion output signal scalar

断言输出信号，如果断言成功则为 `true (1)`，如果断言失败则为 `false (0)`。如果在配置参数窗口中，在 **数学和数据类型** 部分下的 **高级参数** 下，选择 **将逻辑信号实现为 Boolean 数据**，则输出数据类型为 `Boolean`。否则，信号的数据类型为 `double`。

#### 依赖关系

要启用此输出端口，请选中 **输出断言信号** 参数复选框。

**数据类型：** `double` | `Boolean`

## 参数

### **下限** — 下边界值 标量 | 向量 | 矩阵

指定输入信号可具有的幅度范围的下限。

#### 编程用法

|  |
| --- |
| **参数：** `min` |
| **类型：** string scalar or character vector |
| **默认：** `"0"` |

### **包含边界** — 在范围内包含下限 `on`（默认） | `off`

选中此复选框可使有效输入幅度范围包含下限。

#### 编程用法

|  |
| --- |
| **参数：** `min_included` |
| **类型：** string scalar character vector |
| **值：** `"on"` | `"off"` |
| **默认：** `"on"` |

### **启用断言** — 启用或禁用检查 `on`（默认） | `off`

清除此参数将禁用模块，并使模型的行为如同该模块不存在。要启用或禁用所有验证模块，而不考虑此选项的设置，请转到配置参数窗口，单击 **诊断** > **数据有效性**，展开 **高级参数** 部分，并将 **模型验证模块启用** 设置为 `Enable all` 或 `Disable all`。

#### 编程用法

|  |
| --- |
| **参数：** `enabled` |
| **类型：** string scalar or character vector |
| **值：** `"on"` | `"off"` |
| **默认：** `"on"` |

### **断言失败时的仿真回调（可选）** — 断言失败时要计算的表达式 `""`（默认） | MATLAB 表达式

指定断言失败时要计算的 MATLAB® 表达式。由于该表达式在 MATLAB 工作区中计算，因此请在该工作区中定义表达式中使用的所有变量。

#### 依赖关系

要启用此参数，请选择 **启用断言**。

#### 编程用法

|  |
| --- |
| **参数：** `callback` |
| **类型：** string scalar or character vector |
| **默认：** `""` |

### **断言失败时停止仿真** — 检查失败时是否停止仿真 `on`（默认） | `off`

选中此参数可在检查失败时停止仿真。清除此参数可显示警告并继续仿真。

#### 编程用法

|  |
| --- |
| **参数：** `stopWhenAssertionFail` |
| **类型：** string scalar or character vector |
| **值：** `"on"` | `"off"` |
| **默认：** `"on"` |

### **输出断言信号** — 创建输出信号 `off`（默认） | `on`

选中此参数以启用输出端口。

#### 编程用法

|  |
| --- |
| **参数：** `export` |
| **类型：** string scalar or character vector |
| **值：** `"on"` | `"off"` |
| **默认：** `"off"` |

### **选择图标类型** — 选择图标类型 `graphic`（默认） | `text`

指定模块图标的样式。`graphic` 选项在图标上显示断言条件的图形表示。`text` 选项显示表示断言条件的数学表达式。

#### 编程用法

|  |
| --- |
| **参数：** `icon` |
| **类型：** string scalar or character vector |
| **值：** `"graphic"` | `"text"` |
| **默认：** `"graphic"` |

## 所属库

Simulink / Model Verification HDL Coder / Model Verification

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

有关 Simulink® Coder™ 生成的代码如何处理 Model Verification 模块的信息，请参阅 Configure Model for Debugging (Simulink Coder)。

不推荐用于生产代码。

### HDL 代码生成

使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| `No HDL` | 不为此模块生成 HDL 代码。 |

**HDL 模块属性**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | 控制未连接逻辑的移除。默认值为 `off`，表示未连接逻辑不会保留在 HDL 代码中。有关更多详细信息，请参阅 PreserveUpstreamLogic (HDL Coder)。 |

### PLC 代码生成

使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

### 定点转换

使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

检查信号是否大于（或可选地等于）静态下限

Check Static Lower Bound 模块在每个时间步检查输入信号是否大于（或可选地等于）指定的下限，并在比较后执行断言。**下限** 参数定义下限。如果输入信号大于下限，则断言为 `true (1)`，模块不执行任何操作。否则，默认情况下模块会停止仿真并返回错误消息。

输入信号和边界可以是标量、向量或矩阵。输入和边界必须具有相同的数据类型。模块根据信号以不同方式将输入值与边界进行比较。

- 当将标量与向量或矩阵进行比较时，模块将标量与输入信号或边界（非标量）的每个元素进行比较。
- 当将向量或矩阵输入信号与向量或矩阵边界进行比较时，模块逐个元素地将输入信号与边界进行比较。
- 对于输入信号和边界均为向量或矩阵的模型，输入信号和边界必须具有相同的维度。
