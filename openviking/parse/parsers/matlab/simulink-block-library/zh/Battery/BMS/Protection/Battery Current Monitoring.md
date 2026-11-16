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

### 输入

### **PackCurrent** — 电池组电流，A 标量

电池组电流，以 ampere 为单位，指定为标量。

### **ChargingLimit** — 充电电流限值，A 标量

电池的充电电流限值，以 ampere 为单位，指定为标量。

### **DischargingLimit** — 放电电流限值，A 标量

电池的放电电流限值，以 ampere 为单位，指定为标量。

### 输出

### **OvercurrentError** — 过流错误指示 `0` | `1`

过流错误的指示。如果此输出等于 `1`，则电池处于过流状态。

## 参数

### **Current error limit (A)** — 电流误差限值 `0` (默认) | 非负标量

允许与充电和放电限值存在小偏差的阈值，以 ampere 为单位。

### **Qualification time (s)** — 错误确认时间 `2` (默认) | 正标量

确认错误所需的时间，以 seconds 为单位。

### **Disqualification time (s)** — 错误取消确认时间 `0` (默认) | 非负标量

取消确认错误所需的时间，以 seconds 为单位。如果将此参数设置为 `0`，则模块不会取消确认该错误。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1` (默认) | 0 | 正整数

连续模块执行之间的时间。在执行期间，模块生成输出，并在适当情况下更新其内部状态。有关详细信息，请参阅什么是采样时间？和指定采样时间。

对于继承的离散时间操作，请将此参数指定为 `-1`。对于离散时间操作，请将此参数指定为正整数。对于连续时间操作，请将此参数指定为 `0`。

如果此模块位于允许在连续操作和离散操作之间切换的封装子系统或变体子系统中，请提升采样时间参数。提升采样时间参数可确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅在封装上提升模块参数。

### **Algorithm data type** — 用于选择模块算法数据类型的选项 `Inherit: auto` (默认) | `double` | `single` | `<data type expression>`

*自 R2025a 起*

用于选择模块算法数据类型的选项，指定为下列值之一：

- `Inherit: auto` — 您可以以 `single` 和 `double` 精度对模块进行仿真。必须将输入和参数显式提供为 `single` 或 `double`。
- `double` — 模块算法将所有输入和参数转换为 `double` 数据类型。
- `single` — 模块算法将所有输入和参数转换为 `single` 数据类型。
- `<data type expression>` — 模块算法将所有输入和参数转换为指定的数据类型对象。

点击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用数据类型助手指定数据类型和控制信号的数据类型。

## 所属库

Simscape / Battery / BMS / Protection

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

### R2025a：使用 **Algorithm data type** 参数在单精度和双精度浮点仿真之间切换

现在，您可以使用 **Algorithm data type** 参数轻松地在模块算法的单精度和双精度浮点仿真之间切换。

## 描述

电池电流监测器

Battery Current Monitoring 模块实现电池过流监测。过流保护在电气电路中是必要的。暴露于过流的电池会经历电芯温度的显著升高，并处于危险的不稳定状态。

您可以使用 **Sample time (-1 for inherited)** 参数在模块的连续实现和离散实现之间切换。要将模块配置为连续时间，请将 **Sample time (-1 for inherited)** 参数设置为 `0`。要将模块配置为离散时间，请将 **Sample time (-1 for inherited)** 参数设置为正的非零值，或设置为 `-1` 以从上游模块继承采样时间。

下图显示了模块的结构：

### 方程

此模块使用以下方程计算过流症状：

Overcurrent Symptom=(i− Chargelimit)>ErrorLimit∥( DischargeLimit−i )>ErrorLimit.

Battery Current Monitoring 模块随后将过流症状传递到 Fault Qualification 模块，由该模块确认错误。
