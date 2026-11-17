---
type: simulink-block
title: 'Stair Generator'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'stairgenerator'
documentation_source_path: 'ref/stairgenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Stair Generator

## 端口
```yaml
ports:
- name: Port_1
  summary: 阶梯信号 Simulink® 信号
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64
```

### 输出

### **Port\_1** — 阶梯信号 Simulink® 信号

阶梯信号，作为 Simulink 输出信号返回。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
## 参数
```yaml
parameters:
- name: Time (s)
  summary: 过渡时间 [0.5 1 3 3.5]（默认）| 非负值行向量
  group: 主
- name: Amplitude
  summary: 阶梯信号值的幅值 [1 -1 2.5 0]（默认）| 行向量
  group: 主
- name: Sample time (-1 for inherited)
  summary: 模块采样时间 -1（默认）| 0 | 正标量
  group: 主
- name: Repeat stair pattern indefinitely
  summary: 阶梯模式重复 off（默认）| on
  group: 主
- name: Output data type
  summary: '指定输出数据类型 double（默认）| Inherit: auto | Inherit: Inherit via internal rule | Inherit: Inherit via back propagation
    | single | int8 | uint8 | int16 | uint16 | int32 | uint32 | int64 | uint64 | <data type expression>'
  group: 信号属性
  block_parameter: OutDataTypeStr
  type: 字符向量
  values: '''Inherit: auto'' | ''Inherit: Inherit via internal rule''| ''Inherit: Inherit via back propagation'' | ''single''
    | ''double'' | ''int8'' | ''uint8'' | ''int16'' | ''uint16'' | ''int32'' | ''uint32''|''int64''|''uint64''| ''<data type
    expression>'''
```

### 主

### **Time (s)** — 过渡时间 `[0.5 1 3 3.5]`（默认）| 非负值行向量

输出变为 **Amplitude** 参数所指定值的过渡时间，以秒为单位。此参数的值必须严格递增。

### **Amplitude** — 阶梯信号值的幅值 `[1 -1 2.5 0]`（默认）| 行向量

阶梯信号在 **Time (s)** 参数所指定时间处的幅值。此向量的元素数量必须与 **Time (s)** 参数相同。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| `0` | 正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当情况下更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，将此参数设置为 `-1`。对于离散时间操作，将此参数设置为正整数。对于连续时间操作，将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

### **Repeat stair pattern indefinitely** — 阶梯模式重复 `off`（默认）| `on`

是否无限重复阶梯模式。如果选择此参数，输出将无限重复由 **Time (s)** 和 **Amplitude** 参数定义的阶梯模式。

如果清除此参数，输出仅执行一次阶梯模式，然后保持最后一个幅值在所有后续时间处于激活状态。

### 信号属性

### **Output data type** — 指定输出数据类型 `double`（默认）| `Inherit: auto` | `Inherit: Inherit via internal rule` | `Inherit: Inherit via back propagation` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `<data type expression>`

输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当选择继承选项时，模块表现出以下行为：

- `Inherit: Inherit via internal rule` — Simulink 选择一种数据类型，以在数值精度、性能和生成代码大小之间取得平衡，同时考虑嵌入式目标硬件的属性。如果更改嵌入式目标设置，内部规则所选择的数据类型可能会改变。软件并不总是能够同时优化效率和数值精度。
- `Inherit: Inherit via back propagation` — Simulink 在数据类型传播期间自动确定模块的输出数据类型（请参阅 Data Type Propagation）。在这种情况下，模块使用下游模块或信号对象的数据类型。
- `Inherit: auto` — 使用继承数据类型的规则。

有关详细信息，请参阅 Control Data Types of Signals。

#### 程序化使用

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: auto'` | `'Inherit: Inherit via internal rule'`| `'Inherit: Inherit via back propagation'` | `'single'` | `'double'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'`|`'int64'`|`'uint64'`| `'<data type expression>'` |
| **默认**：`'Inherit: Inherit via internal rule'` |
## 所属库

Simscape / Electrical / Control / General Control

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2020a 中引入**

## 描述

离散时间或连续时间阶梯信号发生器

Stair Generator 模块根据 **Time (s)** 和 **Amplitude** 参数中指定的值生成阶梯信号。

该模块可以输出重复的阶梯模式，也可以通过保持最后一个幅值在所有后续时间处于激活状态来仅执行一次该模式。
