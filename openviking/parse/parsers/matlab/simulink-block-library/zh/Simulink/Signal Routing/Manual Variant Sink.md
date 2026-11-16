---
type: simulink-block
title: 'Manual Variant Sink'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'manualvariantsink'
documentation_source_path: 'slref/manualvariantsink.html'
language: zh-CN
chinese_source: official
---

# Manual Variant Sink

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量

传递到活动输出端口的输入信号。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **Port\_1** — 第一个变体输出 标量 | 向量

第一个变体输出信号。当您将拨动开关连接到此输出端口时，该模块将输入信号传递到此端口。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **Port\_n** — 第 *n* 个变体输出 标量 | 向量

第 *n* 个变体输出信号。当您将拨动开关连接到此输出端口时，该模块将输入信号传递到此端口。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

要访问模块参数，请右键点击该模块并选择**封装** > **封装参数**。

### **选择项的数量** — 输出选择项的数量 2 (默认) | 标量

指定变体输出端口的数量。

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

在输出端的多个变体选择项之间切换

Manual Variant Sink 模块是拨动开关，可激活输出端的变体选择项之一以传递输入。

该模块可以有两个或多个输出端口，并且有一个输入端口。每个输出端口都与一个变体控制项相关联。要更改输出端口的数量，请右键点击该模块并选择**封装参数**，然后在**选择项的数量**框中键入值。

要在输出端的变体选择项之间切换，请双击该模块。该模块通过一条将输入连接到输出的线显示活动选择项。在仿真期间，该模块传播输出端的活动变体选择项，并丢弃连接到非活动输出端口的模块。

**注意**

- 双击 Manual Variant Sink 模块不会打开模块对话框，而是切换输出选择项。
- 不支持在编译、仿真或暂停状态期间更改活动选择项。
