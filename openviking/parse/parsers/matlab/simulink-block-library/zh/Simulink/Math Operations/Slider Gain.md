---
type: simulink-block
title: 'Slider Gain'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'slidergain'
documentation_source_path: 'slref/slidergain.html'
language: zh-CN
chinese_source: worker-translation
---

# Slider Gain

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_1
  summary: 输入乘以增益 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
```

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

Slider Gain 模块接受实数或复数值的标量、向量或矩阵输入。该模块支持定点数据类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 输入乘以增益 标量 | 向量 | 矩阵

Slider Gain 模块输出输入乘以常量增益值的结果。当模块的输入为实数且增益为复数时，输出为复数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
## 参数
```yaml
parameters:
- name: Slider gain
  summary: 增益值 0（默认）| 实数值
  group: ''
  block_parameter: gain
  type: 字符向量
  values: 实数标量
  default: '''1'''
- name: Low
  summary: 滑块范围的下限 0（默认）| 实数值
  group: ''
  block_parameter: low
  type: 字符向量
  values: 实数标量
  default: '''0'''
- name: High
  summary: 滑块范围的上限 2（默认）| 实数值
  group: ''
  block_parameter: high
  type: 字符向量
  values: 实数标量
  default: '''2'''
```

### **Slider gain** — 增益值 `0`（默认）| 实数值

选择应用于输入的增益值。

#### 编程使用

|  |
| --- |
| **模块参数**：`gain` |
| **类型**：字符向量 |
| **值**：实数标量 |
| **默认值**：`'1'` |

### **Low** — 滑块范围的下限 `0`（默认）| 实数值

指定滑块范围的下限。

#### 编程使用

|  |
| --- |
| **模块参数**：`low` |
| **类型**：字符向量 |
| **值**：实数标量 |
| **默认值**：`'0'` |

### **High** — 滑块范围的上限 `2`（默认）| 实数值

指定滑块范围的上限。

#### 编程使用

|  |
| --- |
| **模块参数**：`high` |
| **类型**：字符向量 |
| **值**：实数标量 |
| **默认值**：`'2'` |
## 所属库

Simulink / Math Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用滑块改变标量增益

Slider Gain 模块执行标量增益，您可以在仿真过程中修改该增益。使用滑块参数修改增益。
