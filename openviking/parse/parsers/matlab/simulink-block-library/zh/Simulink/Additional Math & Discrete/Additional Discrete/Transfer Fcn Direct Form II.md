---
type: simulink-block
title: 'Transfer Fcn Direct Form II'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Additional Math & Discrete / Additional Discrete'
documentation_page: 'transferfcndirectformii'
documentation_source_path: 'slref/transferfcndirectformii.html'
language: zh-CN
chinese_source: worker-translation
---

# Transfer Fcn Direct Form II

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量

输入信号，指定为标量或向量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

输出信号，指定为标量或向量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### **Numerator coefficients** — 分子系数 `[0.2 0.3 0.2]`（默认）| 向量

将分子系数指定为向量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `NumCoefVec` |
| **类型：** 字符向量 |
| **值：** 向量 |
| **默认：** `'[0.2 0.3 0.2]'` |

### **Denominator coefficients excluding lead** — 分母系数 `[-0.9 0.6]`（默认）| 向量

指定分母系数，不包括首项系数，首项系数必须为 `1.0`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DenCoefVec` |
| **类型：** 字符向量 |
| **值：** 向量 |
| **默认：** `'[-0.9 0.6]'` |

### **Initial condition** — 初始条件 `0.0`（默认）| 标量

将初始条件指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `vinit` |
| **类型：** 字符向量 |
| **值：** 标量 |
| **默认：** `'0.0'` |

### **Integer rounding mode** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。
有关详细信息，请参阅舍入模式（Fixed-Point Designer）。

#### 程序化使用

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** 字符向量 |
| **值：** `'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **默认：** `'Floor'` |

### **Saturate to max or min when overflows occur** — 溢出操作方法 `off`（默认）| `on`

选中此复选框时，溢出饱和到数据类型所能表示的最大值或最小值。
否则，溢出将回绕。

选中此复选框时，饱和适用于模块上的每个内部运算，而不仅仅是输出或结果。通常，代码生成过程可以检测到不可能发生溢出的情况。在这种情况下，代码生成器不会生成饱和代码。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DoSatur` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认：** `'off'` |

## 所属库

Simulink / Additional Math & Discrete / Additional Discrete

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

代码生成器不会在生成的代码中显式地将构成非原子掩码子系统的原始模块分组。这种灵活性允许更高效的代码生成。在某些情况下，您可以通过选择 **Treat as atomic unit** 选项将掩码子系统模块配置为作为原子单元执行，从而实现分组。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

实现传递函数的 Direct Form II 实现

Transfer Fcn Direct Form II 模块实现由 **Numerator coefficients** 和 **Denominator coefficients excluding lead** 参数指定的传递函数的 Direct Form II 实现。该模块仅支持单输入单输出（SISO）传递函数。

该模块自动选择输出、系数以及任何临时变量的数据类型和定标。
