---
type: simulink-block
title: 'Interval Test'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'intervaltest'
documentation_source_path: 'slref/intervaltest.html'
language: zh-CN
chinese_source: worker-translation
---

# Interval Test

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵 | N 维数组

输入信号，指定为标量、向量、矩阵或 N 维数组。

#### 限制

当输入信号为枚举类型时，**Upper limit** 和 **Lower limit** 值必须为相同的枚举类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵 | N 维数组

输出信号，指示输入值是否落在指定区间内。您可以将 **Output data type** 指定为 `boolean` 或 `uint8`。

**数据类型：** `uint8` | `Boolean`

## 参数

### **Interval closed on right** — 包含上限值 `on`（默认）| `off`

当您选中此复选框时，**Upper limit** 包含在模块输出 true（`1`）的区间内。

#### 编程使用

|  |
| --- |
| **模块参数**：`IntervalClosedRight` |
| **类型**：character vector |
| **值**：`'on' | 'off'` |
| **默认值**：`'on'` |

### **Upper limit** — 区间上限 `0.5`（默认）| 标量 | 向量 | 矩阵 | N 维数组

模块输出 true（`1`）的区间上限。

#### 编程使用

|  |
| --- |
| **模块参数**：`uplimit` |
| **类型**：character vector |
| **值**：scalar | vector | matrix | N-D array |
| **默认值**：`'0.5'` |

### **Interval closed on left** — 包含下限值 `on`（默认）| `off`

当您选中此复选框时，**Lower limit** 包含在模块输出 true（`1`）的区间内。

#### 编程使用

|  |
| --- |
| **模块参数**：`IntervalClosedLeft` |
| **类型**：character vector |
| **值**：`'on' | 'off'` |
| **默认值**：`'on'` |

### **Lower limit** — 区间下限 `-0.5`（默认）| 标量 | 向量 | 矩阵 | N 维数组

模块输出 true（`1`）的区间下限。

#### 编程使用

|  |
| --- |
| **模块参数**：`lowlimit` |
| **类型**：character vector |
| **值**：scalar | vector | matrix | N-D array |
| **默认值**：`'-0.5'` |

### **Output data type** — 输出数据类型 `boolean`（默认）| `uint8`

将输出数据类型指定为 `boolean` 或 `uint8`。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：character vector |
| **值**：`'boolean' | 'uint8'` |
| **默认值**：`'boolean'` |

## 所属库

Simulink / Logic and Bit Operations

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| `Module`（默认） | 为子系统及子系统内的模块生成代码。 |
| `BlackBox` | 生成黑盒接口。生成的 HDL 代码仅包含子系统的输入/输出端口定义。因此，您可以在模型中使用子系统来生成与现有手写 HDL 代码的接口。子系统的黑盒接口生成类似于 Model 模块接口生成，但不包含时钟信号。 |
| `No HDL` | 从生成的代码中移除子系统。您可以在仿真中使用该子系统，但在 HDL 代码中将其视为“空操作”。 |

**黑盒接口自定义**

