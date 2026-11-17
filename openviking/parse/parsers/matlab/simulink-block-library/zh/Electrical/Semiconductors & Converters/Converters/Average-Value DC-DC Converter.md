---
type: simulink-block
title: 'Average-Value DC-DC Converter'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'averagevaluedcdcconverter'
documentation_source_path: 'ref/averagevaluedcdcconverter.html'
language: zh-CN
chinese_source: worker-translation
---

# Average-Value DC-DC Converter

## 端口
```yaml
ports:
- name: DutyCycle
  summary: 占空比物理信号 | 标量
  direction: conserving
  data_types: double
- name: Iref
  summary: 电流参考物理信号
  direction: conserving
  data_types: double
- name: Vref
  summary: 电压参考物理信号
  direction: conserving
  data_types: double
- name: 1+
  summary: 正直流电压 1 电气端口 | 标量
  direction: conserving
  data_types: double
- name: 1-
  summary: 负直流电压 1 电气端口 | 标量
  direction: conserving
  data_types: double
- name: 2+
  summary: 正直流电压 2 电气端口 | 标量
  direction: conserving
  data_types: double
- name: 2-
  summary: 负直流电压 2 电气端口 | 标量
  direction: conserving
  data_types: double
```

### 守恒端口

### **DutyCycle** — 占空比物理信号 | 标量

与占空比关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Control Input** 设置为 `Duty
Cycle`。

**数据类型：** `double`

### **Iref** — 电流参考物理信号

与电流参考关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Control Input** 设置为 `Current
reference`。

**数据类型：** `double`

### **Vref** — 电压参考物理信号

与电压参考关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Control Input** 设置为 `Voltage
reference`。

**数据类型：** `double`

### **1+** — 正直流电压 1 电气端口 | 标量

与第一个直流电压正极端子关联的电气守恒端口。

**数据类型：** `double`

### **1-** — 负直流电压 1 电气端口 | 标量

与第一个直流电压负极端子关联的电气守恒端口。

**数据类型：** `double`

### **2+** — 正直流电压 2 电气端口 | 标量

与第二个直流电压正极端子关联的电气守恒端口。

**数据类型：** `double`

### **2-** — 负直流电压 2 电气端口 | 标量

与第二个直流电压负极端子关联的电气守恒端口。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Implementation mode
  summary: 变换器实现模式 Behavioral（默认）| Average value
  group: ''
- name: Converter type
  summary: 变换器类型 Buck converter（默认）| Buck-boost converter | Boost converter
  group: ''
- name: Control input
  summary: 控制输入 Duty cycle（默认）| Current reference | Voltage reference
  group: ''
- name: Converter efficiency
  summary: 变换器效率参数化 Constant（默认）| Tabulated
  group: ''
- name: Efficiency (%)
  summary: 变换器效率 100（默认）| 正标量
  group: ''
- name: Output current vector
  summary: 输出电流向量 [0, 2, 5] A（默认）| 至少包含两个元素的行向量
  group: ''
- name: Efficiency vector (%)
  summary: 效率向量 [90, 95, 98]（默认）| 至少包含两个元素的行向量
  group: ''
- name: Inductance
  summary: 电感 1e-6 H（默认）| 正标量
  group: ''
- name: Inductor series resistance
  summary: 电感串联电阻 0 Ohm（默认）| 非负标量
  group: ''
- name: Capacitance
  summary: 电容 1e-7 F（默认）| 正标量
  group: ''
- name: Capacitor effective series resistance
  summary: 电容串联电阻 1e-6 Ohm（默认）| 非负标量
  group: ''
