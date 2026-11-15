---
type: simulink-block
title: 'Interval Test'
family: logic-and-bit-operations
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'intervaltest'
---

# Interval Test

Determine if signal is in specified interval

## 中文

确定信号是否在指定区间中

### 所属库

Simulink / Logic and Bit Operations

### 描述

如果输入介于**下限**和**上限**指定的值之间，Interval Test 模块将输出 true (`1`)。如果输入在这些值的范围之外，模块将输出 false (`0`)。当输入等于**下限**或**上限**时，模块的输出取决于您是选中**左半闭区间**还是**右半闭区间**复选框。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量 | 矩阵 | N 维数组

输入信号，指定为标量、向量、矩阵或 N 维数组。

##### 限制

当输入信号为枚举类型时，**上限**和**下限**值必须具有相同的枚举类型。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
#### 输出

#### **Port\_1** — 输出信号 标量 | 向量 | 矩阵 | N 维数组

指示输入值是否在指定区间内的输出信号。您可以将**输出数据类型**指定为 **boolean** 或 **uint8**。

**数据类型:** `uint8` | `Boolean`

### 参数

#### **右半闭区间** — 包含上限值 `on` (默认) | `off`

当选中此复选框时，**上限**包括在模块对其输出 true (`1`) 的区间中。

##### 编程用法

|  |
| --- |
| **模块参数**： `IntervalClosedRight` |
| **类型：**字符向量 |
| **值：**`'on' | 'off'` |
| **默认值：**`'on'` |

#### **上限** — 区间的上限 `0.5` (默认) | 标量 | 向量 | 矩阵 | N 维数组

模块对其输出 true (`1`) 的区间的上限值。

##### 编程用法

|  |
| --- |
| **模块参数**：`uplimit` |
| **类型：**字符向量 |
| **值：**标量 | 向量 | 矩阵 | N 维数组 |
| **默认值：**`'0.5'` |

#### **左半闭区间** — 包含下限值 `on` (默认) | `off`

当选中此复选框时，**下限**包括在模块对其输出 true (`1`) 的区间中。

##### 编程用法

|  |
| --- |
| **模块参数**： `IntervalClosedLeft` |
| **类型：**字符向量 |
| **值：**`'on' | 'off'` |
| **默认值：**`'on'` |

#### **下限** — 区间的下限 `-0.5` (默认) | 标量 | 向量 | 矩阵 | N 维数组

模块对其输出 true (`1`) 的区间的下限值。

##### 编程用法

|  |
| --- |
| **模块参数**：`lowlimit` |
| **类型：**字符向量 |
| **值：**标量 | 向量 | 矩阵 | N 维数组 |
| **默认值：**`'-0.5'` |

#### **输出数据类型** — 输出数据类型 **boolean** (默认) | **uint8**

将输出数据类型指定为 `boolean` 或 `uint8`。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'boolean' | 'uint8'` |
| **默认值：**`'boolean'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| **模块**（默认值） | 为子系统和子系统内的模块生成代码。 |
| **BlackBox** | 生成黑盒接口。生成的 HDL 代码仅包括子系统的输入/输出端口定义。因此，您可以在模型中使用子系统来生成与手动编写的现有 HDL 代码的接口。  子系统的黑盒接口生成类似于没有时钟信号的 Model 模块接口生成。 |
| **无 HDL** | 从生成的代码中删除子系统。您可以在仿真中使用子系统，但在 HDL 代码中将其视为“无操作”。 |

**黑盒接口自定义**

对于 **BlackBox** 架构，您可以自定义端口名称并设置外部组件接口的属性。请参阅Customize Black Box or HDL Cosimulation Interface (HDL Coder)。

**HDL 模块属性**

