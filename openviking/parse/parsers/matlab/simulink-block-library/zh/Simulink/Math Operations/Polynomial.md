---
type: simulink-block
title: 'Polynomial'
family: 'libsb2sl'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'ALG'
documentation_page: 'polynomial'
documentation_source_path: 'slref/polynomial.html'
language: zh-CN
chinese_source: worker-translation
---

# Polynomial

## 端口

### 输入

### **Port\_1** — 输入信号 实数标量或向量

用于计算多项式 *P(u)* 的值。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — 计算得到的多项式值 实数标量或向量

在输入信号处计算得到的多项式 *P(u)* 的值。

**数据类型：** `single` | `double`

## 参数

### **Polynomial coefficients** — 待计算多项式的系数 `[ +2.081618890e-019, -1.441693666e-014, +4.719686976e-010, -8.536869453e-006, +1.621573104e-001, -8.087801117e+001 ]`（默认）| 实数数组

以 MATLAB `polyval` 形式指定多项式系数。第一个系数对应 *xN*，其余系数对应 *x* 的降幂。最后一个系数表示多项式的常数项。

#### 编程用法

|  |
| --- |
| **模块参数：** `coefs` |
| **类型：** 实数数组 |
| **默认值：** `[ +2.081618890e-019, -1.441693666e-014, +4.719686976e-010, -8.536869453e-006, +1.621573104e-001, -8.087801117e+001 ]` |

## 所属库

Simulink / Math Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

对输入值执行多项式系数计算

Polynomial 模块在每个时间步对输入 *u* 计算 *`P(u)`*。您可以按照 MATLAB® `polyval` 命令接受的形式定义一组多项式系数。
