---
type: simulink-block
title: 'Multiply-Accumulate'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Code Generation from Simulink / Speed and Area Optimization / Speed Optimization'
documentation_page: 'multiplyaccumulate'
documentation_source_path: 'ref/multiplyaccumulate.html'
language: zh-CN
chinese_source: worker-translation
---

# Multiply-Accumulate

## 端口

### 输入

### **a** — 输入信号 向量 | 矩阵 | 数组 | bus

用于向模块提供输入的端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **b** — 输入信号 标量 | 向量 | 矩阵 | 数组 | bus

用于向模块提供输入的端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **c** — 偏置信号 标量 | 向量 | 矩阵 | 数组 | bus

用于向模块提供偏置信号的端口。模块将此偏置加到输入上。请确保偏置信号的数据类型与输入点积的数据类型匹配。

#### 依赖关系

要启用此端口，请将 **Source** 设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **startIn** — 累加开始控制信号 标量 | 向量 | 矩阵 | 数组 | bus

用于提供启动累加的控制信号的端口。建议您使用 `boolean` 数据类型信号作为该端口的输入。要开始从 **dataOut** 信号获取累加输出值，**startIn** 和 **validIn** 信号必须均为高。**dataOut** 信号从下一个时钟周期开始产生累加结果。

#### 依赖关系

要启用此端口，请将 **Operation Mode** 设置为 `Streaming - using Start and End Ports`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **validIn** — 有效输入控制信号 标量 | 向量 | 矩阵 | 数组 | bus

用于提供控制信号以指示输入信号对累加有效的端口。建议您使用 `boolean` 数据类型信号作为该端口的输入。要开始从 **dataOut** 信号获取累加输出值，**validIn** 和 **startIn** 信号必须均为高。**dataOut** 信号从下一个时钟周期开始产生累加结果。**validIn** 信号比 **startIn** 和 **endIn** 信号具有更高优先级。

#### 依赖关系

要启用此端口，请将 **Operation Mode** 设置为 `Streaming - using Start and End Ports` 或 `Streaming - using Number of Samples`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **endIn** — 累加结束控制信号 标量 | 向量 | 矩阵 | 数组 | bus

用于提供控制信号以指示累加结束的端口。您可以将 **startIn** 和 **endIn** 信号与 **validIn** 信号一起使用，以指示包含累加输出的帧。

#### 依赖关系

要启用此端口，请将 **Operation Mode** 设置为 `Streaming - using Start and End Ports`，然后选择 **End input and output ports**。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### 输出

### **dataOut** — 输出信号 标量 | 向量 | 矩阵 | 数组 | bus

用于从乘加运算生成输出数据的端口。默认情况下，模块使用 `Vector` 操作模式计算输入信号的点积，并加上偏置以产生结果。如果将流模式指定为 **Operation Mode**，则 **dataOut** 信号的值取决于您提供的控制信号。输出信号的数据类型与累加器的数据类型相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **startOut** — 累加开始输出控制信号 标量 | 向量 | 矩阵 | 数组 | bus

用于生成输出控制信号以指示累加开始的端口。当 **validIn** 和 **startIn** 均为高时，**startOut** 信号在下一个时钟周期变为高。**startOut** 变为高的时钟周期指示帧的开始，并且 **dataOut** 信号已开始产生有效的累加输出。

#### 依赖关系

要启用此端口，请将 **Operation Mode** 设置为 `Streaming - using Start and End Ports`，然后选择 **Start output port**。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **validOut** — 有效输出控制信号 标量 | 向量 | 矩阵 | 数组 | bus

用于生成输出控制信号以指示 **dataOut** 信号有效的端口。当 **validIn** 信号变为高时，**validOut** 信号在下一个时钟周期变为高，并指示 **dataOut** 有效。

#### 依赖关系

要启用此端口，请将 **Operation Mode** 设置为 `Streaming - using Start and End Ports`，然后选择 **Valid output port**。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **endOut** — 累加结束输出控制信号 标量 | 向量 | 矩阵 | 数组 | bus

