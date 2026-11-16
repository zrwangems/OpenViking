---
type: simulink-block
title: 'Current Sensor (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sensors & Transducers'
documentation_page: 'currentsensorthreephase'
documentation_source_path: 'ref/currentsensorthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Current Sensor (Three-Phase)

## 端口

### 输出

### **I** — 三元素向量物理信号

三元素物理信号向量输出端口，与相电流关联。
### 守恒

### **~1** — 三相电气端口

可扩展三相电气守恒端口。

### **~2** — 三相电气端口

可扩展三相电气守恒端口。

## 参数

### **Modeling option** — 是否对复合三相端口或扩展三相端口建模 `Composite three-phase ports`（默认） | `Expanded three-phase ports`

是否对复合三相端口或扩展三相端口建模。

复合三相端口用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口构建对应于三相电力系统单线图的模型。

扩展三相端口使用三个单独的电气守恒端口表示三相系统的各相。

## 所属库

Simscape / Electrical / Sensors & Transducers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

## 描述

理想三相电流测量

Current Sensor (Three-Phase) 模块表示理想三相电流传感器。该模块测量从端口 **~1** 流向端口 **~2** 的三个电流中的每一个，并输出单个三元素物理信号向量。物理信号输出向量的每个元素与其相应相中的电流成比例。

**注意**

必须将 Current Sensor (Three-Phase) 模块与三相元件串联。有关如何使用此模块的更多信息，请参阅 Build and Simulate Composite and Expanded Three-Phase Models。
