---
type: simulink-block
title: 'Rate Transition'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Signal Attributes'
documentation_page: 'ratetransition'
documentation_source_path: 'slref/ratetransition.html'
language: zh-CN
chinese_source: worker-translation
---

# Rate Transition

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 标量 | 向量 | 矩阵 | N 维数组
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus
- name: Port_1
  summary: 输出信号 标量 | 向量 | 矩阵 | N 维数组
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus
```

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵 | N 维数组

转换到新采样率的输入信号，指定为标量、向量、矩阵或 N 维数组。要了解使您能够以数据完整性和确定性传输换取更快响应或更低内存要求的模块参数，请参阅转换处理行为。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵 | N 维数组

转换为您指定的采样率的输入信号。默认配置确保安全且确定性的数据传输。要了解使您能够以数据完整性和确定性传输换取更快响应或更低内存要求的模块参数，请参阅转换处理行为。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
## 参数
```yaml
parameters:
- name: Ensure data integrity during data transfer
  summary: 确保数据完整性 on（默认）| off
  group: ''
  block_parameter: Integrity
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''on'''
- name: Ensure deterministic data transfer (maximum delay)
  summary: 确保确定性数据传输 on（默认）| off
  group: ''
  block_parameter: Deterministic
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''on'''
- name: Initial conditions
  summary: 初始条件 0（默认）| 标量 | 向量 | 矩阵 | N 维数组
  group: ''
  block_parameter: InitialCondition
  type: 字符向量
  values: 有限标量
  default: '''0'''
- name: Output port sample time options
  summary: 指定输出端口采样时间的模式 Specify（默认）| Inherit | Multiple of input port sample time
  group: ''
  block_parameter: OutPortSampleTimeOpt
  type: 字符向量
  values: '''Specify'' | ''Inherit'' | ''Multiple of input port sample time'''
  default: '''Specify'''
- name: Output port sample time
  summary: 输出速率 -1（默认）| 标量 | 向量
  group: ''
  block_parameter: OutPortSampleTime
  type: 字符向量
  values: 标量 | 向量
  default: '''-1'''
- name: Sample time multiple (>0)
  summary: 采样时间倍数 1（默认）| 正标量
  group: ''
  block_parameter: OutPortSampleTimeMultiple
  type: 字符向量
  values: 标量
  default: '''1'''
```

### **Ensure data integrity during data transfer** — 确保数据完整性 `on`（默认）| `off`

选中此参数将生成在模块传输数据时确保数据完整性的代码。如果您选中此参数且传输是非确定性的（请参阅 **Ensure deterministic data transfer**），则根据输入速率和输出速率的优先级，生成的代码将使用适当的算法（使用单个或多个缓冲区）在数据传输期间保护数据完整性。

否则，Rate Transition 模块将被缩减，或通过使用复制操作来影响数据传输的方式生成代码。此未保护模式消耗更少内存。但是，复制操作是可中断的，这可能导致数据传输期间数据完整性丢失。如果您希望生成的代码以最大响应性（即非确定性）运行并保持数据完整性，请选中此参数。有关详细信息，请参阅 Control Data Transfer Behavior in Generated Code (Simulink Coder)。

#### 编程用法

|  |
| --- |
| **模块参数：** `Integrity` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'on'` |

### **Ensure deterministic data transfer (maximum delay)** — 确保确定性数据传输 `on`（默认）| `off`

选中此参数将生成以较慢模块的采样率传输数据（即确定性地）的代码。如果您不选中此参数，数据传输将在源模块有新数据可用且接收模块准备好接收数据时发生。您避免了传输延迟，从而确保系统以最大响应性运行。但是，传输可能不可预测地发生，这在某些应用中是不希望的。有关详细信息，请参阅 Control Data Transfer Behavior in Generated Code (Simulink Coder)。

#### 编程用法

