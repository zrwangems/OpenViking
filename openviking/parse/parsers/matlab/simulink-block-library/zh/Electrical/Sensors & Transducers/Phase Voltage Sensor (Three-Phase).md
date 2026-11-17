---
type: simulink-block
title: 'Phase Voltage Sensor (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sensors & Transducers'
documentation_page: 'phasevoltagesensorthreephase'
documentation_source_path: 'ref/phasevoltagesensorthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Phase Voltage Sensor (Three-Phase)

## 端口

### 输出

### **V** — 三元素矢量物理信号

与相电压相关联的三元素物理信号矢量输出端口

### 守恒

### **~1** — 三相端口电气

可扩展三相端口。

### **~2** — 三相端口电气

可扩展三相端口。

## 参数

### **Modeling option** — 是对复合三相端口还是扩展三相端口进行建模 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

是对复合三相端口还是扩展三相端口进行建模。

复合三相端口用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口来构建与三相电气系统单线图相对应的模型。

扩展三相端口使用三个独立的电气守恒端口来表示三相系统的各个相。

## 所属库

Simscape / Electrical / Sensors & Transducers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

## 描述

理想三相相电压测量

Phase Voltage Sensor (Three-Phase) 模块表示一个理想三相电压传感器。它测量三相端口 **~1** 和 **~2** 两端的电压，并输出一个三元素物理信号矢量。物理信号输出矢量的每个元素等于相应相的电压。

**注意**

您必须将 Phase Voltage Sensor (Three-Phase) 模块并联或并行连接到三相元件。有关如何使用此模块的详细信息，请参阅 Build and Simulate Composite and Expanded Three-Phase Models。
