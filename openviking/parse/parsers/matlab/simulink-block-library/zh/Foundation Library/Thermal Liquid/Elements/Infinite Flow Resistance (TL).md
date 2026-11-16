---
type: simulink-block
title: 'Infinite Flow Resistance (TL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal Liquid / Elements'
documentation_page: 'infiniteflowresistancetl'
documentation_source_path: 'ref/infiniteflowresistancetl.html'
language: zh-CN
chinese_source: worker-translation
---

# Infinite Flow Resistance (TL)

## 端口

### 守恒

### **A** — 流量为零的热流体

无流体或热流的热流体守恒端口。

### **B** — 流量为零的热流体

无流体或热流的热流体守恒端口。

## 参数

未在 R2025b 中记录。

## 所属库

Simscape / Foundation Library / Thermal Liquid / Elements

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2014b 中引入**

## 描述

热流体网络中的完全隔热断点

Infinite Flow Resistance (TL) 模块表示热流体网络中的一个断点。没有质量或能量流过该断点。但是，由连接到该回路的 Thermal Liquid Settings (TL) 模块指定的流体属性在断点两侧相同。使用此模块可设置端口 **A** 和端口 **B** 之间压力和温度差的优先级和初始目标值。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅修改模块变量的标称值。
