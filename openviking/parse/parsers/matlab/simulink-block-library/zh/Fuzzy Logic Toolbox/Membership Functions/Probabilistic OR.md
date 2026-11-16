---
type: simulink-block
title: 'Probabilistic OR'
family: 'fuzzy'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: 'Membership Functions'
documentation_page: 'probabilisticor'
documentation_source_path: 'probabilisticor.html'
language: zh-CN
chinese_source: worker-translation
---

# Probabilistic OR

## 端口

### 输入

### **In1** — 输入值数组 | 行向量

输入值，指定为数组或行向量 *x*。
### 输出

### **Out1** — Probabilistic OR 值行向量

Probabilistic OR 值，返回为行向量 *y*，其列数与输入 *x* 相同。*y* 的每个元素包含 *x* 中对应列的概率 OR 值。

如果 *x* 有一行，则 *y* = *x*。

如果 *x* = `[A;B]`，其中 `A` 和 `B` 是行向量，则 *y* 的第 *i* 个元素是以下代数和。

```
y(i) = A(i) + B(i) - A(i)*B(i);
```

如果 *x* 多于两行，则首先对前两行计算概率 OR。然后，在结果与下一行之间计算概率 OR。此过程对每个后续行重复。

```
x = [A;B;C;D]
y(i) = A(i) + B(i) - A(i)*B(i);
y(i) = y(i) + C(i) - y(i)*C(i);
y(i) = y(i) + D(i) - y(i)*D(i);
```

## 参数

未在 R2025b 中记录。

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

Probabilistic OR 函数

Probabilistic OR 模块返回输入信号的概率 OR 值，即代数和。
