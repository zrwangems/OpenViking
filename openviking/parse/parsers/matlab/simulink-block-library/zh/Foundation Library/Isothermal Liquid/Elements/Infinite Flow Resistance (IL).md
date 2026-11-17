---
type: simulink-block
title: 'Infinite Flow Resistance (IL)'
family: 'isothermal-liquid'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Elements'
documentation_page: 'infiniteflowresistanceil'
documentation_source_path: 'ref/infiniteflowresistanceil.html'
language: zh-CN
chinese_source: worker-translation
---

# Infinite Flow Resistance (IL)

## 端口

### 守恒

### **A** — 流量为零的等温液体

无流体流动的等温液体守恒端口。

### **B** — 流量为零的等温液体

无流体流动的等温液体守恒端口。

## 参数

在 R2025b 中未记录。

## 所属库

Simscape / Foundation Library / Isothermal Liquid / Elements

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

用于设置两个节点之间初始压力差的等温液体元件

Infinite Flow Resistance (IL) 模块表示等温液体网络中的一个断口。没有液体流过该断口。但是，由连接到回路的 Isothermal Liquid Properties (IL) 模块指定的液体属性在断口两侧相同。使用此模块可将优先级和初始目标值设置为端口 **A** 和端口 **B** 之间的压力差。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅为模块变量设置优先级和初始目标。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅修改模块变量的标称值。
