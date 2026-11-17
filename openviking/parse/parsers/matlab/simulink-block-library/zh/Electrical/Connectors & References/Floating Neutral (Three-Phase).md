---
type: simulink-block
title: 'Floating Neutral (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Connectors & References'
documentation_page: 'floatingneutralthreephase'
documentation_source_path: 'ref/floatingneutralthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Floating Neutral (Three-Phase)

## 端口

### 守恒端口

### **~** — 三相端口电气

可扩展复合（**a**、**b**、
**c**）三相
端口。

## 参数

### **Modeling option** — 对复合或扩展三相端口建模 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

对复合或扩展三相端口建模。

复合三相端口用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口构建对应于三相电气系统单线图的模型。

扩展三相端口使用三个独立的电气守恒端口表示三相系统的各相。

### **Parasitic ground conductance** — 寄生对地电导 `1e-12` `1/Ohm`（默认）

寄生对地电导。某些电路拓扑的仿真需要非零值。

## 所属库

Simscape / Electrical / Connectors & References

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

## 描述

用于 wye 连接网络的内部浮动中性点

Floating Neutral (Three-Phase) 模块连接三相系统的各相，以形成浮动中性点。

**注意**

如果要创建可连接到其他模块的中性点，请使用 Neutral Port (Three-Phase) 模块。如果要创建连接到地的中性点，请使用 Grounded Neutral (Three-Phase) 模块。
