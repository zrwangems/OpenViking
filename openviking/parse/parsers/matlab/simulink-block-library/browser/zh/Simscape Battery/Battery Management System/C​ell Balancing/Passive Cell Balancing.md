---
type: simulink-block
title: 'Passive Cell Balancing'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Battery Management System / C\u200bell Balancing'
documentation_page: 'passivecellbalancing'
documentation_source_path: 'ref/passivecellbalancing.html'
language: zh-CN
chinese_source: worker-translation
---

# Passive Cell Balancing

## 端口

### 输入

### **u** — 电芯电压或电芯 SOC 值向量

电芯电压或电芯 SOC 值，指定为向量。

**注意**

输入端口 **u** 期望来自真实传感器的电芯电压。为了模拟传感器并求解代数环，如果您从模型馈送仿真输出，请添加单位延迟、传递函数或任何其他滤波器。

### **Enable** — 是否启用电芯平衡标量

是否启用被动电芯平衡，指定为 `1`（启用）或 `0`（禁用）。

### 输出

### **Command** — 平衡命令向量

平衡命令，返回为由等于 `0` 或 `1` 的项组成的向量。此向量的大小等于 **u** 输入的大小。

### **BalancingActive** — 平衡过程是否处于活动状态标量

平衡过程是否处于活动状态，返回为标量。

## 参数

### 主要

### **Threshold for balancing** — 平衡阈值 `0.2` (默认) | 非负标量

模块用于平衡的阈值。

### **Hysteresis band for switching balancing off** — 用于关闭被动平衡的迟滞带 `0` (默认) | 非负标量

*自 R2023b 起*

用于关闭被动电芯平衡的迟滞带。此参数的值必须小于或等于 **Threshold for balancing** 参数的值。

### **ON delay time (s)** — 平衡激活前的时间延迟 `1` (默认) | 非负标量

激活电芯平衡前的时间延迟，以秒为单位。

### **OFF delay time (s)** — 平衡完成后的时间延迟 `1` (默认) | 非负标量

模块完成平衡过程后的时间延迟，以秒为单位。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1` (默认) | 0 | 正整数

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，将此参数指定为 `-1`。对于离散时间操作，将此参数指定为正整数。对于连续时间操作，将此参数指定为 `0`。

如果此模块位于允许在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升采样时间参数。提升采样时间参数可确保在模块的连续和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

### 信号属性

### **Command Data Type** — Command 输出的数据类型 `double` (默认) | `single` | `boolean` | `<data type expression>`

指定 **Command** 输出的数据类型。您可以直接指定类型，也可以将其表示为数据类型对象，例如 `Simulink.NumericType`。

点击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

## 所属库

Simscape / Battery / BMS / Cell Balancing

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2022b 中引入**

## 描述

被动电池电芯平衡算法

此模块实现被动电池电芯平衡算法。被动电芯平衡技术通过将多余电荷消耗在泄放电阻中来保持所有电芯具有相似的荷电状态值。

**u** 输入端口的值可以是电芯电压或电芯荷电状态 (SOC) 值。**Enable** 输入端口充当平衡过程的触发器。当 **Enable** 为 `1` 时，模块开始平衡电池，直到电池完全平衡。

此模块支持单精度和双精度浮点仿真。

**注意**

要启用继承的单精度浮点仿真，所有输入和参数（**Sample time (-1 for inherited)** 参数除外）的数据类型都必须为 `single`。

您可以使用 **Sample time (-1 for inherited)** 参数在模块的连续和离散实现之间切换。要将模块配置为连续时间，请将 **Sample time (-1 for inherited)** 参数设置为 `0`。要将模块配置为离散时间，请将 **Sample time (-1 for inherited)** 参数设置为正的非零值，或设置为 `-1` 以从上游模块继承采样时间。

**注意**

此模块的连续时间实现仅适用于双精度浮点仿真。如果您提供单精度浮点参数和输入，此模块会将它们转换为双精度浮点值以防止错误。

此图显示了模块的结构：

### 方程

当 **Enable** 输入端口处的值为 `1` 时，模块开始平衡电池，直到电池完全平衡。为了平衡电池，算法会放电某些电芯，直到其电压或荷电状态等于具有最低值的电芯的电压或荷电状态。

**Command** 输出端口将平衡命令指定为元素等于 0 或 1 的向量。此方程确定 **Command** 的每个元素：

Command={0如果 u−min(u)≤Threshold−HysteresisBandCommandold如果 Threshold−HysteresisBand<u−min(u)<Threshold1如果 u−min(u)≥Threshold

其中 *Threshold* 是 **Threshold for balancing** 参数的值，*HysteresisBand* 是 **Hysteresis band for switching balancing off** 参数的值，*Commandold* 是上一步的命令。

要指定 **Command** 输出端口的数据类型，请使用 **Command Data Type** 参数。

如果电池的任何电芯超过阈值，则 **BalancingActive** 输出端口为 true。
