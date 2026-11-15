---
type: simulink-block
title: 'Switch'
family: signal-routing
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'switch'
---

# Switch

Switch output between first input and third input based on value of second input

## 中文

基于第二个输入的值在第一个输入和第三个输入之间切换输出

### 所属库

Simulink / Commonly Used Blocks Simulink / Signal Routing HDL Coder / Commonly Used Blocks HDL Coder / Signal Routing

### 描述

#### 模块输入的类型

Switch 模块根据第二个输入的值，传递第一个输入或第三个输入。第一个和第三个输入称为*数据输入*。第二个输入称为*控制输入*。可以使用**首个输入传递条件**和**阈值**参数指定模块传递第一个输入的条件。

要立即将已知的输出数据类型反向传播到第一个和第三个输入端口，请将**输出数据类型**参数设置为**继承:通过内部规则继承**并选中**要求所有数据端口输入具有相同的数据类型**复选框。

**提示**

对于反向传播**继承:通过内部规则继承**，必须选择**要求所有数据端口输入具有相同的数据类型**参数。否则，模块不会自动将输出数据类型反向传播到第一个和第三个输出端口。

#### 数据输入的限制

如果您选择**允许不同数据输入大小**，则两个数据输入的大小可以不同。然而，此模块不支持可变大小输入信号。因此，在仿真期间，每个输入的大小无法更改。

如果 Switch 模块的数据输入是总线，两个总线的元素名称必须相同。使用相同的元素名称可以确保输出总线具有相同的元素名称，而不管模块选择了哪些输入总线。要确保您的模型满足此要求，请使用总线对象定义总线并将**元素名称不匹配**诊断设置为**错误**。有关详细信息，请参阅模型配置参数：连接诊断。

#### 模块图标外观

模块图标可帮助您识别**首个输入传递条件**和**阈值**而无需打开模块对话框。

有关各种模块方向的端口顺序的信息，请参阅标识旋转或翻转模块上的端口位置。

#### 布尔控制输入的模块行为

当控制输入为 `Boolean` 信号时，可使用条件和阈值的以下组合之一：

- **u2 >= 阈值**，其中阈值等于 `1`
- **u2 > 阈值**，其中阈值等于 `0`
- **u2 ~=0**

否则，Switch 模块忽略阈值，并使用布尔输入进行信号路由。如果控制输入为 `1`，该模块传递第一个输入；如果控制输入为 `0`，该模块传递第三个输入。在本例中，模块图标在编译时后会发生变化，并使用 `T` 和 `F` 分别标记第一个和第三个输入。

#### 数据类型支持

控制输入可以是 Simulink® 支持的任何数据类型，包括定点和枚举类型。控制输入不能为复数。如果控制输入为枚举，**阈值**参数必须为相同枚举类型的值。

数据输入可以是 Simulink 支持的任何数据类型。如果有任一个数据输入为枚举类型，另一个必须为相同的枚举类型。

如果输出是枚举类型，则两个数据输入必须使用与输出相同的枚举类型。

有关详细信息，请参阅 Simulink 支持的数据类型。

### 端口

#### 输入

#### **Port\_1** — 第一个数据输入信号 标量 | 向量

两个数据输入中的第一个。模块将第一个或第二个数据输入传播到输出。模块根据控制输入选择要传递的输入。使用**首个输入传递条件**和**阈值**参数指定控制输入传递第一个输入的条件。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

#### **Port\_2** — 控制输入信号 标量 | 向量

控制信号，模块用该信号来确定是将第一个还是第二个数据输入传递给输出。如果控制输入满足**首个输入传递条件**参数中设置的条件，则模块将传递第一个数据输入。否则，模块将传递第二个数据输入。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

#### **Port\_3** — 第二个数据输入信号 标量 | 向量

两个数据输入中的第二个。模块将第一个或第二个数据输入传播到输出。模块根据控制输入选择要传递的输入。使用**首个输入传递条件**和**阈值**参数指定控制输入传递第一个或第二个输入的条件。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
#### 输出

#### **Port\_1** — 输出信号 标量 | 向量

