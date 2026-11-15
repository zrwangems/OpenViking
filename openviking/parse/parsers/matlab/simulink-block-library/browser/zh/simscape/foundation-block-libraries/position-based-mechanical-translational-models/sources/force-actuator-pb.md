---
type: simulink-block
title: 'Force Actuator (PB)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Position-Based Mechanical Translational Models / Sources'
documentation_page: 'forceactuatorpb'
documentation_source_path: 'ref/forceactuatorpb.html'
language: zh-CN
chinese_source: worker-translation
---

# Force Actuator (PB)

## 端口

### 输入

### **S** — 控制信号，N physical signal

用于驱动源的控制信号的 physical signal 输入端口。此端口处的正信号在端口 **F** 处向网络施加正力，并且当执行器长度为正值时，用于分离端口 **B** 和 **F**。

### 守恒

### **B** — 基座端口，基于位置的机械平移

表示基座连接的基于位置的机械平移守恒端口。

### **F** — 从动端口，基于位置的机械平移

表示从动连接的基于位置的机械平移守恒端口。对于正长度，端口 **F** 的位置比端口 **B** 更正。

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

带长度的理想力执行器，生成与输入信号成比例的力

Force Actuator (PB) 模块表示一种具有长度的理想力执行器，其生成指定的力，而与连接端口处的负载或速度无关。

连接 **B** 和 **F** 是基于位置的机械平移守恒端口。在 physical signal 端口 **S** 指定力。端口 **S** 处的正信号在端口 **F** 处向网络施加正力，并且当执行器长度为正值时，用于分离端口 **B** 和 **F**。

例如，在此模型中，Force Actuator (PB) 模块在两个弹簧之间施加 1 N 的正力。导轨的正方向为水平方向，从左到右。

施加力后的模型图

端口 **F** 向右侧弹簧施加正力。该弹簧处于压缩状态。同时，由于执行器力用于分离端口，端口 **B** 向左侧弹簧施加大小相等但方向相反的力。该弹簧也处于压缩状态。

该模块记录以下变量：

- `f` — 力
- `v` — 相对速度，v=vF−vB

有关详细信息，请参阅数据记录。

执行器长度为 length=xF−xB。

该模块没有参数。您将执行器长度指定为初始变量目标。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可来自不同来源，其中之一是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅修改模块变量的标称值。
