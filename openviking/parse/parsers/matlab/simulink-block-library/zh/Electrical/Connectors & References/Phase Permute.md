---
type: simulink-block
title: 'Phase Permute'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Connectors & References'
documentation_page: 'phasepermute'
documentation_source_path: 'ref/phasepermute.html'
language: zh-CN
chinese_source: worker-translation
---

# Phase Permute

## 端口

### 守恒

### **~123** — 可扩展三相端口 electrical

可扩展复合（**a1**、**b1**、
**c1**）三相端口。

### **~231** — 可扩展三相端口 electrical

可扩展复合（**a2**、**b2**、
**c2**）三相端口。

## 参数

### **Modeling option** — 对复合三相端口还是扩展三相端口进行建模 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

对复合三相端口还是扩展三相端口进行建模。

复合三相端口用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口构建对应于三相电气系统单线图的模型。

扩展三相端口使用三个独立的电气守恒端口表示三相系统的各相。

## 所属库

Simscape / Electrical / Connectors & References

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

## 描述

置换三相系统的相位

Phase Permute 模块对三相系统的相位进行循环置换（改变顺序）。

该模块有两个与其端子关联的三相连接。如果将模块上标记为 **~123**
（展开视图中为 **a1**、**b1**、**c1**）的一侧视为侧 1，将模块上标记为 **~231**
（**a2**、**b2**、**c2**）的一侧视为侧 2，则该模块按表中所示连接各相。

| 侧 1 相位 | 连接到侧 2 相位 |
| --- | --- |
| *a1* | *c2* |
| *b1* | *a2* |
| *c1* | *b2* |
