---
type: simulink-block
title: 'Mutual Inductor'
family: 'electrical'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Elements'
documentation_page: 'mutualinductor'
documentation_source_path: 'ref/mutualinductor.html'
language: zh-CN
chinese_source: worker-translation
---

# Mutual Inductor

## 端口

### 守恒

### **1+** — 一次绕组正极端子（电气）

与一次绕组正极端子关联的电气守恒端口。

### **1-** — 一次绕组负极端子（电气）

与一次绕组负极端子关联的电气守恒端口。

### **2+** — 二次绕组正极端子（电气）

与二次绕组正极端子关联的电气守恒端口。

### **2-** — 二次绕组负极端子（电气）

与二次绕组负极端子关联的电气守恒端口。

## 参数

### **电感 L1** — 一次绕组的自感 `10 H`（默认） | 正标量

一次绕组的自感。

### **电感 L2** — 二次绕组的自感 `0.1 H`（默认） | 正标量

二次绕组的自感。

### **完美耦合 – 无漏磁** — 使用理想互感 `Off`（默认） | `On`

如果您选中此复选框，该模块会将耦合系数设为 1，并将漏磁阻设为 0。在这种情况下，该模块表示无漏磁且无快极点的理想互感，同时仍保留正确的低频行为，并阻断直流。

### **耦合系数** — 互感的耦合系数 `0.9`（默认） | 范围 (0,1) 内的标量

耦合系数，用于定义互感。该参数值应大于零且小于 1。避免将此参数设置为接近 1 的值（例如 0.9999），因为这会引入快速的仿真动态。

#### 依赖项

要启用此参数，请清除 **完美耦合 – 无漏磁** 复选框。

## 所属库

Simscape / Foundation Library / Electrical / Electrical Elements

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

电气系统中的互感

Mutual Inductor 模块对互感进行建模，由以下方程描述：

V1=L1dI1dt+MdI2dt

V2=L2dI2dt+MdI1dt

M=kL1·L2

其中：

- *V1* 是一次绕组两端的电压。
- *V2* 是二次绕组两端的电压。
- *I1* 是流入一次绕组 **+** 端子的电流。
- *I2* 是流出二次绕组 **+** 端子的电流。
- *L1*、*L2* 是绕组自感。
- *M* 是互感。
- *k* 是耦合系数，0 < *k* < 1。
- *t* 是时间。

连接到一次绕组和二次绕组的两个电气网络必须各自具有自己的 Electrical Reference 模块。

使用此模块表示交流变压器。如果电感项和互感项在模型中不重要，或者未知，则可以改用 Ideal Transformer 模块。

Simscape™ 和 Simscape Electrical™ 库包含若干可对同一类型变压器设备建模的模块。但是，这些模块做出的建模假设不同。要为您的应用选择正确的模块，必须理解这些假设如何影响模块随频率变化的行为。有关详细信息，请参阅选择用于对变压器建模的模块 (Simscape Electrical)。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅修改模块变量的标称值。
