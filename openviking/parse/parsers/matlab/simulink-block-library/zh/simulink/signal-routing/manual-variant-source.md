---
type: simulink-block
title: 'Manual Variant Source'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Signal Routing'
documentation_page: 'manualvariantsource'
documentation_source_path: 'slref/manualvariantsource.html'
language: zh-CN
chinese_source: official
---

# Manual Variant Source

## 端口

### 输入

### **Port\_1** — 第一个变体输入信号 标量 | 向量

第一个变体输入信号。当您将拨动开关连接到输出端口时，该模块将此输入信号传递到此端口。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **Port\_n** — 第 *n* 个变体输入信号 标量 | 向量

第 *n* 个变体输入信号。当您将拨动开关连接到输出端口时，该模块将此输入信号传递到此端口。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

从活动变体输入信号传递的输出信号。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

要访问模块参数，请右键点击该模块并选择**封装** > **封装参数**。

### **选择项的数量** — 输入选择项的数目 2 (默认) | 标量

指定变体输入端口的数量。

#### 编程用法

|  |
| --- |
| **模块参数**：`NumChoices` |
| **类型：**字符向量 |
| **值：**`integer` |
| **默认值：**`'2'` |

## 所属库

Simulink / Signal Routing

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2016b 中推出**

## 描述

在输入端的多个变体选择项之间切换

Manual Variant Source 模块是一个拨动开关，用于激活输入端的变体选择项之一并将其直接传递给输出端。

Manual Variant Source 模块可以有两个或多个输入端口和一个输出端口。每个输入端口都与一个变体控制项相关联。要更改输入端口的数量，请右键点击该模块并选择**封装参数**，然后在**选择项的数量**框中键入值。

要在输入端的变体选择项之间切换，请双击该模块。该模块通过一条将输入连接到输出的线显示活动选择项。该模块将输入端的活动变体选择项直接传播到输出端，并在仿真期间丢弃连接到非活动输入端口的模块。

**注意**

- 双击 Manual Variant Source 模块不会打开模块对话框，而是切换输出选择项。
- 不支持在编译、仿真或暂停状态期间更改活动选择项。
