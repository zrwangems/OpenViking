---
type: simulink-block
title: 'Synchronous Subsystem'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Subsystems'
documentation_page: 'synchronoussubsystem'
documentation_source_path: 'ref/synchronoussubsystem.html'
language: zh-CN
chinese_source: worker-translation
---

# Synchronous Subsystem

## 端口

### 输入

### **in1** — 子系统的输入信号 标量 | 向量 | 矩阵

有关子系统输入端口接受的数据类型的信息，请参阅 Inport。

有关详细信息，请参阅 Simulink 文档中的 Data Types Supported by Simulink。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **out1** — 子系统的输出信号 标量 | 向量 | 矩阵

有关子系统输出端口输出的数据类型的信息，请参阅 Outport。

有关详细信息，请参阅 Simulink 文档中的 Data Types Supported by Simulink。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **显示端口标签** — 端口标签的显示选项 `FromPortIcon` (默认) | `FromPortBlockName` | `SignalName` | `none`

选择在 Synchronous Subsystem 模块图标上如何显示端口标签。

`none`
:   不显示端口标签。

`FromPortIcon`
:   如果对应端口图标显示信号名称，则在 Subsystem 模块上显示该信号名称。否则，显示端口模块名称；如果模块名称为默认名称，则显示端口号。

`FromPortBlockName`
:   在 Subsystem 模块上显示对应端口模块的名称。

`SignalName`
:   如果连接到端口的信号已命名，则在 Subsystem 模块上显示该信号名称。否则，显示对应端口模块的名称。

#### 程序化使用

|  |
| --- |
| **参数**：`ShowPortLabels` |
| **类型**：character vector |
| **值**：`'FromPortIcon'` | `'FromPortBlockName'` | `'SignalName'` | `'none'` |
| **默认值**：`'FromPortIcon'` |

### **读/写权限** — 对子系统内容的访问级别 `ReadWrite` (默认) | `ReadOnly` | `NoReadOrWrite`

控制用户对子系统内容的访问。

#### 设置

**默认：**
`ReadWrite`

`ReadWrite`
:   启用打开和修改子系统内容。

`ReadOnly`
:   启用打开子系统，但不能修改。如果子系统位于模块库中，您可以创建并打开该子系统的链接，并且可以创建和修改该子系统的本地副本，但不能更改权限或修改原始库实例的内容。

`NoReadOrWrite`
:   禁止打开或修改子系统。如果子系统位于库中，您可以在模型中创建该子系统的链接，但不能打开、修改、更改权限或创建该子系统的本地副本。

#### 程序化使用

|  |
| --- |
| **参数**：`Permissions` |
| **类型**：character vector |
| **值**：`'ReadWrite'` | `'ReadOnly'` | `'NoReadOrWrite'` |
| **默认值**：`'ReadWrite'` |

### **错误回调函数名称** — 发生错误时要调用的函数名称 `''` (默认) | function name

输入在 Simulink 软件执行子系统期间发生错误时要调用的函数名称。

Simulink 软件向该函数传递两个参数：子系统的句柄以及指定错误类型的字符向量。如果未指定函数，则执行子系统导致错误时，Simulink 软件会显示一般错误消息。

#### 程序化使用

|  |
| --- |
| **参数**：`ErrorFcn` |
| **类型**：character vector |
| **值**：`''` | `'<function name>'` |
| **默认值**：`''` |

### **允许层次化解析** — 工作区变量名称的解析 `All` (默认) | `ExplicitOnly` | `None`

选择是否解析此子系统引用的工作区变量名称。

有关详细信息，请参阅 Symbol Resolution 和 Symbol Resolution Process。

`All`
:   解析此子系统使用的所有工作区变量名称，包括用于指定模块参数值和 Simulink 数据对象（例如 `Simulink.Signal` 对象）的名称。

`ExplicitOnly`
:   仅解析用于指定模块参数值、数据存储内存（不存在模块的位置）、信号以及标记为“必须解析”的状态的工作区变量名称。

`None`
:   不解析工作区变量名称。

#### 程序化使用

|  |
| --- |
| **参数**：`PermitHierarchicalResolution` |
| **类型**：character vector |
| **值**：`'All'` | `'ExplicitOnly'` | `'None'` |
| **默认值**：`'All'` |

### **函数打包** — 代码格式 `Auto` (默认) | `Inline` | `Nonreusable function` | `Reusable function`

选择要为原子（非虚拟）子系统生成的代码格式。

