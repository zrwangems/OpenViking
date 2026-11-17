---
type: simulink-block
title: 'Battery Current Monitoring'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'BMS / Protection'
documentation_page: 'batterycurrentmonitoring'
documentation_source_path: 'ref/batterycurrentmonitoring.html'
language: zh-CN
chinese_source: worker-translation
---

# Battery Current Monitoring

## 端口
```yaml
ports:
- name: PackCurrent
  summary: 电池组电流，A 标量
  direction: input
- name: ChargingLimit
  summary: 充电电流限值，A 标量
  direction: input
- name: DischargingLimit
  summary: 放电电流限值，A 标量
  direction: input
- name: OvercurrentError
  summary: 过流错误指示 0 | 1
  direction: output
```

### 输入

### **PackCurrent** — 电池组电流，A 标量

电池组电流，单位为安培，指定为标量。

### **ChargingLimit** — 充电电流限值，A 标量

电池的充电电流限值，单位为安培，指定为标量。

### **DischargingLimit** — 放电电流限值，A 标量

电池的放电电流限值，单位为安培，指定为标量。

### 输出

### **OvercurrentError** — 过流错误指示 `0` | `1`

过流错误的指示。如果此输出等于 `1`，则电池处于过流状态。
## 参数
```yaml
parameters:
- name: Current error limit (A)
  summary: 电流误差限值 0（默认值）| 非负标量
  group: ''
- name: Qualification time (s)
  summary: 错误确认时间 2（默认值）| 正标量
  group: ''
- name: Disqualification time (s)
  summary: 错误取消确认时间 0（默认值）| 非负标量
  group: ''
- name: Sample time (-1 for inherited)
  summary: 模块采样时间 -1（默认值）| 0 | 正整数
  group: ''
- name: Algorithm data type
  summary: '选择模块算法数据类型的选项 Inherit: auto（默认值）| double | single | <data type expression>'
  group: ''
```

### **Current error limit (A)** — 电流误差限值 `0`（默认值）| 非负标量

允许与充电和放电限值存在微小偏差的阈值，单位为安培。

### **Qualification time (s)** — 错误确认时间 `2`（默认值）| 正标量

确认错误所需的时间，单位为秒。

### **Disqualification time (s)** — 错误取消确认时间 `0`（默认值）| 非负标量

取消确认错误所需的时间，单位为秒。如果将此参数设置为 `0`，则该模块不会取消确认错误。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认值）| 0 | 正整数

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当的情况下更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，请将此参数指定为 `-1`。对于离散时间操作，请将此参数指定为正整数。对于连续时间操作，请将此参数指定为 `0`。

如果此模块位于允许在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升采样时间参数。提升采样时间参数可确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

### **Algorithm data type** — 选择模块算法数据类型的选项 `Inherit: auto`（默认值）| `double` | `single` | `<data type expression>`

*自 R2025a 起*

选择模块算法数据类型的选项，指定为以下值之一：

- `Inherit: auto` — 您可以以 `single` 和 `double` 精度仿真该模块。您必须将输入和参数显式提供为 `single` 或 `double`。
- `double` — 模块算法将所有输入和参数转换为 `double` 数据类型。
- `single` — 模块算法将所有输入和参数转换为 `single` 数据类型。
- `<data type expression>` — 模块算法将所有输入和参数转换为您指定的数据类型对象。

单击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant 和 Control Data Types of Signals。
## 所属库

Simscape / Battery / BMS / Protection

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

### R2025a：使用 **Algorithm data type** 参数在单精度和双精度浮点仿真之间切换

您现在可以使用 **Algorithm data type** 参数轻松地在模块算法的单精度和双精度浮点仿真之间切换。

## 描述

电池电流监测

电池电流监测模块实现电池过流监测。过流保护在电路中是必要的。暴露于过流的电池会经历电芯温度显著升高，并处于危险的不稳定状态。

您可以通过使用 **Sample time (-1 for inherited)** 参数在模块的连续实现和离散实现之间切换。要将模块配置为连续时间，请将 **Sample time (-1 for inherited)** 参数设置为 `0`。要将模块配置为离散时间，请将 **Sample time (-1 for inherited)** 参数设置为正的非零值，或设置为 `-1` 以从上游模块继承采样时间。

此图显示了该模块的结构：

### 方程

该模块使用以下方程计算过流症状：

Overcurrent Symptom=(i− Chargelimit)>ErrorLimit∥( DischargeLimit−i )>ErrorLimit。

然后，电池电流监测模块将过流症状传递给故障鉴定模块，由该模块对错误进行鉴定。