```

### **Implementation mode** — 变换器实现模式 `Behavioral`（默认）| `Average value`

*自 R2025a 起*

用于指定变换器实现模式的选项。要控制逆变器状态变量，请将此参数设置为 `Average
value`。要进行无动态特性的快速仿真，请将此参数设置为 `Behavioral`。

### **Converter type** — 变换器类型 `Buck converter`（默认）| `Buck-boost converter` | `Boost converter`

变换器的类型。

#### 依赖关系

要启用此参数，请将 **Control Input** 设置为
`Duty Cycle`，或将 **Implementation
mode** 设置为 `Average value`。

### **Control input** — 控制输入 `Duty cycle`（默认）| `Current reference` | `Voltage reference`

指定用于在两侧之间转换电能的控制输入。

#### 依赖关系

要启用此参数，请将 **Implementation mode**
设置为 `Behavioral`。

### **Converter efficiency** — 变换器效率参数化 `Constant`（默认）| `Tabulated`

指定变换器效率的参数化方式。如果选择
`Tabulated`，导通损耗取决于所提供的输出电流。

**注意**

对于表格化效率，外推方法为最近邻。
因此，效率不会高于 **Efficiency vector (%)**
参数中的最高值，也不会低于最低值。

#### 依赖关系

要启用此参数，请将 **Implementation mode**
设置为 `Behavioral`。

### **Efficiency (%)** — 变换器效率 `100`（默认）| 正标量

变换器的效率，以百分比表示。

#### 依赖关系

要启用此参数，请将 **Implementation mode** 设置为
`Behavioral`，并将 **Converter
efficiency** 设置为 `Constant`。

### **Output current vector** — 输出电流向量 `[0, 2, 5]` `A`（默认）| 至少包含两个元素的行向量

输出电流向量。

#### 依赖关系

要启用此参数，请将 **Implementation mode** 设置为
`Behavioral`，并将 **Converter
efficiency** 设置为
`Tabulated`。

### **Efficiency vector (%)** — 效率向量 `[90, 95, 98]`（默认）| 至少包含两个元素的行向量

**Output current vector** 中指定的每个输出电流对应的效率向量，以百分比表示。此
参数的大小必须与 **Output current
vector** 相同。

#### 依赖关系

要启用此参数，请将 **Implementation mode** 设置为
`Behavioral`，并将 **Converter
efficiency** 设置为
`Tabulated`。

### **Inductance** — 电感 `1e-6` `H`（默认）| 正标量

*自 R2025a 起*

电感。

#### 依赖关系

要启用此参数，请将 **Implementation mode**
设置为 `Average value`。

### **Inductor series resistance** — 电感串联电阻 `0` `Ohm`（默认）| 非负标量

*自 R2025a 起*

电感的串联电阻。

#### 依赖关系

要启用此参数，请将 **Implementation mode**
设置为 `Average value`。

### **Capacitance** — 电容 `1e-7` `F`（默认）| 正标量

*自 R2025a 起*

电容。

#### 依赖关系

要启用此参数，请将 **Implementation mode**
设置为 `Average value`。

### **Capacitor effective series resistance** — 电容串联电阻 `1e-6` `Ohm`（默认）| 非负标量

*自 R2025a 起*

电容的串联电阻。

#### 依赖关系

要启用此参数，请将 **Implementation mode**
设置为 `Average value`。
## 所属库

Simscape / Electrical / Semiconductors & Converters / Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

### R2025a：支持双向功率流动并对 LC 动态特性建模

Average-Value DC-DC Converter 模块现在支持双向功率流动。您还可以对
变换器 LC 动态特性建模。要对 LC 动态特性建模，请将 **Implementation
mode** 参数设置为 `Average value`。此
选项会公开 LC 参数，包括电感和
电容。

## 描述

平均值 DC-DC 变换器

Average-Value DC-DC Converter 模块表示一个
受控的平均值 DC-DC 变换器。您可以通过提供占空比将该模块编程为 buck 变换器、
boost 变换器或 buck-boost 变换器。该图显示了
以占空比作为输入的模块等效电路。该变换器包含一个
受控电流源和一个受控电压源。使用占空比、
电流参考或电压参考端口作为控制输入，以在变换器两侧所连接组件之间转换
电能。

### 方程

如果将 **Control input** 参数设置为 `Duty
cycle`，则输入电流和输出电压是
占空比的函数，并取决于变换器类型。

**电压和电流方程**

| 变换器类型 | 输出电压，v2 | 输入电流，i1 |
| --- | --- | --- |
| **Buck** | v2=DutyCycle⋅v1 | i1=DutyCycle⋅i2 |
| **Boost** | v2=v11−DutyCycle | i1=i21−DutyCycle |
| **Buck-Boost** | v2=DutyCycle⋅v11−DutyCycle | i1=DutyCycle⋅i21−DutyCycle |

如果将 **Control input** 参数设置为 `Current
reference`，则变换器设置输出电流并计算
电压。

类似地，如果将 **Control input** 参数设置为
`Voltage reference`，则变换器设置输出
电压并计算电流。

### 变量

*自 R2025a 起*

要启用 **Initial Targets** 和 **Nominal
Values** 部分，请将 **Implementation mode**
参数设置为 `Average value`。

要在仿真前设置模块变量的优先级和初始目标值，
请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期幅值的方法。使用
基于标称值的系统缩放可提高仿真
鲁棒性。您可以使用不同来源指定标称值，包括
模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。

### 限制和假设

- 输入电压为正。
- 所有变换器类型的输入和输出使用相同极性。