`Auto`
:   Simulink Coder™ 会根据模型中存在的子系统实例的类型和数量为您选择最佳格式。

`Inline`
:   Simulink Coder 无条件地内联该子系统。

`Nonreusable function`
:   Simulink Coder 软件会在单独的文件中显式生成单独的函数。使用此设置的子系统生成的函数可能具有参数，具体取决于 **Function interface** 参数设置。您可以使用 **Function name** 和 **File name (no extension)** 参数命名生成的函数和文件。这些函数不可重入。

`Reusable function`
:   Simulink Coder 软件生成带参数的函数，当模型包含多个子系统实例时，允许重用子系统代码。

    此选项还生成带参数的函数，允许在模型引用层级的生成代码中重用子系统代码，该层级包括跨引用模型的多个子系统实例。在这种情况下，子系统必须位于库中。

#### 程序化使用

|  |
| --- |
| **参数**：`RTWSystemCode` |
| **类型**：character vector |
| **值**：`'Auto'` | `'Inline'` | `'Nonreusable function'` | `'Reusable function'` |
| **默认值**：`'Auto'` |

## 所属库

HDL Coder / HDL Subsystems

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

实际数据类型或功能支持取决于模块实现。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| `Module` (默认) | 为子系统及子系统内的模块生成代码。 |
| `BlackBox` | 生成黑盒接口。生成的 HDL 代码仅包括子系统的输入/输出端口定义。因此，您可以在模型中使用子系统来生成与现有手写 HDL 代码的接口。子系统的黑盒接口生成类似于 Model 模块接口生成，但不包含时钟信号。 |
| `No HDL` | 从生成代码中删除该子系统。您可以在仿真中使用该子系统，但在 HDL 代码中将其视为“空操作”。 |

**黑盒接口自定义**

对于 `BlackBox` 架构，您可以自定义端口名称并设置外部组件接口的属性。请参阅 Customize Black Box or HDL Cosimulation Interface。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **AdaptivePipelining** | 基于综合工具、目标频率和乘法器字长自动插入流水线。默认值为 `inherit`。另请参阅 AdaptivePipelining。 |
| **ClockRatePipelining** | 以更快的时钟速率而不是较慢的数据速率插入流水线寄存器。默认值为 `inherit`。另请参阅 ClockRatePipelining。 |
| **ConstrainedOutputPipeline** | 通过在设计中移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline。 |
| **DistributedPipelining** | 流水线寄存器分布，或寄存器重定时。默认值为 `inherit`。另请参阅 DistributedPipelining。 |
| **DSPStyle** | 用于乘法器映射的综合属性。默认值为 `none`。另请参阅 DSPStyle。 |
| **FlattenHierarchy** | 从生成的 HDL 代码中删除子系统层级。默认值为 `inherit`。另请参阅 FlattenHierarchy。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline。 |
| **SharingFactor** | 映射到单个共享资源的函数等价资源数量。默认值为 0。另请参阅 Resource Sharing。 |
| **StreamingFactor** | 被时间复用以转换为串行标量数据路径的并行数据路径（或向量）数量。默认值为 0，这实现完全并行的数据路径。另请参阅 Streaming。 |

如果此模块不是 DUT，则 **Target Specification** 选项卡中的模块属性设置将被忽略。在 HDL Workflow Advisor 中，如果使用 **IP Core Generation** 工作流，这些目标规范模块属性值会随模型保存。如果使用 `hdlset_param` 指定这些目标规范模块属性值，则打开 HDL Workflow Advisor 时，这些字段会填充为相应值。

