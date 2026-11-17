---
type: simulink-block
title: 'Ramp'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Classic Platform / Library Routines / Math Operations'
documentation_page: 'ramp'
documentation_source_path: 'ref/ramp.html'
language: zh-CN
chinese_source: worker-translation
---

# Ramp

## 端口
```yaml
ports:
- name: u
  summary: 输入信号 标量
  direction: input
  data_types: single
- name: R
  summary: 复位端口 标量
  direction: input
  data_types: Boolean
- name: rs
  summary: 上升斜率 标量
  direction: input
  data_types: single
- name: fs
  summary: 下降斜率 标量
  direction: input
  data_types: single
- name: Port_1
  summary: 输出信号 标量
  direction: output
  data_types: single
```

### 输入

### **u** — 输入信号 标量

用于生成斜坡信号的输入信号，指定为标量。

**数据类型：** `single`

### **R** — 复位端口 标量

将输出信号复位为初始条件的选项，指定为标量。

#### 依赖关系

要启用此端口，请选中 **Show reset port** 参数。

**数据类型：** `Boolean`

### **rs** — 上升斜率 标量

输出信号的增加速率，指定为标量。

#### 依赖关系

要启用此端口，请将 **Rise slope** 参数的 **Source** 字段设置为 `Input port`。

**数据类型：** `single`

### **fs** — 下降斜率 标量

输出信号的减小速率，指定为标量。

#### 依赖关系

要启用此端口，请将 **Fall Slope** 参数的 **Source** 字段设置为 `Input port`。

**数据类型：** `single`
### 输出

### **Port\_1** — 输出信号 标量

输出信号，以标量形式返回。

**数据类型：** `single`
## 参数
```yaml
parameters:
- name: Rise slope
  summary: 输出的增加值 Dialog | Input port
  group: ''
  block_parameter: RiseSlopeSource
  type: 字符向量
  values: '''Dialog'' | ''Input port'''
  default: '''Dialog'''
- name: Fall slope
  summary: 输出的减小值 标量
  group: ''
  block_parameter: FallSlopeSource
  type: 字符向量
  values: '''Dialog'' | ''Input Port'''
  default: '''Dialog'''
- name: Show reset port
  summary: 添加 R 输入端口的选项 'off'（默认）| 'on'
  group: ''
  block_parameter: ShowResetPort
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''off'''
- name: Initial condition
  summary: 输出信号的初始值 0（默认）| double
  group: ''
  block_parameter: InitialCondition
  type: 字符向量
  values: 实数有限值
  default: '''0'''
- name: Sample time
  summary: 采样周期 -1（默认）| [-1, 0] | 向量
  group: ''
  block_parameter: SampleTime
  type: 字符向量
  values: 实数有限值
  default: '''-1'''
```

### **Rise slope** — 输出的增加值 `Dialog` | `Input port`

将此参数的 **Source** 字段指定为以下值之一。

- `Dialog` — 使用此参数的 **Value** 字段设置斜率。
- `Input port` — 使用 **rs** 端口设置斜率。模块使用此端口的值作为斜率。

#### 编程用法

|  |
| --- |
| **模块参数：** `RiseSlope` |
| **类型：** 字符向量 |
| **值：** 实数有限非负值 |
| **默认值：** `'1'` |

#### 编程用法

|  |
| --- |
| **模块参数：** `RiseSlopeSource` |
| **类型：** 字符向量 |
| **值：** `'Dialog' | 'Input port'` |
| **默认值：** `'Dialog'` |

### **Fall slope** — 输出的减小值 标量

将此参数的 **Source** 字段指定为以下值之一。

- `Dialog` — 使用此参数的 **Value** 字段设置斜率。
- `Input port`  — 使用 **fs** 端口设置斜率。模块使用此端口的值作为斜率。

#### 编程用法

|  |
| --- |
| **模块参数：** `FallSlope` |
| **类型：** 字符向量 |
| **值：** 实数有限非负值 |
| **默认值：** `'1'` |

#### 编程用法

|  |
| --- |
| **模块参数：** `FallSlopeSource` |
| **类型：** 字符向量 |
| **值：** `'Dialog' | 'Input Port'` |
| **默认值：** `'Dialog'` |

### **Show reset port** — 添加 `R` 输入端口的选项 `'off'`（默认）| `'on'`

启用 **R** 输入端口。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowResetPort` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

### **Initial condition** — 输出信号的初始值 `0`（默认）| double

输出信号的初始条件，指定为 double。默认值为 `0`。

当选中 **Show reset port** 时，初始条件设置为 **Initial Condition** 参数中指定的值。

#### 编程用法

|  |
| --- |
| **模块参数：** `InitialCondition` |
| **类型：** 字符向量 |
| **值：** 实数有限值 |
| **默认值：** `'0'` |

### **Sample time** — 采样周期 `-1`（默认）| `[-1, 0]` | 向量

以秒为单位指定采样周期。

有关指定离散采样时间的详细信息，请参阅 Specify Sample Time。

#### 编程用法

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** 字符向量 |
| **值：** 实数有限值 |
| **默认值：** `'-1'` |
## 所属库

AUTOSAR Blockset / Classic Platform / Library Routines / Math Operations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

### R2025a：AUTOSAR 代码替换库支持 4.0 之后的架构版本

从 25a 开始，AUTOSAR 代码替换库支持 AUTOSAR 4.0 之后的 AUTOSAR 架构版本。要使用最新的 AUTOSAR 例程，请在模型配置参数对话框的 **Code Generation** > **Interface** 窗格中，将 **Code replacement libraries** 指定为 `AUTOSAR 4.x`。

## 描述

生成遵循输入值的信号，受上升或下降斜率约束

Mathematical Floating point Library (MFL) Ramp 模块生成一个信号，该信号从指定值开始，以指定速率变化，直到达到输入信号的值。模块参数 **Rise slope**、**Fall slope**、**Initial condition** 和 **Sample time**，以及输入信号 **u** 决定了输出信号的特性。

当您为 AUTOSAR 模型选择 `AUTOSAR 4.x` 代码替换库 (CRL) 时，模型会将该模块生成的代码替换为对以下 AUTOSAR 库例程的调用：

- `Mfl_Ramp_InitState`
- `Mfl_Ramp_SetParam`
- `Mfl_RampCalc`
- `Mfl_RampOut_f32`
