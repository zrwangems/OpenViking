---
type: simulink-block
title: 'Pulse Generator'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Quick Insert / Sources'
documentation_page: 'pulsegenerator'
documentation_source_path: 'slref/pulsegenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Pulse Generator

## 端口
```yaml
ports:
- name: Port_1
  summary: 输出信号 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

由参数指定的生成方波脉冲信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## 参数
```yaml
parameters:
- name: Pulse type
  summary: 计算技术 Time based（默认）| Sample based
  group: ''
  block_parameter: PulseType
  type: 字符向量
  values: '''Time based'' | ''Sample based'''
  default: '''Time based'''
- name: Time (t)
  summary: 时间变量来源 Use simulation time（默认）| Use external signal
  group: ''
  block_parameter: TimeSource
  type: 字符向量
  values: '''Use simulation time'' | ''Use external signal'''
  default: '''Use simulation time'''
- name: Amplitude
  summary: 信号幅值 1（默认）| scalar
  group: ''
  block_parameter: Amplitude
  type: 字符向量
  values: 标量
  default: '''1'''
- name: Period (secs)
  summary: 脉冲周期 10（默认）| scalar
  group: ''
  block_parameter: Period
  type: 字符向量
  values: 标量
  default: '''10'''
- name: Pulse width
  summary: 占空比 5（默认）| scalar in the range [0,100]
  group: ''
  block_parameter: PulseWidth
  type: 字符向量
  values: 标量
  default: '''5'''
- name: Phase delay (secs)
  summary: 脉冲前延迟 0（默认）| scalar
  group: ''
  block_parameter: PhaseDelay
  type: 字符向量
  values: 标量
  default: '''0'''
- name: Sample time
  summary: 采样时间长度 0（默认）| scalar | 向量
  group: ''
  block_parameter: SampleTime
  type: 字符向量
  values: 标量
  default: '''1'''
