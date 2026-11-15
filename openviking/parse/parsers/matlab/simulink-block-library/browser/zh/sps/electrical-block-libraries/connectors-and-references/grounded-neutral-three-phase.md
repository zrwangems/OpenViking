---
type: simulink-block
title: 'Grounded Neutral (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Connectors and References\u200b'
documentation_page: 'groundedneutralthreephase'
documentation_source_path: 'ref/groundedneutralthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Grounded Neutral (Three-Phase)

## 端口

### 守恒

### **~** — 三相电气端口

可扩展复合（**a**、**b**、
**c**）三相
端口。

## 参数

### **建模选项** — 选择对复合三相端口还是扩展三相端口建模 `Composite three-phase ports`（默认） | `Expanded three-phase ports`

选择对复合三相端口还是扩展三相端口建模。

复合三相端口使用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口构建对应于三相电气系统单线图的模型。

扩展三相端口使用三个独立的电气守恒端口表示三相系统的各相。

## 所属库

Simscape / Electrical / Connectors & References

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

## 描述

将三相系统的各相连接到电气参考

Grounded Neutral (Three-Phase) 模块将三相系统的各相连接到地。

**注意**

如果要将三相系统的中性点连接到其他模块，请改用 Neutral Port (Three-Phase) 模块。如果要创建浮动中性点，请使用 Floating Neutral (Three-Phase) 模块。
