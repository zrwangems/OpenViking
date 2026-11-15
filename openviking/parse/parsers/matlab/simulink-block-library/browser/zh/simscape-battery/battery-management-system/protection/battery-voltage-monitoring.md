---
type: simulink-block
title: 'Battery Voltage Monitoring'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Battery Management System / Protection\u200b'
documentation_page: 'batteryvoltagemonitoring'
documentation_source_path: 'ref/batteryvoltagemonitoring.html'
language: zh-CN
chinese_source: worker-translation
---

# Battery Voltage Monitoring

## 端口

### 输入

### **CellVoltage** — 电芯电压，V 标量 | 向量

电芯电压，单位为 volt，对于单个电芯指定为标量，对于多个电芯指定为向量。

### **PackVoltage** — 电池包电压，V 标量

电池包电压，单位为 volt，指定为标量。
### 输出

### **UndervoltageError** — 欠压错误指示 `0` | `1`

欠压错误指示。如果此输出等于 `1`，则电池处于欠压状态。

### **OvervoltageError** — 过压错误指示 `0` | `1`

过压错误指示。如果此输出等于 `1`，则电池处于过压状态。

### **SensoryFaultyError** — 传感器故障错误指示 `0` | `1`

传感器故障错误指示。如果此输出等于 `1`，则传感器发生故障。

## 参数

### **欠压限值 (V)** — 欠压限值 `2.5`（默认）| 正标量

电池处于欠压状态时的电压限值，单位为 volt。

### **过压限值 (V)** — 过压限值 `4.5`（默认）| 正标量

电池处于过压状态时的电压限值，单位为 volt。此参数的值必须大于 **欠压限值 (V)** 参数的值。

### **电压传感器故障阈值 (V)** — 电压传感器故障阈值 `0.25`（默认）| 正标量

传感器发生故障时的电压阈值，单位为 volt。

### **欠压确认时间 (s)** — 欠压确认时间 `2`（默认）| 正标量

确认欠压错误所需的时间，单位为 seconds。

### **欠压取消确认时间 (s)** — 欠压取消确认时间 `0`（默认）| 非负标量

取消确认欠压错误所需的时间，单位为 seconds。如果将此参数设置为 `0`，则模块不会取消确认该错误。

### **过压确认时间 (s)** — 过压确认时间 `2`（默认）| 正标量

确认过压错误所需的时间，单位为 seconds。

### **过压取消确认时间 (s)** — 过压取消确认时间 `0`（默认）| 非负标量

取消确认过压错误所需的时间，单位为 seconds。如果将此参数设置为 `0`，则模块不会取消确认该错误。

### **传感器故障确认时间 (s)** — 传感器故障确认时间 `2`（默认）| 正标量

确认传感器故障错误所需的时间，单位为 seconds。

### **传感器故障取消确认时间 (s)** — 传感器故障取消确认时间 `0`（默认）| 非负标量

取消确认传感器故障错误所需的时间，单位为 seconds。如果将此参数设置为 `0`，则模块不会取消确认该错误。

### **采样时间（-1 表示继承）** — 模块采样时间 `-1`（默认）| 0 | 正整数

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅什么是采样时间？和指定采样时间。

对于继承的离散时间操作，将此参数指定为 `-1`。对于离散时间操作，将此参数指定为正整数。对于连续时间操作，将此参数指定为 `0`。

如果此模块位于允许在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升采样时间参数。提升采样时间参数可确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅在掩码上提升模块参数。

### **算法数据类型** — 用于选择模块算法数据类型的选项 `Inherit: auto`（默认）| `double` | `single` | `<data type expression>`

*自 R2025a 起*

用于选择模块算法数据类型的选项，指定为以下值之一：

- `Inherit: auto` — 您可以在 `single` 和 `double` 精度下仿真模块。必须将输入和参数显式提供为 `single` 或 `double`。
- `double` — 模块算法将所有输入和参数转换为 `double` 数据类型。
- `single` — 模块算法将所有输入和参数转换为 `single` 数据类型。
- `<data type expression>` — 模块算法将所有输入和参数转换为指定的数据类型对象。

点击 **显示数据类型助手** 按钮  以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用数据类型助手指定数据类型和控制信号的数据类型。

## 所属库

Simscape / Battery / BMS / Protection

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

### R2025a: 使用 **算法数据类型** 参数在单精度和双精度浮点仿真之间切换

现在，您可以使用 **算法数据类型** 参数轻松地在模块算法的单精度和双精度浮点仿真之间切换。

## 描述

电池电压监测

Battery Voltage Monitoring 模块监测电池的电压。电压保护在电路中是必要的。暴露在极高或极低电压下的电池可能进入危险的不稳定状态。

您可以使用 **采样时间（-1 表示继承）** 参数在模块的连续实现和离散实现之间切换。要将模块配置为连续时间，请将 **采样时间（-1 表示继承）** 参数设置为 `0`。要将模块配置为离散时间，请将 **采样时间（-1 表示继承）** 参数设置为正的非零值，或设置为 `-1` 以从上游模块继承采样时间。

此图显示模块的结构：

### 方程

此模块使用以下方程计算欠压症状：

欠压症状=min(CellVoltage)≤ UndervoltageLimit

此模块使用以下方程计算过压症状：

过压症状=max(CellVoltage)≥ OvervoltageLimit

此模块使用以下方程计算故障传感器症状：

故障传感器症状=|PackVoltage−∑i−1nCellVoltagei|≥ FaultySensorThreshold

对电芯电压之和的检查假设所有电芯均串联。

Battery Voltage Monitoring 模块随后将这些症状传递给 Fault Qualification 模块，由该模块确认错误。
