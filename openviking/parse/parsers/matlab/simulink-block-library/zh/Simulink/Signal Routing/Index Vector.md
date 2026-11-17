---
type: simulink-block
title: 'Index Vector'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'indexvector'
documentation_source_path: 'slref/indexvector.html'
language: zh-CN
chinese_source: worker-translation
---

# Index Vector

## 端口

### 输入

### **Port\_1** — 控制信号标量

控制信号，指定为标量。当控制输入不是整数值时，模块通过向零舍入将值截断为整数。

有关枚举类型控制信号的信息，请参阅 Multiport Switch 模块参考页上的 Guidelines on Setting Parameters for Enumerated Control Port。

#### 限制

- 如果控制信号是数值类型，则控制信号不能为复数。
- 如果控制信号是枚举信号，模块使用底层整数的值来选择数据端口。
- 如果底层整数不对应于数据输入，则发生错误。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **0 或 1** — 第一个数据输入标量 | 向量

第一个数据输入，指定为标量或向量。当您将 **Data port order** 设置为 `Zero-based contiguous` 时，该端口标记为 **0**；当您将 **Data port order** 设置为 `One-based contiguous` 时，该端口标记为 **1**。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus` | `enumerated` | `string`
### 输出

### **Port\_1** — 基于控制信号值选择的数据输入标量

模块根据控制信号值从输入数据向量中输出所选值。输出为标量。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### 主要

### **Data port order** — 数据输入端口的排序类型 `Zero-based contiguous`（默认）| `One-based contiguous` | `Specify indices`

指定数据输入端口的排序类型。

- `Zero-based contiguous` — 模块使用从零开始的索引对连续数据端口进行排序。这是 Index Vector 模块的默认值。
- `One-based contiguous` — 模块使用从一开始的索引对连续数据端口进行排序。这是 Multiport Switch 模块的默认值。
- `Specify indices` — 模块使用非连续索引对数据端口进行排序。此值仅支持具有两个或更多输入数据端口的配置。

#### 提示

- 当控制端口为枚举类型时，选择 `Specify indices`。
- 如果选择 `Zero-based contiguous` 或 `One-based contiguous`，请验证控制端口不是枚举类型。此配置已弃用并会产生错误。您可以对模型运行 Upgrade Advisor，将此配置的每个 Multiport Switch 模块替换为显式指定数据端口索引的模块。请参阅 Model Upgrades。
- 避免模块在仿真或代码生成中包含未使用的数据端口的情况。当控制端口为定点或内置数据类型时，请验证所有数据端口索引均可由该类型表示。否则，将发生以下模块行为：

  | 如果模块具有未使用的数据端口且数据端口顺序为： | 模块产生： |
  | --- | --- |
  | `Zero-based contiguous` 或 `One-based contiguous` | 警告 |
  | `Specify indices` | 错误 |

#### 依赖关系

选择 `Zero-based contiguous` 或 `One-based contiguous` 将启用 **Number of data ports** 参数。

选择 `Specify indices` 将启用 **Data port indices** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `DataPortOrder` |
| **类型：** 字符向量 |
| **值：** `'Zero-based contiguous' | 'One-based contiguous' | 'Specify indices'` |
| **默认值：** `'Zero-based contiguous'` |

### **Number of data ports** — 数据输入端口数量 `1`（默认）| 1 到 65536 之间的整数

指定模块的数据输入端口数量。

#### 依赖关系

要启用此参数，请将 **Data port order** 设置为 `Zero-based contiguous` 或 `One-based contiguous`。

#### 编程用法

|  |
| --- |
| **模块参数：** `Inputs` |
| **类型：** 字符向量 |
| **值：** 1 到 65536 之间的整数 |
| **默认值：** `'1'` |

### 信号属性

### **Require all data port inputs to have the same data type** — 要求所有输入具有相同的数据类型 `off`（默认）| `on`

选中此复选框可要求所有数据输入端口具有相同的数据类型。清除此复选框时，模块允许数据端口输入具有不同的数据类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `InputSameDT` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

### **Output minimum** — 用于范围检查的最小输出值 `[]`（默认）| 标量

软件检查的输出范围的下限值。

软件使用最小值执行：

- 参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）用于某些模块。
- 仿真范围检查（请参阅 Specify Signal Ranges 和 Enable Simulation Range Checking）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可能移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

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

- 参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）用于某些模块。
- 仿真范围检查（请参阅 Specify Signal Ranges 和 Enable Simulation Range Checking）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可能移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output maximum** 不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMax` |
| **值：** | `'[]'`（默认）| 带引号的标量 |

### **Output data type** — 指定输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Inherit via back propagation` | `Inherit: Same as first data input` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `string` | `Simulink.ImageType(480,640,3)` | `<data type expression>`

选择输出的数据类型。该类型可以是继承的、直接指定的，或表示为数据类型对象（如 `Simulink.NumericType`）。

