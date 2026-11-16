---
type: simulink-block
title: 'Battery Discharging Current Limit'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Battery Management System / Current Management\u200b'
documentation_page: 'batterydischargingcurrentlimit'
documentation_source_path: 'ref/batterydischargingcurrentlimit.html'
language: zh-CN
chinese_source: worker-translation
---

# Battery Discharging Current Limit

## 端口

### 输入

### **CellVoltage** — 电芯电压，V 标量 | 向量

电芯电压，单位为 V，指定为单个电芯的标量或多个电芯的向量。

*在 R2025a 中：如果选择 **Specify inputs as [Min,Max]** 参数，则必须为此端口指定最小值和最大值，例如 `CellVoltage=[CellVoltageMin,CellVoltageMax]`。*

### **CellTemperature** — 电芯温度，K 标量 | 向量

电芯温度，指定为单个电芯的标量或多个电芯的向量。此输入端口的尺寸必须等于 **CellVoltage** 参数的尺寸。

如果选择 **Specify inputs as [Min,Max]** 参数，则必须为此端口指定最小值和最大值，例如 `CellTemperature=[CellTemperatureMin,CellTemperatureMax]`。*（自 R2025a 起）*

### 输出

### **CurrentLimit** — 电池包充电电流限值，标量

电池包的放电电流限值，以标量形式返回。

## 参数

### **Specify inputs as [Min,Max]** — 用于将输入指定为最小值和最大值的选项 `off` (默认) | `on`

*自 R2025a 起*

用于将 **CellVoltage** 和 **CellTemperature** 输入端口处的值指定为最小值和最大值向量的选项。如果清除此参数，则必须为输入端口指定单个值。然后模块会在内部计算最小值和最大值。

### **Cell undervoltage limit (V)** — 电芯欠压限值 `2.5` (默认) | 正标量

低于该限值时，电池电芯处于欠充状态，单位为 volt。

### **Terminal resistance (ohm)** — 端子电阻 `0.0025` (默认) | 正标量

端子电阻 *R0*，单位为 ohm。

### **Vector of temperatures, T** — 电芯温度 `[243.15, 258.15, 273.15, 288.15, 303.15, 318.15, 333.15]` (默认) | 标量组成的向量

电芯温度。此参数的物理单位必须与 **CellTemperature** 输入端口的物理单位相同。

### **Current limit for coolest cell, iCool(T), (A)** — 最冷电芯的电流限值 `[ 0, 0, 0, 0, 100, 100, 100]` (默认) | 正标量组成的向量

最冷电芯的电流限值，单位为 ampere。此向量的大小必须等于 **Vector of temperature, T** 参数的大小。

### **Current limit for hottest cell, iHot(T), (A)** — 最热电芯的电流限值 `[100, 100, 100, 100, 0, 0, 0]` (默认) | 正标量组成的向量

最热电芯的电流限值，单位为 ampere。此向量的大小必须等于 **Vector of temperature, T** 参数的大小。

### **Algorithm data type** — 用于为模块算法选择数据类型的选项 `Inherit: auto` (默认) | `double` | `single` | `<data type expression>`

*自 R2025a 起*

用于为模块算法选择数据类型的选项，指定为以下值之一：

- `Inherit: auto` — 您可以在 `single` 和 `double` 精度下仿真模块。必须显式地将输入和参数提供为 `single` 或 `double`。
- `double` — 模块算法将所有输入和参数转换为 `double` 数据类型。
- `single` — 模块算法将所有输入和参数转换为 `single` 数据类型。
- `<data type expression>` — 模块算法将所有输入和参数转换为您指定的数据类型对象。

单击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用数据类型助手指定数据类型和控制信号的数据类型。

## 所属库

Simscape / Battery / BMS / Current Management

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

### R2025a：使用 **Algorithm data type** 参数在单精度和双精度浮点仿真之间切换

现在，您可以使用 **Algorithm data type** 参数轻松地在模块算法的单精度和双精度浮点仿真之间切换。

### R2025a：为输入端口指定最小值和最大值

您可以为 **CellVoltage** 和 **CellTemperature** 输入端口指定最小值和最大值。要将这些输入指定为最小值和最大值，请选择 **Specify inputs as [Min,Max]** 参数。

## 描述

最大电池放电电流

Battery Discharging Current Limit 模块计算电池的最大放电电流。在建模电池包时，限制充电和放电电流是一项重要考虑因素。

此模块支持单精度和双精度浮点仿真。

**注意**

要启用单精度浮点仿真，所有输入和参数的数据类型必须为 `single`。

此图显示了模块的结构：

### 方程

放电电流限值等于以下值中的最小值：

- 最冷和最热电芯的温度相关限值
- 基于电芯欠压限值的理论电流
- 端子电阻

CurrentLimit=−min(i1,i2,i3)
i1=(min(CellVoltage)−UndervoltageLimit)/R0
i2=f(min(CellTemperature))
i3=g(max(CellTemperature))

其中

- *UndervoltageLimit* 是 **Cell undervoltage limit (V)** 参数的值。
- *CellVoltage* 是 **CellVoltage** 输入端口的值。
- *R0* 是 **Terminal resistance (ohm)** 参数的值。
- *CellTemperature* 是 **CellTemperature** 输入端口的值。
