---
type: simulink-block
title: 'Translational Damper (PB)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Position-Based Mechanical Translational Models / Elements'
documentation_page: 'translationaldamperpb'
documentation_source_path: 'ref/translationaldamperpb.html'
language: zh-CN
chinese_source: worker-translation
---

# Translational Damper (PB)

## 端口

### 守恒端口

### **B** — 基座端口，基于位置的机械平移

基于位置的机械平移守恒端口，表示基座连接。

### **F** — 从动端口，基于位置的机械平移

基于位置的机械平移守恒端口，表示从动连接。对于正长度，端口 **F** 的位置比端口 **B** 更正。

## 参数

### **Damping coefficient** — 由黏性摩擦定义的阻尼系数 `1e5 N/(m/s)`（默认） | scalar

由黏性摩擦定义的阻尼系数。

## 所属库

Simscape / Foundation Library / Translational / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

基于位置的机械平移系统中的黏性阻尼器

Translational Damper (PB) 模块表示基于位置的机械平移系统中的理想黏性阻尼器。该模块使用以下方程

f=−D⋅v

v=vF−vB

length=xF−xB

power\_dissipated=D⋅v2

其中：

- *f* 是通过阻尼器传递的力。
- *D* 是由黏性摩擦定义的阻尼系数。
- *v* 是相对速度。
- *v*F 和 *v*B 分别是端口 **B** 和 **F** 的绝对速度。
- *length* 是阻尼器长度。
- *x*B 和 *x*F 分别是端口 **B** 和 **F** 的绝对位置。
- *power\_dissipated* 是通过阻尼器耗散的功率。

连接 **B** 和 **F** 是基于位置的机械平移守恒端口。阻尼器力从端口 **B** 作用到端口 **F**。第一个方程中的负号反映了基于位置的机械平移域中使用的力流约定。有关详细信息，请参阅双端口模块方向和力流约定。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅修改模块变量的标称值。