根据控制信号值从第一个或第二个输入信号传播而来的输出信号。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

### 参数

#### 常设

#### **首个输入传递条件** — 传递第一个数据输入的条件 **u2 > 阈值** (默认) | **u2 >= 阈值** | **u2~=0**

选择模块传递第一个数据输入的条件。如果控制输入满足**首个输入传递条件**参数中设置的条件，模块将传递第一个输入。否则，模块将从输入 `Port_3` 传递第二个数据输入信号。

**u2 >= 阈值**
:   检查控制输入是否大于或等于阈值。

**u2 > 阈值**
:   检查控制输入是否大于阈值。

**u2~=0**
:   检查控制输入是否非零。

    **注意**

    对于枚举数据类型，Switch 模块不支持 **u2 ~= 0** 模式。

##### 提示

当控制输入为布尔信号时，可使用条件和阈值的以下组合之一：

- **u2 >= 阈值**，其中阈值等于 1
- **u2 > 阈值**，其中阈值等于 0
- **u2~=0**

否则，Switch 模块将忽略阈值，并使用布尔值进行信号路由。如果值为 1，模块将传递第一个输入；如果值为 0，模块将传递第三个输入。MATLAB® 命令行窗口中也会显示描述此行为的警告消息。

##### 编程用法

|  |
| --- |
| **模块参数**：`Criteria` |
| **类型：**字符向量 |
| **值：**`'u2 >= Threshold'` | `'u2 > Threshold'` | `'u2 ~= 0'` |
| **默认值：**`'u2 > Threshold'` |

#### **阈值** — 条件中使用的阈值 `0` (默认) | `scalar`

指定**首个输入传递条件**中使用的阈值，该阈值用于确定模块将哪个输入传递给输出的条件。**阈值**必须大于**输出最小值**且小于**输出最大值**。

要指定非标量阈值，请使用括号。例如，以下输入是有效的：

- `[1 4 8 12]`
- `[MyColors.Red, MyColors.Blue]`

##### 依赖关系

将**首个输入传递条件**设置为 **u2 ~= 0** 将禁用此参数。

##### 编程用法

