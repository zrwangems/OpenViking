---
type: simulink-block
title: 'Enabled Synchronous Subsystem'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Code Generation from Simulink / Model and Architecture Design / Model Design / Hierarchical Designs and Synchronous Hardware Behavior'
documentation_page: 'enabledsynchronoussubsystem'
documentation_source_path: 'ref/enabledsynchronoussubsystem.html'
language: zh-CN
chinese_source: worker-translation
---

# Enabled Synchronous Subsystem

## 端口

### 输入

### **Port\_1** — 输入到子系统的信号 标量 | 向量

有关子系统输入端口接受的数据类型的信息，请参阅 Inport。

有关详细信息，请参阅 Simulink 文档中的 Simulink 支持的数据类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

有关子系统输出端口输出的数据类型的信息，请参阅 Outport。

有关详细信息，请参阅 Simulink 文档中的 Simulink 支持的数据类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **显示端口标签** — 端口标签的显示选项 `FromPortIcon`（默认）| `FromPortBlockName` | `SignalName` | `none`

选择如何在 Synchronous Subsystem 模块图标上显示端口标签。

`none`
:   不显示端口标签。

`FromPortIcon`
:   如果对应端口图标显示信号名称，则在 Subsystem 模块上显示该信号名称。否则，如果模块名称是默认名称，则显示端口模块名称或端口号。

`FromPortBlockName`
:   在 Subsystem 模块上显示对应端口模块的名称。

`SignalName`
:   如果连接到端口的信号已命名，则在 Subsystem 模块上显示该信号的名称。否则，显示对应端口模块的名称。

#### 编程用法

|  |
| --- |
| **参数**：`ShowPortLabels` |
| **类型**：character vector |
| **值**：`'FromPortIcon'` | `'FromPortBlockName'` | `'SignalName'` | `'none'` |
| **默认**：`'FromPortIcon'` |

### **读/写权限** — 对子系统内容的访问级别 `ReadWrite`（默认）| `ReadOnly` | `NoReadOrWrite`

控制用户对子系统内容的访问。

#### 设置

**默认：**
`ReadWrite`

`ReadWrite`
:   允许打开和修改子系统内容。

`ReadOnly`
:   允许打开子系统，但不允许修改。如果子系统位于模块库中，您可以创建并打开指向该子系统的链接，也可以创建和修改该子系统的本地副本，但不能更改权限或修改原始库实例的内容。

`NoReadOrWrite`
:   禁止打开或修改子系统。如果子系统位于库中，您可以在模型中创建指向该子系统的链接，但不能打开、修改、更改权限或创建该子系统的本地副本。

#### 编程用法

|  |
| --- |
| **参数**：`Permissions` |
| **类型**：character vector |
| **值**：`'ReadWrite'` | `'ReadOnly'` | `'NoReadOrWrite'` |
| **默认**：`'ReadWrite'` |

### **错误回调函数名称** — 发生错误时要调用的函数名称 `''`（默认）| 函数名称

输入一个函数的名称，当 Simulink 软件执行该子系统期间发生错误时将调用该函数。

Simulink 软件向该函数传递两个参数：子系统的句柄以及指定错误类型的 character vector。如果未指定函数，则当执行子系统导致错误时，Simulink 软件会显示一般错误消息。

#### 编程用法

|  |
| --- |
| **参数**：`ErrorFcn` |
| **类型**：character vector |
| **值**：`''` | `'<function name>'` |
| **默认**：`''` |

### **允许层次化解析** — 工作区变量名称的解析 `All`（默认）| `ExplicitOnly` | `None`

选择是否解析此子系统引用的工作区变量名称。

有关详细信息，请参阅符号解析和符号解析过程。

`All`
:   解析此子系统使用的所有工作区变量名称，包括用于指定模块参数值和 Simulink 数据对象（例如 `Simulink.Signal` 对象）的名称。

`ExplicitOnly`
:   仅解析用于指定模块参数值、数据存储内存（不存在对应模块时）、信号以及标记为“必须解析”的状态的工作区变量名称。

`None`
:   不解析工作区变量名称。

#### 编程用法

|  |
| --- |
| **参数**：`PermitHierarchicalResolution` |
| **类型**：character vector |
| **值**：`'All'` | `'ExplicitOnly'` | `'None'` |
| **默认**：`'All'` |

### **函数打包** — 代码格式 `Auto`（默认）| `Inline` | `Nonreusable function` | `Reusable function`

选择要为原子（非虚拟）子系统生成的代码格式。

`Auto`
:   Simulink
    Coder™ 会根据模型中存在的子系统类型和实例数量为您选择最佳格式。

