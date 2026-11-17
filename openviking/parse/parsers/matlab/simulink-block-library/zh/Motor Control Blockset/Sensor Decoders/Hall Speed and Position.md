---
type: simulink-block
title: 'Hall Speed and Position'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Sensor Decoders'
documentation_page: 'hallspeedandposition'
documentation_source_path: 'ref/hallspeedandposition.html'
language: zh-CN
chinese_source: worker-translation
---

# Hall Speed and Position

## 端口
```yaml
ports:
- name: HallVal
  summary: 当前霍尔传感器输出状态标量
  direction: input
  data_types: uint8 | uint16 | uint32
- name: Cnt
  summary: 外部计数器值标量
  direction: input
  data_types: uint8 | uint16 | uint32
- name: SpdCnt
  summary: 霍尔状态变化时的计数值标量
  direction: input
  data_types: uint8 | uint16 | uint32
- name: Dir
  summary: 当前霍尔状态期间的转子旋转方向标量
  direction: input
  data_types: int8 | int16 | int32
- name: SpdVal
  summary: 当前和前一霍尔状态及速度计算的有效性标量
  direction: input
  data_types: uint8 | uint16 | uint32
- name: HallChng
  summary: 霍尔状态变化标志的值标量
  direction: input
  data_types: uint8 | uint16 | uint32
- name: θe
  summary: 转子电角度位置标量
  direction: output
  data_types: single | double | fixed point
- name: ⍵m
  summary: 转子机械速度标量
  direction: output
  data_types: single | double | fixed point
- name: HallChngRst
  summary: 将霍尔状态变化标志重置为零标量
  direction: output
  data_types: single | double | fixed point
```

### 输入

### **HallVal** — 当前霍尔传感器输出状态标量

当前时刻的霍尔状态。例如，以下是可能的有效霍尔状态（其中 MSB 表示所连接的第一个霍尔传感器的输出）：

- 5 - (101)
- 4 - (100)
- 6 - (110)
- 2 - (010)
- 3 - (011)
- 1 - (001)

**数据类型：** `uint8` | `uint16` | `uint32`

### **Cnt** — 外部计数器值标量

模块用于确定霍尔状态变化与模块执行之间所经过时间的外部计数器值。

**数据类型：** `uint8` | `uint16` | `uint32`

### **SpdCnt** — 霍尔状态变化时的计数值标量

该值表示两次连续霍尔状态变化之间经过的时钟周期（时间）。

**数据类型：** `uint8` | `uint16` | `uint32`

### **Dir** — 当前霍尔状态期间的转子旋转方向标量

当前霍尔状态期间转子的旋转方向（+1 或 –1 分别表示正方向或负方向旋转）。

**数据类型：** `int8` | `int16` | `int32`

### **SpdVal** — 当前和前一霍尔状态及速度计算的有效性标量

该端口值表示霍尔状态的有效性。值为零表示当前或前一霍尔状态无效，模块无法计算速度和位置。

值为一表示当前和前一霍尔状态均有效，模块可以计算速度和位置。

**数据类型：** `uint8` | `uint16` | `uint32`

### **HallChng** — 霍尔状态变化标志的值标量

该端口值表示霍尔状态变化和模块执行状态。值为一表示霍尔状态已变化，但模块执行尚未完成。值为零表示模块已完成对上一次霍尔状态变化的执行。

**数据类型：** `uint8` | `uint16` | `uint32`
### 输出

### **θe** — 转子电角度位置标量

基于 **Expected hall sequence in positive direction** 参数以及 `Direction`、`HallVal` 和 `CounterValue` 输入估算的转子电角度位置。

#### 依赖

要启用此端口，请将 **Block output** 设置为 `Position` 或 `Speed and position`。

**数据类型：** `single` | `double` | `fixed point`

### **⍵m** — 转子机械速度标量

转子的机械速度，单位为每分钟转数。模块通过跟踪霍尔状态变化来计算该值。

如果 `SpdVal` 输入为零，则该端口返回零。

#### 依赖

要启用此端口，请将 **Block output** 设置为 `Speed` 或 `Speed and position`。

**数据类型：** `single` | `double` | `fixed point`

### **HallChngRst** — 将霍尔状态变化标志重置为零标量

该端口输出零值（将霍尔状态变化标志设置为零），表示模块已成功完成对上一次霍尔状态变化的速度和位置计算。

