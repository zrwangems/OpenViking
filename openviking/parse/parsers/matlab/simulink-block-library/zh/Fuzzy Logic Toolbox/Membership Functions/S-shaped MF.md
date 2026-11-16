---
type: simulink-block
title: 'S-shaped MF'
family: 'fuzzy'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: 'Membership Functions'
documentation_page: 'sshapedmf'
documentation_source_path: 'sshapedmf.html'
language: zh-CN
chinese_source: worker-translation
---

# S-shaped MF

## 端口

### 输入

### **x** — 输入值 标量 | 向量

用于计算隶属度值的输入值，指定为标量或向量。

### 输出

### **S MF** — 隶属度值 标量 | 向量

隶属度值，以标量或向量形式返回。**S MF** 的维度与 **x** 的维度匹配。**S MF** 的每个元素是针对 **x** 的对应元素计算得到的隶属度值。

## 参数

### **左点 a** — 过渡区最左点 `-3` （默认） | 标量

过渡区的最左点 *a*。

#### 编程用法

|  |
| --- |
| **模块参数：** `a` |
| **类型：** string, character vector |
| **默认值：** `"-3"` |

### **右点 b** — 过渡区最右点 `3` （默认） | 标量

过渡区的最右点 *b*。

#### 编程用法

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

S 形隶属函数

S-shaped MF 模块实现 S 形隶属函数。

f(x;a,b)={0,x≤a2(x−ab−a)2,a≤x≤a+b21-2(x−bb-a)2,a+b2≤x≤b1,x≥b}

从左到右，函数从 0 增加到 1。参数 *a* 和 *b* 控制曲线倾斜部分的左右两端。

此模块与 Z-shaped MF 和 Pi-shaped MF 模块相关。
