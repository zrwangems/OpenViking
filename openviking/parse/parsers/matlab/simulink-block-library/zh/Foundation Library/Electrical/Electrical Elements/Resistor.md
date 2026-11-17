---
type: simulink-block
title: 'Resistor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Elements'
documentation_page: 'resistor'
documentation_source_path: 'ref/resistor.html'
language: zh-CN
chinese_source: worker-translation
---

# Resistor

## 端口

### 守恒端口

### **+** — 正极端子电气

与电阻正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与电阻负极端子关联的电气守恒端口。

## 参数

### **Resistance** — 电阻的阻值 `1 Ohm`（默认）| 正标量

电阻值。

## 所属库

Simscape / Foundation Library / Electrical / Electrical Elements

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

电气系统中的线性电阻

Resistor 模块对线性电阻进行建模，用以下方程描述：

V=I·R

其中：

- *V* 是电压。
- *I* 是电流。
- *R* 是电阻。

连接 + 和 – 是对应于电阻正极端子和负极端子的守恒电气端口。按照惯例，电阻两端的电压由 *V*(+) – *V*(–) 给出，当电流从正极端子流向负极端子通过器件时，电流的符号为正。此惯例确保电阻吸收的功率始终为正。

### 变量

要在仿真之前为模块变量设置优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同的来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