| Target Specification | |
| --- | --- |
| **AdditionalTargetInterfaces** | 附加目标接口，指定为字符向量。要在模型上保存此模块属性，请在 **IP Core Generation** 工作流的 **Set Target Interface** 任务中，针对要添加更多接口的 DUT 端口，选择 **Add more...**。然后，您可以在 Add New Target Interfaces 对话框中添加更多接口。指定接口类型、附加接口数量以及每个附加接口的唯一名称。值：`''`（默认）| 字符向量元胞数组 示例：`'{{'AXI4-Stream','InterfaceID','AXI4-Stream1'}}'` |
| **ProcessorFPGASynchronization** | 处理器/FPGA 同步模式，指定为字符向量。要在模型上保存此模块属性，请在 **IP Core Generation** 工作流的 **Set Target Interface** 任务中指定 **Processor/FPGA Synchronization**。值：`Free running`（默认）| `Coprocessing - blocking` 示例：`'Free running'` |
| **TestPointMapping** | 要在模型上保存此模块属性，请在 **IP Core Generation** 工作流的 **Set Target Interface** 任务中指定测试点端口到目标平台接口的映射。值：`''`（默认）| 字符向量元胞数组 示例：`'{{'TestPoint','AXI4-Lite','x"108"'}}'` |
| **TunableParameterMapping** | 要在模型上保存此模块属性，请在 **IP Core Generation** 工作流的 **Set Target Interface** 任务中指定可调参数端口到目标平台接口的映射。值：`''`（默认）| 字符向量元胞数组 示例：`'{{'myParam','AXI4-Lite','x"108"'}}'` |
| **AXI4RegisterReadback** | 要在模型上保存此模块属性，请在 **IP Core Generation** 工作流的 **Generate RTL Code and IP Core** 任务中指定是否要启用 AXI4 从属写寄存器的回读。要了解详细信息，请参阅 Model Design for AXI4 Slave Interface Generation。值：`'off'`（默认）| `'on'` |
| **AXI4SlaveIDWidth** | 要在模型上保存此模块属性，请使用 **IP Core Generation** 工作流的 **Generate RTL Code and IP Core** 任务中的 **AXI4 Slave ID Width** 设置，指定要将 DUT IP 核连接到的 AXI 管理器接口数量。要了解详细信息，请参阅 Define Multiple AXI Master Interfaces in Reference Designs to Access DUT AXI4 Slave Interface。值：`'off'`（默认）| `'on'` |
| **RegisterInterfaceReadPipeline** | 要在模型上保存此模块属性，请使用 **IP Core Generation** 工作流的 **Generate RTL Code and IP Core** 任务中的 **Register interface read pipeline** 设置，指定要在读地址解码器路径中插入的流水线级数。要了解详细信息，请参阅 Model Design for AXI4 Slave Interface Generation。值：`0`（默认）| 字符向量 |
| **GenerateDefaultAXI4Slave** | 要在模型上保存此模块属性，请在 **IP Core Generation** 工作流的 **Generate RTL Code and IP Core** 任务中指定是否要禁用默认 AXI4 从属接口的生成。值：`'on'`（默认）| `'off'` |
| **IPCoreAdditionalFiles** | 设计中黑盒的 Verilog®、SystemVerilog 或 VHDL® 文件。指定每个文件的完整路径，并使用分号 (;) 分隔文件名。您可以在 HDL Workflow Advisor 的 **Additional source files** 字段中设置此属性。值：`''`（默认）| 字符向量 示例：`'C:\myprojfiles\led_blinking_file1.vhd;C:\myprojfiles\led_blinking_file2.vhd;'` |
| **IPCoreName** | IP 核名称，指定为字符向量。您可以在 HDL Workflow Advisor 的 **IP core name** 字段中设置此属性。如果将此属性设置为默认值，HDL Workflow Advisor 将基于 DUT 的名称构造 IP 核名称。值：`''`（默认）| 字符向量 示例：`'my_model_name'` |
| **IPCoreVersion** | IP 核版本号，指定为字符向量。您可以在 HDL Workflow Advisor 的 **IP core version** 字段中设置此属性。如果将此属性设置为默认值，HDL Workflow Advisor 将设置 IP 核版本。值：`''`（默认）| 字符向量 示例：`'1.3'` |
| **IPDataCaptureBufferSize** | FPGA Data Capture 缓冲区大小，指定为字符向量。在 FPGA 上运行时，使用 FPGA Data Capture 观察设计中的信号。缓冲区大小使用 128\*2^n 的值，其中 n 是整数。默认情况下，缓冲区大小为 128 (n=0)。n 的最大值为 13，这意味着缓冲区大小的最大值为 1048576 (=128\*2^13)。值：`''`（默认）| 字符向量 示例：`'1.3'` |

**限制**

如果您的 DUT 是封装子系统，则仅当其位于模型的顶层时才能生成代码。

## 版本历史

**在 R2016a 中引入**

## 描述

表示具有同步复位和使能行为的子系统

Synchronous Subsystem 是使用 State Control 模块的 `Synchronous` 模式的子系统。如果子系统中出现 **S** 符号，则该子系统是同步的。

要创建 Synchronous Subsystem，请从 HDL Subsystems 模块库中将该模块添加到您的 Simulink® 模型中。您还可以在子系统内添加一个 State Control 模块，并将 **State control** 设置为 `Synchronous`。
