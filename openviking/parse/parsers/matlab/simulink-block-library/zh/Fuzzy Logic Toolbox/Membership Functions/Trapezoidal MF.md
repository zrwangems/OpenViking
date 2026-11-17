---
type: simulink-block
title: 'Trapezoidal MF'
family: 'fuzzy'
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

### **x** — 输入值 标量 | 向量

用于计算隶属度值的输入值，指定为标量或向量。

### 输出

### **MF** — 隶属度值 标量 | 向量

隶属度值，以标量或向量形式返回。**MF** 的维度与 **x** 的维度一致。**MF** 的每个元素是为 **x** 中对应元素计算得到的隶属度值。

## 参数

### **Left base point a** — 梯形左底点 `-8`（默认）| 标量

梯形的左底点 *a*。

#### 编程使用

|  |
| --- |
| **模块参数**：`a` |
| **类型**：string, character vector |
| **默认值**：`"-8"` |

### **Left top point b** — 梯形左肩点 `-4`（默认）| 标量

梯形的左肩点 *b*。

#### 编程使用

|  |
| --- |
| **模块参数**：`b` |
| **类型**：string, character vector |
| **默认值**：`"-4"` |

### **Right top point c** — 梯形右肩点 `2`（默认）| 标量

梯形的右肩点 *c*。

#### 编程使用

|  |
| --- |
| **模块参数**：`c` |
| **类型**：string, character vector |
| **默认值**：`"2"` |

### **Right base point d** — 梯形右底点 `9`（默认）| 标量

梯形的右底点 *d*。

#### 编程使用

|  |
| --- |
| **模块参数**：`d` |
| **类型**：string, character vector |
| **默认值**：`"9"` |

## 所属库

Fuzzy Logic Toolbox / Membership Functions

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

梯形隶属函数

Trapezoidal MF 模块实现梯形隶属函数。

f(x;a,b,c,d)=max(min(x−ab−a,1,d−xd−c),0)

参数 *a* 和 *d* 控制梯形的左、右*底点*或基点。参数 *b* 和 *c* 控制梯形的左、右*肩点*或顶点。

隶属函数的形状取决于 *b* 和 *c* 的相对值。

- 当 *c* 大于 *b* 时，得到的隶属函数为梯形。
- 当 *b* 等于 *c* 时，得到的隶属函数等价于参数为 [*a* *b* *d*] 的三角形隶属函数。
- 当 *c* 小于 *b* 时，得到的隶属函数为三角形，且最大值小于 1。

此模块与 Triangular MF、Linear S-shaped MF 和 Linear Z-shaped MF 模块相关。
