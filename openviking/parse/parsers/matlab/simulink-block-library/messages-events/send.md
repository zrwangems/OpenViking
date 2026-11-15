---
type: simulink-block
title: 'Send'
family: messages-events
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Messages & Events'
documentation_page: 'send'
---

# Send

Create and send message

## 中文

创建并发送消息

### 所属库

Simulink / Messages & Events SimEvents

### 描述

Send 模块读取输入信号的值，并发送携带此值的消息。在基于消息的通信中，消息是感兴趣的离散项，携带 Simulink 支持的任何类型的数据。Send 和 Message Send 模块是相同的模块。

### 端口

#### 输入

#### **Port\_Enable** — 外部使能信号 标量

使模块能够发送消息的输入端口。对于任何大于 `0` 的输入值，发送都被启用。对于任何小于或等于 `0` 的值，发送都被禁用。

##### 依赖关系

要启用此端口，请选中标签为**显示使能端口**的框。

**数据类型:** `double`

#### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

此模块接受 Simulink® 支持的任何类型的输入，包括枚举类型，并将输入信号转换为消息。有关详细信息，请参阅 Simulink 支持的数据类型。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
#### 输出

#### **Port\_1** — 输出消息 标量 | 向量 | 矩阵

模块输出具有常量优先级 `20` 的消息。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### 参数

#### **显示使能端口** — 显示使能端口 `off` (默认) | `on`

选中此复选框以显示使能端口。对于任何大于 `0` 的输入值，发送都被启用。对于任何小于或等于 `0` 的值，发送都被禁用。

##### 编程用法

|  |
| --- |
| **模块参数**：`ShowEnablePort` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` | `string` |
| **直接馈通** | `否` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

**注意**

Send 模块不支持行优先代码生成。

### 版本历史记录

**在 R2016a 中推出**

## Libraries

Simulink / Messages & Events SimEvents

## Description

The Send block reads the value of an input signal, and sends a message
that carries this value. In message-based communication, a message is a discrete-item of
interest that carry data of any type that Simulink supports. Send and
Message Send blocks are identical blocks.

## Ports

### Input

### **Port\_Enable** — External enable signal scalar

Input port to enable the block to send a message. For any input value
that is greater than `0` send is enabled. For any value
less than or equal to `0`, the send is disabled.

#### Dependencies

To enable this port, select the box labeled **Show enable
port**.

**Data Types:** `double`

### **Port\_1** — Input signal scalar | vector | matrix

This block accepts inputs of any type that Simulink® supports, including enumerated types and converts the
input signal to a message. For more information, see Data Types Supported by Simulink.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
### Output

### **Port\_1** — Output message scalar | vector | matrix

The block outputs a message with constant priority
`20`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

## Parameters

### **Show enable port** — Display the enable port `off` (default) | `on`

Select this check box to display enable port. For any input value that is
greater than `0` send is enabled. For any value less than
or equal to `0`, the send is disabled.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ShowEnablePort` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

**Note**

Send blocks do not support row-major code generation.

## Version History

**Introduced in R2016a**
