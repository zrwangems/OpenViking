---
type: simulink-block
title: 'Switch'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Commonly Used Blocks'
documentation_page: 'switch'
documentation_source_path: '../simulink/slref/switch.html'
language: zh-CN
chinese_source: worker-translation
---

# Switch

## 端口

### 输入

### **Port\_1** — 第一个数据输入信号 标量 | 向量

两个数据输入中的第一个。该模块将第一个或第二个数据输入传播到输出。该模块根据控制输入选择传递哪个输入。使用 **Criteria for passing first input** 和 **Threshold** 参数指定控制输入传递第一个输入的条件。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

### **Port\_2** — 控制输入信号 标量 | 向量

该模块用于确定将第一个还是第二个数据输入传递到输出的控制信号。如果控制输入满足 **Criteria for passing first input** 参数中设置的条件，则该模块传递第一个数据输入。否则，该模块传递第二个数据输入。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

### **Port\_3** — 第二个数据输入信号 标量 | 向量

两个数据输入中的第二个。该模块将第一个或第二个数据输入传播到输出。该模块根据控制输入选择传递哪个输入。使用 **Criteria for passing first input** 和 **Threshold** 参数指定控制输入传递第一个或第二个输入的条件。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

根据控制信号值，从第一个或第二个输入信号传播的输出信号。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

## 参数

### 主要

### **Criteria for passing first input** — 传递第一个数据输入的选择条件 `u2 > Threshold`（默认）| `u2 >= Threshold` | `u2 ~= 0`

选择该模块传递第一个数据输入的条件。如果控制输入满足 **Criteria for passing first input** 参数中设置的条件，则该模块传递第一个输入。否则，该模块传递来自输入 `Port_3` 的第二个数据输入信号。

`u2 >= Threshold`
:   检查控制输入是否大于或等于阈值。

`u2 > Threshold`
:   检查控制输入是否大于阈值。

`u2 ~= 0`
:   检查控制输入是否非零。

    **注意**

    Switch 模块不支持枚举数据类型的 `u2 ~= 0` 模式。

#### 提示

当控制输入为布尔信号时，使用以下条件与阈值组合之一：

- `u2 >= Threshold`，其中阈值等于 1
- `u2 > Threshold`，其中阈值等于 0
- `u2 ~= 0`

否则，Switch 模块将忽略阈值，并使用布尔值进行信号路由。对于值 1，该模块传递第一个输入；对于值 0，该模块传递第三个输入。描述此行为的警告消息也会出现在 MATLAB® 命令窗口中。

#### 编程使用

|  |
| --- |
| **模块参数**：`Criteria` |
| **类型**：character vector |
| **Value:** `'u2 >= Threshold'` | `'u2 > Threshold'` | `'u2 ~= 0'` |
| **默认值**：`'u2 > Threshold'` |

### **Threshold** — 条件中使用的阈值 `0`（默认）| `scalar`

指定 **Criteria for passing first input** 中使用的阈值，该阈值确定该模块将哪个输入传递到输出。**Threshold** 必须大于 **Output minimum** 且小于 **Output maximum**。

要指定非标量阈值，请使用方括号。例如，以下条目是有效的：

- `[1 4 8 12]`
- `[MyColors.Red, MyColors.Blue]`

#### 依赖关系

将 **Criteria for passing first input** 设置为 `u2 ~= 0` 会禁用此参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`Threshold` |
| **类型**：character vector |
| **Value:** scalar |
| **默认值**：`'0'` |

### **Enable zero-crossing detection** — 启用零交叉检测 `on`（默认）| `off`

选择以启用零交叉检测。有关详细信息，请参阅 Zero-Crossing Detection。

#### 编程使用

|  |
| --- |
| **模块参数**：`ZeroCross` |
| **类型**：character vector | string |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |

### 信号属性

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请单击 Show data type assistant 按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

### **Require all data port inputs to have the same data type** — 要求数据端口具有相同的数据类型 `off`（默认）| `on`

要求所有数据输入具有相同的数据类型。

#### 编程使用

|  |
| --- |
| **模块参数**：`InputSameDT` |
| **类型**：character vector |
| **Value: `'off'` | `'on'`** |
| **默认值**：`'off'` |

### **Output minimum** — 用于范围检查的最小输出值 `[]`（默认）| `scalar`

软件检查的输出范围的下限值。

