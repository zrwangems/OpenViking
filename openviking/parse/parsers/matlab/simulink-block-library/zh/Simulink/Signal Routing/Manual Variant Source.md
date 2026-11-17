---
type: simulink-block
title: 'Manual Variant Source'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'manualvariantsource'
documentation_source_path: 'slref/manualvariantsource.html'
language: zh-CN
chinese_source: worker-translation
---

# Manual Variant Source

## 端口
```yaml
ports:
- name: Port_1
  summary: 第一个变体输入信号 标量 | 向量
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus
- name: Port_n
  summary: 第 *n* 个变体输入信号 标量 | 向量
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus
- name: Port_1
  summary: 输出信号 标量 | 向量
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus
```

### 输入

### **Port\_1** — 第一个变体输入信号 标量 | 向量

第一个变体输入信号。当您将拨动开关连接到此端口时，该模块将此输入信号传递到输出端口。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **Port\_n** — 第 *n* 个变体输入信号 标量 | 向量

第 *n* 个变体输入信号。当您将拨动开关连接到此端口时，该模块将此输入信号传递到输出端口。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

从活动变体输入信号传递的输出信号。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
## 参数
```yaml
parameters:
- name: Number of choices
  summary: 输入选项的数量 2（默认）| 标量
  group: ''
  block_parameter: NumChoices
  type: character vector
  values: integer
  default: '''2'''
```

要访问模块参数，请右键单击该模块并选择 **Mask** > **Mask Parameters**。

### **Number of choices** — 输入选项的数量 2（默认）| 标量

指定变体输入端的数量。

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

在多个变体选项之间切换输入

Manual Variant Source 模块是一个拨动开关，它激活输入端的一个变体选项以传递到输出。

一个 Manual Variant Source 模块可以有两个或多个输入端口，并有一个输出端口。每个输入端口与一个变体控制相关联。要更改输入端口的数量，请右键单击该模块并选择 **Mask Parameters**，然后在 **Number of choices** 框中键入一个值。

要在输入端的变体选项之间切换，请双击该模块。该模块显示活动选项，并用一条线连接输入到输出。该模块将输入端的活动变体选项直接传播到输出，并在仿真期间丢弃连接到非活动输入端口的模块。

**注意**

- 双击 Manual Variant Source 模块不会打开模块对话框，而是切换输出选项。
- 不支持在编译、仿真或暂停状态下更改活动选项。
