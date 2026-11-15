---
type: simulink-block
title: 'Algebraic Constraint'
family: math-operations
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'algebraicconstraint'
---

# Algebraic Constraint

Constrain input signal

## 中文

限制输入信号

### 所属库

Simulink / Math Operations

### 描述

Algebraic Constraint 模块将输入信号 f(*z*) 限制为 *z* 或 0，并输出代数状态 *z*。模块输出一个值，使得输入处函数的结果为 0 或 *z*。输出必须通过直接反馈路径影响输入。换句话说，反馈路径只包含具有直接馈通的模块。例如，您可以为指数为 1 的微分代数方程组 (DAE) 指定代数方程。

### 端口

#### 输入

#### **f(z)** — 输入信号 实数标量或向量

信号受制于约束 *f(z) = 0* 或 *f(z) = z* 来求解代数环。

**数据类型:** `double`
#### 输出

#### **z** — 输出状态 实数标量或向量

当输入信号 **f(z)** 受制于约束 *f(z) = 0* 或 *f(z) = z* 时代数环的解。

**数据类型:** `double`

### 参数

#### **约束** — 输入信号的约束 **f(z) = 0** (默认) | **f(z) = z**

要对其求解的约束的类型。您可以对 **f(z) = 0** 或 **f(z) = z** 求解。

##### 编程用法

|  |
| --- |
| **模块参数**：`Constraint` |
| **类型：**字符向量 |
| **值：**`'f(z) = 0' | 'f(z) = z'` |
| **默认值：**`'f(z) = 0'` |

#### **求解器** — 代数环求解器 **自动** (默认) | **信赖域** | **线搜索**

在信赖域 [1]、[2] 或线搜索 [3] 算法之间选择来求解代数环。默认情况下，此值设置为**自动**，即根据模型配置选择代数环求解器，并在仿真期间在信赖域和线搜索算法之间切换求解器

##### 编程用法

|  |
| --- |
| **模块参数**：`Solver` |
| **类型：**字符向量 |
| **值：**`'auto' | 'Trust region' | 'Line search'` |
| **默认值：**`'auto'` |

#### **容差** — 求解器容差 **自动** (默认) | 正标量

当您在**求解器**下拉菜单中显式指定要使用的求解器（信赖域或线搜索）时，此选项是可见的。指定较小的值可获得较高的精度，指定较大的值可实现较快的执行速度。默认设置为**自动**。

##### 编程用法

|  |
| --- |
| **模块参数**：`Tolerance` |
| **类型：**字符向量 |
| **值：**`'auto'` | 正标量 |
| **默认值：**`'auto'` |

#### **初始估计值** — 解值的初步估计值 0 (默认) | 标量

接近于预期解值的代数状态 *z* 的初始估计值，用于提高代数环求解器的效率。默认情况下，此值设置为 0。

##### 编程用法

|  |
| --- |
| **模块参数**：`InitialGuess` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'0'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

不建议用于生产代码。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Math Operations

## Description

The Algebraic Constraint block constrains the input signal f(*z*)
to *z* or 0 and outputs an algebraic state *z*.
The block outputs a value that produces 0 or *z* at the input. The
output must affect the input through a direct feedback path. In other words, the
feedback path only contains blocks with direct feedthrough. For example, you can specify
algebraic equations for index 1 differential-algebraic systems (DAEs).

## Ports

### Input

### **f(z)** — Input signal real scalar or vector

Signal is subjected to the constraint *f(z) = 0* or
*f(z) = z* to solve the algebraic loop.

**Data Types:** `double`
### Output

### **z** — Output state real scalar or vector

Solution to the algebraic loop when the input signal
**f(z)** is subjected to the constraint
*f(z) = 0* or *f(z) =
z*.

**Data Types:** `double`

## Parameters

### **Constraint** — Constraint on input signal `f(z) = 0` (default) | `f(z) = z`

Type of constraint for which to solve. You can solve for `f(z)
= 0` or `f(z) = z`

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Constraint` |
| **Type:** character vector |
| **Values:** `'f(z) = 0' | 'f(z) = z'` |
| **Default:** `'f(z) = 0'` |

### **Solver** — Algebraic Loop Solver `auto` (default) | `Trust region` | `Line search`

Choose between the Trust region [1], [2] or Line search [3] algorithms to
solve the algebraic loop. By default this value is set to
`auto`, which selects the algebraic loop solver based on the
model configuration and switches the solver between the Trust region and Line search algorithm during simulation

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Solver` |
| **Type:** character vector |
| **Values:** `'auto' | 'Trust region' | 'Line search'` |
| **Default:** `'auto'` |

### **Tolerance** — Solver Tolerance `auto` (default) | positive scalar

This option is visible when you explicitly specify a solver to be used
(Trust region or Line Search) in the **Solver** drop-down
menu. Specify a smaller value for higher accuracy or a larger value for
faster execution. By default it is set to
`auto`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Tolerance` |
| **Type:** character vector |
| **Values:** `'auto'` | positive scalar |
| **Default:** `'auto'` |

### **Initial Guess** — Initial guess of solution value 0 (default) | scalar

Initial guess for the algebraic state *z* that is close
to the expected solution value to improve the efficiency of the algebraic
loop solver. By default, this value is set to 0

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialGuess` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'0'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production code.

## Version History

**Introduced before R2006a**
