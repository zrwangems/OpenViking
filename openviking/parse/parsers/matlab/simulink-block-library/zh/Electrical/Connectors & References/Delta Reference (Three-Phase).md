---
type: simulink-block
title: 'Delta Reference (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Connectors & References'
documentation_page: 'deltareferencethreephase'
documentation_source_path: 'ref/deltareferencethreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Delta Reference (Three-Phase)

## 端口

### 守恒

### **~** — 可扩展三相端口 electrical

可扩展复合（**a**,**b**, **c**）三相端口。

## 参数

### **建模选项** — 是对复合三相端口还是扩展三相端口进行建模 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

是对复合三相端口还是扩展三相端口进行建模。

复合三相端口使用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口构建与三相电气系统单线图对应的模型。

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

三角形连接网络的内部参考点

在 Simscape™ Electrical™ 模型中，将 Delta Reference (Three-Phase) 模块连接到三相系统中采用三角形绕组配置连接的任何部分。该模块为三角形绕组提供参考点，表示线间电压矢量三角形的中心。软件相对于该参考点处的电压计算绝对节点电压。

例如，假设您建模一个输电系统，该系统由以星形配置连接的发电机、星形-三角形变压器、三角形-星形变压器和以星形连接的负载组成。将 Delta Reference (Three-Phase) 模块连接到两个变压器之间的电路部分。
