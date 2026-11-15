---
type: simulink-block
title: 'Check Input Resolution'
family: model-verification
documentation_release: R2025b
official_category: 'Model Verification'
documentation_page: 'checkinputresolution'
language: zh-CN
chinese_source: worker-translation
---

# Check Input Resolution

## 端口

### 输入

### **Port\_1** — 根据分辨率检查的输入信号 标量 | 向量

模块根据 **Resolution** 参数指定的分辨率检查的输入信号。

**数据类型:** `double`
### 输出

### **Port\_1** — 断言输出信号 标量

输出信号，如果断言成功则为 `true (1)`，如果断言失败则为 `false (0)`。如果，在 Configuration Parameters 窗口中，在 **Math and Data Types** 部分下，在 **Advanced parameters** 下，您选择 **Implement logic signals as Boolean data**，则输出数据类型为 `Boolean`。否则，信号的数据类型为 `double`。

#### 依赖关系

要启用此端口，请选择 **Output assertion signal**。

**数据类型:** `double` | `Boolean`

## 参数

### **Resolution** — 用于与输入信号比较的分辨率值 标量 | 向量

指定输入信号的分辨率要求。

#### 编程用法

|  |
| --- |
| **参数:** `resolution` |
| **类型:** 字符串标量或字符向量 |
| **默认:** `"1"` |

### **Enable assertion** — 启用或禁用检查 `on`（默认）| `off`

清除此参数会禁用该模块，并使模型的行为如同该模块不存在一样。要启用或禁用所有验证模块，无论此选项的设置如何，请转到 Configuration Parameters 窗口，单击 **Diagnostics** > **Data Validity**，展开 **Advanced parameters** 部分，并将 **Model Verification block enabling** 设置为 `Enable all` 或 `Disable all`。

#### 编程用法

|  |
| --- |
| **参数:** `enabled` |
| **类型:** 字符串标量或字符向量 |
| **值:** `"on"` | `"off"` |
| **默认:** `"on"` |

### **Simulation callback when assertion fails (optional)** — 断言失败时要计算的表达式 `""`（默认）| MATLAB 表达式

指定断言失败时要计算的 MATLAB® 表达式。由于该表达式在 MATLAB 工作区中计算，因此请在该工作区中定义表达式中使用的所有变量。

#### 依赖关系

要启用此参数，请选择 **Enable assertion**。

#### 编程用法

|  |
| --- |
| **参数:** `callback` |
| **类型:** 字符串标量或字符向量 |
| **默认:** `""` |

### **Stop simulation when assertion fails** — 检查失败时是否停止仿真 `on`（默认）| `off`

选择此参数可在检查失败时停止仿真。清除此参数可显示警告并继续仿真。

#### 编程用法

|  |
| --- |
| **参数:** `stopWhenAssertionFail` |
| **类型:** 字符串标量或字符向量 |
| **值:** `"on"` | `"off"` |
| **默认:** `"on"` |

### **Output assertion signal** — 创建输出信号 `off`（默认）| `on`

选择此参数以启用输出端口。

#### 编程用法

|  |
| --- |
| **参数:** `export` |
| **类型:** 字符串标量或字符向量 |
| **值:** `"on"` | `"off"` |
| **默认:** `"off"` |

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

不推荐用于生产代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的附加配置选项。

**HDL Architecture**

此模块可用于在仿真期间检查输入信号是否具有指定的分辨率，但它不包含在生成的代码中。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

检查输入信号是否具有指定的分辨率

Check Input Resolution 模块检查输入信号是否具有指定的分辨率。模块输入和分辨率可以是标量或向量。输入和分辨率必须是相同的数据类型。

如果 **Resolution** 参数是标量，模块计算输入信号对提供的标量分辨率的模。然后将计算出的模与容差 `10e-3` 进行比较，并在比较后执行断言。如果模小于该容差，则断言为 `true (1)`，模块不执行任何操作。如果不是，则默认情况下，模块停止仿真并返回错误消息。如果 **Resolution** 参数是向量，则当输入信号的值等于分辨率向量中的任何元素时，它断言为 `true (1)`。

模块根据信号和分辨率的维度，以几种附加方式将输入与分辨率进行比较。

- 当将标量输入信号或分辨率与向量输入信号或分辨率进行比较时，模块将标量与向量的每个元素进行比较。
- 当将向量输入信号与向量分辨率进行比较时，模块将输入信号与分辨率逐元素进行比较。
- 对于输入信号和分辨率均为向量的模型，输入信号和分辨率必须具有相同的维度。
