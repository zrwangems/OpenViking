---
type: simulink-block
title: 'Translational Spring (PB)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Translational / Elements'
documentation_page: 'translationalspringpb'
documentation_source_path: 'ref/translationalspringpb.html'
language: zh-CN
chinese_source: worker-translation
---

# Translational Spring (PB)

## 端口

### 守恒

### **B** — 基于位置的机械平移基础端口

基于位置的机械平移守恒端口，表示基础连接。

### **F** — 基于位置的机械平移从动端口

基于位置的机械平移守恒端口，表示从动连接。对于正长度，端口 **F** 的位置比端口 **B** 更正。

## 参数

### **Spring stiffness** — 弹簧刚度 `1e5 N/m`（默认）| 标量

弹簧刚度。

## 所属库

Simscape / Foundation Library / Translational / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

基于位置的机械平移系统中的理想弹簧

Translational Spring (PB) 模块表示一个理想平移弹簧。弹簧变形量是长度与静止长度之差。正变形量增加长度。

f=−K⋅δ

δ=length−lengthrest

length=xF−xB

其中：

- *f* 是通过弹簧传递的力。
- *K* 是弹簧刚度。
- *δ* 是弹簧变形量。
- *length* 是弹簧长度。
- *length*rest 是弹簧静止长度。
- *x*B 和 *x*F 分别是端口 **B** 和 **F** 的绝对位置。
- *power\_dissipated* 是通过阻尼器耗散的功率。

连接 **B** 和 **F** 是基于位置的机械平移守恒端口。弹簧力从端口 **B** 作用于端口 **F**。正弹簧力驱动端口 **F** 沿正方向运动。如果长度为正，正弹簧力对应于弹簧处于压缩状态。有关更多信息，请参阅 Two-Port Block Orientation and Force Flow Conventions。

### 变量

要在仿真之前为模块变量设置优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关更多信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关更多信息，请参阅 Modify Nominal Values for a Block Variable。

初始化模块的正确方式取决于其在框图中的作用：

- 通常，将任意两个变量指定为高优先级目标，例如 **Force** 和 **Length**，或 **Rest length** 和 **Deformation**。例外是 **Force** 和 **Deformation**，因为这两个变量彼此成比例。
- 如果弹簧与已知力串联，则仅将 **Length** 或 **Rest length** 指定为高优先级目标。
- 如果弹簧与已知长度并联，则仅将 **Force**、**Deformation** 或 **Rest length** 指定为高优先级目标。
- 如果弹簧与已知力串联并与已知长度并联，则不要指定任何高优先级目标。
