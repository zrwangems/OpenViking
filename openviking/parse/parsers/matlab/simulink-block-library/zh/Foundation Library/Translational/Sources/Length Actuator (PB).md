---
type: simulink-block
title: 'Length Actuator (PB)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Translational / Sources'
documentation_page: 'lengthactuatorpb'
documentation_source_path: 'ref/lengthactuatorpb.html'
language: zh-CN
chinese_source: worker-translation
---

# Length Actuator (PB)

## 端口

### 输入

### **S** — 控制信号，m 物理信号

用于驱动源的物理信号输入端口。此端口上的正信号会施加从端口 **B** 到端口 **F** 的正力，并且当执行器长度为正值时，使端口 **B** 和 **F** 分开。
### 守恒

### **B** — 基座端口，基于位置的机械平移

基于位置的机械平移守恒端口，表示基座连接。

### **F** — 从动端口，基于位置的机械平移

基于位置的机械平移守恒端口，表示从动连接。对于正长度，端口 **F** 的位置比端口 **B** 更正。

## 参数

未在 R2025b 中记录。

## 所属库

Simscape / Foundation Library / Translational / Sources

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

理想执行器，保持长度与输入信号成比例

Length Actuator (PB) 模块表示一个理想执行器，无论连接端口上的负载如何，都保持指定长度。

连接 **B** 和 **F** 是基于位置的机械平移守恒端口。端口 **S** 上的物理信号指定端口 **B** 和 **F** 之间的距离。端口 **S** 上的正信号表示端口 **F** 的位置比端口 **B** 更正。

该模块记录以下变量：

- `f` — 端口 **B** 施加到端口 **F** 的力。记录的正力表示当长度为正值时，执行器使端口分开，即执行器处于压缩状态。记录的负力表示当长度为正值时，执行器使端口彼此靠近，即执行器处于拉伸状态。
- `v` — 相对速度，v=vF−vB
- `length` — 端口之间的距离，由端口 **S** 上的信号指定，length=xF−xB。

有关详细信息，请参阅数据记录。
