---
type: simulink-block
title: 'Check Dynamic Range'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Model Verification'
documentation_page: 'checkdynamicrange'
documentation_source_path: 'slref/checkdynamicrange.html'
language: zh-CN
chinese_source: worker-translation
---

# Check Dynamic Range



检查信号是否落在随每个时间步变化的幅值范围内

## 库

Simulink / Model Verification HDL Coder / Model Verification

## 说明

Check Dynamic Range 模块检查信号在每个时间步是否落在某个值范围内，并在比较后执行断言。该范围的宽度可以随每个时间步变化。**u** 端口是被测输入信号。**min** 和 **max** 端口分别是范围的下界和上界，其中 **min** 和 **max** 均为不包含的边界。如果 **u** 位于 **max** 和 **min** 之间，则断言为 `true (1)`，并且该模块不执行任何操作。否则，默认情况下该模块会停止仿真并返回错误消息。

输入信号可以是标量、向量或矩阵。所有三个输入信号必须具有相同的数据类型。该模块会根据信号以不同方式将 **u** 的值与边界进行比较。

- 当将标量与向量或矩阵进行比较时，该模块会将标量信号与非标量信号的每个元素进行比较。
- 当将向量或矩阵信号与其他向量或矩阵进行比较时，该模块会逐元素检查输入。
- 对于具有多个向量或矩阵输入信号的模型，这些向量或矩阵必须具有相同的维度。

## 端口

### 输入

### **max** — 动态范围检查的上界 标量 | 向量 | 矩阵

指定范围上界的信号。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **min** — 动态范围检查的下界 标量 | 向量 | 矩阵

指定范围下界的信号。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **u** — 针对范围检查的输入信号 标量 | 向量 | 矩阵

根据 **max** 和 **min** 端口指定的范围进行检查的信号。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
### 输出

### **Port\_1** — 断言输出信号 标量

如果断言成功，则输出信号为 `true (1)`；如果断言失败，则为 `false (0)`。如果在配置参数窗口中，在 **数学和数据类型** 部分下的 **高级参数** 中，选择 **将逻辑信号实现为布尔数据**，则输出数据类型为 `Boolean`。否则，该信号的数据类型为 `double`。

#### 依赖关系

要启用此端口，请选择 **输出断言信号** 参数。

**数据类型：** `double` | `Boolean`

## 参数

### **启用断言** — 启用或禁用检查 `on`（默认） | `off`

清除此参数会禁用该模块，并使模型的行为就像该模块不存在一样。要启用或禁用所有验证模块，无论此选项的设置如何，请转到配置参数窗口，单击 **诊断** > **数据有效性**，展开 **高级参数** 部分，并将 **模型验证模块启用** 设置为 `Enable all` 或 `Disable all`。

#### 编程使用

|  |
| --- |
| **参数：** `enabled` |
| **类型：** string scalar or character vector |
| **值：** `"on"` | `"off"` |
| **默认：** `"on"` |

### **断言失败时的仿真回调（可选）** — 断言失败时要求值的表达式 `""`（默认） | MATLAB expression

指定断言失败时要计算的 MATLAB® 表达式。由于该表达式在 MATLAB 工作区中计算，请在该工作区中定义表达式中使用的所有变量。

#### 依赖关系

要启用此参数，请选择 **启用断言**。

#### 编程使用

|  |
| --- |
| **参数：** `callback` |
| **类型：** string scalar or character vector |
| **默认：** `""` |

### **断言失败时停止仿真** — 检查失败时是否停止仿真 `on`（默认） | `off`

选择此参数可在检查失败时停止仿真。清除此参数可显示警告并继续仿真。

#### 编程使用

|  |
| --- |
| **参数：** `stopWhenAssertionFail` |
| **类型：** string scalar or character vector |
| **值：** `"on"` | `"off"` |
| **默认：** `"on"` |

### **输出断言信号** — 创建输出信号 `off`（默认） | `on`

选择此参数可启用输出端口。

#### 编程使用

|  |
| --- |
| **参数：** `export` |
| **类型：** string scalar or character vector |
| **值：** `"on"` | `"off"` |
| **默认：** `"off"` |

### **选择图标类型** — 选择图标类型 `graphic`（默认） | `text`

指定模块图标的样式。`graphic` 选项在图标上显示断言条件的图形表示。`text` 选项显示表示断言条件的数学表达式。

#### 编程使用

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

有关 Simulink®
Coder™ 生成的代码如何处理 Model Verification 模块的信息，请参阅 Configure Model for Debugging (Simulink Coder)。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

| 架构 | 说明 |
| --- | --- |
| `No HDL` | 不为此模块生成 HDL 代码。 |

**HDL 模块属性**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | 控制未连接逻辑的移除。默认值为 `off`，这意味着未连接逻辑不会保留在 HDL 代码中。有关更多详细信息，请参阅 PreserveUpstreamLogic (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**
