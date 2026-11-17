---
type: simulink-block
title: 'Translational Initial Spacer (PB)'
family: 'simscape'
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
```yaml
ports:
- name: B
  summary: 基于位置的机械平移基础端口
  direction: conserving
- name: F
  summary: 基于位置的机械平移从动端口
  direction: conserving
```

### 守恒端口

### **B** — 基于位置的机械平移基础端口

基于位置的机械平移守恒端口，表示基础连接。

### **F** — 基于位置的机械平移从动端口

基于位置的机械平移守恒端口，表示从动连接。对于正长度，端口 **F** 的位置比端口 **B** 更正。
## 参数
```yaml
parameters: []
```

在 R2025b 中未记录。
## 所属库

Simscape / Foundation Library / Translational / Elements

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

模块之间的初始距离

Translational Initial Spacer (PB) 模块在端口 **B** 和 **F** 之间提供初始距离。

连接 **B** 和 **F** 是基于位置的机械平移守恒端口。当端口 **F** 的位置比端口 **B** 更正时，长度为正值。该模块不传递力。

该模块没有参数。您将长度指定为初始变量目标。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同的来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
