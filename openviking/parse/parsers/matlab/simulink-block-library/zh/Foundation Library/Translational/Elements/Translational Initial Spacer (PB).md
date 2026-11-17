---
type: simulink-block
title: 'Translational Initial Spacer (PB)'
family: 'translational'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Translational / Elements'
documentation_page: 'translationalinitialspacerpb'
documentation_source_path: 'ref/translationalinitialspacerpb.html'
language: zh-CN
chinese_source: worker-translation
---

# Translational Initial Spacer (PB)

## 端口

### 守恒

### **B** — 基座端口，基于位置的机械平移

表示基座连接的基于位置的机械平移守恒端口。

### **F** — 从动端口，基于位置的机械平移

表示从动连接的基于位置的机械平移守恒端口。对于正长度，端口 **F** 的位置比端口 **B** 更正。

## 参数

R2025b 中未记录。

## 所属库

Simscape / Foundation Library / Translational / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

模块之间的初始距离

Translational Initial Spacer (PB) 模块提供端口 **B** 和 **F** 之间的初始距离。

连接 **B** 和 **F** 是基于位置的机械平移守恒端口。当端口 **F** 的位置比端口 **B** 更正时，长度为正值。该模块不传递力。

该模块没有参数。您将长度指定为初始变量目标。

### 变量

要在仿真之前为模块变量设置优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅为模块变量设置优先级和初始目标。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅修改模块变量的标称值。