|  |
| --- |
| **模块参数**：`Threshold` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'0'` |

#### **启用过零检测** — 启用过零检测 `on` (默认) | `off`

选择此项以启用过零检测。有关详细信息，请参阅过零检测。

##### 编程用法

|  |
| --- |
| **模块参数**：`ZeroCross` |
| **类型**：字符向量 | 字符串 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |

#### 信号属性

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

#### **要求所有数据端口输入具有相同的数据类型** — 要求数据端口具有相同的数据类型 `off` (默认) | `on`

要求所有数据输入具有相同的数据类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`InputSameDT` |
| **类型：**字符向量 |
| **值：`'off'` | `'on'`** |
| **默认值：**`'off'` |

#### **输出最小值** — 范围检查的最小输出值 `[]` (默认) | 标量

软件检查的输出范围的下限值。

软件使用最小值执行下列操作：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值）。
- 仿真范围检查（请参阅指定信号范围和启用仿真范围检查）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和值进行优化 (Embedded Coder)。

##### 提示

**输出最小值**不会对实际输出信号进行饱和处理或截断。请改用 Saturation 模块。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `OutMin` |
| **值:** | `'[]'` (默认) | scalar in quotes |

#### **输出最大值** — 范围检查的最大输出值 `[]` (默认) | 标量

软件检查的输出范围的上限值。

软件使用最大值执行下列操作：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值）。
- 仿真范围检查（请参阅指定信号范围和启用仿真范围检查）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和值进行优化 (Embedded Coder)。

##### 提示

**输出最大值**不会对实际输出信号进行饱和处理或截断。请改用 Saturation 模块。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `OutMax` |
| **值:** | `'[]'` (默认) | scalar in quotes |

#### **输出数据类型** — 输出数据类型 **继承: 从内部规则继承** (默认) | **继承: 通过反向传播继承** | **继承: 与第一个输入相同** | **double** | **single** | **half** | **int8** | **uint8** | **int16** | **uint16** | **int32** | **uint32** | **int64** | **uint64** | **fixdt(1,16)** | **fixdt(1,16,0)** | **fixdt(1,16,2^0,0)** | **字符串** | **Enum: <class name>** | **<数据类型表达式>** | **Simulink.ImageType(480,640,3)**

指定输出数据类型。

**继承: 从内部规则继承**
:   使用以下规则确定输出数据类型。

    | 第一个输入端口的数据类型 | 输出数据类型 |
    | --- | --- |
    | 大于第三个输入端口的正数范围 | 从第一个输入端口继承 |
    | 等于第三个输入端口的正数范围 | 从第三个输入端口继承 |
    | 具有比第三个输入端口更小的正数范围 |
    | 是布尔值，第三个输入端口是 `uint8` |
    | 是 `uint8`，第三个输入端口是布尔值 |
    | 是布尔值，另一个是 `int8` | 设置为布尔值 |
    | 是 `uint8`，另一个是布尔值 |

    | 两个输入端口的数据类型 | 输出数据类型 |
    | --- | --- |
    | 一个输入类型为布尔值，另一个是 `uint8` | 设置为第三个数据端口的数据类型 |
    | 一个输入是布尔值，另一个是 `int8` | 设置为布尔值 |

**继承: 通过反向传播继承**
:   根据输出模块采用数据类型。

**继承:与第一个输入相同**
:   使用第一个数据输入端口的数据类型。

**double**
:   指定输出数据类型为 `double`。

**single**
:   指定输出数据类型为 `single`。

**half**
:   指定输出数据类型为 `half`。

**int8**
:   指定输出数据类型为 `int8`。

**uint8**
:   指定输出数据类型为 `uint8`。

**int16**
:   指定输出数据类型为 `int16`。

**uint16**
:   指定输出数据类型为 `uint16`。

**int32**
:   指定输出数据类型为 `int32`。

**uint32**
:   指定输出数据类型为 `uint32`。

**int64**
:   指定输出数据类型为 `int64`。

**uint64**
:   指定输出数据类型为 `uint64`。

**fixdt(1,16,0)**
:   指定输出数据类型为定点 `fixdt(1,16,0)`。

**fixdt(1,16,2^0,0)**
:   指定输出数据类型为定点 `fixdt(1,16,2^0,0)`。

**Enum: <class name>**
:   使用枚举数据类型，例如 `Enum: BasicColors`。

**Simulink.ImageType(480,640,3)**
:   如果您有 Computer Vision Toolbox™，请使用 `Simulink.ImageType` (Computer Vision Toolbox) 对象。

**字符串**
:   指定输出数据类型为字符串。

**<数据类型表达式>**
:   使用数据类型对象，例如 **Simulink.NumericType**。

##### 提示

如果输出是枚举类型，则两个数据输入必须使用与输出相同的枚举类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: Inherit via internal rule` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'`  | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'`, `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `Enum: <class name>` | `Simulink.ImageType(480,640,3)` | `'string'` | `'<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

#### **锁定数据类型设置以防止被定点工具更改** — 防止定点工具覆盖数据类型 `off` (默认) | `on`

选择此参数可防止定点工具覆盖您对此模块指定的数据类型。有关详细信息，请参阅Lock the Output Data Type Setting (Fixed-Point Designer)。

##### 编程用法

|  |
| --- |
| **模块参数**：`LockScale` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

#### **整数舍入模式** — 指定定点运算的舍入模式 **向下** (默认) | **向上** | **收敛** | **最邻近值** | **舍入** | **最简** | **零**

选择下列舍入模式之一。

**向上**
:   将正值和负值朝正无穷方向舍入。等同于 MATLAB `ceil` 函数。

**收敛**
:   将数值舍入到最邻近的可表示值。如果出现结值，则舍入到最邻近的偶数整数。等同于 Fixed-Point Designer™ `convergent` 函数。

**向下**
:   将正值和负值朝负无穷方向舍入。等同于 MATLAB `floor` 函数。

**最邻近值**
:   将数值舍入到最邻近的可表示值。如果出现结值，则朝正无穷方向舍入。等同于 Fixed-Point Designer `nearest` 函数。

**舍入**
:   将数值舍入到最邻近的可表示值。如果出现结值，则将正数朝正无穷方向舍入，将负数朝负无穷方向舍入。等同于 Fixed-Point Designer `round` 函数。

**最简**
:   自动选择是向负无穷大方向舍入还是向零舍入，以生成尽可能有效的舍入代码。

**零**
:   将数值向零舍入。等同于 MATLAB `fix` 函数。

##### 编程用法

|  |
| --- |
| **模块参数**：`RndMeth` |
| **类型**：字符向量 |
| **值**：`'Ceiling'` | `'Convergent'` | `'Floor'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |
| **默认值**：`'Floor'` |

