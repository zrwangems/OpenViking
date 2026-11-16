---
type: simulink-block
title: 'SOE Estimator (Energy Counting)'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'BMS / Estimators'
documentation_page: 'soeestimatorenergycounting'
documentation_source_path: 'ref/soeestimatorenergycounting.html'
language: zh-CN
chinese_source: worker-translation
---

# SOE Estimator (Energy Counting)

## 端口

### 输入

### **Current** — 电池电流，ampere 标量 | 向量

电池电流，以 ampere 为单位，对于单个电芯指定为标量，对于多个电芯指定为向量。要将此输入指定为电芯电流的向量，请选择 **将 Current 输入指定为电芯电流** 参数。

### **Voltage** — 电池电压，volt 标量 | 向量

电池电压，以 volt 为单位，对于单个电芯指定为标量，对于多个电芯指定为向量。

### **InitialSOE** — 初始能量状态，无量纲标量 | 向量

初始能量状态，指定为范围为 [0, 1] 的标量或向量。此输入端口的大小必须等于 **Current** 输入端口的大小。

### 输出

### **SOE** — 电池能量状态 标量 | 向量

电池的能量状态，以标量或向量形式返回。此输出端口的大小等于 **Current** 和 **InitialSOE** 输入端口的大小。

## 参数

### **将 Current 输入指定为电芯电流** — 用于将电流输入端口指定为向量的选项 `off` (默认) | `on`

用于将 **Current** 输入端口的值指定为电芯电流向量的选项。如果选择此参数，则 **Current** 输入端口处的值可以是标量，也可以是大小等于模块输入大小的向量。

### **标称电芯能量容量, Enom, (W\*Hr)** — 电芯的标称能量容量 `113.1300` (默认) | 正标量

电池电芯的标称能量容量，单位为瓦时。

### **采样时间（-1 表示继承）** — 模块采样时间 `1` (默认) | 0 | -1 | 整数

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当情况下更新其内部状态。有关详细信息，请参阅什么是采样时间？和指定采样时间。

对于继承的离散时间操作，请将此参数指定为 `-1`。对于离散时间操作，请将此参数指定为正整数。对于连续时间操作，请将此参数指定为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩膜子系统或变体子系统中，请提升采样时间参数。提升采样时间参数可确保模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅提升掩膜上的模块参数。

### **算法数据类型** — 用于选择模块算法数据类型的选项 `Inherit: auto` (默认) | `double` | `single` | `<data type expression>`

*自 R2025a 起*

用于选择模块算法数据类型的选项，指定为以下值之一：

- `Inherit: auto` — 您可以以 `single` 和 `double` 精度仿真该模块。您必须将输入和参数显式提供为 `single` 或 `double`。
- `double` — 模块算法将所有输入和参数转换为 `double` 数据类型。
- `single` — 模块算法将所有输入和参数转换为 `single` 数据类型。
- `<data type expression>` — 模块算法将所有输入和参数转换为您指定的数据类型对象。

单击 **显示数据类型助手** 按钮 以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用数据类型助手指定数据类型和控制信号的数据类型。

## 所属库

Simscape / Battery / BMS / Estimators

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

### R2025a: 使用 **算法数据类型** 参数在单精度和双精度浮点仿真之间切换

现在，您可以使用 **算法数据类型** 参数轻松地在模块算法的单精度和双精度浮点仿真之间切换。

## 描述

使用能量计数的能量状态估计器

SOE Estimator (Energy Counting) 模块实现了一个估计器，该估计器使用能量计数方法计算电池的能量状态 (SOE)。

SOE 是剩余能量 *E*remain 与总能量 *E*total 的比值：

SOE=EremainEtotal.

此模块支持单精度和双精度浮点仿真。

**注意**

要启用继承的单精度浮点仿真，所有输入和参数（**采样时间（-1 表示继承）** 参数除外）的数据类型必须为 `single`。

您可以使用 **采样时间（-1 表示继承）** 参数在模块的连续实现和离散实现之间切换。要将模块配置为连续时间，请将 **采样时间（-1 表示继承）** 参数设置为 `0`。要将模块配置为离散时间，请将 **采样时间（-1 表示继承）** 参数设置为正的非零值，或设置为 `-1` 以从上游模块继承采样时间。

**注意**

此模块的连续时间实现仅在双精度浮点仿真中工作。如果您提供单精度浮点参数和输入，此模块会将它们转换为双精度浮点值以防止错误。

此图显示了模块的结构：

### 方程

为了计算电池的 SOE，SOE Estimator (Energy Counting) 模块使用以下方程：

SOE=SOE(t0)+1Enom∫0tVt(t)i(t)dt

其中 *V*t 是端电压，*i* 是电流，*E*nom 是电池的标称能量容量，单位为瓦时。