软件使用最小值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）。
- 仿真范围检查（请参阅 Specify Signal Ranges and Enable Simulation Range Checking）。
- 定点数据类型的自动缩放。
- 优化从模型生成的代码。此优化可能会移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output minimum** 不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `OutMin` |
| **值**：| `'[]'`（默认）| 带引号的标量 |

### **Output maximum** — 用于范围检查的最大输出值 `[]`（默认）| `scalar`

软件检查的输出范围的上限值。

软件使用最大值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）。
- 仿真范围检查（请参阅 Specify Signal Ranges and Enable Simulation Range Checking）。
- 定点数据类型的自动缩放。
- 优化从模型生成的代码。此优化可能会移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output maximum** 不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `OutMax` |
| **值**：| `'[]'`（默认）| 带引号的标量 |

### **Output data type** — 输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `string` | `Enum: <class name>` | `<data type expression>` | `Simulink.ImageType(480,640,3)`

指定输出数据类型。

`Inherit: Inherit via internal rule`
:   使用以下规则确定输出数据类型。

    | 第一个输入端口的数据类型 | 输出数据类型 |
    | --- | --- |
    | 正范围大于第三个输入端口 | 继承自第一个输入端口 |
    | 正范围与第三个输入端口相同 | 继承自第三个输入端口 |
    | 正范围小于第三个输入端口 |
    | 为布尔值且第三个输入端口为 `uint8` |
    | 为 `uint8` 且第三个输入端口为布尔值 |
    | 为布尔值且另一个为 `int8` | 设置为布尔值 |
    | 为 `uint8` 且另一个为布尔值 |

    | 两个输入端口的数据类型 | 输出数据类型 |
    | --- | --- |
    | 一个输入类型为布尔值，另一个为 `uint8` | 设置为第三个数据端口的数据类型 |
    | 一个输入为布尔值，另一个为 `int8` | 设置为布尔值 |

`Inherit: Inherit via back propagation`
:   采用输出模块的数据类型。

`Inherit: Inherit same as first input`
:   使用第一个数据输入端口的数据类型。

`double`
:   指定输出数据类型为 `double`。

`single`
:   指定输出数据类型为 `single`。

`half`
:   指定输出数据类型为 `half`。

`int8`
:   指定输出数据类型为 `int8`。

`uint8`
:   指定输出数据类型为 `uint8`。

`int16`
:   指定输出数据类型为 `int16`。

`uint16`
:   指定输出数据类型为 `uint16`。

`int32`
:   指定输出数据类型为 `int32`。

`uint32`
:   指定输出数据类型为 `uint32`。

`int64`
:   指定输出数据类型为 `int64`。

`uint64`
:   指定输出数据类型为 `uint64`。

`fixdt(1,16,0)`
:   指定输出数据类型为定点 `fixdt(1,16,0)`。

`fixdt(1,16,2^0,0)`
:   指定输出数据类型为定点 `fixdt(1,16,2^0,0)`。

`Enum: <class name>`
:   使用枚举数据类型，例如 `Enum: BasicColors`。

`Simulink.ImageType(480,640,3)`
:   如果您有 Computer Vision Toolbox™，则使用 `Simulink.ImageType` (Computer Vision Toolbox) 对象。

`string`
:   指定输出数据类型为 string。

`<data type expression>`
:   使用数据类型对象，例如 `Simulink.NumericType`。

#### 提示

当输出为枚举类型时，两个数据输入都应使用与输出相同的枚举类型。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Inherit via internal rule` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'`  | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'`, `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `Enum: <class name>` | `Simulink.ImageType(480,640,3)` | `'string'` | `'<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此参数以防止定点工具覆盖您在此模块上指定的数据类型。有关详细信息，请参阅 Lock the Output Data Type Setting (Fixed-Point Designer)。

#### 编程使用

|  |
| --- |
| **模块参数**：`LockScale` |
| **类型**：character vector |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |

### **Integer rounding mode** — 指定定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

选择以下舍入模式之一。

`Ceiling`
:   将正数和负数都向正无穷方向舍入。等效于 MATLAB `ceil` 函数。

`Convergent`
:   将数字舍入到最接近的可表示值。如果出现平局，则舍入到最接近的偶数整数。等效于 Fixed-Point Designer™ `convergent` 函数。

`Floor`
:   将正数和负数都向负无穷方向舍入。等效于 MATLAB `floor` 函数。

`Nearest`
:   将数字舍入到最接近的可表示值。如果出现平局，则向正无穷方向舍入。等效于 Fixed-Point Designer `nearest` 函数。

