---
type: simulink-block
title: 'Waveform Generator'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'waveformgenerator'
documentation_source_path: 'slref/waveformgenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Waveform Generator

## 端口
```yaml
ports:
- name: Port_1
  summary: 生成的输出信号 标量 | 向量
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    bus
```

### 输出

### **Port\_1** — 生成的输出信号 标量 | 向量

由 **Waveform Definition** 表中的条目指定的输出信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`
## 参数
```yaml
parameters:
- name: Output Signal
  summary: 输出信号 1 的波形（默认）| 整数
  group: 主
  block_parameter: SelectedSignal
  type: 字符向量
  values: 标量
  default: '''1'''
- name: Waveform Definition
  summary: 波形信号表示法 constant | gaussian(mean,variance,seed) | pulse(amplitude,trigger_time,duration) | sawtooth(amplitude,frequence,phase_offset)
    | sin(amplitude,frequence,phase_offset) | square(amplitude,frequence,phase_offset) | step(step_time,initial_value,final_value)
  group: 主
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
    | ''int32'' | ''uint32'' | ''int64'' | ''uint64'' | fixdt(1,16,0) | fixdt(1,16,2^0,0) | fixdt(1,16,2^0,0) | ''<data type
    expression>'''
  default: '''double'''
- name: Lock output data type setting against changes by the fixed-point tools
  summary: 防止定点工具覆盖数据类型 off（默认）| on
  group: 信号属性
  block_parameter: LockScale
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''off'''
- name: Integer rounding mode
  summary: 指定定点运算的舍入模式 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: 信号属性
  block_parameter: RndMeth
  type: 字符向量
  values: '''Ceiling'' | ''Convergent'' | ''Floor'' | ''Nearest'' | ''Round'' | ''Simplest'' | ''Zero'''
  default: '''Floor'''
- name: Saturate on integer overflow
  summary: 溢出操作的方法 off（默认）| on
  group: 信号属性
  block_parameter: SaturateOnIntegerOverflow
  values: '''off''（默认）| ''on'''
- name: Sample time
  summary: 采样之间的时间间隔 0.1（默认）| 标量
  group: 信号属性
  block_parameter: SampleTime
  type: 字符向量
  values: 标量
  default: '''0.1'''
```

### 主

### **Output Signal** — 输出信号 1 的波形（默认）| 整数

选择波形定义以指定输出信号。该数字对应于 **Waveform Definition** 表中的行项。您可以在仿真运行期间更改此参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`SelectedSignal` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'1'` |

### **Waveform Definition** — 波形信号表示法 constant | `gaussian(mean,variance,seed)` | `pulse(amplitude,trigger_time,duration)` | `sawtooth(amplitude,frequence,phase_offset)` | `sin(amplitude,frequence,phase_offset)` | `square(amplitude,frequence,phase_offset)` | `step(step_time,initial_value,final_value)`

在 **Waveform Definition** 表中输入信号表示法，每行一个波形定义。有关语法详细信息，请参阅算法。

### 信号属性

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请点击 Show data type assistant 按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

### **Output minimum** — 用于范围检查的最小输出值 `[]`（默认）| 标量

软件检查的输出范围的下限值。

软件使用最小值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）。
- 仿真范围检查（请参阅 Specify Signal Ranges 和 Enable Simulation Range Checking）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可能会移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output minimum** 不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter：** | `OutMin` |
| **值**：| `'[]'`（默认）| 带引号的标量 |

### **Output maximum** — 用于范围检查的最大输出值 `[]`（默认）| 标量

软件检查的输出范围的上限值。

软件使用最大值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）。
- 仿真范围检查（请参阅 Specify Signal Ranges 和 Enable Simulation Range Checking）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可能会移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output maximum** 不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter：** | `OutMax` |
| **值**：| `'[]'`（默认）| 带引号的标量 |

### **Output data type** — 指定输出数据类型 `double`（默认）| `Inherit: Inherit via back propagation` | `single` | `int8` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,2^0,0)` | `<data type expression>` | ...

选择输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `int16` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `fixdt(1,16,2^0,0)` | `'<data type expression>'` |
| **默认值**：`'double'` |

### **Lock output data type setting against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此项可锁定此模块的输出数据类型设置，防止被 Fixed-Point Tool 和 Fixed-Point Advisor 更改。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程使用

|  |
| --- |
| **模块参数**：`LockScale` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Integer rounding mode** — 指定定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

选择以下舍入模式之一。

