---
type: simulink-block
title: 'Message Send'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'send'
documentation_source_path: 'ref/send.html'
language: zh-CN
chinese_source: worker-translation
---

# Message Send

## 端口
```yaml
ports:
- name: Port_Enable
  summary: 外部使能信号 标量
  direction: input
  data_types: double
- name: Port_1
  summary: 输入信号 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | enumerated | bus
    | fixed point
- name: Port_1
  summary: 输出消息 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | enumerated | bus
    | fixed point
```

### 输入

### **Port\_Enable** — 外部使能信号 标量

用于使能模块发送消息的输入端口。对于任何大于 `0` 的输入值，发送被使能。对于任何小于或等于 `0` 的值，发送被禁用。

#### 依赖

要使能此端口，请选中标记为 **Show enable port** 的框。

**数据类型：** `double`

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

此模块接受 Simulink® 支持的任何类型的输入，包括枚举类型，并将输入信号转换为消息。有关详细信息，请参阅 Data Types Supported by Simulink。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
### 输出

### **Port\_1** — 输出消息 标量 | 向量 | 矩阵

该模块输出具有常量优先级 `20` 的消息。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
## 参数
```yaml
parameters:
- name: Show enable port
  summary: 显示使能端口 off（默认）| on
  group: ''
  block_parameter: ShowEnablePort
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
```

### **Show enable port** — 显示使能端口 `off`（默认）| `on`

选中此复选框以显示使能端口。对于任何大于 `0` 的输入值，发送被使能。对于任何小于或等于 `0` 的值，发送被禁用。

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

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

**注意**

Send 模块不支持行优先代码生成。

## 版本历史

**在 R2016a 中引入**

## 描述

创建并发送消息

Send 模块读取输入信号的值，并发送携带该值的消息。在基于消息的通信中，消息是携带 Simulink 支持的任何类型数据的离散关注项。Send 和 Message Send 模块是相同的模块。
