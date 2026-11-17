---
type: simulink-block
title: 'Capacitor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Elements'
documentation_page: 'capacitor'
documentation_source_path: 'ref/capacitor.html'
language: zh-CN
chinese_source: worker-translation
---

# Capacitor

## 端口

### 守恒端口

### **+** — 正极端子电气

与电容正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与电容负极端子关联的电气守恒端口。

## 参数

### **Capacitance** — 电容的电容值 `1e-6 F`（默认）| 正标量

电容值。

### **Series resistance** — 小寄生效应 `1e-6 Ohm`（默认）| 非负标量

表示小寄生效应。串联电阻可用于表示元件内阻、等效串联电阻（ESR）或连接电阻。某些电路的仿真可能需要存在小串联电阻。

### **Parallel conductance** — 小寄生效应 `0 1/Ohm`（默认）| 非负标量

表示小寄生效应。直接跨接在电容两端的并联电导可用于建模介质损耗，或每伏特的泄漏电流。

## 所属库

Simscape / Foundation Library / Electrical / Electrical Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

电气系统中的线性电容

Capacitor 模块对线性电容进行建模，用以下方程描述：

I=CdVdt

其中：

- *I* 是电流。
- *C* 是电容。
- *V* 是电压。
- *t* 是时间。

**Series resistance** 和 **Parallel conductance** 参数表示小寄生效应。直接跨接在电容两端的并联电导可用于建模介质损耗，或等效地建模每伏特的泄漏电流。串联电阻可用于表示元件等效串联电阻（ESR）或连接电阻。某些电路的仿真可能需要存在小串联电阻。有关更多信息，请参阅 Modeling Best Practices。

连接 + 和 – 是对应于电容正极和负极端子的守恒电气端口。如果电流从正极流向负极，则电流为正，电容两端的电压等于正极端子电压与负极端子电压之差，*V*(+) – *V*(–)。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关更多信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期量级的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关更多信息，请参阅 Modify Nominal Values for a Block Variable。

**Current** 和 **Voltage** 是电气域变量。**Capacitor voltage** 是电容两端的初始电压。有关更多信息，请参阅模块源代码。
