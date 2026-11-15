---
type: simulink-block
title: 'Phase Permute'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Connectors and References\u200b'
documentation_page: 'phasepermute'
documentation_source_path: 'ref/phasepermute.html'
language: zh-CN
chinese_source: worker-translation
---

# Phase Permute

## 端口

### 守恒

### **~123** — 可扩展三相端口（电气）

可扩展复合（**a1**、**b1**、
**c1**）三相
端口。

### **~231** — 可扩展三相端口（电气）

可扩展复合（**a2**、**b2**、
**c2**）三相
端口。

## 参数

### **建模选项** — 是否对复合三相端口或扩展三相端口建模 `Composite three-phase ports`（默认） | `Expanded three-phase ports`

是否对复合三相端口或扩展三相端口建模。

复合三相端口用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口构建对应于三相电力系统单线图的模型。

扩展三相端口使用三个独立的电气守恒端口表示三相系统的各相。

## 所属库

Simscape / Electrical / Connectors & References

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

## 描述

置换三相系统的相

Phase Permute 模块对三相系统的各相进行循环置换（改变顺序）。

该模块有两个与其端子关联的三相连接。如果将模块中标记为 **~123**（展开视图中为 **a1**、**b1**、**c1**）的一侧视为第 1 侧，并将标记为 **~231**（**a2**、**b2**、**c2**）的一侧视为第 2 侧，则该模块按下表所示连接各相。

| 第 1 侧的相 | 连接到第 2 侧的相 |
| --- | --- |
| *a1* | *c2* |
| *b1* | *a2* |
| *c1* | *b2* |