- name: Interpret vector parameters as 1-D
  summary: 将向量视为一维 on（默认）| off
  group: ''
  block_parameter: VectorParams1D
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''on'''
```

### **Pulse type** — 计算技术 `Time based`（默认）| `Sample based`

此模块生成方波所采用的计算技术，可以是基于时间的或基于采样的。对话框中的某些参数会根据您选择基于时间还是基于采样而显示。

#### 编程方式使用

|  |
| --- |
| **模块参数**：`PulseType` |
| **类型**：字符向量 |
| **值**：`'Time based'` | `'Sample based'` |
| **默认值**：`'Time based'` |

### **Time (t)** — 时间变量来源 `Use simulation time`（默认）| `Use external signal`

指定是将仿真时间还是外部信号用作输出脉冲时间变量的值来源。如果指定外部来源，模块将显示一个输入端口用于连接该来源。输出脉冲的区别如下：

- `Use simulation time`：模块生成输出脉冲，其中时间变量等于仿真时间。
- `Use external signal`：模块生成输出脉冲，其中时间变量等于来自输入端口的信号值，该值可以与仿真时间不同。

#### 编程方式使用

|  |
| --- |
| **模块参数**：`TimeSource` |
| **类型**：字符向量 |
| **值**：`'Use simulation time'` | `'Use external signal'` |
| **默认值**：`'Use simulation time'` |

### **Amplitude** — 信号幅值 `1`（默认）| `scalar`

指定信号的幅值。

#### 编程方式使用

|  |
| --- |
| **模块参数**：`Amplitude` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'1'` |

### **Period (secs)** — 脉冲周期 `10`（默认）| `scalar`

如果脉冲类型为基于时间的，则以秒为单位指定脉冲周期。如果脉冲类型为基于采样的，则周期指定为采样时间的数量。

#### 编程方式使用

|  |
| --- |
| **模块参数**：`Period` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'10'` |

### **Pulse width** — 占空比 `5`（默认）| `scalar in the range [0,100]`

如果为基于时间的，则指定为信号处于开启状态的脉冲周期百分比；如果为基于采样的，则指定为采样时间的数量。

#### 编程方式使用

|  |
| --- |
| **模块参数**：`PulseWidth` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'5'` |

### **Phase delay (secs)** — 脉冲前延迟 `0`（默认）| `scalar`

如果脉冲类型为基于时间的，则以秒为单位指定生成脉冲前的延迟；如果脉冲类型为基于采样的，则指定为采样时间的数量。

#### 编程方式使用

|  |
| --- |
| **模块参数**：`PhaseDelay` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'0'` |

### **Sample time** — 采样时间长度 `0`（默认）| `scalar` | 向量

此模块的采样时间长度，以秒为单位。此参数仅在模块的脉冲类型为基于采样时显示。请参阅 Specify Sample Time。

#### 编程方式使用

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'1'` |

### **Interpret vector parameters as 1-D** — 将向量视为一维 `on`（默认）| `off`

如果 **Amplitude**、**Period**、**Pulse width** 或 **Phase delay** 参数求值为 `N` 元素的行向量或列向量，则选中此复选框以输出长度为 `N` 的向量。

- 选中此复选框时，如果任一值参数求值为 `N` 元素的行向量或列向量，则模块输出长度为 `N` 的向量。例如，模块输出维度为 `1-by-N` 或 `N-by-1` 的矩阵。
- 清除此复选框时，如果任一值参数求值为 `N` 元素的行向量或列向量，则模块不输出长度为 `N` 的向量。

有关此参数使用方式的详细信息，请参阅 Determine the Output Dimensions of Source Blocks。

#### 编程方式使用

|  |
| --- |
| **模块参数：** `VectorParams1D` |
| **类型：** 字符向量 |
| **值：** `'on' | 'off'` |
| **默认值：** `'on'` |
## 所属库

Simulink / Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

不能在触发子系统层次结构内使用。

这些模块在配置为基于采样操作时不引用绝对时间。在基于时间操作时，它们依赖于绝对时间。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

此模块支持 HDL 代码生成，需将 **Pulse type** 参数设置为 `Sample based`，并将 **Time (t)** 参数设置为 `Use simulation time`。

**限制**

将 Pulse Generator 模块连接到 DUT 端口以在模型中将其用作源模块，但确保它不放置在 DUT 子系统内。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

以固定间隔生成方波脉冲

Pulse Generator 模块以固定间隔生成方波脉冲。模块波形参数 **Amplitude**、**Pulse Width**、**Period** 和 **Phase delay** 决定输出波形的形状。下图显示了每个参数如何影响波形。

Pulse Generator 模块可以发出任何实数数据类型的标量、向量或矩阵信号。要发出标量信号，请使用标量指定波形参数。要发出向量或矩阵信号，请分别使用向量或矩阵指定波形参数。波形参数的每个元素影响输出信号的对应元素。例如，向量幅值参数的第一个元素决定向量输出脉冲第一个元素的幅值。所有波形参数在标量扩展后必须具有相同的维度。输出的数据类型与 **Amplitude** 参数的数据类型相同。

模块输出可以在基于时间或基于采样的模式下生成，由 **Pulse type** 参数决定。

### 基于时间模式

在基于时间模式下，Simulink® 仅在输出实际发生变化时计算模块输出。这种方法在仿真时间段内减少了模块输出的计算次数。通过将 **Pulse type** 参数设置为 `Time based` 来激活此模式。

该模块不支持导致恒定输出信号的基于时间配置。如果参数 **Pulse Width** 和 **Period** 满足以下任一条件，Simulink 将返回错误：

Period​\*PulseWidth100=0Period​\*PulseWidth100=Period

根据脉冲波形特性，模块输出变化之间的间隔可能不同。因此，基于时间的 Pulse Generator 模块具有可变采样时间。此类模块的采样时间颜色为棕色（有关详细信息，请参阅 View Sample Time Information）。

Simulink 无法使用固定步长求解器计算基于时间脉冲发生器的输出。如果您为包含基于时间脉冲发生器的模型指定固定步长求解器，Simulink 将为基于时间脉冲发生器计算固定采样时间。然后，基于时间的脉冲发生器将作为基于采样的进行仿真。

如果您使用固定步长求解器且 **Pulse type** 为 `Time based`，请选择步长，使得周期、相位延迟和脉冲宽度（以秒为单位）是求解器步长的整数倍。例如，假设周期为 `4` 秒，脉冲宽度为 `75%`（即 `3` 秒），相位延迟为 `1` 秒。在这种情况下，计算得到的采样时间为 `1` 秒。因此，选择固定步长为 `1` 或能整除 `1` 的数（例如 `0.25`）。为确保此设置，请在“配置参数”对话框的 **Solver** 窗格上选择 `auto`。

### 基于采样模式

在基于采样模式下，模块按您指定的固定间隔计算其输出。通过将 **Pulse type** 参数设置为 `Sample based` 来激活此模式。

基于时间模式和基于采样模式的一个重要区别是：在基于时间模式下，模块输出基于仿真时间；而在基于采样模式下，模块输出仅取决于仿真开始，与经过的仿真时间无关。

此模块在基于采样模式下支持重置语义。例如，如果 Pulse Generator 模块位于可重置子系统中并触发重置，则模块输出重置为其初始条件。