##### 另请参阅

有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

#### **对整数溢出进行饱和处理** — 溢出操作的方法 `off` (默认) | `on`

指定对溢出是进行饱和处理还是绕回处理。

- `on` - 将溢出饱和处理为数据类型能够表示的最小值或最大值。
- `off` - 溢出将绕回到数据类型可以表示的合适值。

例如，有符号 8 位整数 `int8` 可以表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。

- 选择此参数后，模块输出将在达到 127 时饱和。类似地，模块输出将在达到最小输出值 -128 时饱和。
- 清除此参数后，软件会将导致溢出的值解释为 `int8`，这可能产生意外结果。例如，以 `int8` 表示的模块结果 130（二进制 1000 0010）为 -126。

##### 提示

- 如果您的模型存在可能的溢出，而您希望在生成的代码中进行显式饱和保护，请考虑选中此参数。
- 如果您希望优化生成的代码的效率，请考虑清除此参数。清除此参数还可以帮助您避免过度地指定信号超出范围时模块的处理方式。有关详细信息，请参阅信号范围错误故障排除。
- 如果选中此参数，饱和将应用于模块中的每个内部操作，而不仅仅应用于输出或结果。
- 一般情况下，代码生成进程可以检测到何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `SaturateOnIntegerOverflow` |
| **值:** | `'off'` (默认) | `'on'` |

#### **允许不同数据输入大小** — 允许不同数据输入大小 `off` (默认) | `on`

选中此复选框将允许输入信号具有不同大小。模块将输入信号大小传播到输出信号。如果两个数据输入都是可变大小信号，信号的最大大小可以相同，也可以不相同。

##### 编程用法