用于生成输出控制信号以指示累加结束的端口。您可以使用 **startOut** 信号变为高与 **endOut** 信号变为高之间的时钟周期来指示包含累加输出的有效帧。

#### 依赖关系

要启用此端口，请将 **Operation Mode** 设置为 `Streaming - using Start and End Ports`，然后选择 **End input and output ports**。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **countOut** — 计数输出控制信号 标量 | 向量 | 矩阵 | 数组 | bus

用于生成输出控制信号以指示要累加的样本数的端口。此信号的值从 `1` 增加到您为 **Number of Samples** 指定的值。只要 **validIn** 信号为高，**countOut** 每个时钟周期递增 `1`。

#### 依赖关系

要启用此端口，请将 **Operation Mode** 设置为 `Streaming - using Number of Samples`，然后选择 **Count output port**。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

## 参数

### **Operation Mode** — 输入的累加模式 `'Vector'` （默认） | `'Streaming - using Start and End Ports'` | `'Streaming - using Number of Samples'`

您可以将 **Operation Mode** 指定为：

- `Vector`：您可以使用标量或向量作为输入。模块执行输入 `u1` 和 `u2` 的点积，并加上偏置 `k` 以产生结果。
- `Streaming - using Start and End Ports`：使用标量输入进行 HDL 代码生成。在此模式下，您可以使用 **startIn** 和 **endIn** 控制信号确定何时开始和停止累加。当 **validIn** 为高时，输出数据有效。
- `Streaming - using Number of Samples`：使用标量输入进行 HDL 代码生成。在此模式下，您可以指定 **Number of Samples** 并使用 **countIn** 控制信号确定何时开始和停止累加。当 **validIn** 为高时，输出数据有效。

#### 编程用法

|  |
| --- |
| **模块参数:** `opMode` |
| **类型:** 字符向量 |
| **值:** `'Vector'` | `'Streaming - using Start and End Ports'` | `'Streaming - using Number of Samples'` |
| **默认值:** `'Vector'` |

### **Bias** — 要加到输入点积的偏移量 `{'0.0'}` （默认）

您可以通过以下方式指定偏置：

- 将 **Source** 设置为 `Dialog`。然后，指定 **Value**。
- 将 **Source** 设置为 `Input port`。此设置会创建一个外部输入端口 `c`，用于将偏置信号输入到模块。

#### 编程用法

|  |
| --- |
| **模块参数:** `initValueSetting` |
| **类型:** 字符向量 |
| **值:** `'Dialog'` | `'Input port'` |
| **默认值:** `'Dialog'` |

如果将 **Source** 设置为 `Dialog`，则可以使用 `initValue2` 设置指定初始值。

|  |
| --- |
| **模块参数:** `initValue2` |
| **类型:** 字符向量 |
| **值:** 大于或等于零的整数 |
| **默认值:** `'0.0'` |

### **Number of Samples** — 有效累加输出信号的样本数 `{'2'}` （默认）

您可以指定 **Number of Samples** 来指定一个帧，其中包含有效累加输出 **dataOut** 的样本数。

#### 依赖关系

要启用此端口，请将 **Operation Mode** 设置为 `Streaming - using Number of Samples`。

#### 编程用法

|  |
| --- |
| **模块参数:** `num_samples` |
| **类型:** 字符向量 |
| **值:** 大于或等于零的整数 |
| **默认值:** `'2'` |

### **Output data type** — 模块输出的数据类型 `Inherit: Inherit via back propagation` （默认）

将输出数据类型设置为：

- 继承数据类型的规则，例如 `Inherit: Same as first input`。
- 内置数据类型，例如 `single` 或 `int16`。
- 数据类型对象的名称，例如 `Simulink.NumericType` 对象。
- 计算结果为有效数据类型的表达式，例如 `fixdt(1,16,0)`

流模式不支持 `Inherit: Inherit via internal rule`。设置 **Output data type** 时，您可以使用 **Data Type Assistant**。要显示助手，请点击 **Show data type assistant**。

#### 编程用法

