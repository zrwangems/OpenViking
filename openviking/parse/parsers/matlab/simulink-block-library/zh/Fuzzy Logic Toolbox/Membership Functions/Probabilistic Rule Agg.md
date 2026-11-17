---
type: simulink-block
title: 'Probabilistic Rule Agg'
family: 'fuzzy'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: 'Membership Functions'
documentation_page: 'probabilisticruleagg'
documentation_source_path: 'probabilisticruleagg.html'
language: zh-CN
chinese_source: worker-translation
---

# Probabilistic Rule Agg

## 端口
```yaml
ports:
- name: In1
  summary: 输入值行向量
  direction: input
- name: In2
  summary: 输入值行向量
  direction: input
- name: Out1
  summary: 概率 OR 值行向量
  direction: output
```

### 输入

### **In1** — 输入值行向量

输入值，指定为与 **In2** 具有相同元素数量的行向量。

### **In2** — 输入值行向量

输入值，指定为与 **In1** 具有相同元素数量的行向量。
### 输出

### **Out1** — 概率 OR 值行向量

概率 OR 值，返回为与 **In1** 和 **In2** 均具有相同元素数量的行向量 *y*。
*y* 的每个元素包含输入向量中对应元素的概率 OR。

令 `A` = **In1**，`B` = **In2**。则输入向量第 *i* 个元素的概率 OR 为以下代数和。

```
y(i) = A(i) + B(i) - A(i)*B(i);
```
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
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

用于规则聚合的概率 OR 函数

Probabilistic Rule Agg 模块返回两个输入向量的逐元素概率 OR，即代数和。
