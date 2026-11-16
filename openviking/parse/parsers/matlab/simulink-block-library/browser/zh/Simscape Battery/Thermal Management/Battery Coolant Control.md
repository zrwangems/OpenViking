---
type: simulink-block
title: 'Battery Coolant Control'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Thermal Management'
documentation_page: 'batterycoolantcontrol'
documentation_source_path: 'ref/batterycoolantcontrol.html'
language: zh-CN
chinese_source: worker-translation
---

# Battery Coolant Control

## 端口

### 输入

### **CellTemperature** — 电芯温度，K 标量 | 向量

电池单体的温度，指定为单个电芯的标量或用于多个电芯的向量。

如果选择 **Specify CellTemperature input as [Min,Max]** 参数，则必须为此端口指定最小值和最大值，例如 `CellTemperature=[CellTemperatureMin,CellTemperatureMax]`。*（自 R2025a 起）*

### **AmbientTemperature** — 环境温度，K 标量

环境的温度，指定为标量。

### **CoolantTemperature** — 冷却液温度，K 标量

冷却液的温度，指定为标量。

### 输出

### **FlowRateCommand** — 流量指令，标量

流量指令，返回为 [0, 1] 范围内的标量。此输出表示相对于最大和最小流量值的流量。值 0 对应于最小流量。值 1 对应于最大流量。

### **FlowTemperature** — 流动温度，标量

流动温度，返回为正或负标量。冷却液总入口温度等于此值与 **AmbientTemperature** 输入端口处的值之和。

## 参数

### **Specify CellTemperature input as [Min,Max]** — 将 CellTemperature 输入指定为最小值和最大值的选项 `off`（默认）| `on`

*自 R2025a 起*

用于将 **CellTemperature** 输入端口处的值指定为最小值和最大值向量的选项。如果清除此参数，则必须为 **CellTemperature** 输入端口指定单个值。模块随后会在内部计算最小值和最大值。

### **Control strategy** — 控制策略 `ON-OFF control`（默认）| `Step control`

用于计算流量指令的控制策略。

### **Switch-on temperature** — 冷却液开启温度 `305.15`（默认）| 正标量

冷却液泵开启时的温度。此参数的值必须大于或等于 **Switch-off temperature** 参数的值。

#### 依赖关系

要启用此参数，请将 **Control strategy** 设置为 `ON-OFF control`。

### **Switch-off temperature** — 冷却液关闭温度 `301.15`（默认）| 正标量

冷却液泵关闭时的温度。

#### 依赖关系

要启用此参数，请将 **Control strategy** 设置为 `ON-OFF control`。

### **Constant used in f(deltaT)=c\*deltaT** — 冷却策略的常数 `0.1`（默认）| 正标量

控制冷却策略激进程度的常数。

#### 依赖关系

要启用此参数，请将 **Control strategy** 设置为 `Step control`。

### **Flow rate step** — 流量步长 `0.2`（默认）| 正标量

用于计算流量指令的步长值。此参数的值必须小于或等于 `1`。

#### 依赖关系

要启用此参数，请将 **Control strategy** 设置为 `Step control`。

### **Algorithm data type** — 为模块算法选择数据类型的选项 `Inherit: auto`（默认）| `double` | `single` | `<data type expression>`

*自 R2025a 起*

用于为模块算法选择数据类型的选项，指定为以下值之一：

- `Inherit: auto` — 您可以以 `single` 和 `double` 精度仿真模块。您必须将输入和参数显式提供为 `single` 或 `double`。
- `double` — 模块算法将所有输入和参数转换为 `double` 数据类型。
- `single` — 模块算法将所有输入和参数转换为 `single` 数据类型。
- `<data type expression>` — 模块算法将所有输入和参数转换为您指定的数据类型对象。

单击 **Show data type assistant** 按钮  以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant 和 Control Data Types of Signals。

## 所属库

Simscape / Battery / BMS / Thermal Management

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

### R2025a：使用 **Algorithm data type** 参数在单精度和双精度浮点仿真之间切换

现在，您可以使用 **Algorithm data type** 参数轻松地在模块算法的单精度和双精度浮点仿真之间切换。

### R2025a：为 **CellTemperature** 输入端口指定最小值和最大值

您可以为 **CellTemperature** 输入端口指定最小值和最大值。要将此输入指定为最小值和最大值的向量，请选择 **Specify CellTemperature input as [Min,Max]** 参数。

## 描述

电池冷却液控制算法

Battery Coolant Control 模块实现电池冷却液控制算法。

温度对电池至关重要，因为高温会显著缩短电池寿命。重要的是控制电池每个电芯的温度，并激活加热器或冷却器以将温度保持在安全范围内。如果温度过高，电池管理系统 (BMS) 会启用冷却风扇。

此模块支持单精度和双精度浮点仿真。

**注意**

要启用单精度浮点仿真，所有输入和参数的数据类型必须为 `single`。

此图显示模块的结构：

### 方程

Battery Coolant Control 模块使用以下方程计算流动温度：

FlowTemperature=Tamb−Tcool

其中 *Tamb* 是环境温度，*Tcool* 是冷却液温度。

如果 **FlowRateCommand** 输出端口处的值等于 `0`，则电池中没有流动。如果此值等于 `1`，则电池中的流量达到其最高可能值。

如果将 **Control strategy** 参数设置为 `ON-OFF control`，则模块使用以下方程计算流量指令：

FlowRateCommand={1,Thottest≥TonFlowRateCommandold,Toff<Thottest<Ton0,Thottest<Toff

其中

- *Thottest* 是最热电芯的温度。
- *Ton* 是开启温度。
- *Toff* 是关闭温度，其必须小于 Ton。
- *FlowRateCommandold* 是上一时间步的流量指令。

如果将 **Control strategy** 参数设置为 `Step control`，则模块使用以下方程计算流量指令：

f(ΔT)=c(Thottest−min(Tcoolest,Tamb−Tcool))FlowRateCommand=min(f(ΔT)−mod(f(ΔT),step),1)

其中

- *Tcoolest* 是最冷电芯的温度。
- *step* 是流量步长指令。例如，如果 *step = 0.2*，则 **FlowRateCommand** 输出端口处的值是以下值之一：[0,0.2,0.4,0.6,0.8,1]。
- *c* 控制冷却策略的激进程度。此值是一个常数，使得如果 *f(ΔT)≥ 1*，则 **FlowRateCommand** 输出端口处的值等于 1。否则，模块将流量指令线性缩放至 `0`。

步进控制策略允许使用您为 **Flow rate step** 参数指定的值作为中间流量指令。为计算实际指令，模块使用温度梯度的函数。
