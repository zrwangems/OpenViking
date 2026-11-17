---
type: simulink-block
title: 'IC'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Signal Attributes'
documentation_page: 'ic'
documentation_source_path: 'slref/ic.html'
language: zh-CN
chinese_source: worker-translation
---

# IC

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 标量 | 向量 | 矩阵 | N 维数组
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated | bus
- name: Port_1
  summary: 输出信号 标量 | 向量 | 矩阵 | N 维数组
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated | bus
```

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵 | N 维数组

输入信号，指定为标量、向量、矩阵或 N 维数组。该模块将此信号的初始条件设置为您指定的**初始值**。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵 | N 维数组

输出信号，由您指定的**初始值**提供，随后是输入信号的实际值。有关详细信息，请参阅非零采样时间偏移时的行为。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
## 参数
```yaml
parameters:
- name: 初始值
  summary: 初始值 1 （默认） | 实数、有限标量、向量、矩阵或 N 维数组
  group: ''
  block_parameter: Value
  type: 字符向量
  values: 标量 | 向量 | 矩阵 | N 维数组
  default: '''1'''
- name: 采样时间（-1 表示继承）
  summary: 采样之间的间隔 -1 （默认） | 标量 | 向量
  group: ''
  block_parameter: SampleTime
  values: '"-1" （默认） | 带引号的标量或向量'
```

### **初始值** — 初始值 `1` （默认） | 实数、有限标量、向量、矩阵或 N 维数组

将输入信号的初始值指定为有限的实值标量、向量、矩阵或 N 维数组。该值必须是标量，或者与输入信号具有相同的维度。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Value` |
| **类型：** 字符向量 |
| **值：** 标量 | 向量 | 矩阵 | N 维数组 |
| **默认值：** `'1'` |

### **采样时间（-1 表示继承）** — 采样之间的间隔 `-1` （默认） | 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅指定采样时间。

#### 依赖关系

仅当您将此参数设置为 `-1` 以外的值时，此参数才可见。要了解更多信息，请参阅不建议使用采样时间的模块。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `"-1"` （默认） | 带引号的标量或向量 |
## 所属库

Simulink / Signal Attributes

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

不建议用于生产代码。涉及嵌入式系统中常见的资源限制以及速度和内存限制。生成的代码可能包含动态内存分配和释放、递归、额外的内存开销以及变化较大的执行时间。虽然代码在功能上是有效的，并且在资源丰富的环境中通常可以接受，但较小的嵌入式目标通常无法支持此类代码。通常，模块会朝着适合生产代码的方向发展。因此，适合生产代码的模块仍然适合。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

### R2023b：IC 模块行优先支持更新

IC 模块现在支持行优先数组布局的代码生成。

## 描述

设置信号的初始值

IC 模块在其输入端口设置信号的初始条件，例如仿真开始时间（`tstart`）时的信号值。为此，该模块在您开始仿真时输出指定的初始条件，无论输入信号的实际值如何。此后，该模块输出输入信号的实际值。

IC 模块可用于为循环中的代数状态变量提供初始猜测。有关详细信息，请参阅代数环概念。

### 非零采样时间偏移时的行为

如果 IC 模块具有非零采样时间偏移（`toffset`），则 IC 模块在时间 `t` 输出其初始值，

```
t = n * tperiod + toffset
```

其中 `n` 是使 `t ≥ tstart` 成立的最小整数。

也就是说，IC 模块在采样时间为 `[tperiod, toffset]` 的模块首次执行时输出其初始值，这可能在 `tstart` 之后。
