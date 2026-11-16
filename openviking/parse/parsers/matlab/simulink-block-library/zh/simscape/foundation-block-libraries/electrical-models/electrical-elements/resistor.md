---
type: simulink-block
title: 'Resistor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Electrical Models / Electrical Elements'
documentation_page: 'resistor'
documentation_source_path: 'ref/resistor.html'
language: zh-CN
chinese_source: official
---

# Resistor

## 端口

### 守恒

### **+** — 正极端子 电气

与电阻器正极端子相关联的电气守恒端口。

### **-** — 负极端子 电气

与电阻器负极端子相关联的电气守恒端口。

## 参数

### **电阻** — 电阻器的电阻 `1 Ohm` (默认) | 正标量

电阻值。

## 所属库

Simscape / Foundation Library / Electrical / Electrical Elements

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2007a 中推出**

## 描述

电气系统中的线性电阻器

Resistor 模块对一个线性电阻器进行建模，用以下方程描述：

V=I·R

其中：

- *V* 是电压。
- *I* 是电流。
- *R* 是电阻。

连接端 + 和 - 是分别对应于电阻器的正极端子和负极端子的守恒电气端口。根据约定，电阻器两端的电压根据 *V*(+) – *V*(–) 得出，当电流从器件的正极端子流向负极端子时，电流的符号为正。此约定可确保电阻器吸收的功率始终为正。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的**初始目标**部分。有关详细信息，请参阅设置模块变量的优先级和初始目标值。

标称值提供了一种指定模型中变量的预期模的方法。使用基于标称值的系统缩放可提高仿真的稳健性。标称值可以来自不同的来源，其中之一是模块对话框或属性检查器中的的**标称值**部分。有关详细信息，请参阅Modify Nominal Values for a Block Variable。
