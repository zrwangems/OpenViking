---
type: simulink-block
title: 'Battery Charging Current Limit'
family: 'bms'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'BMS / Current Management'
documentation_page: 'batterychargingcurrentlimit'
documentation_source_path: 'ref/batterychargingcurrentlimit.html'
language: zh-CN
chinese_source: worker-translation
---

# Battery Charging Current Limit

## 端口

### 输入

### **CellVoltage** — 电芯电压，V 标量 | 向量

电芯电压，单位为 volt，指定为单个电芯的标量或多个电芯的向量。

如果选择 **将输入指定为 [Min,Max]** 参数，则必须为此端口指定最小值和最大值，例如 `CellVoltage=[CellVoltageMin,CellVoltageMax]`。*(自 R2025a 起)*

### **CellTemperature** — 电芯温度，K 标量 | 向量

电芯温度，指定为单个电芯的标量或多个电芯的向量。此输入端口的大小必须等于 **CellVoltage** 参数的大小。

如果选择 **将输入指定为 [Min,Max]** 参数，则必须为此端口指定最小值和最大值，例如 `CellTemperature=[CellTemperatureMin,CellTemperatureMax]`。*(自 R2025a 起)*

### 输出

### **CurrentLimit** — 电池包的充电电流限制 标量

电池包的充电电流限制，以标量形式返回。

## 参数

### **将输入指定为 [Min,Max]** — 用于将输入指定为最小值和最大值的选项 `off`（默认） | `on`

*自 R2025a 起*

用于将 **CellVoltage** 和 **CellTemperature** 输入端口处的值指定为最小值和最大值向量的选项。如果取消选中此参数，则必须为输入端口指定各个值。然后，模块会在内部计算最小值和最大值。

### **电芯过压限制 (V)** — 电芯的过压限制 `4.5`（默认） | 正标量

电池电芯超过该限制即视为过充，单位为 volt。

### **端子电阻 (ohm)** — 端子电阻 `0.0025`（默认） | 正标量

端子电阻，*R0*，单位为 ohm。

### **温度向量, T** — 电芯温度 `[243.15, 258.15, 273.15, 288.15, 303.15, 318.15, 333.15]`（默认） | 标量向量

电芯温度。此参数的物理单位必须与 **CellTemperature** 输入端口的物理单位相同。

### **最冷电芯的电流限制, iCool(T), (A)** — 最冷电芯的电流限制 `[ 0, 0, 0, 0, 100, 100, 100]`（默认） | 正标量向量

最冷电芯的电流限制，单位为 ampere。此向量的大小必须等于 **温度向量, T** 参数的大小。

### **最热电芯的电流限制, iHot(T), (A)** — 最热电芯的电流限制 `[100, 100, 100, 100, 0, 0, 0]`（默认） | 正标量向量

最热电芯的电流限制，单位为 ampere。此向量的大小必须等于 **温度向量, T** 参数的大小。

### **算法数据类型** — 用于选择模块算法数据类型的选项 `Inherit: auto`（默认） | `double` | `single` | `<data type expression>`

*自 R2025a 起*

用于选择模块算法数据类型的选项，指定为以下值之一：

- `Inherit: auto` — 您可以在 `single` 和 `double` 精度下仿真该模块。必须将输入和参数显式提供为 `single` 或 `double`。
- `double` — 模块算法将所有输入和参数转换为 `double` 数据类型。
- `single` — 模块算法将所有输入和参数转换为 `single` 数据类型。
- `<data type expression>` — 模块算法将所有输入和参数转换为指定的数据类型对象。

单击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用数据类型助手指定数据类型和控制信号的数据类型。

## 所属库

Simscape / Battery / BMS / Current Management

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

### R2025a：使用 **算法数据类型** 参数在单精度和双精度浮点仿真之间切换

现在，您可以使用 **算法数据类型** 参数轻松地在模块算法的单精度和双精度浮点仿真之间切换。

### R2025a：为输入端口指定最小值和最大值

您可以为 **CellVoltage** 和 **CellTemperature** 输入端口指定最小值和最大值。要将这些输入指定为最小值和最大值，请选择 **将输入指定为 [Min,Max]** 参数。

## 描述

最大电池充电电流

Battery Charging Current Limit 模块计算电池的最大充电电流。在对电池包建模时，限制充电和放电电流是一项重要考虑因素。

此模块支持单精度和双精度浮点仿真。

**注意**

要启用单精度浮点仿真，所有输入和参数的数据类型必须为 `single`。

下图显示该模块的结构：

### 方程

充电电流限制等于以下值中的最小值：

- 最冷和最热电芯的温度相关限制
- 基于电芯过压限制的理论电流
- 端子电阻

CurrentLimit=min(i1,i2,i3)i1=OvervoltageLimit−max(CellVoltage)R0i2=f(min(CellTemperature))i3=g(max(CellTemperature))

其中

- *OvervoltageLimit* 是 **电芯过压限制 (V)** 参数的值。
- *CellVoltage* 是 **CellVoltage** 输入端口的值。
- *R0* 是 **端子电阻 (ohm)** 参数的值。
- *CellTemperature* 是 **CellTemperature** 输入端口的值。
