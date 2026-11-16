---
type: simulink-block
title: 'Probabilistic Rule Agg'
family: 'fuzzy'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: 'Fuzzy Logic in Simulink'
documentation_page: 'probabilisticruleagg'
documentation_source_path: 'probabilisticruleagg.html'
language: zh-CN
chinese_source: worker-translation
---

# Probabilistic Rule Agg

## 端口

### 输入

### **In1** — 输入值行向量

输入值，指定为与 **In2** 具有相同元素数的行向量。

### **In2** — 输入值行向量

输入值，指定为与 **In1** 具有相同元素数的行向量。

### 输出

### **Out1** — 概率 OR 值行向量

概率 OR 值，返回为行向量 *y*，其元素数与 **In1** 和 **In2** 均相同。
*y* 的每个元素包含来自输入向量的对应元素的概率 OR。

令 `A` = **In1** 且 `B` = **In2**。然后，输入向量的第 *i* 个元素的概率 OR 是以下代数和。

```
y(i) = A(i) + B(i) - A(i)*B(i);
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

用于规则聚合的概率 OR 函数

Probabilistic Rule Agg 模块返回两个输入向量的逐元素概率 OR，即代数和。
