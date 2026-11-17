---
type: simulink-block
title: 'Hall Validity'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Sensor Decoders'
documentation_page: 'hallvalidity'
documentation_source_path: 'ref/hallvalidity.html'
language: zh-CN
chinese_source: worker-translation
---

# Hall Validity

## 端口
```yaml
ports:
- name: HallVal
  summary: 当前霍尔传感器输出状态标量
  direction: input
  data_types: uint8 | uint16 | uint32
- name: PrevHallVal
  summary: 前一霍尔传感器输出状态标量
  direction: input
  data_types: uint8 | uint16 | uint32
- name: Cnt
  summary: 外部计数器值标量
  direction: input
  data_types: uint8 | uint16 | uint32
- name: PrevDir
  summary: 前一霍尔状态期间的转子旋转方向标量
  direction: input
  data_types: int8 | int16 | int32
- name: Invalid
  summary: 霍尔状态有效性指示标量
  direction: output
  data_types: single | double | fixed point
- name: SpdCnt
  summary: 霍尔状态变化时的计数值标量
  direction: output
  data_types: single | double | fixed point
- name: Dir
  summary: 当前霍尔状态期间的转子旋转方向标量
  direction: output
  data_types: single | double | fixed point
- name: SpdVal
  summary: 当前和前一霍尔状态的有效性及速度计算标量
  direction: output
  data_types: single | double | fixed point
- name: HallChng
  summary: 标志置为 1，表示霍尔状态变化标量
  direction: output
  data_types: single | double | fixed point
```

### 输入

### **HallVal** — 当前霍尔传感器输出状态标量

当前时刻的霍尔状态。以下是可能的输入值（三位二进制数，其中最高有效位表示所连接的第一个霍尔的输出）：

- 5 - (101)
- 4 - (100)
- 6 - (110)
- 2 - (010)
- 3 - (011)
- 1 - (001)

**注意**

输出端口 `Invalid` 表示霍尔传感器状态异常。

**数据类型：** `uint8` | `uint16` | `uint32`

### **PrevHallVal** — 前一霍尔传感器输出状态标量

当前状态之前的霍尔状态。

**数据类型：** `uint8` | `uint16` | `uint32`

### **Cnt** — 外部计数器值标量

模块用于确定霍尔状态变化与模块执行之间所经过时间的外部计数器值。

**注意**

当霍尔状态发生变化时，计数器必须复位。

**数据类型：** `uint8` | `uint16` | `uint32`

### **PrevDir** — 前一霍尔状态期间的转子旋转方向标量

前一霍尔状态期间的转子旋转方向（+1 或 -1，分别表示正方向或负方向旋转）。

**数据类型：** `int8` | `int16` | `int32`
### 输出

### **Invalid** — 霍尔状态有效性指示标量

当前或前一霍尔状态期间霍尔传感器有效性的指示。模块通过将 `HallVal` 和 `PrevHallVal` 输入端口的值与 **Expected hall sequence in positive direction** 参数的值进行比较来检查传感器的有效性。该端口可输出以下值：

- 1 – (001) 表示一个（或多个）传感器异常。
- 0 – (000) 表示所有传感器正常。

**数据类型：** `single` | `double` | `fixed point`

### **SpdCnt** — 霍尔状态变化时的计数值标量

霍尔状态变化时 `Cnt` 输入端口的值。

**注意**

当霍尔状态发生变化时，计数器必须复位。因此，该端口表示前一霍尔状态期间的计数值。

**数据类型：** `single` | `double` | `fixed point`

### **Dir** — 当前霍尔状态期间的转子旋转方向标量

当前霍尔状态期间的转子旋转方向（+1 或 –1，分别表示正方向或负方向旋转）。模块通过将 `HallVal` 和 `PrevHallVal` 输入端口的值与 **Expected hall sequence in positive direction** 参数的值进行比较来计算方向。

**数据类型：** `single` | `double` | `fixed point`

### **SpdVal** — 当前和前一霍尔状态的有效性及速度计算标量

当出现以下任一或两种情况时，该端口输出零：

- 模块检测到霍尔传感器状态异常（`HallVal` 或 `PrevHallVal` 输入端口值中任一异常）。
- 模块检测到转子旋转方向发生变化。

零值表示由于 `SpdCnt` 的当前值无效，无法计算当前霍尔状态的有效速度。该端口输出值 1 表示可以进行有效的速度计算。

**数据类型：** `single` | `double` | `fixed point`

### **HallChng** — 标志置为 1，表示霍尔状态变化标量

在霍尔状态发生变化且模块完成执行后，该端口输出值 1（并将霍尔状态变化标志置为 1）。

**数据类型：** `single` | `double` | `fixed point`
## 参数
```yaml
parameters:
- name: Expected hall sequence in positive direction
  summary: 表示正方向的序列 ABC（默认）| CBA | Custom sequence
  group: ''
- name: Sequence
  summary: 表示正方向的自定义序列 [5,4,6,2,3,1]（默认）| 标量
  group: ''
- name: Counter size
  summary: 外部计数器寄存器的尺寸 16 bits（默认）| 8 bits | 32 bits
  group: ''
```

### **Expected hall sequence in positive direction** — 表示正方向的序列 `ABC`（默认）| `CBA` | `Custom sequence`

表示转子正方向旋转的霍尔传感器序列。

### **Sequence** — 表示正方向的自定义序列 `[5,4,6,2,3,1]`（默认）| 标量

可输入用于表示转子正方向旋转的自定义序列。

#### 依赖

要启用此参数，请将 **Expected hall sequence in positive direction** 设置为 `Custom sequence`。

### **Counter size** — 外部计数器寄存器的尺寸 `16 bits`（默认）| `8 bits` | `32 bits`

外部计数器的寄存器尺寸。最大计数值为 2n-1，其中 n = 计数器尺寸。
## 所属库

Motor Control Blockset / Sensor Decoders

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中引入**

## 描述

计算转子旋转方向和霍尔传感器序列的有效性

Hall Validity 模块检查并验证霍尔传感器输出序列的每个状态。该模块识别一个或多个霍尔传感器处于无效状态的情况。

该模块在霍尔传感器输出状态（或霍尔状态）发生变化时执行。
