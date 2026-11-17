---
type: simulink-block
title: 'Battery Heater Control'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'BMS / Thermal Management'
documentation_page: 'batteryheatercontrol'
documentation_source_path: 'ref/batteryheatercontrol.html'
language: zh-CN
chinese_source: worker-translation
---

# Battery Heater Control

## 端口
```yaml
ports:
- name: AmbientTemperature
  summary: 环境温度标量
  direction: input
- name: CoolantTemperature
  summary: 冷却液温度标量
  direction: input
- name: Command
  summary: 加热器命令标量
  direction: output
```

### 输入

### **AmbientTemperature** — 环境温度标量

环境的温度，指定为标量。

### **CoolantTemperature** — 冷却液温度标量

冷却液的温度，指定为标量。
### 输出

### **Command** — 加热器命令标量

加热器命令，以标量形式返回。如果该值等于 `0`，
则加热器关闭。如果该值等于 `1`，
则加热器开启。
## 参数
```yaml
parameters:
- name: Ambient temperature threshold for heater
  summary: 加热器的环境温度阈值 278.15（默认）| 正标量
  group: ''
- name: Switch-on coolant temperature
  summary: 开启冷却液温度 278.15（默认）| 正标量
  group: ''
- name: Switch-off coolant temperature
  summary: 关闭冷却液温度 290.15（默认）| 正标量
  group: ''
- name: Algorithm data type
  summary: '用于选择模块算法数据类型的选项 Inherit: auto（默认）| double | single | <data type expression>'
  group: ''
```

### **Ambient temperature threshold for heater** — 加热器的环境温度阈值 `278.15`（默认）| 正标量

模块激活加热器时的环境温度。

### **Switch-on coolant temperature** — 开启冷却液温度 `278.15`（默认）| 正标量

加热器开启时的冷却液温度。

### **Switch-off coolant temperature** — 关闭冷却液温度 `290.15`（默认）| 正标量

加热器关闭时的冷却液温度。此参数的值必须大于 **Switch-on coolant
temperature** 参数的值。

### **Algorithm data type** — 用于选择模块算法数据类型的选项 `Inherit: auto`（默认）| `double` | `single` | `<data type expression>`

*自 R2025a 起*

用于选择模块算法数据类型的选项，指定为以下值之一：

- `Inherit: auto` — 您可以以
  `single` 和 `double`
  精度对模块进行仿真。您必须将输入和参数显式指定为
  `single` 或
  `double`。
- `double` — 模块算法将所有输入
  和参数转换为 `double` 数据类型。
- `single` — 模块算法将所有输入
  和参数转换为 `single` 数据类型。
- `<data type expression>` — 模块
  算法将所有输入和参数转换为您指定的数据类型对象。

点击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant 和 Control Data Types of Signals。
## 所属库

Simscape / Battery / BMS / Thermal Management

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

### R2025a：使用 **Algorithm data type** 参数在单精度和双精度浮点仿真之间切换

您现在可以使用 **Algorithm data type** 参数，轻松地在模块算法的单精度和双精度浮点仿真之间切换。

## 描述

电池加热器控制算法

Battery Heater Control 模块实现了一种电池加热器控制
算法。

温度对电池至关重要，因为低温会显著缩短电池
寿命。因此，控制电池每个电芯的温度并激活加热器或冷却器以将温度保持在安全限值内至关重要。如果
温度过低，电池管理系统 (BMS) 会启用加热器。

此模块支持单精度和双精度
浮点仿真。

**注意**

要启用单精度浮点仿真，所有输入和
参数的数据类型必须为 `single`。

此图显示了模块的结构：

### 方程

Battery Heater Control 模块仅在环境
温度降至 **Ambient
temperature threshold for heater** 参数的值以下时激活加热器。如果温度降至
此阈值以下，**Command** 输出端口的值
等于：

Command={0,Tcoolant≥ToffCommandold,Ton<Tcoolant<Toff1,Tcoolant≤Ton

其中

- *Tcoolant* 是冷却液
  温度。
- *Ton* 是加热器开启时的冷却液
  温度。
- *Toff* 是加热器关闭时的冷却液温度。此值大于
  *T*on。
- *Commandold* 是
  上一时间步的命令。
