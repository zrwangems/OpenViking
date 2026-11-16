---
type: simulink-block
title: 'Linear S-shaped MF'
family: 'fuzzy'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: 'Membership Functions'
documentation_page: 'linearsshapedmf'
documentation_source_path: 'linearsshapedmf.html'
language: zh-CN
chinese_source: worker-translation
---

# Linear S-shaped MF

## 端口

### 输入

### **x** — 输入值 scalar | vector

用于计算隶属度值的输入值，指定为 scalar 或 vector。
### 输出

### **MF** — 隶属度值 scalar | vector

隶属度值，以 scalar 或 vector 形式返回。**MF** 的维度与 **x** 的维度匹配。**MF** 的每个元素都是为 **x** 的对应元素计算出的隶属度值。

## 参数

### **左点 a** — 过渡区域的最左点 `4`（默认）| scalar

过渡区域的最左点 *a*。

#### 编程使用

|  |
| --- |
| **模块参数：** `a` |
| **类型：** string, character vector |
| **默认：** `"4"` |

### **右点 b** — 过渡区域的最右点 `6`（默认）| scalar

过渡区域的最右点 *b*。

#### 编程使用

|  |
| --- |
| **模块参数：** `b` |
| **类型：** string, character vector |
| **默认：** `"6"` |

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

线性 S 形饱和隶属度函数

Linear S-Shaped MF 模块实现线性 S 形饱和隶属度函数。

- 当 *a* < *b* 时：

  f(x;a,b)={0,x<ax−ab−a,a≤x≤b1,x>b}
- 当 *a* = *b* 时：

  f(x;a,b)={0,x<a1,x≥a}

参数 *a* 和 *b* 分别控制隶属度函数的底部和肩部。将 *a* 设置为等于 *b* 会生成清晰隶属度函数。

此模块与 Triangular MF、Trapezoidal MF 和 Linear Z-shaped MF 模块相关。