**数据类型：** `single` | `double` | `fixed point`
## 参数
```yaml
parameters:
- name: Block output
  summary: 选择输出端口 Speed and position（默认）| Speed | Position
  group: 常规
- name: Counter size
  summary: 外部计数器寄存器的大小 32 bits（默认）| 8 bits | 16 bits
  group: 常规
- name: Counter clock frequency (Hz)
  summary: 外部计数器的时钟频率 90e6（默认）| 标量
  group: 常规
- name: Discrete step size (s)
  summary: 模块再次执行的采样时间 50e-6（默认）| 标量
  group: 常规
- name: Number of pole pairs
  summary: 电机中可用的极对数 8（默认）| 标量
  group: 常规
- name: Minimum detectable speed (RPM)
  summary: 模块能够检测的最小速度 20（默认值）| 标量
  group: 常规
- name: Speed measurement interval
  summary: 模块测量速度的间隔 Every 180 Degrees（默认值）| Every 60 Degrees
  group: 常规
- name: Speed unit
  summary: 转子角速度输出的单位 Radians/sec（默认值）| Degrees/sec | RPM | Per unit
  group: 常规
- name: Speed datatype
  summary: 转子角速度输出的数据类型 single（默认值）| double | fixed point
  group: 常规
- name: Expected hall sequence in positive direction
  summary: 表示正方向的序列 ABC（默认值）| CBA | Custom sequence
  group: Position
- name: Sequence
  summary: 表示正方向的自定义序列 [5,4,6,2,3,1]（默认值）| 标量
  group: Position
- name: Order of extrapolation of position
  summary: 表示位置计算的精度 1st Order（默认值）| 2nd Order
  group: Position
- name: Position unit
  summary: 角位置输出的单位 Radians（默认值）| Degrees | Per unit
  group: Position
- name: Position datatype
  summary: 角位置输出的数据类型 single（默认值）| double | fixed point
  group: Position
```

### 常规

### **Block output** — 选择输出端口 `Speed and position`（默认）| `Speed` | `Position`

将可用的模块输出端口选择为以下值之一：

- Speed and position
- Speed
- Position

### **Counter size** — 外部计数器寄存器的大小 `32 bits`（默认）| `8 bits` | `16 bits`

外部计数器的寄存器大小。最大计数值为 2n-1，其中 n = 计数器大小。

### **Counter clock frequency (Hz)** — 外部计数器的时钟频率 `90e6`（默认）| 标量

外部计数器的时钟频率。

### **Discrete step size (s)** — 模块再次执行的采样时间 `50e-6`（默认）| 标量

两次连续模块执行实例之间的时间。

### **Number of pole pairs** — 电机中可用的极对数 `8`（默认）| 标量

电机中可用的极对数。

### **Minimum detectable speed (RPM)** — 模块能够检测的最小速度 `20`（默认值）| 标量

当速度低于此值时，模块不计算位置。

### **Speed measurement interval** — 模块测量速度的间隔 `Every 180 Degrees`（默认值）| `Every 60 Degrees`

表示 `SpdCnt` 端口值计算间隔的转子角位移。

### **Speed unit** — 转子角速度输出的单位 `Radians/sec`（默认值）| `Degrees/sec` | `RPM` | `Per unit`

角速度或机械速度（`⍵m`）输出的单位。

#### 依赖关系

要启用此参数，请将 **Block output** 设置为 `Speed` 或 `Speed and position`。

### **Speed datatype** — 转子角速度输出的数据类型 `single`（默认值）| `double` | `fixed point`

转子角速度输出的数据类型。

#### 依赖关系

要启用此参数，请将 **Block output** 设置为 `Speed` 或 `Speed and position`。

### Position

### **Expected hall sequence in positive direction** — 表示正方向的序列 `ABC`（默认值）| `CBA` | `Custom sequence`

表示转子正方向旋转的霍尔传感器序列。

#### 依赖关系

要启用此参数，请将 **Block output** 设置为 `Position` 或 `Speed and position`。

### **Sequence** — 表示正方向的自定义序列 `[5,4,6,2,3,1]`（默认值）| 标量

您可以输入的自定义序列，用于表示转子正方向旋转。

#### 依赖关系

要启用此参数：

- 将 **Block output** 设置为 `Position` 或 `Speed and position`。
- 将 **Expected hall sequence in positive direction** 设置为 `Custom sequence`。

### **Order of extrapolation of position** — 表示位置计算的精度 `1st Order`（默认值）| `2nd Order`

`1st Order` 选项在计算位置时精度较低，但速度快。`2nd Order` 选项精度更高，但需要更多计算时间。以下方程描述了这些选项：

θ1st Order=θsector+ωt

θ2nd Order=θsector+ωt+12αt2

其中：

θ1st Order = 使用一阶外推计算的位置。

θ2nd Order = 使用二阶外推计算的位置。

θsector = 由霍尔传感器输出定义的扇区角度。

ω = 转子的角速度。

α = 转子的角加速度。

t = 在扇区中花费的时间。

#### 依赖关系

要启用此参数，请将 **Block output** 设置为 `Position` 或 `Speed and position`。

### **Position unit** — 角位置输出的单位 `Radians`（默认值）| `Degrees` | `Per unit`

角位置输出的单位。

#### 依赖关系

要启用此参数，请将 **Block output** 设置为 `Position` 或 `Speed and position`。

### **Position datatype** — 角位置输出的数据类型 `single`（默认值）| `double` | `fixed point`

角位置输出的数据类型。

#### 依赖关系

要启用此参数，请将 **Block output** 设置为 `Position` 或 `Speed and position`。
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

使用霍尔传感器计算转速并估算转子位置

Hall Speed and Position 模块通过跟踪霍尔状态的变化来计算转子的机械速度。该模块还使用方向、霍尔状态和外部计数器值输入来估算转子的电位置。

该模块在控制器算法定义的固定时间间隔后周期性执行。