当您选择继承选项时，模块的行为如下：

- `Inherit: Inherit via internal rule`—Simulink® 选择一种数据类型以平衡数值精度、性能和生成的代码大小，同时考虑嵌入式目标硬件的属性。如果您更改嵌入式目标设置，内部规则选择的数据类型可能会更改。软件并不总是能够同时优化代码效率和数值精度。如果内部规则不满足您对数值精度或性能的特定需求，请使用以下选项之一：

  - 显式指定输出数据类型。
  - 显式指定默认数据类型（如 `fixdt(1,32,16)`），然后使用 Fixed-Point Tool 为您的模型提议数据类型。有关详细信息，请参阅 `fxptdlg` (Fixed-Point Designer)。
  - 要指定您自己的继承规则，请使用 `Inherit: Inherit via back propagation`，然后使用 Data Type Propagation 模块。有关如何使用此模块的示例可在 Signal Attributes 库的 Data Type Propagation Examples 模块中找到。
- `Inherit: Inherit via back propagation` — 使用驱动模块的数据类型。
- `Inherit: Same as first data input` — 使用第一个数据输入端口的类型。

#### 编程用法

|  |
| --- |
| **模块参数**： `OutDataTypeStr` |
| **类型**： 字符向量 |
| **值**： `'Inherit: Inherit via internal rule` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'string'` | `Simulink.ImageType(480,640,3)` | `'<data type expression>'` |
| **默认值**： `'Inherit: Inherit via internal rule'` |

### **Lock output data type setting against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此项可锁定此模块的输出数据类型设置，防止 Fixed-Point Tool 和 Fixed-Point Advisor 对其进行更改。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程用法

|  |
| --- |
| **模块参数**： `LockScale` |
| **类型**： 字符向量 |
| **值**： `'off'` | `'on'` |
| **默认值**： `'off'` |

### **Integer rounding mode** — 指定定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

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
:   自动在向 floor 舍入和向零舍入之间选择，以生成尽可能高效的舍入代码。

`Zero`
:   将数字向零方向舍入。等效于 MATLAB 的 `fix` 函数。

#### 编程用法

|  |
| --- |
| **模块参数**： `RndMeth` |
| **类型**： 字符向量 |
| **值**： `'Ceiling'` | `'Convergent'` | `'Floor'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |
| **默认值**： `'Floor'` |

#### 另请参阅

有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

### **Saturate on integer overflow** — 溢出操作的方法 `off`（默认）| `on`

指定溢出是饱和还是回绕。

- `on` — 溢出饱和到数据类型可以表示的最小值或最大值。
- `off` — 溢出回绕到数据类型可以表示的适当值。

例如，有符号 8 位整数 `int8` 可以表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。

- 选中此参数时，模块输出在 127 处饱和。类似地，模块输出在最小输出值 -128 处饱和。
- 清除此参数时，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 -126。

#### 提示

- 当您的模型可能存在溢出并且您希望在生成的代码中具有显式的饱和保护时，请考虑选中此参数。
- 当您希望优化生成代码的效率时，请考虑清除此参数。清除此参数还有助于避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅 Troubleshoot Signal Range Errors。
- 当您选中此参数时，饱和适用于模块上的每个内部运算，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SaturateOnIntegerOverflow` |
| **值：** | `'off'`（默认）| `'on'` |

### **Allow different data input sizes (Results in variable-size output signal)** — 允许不同大小的输入信号 `off`（默认）| `on`

选中此复选框可允许不同大小的输入信号。

- `On` — 允许不同大小的输入信号，并将输入信号大小传播到输出信号。在此模式下，模块产生可变大小输出信号。
- `Off` — 要求所有非标量数据输入信号具有相同的大小。

#### 编程用法

|  |
| --- |
| **参数：** `AllowDiffInputSizes` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认值：** `'off'` |

## 所属库

Simulink / Signal Routing HDL Coder / Signal Routing

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

Index Vector 模块是 **Number of data ports** 设置为 1 的 Multiport Switch 模块。有关 HDL 代码生成信息，请参阅 Multiport Switch。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

根据第一个输入的值在不同输入之间切换输出

Index Vector 模块是 Multiport Switch 模块的一种特殊配置，其中您指定一个数据输入，并且控制输入从零开始。该模块的输出是输入向量中索引与控制输入匹配的元素。例如，如果输入向量为 `[18 15 17 10]`，控制输入为 `3`，则与索引 3（从零开始）匹配的元素是 10，该值成为输出值。

Index Vector 和 Multiport Switch 模块是同一模块的替代配置。

- Index Vector — 根据第一个输入的值在不同输入之间切换输出。
- Multiport Switch — 根据控制信号选择输出信号。

要将 Multiport Switch 模块配置为 Index Vector 模块，请将 **Number of data ports** 设置为 `1`，并将 **Data port order** 设置为 `Zero-based contiguous`。
