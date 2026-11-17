---
type: simulink-block
title: 'Battery Temperature Monitoring'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'BMS / Protection'
documentation_page: 'batterytemperaturemonitoring'
documentation_source_path: 'ref/batterytemperaturemonitoring.html'
language: zh-CN
chinese_source: worker-translation
---

# Battery Temperature Monitoring

## 端口

### 输入

### **CellTemperature** — 电芯温度，K 标量 | 向量

电池电芯的温度，指定为单个电芯的标量或多个电芯的向量。

如果选择 **Specify input as [Min,Max]** 参数，则必须为此端口指定最小值和最大值，例如 `CellTemperature=[CellTemperatureMin,CellTemperatureMax]`。*（自 R2025a 起）*
### 输出

### **UndertemperatureError** — 欠温错误指示，无单位 `0` | `1`

欠温错误的指示。如果此输出等于 `1`，则电池处于欠温状态。

### **OvertemperatureError** — 过温错误指示，无单位 `0` | `1`

过温错误的指示。如果此输出等于 `1`，则电池处于过温状态。

## 参数

### **Specify input as [Min,Max]** — 将输入指定为最小值和最大值的选项 `off`（默认）| `on`

*自 R2025a 起*

将 **CellTemperature** 输入端口的值指定为最小值和最大值向量的选项。如果清除此参数，则必须为输入端口指定单个值。模块随后在内部计算最小值和最大值。

### **Undertemperature limit** — 欠温限值 `270`（默认）| 非负标量

电池处于欠温状态时的温度限值。

### **Overtemperature limit** — 过温限值 `320`（默认）| 非负标量

电池处于欠温状态时的温度限值。此参数的值必须大于 **Undertemperature limit** 参数的值。

### **Qualification time undertemperature (s)** — 欠温确认时间 `2`（默认）| 正标量

确认欠温错误所需的时间，以秒为单位。

### **Disqualification time undertemperature (s)** — 欠温解除时间 `0`（默认）| 非负标量

解除欠温错误所需的时间，以秒为单位。如果将此参数设置为 `0`，则模块不会解除该错误。

### **Qualification time overtemperature (s)** — 过温确认时间 `2`（默认）| 正标量

确认过温错误所需的时间，以秒为单位。

### **Disqualification time overtemperature (s)** — 过温解除时间 `0`（默认）| 非负标量

解除过温错误所需的时间，以秒为单位。如果将此参数设置为 `0`，则模块不会解除该错误。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| 0 | 正整数

连续模块执行之间的时间。
在执行期间，模块产生输出，并在适当情况下更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，请将此参数指定为 `-1`。对于离散时间操作，请将此参数指定为正整数。对于连续时间操作，请将此参数指定为 `0`。

如果此模块位于允许在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升采样时间参数。提升采样时间参数可确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

### **Algorithm data type** — 选择模块算法数据类型的选项 `Inherit: auto`（默认）| `double` | `single` | `<data type expression>`

*自 R2025a 起*

选择模块算法数据类型的选项，指定为以下值之一：

- `Inherit: auto` — 您可以以 `single` 和 `double` 精度仿真模块。您必须将输入和参数显式提供为 `single` 或 `double`。
- `double` — 模块算法将所有输入和参数转换为 `double` 数据类型。
- `single` — 模块算法将所有输入和参数转换为 `single` 数据类型。
- `<data type expression>` — 模块算法将所有输入和参数转换为指定的数据类型对象。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant 和 Control Data Types of Signals。

## 所属库

Simscape / Battery / BMS / Protection

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

### R2025a: 使用 **Algorithm data type** 参数在单精度和双精度浮点仿真之间切换

您现在可以使用 **Algorithm data type** 参数轻松地在模块算法的单精度和双精度浮点仿真之间切换。

### R2025a: 为 **Temperature** 输入端口指定最小值和最大值

您可以为 **CellTemperature** 输入端口指定最小值和最大值。要将此输入指定为最小值和最大值的向量，请选择 **Specify input as [Min,Max]** 参数。

## 描述

电池温度监测

Battery Temperature Monitoring 模块监测电池的温度。温度保护在电路中是必要的。暴露在极高或极低温度下的电池可能会进入危险的不稳定状态。

您可以使用 **Sample time (-1 for inherited)** 参数在模块的连续实现和离散实现之间切换。要将模块配置为连续时间，请将 **Sample time (-1 for inherited)** 参数设置为 `0`。要将模块配置为离散时间，请将 **Sample time (-1 for inherited)** 参数设置为正的非零值，或设置为 `-1` 以从上游模块继承采样时间。

此图说明了模块的整体结构：

### 方程

此模块使用以下方程计算欠温症状：

Undertemperature Symptom=min(Temperature)≤ UndertemperatureLimit

此模块使用以下方程计算过温症状：

Overtemperature Symptom=max(Temperature)≥ OvertemperatureLimit

Battery Temperature Monitoring 模块随后将欠温症状和过温症状传递给 Fault Qualification 模块，由该模块确认错误。
