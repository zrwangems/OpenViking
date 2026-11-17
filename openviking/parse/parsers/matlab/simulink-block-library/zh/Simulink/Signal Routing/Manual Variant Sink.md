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
chinese_source: worker-translation
---

# Manual Variant Sink

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 标量 | 向量
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus
- name: Port_1
  summary: 第一个变体输出 标量 | 向量
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus
- name: Port_n
  summary: 第 *n* 个变体输出 标量 | 向量
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus
```

### 输入

### **Port\_1** — 输入信号 标量 | 向量

传递到活动输出端口的输入信号。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **Port\_1** — 第一个变体输出 标量 | 向量

第一个变体输出信号。当您将切换开关连接到此端口时，该模块将输入信号传递到此输出端口。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **Port\_n** — 第 *n* 个变体输出 标量 | 向量

第 *n* 个变体输出信号。当您将切换开关连接到此端口时，该模块将输入信号传递到此输出端口。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
## 参数
```yaml
parameters:
- name: Number of choices
  summary: 输出选择的数量 2（默认）| 标量
  group: ''
  block_parameter: NumChoices
  type: character vector
  values: integer
  default: '''2'''
```

要访问模块参数，请右键单击该模块并选择 **Mask** > **Mask Parameters**。

### **Number of choices** — 输出选择的数量 2（默认）| 标量

指定变体输出端口的数量。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumChoices` |
| **类型**：character vector |
| **Value:** `integer` |
| **默认值**：`'2'` |
## 所属库

Simulink / Signal Routing

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2016b 中引入**

## 描述

在输出端的多个变体选择之间切换

Manual Variant Sink 模块是一个切换开关，用于激活其输出端的某个变体选择以传递输入。

该模块可以有两个或多个输出端口，并具有一个输入端口。每个输出端口都与一个变体控制相关联。要更改输出端口的数量，请右键单击该模块并选择 **Mask Parameters**，然后在 **Number of choices** 框中键入一个值。

要在输出端的变体选择之间切换，请双击该模块。该模块会显示活动选择，并用一条线将输入连接到输出。该模块在输出端传播活动变体选择，并在仿真期间丢弃连接到非活动输出端口的模块。

**注意**

- 双击 Manual Variant Sink 模块不会打开模块对话框，而是切换输出选择。
- 不支持在编译、仿真或暂停状态下更改活动选择。
