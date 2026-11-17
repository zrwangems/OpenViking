---
type: simulink-block
title: 'Translational Spacer (PB)'
family: 'simscape'
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
```yaml
ports:
- name: B
  summary: 基于位置的机械平移基准端口
  direction: unspecified
- name: F
  summary: 基于位置的机械平移从动端口
  direction: unspecified
```

### 守恒

### **B** — 基于位置的机械平移基准端口

基于位置的机械平移守恒端口，表示基准连接。

### **F** — 基于位置的机械平移从动端口

基于位置的机械平移守恒端口，表示从动连接。对于正长度，端口 **F** 的位置比端口 **B** 更正。
## 参数
```yaml
parameters: []
```

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

仿真期间模块间的固定长度

Translational Spacer (PB) 模块在仿真期间保持端口 **B** 和 **F** 之间的固定长度：

length=xF−xB

vB=vF

连接 **B** 和 **F** 是基于位置的机械平移守恒端口。当端口 **F** 的位置比端口 **B** 更正时，长度为正值。间隔力从端口 **B** 作用于端口 **F**。正间隔力驱动端口 **F** 沿正方向运动。当长度为正值时，正间隔力对应于间隔件处于压缩状态。

该模块没有参数。您将长度指定为初始变量目标。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。

要指定长度：

- 对于已知长度，将其指定为高优先级目标。
- 对于未知固定长度，指定任意值并将优先级设置为低或无。然后求解器在模型初始化期间计算长度的值。