`Ceiling`
:   将正数和负数都向正无穷方向舍入。等效于 MATLAB® 的 `ceil` 函数。

`Convergent`
:   将数字舍入到最接近的可表示值。如果出现平局，则舍入到最接近的偶数整数。等效于 Fixed-Point Designer™ 的 `convergent` 函数。

`Floor`
:   将正数和负数都向负无穷方向舍入。等效于 MATLAB 的 `floor` 函数。

`Nearest`
:   将数字舍入到最接近的可表示值。如果出现平局，则向正无穷方向舍入。等效于 Fixed-Point Designer 的 `nearest` 函数。

`Round`
:   将数字舍入到最接近的可表示值。如果出现平局，则将正数向正无穷方向舍入，将负数向负无穷方向舍入。等效于 Fixed-Point Designer 的 `round` 函数。

`Simplest`
:   自动在向 floor 舍入和向零舍入之间选择，以生成尽可能高效的舍入代码。

`Zero`
:   将数字向零方向舍入。等效于 MATLAB 的 `fix` 函数。

#### 编程使用

|  |
| --- |
| **模块参数**：`RndMeth` |
| **类型**：字符向量 |
| **值**：`'Ceiling'` | `'Convergent'` | `'Floor'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |
| **默认值**：`'Floor'` |

#### 另请参阅

有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

### **Saturate on integer overflow** — 溢出操作的方法 `off`（默认）| `on`

指定溢出时是饱和还是回绕。

- `on` — 溢出饱和到数据类型能够表示的最小值或最大值。
- `off` — 溢出回绕到数据类型能够表示的相应值。

例如，有符号 8 位整数 `int8` 能够表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。

- 选中此参数时，模块输出饱和于 127。类似地，模块输出饱和于最小输出值 -128。
- 清除此参数时，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 -126。

#### 提示

- 当您的模型可能存在溢出并且您希望在生成的代码中显式提供饱和保护时，请考虑选中此参数。
- 当您希望优化生成代码的效率时，请考虑清除此参数。清除此参数还有助于避免过度指定模块处理超出范围信号的方式。有关详细信息，请参阅 Troubleshoot Signal Range Errors。
- 选中此参数时，饱和适用于模块上的每个内部运算，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测到不可能发生溢出的情况。在这种情况下，代码生成器不会生成饱和代码。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter：** | `SaturateOnIntegerOverflow` |
| **值**：| `'off'`（默认）| `'on'` |

### **Sample time** — 采样之间的时间间隔 `0.1`（默认）| 标量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅 Specify Sample Time。

#### 编程使用

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'0.1'` |
## 所属库

Simulink / Sources

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

不建议用于生产代码。

### Fixed-Point Conversion 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2015b 中引入**

## 描述

使用信号表示法输出波形

Waveform Generator 模块根据您在 **Waveform Definition** 表中输入的信号表示法输出波形。

此模块支持以下信号表示法语法：

- 函数语法 — 按信号语法的特定顺序指定所有参数（请参阅算法）。
- 名称-值语法 — 指定可选的逗号分隔的 `Name,Value` 参数对。`Name` 是参数名称，`Value` 是对应的值。`Name` 必须出现在单引号（`' '`）内。您可以按任意顺序指定多个名称和值对参数，如 `Name1,Value1,...,NameN,ValueN`。有关详细信息，请参阅算法。

此模块支持普通、加速和快速加速模式以及快速重启。

### 支持的运算符

| 运算 | 运算符 |
| --- | --- |
| 绝对值 | `abs()` |
| 加法 | `+` |
| 除法 | `/` |
| 乘法 | `*` |
| 括号 | `()` |
| 减法 | `-` |
| 一元负号 | `-` |

Waveform 模块遵循以下运算符优先级规则：

1. `( )`
2. `+ -`（一元）
3. `* /`
4. `+ -`

### 支持的操作

Waveform Generator 模块一次输出一个信号。您可以更改此输出信号。频率和相位偏移参数以弧度表示。您还可以：

- 嵌套信号表示法，例如：

  ```
  sin('Amplitude',sin('Amplitude',1,'Frequency',1,'Phase',0),'Frequency',1,'Phase',1)
  ```
- 引用基础工作区或模型工作区中的实标量变量，例如：

  ```
  sin('Amplitude',x,'Frequency',y,'Phase',z)
  ```

  *x*、*y* 和 *z* 存在于基础工作区中。

有关波形的详细信息，请参阅算法。

要快速确定系统对不同类型输入的响应，您可以在仿真进行期间更改 Waveform Generator 模块的输出信号。