|  |
| --- |
| **模块参数：** `Deterministic` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'on'` |

### **Initial conditions** — 初始条件 `0`（默认）| 标量 | 向量 | 矩阵 | N 维数组

此参数仅适用于慢到快转换。它指定转换开始时 Rate Transition 模块的初始输出，此时由于没有来自慢速模块的输入信号而没有输出信号。Simulink® 不允许此模块的初始输出为 `Inf` 或 `NaN`。您指定的值必须是标量，或具有与输入信号相同的维度。

#### 编程用法

|  |
| --- |
| **模块参数：** `InitialCondition` |
| **类型：** 字符向量 |
| **值：** 有限标量 |
| **默认值：** `'0'` |

### **Output port sample time options** — 指定输出端口采样时间的模式 `Specify`（默认）| `Inherit` | `Multiple of input port sample time`

指定设置输出端口采样时间的模式。

- `Specify` — 使用 **Output port sample time** 参数指定模块将其输入速率转换到的输出速率。
- `Inherit` — 模块从输出端口所连接的模块继承输出速率。
- `Multiple of input port sample time` — 使用 **Sample time multiple (>0)** 参数将模块输出速率指定为其输入速率的倍数。

如果您选择 `Inherit` 且连接到输出端口的模块也继承采样时间，则模型中最快的采样时间适用。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutPortSampleTimeOpt` |
| **类型：** 字符向量 |
| **值：** `'Specify' | 'Inherit' | 'Multiple of input port sample time'` |
| **默认值：** `'Specify'` |

### **Output port sample time** — 输出速率 `-1`（默认）| 标量 | 向量

输入一个值，指定模块将其输入速率转换到的输出速率。默认值（`-1`）指定 Rate Transition 模块从输出端口所连接的模块继承输出速率。有关如何指定输出速率的信息，请参阅 Specify Sample Time。

#### 依赖关系

要启用此参数，请将 **Output port sample time options** 设置为 `Specify`。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutPortSampleTime` |
| **类型：** 字符向量 |
| **值：** 标量 | 向量 |
| **默认值：** `'-1'` |

### **Sample time multiple (>0)** — 采样时间倍数 `1`（默认）| 正标量

输入一个正值，将输出速率指定为输入端口采样时间的倍数。默认值（`1`）指定输出速率与输入速率相同。值 `0.5` 指定输出速率是输入速率的一半。值 `2` 指定输出速率是输入速率的两倍。

#### 依赖关系

要启用此参数，请将 **Output port sample time options** 设置为 `Multiple of input port sample time`。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutPortSampleTimeMultiple` |
| **类型：** 字符向量 |
| **值：** 标量 |
| **默认值：** `'1'` |
## 所属库

Simulink / Signal Attributes HDL Coder / Signal Attributes

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

- 在某些条件下，例如对于多维信号，生成的代码依赖于 `memcpy` 或 `memset` 函数（`string.h`）。
- 不要在触发子系统层级内使用 Rate Transition 模块。
- 并发程序的生成代码是平台特定的，并假定部署平台和开发平台相同。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的配置选项。

**最佳实践**

- 当 Rate Transition 模块以快速输入速率和慢速输出速率运行时，最佳实践是在 Rate Transition 模块之后跟一个单位延迟。这样做可以防止代码生成器在 HDL 代码中插入额外的旁路寄存器。另请参阅 Multirate Model Requirements for HDL Code Generation (HDL Coder)。
- 要在不引入单位延迟的情况下对输入信号进行上采样，请按如下方式配置 Rate Transition 模块参数：

  - 清除 **Ensure data integrity during data transfer**。

    清除此参数会隐藏 **Ensure deterministic data transfer (maximum delay)** 参数。
  - 将模块的输出端口采样时间配置为输入端口采样时间的整数倍。为 **Sample time multiple** 指定分数值 `1/n`，其中 `n` 是整数。如果 **Sample time multiple** 使用值 `1/n`，您可以为模块参数 **Output port sample time** options 选择任意值。

  **注意**

  在对输入信号进行下采样时，请保持 **Ensure data integrity during data transfer** 和 **Ensure deterministic data transfer (maximum delay)** 参数处于选中状态。此模式会在 HDL 代码中生成额外的旁路寄存器。

  另请参阅 Usage of Rate Change and Constant Blocks (HDL Coder)。

**限制**