`Inline`
:   Simulink
    Coder 无条件地内联该子系统。

`Nonreusable function`
:   Simulink
    Coder 软件显式地在单独文件中生成单独函数。采用此设置的子系统所生成的函数可能具有参数，具体取决于 **函数接口** 参数设置。您可以使用 **函数名称** 和 **文件名（无扩展名）** 参数命名生成的函数和文件。这些函数不可重入。

`Reusable function`
:   Simulink
    Coder 软件生成带参数的函数，当模型包含多个子系统实例时，允许重用子系统代码。

    此选项还会生成带参数的函数，允许在模型引用层次结构的生成代码中重用子系统代码，该层次结构跨被引用模型包含多个子系统实例。在这种情况下，子系统必须位于库中。

#### 编程用法

|  |
| --- |
| **参数**：`RTWSystemCode` |
| **类型**：character vector |
| **值**：`'Auto'` | `'Inline'` | `'Nonreusable function'` | `'Reusable function'` |
| **默认**：`'Auto'` |

## 所属库

HDL Coder / HDL Subsystems

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| `Module`（默认） | 为子系统以及子系统内的模块生成代码。 |
| `BlackBox` | 生成黑盒接口。生成的 HDL 代码仅包括子系统的输入/输出端口定义。因此，您可以在模型中使用子系统来生成与现有手写 HDL 代码的接口。子系统黑盒接口生成类似于 Model 模块接口生成，但不包含时钟信号。 |
| `No HDL` | 从生成的代码中移除该子系统。您可以在仿真中使用该子系统，但在 HDL 代码中将其视为“no-op”。 |

**黑盒接口自定义**

对于 `BlackBox` 架构，您可以自定义端口名称，并设置外部组件接口的属性。请参阅自定义黑盒或 HDL Cosimulation 接口。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **AdaptivePipelining** | 基于综合工具、目标频率和乘法器字长自动插入流水线。默认值为 `inherit`。另请参阅 AdaptivePipelining。 |
| **ClockRatePipelining** | 以更快的时钟速率而不是更慢的数据速率插入流水线寄存器。默认值为 `inherit`。另请参阅 ClockRatePipelining。 |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline。 |
| **DistributedPipelining** | 流水线寄存器分布，或寄存器重定时。默认值为 `inherit`。另请参阅 DistributedPipelining。 |
| **DSPStyle** | 用于乘法器映射的综合属性。默认值为 `none`。另请参阅 DSPStyle。 |
| **FlattenHierarchy** | 从生成的 HDL 代码中移除子系统层次结构。默认值为 `inherit`。另请参阅 FlattenHierarchy。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline。 |
| **SharingFactor** | 要映射到单个共享资源的等效功能资源数量。默认值为 0。另请参阅资源共享。 |
| **StreamingFactor** | 并行数据路径或向量数量，它们经过时分多路复用转换为串行标量数据路径。默认值为 0，表示实现完全并行的数据路径。另请参阅流式传输。 |

如果此模块不是 DUT，则 **目标规范** 选项卡中的模块属性设置会被忽略。在 HDL Workflow Advisor 中，如果您使用 **IP 核生成** 工作流，这些目标规范模块属性值会随模型一起保存。如果您使用 `hdlset_param` 指定这些目标规范模块属性值，则当您打开 HDL Workflow Advisor 时，这些字段会填充相应的值。

