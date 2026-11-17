---
type: simulink-block
title: 'Sigmoidal MF'
family: 'membership-functions'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: 'Membership Functions'
documentation_page: 'sigmoidalmf'
documentation_source_path: 'sigmoidalmf.html'
language: zh-CN
chinese_source: worker-translation
---

# Sigmoidal MF

## 端口

### 输入

### **x** — 输入值 标量 | 向量

用于计算隶属度值的输入值，指定为标量或向量。
### 输出

### **MF** — 隶属度值 标量 | 向量

隶属度值，以标量或向量形式返回。**MF** 的维度与 **x** 的维度匹配。**MF** 的每个元素是为 **x** 的对应元素计算得到的隶属度值。

## 参数

### **a** — 过渡区域形状参数 `1`（默认）| 标量

控制过渡区域形状的参数。**a** 的大小控制过渡区域的宽度。

当 **a** 的符号为正时，曲线从左到右递增。反之，当 **a** 的符号为负时，曲线从左到右递减。

#### 编程用法

|  |
| --- |
| **模块参数：** `a` |
| **类型：** string, character vector |
| **默认值：** `"1"` |

### **c** — 过渡区域中心 `0`（默认）| 标量

过渡区域中心。

#### 编程用法

|  |
| --- |
| **模块参数：** `c` |
| **类型：** string, character vector |
| **默认值：** `"0"` |

## 所属库

Fuzzy Logic Toolbox / Membership Functions

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

## 版本历史

**R2006a 之前引入**

## 描述

S 形隶属度函数

Sigmoidal MF 模块实现 S 形隶属度函数。

f(x;a,c)=11+e−a(x−c)

当 *a* 的符号为正时，曲线从左到右递增。反之，当 *a* 的符号为负时，曲线从左到右递减。参数 *c* 设置曲线的拐点。

此模块与 Diff. Sigmoidal MF 和 Prod. Sigmoidal MF 模块相关。