| 通用 | |
| --- | --- |
| **AdaptivePipelining** | 基于综合工具、目标频率和乘法器字长的自动流水线插入。默认值为 **inherit**。另请参阅AdaptivePipelining (HDL Coder)。 |
| **ClockRatePipelining** | 以较快的时钟频率而不是较慢的数据速率插入流水线寄存器。默认值为 **inherit**。另请参阅ClockRatePipelining (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **DistributedPipelining** | 流水线寄存器分配或寄存器重定时。默认值为 **inherit**。另请参阅DistributedPipelining (HDL Coder)。 |
| **DSPStyle** | 乘法器映射的综合属性。默认值为**无**。另请参阅DSPStyle (HDL Coder)。 |
| **FlattenHierarchy** | 从生成的 HDL 代码中删除子系统层次结构。默认值为 **inherit**。另请参阅FlattenHierarchy (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |
| **SharingFactor** | 要映射到单个共享资源的功能等效的资源的数量。默认值为 0。另请参阅Resource Sharing (HDL Coder)。 |
| **StreamingFactor** | 并行数据路径或向量的数量，这些路径或向量通过时间多路复用的方式变换为串行标量数据路径。默认值为 0，表示实现完全并行的数据路径。另请参阅Streaming (HDL Coder)。 |

如果此模块不是 DUT，将忽略**目标设定**选项卡中的模块属性设置。在 HDL 工作流顾问中，如果您使用 **IP 核生成**工作流，这些目标设定模块属性值将随模型一起保存。如果您使用 `hdlset_param` 指定这些目标设定模块属性值，则当您打开 HDL 工作流顾问时，系统将使用对应的值填充这些字段。

| 目标设定 | |
| --- | --- |
| **AdditionalTargetInterfaces** | 附加目标接口，指定为字符向量。  要在模型上保存此模块属性，请在 **IP 核生成**工作流的**设置目标接口**任务中，对应于您要添加更多接口的 DUT 端口，选择 **Add more...**。然后，您可以在“添加新目标接口”对话框中添加更多接口。指定接口类型、附加接口数量以及每个附加接口的唯一名称。  值：`''`（默认值）| 字符向量元胞数组  示例：`'{{'AXI4-Stream','InterfaceID','AXI4-Stream1'}}'` |
| **ProcessorFPGASynchronization** | 处理器/FPGA 同步模式，指定为字符向量。  要在模型上保存此模块属性，请在 **IP 核生成**工作流的**设置目标接口**任务中指定**处理器/FPGA 同步**。  值：`Free running`（默认值）| `Coprocessing - blocking`  示例：`'Free running'` |
| **TestPointMapping** | 要在模型上保存此模块属性，请在 **IP 核生成**工作流的**设置目标接口**任务中指定测试点端口到目标平台接口的映射。  值：`''`（默认值）| 字符向量元胞数组  示例：`'{{'TestPoint','AXI4-Lite','x"108"'}}'` |
| **TunableParameterMapping** | 要在模型上保存此模块属性，请在 **IP 核生成**工作流的**设置目标接口**任务中指定可调参数端口到目标平台接口的映射。  值：`''`（默认值）| 字符向量元胞数组  示例：`'{{'myParam','AXI4-Lite','x"108"'}}'` |
| **AXI4RegisterReadback** | 要在模型上保存此模块属性，请在 **IP 核生成**工作流的**生成 RTL 代码和 IP 核**任务中指定是否对 AXI4 从属站写寄存器启用读回。要了解详细信息，请参阅Model Design for AXI4 Slave Interface Generation (HDL Coder)。  值：`'off'`（默认值）| `'on'` |
| **AXI4SlaveIDWidth** | 要在模型上保存此模块属性，请使用 **IP 核生成**工作流的**生成 RTL 代码和 IP 核**任务中的 **AXI4 从属 ID 宽度**设置，指定要将 DUT IP 核连接到的 AXI 主设备接口的数量。要了解详细信息，请参阅Define Multiple AXI Master Interfaces in Reference Designs to Access DUT AXI4 Slave Interface (HDL Coder)。  值：`'off'`（默认值）| `'on'` |
| **RegisterInterfaceReadPipeline** | 要在模型上保存此模块属性，请使用 **IP 核生成**工作流的**生成 RTL 代码和 IP 核**任务中的**寄存器接口读取流水线**设置，指定要在读取地址解码器路径中插入的流水线阶段数。要了解详细信息，请参阅Model Design for AXI4 Slave Interface Generation (HDL Coder)。  值：`0`（默认值）| 字符向量 |
| **GenerateDefaultAXI4Slave** | 要在模型上保存此模块属性，请在 **IP 核生成**工作流的**生成 RTL 代码和 IP 核**任务中指定是否要禁用默认 AXI4 从属站接口的生成。  值：`'on'`（默认值）| `'off'` |
| **IPCoreAdditionalFiles** | 设计中黑盒的 Verilog®、SystemVerilog 或 VHDL® 文件。指定每个文件的完整路径，并用分号 (;) 分隔各文件名。  您可以在 HDL 工作流顾问的**其他源文件**字段中设置此属性。  值：`''`（默认值）| 字符向量  示例：`'C:\myprojfiles\led_blinking_file1.vhd;C:\myprojfiles\led_blinking_file2.vhd;'` |
| **IPCoreName** | IP 核名称，指定为字符向量。  您可以在 HDL 工作流顾问的 **IP 核名称**字段中设置此属性。如果将此属性设置为默认值，HDL 工作流顾问将基于 DUT 的名称构造 IP 核名称。  值：`''`（默认值）| 字符向量  示例：`'my_model_name'` |
| **IPCoreVersion** | IP 核版本号，指定为字符向量。  您可以在 HDL 工作流顾问的 **IP 核版本**字段中设置此属性。如果此属性设置为默认值，则 HDL 工作流顾问将设置 IP 核版本。  值：`''`（默认值）| 字符向量  示例：`'1.3'` |
| **IPDataCaptureBufferSize** | FPGA 数据采集缓冲区大小，指定为字符向量。当在 FPGA 上运行时，请使用 FPGA 数据采集来观察设计中的信号。  缓冲区大小的值为 128\*2^n，其中 n 是整数。默认情况下，缓冲区大小为 128 (n=0)。n 的最大值是 13，即缓冲区大小的最大值是 1048576 (=128\*2^13)。  值：`''`（默认值）| 字符向量  示例：`'1.3'` |

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Logic and Bit Operations

## Description

The Interval Test block outputs true (`1`) if the
input is between the values specified by the **Lower limit** and
**Upper limit** parameters. The block outputs false
(`0`) if the input is outside those values. The output of the block
when the input is equal to the **Lower limit** or the **Upper
limit** is determined by whether you select the **Interval closed
on left** and **Interval closed on right** check
boxes.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix | N-D array

Input signal, specified as a scalar, vector, matrix, or N-D
array.

#### Limitations

When the input signal is an enumerated type, the **Upper
limit** and **Lower limit** values
must be of the same enumerated type.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
### Output

### **Port\_1** — Output signal scalar | vector | matrix | N-D array

Output signal indicating whether the input values fall within the
specified interval. You can specify the **Output data
type** as `boolean` or
`uint8`.

**Data Types:** `uint8` | `Boolean`

## Parameters

### **Interval closed on right** — Include upper limit value `on` (default) | `off`

When you select this check box, the **Upper limit** is
included in the interval for which the block outputs true
(`1`).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `IntervalClosedRight` |
| **Type:** character vector |
| **Values:** `'on' | 'off'` |
| **Default:** `'on'` |

### **Upper limit** — Upper limit of interval `0.5` (default) | scalar | vector | matrix | N-D array

The upper limit of the interval for which the block outputs true
(`1`).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `uplimit` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix | N-D array |
| **Default:** `'0.5'` |

### **Interval closed on left** — Include lower limit value `on` (default) | `off`

When you select this check box, the **Lower limit** is
included in the interval for which the block outputs true
(`1`).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `IntervalClosedLeft` |
| **Type:** character vector |
| **Values:** `'on' | 'off'` |
| **Default:** `'on'` |

### **Lower limit** — Lower limit of interval `-0.5` (default) | scalar | vector | matrix | N-D array

The lower limit of the interval for which the block outputs true
(`1`).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `lowlimit` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix | N-D array |
| **Default:** `'-0.5'` |

### **Output data type** — Output data type `boolean` (default) | `uint8`

Specify the output data type as `boolean` or
`uint8`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutDataTypeStr` |
| **Type:** character vector |
| **Values:** `'boolean' | 'uint8'` |
| **Default:** `'boolean'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

| Architecture | Description |
| --- | --- |
| `Module` (default) | Generate code for the subsystem and the blocks within the subsystem. |
| `BlackBox` | Generate a black box interface. The generated HDL code includes only the input/output port definitions for the subsystem. Therefore, you can use a subsystem in your model to generate an interface to existing, manually written HDL code.  The black-box interface generation for subsystems is similar to the Model block interface generation without the clock signals. |
| `No HDL` | Remove the subsystem from the generated code. You can use the subsystem in simulation, however, treat it as a “no-op” in the HDL code. |

**Black Box Interface Customization**

For the `BlackBox` architecture, you
can customize port names and set attributes of the external component
interface. See Customize Black Box or HDL Cosimulation Interface (HDL Coder).

**HDL Block Properties**

| General | |
| --- | --- |
| **AdaptivePipelining** | Automatic pipeline insertion based on the synthesis tool, target frequency, and multiplier word-lengths. The default is `inherit`. See also AdaptivePipelining (HDL Coder). |
| **ClockRatePipelining** | Insert pipeline registers at a faster clock rate instead of the slower data rate. The default is `inherit`. See also ClockRatePipelining (HDL Coder). |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **DistributedPipelining** | Pipeline register distribution, or register retiming. The default is `inherit`. See also DistributedPipelining (HDL Coder). |
| **DSPStyle** | Synthesis attributes for multiplier mapping. The default is `none`. See also DSPStyle (HDL Coder). |
| **FlattenHierarchy** | Remove subsystem hierarchy from generated HDL code. The default is `inherit`. See also FlattenHierarchy (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **SharingFactor** | Number of functionally equivalent resources to map to a single shared resource. The default is 0. See also Resource Sharing (HDL Coder). |
| **StreamingFactor** | Number of parallel data paths, or vectors, that are time multiplexed to transform into serial, scalar data paths. The default is 0, which implements fully parallel data paths. See also Streaming (HDL Coder). |

If this block is not the DUT, the block property settings in the **Target
Specification** tab are ignored. In the HDL Workflow Advisor, if you use the
**IP Core Generation** workflow, these target specification block
property values are saved with the model. If you specify these target specification block
property values using `hdlset_param`, when you open HDL Workflow Advisor,
the fields are populated with the corresponding values.

| Target Specification | |
| --- | --- |
| **AdditionalTargetInterfaces** | Additional target interfaces, specified as a character vector.  To save this block property on the model, in the **Set Target Interface** task of the **IP Core Generation** workflow, corresponding to the DUT ports that you want to add more interfaces, select **Add more...**. You can then add more interfaces in the Add New Target Interfaces dialog box. Specify the type of interface, number of additional interfaces, and a unique name for each additional interface.  Values: `''` (default) | cell array of character vectors  Example: `'{{'AXI4-Stream','InterfaceID','AXI4-Stream1'}}'` |
| **ProcessorFPGASynchronization** | Processor/FPGA synchronization mode, specified as a character vector.  To save this block property on the model, specify the **Processor/FPGA Synchronization** in the **Set Target Interface** task of the **IP Core Generation** workflow.  Values: `Free running` (default) | `Coprocessing - blocking`  Example: `'Free running'` |
| **TestPointMapping** | To save this block property on the model, specify the mapping of test point ports to target platform interfaces in the **Set Target Interface** task of the **IP Core Generation** workflow.  Values: `''` (default) | cell array of character vectors  Example: `'{{'TestPoint','AXI4-Lite','x"108"'}}'` |
| **TunableParameterMapping** | To save this block property on the model, specify the mapping of tunable parameter ports to target platform interfaces in the **Set Target Interface** task of the **IP Core Generation** workflow.  Values: `''` (default) | cell array of character vectors  Example: `'{{'myParam','AXI4-Lite','x"108"'}}'` |
| **AXI4RegisterReadback** | To save this block property on the model, specify whether you want to enable readback on AXI4 subordinate write registers in the **Generate RTL Code and IP Core** task of the **IP Core Generation** workflow. To learn more, see Model Design for AXI4 Slave Interface Generation (HDL Coder).  Values: `'off'` (default) | `'on'` |
| **AXI4SlaveIDWidth** | To save this block property on the model, specify the number of AXI manager interfaces that you want to connect the DUT IP core to by using the **AXI4 Slave ID Width** setting in the **Generate RTL Code and IP Core** task of the **IP Core Generation** workflow. To learn more, see Define Multiple AXI Master Interfaces in Reference Designs to Access DUT AXI4 Slave Interface (HDL Coder).  Values: `'off'` (default) | `'on'` |
| **RegisterInterfaceReadPipeline** | To save this block property on the model, Specify the number of pipeline stages to insert in the read address decoder path by using the **Register interface read pipeline** setting in the **Generate RTL Code and IP Core** task of the **IP Core Generation** workflow. To learn more, see Model Design for AXI4 Slave Interface Generation (HDL Coder).  Values: `0` (default) | character vector |
| **GenerateDefaultAXI4Slave** | To save this block property on the model, specify whether you want to disable generation of default AXI4 subordinate interfaces in the **Generate RTL Code and IP Core** task of the **IP Core Generation** workflow.  Values: `'on'` (default) | `'off'` |
| **IPCoreAdditionalFiles** | Verilog®, SystemVerilog, or VHDL® files for black boxes in your design. Specify the full path to each file, and separate file names with a semicolon (;).  You can set this property in the HDL Workflow Advisor, in the **Additional source files** field.  Values: `''` (default) | character vector  Example: `'C:\myprojfiles\led_blinking_file1.vhd;C:\myprojfiles\led_blinking_file2.vhd;'` |
| **IPCoreName** | IP core name, specified as a character vector.  You can set this property in the HDL Workflow Advisor, in the **IP core name** field. If this property is set to the default value, the HDL Workflow Advisor constructs the IP core name based on the name of the DUT.  Values: `''` (default) | character vector  Example: `'my_model_name'` |
| **IPCoreVersion** | IP core version number, specified as a character vector.  You can set this property in the HDL Workflow Advisor, in the **IP core version** field. If this property is set to the default value, the HDL Workflow Advisor sets the IP core version.  Values: `''` (default) | character vector  Example: `'1.3'` |
| **IPDataCaptureBufferSize** | FPGA Data Capture buffer size, specified as a character vector. Use FPGA Data Capture to observe signals in a design when running on an FPGA.  The buffer size uses values that are 128\*2^n, where n is an integer. By default, the buffer size is 128 (n=0). The maximum value of n is 13, which means that the maximum value for buffer size is 1048576 (=128\*2^13).  Values: `''` (default) | character vector  Example: `'1.3'` |

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
