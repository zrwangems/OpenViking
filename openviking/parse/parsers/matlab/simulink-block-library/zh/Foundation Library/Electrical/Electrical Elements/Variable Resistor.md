---
type: simulink-block
title: 'Variable Resistor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Elements'
documentation_page: 'variableresistor'
documentation_source_path: 'ref/variableresistor.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable Resistor

## 端口

### 输入

### **R** — 电阻控制信号，Ohm 物理信号

用于指定电阻值的输入物理信号。
### 守恒

### **+** — 正极端子 电气

与电阻正极端子关联的电气守恒端口。

### **-** — 负极端子 电气

与电阻负极端子关联的电气守恒端口。

### **H** — 热端口 热

提供电阻温度的热守恒端口。

#### 依赖关系

要启用此端口，请选中 **Add thermal port** 复选框。

## 参数

### **Minimum resistance R>=0** — 最小可接受电阻 `0 Ohm`（默认）| 非负标量

最小电阻值。如果输入信号低于此水平（例如变为负值），则使用此最小电阻值。参数值必须为非负。

### **Add thermal port** — 控制热端口可见性 `Off`（默认）| `On`

选中此复选框将显示热端口 **H**，使您能够将电阻连接到热网络。选中此复选框还会启用 **Thermal mass** 参数，并将 **Temperature** 变量添加到 **Initial Targets** 和 **Nominal Values** 部分。

### **Thermal mass** — 电阻的热质量 `1 J/K`（默认）| 非负标量

电阻的热质量。

#### 依赖关系

要启用此参数，请选中 **Add thermal port** 复选框。

## 所属库

Simscape / Foundation Library / Electrical / Electrical Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

### R2023b：将模块连接到热网络

该模块现在具有可选的热端口 **H**，使您能够将电阻连接到热网络。要显示热端口，请选中 **Add thermal port** 复选框，并使用 **Thermal mass** 参数指定电阻的热质量。您还可以指定 **Temperature** 变量的初始目标。该复选框、参数和变量也是此版本中新增的。

## 描述

电气系统中的线性可变电阻

Variable Resistor 模块对线性可变电阻进行建模，用以下方程描述：

V=I·R

其中：

- *V* 是电压。
- *I* 是电流。
- *R* 是电阻，即控制端口处的信号值。

连接 **+** 和 **-** 是对应于电阻正极和负极端子的守恒电气端口。**R** 是控制电阻值的物理信号输入端口。如果电流从正极流向负极，则电流为正，电阻两端的电压等于正极端子与负极端子电压之差，*V*(+) – *V*(–)。

可选的热端口 **H** 使您能够将电阻连接到热网络。要显示热端口，请选中 **Add thermal port** 复选框，并使用 **Thermal mass** 参数指定电阻的热质量。您还可以指定 **Temperature** 变量的初始目标。该模块不对其他效应建模，例如基于温度的电阻变化。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期量级的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
