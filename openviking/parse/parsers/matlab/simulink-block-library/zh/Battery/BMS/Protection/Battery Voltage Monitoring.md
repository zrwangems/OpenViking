---
type: simulink-block
title: 'Battery Voltage Monitoring'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'BMS / Protection'
documentation_page: 'batteryvoltagemonitoring'
documentation_source_path: 'ref/batteryvoltagemonitoring.html'
language: zh-CN
chinese_source: worker-translation
---

# Battery Voltage Monitoring

## 端口
```yaml
ports:
- name: CellVoltage
  summary: 电芯电压，V 标量 | 向量
  direction: input
- name: PackVoltage
  summary: 电池包电压，V 标量
  direction: input
- name: UndervoltageError
  summary: 欠压错误指示 0 | 1
  direction: output
- name: OvervoltageError
  summary: 过压错误指示 0 | 1
  direction: output
- name: SensoryFaultyError
  summary: 传感器故障错误指示 0 | 1
  direction: output
```

### 输入

### **CellVoltage** — 电芯电压，V 标量 | 向量

电芯电压，单位为伏特，指定为单个电芯的标量或多个电芯的向量。

### **PackVoltage** — 电池包电压，V 标量

电池包电压，单位为伏特，指定为标量。
### 输出

### **UndervoltageError** — 欠压错误指示 `0` | `1`

欠压错误指示。如果此输出等于
`1`，则电池处于欠压
状态。

### **OvervoltageError** — 过压错误指示 `0` | `1`

过压错误指示。如果此输出等于
`1`，则电池处于过压状态。

### **SensoryFaultyError** — 传感器故障错误指示 `0` | `1`

传感器故障错误指示。如果此输出等于
`1`，则传感器发生故障。
## 参数
```yaml
parameters:
- name: Undervoltage limit (V)
  summary: 欠压限值 2.5（默认值）| 正标量
  group: ''
- name: Overvoltage limit (V)
  summary: 过压限值 4.5（默认值）| 正标量
  group: ''
- name: Voltage sensor fault threshold (V)
  summary: 电压传感器故障阈值 0.25（默认值）| 正标量
  group: ''
- name: Qualification time undervoltage (s)
  summary: 欠压确认时间 2（默认值）| 正标量
  group: ''
- name: Disqualification time undervoltage (s)
  summary: 欠压取消确认时间 0（默认值）| 非负标量
  group: ''
- name: Qualification time overvoltage (s)
  summary: 过压确认时间 2（默认值）| 正标量
  group: ''
- name: Disqualification time overvoltage (s)
  summary: 过压取消确认时间 0（默认值）| 非负标量
  group: ''
- name: Qualification time faulty sensor (s)
  summary: 故障传感器确认时间 2（默认值）| 正标量
  group: ''
- name: Disqualification time faulty sensor (s)
  summary: 故障传感器取消确认时间 0（默认值）| 非负标量
  group: ''
- name: Sample time (-1 for inherited)
  summary: 模块采样时间 -1（默认值）| 0 | 正整数
  group: ''
- name: Algorithm data type
  summary: '选择模块算法数据类型的选项 Inherit: auto（默认值）| double | single | <data type expression>'
  group: ''
```

### **Undervoltage limit (V)** — 欠压限值 `2.5`（默认值）| 正标量

电池处于欠压状态的电压限值，单位为伏特。

### **Overvoltage limit (V)** — 过压限值 `4.5`（默认值）| 正标量

电池处于过压状态的电压限值，单位为伏特。此参数的值必须大于 **Undervoltage
limit (V)** 参数的值。

### **Voltage sensor fault threshold (V)** — 电压传感器故障阈值 `0.25`（默认值）| 正标量

传感器发生故障的电压阈值，单位为伏特。

### **Qualification time undervoltage (s)** — 欠压确认时间 `2`（默认值）| 正标量

确认欠压错误所需的时间，单位为秒。

### **Disqualification time undervoltage (s)** — 欠压取消确认时间 `0`（默认值）| 非负标量

取消确认欠压错误所需的时间，单位为秒。如果将此参数设置为
`0`，则模块不会取消确认该
错误。

### **Qualification time overvoltage (s)** — 过压确认时间 `2`（默认值）| 正标量

确认过压错误所需的时间，单位为秒。

### **Disqualification time overvoltage (s)** — 过压取消确认时间 `0`（默认值）| 非负标量

取消确认过压错误所需的时间，单位为秒。如果将此参数设置为
`0`，则模块不会取消确认该
错误。

### **Qualification time faulty sensor (s)** — 故障传感器确认时间 `2`（默认值）| 正标量

确认故障传感器错误所需的时间，单位为秒。

### **Disqualification time faulty sensor (s)** — 故障传感器取消确认时间 `0`（默认值）| 非负标量

取消确认故障传感器错误所需的时间，单位为秒。如果将此参数设置为
`0`，则模块不会取消确认
该错误。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认值）| 0 | 正整数

连续模块执行之间的时间。
在执行期间，模块产生输出，并在适当的情况下更新
其内部状态。有关详细信息，请参阅 What Is Sample Time? 和
Specify Sample Time。

对于继承的离散时间操作，请将此参数指定为
`-1`。对于离散时间操作，请将此
参数指定为正整数。对于连续时间操作，请将此参数指定为 `0`。

如果此模块位于允许在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升
采样时间参数。提升采样时间参数可确保在模块的连续实现和离散实现之间正确切换。
有关详细信息，请参阅 Promote Block Parameters on a Mask。

### **Algorithm data type** — 选择模块算法数据类型的选项 `Inherit: auto`（默认值）| `double` | `single` | `<data type expression>`

*自 R2025a 起*

选择模块算法数据类型的选项，指定为以下值之一：

- `Inherit: auto` — 您可以在
  `single` 和 `double`
  精度下仿真该模块。您必须将输入和参数显式提供为
  `single` 或
  `double`。
- `double` — 模块算法将所有输入
  和参数转换为 `double` 数据类型。
- `single` — 模块算法将所有输入
  和参数转换为 `single` 数据类型。
- `<data type expression>` — 模块
  算法将所有输入和参数转换为您指定的数据类型对象。

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

## 描述

电池电压监测

Battery Voltage Monitoring 模块监测电池的电压。
电压保护在电路中是必要的。暴露在极高或极低电压下的电池可能会进入危险的不稳定状态。

您可以使用 **Sample time (-1 for inherited)** 参数在模块的连续实现和离散实现之间切换。要将
模块配置为连续时间，请将 **Sample time (-1 for
inherited)** 参数设置为 `0`。要将模块配置为
离散时间，请将 **Sample time (-1 for inherited)**
参数设置为正的非零值，或设置为 `-1` 以从上游模块继承
采样时间。

此图显示了该模块的结构：

### 方程

此模块使用以下方程计算欠压症状：

Undervoltage Symptom=min(CellVoltage)≤ UndervoltageLimit

此模块使用以下方程计算过压症状：

Overvoltage Symptom=max(CellVoltage)≥ OvervoltageLimit

此模块使用以下方程计算故障传感器症状：

FaultySensor Symptom=|PackVoltage−∑i−1nCellVoltagei|≥ FaultySensorThreshold

对电芯电压之和的检查假设所有电芯均为串联。

然后，Battery Voltage Monitoring 模块将这些症状传递给 Fault
Qualification 模块，由该模块确认错误。