|  |
| --- |
| **模块参数:** `OutDataTypeStr` |
| **类型:** 字符向量 |
| **默认值:** `{'Inherit: Inherit via internal rule'}` |

要查看可为该参数指定的可能值，请参阅 Programmatically Specify Block Parameters and Properties。

### **Integer rounding mode** — 定点运算的舍入模式 `Floor` （默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

将舍入操作指定为：

`Ceiling`
:   将正数和负数向正无穷方向舍入。等效于 MATLAB®
    `ceil` 函数。

`Convergent`
:   将数字舍入到最接近的可表示值。如果出现平局，则舍入到最接近的偶数整数。等效于 Fixed-Point Designer™
    `convergent` 函数。

`Floor`
:   将正数和负数向负无穷方向舍入。等效于 MATLAB
    `floor` 函数。

`Nearest`
:   将数字舍入到最接近的可表示值。如果出现平局，则向正无穷方向舍入。等效于 Fixed-Point Designer
    `nearest` 函数。

`Round`
:   将数字舍入到最接近的可表示值。如果出现平局，则正数向正无穷方向舍入，负数向负无穷方向舍入。等效于 Fixed-Point Designer
    `round` 函数。

`Simplest`
:   在向 floor 舍入和向零舍入之间选择，以生成尽可能高效的舍入代码。

`Zero`
:   将数字向零舍入。等效于 MATLAB
    `fix` 函数。

#### 编程用法

|  |
| --- |
| **模块参数:** `RndMeth` |
| **类型:** 字符向量 |
| **默认值:** `{'Floor'}` |

要查看可为该参数指定的可能值，请参阅 Programmatically Specify Block Parameters and Properties。

### **Valid output port** — 控制 validOut 输出端口的生成 off （默认） | on

控制 **validOut** 输出端口的生成。此端口指示 **dataOut** 是否有效。

off
:   不显示 **validOut** 输出端口。

on
:   显示 **validOut** 输出端口。

#### 依赖关系

要启用此端口，请将 **Operation Mode** 设置为 `Streaming - using Number of Samples` 或 `Streaming - using Start and End Ports`。

#### 编程用法

|  |
| --- |
| **模块参数:** `validOut` |
| **类型:** 字符向量 |
| **值:** `'off'` | `'on'` |
| **默认值:** `'off'` |

### **End input and output ports** — 控制 endIn 输入端口和 endOut 输出端口的生成 off （默认） | on

控制 **endIn** 输入端口和 **endOut** 输出端口的生成。这些端口指示包含有效累加输出的帧的结束。

off
:   不显示 **endIn** 输入端口和 **endOut** 输出端口。

on
:   显示 **endIn** 输入端口和 **endOut** 输出端口。

#### 依赖关系

要启用此端口，请将 **Operation Mode** 设置为 `Streaming - using Start and End Ports`。

#### 编程用法

|  |
| --- |
| **模块参数:** `endInandOut` |
| **类型:** 字符向量 |
| **值:** `'off'` | `'on'` |
| **默认值:** `'off'` |

### **Start output port** — 控制 startOut 输出端口的生成 off （默认） | on

控制 **startOut** 输出端口的生成。此端口生成 **startOut** 信号，用于指示包含有效累加输出的帧的开始。

off
:   不显示 **startOut** 输出端口。

on
:   显示 **startOut** 输出端口。

#### 依赖关系

要启用此端口，请将 **Operation Mode** 设置为 `Streaming - using Start and End Ports`。

#### 编程用法

|  |
| --- |
| **模块参数:** `startOut` |
| **类型:** 字符向量 |
| **值:** `'off'` | `'on'` |
| **默认值:** `'off'` |

### **Count output port** — 控制 countOut 输出端口的生成 off （默认） | on

控制 **countOut** 输出端口的生成。此端口生成计数器，用于指示包含有效样本的帧。

off
:   不显示 **countOut** 输出端口。

on
:   显示 **countOut** 输出端口。

#### 依赖关系

要启用此端口，请将 **Operation Mode** 设置为 `Streaming - using Number of Samples`。

