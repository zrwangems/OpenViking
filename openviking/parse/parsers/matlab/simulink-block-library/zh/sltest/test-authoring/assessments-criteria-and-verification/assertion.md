---
type: simulink-block
title: 'Assertion'
family: 'sltest'
product_id: 'sltest'
product_name: 'Simulink Test'
documentation_release: R2025b
official_category: 'Test Authoring / Assessments, Criteria, and Verification'
documentation_page: 'assertion'
documentation_source_path: '../simulink/slref/assertion.html'
language: zh-CN
chinese_source: worker-translation
---

# Assertion

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

断言检查的输入信号。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

## 参数

### **启用断言** — 启用或禁用检查 `on`（默认）| `off`

清除此参数将禁用该模块，并使模型的行为如同该模块不存在。要启用或禁用所有验证模块（无论此选项的设置如何），请转到配置参数窗口，单击 **诊断** > **数据有效性**，展开 **高级参数** 部分，并将 **模型验证模块启用** 设置为 `Enable all` 或 `Disable all`。

#### 编程用法

|  |
| --- |
| **参数：** `enabled` |
| **类型：** 字符串标量或字符向量 |
| **值：** `"on"` | `"off"` |
| **默认：** `"on"` |

### **断言失败时的仿真回调** — 断言失败时要计算的表达式 `""`（默认）| MATLAB 表达式

指定当断言失败时要计算的 MATLAB® 表达式。由于该表达式在 MATLAB 工作区中计算，请在该工作区中定义表达式中使用的所有变量。

#### 依赖项

要启用此参数，请选择 **启用断言**。

#### 编程用法

|  |
| --- |
| **参数：** `AssertionFailFcn` |
| **类型：** 字符串标量或字符向量 |
| **默认：** `''` |

### **断言失败时停止仿真** — 检查失败时是否停止仿真 `on`（默认）| `off`

选中此参数可在检查失败时停止仿真。清除此参数可显示警告并继续仿真。

#### 编程用法

|  |
| --- |
| **参数：** `stopWhenAssertionFail` |
| **类型：** 字符串标量或字符向量 |
| **值：** `"on"` | `"off"` |
| **默认：** `"on"` |

### **采样时间（-1 表示继承）** — 采样之间的时间间隔 `-1`（默认）| 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关更多信息，请参阅 Specify Sample Time。

#### 依赖项

仅当将此参数设置为 `-1` 以外的值时，此参数才可见。要了解更多信息，请参阅 Blocks for Which Sample Time Is Not Recommended。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `"-1"`（默认）| 带引号的标量或向量 |

## 所属库

Simulink / Model Verification HDL Coder / Model Verification

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

有关 Simulink® Coder™ 生成的代码如何处理模型验证模块的信息，请参阅 Configure Model for Debugging (Simulink Coder)。

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
| **PreserveUpstreamLogic** | 控制未连接逻辑的移除。默认值为 `off`，这意味着未连接逻辑不会保留在 HDL 代码中。有关更多详细信息，请参阅 PreserveUpstreamLogic (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

检查信号是否为零

Assertion 模块检查输入信号的任意元素是否为 `0`。如果所有元素均非零，则断言为 `true (1)`，模块不执行任何操作。否则，默认情况下模块会停止仿真并返回错误消息。