|  |
| --- |
| **模块参数**：`AllowDiffInputSizes` |
| **类型：**字符向量 |
| **值：**`'on'` | `'off'` |
| **默认值：**`'off'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `是` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

生成的代码在特定条件下依赖于 `memcpy` 或 `memset` 函数 (string.h)。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

**复数数据支持**

此模块支持复信号的代码生成。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Commonly Used Blocks Simulink / Signal Routing HDL Coder / Commonly Used Blocks HDL Coder / Signal Routing

## Description

### Types of Block Inputs

The Switch block passes through the first input or the third input
based on the value of the second input. The first and third inputs are called
*data inputs*. The second input is called the
*control input*. Specify the condition under which the
block passes the first input by using the **Criteria for passing first
input** and **Threshold** parameters.

To immediately back propagate a known output data type to the first and third
input ports, set the **Output data type** parameter to
`Inherit: Inherit via internal rule` and select the
**Require all data port inputs to have the same data type**
check box.

**Tip**

For back propagation `Inherit: Inherit via internal rule`, the
**Require all data port inputs to have the same data
type** parameter must be selected. Otherwise, the block does not
automatically back propagate the output data type to the first and third output
ports.

### Limitations on Data Inputs

The sizes of the two data inputs can be different if you select **Allow
different data input sizes**. However, this block does not support
variable-size input signals. Therefore, the size of each input cannot change during
simulation.

If the data inputs to the Switch block are buses, the element names
of both buses must be the same. Using the same element names ensures that the output
bus has the same element names no matter which input bus the block selects. To
ensure that your model meets this requirement, use a bus object to define the buses
and set the **Element name mismatch** diagnostic to
`error`. For more information, see Model Configuration Parameters: Connectivity Diagnostics.

### Block Icon Appearance

The block icon helps you identify **Criteria for passing first
input** and **Threshold** without having to open the
block dialog box.

For information about port order for various block orientations, see Identify Port Location on Rotated or Flipped Block.

### Block Behavior for Boolean Control Input

When the control input is a `Boolean` signal, use one of these
combinations of criteria and threshold value:

- `u2 >= Threshold`, where the threshold value
  equals `1`
- `u2 > Threshold`, where the threshold value
  equals `0`
- `u2 ~=0`

Otherwise, the Switch block ignores the threshold and uses the
Boolean input for signal routing. For a control input of `1`, the
block passes the first input, and for a control input of `0`, the
block passes the third input. In this case, the block icon changes after compile
time and uses `T` and `F` to label the first and
third inputs, respectively.

### Data Type Support

The control input can be of any data type that Simulink® supports, including fixed-point and enumerated types. The control
input cannot be complex. If the control input is enumerated, the
**Threshold** parameter must be a value of the same enumerated
type.

The data inputs can be of any data type that Simulink supports. If either data input is of an enumerated type, the other
must be of the same enumerated type.

When the output is of enumerated type, both data inputs should use the same
enumerated type as the output.

For more information, see Data Types Supported by Simulink.

## Ports

### Input

### **Port\_1** — First data input signal scalar | vector

First of two data inputs. The block propagates either the first or second data input to
the output. The block selects which input to pass based on the control
input. Specify the condition for the control input to pass the first
input using the **Criteria for passing first input**
and **Threshold** parameters.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

### **Port\_2** — Control input signal scalar | vector

Control signal the block uses to determine whether to pass the first
or second data input to the output. If the control input meets the
condition set in the **Criteria for passing first
input** parameter, then the block passes the first data
input. Otherwise, the block passes the second data input.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

### **Port\_3** — Second data input signal scalar | vector

Second of two data inputs. The block propagates either the first or second data input to
the output. The block selects which input to pass based on the control
input. Specify the condition for the control input to pass the first or
second input using the **Criteria for passing first
input** and **Threshold**
parameters.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
### Output

### **Port\_1** — Output signal scalar | vector

Output signal propagated from either the first or second input signal, based on the
control signal value.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

## Parameters

### Main

### **Criteria for passing first input** — Selection criteria to pass first data input `u2 > Threshold` (default) | `u2 >= Threshold` | `u2 ~= 0`

Select the condition under which the block passes the first data
input. If the control input meets the condition set in the
**Criteria for passing first input** parameter, the
block passes the first input. Otherwise, the block passes the second
data input signal from input `Port_3`.

`u2 >= Threshold`
:   Checks whether the control input is greater than or
    equal to the threshold value.

`u2 > Threshold`
:   Checks whether the control input is greater than the
    threshold value.

`u2 ~= 0`
:   Checks whether the control input is nonzero.

    **Note**

    The Switch block does not support
    `u2 ~= 0` mode for
    enumerated data types.

#### Tip

When the control input is a Boolean signal, use one of these
combinations of condition and threshold value:

- `u2 >= Threshold`, where the
  threshold value equals 1
- `u2 > Threshold`, where the
  threshold value equals 0
- `u2 ~= 0`

Otherwise, the Switch block ignores threshold
values and uses the Boolean value for signal routing. For a value of
1, the block passes the first input, and for a value of 0, the block
passes the third input. A warning message that describes this
behavior also appears in the MATLAB® Command Window.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Criteria` |
| **Type:** character vector |
| **Value:** `'u2 >= Threshold'` | `'u2 > Threshold'` | `'u2 ~= 0'` |
| **Default:** `'u2 > Threshold'` |

### **Threshold** — Threshold used in criteria `0` (default) | `scalar`

Assign the threshold used in the **Criteria for passing first
input** that determines which input the block passes to the
output. **Threshold** must be greater than
**Output minimum** and less than **Output
maximum**.

To specify a nonscalar threshold, use brackets. For example, the
following entries are valid:

- `[1 4 8 12]`
- `[MyColors.Red, MyColors.Blue]`

