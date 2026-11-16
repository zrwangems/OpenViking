---
type: simulink-block
title: 'Polynomial'
family: math-operations
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'polynomial'
language: zh-CN
chinese_source: official
---

# Polynomial

对输入值执行多项式系数计算

## 所属库

Simulink / Math Operations

## 描述

Polynomial 模块将计算输入 *u* 在每个时间步的 *`P(u)`*。您可以采用 MATLAB® `polyval` 命令接受的形式定义一组多项式系数。

## 端口

### 输入

### **Port\_1** — 输入信号 实数标量或向量

用于计算多项式 *P(u)* 的值。

**数据类型:** `single` | `double`
### 输出

### **Port\_1** — 计算多项式所得到的值 实数标量或向量

基于输入信号计算多项式 *P(u)* 所得的值。

**数据类型:** `single` | `double`

## 参数

### **多项式系数** — 要计算的多项式的系数 `[ +2.081618890e-019, -1.441693666e-014, +4.719686976e-010, -8.536869453e-006, +1.621573104e-001, -8.087801117e+001 ]` (默认) | 实数数组

以 MATLAB `polyval` 形式指定多项式系数。第一个系数对应于 *xN*，其余系数对应于 *x* 的降序。最后一个系数表示多项式的常量。

#### 编程用法

|  |
| --- |
| **模块参数：**`coefs` |
| **类型：**实数数组 |
| **默认值：**`[ +2.081618890e-019, -1.441693666e-014, +4.719686976e-010, -8.536869453e-006, +1.621573104e-001, -8.087801117e+001 ]` |

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

## 版本历史记录

**在 R2006a 之前推出**
