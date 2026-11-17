---
type: simulink-block
title: 'Saturation Dynamic'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Discontinuities'
documentation_page: 'saturationdynamic'
documentation_source_path: '../simulink/slref/saturationdynamic.html'
language: zh-CN
chinese_source: worker-translation
---

# Saturation Dynamic

## 端口
```yaml
ports:
- name: u
  summary: 输入信号 标量 | 向量
  direction: input
  data_types: double | single | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: up
  summary: 提供饱和上限的信号 标量 | 向量
  direction: input
  data_types: double | single | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: lo
  summary: 提供饱和下限的信号 标量 | 向量
  direction: input
  data_types: double | single | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: y
  summary: 输出信号 标量 | 向量
  direction: output
  data_types: double | single | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### 输入

### **u** — 输入信号 标量 | 向量

饱和算法的输入信号。

**数据类型：** `double` | `single` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **up** — 提供饱和上限的信号 标量 | 向量

提供饱和上限的动态值。当输入大于 **up** 时，输出值被限制为 **up**。

**数据类型：** `double` | `single` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **lo** — 提供饱和下限的信号 标量 | 向量

提供饱和下限的动态值。当输入小于 **lo** 时，输出值被限制为 **lo**。

**数据类型：** `double` | `single` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **y** — 输出信号 标量 | 向量

输出信号，其值为输入信号、饱和上限或饱和下限的值。

**数据类型：** `double` | `single` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## 参数
```yaml
parameters:
- name: 输出最小值
  summary: 用于范围检查的最小输出值 []（默认）| 标量
  group: ''
  block_parameter: OutMin
  values: '''[]''（默认）| 带引号的标量'
- name: 输出最大值
  summary: 用于范围检查的最大输出值 []（默认）| 标量
  group: ''
  block_parameter: OutMax
  values: '''[]''（默认）| 带引号的标量'
- name: 输出数据类型
  summary: '指定输出数据类型 Inherit: Same as second input（默认）| Inherit: Inherit via back propagation | double | single | int8 | int32
    | uint32 | int64 | uint64 | fixdt(1,16,2^0,0) | <data type expression> | ...'
  group: ''
  block_parameter: OutDataTypeStr
  type: 字符向量
  values: '''Inherit: Same as second input'' | ''Inherit: Inherit via back propagation'' | ''double'' | ''single'' | ''int8''
    | ''uint8'' | int16 | ''uint16'' | ''int32'' | ''uint32'' | ''int64'' | ''uint64'' | fixdt(1,16) | fixdt(1,16,0) | fixdt(1,16,2^0,0)
    | ''<data type expression>'''
- name: 锁定输出数据类型设置以防止被定点工具更改
  summary: 防止定点工具覆盖输出数据类型的选项 off（默认）| on
  group: ''
  block_parameter: LockScale
  values: '''off''（默认）| ''on'''
- name: 整数舍入模式
  summary: 指定定点运算的舍入模式 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: ''
  block_parameter: RndMeth
  type: 字符向量
  values: '''Ceiling'' | ''Convergent'' | ''Floor'' | ''Nearest'' | ''Round'' | ''Simplest'' | ''Zero'''
- name: 整数溢出时饱和
  summary: 溢出操作的方法 off（默认）| on
  group: ''
  block_parameter: DoSatur
  type: 字符向量
  values: '''off'' | ''on'''
```

要编辑 Saturation Dynamic 模块的参数，请双击模块图标。

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请单击“显示数据类型助手”按钮。有关详细信息，请参阅使用数据类型助手指定数据类型。

### **输出最小值** — 用于范围检查的最小输出值 `[]`（默认）| 标量

软件检查的输出范围的下限值。

软件使用最小值执行以下操作：

- 对某些模块进行参数范围检查（请参阅为模块参数指定最小值和最大值）。
- 仿真范围检查（请参阅指定信号范围并启用仿真范围检查）。
- 定点数据类型的自动定标。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

#### 提示

**输出最小值**不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMin` |
| **值：** | `'[]'`（默认）| 带引号的标量 |

### **输出最大值** — 用于范围检查的最大输出值 `[]`（默认）| 标量

软件检查的输出范围的上限值。

软件使用最大值执行以下操作：

