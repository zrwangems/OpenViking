---
type: simulink-block
title: 'Triangular MF'
family: 'fuzzy'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: 'Membership Functions'
documentation_page: 'triangularmf'
documentation_source_path: 'triangularmf.html'
language: zh-CN
chinese_source: worker-translation
---

# Triangular MF

## 端口
```yaml
ports:
- name: x
  summary: 输入值 标量 | 向量
  direction: input
- name: MF
  summary: 隶属度值 标量 | 向量
  direction: output
```

### 输入

### **x** — 输入值 标量 | 向量

用于计算隶属度值的输入值，指定为标量或向量。

### 输出

### **MF** — 隶属度值 标量 | 向量

隶属度值，以标量或向量形式返回。**MF** 的维度与 **x** 的维度一致。**MF** 的每个元素是为 **x** 的对应元素计算得到的隶属度值。
## 参数
```yaml
parameters:
- name: Left base point a
  summary: 三角形的左脚 1（默认）| 标量
  group: ''
  block_parameter: a
  type: string, character vector
  default: '"1"'
- name: Peak location b
  summary: 三角形峰值 3（默认）| 标量
  group: ''
  block_parameter: b
  type: string, character vector
  default: '"3"'
- name: Right base point c
  summary: 三角形的右脚 6（默认）| 标量
  group: ''
  block_parameter: c
  type: string, character vector
  default: '"6"'
```

### **Left base point a** — 三角形的左脚 `1`（默认）| 标量

三角形的左脚 *a*。

#### 编程使用

|  |
| --- |
| **模块参数**：`a` |
| **类型**：string, character vector |
| **默认值**：`"1"` |

### **Peak location b** — 三角形峰值 `3`（默认）| 标量

三角形峰值 *b*。

#### 编程使用

|  |
| --- |
| **模块参数**：`b` |
| **类型**：string, character vector |
| **默认值**：`"3"` |

### **Right base point c** — 三角形的右脚 `6`（默认）| 标量

三角形的右脚 *c*。

#### 编程使用

|  |
| --- |
| **模块参数**：`c` |
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

**在 R2006a 之前引入**

## 描述

三角形隶属度函数

Triangular MF 模块实现三角形隶属度函数。

f(x;a,b,c)={0,x≤ax−ab−a,a≤x≤bc−xc−b,b≤x≤c0,c≤x}

更紧凑地，函数如下所示。

f(x;a,b,c)=max(min(x−ab−a,c−xc−b),0)

参数 *a* 和 *c* 设置三角形的左、右*脚*或基点。参数 *b* 设置三角形峰值的位置。

此模块与 Trapezoidal MF、Linear S-shaped MF 和 Linear Z-shaped MF 模块相关。
