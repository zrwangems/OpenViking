---
type: simulink-block
title: 'Transfer Fcn Direct Form II Time Varying'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Additional Math & Discrete / Additional Discrete'
documentation_page: 'transferfcndirectformiitimevarying'
documentation_source_path: 'slref/transferfcndirectformiitimevarying.html'
language: zh-CN
chinese_source: worker-translation
---

# Transfer Fcn Direct Form II Time Varying

## 端口

### 输入

### **u** — 输入信号 标量 | 向量

输入信号，指定为标量或向量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Num** — 分子系数 标量 | 向量

传递函数的分子系数，指定为标量或向量。

#### 依赖关系

分子系数和分母系数的数据类型可以不同，但分子向量的长度与完整分母向量的长度必须相同。如果需要，用零填充分子向量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Den No Lead** — 分母系数 标量 | 向量

传递函数的分母系数，指定为标量或向量，不包含前导系数 1。完整分母的前导系数为 1，但它不包括在输入信号中。

**示例：** 对于分母系数 `[1 -1.7
0.72]`，指定值为 `[-1.7
0.72]` 的信号。

#### 依赖关系

分子系数和分母系数的数据类型可以不同，但分子向量的长度与完整分母向量的长度必须相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **y** — 输出信号 标量 | 向量

输出信号，指定为标量或向量。

该模块自动选择输出和任何临时变量的数据类型和定标。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **初始条件** — 初始条件 `0.0`（默认） | 标量

将初始条件指定为标量。

#### 编程用法

|  |
| --- |
| **模块参数：** `vinit` |
| **类型：** character vector |
| **取值：** 标量 |
| **默认值：** `'0.0'` |

### **整数舍入模式** — 定点运算的舍入模式 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

#### 编程用法

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** character vector |
| **取值：** `'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **默认值：** `'Floor'` |

### **发生溢出时饱和到最大值或最小值** — 溢出操作的方法 `off`（默认） | `on`

选中此复选框时，溢出会饱和到该数据类型可表示的最大值或最小值。否则，溢出会回绕。

选中此复选框时，饱和会应用于模块上的每个内部运算，而不仅仅是输出或结果。通常，代码生成过程可以检测到不可能发生溢出的情况。在这种情况下，代码生成器不会生成饱和代码。

#### 编程用法

|  |
| --- |
| **模块参数：** `DoSatur` |
| **类型：** character vector |
| **取值：** `'off' | 'on'` |
| **默认值：** `'off'` |

## 所属库

Simulink / Additional Math & Discrete / Additional Discrete

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Booleana` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 不建议将此模块与 Boolean 信号一起使用。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

代码生成器不会在生成的代码中显式地对构成非原子掩码子系统模块的基本模块进行分组。这种灵活性允许更高效的代码生成。在某些情况下，您可以通过选择 **视为原子单元** 选项，将掩码子系统模块配置为作为原子单元执行，从而实现分组。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

实现传递函数的时变 Direct Form II 实现

Transfer Fcn Direct Form II Time Varying 模块实现指定传递函数的 Direct Form II 实现。该模块仅支持单输入单输出 (SISO) 传递函数。

标记为 **Den No Lead** 的输入信号包含传递函数的分母系数。完整分母的前导系数为 1，但它不包括在输入信号中。例如，要使用分母 `[1 -1.7 0.72]`，请指定值为 `[-1.7
0.72]` 的信号。标记为 **Num** 的输入信号包含分子系数。分子系数和分母系数的数据类型可以不同，但分子向量的长度与完整分母向量的长度必须相同。如果需要，用零填充分子向量。

该模块自动选择输出、系数以及任何临时变量的数据类型和定标。
