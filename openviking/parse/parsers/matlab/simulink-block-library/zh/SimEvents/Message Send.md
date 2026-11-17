---
type: simulink-block
title: 'Message Send'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: 'SimEvents'
documentation_page: 'send'
documentation_source_path: 'ref/send.html'
language: zh-CN
chinese_source: worker-translation
---

# Message Send

## 端口

### 输入

### **Port\_Enable** — 外部使能信号标量

Input port to enable the block to send a message. For any input value
that is greater than `0` send is enabled. For any value
less than or equal to `0`, the send is disabled.

#### 依赖关系

To enable this port, select the box labeled **显示使能端口**.

**数据类型：** `double`

### **Port\_1** — 输入信号标量 | 向量 | 矩阵

This block accepts inputs of any type that Simulink® supports, including enumerated types and converts the
input signal to a message. For more information, see Simulink 支持的数据类型.

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
### 输出

### **Port\_1** — 输出消息标量 | 向量 | 矩阵

The block outputs a message with constant priority
`20`.

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

## 参数

### **显示使能端口** — 显示使能端口 `off` (默认) | `on`

Select this check box to display enable port. For any input value that is
greater than `0` send is enabled. For any value less than
or equal to `0`, the send is disabled.

#### 编程使用

|  |
| --- |
| **模块参数**：`ShowEnablePort` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

## 所属库

Simulink / Messages & Events SimEvents

## 模块特性

|  |
| --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` | `string` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

**注意**

Send 模块不支持行优先代码生成。

## 版本历史

**在 R2016a 中引入**

## 描述

创建并发送消息

Send 模块读取输入信号的值，并发送携带该值的消息。在基于消息的通信中，消息是所关注的离散项，承载 Simulink 支持的任何类型的数据。Send 和 Message Send 模块是完全相同的模块。