对于 `BlackBox` 架构，您可以自定义端口名称并设置外部组件接口的属性。请参阅 Customize Black Box or HDL Cosimulation Interface (HDL Coder)。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **AdaptivePipelining** | 基于综合工具、目标频率和乘法器字长的自动流水线插入。默认值为 `inherit`。另请参阅 AdaptivePipelining (HDL Coder)。 |
| **ClockRatePipelining** | 以更快的时钟速率而非较慢的数据速率插入流水线寄存器。默认值为 `inherit`。另请参阅 ClockRatePipelining (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **DistributedPipelining** | 流水线寄存器分配，或寄存器重定时。默认值为 `inherit`。另请参阅 DistributedPipelining (HDL Coder)。 |
| **DSPStyle** | 用于乘法器映射的综合属性。默认值为 `none`。另请参阅 DSPStyle (HDL Coder)。 |
| **FlattenHierarchy** | 从生成的 HDL 代码中移除子系统层级。默认值为 `inherit`。另请参阅 FlattenHierarchy (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **SharingFactor** | 映射到单个共享资源的功能等效资源数量。默认值为 0。另请参阅 Resource Sharing (HDL Coder)。 |
| **StreamingFactor** | 被时分复用转换为串行标量数据路径的并行数据路径（或向量）数量。默认值为 0，表示实现完全并行的数据路径。另请参阅 Streaming (HDL Coder)。 |

如果此模块不是 DUT，则 **Target Specification** 选项卡中的模块属性设置将被忽略。在 HDL Workflow Advisor 中，如果您使用 **IP Core Generation** 工作流，这些目标规范模块属性值将随模型一起保存。如果您使用 `hdlset_param` 指定这些目标规范模块属性值，则当您打开 HDL Workflow Advisor 时，这些字段将填充相应的值。

| 目标规范 | |
| --- | --- |
| **AdditionalTargetInterfaces** | 额外目标接口，指定为字符向量。要将此模块属性保存在模型上，请在 **IP Core Generation** 工作流的 **Set Target Interface** 任务中，针对要添加更多接口的 DUT 端口，选择 **Add more...**。然后您可以在 Add New Target Interfaces 对话框中添加更多接口。指定接口类型、额外接口数量以及每个额外接口的唯一名称。值：`''`（默认）| 字符向量元胞数组 示例：`'{{'AXI4-Stream','InterfaceID','AXI4-Stream1'}}'` |
| **ProcessorFPGASynchronization** | 处理器/FPGA 同步模式，指定为字符向量。要将此模块属性保存在模型上，请在 **IP Core Generation** 工作流的 **Set Target Interface** 任务中指定 **Processor/FPGA Synchronization**。值：`Free running`（默认）| `Coprocessing - blocking` 示例：`'Free running'` |
| **TestPointMapping** | 要将此模块属性保存在模型上，请在 **IP Core Generation** 工作流的 **Set Target Interface** 任务中指定测试点端口到目标平台接口的映射。值：`''`（默认）| 字符向量元胞数组 示例：`'{{'TestPoint','AXI4-Lite','x"108"'}}'` |
| **TunableParameterMapping** | 要将此模块属性保存在模型上，请在 **IP Core Generation** 工作流的 **Set Target Interface** 任务中指定可调参数端口到目标平台接口的映射。值：`''`（默认）| 字符向量元胞数组 示例：`'{{'myParam','AXI4-Lite','x"108"'}}'` |
| **AXI4RegisterReadback** | 要将此模块属性保存在模型上，请在 **IP Core Generation** 工作流的 **Generate RTL Code and IP Core** 任务中指定是否要在 AXI4 从写寄存器上启用回读。要了解更多信息，请参阅 Model Design for AXI4 Slave Interface Generation (HDL Coder)。值：`'off'`（默认）| `'on'` |
| **AXI4SlaveIDWidth** | 要将此模块属性保存在模型上，请在 **IP Core Generation** 工作流的 **Generate RTL Code and IP Core** 任务中使用 **AXI4 Slave ID Width** 设置指定要将 DUT IP 核连接到的 AXI 管理器接口数量。要了解更多信息，请参阅 Define Multiple AXI Master Interfaces in Reference Designs to Access DUT AXI4 Slave Interface (HDL Coder)。值：`'off'`（默认）| `'on'` |
| **RegisterInterfaceReadPipeline** | 要将此模块属性保存在模型上，请在 **IP Core Generation** 工作流的 **Generate RTL Code and IP Core** 任务中使用 **Register interface read pipeline** 设置指定要在读地址解码器路径中插入的流水线级数。要了解更多信息，请参阅 Model Design for AXI4 Slave Interface Generation (HDL Coder)。值：`0`（默认）| 字符向量 |
| **GenerateDefaultAXI4Slave** | 要将此模块属性保存在模型上，请在 **IP Core Generation** 工作流的 **Generate RTL Code and IP Core** 任务中指定是否要禁用默认 AXI4 从接口的生成。值：`'on'`（默认）| `'off'` |
| **IPCoreAdditionalFiles** | 用于设计中黑盒的 Verilog®、SystemVerilog 或 VHDL® 文件。指定每个文件的完整路径，并用分号（;）分隔文件名。您可以在 HDL Workflow Advisor 的 **Additional source files** 字段中设置此属性。值：`''`（默认）| 字符向量 示例：`'C:\myprojfiles\led_blinking_file1.vhd;C:\myprojfiles\led_blinking_file2.vhd;'` |
| **IPCoreName** | IP 核名称，指定为字符向量。您可以在 HDL Workflow Advisor 的 **IP core name** 字段中设置此属性。如果此属性设置为默认值，HDL Workflow Advisor 将基于 DUT 的名称构造 IP 核名称。值：`''`（默认）| 字符向量 示例：`'my_model_name'` |
| **IPCoreVersion** | IP 核版本号，指定为字符向量。您可以在 HDL Workflow Advisor 的 **IP core version** 字段中设置此属性。如果此属性设置为默认值，HDL Workflow Advisor 将设置 IP 核版本。值：`''`（默认）| 字符向量 示例：`'1.3'` |
| **IPDataCaptureBufferSize** | FPGA 数据捕获缓冲区大小，指定为字符向量。使用 FPGA Data Capture 在 FPGA 上运行时观察设计中的信号。缓冲区大小使用 128\*2^n 的值，其中 n 为整数。默认情况下，缓冲区大小为 128（n=0）。n 的最大值为 13，这意味着缓冲区大小的最大值为 1048576（=128\*2^13）。值：`''`（默认）| 字符向量 示例：`'1.3'` |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

确定信号是否在指定区间内

如果输入介于 **Lower limit** 和 **Upper limit** 参数指定的值之间，Interval Test 模块输出 true（`1`）。如果输入在这些值之外，模块输出 false（`0`）。当输入等于 **Lower limit** 或 **Upper limit** 时模块的输出取决于您是否选中 **Interval closed on left** 和 **Interval closed on right** 复选框。
