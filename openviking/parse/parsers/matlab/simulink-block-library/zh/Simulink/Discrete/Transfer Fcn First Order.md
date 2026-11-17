---
type: simulink-block
title: 'Transfer Fcn First Order'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'transferfcnfirstorder'
documentation_source_path: 'slref/transferfcnfirstorder.html'
language: zh-CN
chinese_source: worker-translation
---

# Transfer Fcn First Order

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 标量 | 向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_1
  summary: 传递函数输出信号 标量 | 向量
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
```

### 输入

### **Port\_1** — 输入信号 标量 | 向量

一阶传递函数算法的输入信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 传递函数输出信号 标量 | 向量

输出信号，为输入的离散时间一阶传递函数，具有单位直流增益。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
## 参数
```yaml
parameters:
- name: Pole (in Z plane)
  summary: 极点 0.95（默认）| 标量
  group: ''
  block_parameter: PoleZ
  type: 字符向量
  values: 实标量
  default: '''0.95'''
- name: Initial condition for previous output
  summary: 前一输出的初始条件 0.0（默认）| 标量
  group: ''
  block_parameter: ICPrevOutput
  type: 字符向量
  values: 实标量
  default: '''0.0'''
- name: Integer rounding mode
  summary: 定点运算的舍入模式 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: ''
  block_parameter: RndMeth
  values: '''Floor''（默认）| ''Ceiling'' | ''Convergent'' | ''Nearest'' | ''Round'' | ''Simplest'' | ''Zero'''
- name: Saturate to max or min when overflows occur
  summary: 溢出操作的方法 off（默认）| on
  group: ''
  block_parameter: DoSatur
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''off'''
```

### **Pole (in Z plane)** — 极点 `0.95`（默认）| 标量

指定极点。

#### 编程使用

|  |
| --- |
| **模块参数**：`PoleZ` |
| **类型**：字符向量 |
| **Value**：实标量 |
| **默认值**：`'0.95'` |

### **Initial condition for previous output** — 前一输出的初始条件 `0.0`（默认）| 标量

指定前一输出的初始条件。

#### 编程使用

|  |
| --- |
| **模块参数**：`ICPrevOutput` |
| **类型**：字符向量 |
| **Value**：实标量 |
| **默认值**：`'0.0'` |

### **Integer rounding mode** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅舍入模式（Fixed-Point Designer）。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB® 舍入函数的表达式。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter：** | `RndMeth` |
| **值**：| `'Floor'`（默认）| `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **Saturate to max or min when overflows occur** — 溢出操作的方法 `off`（默认）| `on`

选中此复选框时，溢出饱和到数据类型可表示的最大值或最小值。否则，溢出将回绕。

选中此复选框时，饱和应用于模块上的每个内部运算，而不仅仅是输出或结果。通常，代码生成过程可以检测到不可能发生溢出的情况。在这种情况下，代码生成器不会生成饱和代码。

#### 编程使用

|  |
| --- |
| **模块参数**：`DoSatur` |
| **类型**：字符向量 |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |
## 所属库

Simulink / Discrete

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

实现离散时间一阶传递函数

Transfer Fcn First Order 模块实现输入的离散时间一阶传递函数。该传递函数具有单位直流增益。
