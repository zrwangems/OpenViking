---
type: simulink-block
title: 'Ideal Transformer'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Electrical Models / Electrical Elements'
documentation_page: 'idealtransformer'
documentation_source_path: 'ref/idealtransformer.html'
language: zh-CN
chinese_source: official
---

# Ideal Transformer

## 端口

### 守恒

### **1+** — 一次侧绕组正端子 电气

与一次侧绕组正端子关联的电气守恒端口。

### **1-** — 一次侧绕组负端子 电气

与一次侧绕组负端子关联的电气守恒端口。

### **2+** — 二次侧绕组正端子 电气

与二次侧绕组正端子关联的电气守恒端口。

### **2-** — 二次侧绕组负端子 电气

与二次侧绕组负端子关联的电气守恒端口。

## 参数

### **绕组比** — 一次侧线圈匝数与二次侧线圈匝数的比率 `1` (默认) | 正标量

变压器的绕组比，即一次侧线圈匝数与二次侧线圈匝数的比率。

## 所属库

Simscape / Foundation Library / Electrical / Electrical Elements

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2007a 中推出**

## 描述

电气系统中的理想变压器

Ideal Transformer 模块对一个理想节能变压器进行建模，用以下方程描述：

V1=N·V2

I2=N·I1

其中：

- *V1* 是一次侧电压。
- *V2* 是二次侧电压。
- *I1* 是流入一次侧 **+** 端子的电流。
- *I2* 是流出二次侧 **+** 端子的电流。
- *N* 是绕组比。

连接到一次侧绕组和二次侧绕组的两个电气网络必须各自拥有自己的 Electrical Reference 模块。

可使用此模块来表示 AC 变压器或固态 DC 到 DC 转换器。要对具有电感和互感项的变压器进行建模，请使用 Mutual Inductor 模块。

Simscape™ 和 Simscape Electrical™ 库包含多个模块，可用于对同类型的变压器设备进行建模。但是，这些模块进行了不同的建模假设。要为您的应用选择正确的模块，您必须了解这些假设如何根据频率影响模块行为。有关详细信息，请参阅选择模块来建模变压器 (Simscape Electrical)。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的**初始目标**部分。有关详细信息，请参阅设置模块变量的优先级和初始目标值。

标称值提供了一种指定模型中变量的预期模的方法。使用基于标称值的系统缩放可提高仿真的稳健性。标称值可以来自不同的来源，其中之一是模块对话框或属性检查器中的的**标称值**部分。有关详细信息，请参阅Modify Nominal Values for a Block Variable。
