---
type: simulink-block
title: 'Trapezoidal MF'
family: 'membership-functions'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: 'Membership Functions'
documentation_page: 'trapezoidalmf'
documentation_source_path: 'trapezoidalmf.html'
language: zh-CN
chinese_source: worker-translation
---

# Trapezoidal MF

## 端口

### 输入

### **x** — 输入值 scalar | vector

要计算隶属度值的输入值，指定为 scalar 或 vector。
### 输出

### **MF** — 隶属度值 scalar | vector

隶属度值，以 scalar 或 vector 形式返回。**MF** 的维度与 **x** 的维度匹配。**MF** 的每个元素是为 **x** 的对应元素计算的隶属度值。

## 参数

### **左基点 a** — 梯形的左底脚 `-8`（默认）| scalar

梯形的左底脚 *a*。

#### 编程用法

|  |
| --- |
| **模块参数：** `a` |
| **类型：** string, character vector |
| **默认值：** `"-8"` |

### **左顶点 b** — 梯形的左肩 `-4`（默认）| scalar

梯形的左肩 *b*。

#### 编程用法

|  |
| --- |
| **模块参数：** `b` |
| **类型：** string, character vector |
| **默认值：** `"-4"` |

### **右顶点 c** — 梯形的右肩 `2`（默认）| scalar

梯形的右肩 *c*。

#### 编程用法

|  |
| --- |
| **模块参数：** `c` |
| **类型：** string, character vector |
| **默认值：** `"2"` |

### **右基点 d** — 梯形的右底脚 `9`（默认）| scalar

梯形的右底脚 *d*。

#### 编程用法

|  |
| --- |
| **模块参数：** `d` |
| **类型：** string, character vector |
| **默认值：** `"9"` |

## 所属库

Fuzzy Logic Toolbox / Membership Functions

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

梯形隶属函数

Trapezoidal MF 模块实现梯形形状的隶属函数。

f(x;a,b,c,d)=max(min(x−ab−a,1,d−xd−c),0)

参数 *a* 和 *d* 控制梯形的左、右*底脚*或基点。参数 *b* 和 *c* 控制梯形的左、右*肩部*或顶点。

隶属函数的形状取决于 *b* 和 *c* 的相对值。

- 当 *c* 大于 *b* 时，生成的隶属函数为梯形。
- 当 *b* 等于 *c* 时，生成的隶属函数等效于参数为 [*a* *b* *d*] 的三角形隶属函数。
- 当 *c* 小于 *b* 时，生成的隶属函数为三角形，且最大值小于 1。

此模块与 Triangular MF、Linear S-shaped MF 和 Linear Z-shaped MF 模块相关。
