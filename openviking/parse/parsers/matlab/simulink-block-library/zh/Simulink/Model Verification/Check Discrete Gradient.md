---
type: simulink-block
title: 'Check Discrete Gradient'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Model Verification'
documentation_page: 'checkdiscretegradient'
documentation_source_path: '../simulink/slref/checkdiscretegradient.html'
language: zh-CN
chinese_source: worker-translation
---

# Check Discrete Gradient

## 端口

### 输入

### **Port\_1** — 根据梯度检查的输入信号 标量 | 向量 | 矩阵

该模块检查的输入信号，用于确定相邻样本之间每个元素的差值是否小于 **最大梯度** 参数的绝对值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 断言输出信号 标量

输出信号，如果断言成功则为 `true (1)`，如果断言失败则为 `false (0)`。如果在配置参数窗口的 **数学和数据类型** 部分中的 **高级参数** 下，选择 **将逻辑信号实现为布尔数据**，则输出数据类型为 `Boolean`。否则，信号的数据类型为 `double`。

#### 依赖关系

要启用此输出端口，请选中 **输出断言信号** 参数复选框。

**数据类型：** `double` | `Boolean`

## 参数

### **最大梯度** — 允许差值的最大值 `1`（默认） | 标量

指定输入信号允许梯度的值。

#### 编程使用

|  |
| --- |
| **参数：** `gradient` |
| **类型：** 字符串标量或字符向量 |
| **值：** 实标量 |
| **默认：** `"1"` |

### **启用断言** — 启用或禁用检查 `on`（默认） | `off`

清除此参数会禁用该模块，并使模型的行为如同该模块不存在。要启用或禁用所有验证模块，无论此选项的设置如何，请转到配置参数窗口，单击 **诊断** > **数据有效性**，展开 **高级参数** 部分，并将 **模型验证模块启用** 设置为 `Enable all` 或 `Disable all`。

#### 编程使用

|  |
| --- |
| **参数：** `enabled` |
| **类型：** 字符串标量或字符向量 |
| **值：** `"on"` | `"off"` |
| **默认：** `"on"` |

### **断言失败时的仿真回调（可选）** — 断言失败时要计算的表达式 `""`（默认） | MATLAB 表达式

指定在断言失败时要计算的 MATLAB® 表达式。由于该表达式在 MATLAB 工作区中计算，因此请在该工作区中定义表达式中使用的所有变量。

#### 依赖关系

要启用此参数，请选中 **启用断言**。

#### 编程使用

|  |
| --- |
| **参数：** `callback` |
| **类型：** 字符串标量或字符向量 |
| **默认：** `""` |

### **断言失败时停止仿真** — 检查失败时是否停止仿真 `on`（默认） | `off`

选中此参数可在检查失败时停止仿真。清除此参数将显示警告并继续仿真。

#### 编程使用

|  |
| --- |
| **参数：** `stopWhenAssertionFail` |
| **类型：** 字符串标量或字符向量 |
| **值：** `"on"` | `"off"` |
| **默认：** `"on"` |

### **输出断言信号** — 创建输出信号 `off`（默认） | `on`

选中此参数以启用输出端口。

#### 编程使用

|  |
| --- |
| **参数：** `export` |
| **类型：** 字符串标量或字符向量 |
| **值：** `"on"` | `"off"` |
| **默认：** `"off"` |

### **选择图标类型** — 选择图标类型 `graphic`（默认） | `text`

指定模块图标的样式。`graphic` 选项在图标上显示断言条件的图形表示。`text` 选项显示表示断言条件的数学表达式。

#### 编程使用

|  |
| --- |
| **参数：** `icon` |
| **类型：** 字符串标量或字符向量 |
| **值：** `"graphic"` | `"text"` |
| **默认：** `"graphic"` |

## 所属库

Simulink / Model Verification HDL Coder / Model Verification

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

有关 Simulink® Coder™ 生成的代码如何处理模型验证模块的信息，请参阅 Configure Model for Debugging (Simulink Coder)。

不建议用于生产代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| `No HDL` | 不为此模块生成 HDL 代码。 |

**HDL 模块属性**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | 控制未连接逻辑的移除。默认值为 `off`，这意味着未连接逻辑不会保留在 HDL 代码中。有关详细信息，请参阅 PreserveUpstreamLogic (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

检查离散信号相邻样本之间差值的绝对值是否小于指定值

Check Discrete Gradient 模块检查每个信号元素，并确定该元素的相邻值之间差值的绝对值是否小于指定值。该模块随后在比较后执行断言。您可以通过调整 **最大梯度** 参数来指定梯度值（默认 `1`）。如果输入信号差值小于 **最大梯度** 的绝对值，则断言为 `true (1)`，且该模块不执行任何操作。否则，默认情况下，该模块会停止仿真并返回错误消息。

**注意**

要运行仿真，Check Discrete Gradient 模块需要定步长离散求解器。如果选择了其他求解器，则会提示错误。
