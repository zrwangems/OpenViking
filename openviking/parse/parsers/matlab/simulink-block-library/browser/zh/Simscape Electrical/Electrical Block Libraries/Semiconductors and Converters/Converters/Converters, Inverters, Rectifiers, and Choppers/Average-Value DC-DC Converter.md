---
type: simulink-block
title: 'Average-Value DC-DC Converter'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Semiconductors and Converters / Converters / Converters, Inverters, Rectifiers, and Choppers'
documentation_page: 'averagevaluedcdcconverter'
documentation_source_path: 'ref/averagevaluedcdcconverter.html'
language: zh-CN
chinese_source: worker-translation
---

# Average-Value DC-DC Converter

## 端口

### 守恒端口

### **DutyCycle** — 占空比物理 | 标量

与占空比关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Control Input** 设置为 `Duty Cycle`。

**数据类型：** `double`

### **Iref** — 电流参考物理

与电流参考关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Control Input** 设置为 `Current reference`。

**数据类型：** `double`

### **Vref** — 电压参考物理

与电压参考关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Control Input** 设置为 `Voltage reference`。

**数据类型：** `double`

### **1+** — 正直流电压 1 电气 | 标量

与第一个直流电压的正端子关联的电气守恒端口。

**数据类型：** `double`

### **1-** — 负直流电压 1 电气 | 标量

与第一个直流电压的负端子关联的电气守恒端口。

**数据类型：** `double`

### **2+** — 正直流电压 2 电气 | 标量

与第二个直流电压的正端子关联的电气守恒端口。

**数据类型：** `double`

### **2-** — 负直流电压 2 电气 | 标量

与第二个直流电压的负端子关联的电气守恒端口。

**数据类型：** `double`

## 参数

### **Implementation mode** — 变换器实现模式 `Behavioral`（默认）| `Average value`

*自 R2025a 起*

用于指定变换器实现模式的选项。要控制逆变器状态变量，请将此参数设置为 `Average value`。要执行无动态的快速仿真，请将此参数设置为 `Behavioral`。

### **Converter type** — 变换器类型 `Buck converter`（默认）| `Buck-boost converter` | `Boost converter`

变换器的类型。

#### 依赖关系

要启用此参数，请将 **Control Input** 设置为 `Duty Cycle`，或将 **Implementation mode** 设置为 `Average value`。

### **Control input** — 控制输入 `Duty cycle`（默认）| `Current reference` | `Voltage reference`

指定用于在两侧之间转换电能的控制输入。

#### 依赖关系

要启用此参数，请将 **Implementation mode** 设置为 `Behavioral`。

### **Converter efficiency** — 变换器效率参数化 `Constant`（默认）| `Tabulated`

指定变换器效率的参数化。如果选择 `Tabulated`，则导通损耗取决于提供的输出电流。

**注意**

对于表格化效率，外推方法为最近邻。因此，效率不会高于 **Efficiency vector (%)** 参数中的最高值，也不会低于最低值。

#### 依赖关系

要启用此参数，请将 **Implementation mode** 设置为 `Behavioral`。

### **Efficiency (%)** — 变换器效率 `100`（默认）| 正标量

变换器效率，以百分比表示。

#### 依赖关系

要启用此参数，请将 **Implementation mode** 设置为 `Behavioral`，并将 **Converter efficiency** 设置为 `Constant`。

### **Output current vector** — 输出电流向量 `[0, 2, 5]` `A`（默认）| 至少包含两个元素的行向量

输出电流向量。

#### 依赖关系

要启用此参数，请将 **Implementation mode** 设置为 `Behavioral`，并将 **Converter efficiency** 设置为 `Tabulated`。

### **Efficiency vector (%)** — 效率向量 `[90, 95, 98]`（默认）| 至少包含两个元素的行向量

在 **Output current vector** 中指定的每个输出电流对应的效率向量，以百分比表示。此参数必须与 **Output current vector** 具有相同大小。

#### 依赖关系

要启用此参数，请将 **Implementation mode** 设置为 `Behavioral`，并将 **Converter efficiency** 设置为 `Tabulated`。

### **Inductance** — 电感 `1e-6` `H`（默认）| 正标量

*自 R2025a 起*

电感。

#### 依赖关系

要启用此参数，请将 **Implementation mode** 设置为 `Average value`。

### **Inductor series resistance** — 电感串联电阻 `0` `Ohm`（默认）| 非负标量

*自 R2025a 起*

电感的串联电阻。

#### 依赖关系

要启用此参数，请将 **Implementation mode** 设置为 `Average value`。

### **Capacitance** — 电容 `1e-7` `F`（默认）| 正标量

*自 R2025a 起*

电容。

#### 依赖关系

要启用此参数，请将 **Implementation mode** 设置为 `Average value`。

### **Capacitor effective series resistance** — 电容等效串联电阻 `1e-6` `Ohm`（默认）| 非负标量

*自 R2025a 起*

电容的串联电阻。

#### 依赖关系

要启用此参数，请将 **Implementation mode** 设置为 `Average value`。

## 所属库

Simscape / Electrical / Semiconductors & Converters / Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

### R2025a：支持双向功率流并对 LC 动态建模

Average-Value DC-DC Converter 模块现在支持双向功率流。您还可以对变换器 LC 动态建模。要对 LC 动态建模，请将 **Implementation mode** 参数设置为 `Average value`。此选项会公开 LC 参数，包括电感和电容。

## 描述

平均值 DC-DC 变换器

Average-Value DC-DC Converter 模块表示一个受控的平均值 DC-DC 变换器。您可以通过提供占空比，将该模块编程为 Buck 变换器、Boost 变换器或 Buck-Boost 变换器。该图显示了以占空比作为输入时该模块的等效电路。该变换器包含一个受控电流源和一个受控电压源。使用占空比、电流参考或电压参考端口作为控制输入，以在变换器两侧连接组件之间转换电能。

### 方程

如果将 **Control input** 参数设置为 `Duty cycle`，则输入电流和输出电压是占空比的函数，并且取决于变换器类型。

**电压和电流方程**

| 变换器类型 | 输出电压，v2 | 输入电流，i1 |
| --- | --- | --- |
| **Buck** | v2=DutyCycle⋅v1 | i1=DutyCycle⋅i2 |
| **Boost** | v2=v11−DutyCycle | i1=i21−DutyCycle |
| **Buck-Boost** | v2=DutyCycle⋅v11−DutyCycle | i1=DutyCycle⋅i21−DutyCycle |

如果将 **Control input** 参数设置为 `Current reference`，则变换器设置输出电流并计算电压。

类似地，如果将 **Control input** 参数设置为 `Voltage reference`，则变换器设置输出电压并计算电流。

### 变量

*自 R2025a 起*

要启用 **Initial Targets** 和 **Nominal Values** 部分，请将 **Implementation mode** 参数设置为 `Average value`。

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅为模块变量设置优先级和初始目标。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真稳健性。您可以使用不同来源指定标称值，包括模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅按标称值进行系统缩放。

### 限制和假设

- 输入电压为正。
- 所有变换器类型的输入和输出使用相同极性。