`Round`
:   将数字舍入到最接近的可表示值。如果出现平局，则将正数向正无穷方向舍入，将负数向负无穷方向舍入。等效于 Fixed-Point Designer `round` 函数。

`Simplest`
:   自动在向 floor 舍入和向零舍入之间选择，以生成尽可能高效的舍入代码。

`Zero`
:   将数字向零舍入。等效于 MATLAB `fix` 函数。

#### 编程使用

|  |
| --- |
| **模块参数**：`RndMeth` |
| **类型**：character vector |
| **值**：`'Ceiling'` | `'Convergent'` | `'Floor'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |
| **默认值**：`'Floor'` |

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

- 当您的模型可能发生溢出并且您希望在生成的代码中显式提供饱和保护时，请考虑选择此参数。
- 当您希望优化生成代码的效率时，请考虑清除此参数。清除此参数还有助于避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅 Troubleshoot Signal Range Errors。
- 选择此参数时，饱和应用于模块上的每个内部运算，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SaturateOnIntegerOverflow` |
| **值**：| `'off'`（默认）| `'on'` |

### **Allow different data input sizes** — 允许不同的数据输入大小 `off`（默认）| `on`

选中此复选框以允许具有不同大小的输入信号。该模块将输入信号大小传播到输出信号。如果两个数据输入是可变大小信号，则信号的最大大小可以相等或不同。

#### 编程使用

|  |
| --- |
| **模块参数**：`AllowDiffInputSizes` |
| **类型**：character vector |
| **Value:** `'on'` | `'off'` |
| **默认值**：`'off'` |

## 所属库

Simulink / Commonly Used Blocks Simulink / Signal Routing HDL Coder / Commonly Used Blocks HDL Coder / Signal Routing

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖 `memcpy` 或 `memset` 函数（string.h）。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**复数数据支持**

此模块支持复数信号的代码生成。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

根据第二个输入的值在第一个输入和第三个输入之间切换输出

### 模块输入类型

Switch 模块根据第二个输入的值传递第一个输入或第三个输入。第一个和第三个输入称为*数据输入*。第二个输入称为*控制输入*。使用 **Criteria for passing first input** 和 **Threshold** 参数指定模块传递第一个输入的条件。

要立即将已知输出数据类型反向传播到第一个和第三个输入端口，请将 **Output data type** 参数设置为 `Inherit: Inherit via internal rule`，并选中 **Require all data port inputs to have the same data type** 复选框。

**提示**

对于反向传播 `Inherit: Inherit via internal rule`，必须选中 **Require all data port inputs to have the same data type** 参数。否则，模块不会自动将输出数据类型反向传播到第一个和第三个输出端口。

### 数据输入的限制

如果选中 **Allow different data input sizes**，两个数据输入的大小可以不同。但是，此模块不支持可变大小输入信号。因此，每个输入的大小在仿真期间不能更改。

如果 Switch 模块的数据输入是总线，则两个总线的元素名称必须相同。使用相同的元素名称可确保无论模块选择哪个输入总线，输出总线都具有相同的元素名称。为确保您的模型满足此要求，请使用总线对象定义总线，并将 **Element name mismatch** 诊断设置为 `error`。有关更多信息，请参阅模型配置参数：连接性诊断。

### 模块图标外观

模块图标帮助您识别 **Criteria for passing first input** 和 **Threshold**，而无需打开模块对话框。

有关各种模块方向的端口顺序信息，请参阅识别旋转或翻转模块上的端口位置。

### 布尔控制输入的模块行为

当控制输入为 `Boolean` 信号时，使用以下条件与阈值组合之一：

- `u2 >= Threshold`，其中阈值等于 `1`
- `u2 > Threshold`，其中阈值等于 `0`
- `u2 ~=0`

否则，Switch 模块忽略阈值并使用布尔输入进行信号路由。对于控制输入 `1`，模块传递第一个输入；对于控制输入 `0`，模块传递第三个输入。在这种情况下，模块图标在编译时后更改，并使用 `T` 和 `F` 分别标记第一个和第三个输入。

### 数据类型支持

控制输入可以是 Simulink® 支持的任何数据类型，包括定点类型和枚举类型。控制输入不能为复数。如果控制输入为枚举类型，则 **Threshold** 参数必须是相同枚举类型的值。

数据输入可以是 Simulink 支持的任何数据类型。如果任一数据输入为枚举类型，则另一个必须为相同的枚举类型。

当输出为枚举类型时，两个数据输入应使用与输出相同的枚举类型。

有关更多信息，请参阅 Simulink 支持的数据类型。
