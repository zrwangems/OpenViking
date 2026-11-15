---
type: simulink-block
title: 'Level-2 MATLAB S-Function'
family: user-defined-functions
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'level2matlabsfunction'
language: zh-CN
chinese_source: official
---

# Level-2 MATLAB S-Function

## 端口

### 输入

### **In** — 一个 2 级 MATLAB S-Function 模块的信号输入 标量 | 向量 | 矩阵

Level-2 MATLAB S-Function 模块接受模块特性表中所列类型的输入。有关详细信息，请参阅 Simulink 支持的数据类型。您可以使用 `setup` 回调函数来配置输入端口。使用 `setup` 函数指定输入端口的数量、输入信号的维度、每个端口的采样时间以及端口是否为直接馈通。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Out** — 2 级 MATLAB S-Function 模块的信号输出 标量 | 向量 | 矩阵

S-Function 返回的 Level-2 MATLAB S-Function 模块的信号输出。您可以使用 `setup` 回调函数来配置输入端口。使用 `setup` 函数指定输入端口的数量、输入信号的维度和每个端口的采样时间。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **S-Function 名称** — 指定 S-Function 的名称 `matlabfile` (默认) | S-Function 名称

指定定义此模块行为的 MATLAB 函数的名称。MATLAB 函数必须遵循编写 2 级 MATLAB S-Function 的标准（请参阅编写 2 级 MATLAB S-Function 了解详情）。

#### 编程用法

|  |
| --- |
| **模块参数**：`FunctionName` |
| **类型：**字符向量 |
| **值：**`'matlabfile'` | S-Function 名称 |
| **默认值：**`'matlabfile'` |

### **参数** — 指定此模块的参数值 无默认值 (默认)

指定此模块的参数值。

#### 编程用法

|  |
| --- |
| **模块参数**：`Parameters` |
| **类型：**字符向量 |
| **值：**模块参数的值 |
| **默认值：**`' '` |

## 所属库

Simulink / User-Defined Functions

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Booleana` | `doublea` | `fixed pointa` | `integera` | `singlea` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |
|  |  |
| --- | --- |
| a 一级 MATLAB S-Function 仅支持双精度数据类型。二级 MATLAB S-Function 支持 Simulink 支持的所有数据类型。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

- 如果对应的 TLC 文件可用，则 Level-2 MATLAB S-Function 模块使用 TLC 文件生成代码，否则代码生成会抛出错误。
- 实时代码生成不支持调用 MATLAB 的 S-Function。
- 实际数据类型或功能支持取决于模块实现。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

1 级 MATLAB S-Function 仅支持 `double` 数据类型。Level-2 MATLAB S-functions 支持 Simulink 支持的所有数据类型。

## 版本历史

**在 R2010b 中推出**

## 描述

在模型中使用 2 级 MATLAB S-Function

此模块允许您在模型中使用 2 级 MATLAB® S-Function（请参阅编写 2 级 MATLAB S-Function）。为此，请在模型中创建此模块的实例。然后，在模块参数对话框的 **S-Function 名称**字段中输入 2 级 MATLAB S-Function 的名称。

**注意**

使用 S-Function 模块在模块中包含 1 级 MATLAB S-Function。

如果 2 级 MATLAB S-Function 定义了其他参数，您可以在模块参数对话框的**参数**字段中输入它们。将参数输入为 MATLAB 表达式，以按照 MATLAB S-Function 定义的顺序计算它们的值。使用逗号分隔每个表达式。

如果模型中包含 Level-2 MATLAB S-Function 模块，而 S-Function 中发生错误，则 Level-2 MATLAB S-Function 模块将在对话框中显示该错误的 MATLAB 堆栈跟踪信息。点击**确定**关闭此对话框。
