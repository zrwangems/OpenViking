---
type: simulink-block
title: 'Battery (System-Level)'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'batterysystemlevel'
documentation_source_path: 'ref/batterysystemlevel.html'
language: zh-CN
chinese_source: worker-translation
---

# Battery (System-Level)

## 端口
```yaml
ports:
- name: +
  summary: 正极端子电气
  direction: conserving
- name: '-'
  summary: 负极端子电气
  direction: conserving
- name: H
  summary: 传热热
  direction: conserving
```

### 守恒端口

### **+** — 正极端子电气

与电池正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与电池负极端子关联的电气守恒端口。

### **H** — 传热热

与传热关联的热守恒端口。

#### 依赖关系

要显示此端口，请将 **Thermal port** 设置为
`Model`。
## 参数
```yaml
parameters:
- name: Nominal voltage, Vnom
  summary: 电池完全充电时的输出电压 12 V（默认）| 正标量
  group: 主
- name: Internal resistance
  summary: 电池内阻 2 Ohm（默认）| 正标量
  group: 主
- name: Battery charge capacity
  summary: 模拟放电的选项 Infinite（默认）| Finite
  group: 主
- name: Cell capacity (Ah rating)
  summary: 额定电池容量 50 A*hr（默认）| 正标量
  group: 主
- name: Voltage V1 when charge is AH1
  summary: 电荷水平为 AH1 时的输出电压 11.5 V（默认）| 正标量
  group: 主
- name: Charge AH1 when no-load voltage is V1
  summary: 空载输出电压为 V1 时的电荷水平 25 A*hr（默认）| 正标量
  group: 主
- name: Self-discharge
  summary: 模拟自放电电阻的选项 Disabled（默认）| Enabled
  group: 主
- name: Self-discharge resistance
  summary: 表示电池自放电的电阻 2000 Ohm（默认）| 正标量
  group: 主
- name: Thermal port
  summary: 模拟热效应的选项 Omit（默认）| Model
  group: 热端口
- name: Thermal mass
  summary: 电池的热质量 30000 J/K（默认）
  group: 热端口
```

### 主

### **Nominal voltage, Vnom** — 电池完全充电时的输出电压 `12` `V`（默认）| 正标量

电池完全充电时的空载电压。

### **Internal resistance** — 电池内阻 `2` `Ohm`（默认）| 正标量

电池的内部连接电阻。

### **Battery charge capacity** — 模拟放电的选项 `Infinite`（默认）| `Finite`

模拟有限或无限电池电荷容量的选项。

### **Cell capacity (Ah rating)** — 额定电池容量 `50` `A*hr`（默认）| 正标量

最大电池电荷。安培小时是指电池可以放电 1 安培的小时数。您可以将初始电荷目标指定为变量。

#### 依赖关系

要启用此参数，请将 **Battery charge
capacity** 设置为 `Finite`。

### **Voltage V1 when charge is AH1** — 电荷水平为 AH1 时的输出电压 `11.5` `V`（默认）| 正标量

当电荷水平等于 **Charge AH1 when no-load voltage is V1** 时的基本电池输出电压。

#### 依赖关系

要启用此参数，请将 **Battery charge
capacity** 设置为 `Finite`。

### **Charge AH1 when no-load voltage is V1** — 空载输出电压为 V1 时的电荷水平 `25` `A*hr`（默认）| 正标量

与您为 **Voltage V1 when charge is AH1**
参数指定的空载输出电压对应的电池电荷水平。

#### 依赖关系

要启用此参数，请将 **Battery charge
capacity** 设置为 `Finite`。

### **Self-discharge** — 模拟自放电电阻的选项 `Disabled`（默认）| `Enabled`

模拟自放电电阻的选项。该模块将此效应模拟为电池端子两端的电阻器。

#### 依赖关系

要启用此参数，请将 **Battery charge
capacity** 设置为 `Finite`。

### **Self-discharge resistance** — 表示电池自放电的电阻 `2000` `Ohm`（默认）| 正标量

电池端子两端表示自放电的电阻。

#### 依赖关系

要启用此参数，请将 **Battery charge
capacity** 设置为 `Finite`，并将
**Self-discharge** 设置为
`Enabled`。

### 热端口

### **Thermal port** — 模拟热效应的选项 `Omit`（默认）| `Model`

显示热端口并在模型中包含热效应的选项。

### **Thermal mass** — 电池的热质量 `30000` `J/K`（默认）

使组件温度变化一度所需的热能。热质量越大，组件对温度变化的抵抗能力越强。
## 所属库

Simscape / Driveline / Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

## 描述

通用系统级电池

Battery (System-Level) 模块表示一个通用自放电电池。您可以使用该模块以中等保真度对混合动力和纯电动驱动进行驱动循环分析建模。该模块是 Battery (Simscape Electrical) 模块的简化版本，并在适用的情况下使用相同的参数。这有助于您在必要时过渡到更高保真度的模型。Battery (System-Level) 不支持电池衰减、老化、动态特性或温度相关属性。您可以使用 Battery (Simscape Electrical) 模块访问这些功能。

您可以选择模拟具有有限或无限电荷的电池。该模块还可以帮助您确定电压降低如何影响性能和控制要求。要了解有关观察电池性能的更多信息，请参阅 Plot Basic Voltage-Charge Characteristics of Battery Blocks (Simscape Electrical)。

### 电池模型

当您将 **Battery charge capacity** 设置为
`Infinite` 时，该模块将电池视为串联的电阻器和恒定电压源。当您将 **Battery
charge capacity** 设置为 `Finite` 时，该模块将电池视为串联的电阻器和电荷相关电压源。
在这种情况下，电压是电荷的函数，并具有以下关系：

V=V0SOC1−β(1−SOC)

其中：

- `SOC`（荷电状态）是当前电荷与额定电池容量的比率。
- *V*0 是电池在空载下完全充电时的电压，由 **Nominal
  voltage, Vnom** 参数定义。
- *β* 是一个常数，其计算使得当电荷为
  *AH1* 时电池电压为 *V1*。使用模块参数指定电压 *V1*
  和安培小时额定值 *AH1*。
  *AH1* 是空载（开路）电压为 *V1* 时的电荷，且 *V1* 小于
  额定电压。

该方程定义了电压与剩余电荷之间的近似关系。此近似再现了低电荷值时电压下降速率的增加，并确保当电荷水平为零时电池电压变为零。该模型的优点是它需要很少的参数，这些参数通常可在制造商数据表中获得。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同的来源，其中之一是模块对话框或属性检查器中的 **Nominal
Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。

### 假设和限制

该模块假设自放电电阻不依赖于放电循环次数。
