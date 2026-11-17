---
type: simulink-block
title: 'Ideal Transformer'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Elements'
documentation_page: 'idealtransformer'
documentation_source_path: 'ref/idealtransformer.html'
language: zh-CN
chinese_source: worker-translation
---

# Ideal Transformer

## 端口

### 守恒端口

### **1+** — 一次绕组正极端子 electrical

与一次绕组正极端子关联的电学守恒端口。

### **1-** — 一次绕组负极端子 electrical

与一次绕组负极端子关联的电学守恒端口。

### **2+** — 二次绕组正极端子 electrical

与二次绕组正极端子关联的电学守恒端口。

### **2-** — 二次绕组负极端子 electrical

与二次绕组负极端子关联的电学守恒端口。

## 参数

### **Winding ratio** — 一次线圈匝数与二次线圈匝数之比 `1`（默认）| 正标量

变压器的绕组比，即一次线圈匝数与二次线圈匝数之比。

## 所属库

Simscape / Foundation Library / Electrical / Electrical Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

电气系统中的理想变压器

Ideal Transformer 模块对理想功率守恒变压器进行建模，用以下方程描述：

V1=N·V2

I2=N·I1

其中：

- *V1* 是一次电压。
- *V2* 是二次电压。
- *I1* 是流入一次 **+** 端子的电流。
- *I2* 是流出二次 **+** 端子的电流。
- *N* 是绕组比。

连接到一次绕组和二次绕组的两个电气网络必须各自拥有自己的 Electrical Reference 模块。

使用此模块表示交流变压器或固态 DC-DC 转换器。
要对具有电感和互感项的变压器进行建模，请使用 Mutual Inductor 模块。

Simscape™ 和 Simscape Electrical™ 库包含多个可以对同一类型变压器设备进行建模的模块。然而，这些模块做出不同的建模假设。要为您的应用选择正确的模块，您必须了解这些假设如何影响模块行为随频率的变化。有关详细信息，请参阅 Choose Blocks to Model Transformers (Simscape Electrical)。

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