- 对某些模块进行参数范围检查（请参阅为模块参数指定最小值和最大值）。
- 仿真范围检查（请参阅指定信号范围并启用仿真范围检查）。
- 定点数据类型的自动定标。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

#### 提示

**输出最大值**不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMax` |
| **值：** | `'[]'`（默认）| 带引号的标量 |

### **输出数据类型** — 指定输出数据类型 `Inherit: Same as second input`（默认）| `Inherit: Inherit via back propagation` | `double` | `single` | `int8` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,2^0,0)` | `<data type expression>` | ...

选择输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType` 对象）。有关详细信息，请参阅控制信号的数据类型。

#### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: Same as second input'` | `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `int16` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `'<data type expression>'` |
| **默认**：`'Inherit: Same as input'` |

### **锁定输出数据类型设置以防止被定点工具更改** — 防止定点工具覆盖输出数据类型的选项 `off`（默认）| `on`

选中此参数可防止定点工具覆盖您在模块上指定的**输出**数据类型。有关详细信息，请参阅使用锁定输出数据类型设置 (Fixed-Point Designer)。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `LockScale` |
| **值：** | `'off'`（默认）| `'on'` |

### **整数舍入模式** — 指定定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

选择以下舍入模式之一。

`Ceiling`
:   将正数和负数均向正无穷方向舍入。等效于 MATLAB® 的 `ceil` 函数。

`Convergent`
:   将数字舍入到最接近的可表示值。如果出现平局，则舍入到最接近的偶数整数。等效于 Fixed-Point Designer™ 的 `convergent` 函数。

`Floor`
:   将正数和负数均向负无穷方向舍入。等效于 MATLAB 的 `floor` 函数。

`Nearest`
:   将数字舍入到最接近的可表示值。如果出现平局，则向正无穷方向舍入。等效于 Fixed-Point Designer 的 `nearest` 函数。

`Round`
:   将数字舍入到最接近的可表示值。如果出现平局，则将正数向正无穷方向舍入，将负数向负无穷方向舍入。等效于 Fixed-Point Designer 的 `round` 函数。

`Simplest`
:   自动在向负无穷方向舍入和向零方向舍入之间选择，以生成尽可能高效的舍入代码。

`Zero`
:   将数字向零方向舍入。等效于 MATLAB 的 `fix` 函数。

#### 编程用法

|  |
| --- |
| **模块参数**：`RndMeth` |
| **类型**：字符向量 |
| **值**：`'Ceiling'` | `'Convergent'` | `'Floor'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |
| **默认**：`'Floor'` |

#### 另请参阅

有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

### **整数溢出时饱和** — 溢出操作的方法 `off`（默认）| `on`

指定溢出时是饱和还是回绕。

- `on` — 溢出饱和到数据类型可表示的最小值或最大值。
- `off` — 溢出回绕到数据类型可表示的相应值。

例如，有符号 8 位整数 `int8` 可表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。

- 选中此参数时，模块输出饱和于 127。类似地，模块输出饱和于最小输出值 -128。
- 清除此参数时，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 -126。

#### 提示

- 当您的模型可能存在溢出并且您希望在生成的代码中具有显式饱和保护时，请考虑选中此参数。
- 当您希望优化生成代码的效率时，请考虑清除此参数。清除此参数还有助于避免过度指定模块处理超出范围信号的方式。有关详细信息，请参阅排查信号范围错误。
- 选中此参数时，饱和应用于模块上的每个内部运算，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测到不可能发生溢出的情况。在这种情况下，代码生成器不会生成饱和代码。

#### 编程用法

|  |
| --- |
| **模块参数：** `DoSatur` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认：** `'off'` |
## 所属库

Simulink / Discontinuities HDL Coder / Discontinuities

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Booleana` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 不建议将此模块与布尔信号一起使用。 | |

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

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

将输入信号限制在动态饱和上限和下限值

Saturation Dynamic 模块产生的输出信号是输入信号的值，受来自输入端口 `up` 和 `lo` 的饱和值限制。

| 输入 | 输出 |
| --- | --- |
| `lo` ≤ 输入值 ≤ `up` | 输入值 |
| 输入值 < `lo` | 下限 |
| 输入值 > `up` | 上限 |
