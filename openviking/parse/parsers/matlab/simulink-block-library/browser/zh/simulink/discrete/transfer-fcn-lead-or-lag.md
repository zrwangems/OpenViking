---
type: simulink-block
title: 'Transfer Fcn Lead or Lag'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Discrete'
documentation_page: 'transferfcnleadorlag'
documentation_source_path: 'slref/transferfcnleadorlag.html'
language: zh-CN
chinese_source: official
---

# Transfer Fcn Lead or Lag

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量

模块对其应用离散时间超前或滞后补偿的输入信号。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

作为输入符号的离散时间超前或滞后补偿的输出信号。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### **补偿器的极点(在 Z 平面内)** — 极点 `0.95` (默认) | 标量

指定补偿器的极点。

#### 编程用法

|  |
| --- |
| **模块参数**：`PoleZ` |
| **类型**：字符向量 |
| **值**：实数标量 |
| **默认值**：`'0.95'` |

### **补偿器的零点(在 Z 平面内)** — 补偿器的零点 `0.75` (默认) | 标量

指定补偿器在 Z 平面中的零点。

#### 编程用法

|  |
| --- |
| **模块参数**：`ZeroZ` |
| **类型**：字符向量 |
| **值**：实数标量 |
| **默认值**：`'0.75'` |

### **上一输入的初始条件** — 上一输入的初始条件 `0.0` (默认) | 标量

为上一个输出指定初始条件。

#### 编程用法

|  |
| --- |
| **模块参数**：`ICPrevInput` |
| **类型**：字符向量 |
| **值**：实数标量 |
| **默认值**：`'0.0'` |

### **上一输出的初始条件** — 上一输出的初始条件 `0.0` (默认) | 标量

为上一个输出指定初始条件。

#### 编程用法

|  |
| --- |
| **模块参数**：`ICPrevOutput` |
| **类型**：字符向量 |
| **值**：实数标量 |
| **默认值**：`'0.0'` |

### **整数舍入模式** — 定点运算的舍入模式 **向下** (默认) | **向上** | **收敛** | **最邻近值** | **舍入** | **最简** | **零**

指定定点运算的舍入模式。有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

模块参数始终舍入到最邻近的可表示值。要控制模块参数的舍入方法，请在封装字段中使用 MATLAB® 舍入函数输入表达式。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `RndMeth` |
| **值:** | `'Floor'` (默认) | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **发生溢出时饱和处理为最大值或最小值** — 溢出操作的方法 `off` (默认) | `on`

当您选中此复选框时，溢出将饱和处理为数据类型可表示的最大值或最小值。否则，溢出将绕回。

如果选中此复选框，饱和将应用于模块中的每个内部操作，而不仅仅应用于输出或结果。一般情况下，代码生成进程可以检测到何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 编程用法

|  |
| --- |
| **模块参数**：`DoSatur` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

## 所属库

Simulink / Discrete

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Booleana` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |
|  |  |
| --- | --- |
| a 建议不要将此模块用于布尔信号。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

实现离散时间超前或滞后补偿器

Transfer Fcn Lead or Lag 模块实现输入的离散时间超前或滞后补偿器。补偿器的即时增益为 1，DC 增益等于 `(1-z)/(1-p)`，其中 `z` 是零，`p` 是补偿器的极点。

该模块在 `0<z<p<1` 时实现一个超前补偿器，在 `0<p<z<1` 时实现一个滞后补偿器。