- 模块输入或输出端口的采样率不能为 `0` 或 `Inf`。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **AsyncRTAsWire** | 将异步速率转换映射为线。当 **Output port sample time** 具有非整数值时，它被视为异步速率。启用 **AsyncRTAsWire** 选项以在 Rate Transition 模块存在此类异步速率时生成线。 **依赖关系：** 此选项仅在 **Ensure data integrity during data transfer** 和 **Ensure deterministic data transfer** 参数关闭时可用。 当使用异步速率转换作为线时，将 **Clock inputs** 选项设置为 `Multiple`。 |

**注意**

在将异步速率转换映射为线时，您可能会看到 Simulink 和代码生成结果之间的数值不匹配。

**复数数据支持**

此模块支持复数信号的代码生成。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

处理在不同速率下运行的模块之间的数据传输

Rate Transition 模块将数据从一个以某一速率运行的模块的输出传输到一个以不同速率运行的模块的输入。使用模块参数以数据完整性和确定性传输换取更快响应或更低内存要求。要了解数据完整性和确定性数据传输，请参阅 Data Transfer Considerations (Simulink Coder)。

### 转换处理行为

| 行为 | 参数设置 | 说明 |
| --- | --- | --- |
| - 数据完整性 - 确定性数据传输 - 最大延迟 | 选中： - **Ensure data integrity during data transfer** - **Ensure deterministic data transfer** | - 生成的代码传输数据时确保信号的字节（包括宽信号的元素）来自同一时间步。 - 数据从一个速率传输到另一个速率的相对采样时间（延迟）相同。 - 代码生成器仅生成 ANSI® C 代码。 - 不需要目标特定的临界区保护。 |
| - 数据完整性 - 非确定性数据传输 - 最小延迟 - 更高内存要求 | 选中： - **Ensure data integrity during data transfer** 清除： - **Ensure deterministic data transfer** | - 生成的代码传输数据时确保信号的字节（包括宽信号的元素）来自同一时间步。 - 数据传输的相对采样时间（延迟）可能因每次数据传输而异。读写数据的代码运行频率高于选中 **Ensure data integrity during data transfer** 和 **Ensure deterministic data transfer** 时的情况。在最坏情况下，延迟等同于选中 **Ensure data integrity during data transfer** 和 **Ensure deterministic data transfer** 时的情况，但延迟可能更小，这对某些应用可能很重要。 - 支持与异步速率之间的数据传输。 - 代码生成器仅生成 ANSI C 代码。 - 不需要目标特定的临界区保护。 |
| - 潜在的数据完整性丢失 - 非确定性数据传输 - 最小延迟 - 更低内存要求 | 清除： - **Ensure data integrity during data transfer** - **Ensure deterministic data transfer** | - 代码生成器不为 Rate Transition 模块生成代码。 - 适用于保证标量数据类型原子访问且数据的相对时间值不重要的应用。 - 不引入延迟。 |

Rate Transition 模块的行为取决于：

- 模块所连接端口的采样时间（请参阅 Effects of Synchronous Sample Times 和 Effects of Asynchronous Sample Times）
- 源和目标采样时间的任务优先级（请参阅 Sample time properties）
- 模型指定的是固定步长还是可变步长求解器（请参阅 Compare Solvers）
- 模型配置参数 **Device vendor** 和 **Device type** 的设置（请参阅 Effects of Device Configuration）

### 模块标签

当您更新模型图时，Rate Transition 模块上会出现一个标签以指示仿真行为。

| 标签 | 模块行为 |
| --- | --- |
| `ZOH` | 充当零阶保持 |
| `1/z` | 充当单位延迟 |
| `Buf` | 在信号量控制下将输入复制到输出 |
| `Db_buf` | 使用双缓冲区将输入复制到输出 |
| `3buf` | 使用三缓冲区将输入复制到输出 |
| `Copy` | 未保护的输入到输出复制 |
| `NoOp` | 无操作 |
| `Mixed` | 扩展为具有不同行为的多个模块 |
| `RT` | 在使用 Schedule Editor 时指示分区之间的数据传输。有关更多信息，请参阅 Using the Schedule Editor。 |
| `Memory` | 指示内存模式。当 **Ensure deterministic data transfer (maximum delay)** 被清除时，模块处于内存模式。 |

