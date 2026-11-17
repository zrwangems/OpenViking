---
type: simulink-block
title: 'Transfer Fcn Lead or Lag'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'transferfcnleadorlag'
documentation_source_path: 'slref/transferfcnleadorlag.html'
language: zh-CN
chinese_source: worker-translation
---

# Transfer Fcn Lead or Lag

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量

该模块对其应用离散时间超前或滞后补偿的输入信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

对输入信号进行离散时间超前或滞后补偿后的输出信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### **Pole of compensator (in Z plane)** — 补偿器极点 `0.95`（默认）| 标量

指定补偿器的极点。

#### 编程使用

|  |
| --- |
| **模块参数**：`PoleZ` |
| **类型**：字符向量 |
| **Value**：实标量 |
| **默认值**：`'0.95'` |

### **Zero of compensator (in Z plane)** — 补偿器零点 `0.75`（默认）| 标量

指定补偿器在 Z 平面中的零点。

#### 编程使用

|  |
| --- |
| **模块参数**：`ZeroZ` |
| **类型**：字符向量 |
| **Value**：实标量 |
| **默认值**：`'0.75'` |

### **Initial condition for previous input** — 前一输入的初始条件 `0.0`（默认）| 标量

指定前一输入的初始条件。

#### 编程使用

|  |
| --- |
| **模块参数**：`ICPrevInput` |
| **类型**：字符向量 |
| **Value**：实标量 |
| **默认值**：`'0.0'` |

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

指定定点运算的舍入模式。有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入方式，请在掩码字段中输入使用 MATLAB® 舍入函数的表达式。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter：** | `RndMeth` |
| **值**：| `'Floor'`（默认）| `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **Saturate to max or min when overflows occur** — 溢出操作方式 `off`（默认）| `on`

选中此复选框时，溢出将饱和到数据类型所能表示的最大值或最小值。否则，溢出将回绕。

选中此复选框时，饱和将应用于模块上的每个内部运算，而不仅仅是输出或结果。通常，代码生成过程可以检测到何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

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
| **Data Types** | `Booleana` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a 不建议将此模块用于布尔信号。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

实现离散时间超前或滞后补偿器

Transfer Fcn Lead or Lag 模块对输入实现离散时间超前或滞后补偿器。补偿器的瞬时增益为 1，直流增益等于 `(1-z)/(1-p)`，其中 `z` 是补偿器的零点，`p` 是补偿器的极点。

当 `0<z<p<1` 时，该模块实现超前补偿器；当 `0<p<z<1` 时，实现滞后补偿器。
