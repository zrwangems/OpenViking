---
type: simulink-block
title: 'Polynomial Evaluation'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Polynomial Functions'
documentation_page: 'polynomialevaluation'
documentation_source_path: 'ref/polynomialevaluation.html'
language: zh-CN
chinese_source: worker-translation
---

# Polynomial Evaluation

## 端口

### 输入

### **In** — 输入数据向量 | 矩阵

将模块对其应用多项式函数的输入数据指定为向量或矩阵。

**数据类型：** `single` | `double`
**复数支持：** Yes

### **Coeffs** — 多项式系数向量

按降幂顺序指定系数向量。有关模块如何针对各种系数向量进行运算的详细信息，请参阅**常量系数**。

#### 依赖项

要启用此端口，请清除**使用常量系数**参数。

**数据类型：** `single` | `double`
**复数支持：** Yes
### 输出

### **Out** — 多项式求值的输出向量 | 矩阵

该模块对输入数据应用多项式函数，并输出与输入数据大小和复数属性相同的向量或矩阵。

**数据类型：** `single` | `double`
**复数支持：** Yes

## 参数

### **使用常量系数** — 使用常量系数 `off` (默认) | `on`

选择**使用常量系数**参数时，您在**常量系数**参数中指定多项式表达式。未选择**使用常量系数**参数时，您通过 **Coeffs** 端口指定可变多项式表达式。在这两种情况下，多项式都指定为按降幂顺序排列的实数或复数系数向量。

### **常量系数** — 常量系数 `[5 4 3 2 1]` (默认) | 向量

按降幂顺序指定要应用于输入的多项式系数向量。

下表显示该模块如何针对不同的系数向量进行运算。

| 系数向量 | 等效多项式表达式 |
| --- | --- |
| `[1 2 3 4 5]` | y=u4+2u3+3u2+4u+5 |
| `[1 0 3 0 5]` | y=u4+3u2+5 |
| `[1 2+i 3 4-3i 5i]` | y=u4+(2+i)u3+3u2+(4−3i)u+5i |

#### 依赖项

要启用此参数，请选中**使用常量系数**复选框。

**复数支持：** Yes

## 所属库

DSP System Toolbox / Math Functions / Polynomial Functions

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `No` |
| **可变大小信号** | `No` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2006a 之前引入**

## 描述

计算多项式表达式

Polynomial Evaluation 模块对 **In** 端口处的实数或复数输入应用多项式函数。

等效的 MATLAB® 代码如下所示。

    y = polyval(u)

Polynomial Evaluation 模块执行此操作的效率高于使用 Sum (Simulink) 和 Math Function (Simulink) 模块的等效构造。
