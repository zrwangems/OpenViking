---
type: simulink-block
title: 'Manual Variant Sink'
family: signal-routing
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'manualvariantsink'
---

# Manual Variant Sink

Switch between multiple variant choices at output

## 中文

在输出端的多个变体选择项之间切换

### 所属库

Simulink / Signal Routing

### 描述

Manual Variant Sink 模块是拨动开关，可激活输出端的变体选择项之一以传递输入。

该模块可以有两个或多个输出端口，并且有一个输入端口。每个输出端口都与一个变体控制项相关联。要更改输出端口的数量，请右键点击该模块并选择**封装参数**，然后在**选择项的数量**框中键入值。

要在输出端的变体选择项之间切换，请双击该模块。该模块通过一条将输入连接到输出的线显示活动选择项。在仿真期间，该模块传播输出端的活动变体选择项，并丢弃连接到非活动输出端口的模块。

**注意**

- 双击 Manual Variant Sink 模块不会打开模块对话框，而是切换输出选择项。
- 不支持在编译、仿真或暂停状态期间更改活动选择项。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量

传递到活动输出端口的输入信号。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
#### 输出

#### **Port\_1** — 第一个变体输出 标量 | 向量

第一个变体输出信号。当您将拨动开关连接到此输出端口时，该模块将输入信号传递到此端口。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

#### **Port\_n** — 第 *n* 个变体输出 标量 | 向量

第 *n* 个变体输出信号。当您将拨动开关连接到此输出端口时，该模块将输入信号传递到此端口。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### 参数

要访问模块参数，请右键点击该模块并选择**封装** > **封装参数**。

#### **选择项的数量** — 输出选择项的数量 2 (默认) | 标量

指定变体输出端口的数量。

##### 编程用法

|  |
| --- |
| **模块参数**：`NumChoices` |
| **类型：**字符向量 |
| **值：**`integer` |
| **默认值：**`'2'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2016b 中推出**

## Libraries

Simulink / Signal Routing

## Description

The Manual Variant Sink block is a toggle switch that activates one of its
variant choices at the output to pass the input.

The block can have two or more output ports and has one input port. Each output port is
associated with a variant control. To change the number of output ports, right-click the
block and select **Mask Parameters**, then type a value in the
**Number of choices** box.

To toggle between the variant choices at output, double-click the block. The block displays
the active choice with a line connecting the input to the output. The block propagates
the active variant choice at output and discards the blocks connected to inactive output
ports during simulation.

**Note**

- Double-clicking the Manual Variant Sink block does not open
  the block dialog box instead it toggles the output choice.
- Changing the active choice during compile, simulation, or paused states is
  not supported.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector

Input signal passed to the active output port.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### Output

### **Port\_1** — First variant output scalar | vector

First variant output signal. The block passes the input signal to this
output port when you connect the toggle switch to this port.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **Port\_n** — *n*th variant output scalar | vector

*n*th variant output signal. The block passes the
input signal to this output port when you connect the toggle switch to
this port.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

To access the block parameter, right-click the block and select **Mask** > **Mask Parameters**.

### **Number of choices** — Number of output choices 2 (default) | scalar

Specify the number of variant output ports.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumChoices` |
| **Type:** character vector |
| **Value:** `integer` |
| **Default:** `'2'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2016b**
