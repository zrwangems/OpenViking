---
type: simulink-block
title: 'Relay'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Discontinuities'
documentation_page: 'relay'
documentation_source_path: '../simulink/slref/relay.html'
language: zh-CN
chinese_source: worker-translation
---

# Relay

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_1
  summary: 输出信号 标量
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
```

### 输入

### **Port\_1** — 输入信号 标量

用于打开或关闭继电器的输入信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 输出信号 标量

输出信号在由参数 **Output when on** 和 **Output when off** 确定的两个值之间切换。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
## 参数
```yaml
parameters:
- name: Switch on point
  summary: 打开继电器的输入值 'eps'（默认）| 标量
  group: ''
  block_parameter: OnSwitchValue
  type: 字符向量
  values: 标量
  default: '''eps'''
- name: Switch off point
  summary: 关闭继电器的输入值 'eps'（默认）| 标量
  group: ''
  block_parameter: OffSwitchValue
  type: 字符向量
  values: 标量
  default: '''eps'''
- name: Output when on
  summary: 继电器打开时的输出值 1（默认）| 标量
  group: ''
  block_parameter: OnOutputValue
  type: 字符向量
  values: 标量
  default: '''1'''
- name: Output when off
  summary: 继电器关闭时的输出值 0（默认）| 标量
  group: ''
  block_parameter: OffOutputValue
  type: 字符向量
  values: 标量
  default: '''0'''
- name: Input processing
  summary: 指定基于采样或基于帧的处理 Elements as channels (sample based)（默认）| Columns as channels (frame based)
  group: ''
  block_parameter: InputProcessing
  type: 字符向量
  values: '''Columns as channels (frame based)'' | ''Elements as channels (sample based)'''
  default: '''Elements as channels (sample based)'''
- name: Enable zero-crossing detection
  summary: 启用过零检测 on（默认）| off
  group: ''
  block_parameter: ZeroCross
  type: 字符向量 | 字符串
  values: '''off'' | ''on'''
  default: '''on'''
- name: Sample time (-1 for inherited)
  summary: 采样之间的时间间隔 -1（默认）| 标量 | 向量
  group: ''
  block_parameter: SampleTime
  values: '"-1"（默认）| 带引号的标量或向量'
- name: Output minimum
  summary: 用于范围检查的最小输出值 []（默认）| 标量
  group: ''
  block_parameter: OutMin
  values: '''[]''（默认）| 带引号的标量'
- name: Output maximum
  summary: 用于范围检查的最大输出值 []（默认）| 标量
  group: ''
  block_parameter: OutMax
  values: '''[]''（默认）| 带引号的标量'
- name: Output data type
  summary: '输出信号的数据类型 Inherit: All ports same datatype（默认）| Inherit: Inherit via back propagation | double | single | int8
    | int32 | uint32 | int64 | uint64 | fixdt(1,16,2^0,0) | <data type expression> | ...'
  group: ''
  block_parameter: OutDataTypeStr
  type: 字符向量
  values: '''Inherit: All ports same datatype'' | ''Inherit: Inherit via back propagation'' | ''double'' | ''single'' | ''int8''
    | ''uint8'' | int16 | ''uint16'' | ''int32'' | ''uint32'' | ''int64'' | ''uint64'' | ''boolean'' | fixdt(1,16) | fixdt(1,16,0)
    | fixdt(1,16,2^0,0) | ''Enum: <class name>'' | ''<data type expression>'''
  default: '''Inherit: All ports same datatype'''
