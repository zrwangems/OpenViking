---
type: simulink-block
title: 'Algebraic Constraint'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'algebraicconstraint'
documentation_source_path: 'slref/algebraicconstraint.html'
language: zh-CN
chinese_source: worker-translation
---

# Algebraic Constraint

## 端口

### 输入

### **f(z)** — 输入信号 实数标量或向量

对输入信号施加约束 *f(z) = 0* 或 *f(z) = z* 以求解代数环。

**数据类型：** `double`
### 输出

### **z** — 输出状态 实数标量或向量

当输入信号 **f(z)** 受到约束 *f(z) = 0* 或 *f(z) = z* 时，代数环的解。

**数据类型：** `double`

## 参数

### **Constraint** — 对输入信号的约束 `f(z) = 0`（默认）| `f(z) = z`

要求解的约束类型。您可以求解 `f(z) = 0` 或 `f(z) = z`

#### 编程使用

|  |
| --- |
| **模块参数：** `Constraint` |
| **类型：** 字符向量 |
| **值：** `'f(z) = 0' | 'f(z) = z'` |
| **默认：** `'f(z) = 0'` |

### **Solver** — 代数环求解器 `auto`（默认）| `Trust region` | `Line search`

在 Trust region [1]、[2] 或 Line search [3] 算法之间选择以求解代数环。默认情况下，此值设置为 `auto`，它会根据模型配置选择代数环求解器，并在仿真期间在 Trust region 和 Line search 算法之间切换求解器

#### 编程使用

|  |
| --- |
| **模块参数：** `Solver` |
| **类型：** 字符向量 |
| **值：** `'auto' | 'Trust region' | 'Line search'` |
| **默认：** `'auto'` |

### **Tolerance** — 求解器容差 `auto`（默认）| 正标量

当您在 **Solver** 下拉菜单中明确指定要使用的求解器（Trust region 或 Line Search）时，此选项可见。指定较小的值以获得更高的精度，或指定较大的值以加快执行速度。默认情况下，它设置为 `auto`。

#### 编程使用

|  |
| --- |
| **模块参数：** `Tolerance` |
| **类型：** 字符向量 |
| **值：** `'auto'` | 正标量 |
| **默认：** `'auto'` |

### **Initial Guess** — 解的初始猜测值 0（默认）| 标量

代数状态 *z* 的初始猜测值，该值接近预期的解值，以提高代数环求解器的效率。默认情况下，此值设置为 0

#### 编程使用

|  |
| --- |
| **模块参数：** `InitialGuess` |
| **类型：** 字符向量 |
| **值：** 标量 |
| **默认：** `'0'` |

## 所属库

Simulink / Math Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

不推荐用于生产代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

约束输入信号

Algebraic Constraint 模块将输入信号 f(*z*) 约束为 *z* 或 0，并输出代数状态 *z*。该模块输出一个在输入端产生 0 或 *z* 的值。输出必须通过直接反馈路径影响输入。换句话说，反馈路径仅包含具有直接馈通的模块。例如，您可以为索引 1 微分代数系统（DAE）指定代数方程。
