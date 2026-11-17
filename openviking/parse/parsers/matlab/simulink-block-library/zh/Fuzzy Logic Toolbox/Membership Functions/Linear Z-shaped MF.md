---
type: simulink-block
title: 'Linear Z-shaped MF'
family: 'fuzzy'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: 'Membership Functions'
documentation_page: 'linearzshapedmf'
documentation_source_path: 'linearzshapedmf.html'
language: zh-CN
chinese_source: worker-translation
---

# Linear Z-shaped MF

## 端口

### 输入

### **x** — 输入值 标量 | 向量

用于计算隶属度值的输入值，指定为标量或向量。

### 输出

### **MF** — 隶属度值 标量 | 向量

隶属度值，以标量或向量形式返回。**MF** 的维度与 **x** 的维度一致。**MF** 的每个元素是对 **x** 中对应元素计算得到的隶属度值。

## 参数

### **Left point a** — 过渡区域最左点 `4`（默认）| 标量

过渡区域的最左点 *a*。

#### 编程使用

|  |
| --- |
| **模块参数**：`a` |
| **类型**：string, character vector |
| **默认值**：`"4"` |

### **Right point b** — 过渡区域最右点 `6`（默认）| 标量

过渡区域的最右点 *b*。

#### 编程使用

|  |
| --- |
| **模块参数**：`b` |
| **类型**：string, character vector |
| **默认值**：`"6"` |

## 所属库

Fuzzy Logic Toolbox / Membership Functions

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

## 版本历史

**在 R2022a 中引入**

## 描述

线性 Z 形饱和隶属函数

Linear Z-Shaped MF 模块实现线性 Z 形饱和隶属函数。

- 当 *a* < *b* 时：

  f(x;a,b)={1,x<ab−xb−a,a≤x≤b0,x>b}
- 当 *a* = *b* 时：

  f(x;a,b)={1,x<a0,x≥a}

参数 *a* 和 *b* 分别控制隶属函数的肩部和足部。将 *a* 设为等于 *b* 会生成一个清晰隶属函数。

此模块与 Triangular MF、Trapezoidal MF 和 Linear S-shaped MF 模块相关。