- name: Lock data type settings against changes by the fixed-point tools
  summary: 防止定点工具覆盖数据类型 off（默认）| on
  group: ''
  block_parameter: LockScale
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''off'''
```

### **Switch on point** — 打开继电器的输入值 `'eps'`（默认）| 标量

当输入越过此阈值时，继电器打开。**Switch on point** 值必须大于或等于 **Switch off point**。指定 **Switch on point** 值大于 **Switch off point** 可模拟迟滞，而指定相等的值则模拟在该值处具有阈值的开关。

**Switch on point** 参数在离线状态下使用舍入到最近值和饱和方法转换为输入数据类型。

#### 编程用法

|  |
| --- |
| **模块参数**：`OnSwitchValue` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'eps'` |

### **Switch off point** — 关闭继电器的输入值 `'eps'`（默认）| 标量

当输入越过此阈值时，继电器关闭。**Switch off point** 的值必须小于或等于 **Switch on point**。**Switch off point** 参数在离线状态下使用舍入到最近值和饱和方法转换为输入数据类型。

#### 编程用法

|  |
| --- |
| **模块参数**：`OffSwitchValue` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'eps'` |

### **Output when on** — 继电器打开时的输出值 `1`（默认）| 标量

继电器打开时的输出值。

#### 编程用法

|  |
| --- |
| **模块参数**：`OnOutputValue` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'1'` |

### **Output when off** — 继电器关闭时的输出值 `0`（默认）| 标量

继电器关闭时的输出值。

#### 编程用法

|  |
| --- |
| **模块参数**：`OffOutputValue` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'0'` |

### **Input processing** — 指定基于采样或基于帧的处理 `Elements as channels (sample based)`（默认）| `Columns as channels (frame based)`

指定模块执行基于采样还是基于帧的处理：

- `Columns as channels (frame based)` — 将输入的每一列视为单独的通道（基于帧的处理）。

  **注意**

  基于帧的处理需要 DSP System Toolbox™ 许可证。

  有关详细信息，请参阅 Sample- and Frame-Based Concepts (DSP System Toolbox)。
- `Elements as channels (sample based)` — 将输入的每个元素视为单独的通道（基于采样的处理）。

使用 **Input processing** 指定模块执行基于采样还是基于帧的处理。有关这两种处理模式的详细信息，请参阅 Sample- and Frame-Based Concepts (DSP System Toolbox)。

#### 编程用法

|  |
| --- |
| **模块参数**：`InputProcessing` |
| **类型**：字符向量 |
| **值**：`'Columns as channels (frame based)'` | `'Elements as channels (sample based)'` |
| **默认值**：`'Elements as channels (sample based)'` |

### **Enable zero-crossing detection** — 启用过零检测 `on`（默认）| `off`

选择以启用过零检测。有关详细信息，请参阅 Zero-Crossing Detection。

#### 编程用法

|  |
| --- |
| **模块参数**：`ZeroCross` |
| **类型**：字符向量 | 字符串 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |

### **Sample time (-1 for inherited)** — 采样之间的时间间隔 `-1`（默认）| 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅 Specify Sample Time。

#### 依赖关系

仅当您将此参数设置为 `-1` 以外的值时，此参数才可见。要了解更多信息，请参阅 Blocks for Which Sample Time Is Not Recommended。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `"-1"`（默认）| 带引号的标量或向量 |

### **Output minimum** — 用于范围检查的最小输出值 `[]`（默认）| 标量

软件检查的输出范围的下限值。

软件使用最小值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）。
- 仿真范围检查（请参阅 Specify Signal Ranges and Enable Simulation Range Checking）。
- 定点数据类型的自动定标。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output minimum** 不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMin` |
| **值：** | `'[]'`（默认）| 带引号的标量 |

### **Output maximum** — 用于范围检查的最大输出值 `[]`（默认）| 标量

软件检查的输出范围的上限值。

软件使用最大值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）。
- 仿真范围检查（请参阅 Specify Signal Ranges and Enable Simulation Range Checking）。
- 定点数据类型的自动定标。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output maximum** 不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMax` |
| **值：** | `'[]'`（默认）| 带引号的标量 |

### **Output data type** — 输出信号的数据类型 `Inherit: All ports same datatype`（默认）| `Inherit: Inherit via back propagation` | `double` | `single` | `int8` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,2^0,0)` | `<data type expression>` | ...

指定输出数据类型。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via back propagation`
- 内置数据类型的名称，例如 `single`
- 数据类型对象的名称，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置 **Output data type** 参数。

有关详细信息，请参阅 Control Data Types of Signals。

#### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: All ports same datatype'` | `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `int16` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'boolean'` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `'Enum: <class name>'` | `'<data type expression>'` |
| **默认值**：`'Inherit: All ports same datatype'` |

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您在此模块上指定的数据类型。有关详细信息，请参阅 Lock the Output Data Type Setting (Fixed-Point Designer)。

#### 编程用法

|  |
| --- |
| **模块参数：** `LockScale` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |
## 所属库

Simulink / Discontinuities HDL Coder / Discontinuities

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

此模块不支持用于 HDL 代码生成的浮点数据类型。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

在两个常量之间切换输出

Relay 模块的输出在两个指定值之间切换。当继电器打开时，它会保持打开状态，直到输入降至 **Switch off point** 参数的值以下。当继电器关闭时，它会保持关闭状态，直到输入超过 **Switch on point** 参数的值。该模块接受一个输入并生成一个输出。

**注意**

当初始输入落在 **Switch off point** 和 **Switch on point** 值*之间*时，初始输出为继电器关闭时的值。
