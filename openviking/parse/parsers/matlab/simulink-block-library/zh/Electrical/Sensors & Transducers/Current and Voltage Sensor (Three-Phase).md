---
type: simulink-block
title: 'Current and Voltage Sensor (Three-Phase)'
family: 'sensors-transducers'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sensors & Transducers'
documentation_page: 'currentandvoltagesensorthreephase'
documentation_source_path: 'ref/currentandvoltagesensorthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Current and Voltage Sensor (Three-Phase)

## 端口

### 输出

### **V** — 电压物理信号

与 *a* 相、*b* 相和 *c* 相电压关联的三元素物理信号向量输出端口。

### **I** — 电流物理信号

与 *a* 相、*b* 相和 *c* 相电流关联的三元素物理信号向量输出端口。

### 守恒

### **~1** — 三相电压和电流电气

与三相电压和电流关联的可扩展三相电气守恒端口 1。

### **~2** — 三相电压和电流电气

与三相电压和电流关联的可扩展三相电气守恒端口 2。

## 参数

### **建模选项** — 是否对复合或扩展三相端口建模 `Composite three-phase ports`（默认） | `Expanded three-phase ports`

是否对复合或扩展三相端口建模。

复合三相端口使用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口构建对应于三相电气系统单线图的模型。

扩展三相端口使用三个单独的电气守恒端口表示三相系统的各相。

### **电压测量类型** — 电压测量类型 `phase-to-phase voltage`（默认） | `phase-to-ground voltage`

电压测量的类型。

### **测量输出单位** — 测量系统 `Per unit`（默认） | `SI`

输出电流和电压测量的单位制。

### **标称功率** — 标称功率 `100e6` `V*A`（默认）

标称功率。

#### 依赖关系

要启用此参数，请将 **测量输出单位** 设置为 `Per unit`。

### **标称电压（相间 RMS）** — 标称电压 `24e3` `V`（默认）

标称相间均方根 (RMS) 电压。

#### 依赖关系

要启用此参数，请将 **测量输出单位** 设置为 `Per unit`。

## 所属库

Simscape / Electrical / Sensors & Transducers

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

## 描述

理想三相电流和电压传感器

Current and Voltage Sensor (Three-Phase) 模块测量三相电气节点的电压和电流。

**注意**

必须将 Current and Voltage Sensor (Three-Phase) 模块与三相元件串联。有关如何使用此模块的详细信息，请参阅构建和仿真复合与扩展三相模型。