| 目标规范 | |
| --- | --- |
| **AdditionalTargetInterfaces** | 附加目标接口，指定为 character vector。要将此模块属性保存到模型上，请在 **IP 核生成** 工作流的 **设置目标接口** 任务中，针对要为其添加更多接口的 DUT 端口，选择 **添加更多...**。然后，您可以在“添加新目标接口”对话框中添加更多接口。指定接口类型、附加接口数量以及每个附加接口的唯一名称。 值：`''`（默认）| cell array of character vectors 示例：`'{{'AXI4-Stream','InterfaceID','AXI4-Stream1'}}'` |
| **ProcessorFPGASynchronization** | 处理器/FPGA 同步模式，指定为 character vector。要将此模块属性保存到模型上，请在 **IP 核生成** 工作流的 **设置目标接口** 任务中指定 **处理器/FPGA 同步**。 值：`Free running`（默认）| `Coprocessing - blocking` 示例：`'Free running'` |
| **TestPointMapping** | 要将此模块属性保存到模型上，请在 **IP 核生成** 工作流的 **设置目标接口** 任务中指定测试点端口到目标平台接口的映射。 值：`''`（默认）| cell array of character vectors 示例：`'{{'TestPoint','AXI4-Lite','x"108"'}}'` |
| **TunableParameterMapping** | 要将此模块属性保存到模型上，请在 **IP 核生成** 工作流的 **设置目标接口** 任务中指定可调参数端口到目标平台接口的映射。 值：`''`（默认）| cell array of character vectors 示例：`'{{'myParam','AXI4-Lite','x"108"'}}'` |
| **AXI4RegisterReadback** | 要将此模块属性保存到模型上，请在 **IP 核生成** 工作流的 **生成 RTL 代码和 IP 核** 任务中指定是否要启用 AXI4 从属写寄存器的回读。要了解详细信息，请参阅 AXI4 从接口生成的模型设计。 值：`'off'`（默认）| `'on'` |
| **AXI4SlaveIDWidth** | 要将此模块属性保存到模型上，请使用 **IP 核生成** 工作流的 **生成 RTL 代码和 IP 核** 任务中的 **AXI4 Slave ID Width** 设置，指定要将 DUT IP 核连接到的 AXI 管理器接口数量。要了解详细信息，请参阅在参考设计中定义多个 AXI 主接口以访问 DUT AXI4 从接口。 值：`'off'`（默认）| `'on'` |
| **RegisterInterfaceReadPipeline** | 要将此模块属性保存到模型上，请使用 **IP 核生成** 工作流的 **生成 RTL 代码和 IP 核** 任务中的 **Register interface read pipeline** 设置，指定要在读地址解码器路径中插入的流水线级数。要了解详细信息，请参阅 AXI4 从接口生成的模型设计。 值：`0`（默认）| character vector |
| **GenerateDefaultAXI4Slave** | 要将此模块属性保存到模型上，请在 **IP 核生成** 工作流的 **生成 RTL 代码和 IP 核** 任务中指定是否要禁用默认 AXI4 从属接口的生成。 值：`'on'`（默认）| `'off'` |
| **IPCoreAdditionalFiles** | 设计中黑盒的 Verilog®、SystemVerilog 或 VHDL® 文件。指定每个文件的完整路径，并用分号 (;) 分隔文件名。 您可以在 HDL Workflow Advisor 中的 **其他源文件** 字段中设置此属性。 值：`''`（默认）| character vector 示例：`'C:\myprojfiles\led_blinking_file1.vhd;C:\myprojfiles\led_blinking_file2.vhd;'` |
| **IPCoreName** | IP 核名称，指定为 character vector。 您可以在 HDL Workflow Advisor 中的 **IP 核名称** 字段中设置此属性。如果此属性设置为默认值，则 HDL Workflow Advisor 会根据 DUT 的名称构造 IP 核名称。 值：`''`（默认）| character vector 示例：`'my_model_name'` |
| **IPCoreVersion** | IP 核版本号，指定为 character vector。 您可以在 HDL Workflow Advisor 中的 **IP 核版本** 字段中设置此属性。如果此属性设置为默认值，则 HDL Workflow Advisor 会设置 IP 核版本。 值：`''`（默认）| character vector 示例：`'1.3'` |
| **IPDataCaptureBufferSize** | FPGA 数据捕获缓冲区大小，指定为 character vector。在 FPGA 上运行时，使用 FPGA 数据捕获观察设计中的信号。 缓冲区大小使用 128\*2^n 格式的值，其中 n 是整数。默认情况下，缓冲区大小为 128 (n=0)。n 的最大值为 13，这意味着缓冲区大小的最大值为 1048576 (=128\*2^13)。 值：`''`（默认）| character vector 示例：`'1.3'` |

**限制**

- 您的 DUT 不能是 Enabled Synchronous Subsystem。
- 子系统中不能包含带外部复位端口的 Delay 模块。
- 不能为 Enabled Synchronous Subsystem 内的 LTE Turbo Decoder 模块生成 HDL。
- HDL 代码生成在 Enable 端口仅支持 boolean 数据类型。

## 版本历史

**在 R2016a 中引入**

## 描述

表示具有同步复位和使能行为的使能子系统

Enabled Synchronous Subsystem 是一种 Enabled Subsystem，它使用 State Control 模块的 `Synchronous` 模式。如果子系统中出现 **S** 符号，则该子系统是同步的。

要创建 Enabled Synchronous Subsystem 模块，请从 HDL Subsystems 模块库将该模块添加到您的 Simulink® 模型中。您还可以在 Enabled Subsystem 内添加一个 State Control 模块，并将 **状态控制** 设置为 `Synchronous`。

有关详细信息，请参阅 State Control 和使用 Enabled Subsystems。
