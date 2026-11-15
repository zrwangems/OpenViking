---
type: simulink-block
title: 'Z-shaped MF'
family: 'fuzzy'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: 'Fuzzy Logic in Simulink'
documentation_page: 'zshapedmf'
documentation_source_path: 'zshapedmf.html'
language: zh-CN
chinese_source: worker-translation
---

# Z-shaped MF

## 端口

### 输入

### **x** — 输入值 标量 | 向量

用于计算隶属度值的输入值，指定为标量或向量。
### 输出

### **Z MF** — 隶属度值 标量 | 向量

隶属度值，返回为标量或向量。**Z MF** 的维度与 **x** 的维度匹配。**Z MF** 的每个元素是针对 **x** 的对应元素计算得到的隶属度值。

## 参数

### **左端点 a** — 过渡区域的最左点 `-3`（默认）| 标量

过渡区域的最左点 *a*。

#### 编程使用

|  |
| --- |
| **模块参数：** `a` |
| **类型：** string, character vector |
| **默认值：** `"-3"` |

### **右端点 b** — 过渡区域的最右点 `3`（默认）| 标量

过渡区域的最右点 *b*。

#### 编程使用

|  |
| --- |
| **模块参数：** `b` |
| **类型：** string, character vector |
| **默认值：** `"3"` |

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

Z 形隶属函数

Z-shaped MF 模块实现 Z 形隶属函数。

f(x;a,b)={1,x≤a1−2(x−ab−a)2,a≤x≤a+b22(x−bb-a)2,a+b2≤x≤b0x≥b

从左到右，函数从 1 减小到 0。参数 *a* 和 *b* 控制曲线斜降部分的左右端点。

此模块与 S-shaped MF 和 Pi-shaped MF 模块相关。
