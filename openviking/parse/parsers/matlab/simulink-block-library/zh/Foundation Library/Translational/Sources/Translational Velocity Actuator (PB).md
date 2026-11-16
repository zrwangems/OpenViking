---
type: simulink-block
title: 'Translational Velocity Actuator (PB)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Translational / Sources'
documentation_page: 'translationalvelocityactuatorpb'
documentation_source_path: 'ref/translationalvelocityactuatorpb.html'
language: zh-CN
chinese_source: worker-translation
---

# Translational Velocity Actuator (PB)

## 端口

### 输入

### **S** — 指定端口之间相对速度的控制信号，m/s 物理信号

用于驱动源的控制信号的物理信号输入端口。此端口上的正信号表示端口
**F** 处的速度大于端口 **B** 处的速度。
### 守恒

### **B** — 基座端口，基于位置的机械平移

基于位置的机械平移守恒端口，表示基座连接。

### **F** — 从动端口，基于位置的机械平移

基于位置的机械平移守恒端口，表示从动连接。对于正长度，端口 **F** 的位置比端口 **B** 更正。

## 参数

R2025b 中未记录。

## 所属库

Simscape / Foundation Library / Translational / Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

带长度的理想速度执行器，保持速度与输入信号成比例

Translational Velocity Actuator (PB) 模块表示一个带长度的理想速度执行器，无论所连接端口处的负载如何，它都维持指定的相对速度。

连接 **B** 和 **F** 是基于位置的机械平移守恒端口。端口 **S**
处的物理信号指定端口 **B** 和
**F** 之间的相对速度。端口 **S** 处的正信号表示端口
**F** 处的速度大于端口 **B** 处的速度。

该模块记录以下变量：

- `f` — 端口 **B** 施加到端口
  **F** 的力。记录的正力表示当长度为正值时，执行器作用于使端口分开，即执行器处于压缩状态。记录的负力表示当长度为正值时，执行器作用于使端口彼此靠近，即执行器处于拉伸状态。
- `v` — 端口之间的相对速度，由端口
  **S** 处的信号指定，v=vF−vB

有关详细信息，请参阅数据记录。

执行器长度为 length=xF−xB。

该模块没有参数。您将执行器长度指定为初始变量目标。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用
模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

标称值提供了一种指定模型中变量预期量值的方法。
使用基于标称值的系统缩放可提高仿真的稳健性。标称
值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **标称值** 部分。有关
详细信息，请参阅修改模块变量的标称值。
