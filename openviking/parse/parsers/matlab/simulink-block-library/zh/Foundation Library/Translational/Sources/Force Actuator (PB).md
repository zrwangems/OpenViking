---
type: simulink-block
title: 'Force Actuator (PB)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Translational / Sources'
documentation_page: 'forceactuatorpb'
documentation_source_path: 'ref/forceactuatorpb.html'
language: zh-CN
chinese_source: worker-translation
---

# Force Actuator (PB)

## 端口
```yaml
ports:
- name: S
  summary: 控制信号，N 物理信号
  direction: input
- name: B
  summary: 基座端口 基于位置的机械平移
  direction: input
- name: F
  summary: 从动端口 基于位置的机械平移
  direction: input
```

### 输入

### **S** — 控制信号，N 物理信号

用于驱动源的物理信号输入端口。该端口上的正信号在端口 **F** 处向网络施加正力，并且当执行器长度为正值时，作用于分离端口 **B** 和 **F**。

### 守恒

### **B** — 基座端口 基于位置的机械平移

基于位置的机械平移守恒端口，表示基座连接。

### **F** — 从动端口 基于位置的机械平移

基于位置的机械平移守恒端口，表示从动连接。对于正长度，端口 **F** 的位置比端口 **B** 更正。
## 参数
```yaml
parameters: []
```

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

Force Actuator (PB) 模块表示一个具有长度的理想力执行器，无论连接端口处的负载或速度如何，它都会生成指定的力。

连接 **B** 和 **F** 是基于位置的机械平移守恒端口。在物理信号端口 **S** 处指定力。端口 **S** 上的正信号在端口 **F** 处向网络施加正力，并且当执行器长度为正值时，作用于分离端口 **B** 和 **F**。

例如，在此模型中，Force Actuator (PB) 模块在两个弹簧之间施加 1 N 的正力。导轨的正方向为水平方向，从左到右。

施加力的模型图

端口 **F** 向右侧弹簧施加正力。该弹簧处于压缩状态。同时，由于执行器力作用于分离端口，端口 **B** 向左侧弹簧施加大小相等但方向相反的力。该弹簧也处于压缩状态。

该模块记录以下变量：

- `f` — 力
- `v` — 相对速度，v=vF−vB

有关详细信息，请参阅数据记录。

执行器长度为 length=xF−xB。

该模块没有参数。您将执行器长度指定为初始变量目标。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅修改模块变量的标称值。
