---
type: simulink-block
title: 'Translational Spacer (PB)'
family: 'translational'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Translational / Elements'
documentation_page: 'translationalspacerpb'
documentation_source_path: 'ref/translationalspacerpb.html'
language: zh-CN
chinese_source: worker-translation
---

# Translational Spacer (PB)

## 端口

### 守恒

### **B** — 基础端口 基于位置的机械平移

表示基础连接的基于位置的机械平移守恒端口。

### **F** — 从动端口 基于位置的机械平移

表示从动连接的基于位置的机械平移守恒端口。对于正的 length，端口 **F** 的位置比端口 **B** 更正。

## 参数

R2025b 中未记录。

## 所属库

Simscape / Foundation Library / Translational / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

仿真期间模块之间的固定 length

Translational Spacer (PB) 模块在仿真期间保持端口 **B** 和 **F** 之间的固定 length：

length=xF−xB

vB=vF

连接 **B** 和 **F** 是基于位置的机械平移守恒端口。当端口 **F** 的位置比端口 **B** 更正时，length 为正。隔套力从端口 **B** 作用到端口 **F**。正的隔套力驱动端口 **F** 沿正方向运动。当 length 为正时，正的隔套力对应于隔套处于压缩状态。

该模块没有参数。您将 length 指定为初始变量目标。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

标称值提供了一种指定模型中变量预期量值的方法。使用基于标称值的系统缩放可提高仿真的稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅修改模块变量的标称值。

要指定 length：

- 对于已知的 length，将其指定为高优先级目标。
- 对于未知的固定 length，指定任意值并将优先级设置为低或无。
  然后求解器在模型初始化期间计算 length 的值。
