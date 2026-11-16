---
type: simulink-block
title: 'Stair Generator'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / General Control\u200b / Sources'
documentation_page: 'stairgenerator'
documentation_source_path: 'ref/stairgenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Stair Generator

## 端口

### 输出

### **Port\_1** — 阶梯信号 Simulink® 信号

阶梯信号，返回为 Simulink 输出信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

## 参数

### 主

### **时间 (s)** — 转换时间 `[0.5 1 3 3.5]`（默认）| 非负值的行向量

输出变为 **幅值** 参数中指定值的转换时间，以秒为单位。此参数的值必须严格递增。

### **幅值** — 阶梯信号值的幅值 `[1 -1 2.5 0]`（默认）| 行向量

在 **时间 (s)** 参数指定的时间处，阶梯信号的幅值。此向量必须与 **时间 (s)** 参数具有相同数量的元素。

### **采样时间（继承时为 -1）** — 模块采样时间 `-1`（默认）| `0` | 正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅什么是采样时间？和指定采样时间。

对于继承的离散时间操作，将此参数设置为 `-1`。对于离散时间操作，将此参数设置为正整数。对于连续时间操作，将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩膜子系统或变体子系统中，请提升此参数，以确保模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅在掩膜上提升模块参数。

### **无限重复阶梯模式** — 阶梯模式重复 `off`（默认）| `on`

是否无限重复阶梯模式。如果选择此参数，输出将无限重复由 **时间 (s)** 和 **幅值** 参数定义的阶梯模式。

如果清除此参数，则输出仅执行阶梯模式一次，然后使最后一个幅值在所有后续时间保持有效。

### 信号属性

### **输出数据类型** — 指定输出数据类型 `double`（默认）| `Inherit: auto` | `Inherit: Inherit via internal rule` | `Inherit: Inherit via back propagation` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `<data type expression>`

输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

选择继承选项时，模块会表现出以下行为：

- `Inherit: Inherit via internal rule` — Simulink 选择一种数据类型，以在考虑嵌入式目标硬件属性的同时，平衡数值精度、性能和生成的代码大小。如果更改嵌入式目标设置，内部规则选择的数据类型可能会更改。软件并非总能同时优化效率和数值精度。
- `Inherit: Inherit via back propagation` — Simulink 在数据类型传播期间自动确定模块的输出数据类型（请参阅数据类型传播）。在这种情况下，模块使用下游模块或信号对象的数据类型。
- `Inherit: auto` — 使用继承数据类型的规则。

有关详细信息，请参阅控制信号的数据类型。

#### 编程用法

|  |
| --- |
| **模块参数**: `OutDataTypeStr` |
| **类型**: 字符向量 |
| **值**: `'Inherit: auto'` | `'Inherit: Inherit via internal rule'`| `'Inherit: Inherit via back propagation'` | `'single'` | `'double'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'`|`'int64'`|`'uint64'`| `'<data type expression>'` |
| **默认值**: `'Inherit: Inherit via internal rule'` |

## 所属库

Simscape / Electrical / Control / General Control

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2020a 中引入**

## 描述

离散时间或连续时间阶梯信号发生器

Stair Generator 模块基于 **时间 (s)** 和 **幅值** 参数中指定的值生成阶梯信号。

该模块可以输出重复的阶梯模式，也可以通过使最后一个幅值在所有后续时间保持有效来仅执行该模式一次。
