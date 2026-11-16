---
type: simulink-block
title: 'Check Discrete Gradient'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Model Verification'
documentation_page: 'checkdiscretegradient'
documentation_source_path: 'slref/checkdiscretegradient.html'
language: zh-CN
chinese_source: worker-translation
---

# Check Discrete Gradient



检查离散信号连续样本之间差值的绝对值是否小于指定值

## 库

Simulink / Model Verification HDL Coder / Model Verification

## 描述

Check Discrete Gradient 模块检查每个信号元素，并确定该元素在连续值之间差值的绝对值是否小于指定值。该模块随后在比较后执行断言。您可以通过调整 **最大梯度** 参数来指定梯度值（默认值为 `1`）。如果输入信号差值小于 **最大梯度** 的绝对值，则断言为 `true (1)`，并且该模块不执行任何操作。否则，该模块会停止仿真，并默认返回错误消息。

**注意**

要运行仿真，Check Discrete Gradient 模块需要固定步长离散求解器。如果选择了其他求解器，则会提示错误。

## 端口

### 输入

### **Port\_1** — 输入信号，对照梯度检查 标量 | 向量 | 矩阵

模块检查的输入信号，用于确定每个元素在连续样本之间的差值是否小于 **最大梯度** 参数的绝对值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 断言输出信号 标量

如果断言成功，则输出信号为 `true (1)`；如果断言失败，则为 `false (0)`。如果在配置参数窗口中，在 **数学和数据类型** 部分下的 **高级参数** 下，选择 **将逻辑信号实现为布尔数据**，则输出数据类型为 `Boolean`。否则，信号的数据类型为 `double`。

#### 依赖项

要启用此输出端口，请选中 **输出断言信号** 参数复选框。

**数据类型：** `double` | `Boolean`

## 参数

### **最大梯度** — 允许差值的最大值 `1`（默认）| 标量

指定输入信号允许的梯度值。

#### 编程用法

|  |
| --- |
| **参数：** `gradient` |
| **类型：** string scalar or character vector |
| **值：** real scalar |
| **默认值：** `"1"` |

### **启用断言** — 启用或禁用检查 `on`（默认）| `off`

清除此参数将禁用该模块，并使模型的行为如同该模块不存在。要启用或禁用所有验证模块（无论此选项的设置如何），请转到配置参数窗口，单击 **诊断** > **数据有效性**，展开 **高级参数** 部分，然后将 **模型验证模块启用** 设置为 `Enable all` 或 `Disable all`。

#### 编程用法

|  |
| --- |
| **参数：** `enabled` |
| **类型：** string scalar or character vector |
| **值：** `"on"` | `"off"` |
| **默认值：** `"on"` |

### **断言失败时的仿真回调（可选）** — 断言失败时要计算的表达式 `""`（默认）| MATLAB expression

指定断言失败时要计算的 MATLAB® 表达式。由于该表达式在 MATLAB 工作区中计算，因此请在该工作区中定义表达式中使用的所有变量。

#### 依赖项

要启用此参数，请选择 **启用断言**。

#### 编程用法

|  |
| --- |
| **参数：** `callback` |
| **类型：** string scalar or character vector |
| **默认值：** `""` |

### **断言失败时停止仿真** — 检查失败时是否停止仿真 `on`（默认）| `off`

选择此参数可在检查失败时停止仿真。清除此参数可显示警告并继续仿真。

#### 编程用法

|  |
| --- |
| **参数：** `stopWhenAssertionFail` |
| **类型：** string scalar or character vector |
| **值：** `"on"` | `"off"` |
| **默认值：** `"on"` |

### **输出断言信号** — 创建输出信号 `off`（默认）| `on`

选择此参数可启用输出端口。

#### 编程用法

|  |
| --- |
| **参数：** `export` |
| **类型：** string scalar or character vector |
| **值：** `"on"` | `"off"` |
| **默认值：** `"off"` |

### **选择图标类型** — 选择图标类型 `graphic`（默认）| `text`

指定模块图标的样式。`graphic` 选项在图标上显示断言条件的图形表示。`text` 选项显示表示断言条件的数学表达式。

#### 编程用法

|  |
| --- |
| **参数：** `icon` |
| **类型：** string scalar or character vector |
| **值：** `"graphic"` | `"text"` |
| **默认值：** `"graphic"` |

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

有关 Simulink® Coder™ 生成的代码如何处理 Model Verification 模块的信息，请参阅 Configure Model for Debugging (Simulink Coder)。

不建议用于生产代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了会影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| `No HDL` | 不为此模块生成 HDL 代码。 |

**HDL 模块属性**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | 控制未连接逻辑的删除。默认值为 `off`，这意味着未连接逻辑不会保留在 HDL 代码中。有关更多详细信息，请参阅 PreserveUpstreamLogic (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**R2006a 之前引入**
