---
type: simulink-block
title: 'Check Input Resolution'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Model Verification'
documentation_page: 'checkinputresolution'
documentation_source_path: 'slref/checkinputresolution.html'
language: zh-CN
chinese_source: worker-translation
---

# Check Input Resolution

## 端口

### 输入

### **Port\_1** — 对照分辨率检查的输入信号 标量 | 向量

模块对照 **分辨率** 参数指定的分辨率进行检查的输入信号。

**数据类型：** `double`
### 输出

### **Port\_1** — 断言输出信号 标量

输出信号，如果断言成功则为 `true (1)`，如果断言失败则为 `false (0)`。如果在配置参数窗口中，在 **数学和数据类型** 部分下的 **高级参数** 中，选择 **将逻辑信号实现为布尔数据**，则输出数据类型为 `Boolean`。否则，信号的数据类型为 `double`。

#### 依赖项

要启用此端口，请选择 **输出断言信号**。

**数据类型：** `double` | `Boolean`

## 参数

### **分辨率** — 要与输入信号比较的分辨率值 标量 | 向量

指定输入信号的分辨率要求。

#### 编程用法

|  |
| --- |
| **参数：** `resolution` |
| **类型：** 字符串标量或字符向量 |
| **默认值：** `"1"` |

### **启用断言** — 启用或禁用检查 `on`（默认）| `off`

清除此参数会禁用该模块，并使模型的行为如同该模块不存在。要启用或禁用所有验证模块，而不考虑此选项的设置，请转到配置参数窗口，点击 **诊断** > **数据有效性**，展开 **高级参数** 部分，并将 **模型验证模块启用** 设置为 `Enable all` 或 `Disable all`。

#### 编程用法

|  |
| --- |
| **参数：** `enabled` |
| **类型：** 字符串标量或字符向量 |
| **值：** `"on"` | `"off"` |
| **默认值：** `"on"` |

### **断言失败时的仿真回调（可选）** — 断言失败时要计算的表达式 `""`（默认）| MATLAB 表达式

指定断言失败时要计算的 MATLAB® 表达式。由于该表达式在 MATLAB 工作区中计算，请在该工作区中定义表达式中使用的所有变量。

#### 依赖项

要启用此参数，请选择 **启用断言**。

#### 编程用法

|  |
| --- |
| **参数：** `callback` |
| **类型：** 字符串标量或字符向量 |
| **默认值：** `""` |

### **断言失败时停止仿真** — 检查失败时是否停止仿真 `on`（默认）| `off`

选择此参数可在检查失败时停止仿真。清除此参数可显示警告并继续仿真。

#### 编程用法

|  |
| --- |
| **参数：** `stopWhenAssertionFail` |
| **类型：** 字符串标量或字符向量 |
| **值：** `"on"` | `"off"` |
| **默认值：** `"on"` |

### **输出断言信号** — 创建输出信号 `off`（默认）| `on`

选择此参数可启用输出端口。

#### 编程用法

|  |
| --- |
| **参数：** `export` |
| **类型：** 字符串标量或字符向量 |
| **值：** `"on"` | `"off"` |
| **默认值：** `"off"` |

## 所属库

Simulink / Model Verification HDL Coder / Model Verification

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

有关 Simulink® Coder™ 生成的代码如何处理 Model Verification 模块的信息，请参阅 Configure Model for Debugging (Simulink Coder)。

不建议用于生产代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块可用于在仿真期间检查输入信号是否具有指定的分辨率，但它不包含在生成的代码中。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

检查输入信号是否具有指定的分辨率

Check Input Resolution 模块检查输入信号是否具有指定的分辨率。模块输入和分辨率可以是标量或向量。输入和分辨率必须具有相同的数据类型。

如果 **分辨率** 参数是标量，该模块计算输入信号对提供的标量分辨率取模的结果。然后将计算得到的模与容差 `10e-3` 进行比较，并在比较后执行断言。如果模小于容差，则断言为 `true (1)`，该模块不执行任何操作。否则，默认情况下该模块会停止仿真并返回错误消息。如果 **分辨率** 参数是向量，则当输入信号的值等于分辨率向量中的任一元素时，它会断言为 `true (1)`。

根据信号和分辨率的维度，该模块还会以几种其他方式将输入与分辨率进行比较。

- 将标量输入信号或分辨率与向量输入信号或分辨率进行比较时，该模块会将标量与向量的每个元素进行比较。
- 将向量输入信号与向量分辨率进行比较时，该模块会逐元素地将输入信号与分辨率进行比较。
- 对于输入信号和分辨率均为向量的模型，输入信号和分辨率必须具有相同的维度。
