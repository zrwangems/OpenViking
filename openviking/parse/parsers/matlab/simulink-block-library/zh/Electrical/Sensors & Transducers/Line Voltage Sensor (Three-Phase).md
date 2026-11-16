---
type: simulink-block
title: 'Line Voltage Sensor (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sensors & Transducers'
documentation_page: 'linevoltagesensorthreephase'
documentation_source_path: 'ref/linevoltagesensorthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Line Voltage Sensor (Three-Phase)

## 端口

### 输出

### **V** — 三元素向量物理信号

与相间电压关联的三元素物理信号向量输出端口
### 守恒

### **~1** — 三相电气端口

可扩展三相端口。

## 参数

### **建模选项** — 是否对复合或扩展三相端口进行建模 `Composite three-phase ports` (默认) | `Expanded three-phase ports`

是否对复合或扩展三相端口进行建模。

Composite three-phase ports 用单个模块端口表示三个独立的电气守恒端口。您可以使用 composite three-phase ports 构建与三相电气系统单线图对应的模型。

Expanded three-phase ports 使用三个独立的电气守恒端口表示三相系统的各相。

## 所属库

Simscape / Electrical / Sensors & Transducers

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

## 描述

理想三相线电压测量

Line Voltage Sensor (Three-Phase) 模块表示理想三相线电压传感器。该模块测量三相系统的线间电压，并输出三元素物理信号向量。物理信号输出向量的每个元素与相间电压成比如下：

- 元素 1: *Vab* =
  *Va* -
  *Vb*
- 元素 2: *Vbc* =
  *Vb* -
  *Vc*
- 元素 3: *Vca* =
  *Vc* -
  *Va*

其中 *Va*、*Vb* 和 *Vc* 是绝对 *a*、*b* 和 *c* 相电压。

**注意**

必须将 Line Voltage Sensor (Three-Phase) 模块与三相元件并联连接。有关如何使用此模块的详细信息，请参阅构建和仿真复合与扩展三相模型。
