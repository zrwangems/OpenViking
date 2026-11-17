---
type: simulink-block
title: 'P-H Diagram (2P)'
family: 'two-phase-fluid'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Utilities'
documentation_page: 'phdiagram2p'
documentation_source_path: 'ref/phdiagram2p.html'
language: zh-CN
chinese_source: worker-translation
---

# P-H Diagram (2P)

## 端口

### 输入

### **p** — 压力，MPa 向量

压力向量。该向量的元素数量必须与端口 **h** 处的比焓信号相同

### **h** — 比焓，kJ/kg 向量

比焓向量。该向量的元素数量必须与端口 **p** 处的压力信号相同。

## 参数

R2025b 中未记录。

## 所属库

Simscape / Fluids / Two-Phase Fluid / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块可用于在生成代码的系统中提供仿真可见性，但不会包含在生成的代码中。

## 版本历史

**在 R2021a 中引入**

### R2025a: 更改单位并指定循环点顺序

单击 Settings 按钮  以指定单位和循环点顺序。您可以指定压力、比焓和温度单位。清除 **Array element order of inputs p and h with closed loop** 复选框，以使用 **Array indices of inputs p and h** 参数指定模块连接循环点的顺序。

### R2022b: 访问回放功能

使用图形窗口顶部的控件控制并回放最近一次仿真的动画。

## 描述

两相流体网络的热力学示波器

P-H Diagram (2P) 模块绘制热力学两相流体的压力相对于比焓的 p-h 图。p-h 图指示热力学循环期间关键点处的流体状态。

图中的每个编号点指示制冷循环中动态过程之后的流体状态：

1. 低压冷蒸气
2. 高压热蒸气
3. 高压热液体
4. 低压混合蒸气和液体

要使用 P-H Diagram (2P) 模块：

1. 在要监测的每个位置放置一个 Thermodynamic Properties Sensor (2P) 模块和一个 Pressure, Temperature & Internal Energy Sensor (2P) 模块。

   **注意**

   Pressure & Internal Energy Sensor (2P) 模块测量压差。将端口 **A** 连接到监测点，将端口 **B** 连接到 Absolute Reference (2P) 模块。
2. 使用 PS-Simulink Converter 模块将 Simscape 物理信号转换为 Simulink 信号。
3. 使用 Mux 模块合并压力信号。将输出信号连接到 P-H Diagram (2P) 的 **p** 端口。
4. 使用 Mux 模块合并转换后的比焓信号，并将输出信号连接到 **h** 端口。
5. 在运行仿真之前，双击 P-H Diagram (2P) 模块，然后单击 Select fluid properties 按钮  以设置网络流体属性。

   如果不选择流体属性，该模块将使用默认的两相网络流体，即水。

### 设置

单击 Settings 按钮  以指定压力、比焓和温度单位以及元素顺序。清除 **Array element order of inputs p and h with closed loop** 复选框，以使用 **Array indices of inputs p and h** 参数指定模块连接循环点的顺序。

### P-H Diagram 回放

您还可以回放最近一次仿真的动画。运行模型后，双击该模块，并使用窗口顶部的按钮控制动画。使用 **Time** 字段右侧的下拉菜单控制回放速率。在运行仿真之前、加载模型时以及仿真运行时，回放控件处于禁用状态。

使用回放滑块或 **Time** 字段控制仿真周期。如果输入的时间不是模型时间步，该模块将显示下一个最接近的时间步。

要保存绘图的当前迭代，请指向绘图区域。从绘图右上角的图标中，单击 Export 图标  并选择 Save As 按钮  以保存绘图。
