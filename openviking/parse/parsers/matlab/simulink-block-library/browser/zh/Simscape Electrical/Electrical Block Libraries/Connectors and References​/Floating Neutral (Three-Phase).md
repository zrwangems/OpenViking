---
type: simulink-block
title: 'Floating Neutral (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Connectors and References\u200b'
documentation_page: 'floatingneutralthreephase'
documentation_source_path: 'ref/floatingneutralthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Floating Neutral (Three-Phase)

## 端口

### 守恒

### **~** — 三相端口电气

可扩展复合（**a**、**b**、
**c**）三相端口。

## 参数

### **建模选项** — 是建模复合三相端口还是展开三相端口 `Composite three-phase ports`（默认） | `Expanded three-phase ports`

是建模复合三相端口还是展开三相端口。

复合三相端口使用单个模块端口表示三个单独的电气守恒端口。可以使用复合三相端口构建对应于三相电气系统单线图的模型。

展开三相端口使用三个单独的电气守恒端口表示三相系统的各相。

### **寄生接地电导** — 寄生接地电导 `1e-12` `1/Ohm`（默认）

对地的寄生电导。对于某些电路拓扑的仿真，需要非零值。

## 所属库

Simscape / Electrical / Connectors & References

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

## 描述

用于星形连接网络的内部浮动中性点

Floating Neutral (Three-Phase) 模块连接三相系统的各相，以形成浮动中性点。

**注意**

如果要创建可连接到其他模块的中性点，请使用 Neutral Port (Three-Phase) 模块。如果要创建连接到接地的中性点，请使用 Grounded Neutral (Three-Phase) 模块。