#### Dependencies

Setting **Criteria for passing first input** to `u2 ~=
0` disables this parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Threshold` |
| **Type:** character vector |
| **Value:** scalar |
| **Default:** `'0'` |

### **Enable zero-crossing detection** — Enable zero-crossing detection `on` (default) | `off`

Select to enable zero-crossing detection. For more information, see Zero-Crossing Detection.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ZeroCross` |
| **Type**: character vector | string |
| **Values**: `'off'` | `'on'` |
| **Default**: `'on'` |

### Signal Attributes

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

### **Require all data port inputs to have the same data type** — Require data ports to have the same data type `off` (default) | `on`

Require all data inputs to have the same data type.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InputSameDT` |
| **Type:** character vector |
| **Value: `'off'` | `'on'`** |
| **Default:** `'off'` |

### **Output minimum** — Minimum output value for range checking `[]` (default) | scalar

Lower value of the output range that the software checks.

The software uses the minimum to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters)
  for some blocks.
- Simulation range checking (see Specify Signal Ranges and
  Enable Simulation Range Checking).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes such as SIL or external mode. For more information, see
  Optimize using the specified minimum and maximum values (Embedded Coder).

#### Tips

**Output minimum** does not saturate or clip the actual output
signal. Use the Saturation block instead.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutMin` |
| **Values:** | `'[]'` (default) | scalar in quotes |

### **Output maximum** — Maximum output value for range checking `[]` (default) | scalar

Upper value of the output range that the software checks.

The software uses the maximum value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters)
  for some blocks.
- Simulation range checking (see Specify Signal Ranges and
  Enable Simulation Range Checking).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes such as SIL or external mode. For more information, see
  Optimize using the specified minimum and maximum values (Embedded Coder).

#### Tips

**Output maximum** does not saturate or clip the actual output
signal. Use the Saturation block instead.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutMax` |
| **Values:** | `'[]'` (default) | scalar in quotes |

### **Output data type** — Output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `string` | `Enum: <class name>` | `<data type expression>` | `Simulink.ImageType(480,640,3)`

Specify the output data type.

`Inherit: Inherit via internal rule`
:   Uses the following rules to determine the output data
    type.

    | Data Type of First Input Port | Output Data Type |
    | --- | --- |
    | Has a larger positive range than the third input port | Inherited from the first input port |
    | Has the same positive range as the third input port | Inherited from the third input port |
    | Has a smaller positive range than the third input port |
    | Is a Boolean value and third input port is `uint8` |
    | Is `uint8` and third input port is a Boolean value |
    | Is a Boolean value and other is `int8` | Set to a Boolean value |
    | Is `uint8` and other is a Boolean value |

    | Data Types of Two Input Ports | Output Data Type |
    | --- | --- |
    | Has one input type as a Boolean value and another as `uint8` | Set to data type of the third data port |
    | Has one input as a Boolean value and another as `int8` | Set to a Boolean value |

`Inherit: Inherit via back propagation`
:   Adopts the data type from the output block.

`Inherit: Inherit same as first input`
:   Uses data type of the first data input port.

`double`
:   Specifies output data type is
    `double`.

`single`
:   Specifies output data type is
    `single`.

`half`
:   Specifies output data type is
    `half`.

`int8`
:   Specifies output data type is
    `int8`.

`uint8`
:   Specifies output data type is
    `uint8`.

`int16`
:   Specifies output data type is
    `int16`.

`uint16`
:   Specifies output data type is
    `uint16`.

`int32`
:   Specifies output data type is
    `int32`.

`uint32`
:   Specifies output data type is
    `uint32`.

`int64`
:   Specifies output data type is
    `int64`.

`uint64`
:   Specifies output data type is
    `uint64`.

`fixdt(1,16,0)`
:   Specifies output data type is fixed point
    `fixdt(1,16,0)`.

`fixdt(1,16,2^0,0)`
:   Specifies output data type is fixed point
    `fixdt(1,16,2^0,0)`.

`Enum: <class name>`
:   Uses an enumerated data type, for example,
    `Enum: BasicColors`.

`Simulink.ImageType(480,640,3)`
:   Uses a `Simulink.ImageType` (Computer Vision Toolbox) object if you have
    Computer Vision Toolbox™.

`string`
:   Specifies output data type is string.

`<data type expression>`
:   Uses a data type object, for example,
    `Simulink.NumericType`.

#### Tip

When the output is of enumerated type, both data inputs should use
the same enumerated type as the output.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: Inherit via internal rule` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'`  | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'`, `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `Enum: <class name>` | `Simulink.ImageType(480,640,3)` | `'string'` | `'<data type expression>'` |
| **Default**: `'Inherit: Inherit via internal rule'` |

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data types you specify on this block. For more information, see Lock the Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LockScale` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Integer rounding mode** — Specify the rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Choose one of these rounding modes.

`Ceiling`
:   Rounds both positive and negative numbers
    toward positive infinity. Equivalent to the
    MATLAB
    `ceil` function.

`Convergent`
:   Rounds number to the nearest representable
    value. If a tie occurs, rounds to the nearest even
    integer. Equivalent to the Fixed-Point Designer™
    `convergent` function.

`Floor`
:   Rounds both positive and negative numbers
    toward negative infinity. Equivalent to the
    MATLAB
    `floor` function.

`Nearest`
:   Rounds number to the nearest representable
    value. If a tie occurs, rounds toward positive
    infinity. Equivalent to the Fixed-Point Designer
    `nearest` function.

`Round`
:   Rounds number to the nearest representable
    value. If a tie occurs, rounds positive numbers
    toward positive infinity and rounds negative
    numbers toward negative infinity. Equivalent to
    the Fixed-Point Designer
    `round` function.

`Simplest`
:   Automatically chooses between round toward
    floor and round toward zero to generate rounding
    code that is as efficient as possible.

`Zero`
:   Rounds number toward zero. Equivalent to the
    MATLAB
    `fix` function.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `RndMeth` |
| **Type**: character vector |
| **Values**: `'Ceiling'` | `'Convergent'` | `'Floor'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |
| **Default**: `'Floor'` |

