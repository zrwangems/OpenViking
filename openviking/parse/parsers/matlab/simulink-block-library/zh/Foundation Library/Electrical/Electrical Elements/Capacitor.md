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
chinese_source: official
---

# Capacitor

## 端口

### 守恒

### **+** — 正极端子 电气

与电容器正极端子相关联的电气守恒端口。

### **-** — 负极端子 电气

与电容器负极端子相关联的电气守恒端口。

## 参数

### **电容** — 电容器的电容 `1e-6 F` (默认) | 正标量

电容值。

### **串联电阻** — 小的寄生效应 `1e-6 Ohm` (默认) | 非负标量

表示小的寄生效应。串联电阻可用于表示组件内部电阻、有效串联电阻 (ESR) 或连接电阻。某些电路的仿真可能需要有小的串联电阻。

### **并联电导** — 小的寄生效应 `0 1/Ohm` (默认) | 非负标量

表示小的寄生效应。直接跨电容器的并联电导可用于对介电损耗或每伏漏电流进行建模。

## 所属库

Simscape / Foundation Library / Electrical / Electrical Elements

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2007a 中推出**

## 描述

电气系统中的线性电容器

Capacitor 模块对一个线性电容器进行建模，用以下方程描述：

I=CdVdt

其中：

- *I* 是电流。
- *C* 是电容。
- *V* 是电压。
- *t* 是时间。

**串联电阻**和**并联电导**参数表示小的寄生效应。直接跨电容器的并联电导可用于对介电损耗或等效的每伏漏电流进行建模。串联电阻可用于表示组件有效串联电阻 (ESR) 或连接电阻。某些电路的仿真可能需要有小的串联电阻。有关详细信息，请参阅Modeling Best Practices。

连接端 + 和 - 是分别对应于电容器的正极端子和负极端子的守恒电气端口。如果电流从正极流向负极，则电流为正，电容器两端的电压等于正极端子电压与负极端子电压之差，即 *V*(+) – *V*(-)。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的**初始目标**部分。有关详细信息，请参阅设置模块变量的优先级和初始目标值。

标称值提供了一种指定模型中变量的预期模的方法。使用基于标称值的系统缩放可提高仿真的稳健性。标称值可以来自不同的来源，其中之一是模块对话框或属性检查器中的的**标称值**部分。有关详细信息，请参阅Modify Nominal Values for a Block Variable。

**电流**和**电压**是电气域变量。**电容器电压**是电容器两端的初始电压。有关详细信息，请参阅模块源代码。