模块行为标签显示了确保在不同速率下运行的任务之间安全传输数据的方法。您可以使用采样时间颜色功能（请参阅 View Sample Time Information）来显示模块所桥接的相对速率。考虑此示例模型：

包含处理快到慢速率转换和慢到快速率转换的 Rate Transition 模块的模型。

采样时间颜色和模块行为标签显示：

- 图顶部的 Rate Transition 模块在快到慢转换中充当零阶保持。
- 图底部的 Rate Transition 模块在慢到快转换中充当单位延迟。

有关更多信息，请参阅 Data Transfer Representation and Processing (Simulink Coder)。

### 同步采样时间的影响

下表总结了当输入和输出端口（`inTs` 和 `outTs`）的采样时间为周期性或同步时，各标签的显示方式。

| 模块设置 | | 模块标签 | | |
| --- | --- | --- | --- | --- |
| 速率转换 | 速率转换模块的条件 | 具有数据完整性和确定性 | 仅具有数据完整性 | 无数据完整性或确定性 |
| `inTs` = `outTs`（相等） | `inTsOffset` < `outTsOffset` | 无（错误） | `Buf` | `Copy` 或 `NoOp`（参见表后注释） |
| `inTsOffset` = `outTsOffset` | `Copy` 或 `NoOp`（参见表后注释） | `Copy` 或 `NoOp`（参见表后注释） |
| `inTsOffset` > `outTsOffset` | 无（错误） | `Db_buf` |
| `inTs` < `outTs`（快至慢） | `inTs` = `outTs / N`  `inTsOffset`、`outTsOffset` = 0 | `ZOH` | `Buf` |
| `inTs` = `outTs / N`  `inTsOffset` ≤ `outTsOffset` | 无（错误） |
| `inTs` = `outTs / N`  `inTsOffset` > `outTsOffset` | 无（错误） | `Db_buf` |
| `inTs` ≠ `outTs / N` | 无（错误） |
| `inTs` > `outTs`（慢至快） | `inTs` = `outTs * N`  `inTsOffset`、`outTsOffset` = 0 | `1/z` | `Db_buf` |
| `inTs` = `outTs * N`  `inTsOffset` ≤ `outTsOffset` | 无（错误） |
| `inTs` = `outTs * N`  `inTsOffset` > `outTsOffset` | 无（错误） |
| `inTs` ≠ `outTs * N` | 无（错误） |
| **键**  - `inTs`、`outTs`：分别为输入和输出端口的采样时间 - `inTsOffset`、`outTsOffset`：分别为输入和输出端口的采样时间偏移 - `N`：大于 1 的整数值 | | | | |

**注意**

当您选择模型配置参数 **Block reduction** 时，`Copy` 会简化为 `NoOp`。对于带有 `NoOp` 标签的速率转换模块，不会生成代码。为防止在块简化开启时模块被简化，请向模块输出添加测试点（参见将信号配置为测试点）。

### 异步采样时间的影响

下表总结了当输入或输出端口（`inTs` 或 `outTs`）的采样时间不是周期性的或异步时，各标签的显示方式。

| 模块设置 | | 模块标签 | | |
| --- | --- | --- | --- | --- |
| 具有数据完整性和确定性 | 仅具有数据完整性 | 无数据完整性或确定性 |
| `inTs` = `outTs` | | `Copy` | `Copy` | `Copy` |
| `inTs` ≠ `outTs` | | 无（错误） | `Db_buf` |
| **键**  - `inTs`、`outTs`：分别为输入和输出端口的采样时间 | | | | |

### 设备配置的影响

如果模型配置参数 **Device vendor** 和 **Device type** 的设置指定了支持原子数据加载和存储操作的硬件，则当目标硬件支持所传输信号的数据类型的原子加载和存储操作时，代码生成器会优化生成的速率转换代码。代码生成器利用硬件数据加载和存储能力，将异步任务之间的双缓冲代码替换为执行单次内存复制的代码。