#### See Also

For more information, see Rounding Modes (Fixed-Point Designer).

### **Saturate on integer overflow** — Method of overflow action `off` (default) | `on`

Specify whether overflows saturate or wrap.

- `on` — Overflows saturate to either the minimum or maximum
  value that the data type can represent.
- `off` — Overflows wrap to the appropriate value that the data
  type can represent.

For example, the maximum value that the signed 8-bit integer `int8`
can represent is 127. Any block operation result greater than this maximum value causes
overflow of the 8-bit integer.

- With this parameter selected, the block output saturates at 127.
  Similarly, the block output saturates at a minimum output value of
  -128.
- With this parameter cleared, the software interprets the overflow-causing
  value as `int8`, which can produce an unintended result.
  For example, a block result of 130 (binary 1000 0010) expressed as
  `int8` is -126.

#### Tips

- Consider selecting this parameter when your model has a possible overflow
  and you want explicit saturation protection in the generated code.
- Consider clearing this parameter when you want to optimize efficiency of
  your generated code. Clearing this parameter also helps you to avoid
  overspecifying how a block handles out-of-range signals. For more
  information, see Troubleshoot Signal Range Errors.
- When you select this parameter, saturation applies to every internal
  operation on the block, not just the output or result.
- In general, the code generation process can detect when overflow is not
  possible. In this case, the code generator does not produce saturation
  code.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SaturateOnIntegerOverflow` |
| **Values:** | `'off'` (default) | `'on'` |

### **Allow different data input sizes** — Allow different data input sizes `off` (default) | `on`

Select this check box to allow input signals with different sizes. The
block propagates the input signal size to the output signal. If the two
data inputs are variable-size signals, the maximum size of the signals
can be equal or different.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AllowDiffInputSizes` |
| **Type:** character vector |
| **Value:** `'on'` | `'off'` |
| **Default:** `'off'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on `memcpy` or `memset`
functions (string.h) under certain conditions.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Complex Data Support**

This block supports code generation for complex signals.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
