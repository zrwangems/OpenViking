---
type: simulink-block
title: 'Repeating Sequence Interpolated'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'repeatingsequenceinterpolated'
documentation_source_path: 'slref/repeatingsequenceinterpolated.html'
language: zh-CN
chinese_source: worker-translation
---

# Repeating Sequence Interpolated

## 端口
```yaml
ports:
- name: Port_1
  summary: 周期性输出信号 标量
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
```

### 输出

### **Port\_1** — 周期性输出信号 标量

基于 **Vector of time values** 和 **Vector of output values** 参数中的值生成的输出信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
## 参数
```yaml
parameters:
- name: Vector of output values
  summary: 输出值向量 [3 1 4 2 1].'（默认）| 向量
  group: 主要
  block_parameter: OutValues
  type: 字符向量
  values: 向量
  default: '''[3 1 4 2 1].'''''
- name: Vector of time values
  summary: 时间值向量 [0 0.1 0.5 0.6 1].'（默认）| 向量
  group: 主要
  block_parameter: TimeValues
  type: 字符向量
  values: 向量
  default: '''[0 0.1 0.5 0.6 1].'''''
- name: Lookup Method
  summary: 输出的查找方法 Interpolation-Use End Values（默认）| Use Input Nearest | Use Input Below | Use Input Above
  group: 主要
  block_parameter: LookUpMeth
  type: 字符向量
  values: '''Interpolation-Use End Values'' | ''Use Input Nearest'' | ''Use Input Below'' | ''Use Input Above'''
  default: '''Interpolation-Use End Values'''
- name: Sample time
  summary: 采样之间的时间间隔 0.01（默认）| 标量
  group: 主要
  block_parameter: tsamp
  type: 字符向量
  values: 标量
  default: '''0.01'''
- name: Output minimum
  summary: 用于范围检查的最小输出值 []（默认）| 标量
  group: 信号属性
  block_parameter: OutMin
  values: '''[]''（默认）| 带引号的标量'
- name: Output maximum
  summary: 用于范围检查的最大输出值 []（默认）| 标量
  group: 信号属性
  block_parameter: OutMax
  values: '''[]''（默认）| 带引号的标量'
- name: Output data type
  summary: '指定输出数据类型 double（默认）| Inherit: Inherit via back propagation | single | int8 | int32 | uint32 | int64 | uint64 |
    fixdt(1,16,2^0,0) | <data type expression> | ...'
  group: 信号属性
  block_parameter: OutDataTypeStr
  type: 字符向量
  values: '''Inherit: Inherit via back propagation'' | ''double'' | ''single'' | ''int8'' | ''uint8'' | int16 | ''uint16''
    | ''int32'' | ''uint32'' | ''int64'' | ''uint64'' | fixdt(1,16,0) | fixdt(1,16,2^0,0) | fixdt(1,16,2^0,0). ''<data type
    expression>'''
  default: '''double'''
- name: Lock output data type setting against changes by the fixed-point tools
  summary: 防止定点工具覆盖数据类型 off（默认）| on
  group: 信号属性
  block_parameter: LockScale
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''off'''
```

### 主要

### **Vector of output values** — 输出值向量 `[3 1 4 2 1].'`（默认）| 向量

指定输出波形的输出值向量。每个元素对应于 **Vector of time values** 参数中的时间值。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutValues` |
| **类型**：字符向量 |
| **值**：向量 |
| **默认值**：`'[3 1 4 2 1].''` |

### **Vector of time values** — 时间值向量 `[0 0.1 0.5 0.6 1].'`（默认）| 向量

指定包含时间值的列向量。时间值必须严格递增，并且该向量的大小必须与输出值向量相同。

#### 编程使用

|  |
| --- |
| **模块参数**：`TimeValues` |
| **类型**：字符向量 |
| **值**：向量 |
| **默认值**：`'[0 0.1 0.5 0.6 1].''` |

### **Lookup Method** — 输出的查找方法 `Interpolation-Use End Values`（默认）| `Use Input Nearest` | `Use Input Below` | `Use Input Above`

指定查找方法以确定数据点之间的输出。

#### 编程使用

|  |
| --- |
| **模块参数**：`LookUpMeth` |
| **类型**：字符向量 |
| **值**：`'Interpolation-Use End Values'` | `'Use Input Nearest'` | `'Use Input Below'` | `'Use Input Above'` |
| **默认值**：`'Interpolation-Use End Values'` |

### **Sample time** — 采样之间的时间间隔 `0.01`（默认）| 标量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅 Specify Sample Time。

#### 编程使用

|  |
| --- |
| **模块参数**：`tsamp` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'0.01'` |

### 信号属性

### **Output minimum** — 用于范围检查的最小输出值 `[]`（默认）| 标量

软件检查的输出范围的下限值。

软件使用最小值执行以下操作：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）。
- 仿真范围检查（请参阅 Specify Signal Ranges 和 Enable Simulation Range Checking）。
- 定点数据类型的自动定标。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output minimum** 不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMin` |
| **值：** | `'[]'`（默认）| 带引号的标量 |

### **Output maximum** — 用于范围检查的最大输出值 `[]`（默认）| 标量

软件检查的输出范围的上限值。

软件使用最大值执行以下操作：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）。
- 仿真范围检查（请参阅 Specify Signal Ranges 和 Enable Simulation Range Checking）。
- 定点数据类型的自动定标。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output maximum** 不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMax` |
| **值：** | `'[]'`（默认）| 带引号的标量 |

### **Output data type** — 指定输出数据类型 `double`（默认）| `Inherit: Inherit via back propagation` | `single` | `int8` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,2^0,0)` | `<data type expression>` | ...

选择输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `int16` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `fixdt(1,16,2^0,0)`. `'<data type expression>'` |
| **默认值**：`'double'` |

### **Lock output data type setting against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此项以锁定此模块的输出数据类型设置，防止 Fixed-Point Tool 和 Fixed-Point Advisor 对其进行更改。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程使用

|  |
| --- |
| **模块参数**：`LockScale` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |
## 所属库

Simulink / Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

不能在触发子系统层次结构内使用。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

输出离散时间序列并重复，在数据点之间进行插值

Repeating Sequence Interpolated 模块基于 **Vector of time values** 和 **Vector of output values** 参数中的值输出周期性离散时间序列。在数据点之间，该模块使用您为 **Lookup Method** 参数指定的方法来确定输出。