#### 编程用法

|  |
| --- |
| **模块参数:** `countOut` |
| **类型:** 字符向量 |
| **值:** `'off'` | `'on'` |
| **默认值:** `'off'` |

## 所属库

HDL Coder / HDL Operations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL Code Generation 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供额外配置选项，这些选项会影响 HDL 实现和综合逻辑。

**HDL Architecture**

| HDL Architecture 设置 | 描述 |
| --- | --- |
| `Parallel` | 对于大小为 `N` 的输入向量，此模式使用 `N` 个 Multiply-Add 模块串联来计算结果。此模式使用组合实现，并且不引入任何延迟。如果指定 **Synthesis tool** 和 **Target frequency**，由于自适应流水线优化已启用，代码生成器会为 Multiply-Add 模块插入流水线寄存器。综合设计时，取决于输入位宽，此架构最多在 FPGA 上映射 `N` 个 DSP slices。 |
| `Serial`(Default) | 对于大小为 `N` 的输入向量，此模式使用流式算法实现乘加运算。此架构有两种实现模式：<br><br>- 默认模式使用本地多速率实现。此实现将共享资源过时钟 `N` 倍，并使用一个 Multiply-Add 模块对输入向量进行多路复用。此实现在数据速率下引入一个额外的延迟。<br>- 如果在包含 Multiply-Accumulate 模块的模型或子系统上启用了 clock-rate pipelining，则此架构使用单速率实现。此实现以时钟速率运行共享资源，并使用一个 Multiply-Add 模块对输入向量进行多路复用。此实现在时钟速率下引入 `N` 个额外的延迟。<br><br>综合设计时，取决于输入位宽，此架构映射到 FPGA 上的一个 DSP slice。 |

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中的现有延迟，在输出处放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline。 |

**复数数据支持**

使用复数信号时，此模块可以生成 HDL 代码，但不会映射到 DSP slices。

**Reset type 建议**

为使 Multiply-Accumulate 模块映射到 DSP slices，请使用以下 reset type 设置：

- 对于 Xilinx® FPGA 板，将 **Reset type** 设置为 `Synchronous`。
- 对于 Altera® FPGA 板，将 **Reset type** 设置为 `Asynchronous`。

要设置 reset type，请选择 **HDL Code Generation** > **Global settings** > **Clock settings** > **Reset type**。

**限制**

- 模块端口接口不支持矩阵数据类型。如果有矩阵类型信号，请在矩阵乘法模式下使用 Product, Matrix Multiply 模块。
- 对于 HDL 代码生成，Resettable Subsystem 模块内部不支持该模块的流式操作模式。
- 该模块不支持用于 HDL 代码生成的浮点数据类型。

## 版本历史

**在 R2017b 中引入**

## 描述

对输入执行乘加运算

Multiply-Accumulate 模块对输入 `a` 、 `b` 和偏置 `c` 执行此运算，以计算结果 `dataOut`。

    dataOut = sum(a.* b) + c

默认情况下，模块以向量模式运行。输入 `a` 和 `b` 可以是标量、向量或 2-D 矩阵。默认情况下，偏置值 `c` 等于零。模块计算输入 `a` 和 `b` 的点积。您可以通过将 **Source** 指定为 `Dialog` 或 `Input port` 来为 `c` 指定非零值。模块将此偏置加到 `a` 和 `b` 的点积上。无论 **Output data type** 设置如何，乘法运算均为全精度。**Output data type** 和 **Integer rounding mode** 设置适用于加法运算。要为该模块生成 HDL 代码，请使用向量输入。对于标量输入，请使用 Multiply-Add 模块。

通过使用 **Operation Mode** 设置，您可以为 Multiply-Accumulate 模块指定流式操作模式。对于 HDL 代码生成，当您使用流式操作模式时，必须向该模块输入标量值。该模块有两种流式模式：`Streaming - using Start and End ports` 和 `Streaming - using Number of Samples`。选择这些流式模式时，您可以指定与该模式一起使用的控制信号。控制信号指定何时开始和结束累加以及输出何时有效。
