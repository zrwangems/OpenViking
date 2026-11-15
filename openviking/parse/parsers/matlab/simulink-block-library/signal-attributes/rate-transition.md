---
type: simulink-block
title: 'Rate Transition'
family: signal-attributes
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Signal Attributes'
documentation_page: 'ratetransition'
---

# Rate Transition

Handle transfer of data between blocks operating at different rates

## 中文

处理以不同速率运行的模块之间的数据传输

### 所属库

Simulink / Signal Attributes HDL Coder / Signal Attributes

### 描述

Rate Transition 模块可将数据从按某速率运行的模块的输出端口传输到另一个按不同速率运行的模块的输入端口。可以使用模块参数在数据完整性与确定性传输之间进行取舍，以实现更快的响应速度或者更低的内存要求。有关数据完整性和确定性数据传输的信息，请参阅数据传输注意事项 (Simulink Coder)。

#### 转移处理行为

| 行为 | 参数设置 | 注释 |
| --- | --- | --- |
| - 数据完整性 - 确定性数据传输 - 最大延迟 | 选择：  - **确保数据传输的数据完整性** - **确保确定性数据传输** | - 生成的代码传输数据，以便信号（包括宽信号的元素）的数据字节来自同一时间步。 - 从其将数据从一个速率转换为另一个速率的相对采样时间（延迟）相同。 - 代码生成器仅生成 ANSI® C 代码。 - 不需要特定于目标的临界区保护。 |
| - 数据完整性 - 不确定的数据传输 - 最小延迟 - 更高的内存要求 | 选择：  - **确保数据传输的数据完整性**  清除：  - **确保确定性数据传输** | - 生成的代码传输数据，以便信号（包括宽信号的元素）的数据字节来自同一时间步。 - 从其传输数据的相对采样时间（延迟）可能因具体数据传输而异。与选择**确保数据传输的数据完整性**和**确保确定性数据传输**时的情形相比，读取和写入数据的代码运行得更频繁。在最差情形下，延迟与选择**确保数据传输的数据完整性**和**确保确定性数据传输**时相当，但通常延迟更小，这对某些应用很重要。 - 支持与异步速率之间的数据传输。 - 代码生成器仅生成 ANSI C 代码。 - 不需要特定于目标的临界区保护。 |
| - 可能丢失数据完整性 - 不确定的数据传输 - 最小延迟 - 更低的内存要求 | 清除：  - **确保数据传输的数据完整性** - **确保确定性数据传输** | - 代码生成器不为 Rate Transition 模块生成代码。 - 适用于保证标量数据类型的原子访问且数据的相对时序值不重要的应用。 - 不引入延迟。 |

Rate Transition 模块的行为取决于：

- 模块连接到的端口的采样时间（请参阅同步采样时间的效果和异步采样时间的效果）
- 源和目标采样时间的任务的优先级（请参阅Sample time properties）
- 模型指定的是定步长还是变步长求解器（请参阅比较求解器）
- 模型配置参数**设备供应商**和**设备类型**的设置（请参阅设备配置的影响）

#### 模块标签

当您更新模型图时，Rate Transition 模块上将出现一个标签，以指示仿真行为。

| 标签 | 模块行为 |
| --- | --- |
| `ZOH` | 充当零阶保持器 |
| `1/z` | 充当单位延迟器 |
| `Buf` | 在信号灯控制下将输入复制到输出 |
| `Db_buf` | 使用双缓冲区将输入复制到输出 |
| `3buf` | 使用三缓冲区将输入复制到输出 |
| `Copy` | 在不保护的情况下将输入复制到输出 |
| `NoOp` | 无操作 |
| `Mixed` | 扩展为具有不同行为的多个模块 |
| `RT` | 指示使用调度编辑器时分区之间的数据传输。  有关详细信息，请参阅Using the Schedule Editor。 |
| `Memory` | 指示内存模式。当**确保确定性数据传输(最大延迟)**处于清除状态，该模块处于内存模式。 |

模块行为标签显示了使用的方法，该方法用于确保在以不同速率运行的任务之间安全地传输数据。您可以使用采样时间颜色功能（请参阅查看采样时间信息）显示模块桥接的相对速率。以如下模型为例：

Model that includes Rate Transition blocks that handle a fast-to-slow rate transition and a slow-to-fast rate transition.

采样时间颜色和模块行为标签表明：

- 图中上方的 Rate Transition 模块充当从快速到慢速转移中的零阶保持器。
- 图中下方的 Rate Transition 模块充当从慢速到快速转移中的单位延迟器。

有关详细信息，请参阅数据传输表示和处理 (Simulink Coder)。

#### 同步采样时间的效果

下表总结了当输入和输出端口（`inTs` 和 `outTs`）的采样时间为周期性或同步时每个标签的显示方式。

| 模块设置 | | 模块标签 | | |
| --- | --- | --- | --- | --- |
| 速率转换 | Rate Transition 模块的条件 | 保证数据完整性与确定性 | 仅保证数据完整性 | 不保证数据完整性或确定性 |
| `inTs` = `outTs`  （相等） | `inTsOffset` < `outTsOffset` | 无（错误） | `Buf` | `Copy` 或者 `NoOp`（请参阅表后面的注释） |
| `inTsOffset` = `outTsOffset` | `Copy` 或者 `NoOp`（请参阅表后面的注释） | `Copy` 或者 `NoOp`（请参阅表后面的注释） |
| `inTsOffset` > `outTsOffset` | 无（错误） | `Db_buf` |
| `inTs` < `outTs`  （快速到慢速） | `inTs` = `outTs / N`  `inTsOffset`、`outTsOffset` = 0 | `ZOH` | `Buf` |
| `inTs` = `outTs / N`  `inTsOffset` ≤ `outTsOffset` | 无（错误） |
| `inTs` = `outTs / N`  `inTsOffset` > `outTsOffset` | 无（错误） | `Db_buf` |
| `inTs` ≠ `outTs / N` | 无（错误） |
| `inTs` > `outTs`  （慢速到快速） | `inTs` = `outTs * N`  `inTsOffset`、`outTsOffset` = 0 | `1/z` | `Db_buf` |
| `inTs` = `outTs * N`  `inTsOffset` ≤ `outTsOffset` | 无（错误） |
| `inTs` = `outTs * N`  `inTsOffset` > `outTsOffset` | 无（错误） |
| `inTs` ≠ `outTs * N` | 无（错误） |
| **关键注释**  - `inTs`, `outTs`:分别指输入和输出端口的采样时间 - `inTsOffset`, `outTsOffset`:分别指输入和输出端口的采样时间偏移量 - `N`:大于 1 的整数值 | | | | |

**注意**

当选择模型配置参数**模块简化**时，`Copy` 简化为 `NoOp`。带有 `NoOp` 标签的 Rate Transition 模块不会执行代码生成。要在启用了模块简化处理时阻止模块简化，请在模块输出端口添加一个测试点（请参阅将信号配置为测试点）。

#### 异步采样时间的效果

下表总结了当输入和输出端口（`inTs` 和 `outTs`）的采样时间为非周期性或异步时每个标签的显示方式。

| 模块设置 | | 模块标签 | | |
| --- | --- | --- | --- | --- |
| 保证数据完整性与确定性 | 仅保证数据完整性 | 不保证数据完整性或确定性 |
| `inTs` = `outTs` | | `Copy` | `Copy` | `Copy` |
| `inTs` ≠ `outTs` | | 无（错误） | `Db_buf` |
| **关键注释**  - `inTs`, `outTs`:分别指输入和输出端口的采样时间 | | | | |

#### 设备配置的影响

如果模型配置参数**设备供应商**和**设备类型**的设置指定支持原子数据加载和存储操作的硬件，则当目标硬件支持要传输的信号数据类型的原子数据加载和存储操作时，代码生成器会优化生成的速率转换代码。代码生成器通过将异步任务之间的双缓冲代码替换为执行单次内存复制的代码来利用硬件数据加载和存储能力。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量 | 矩阵 | N 维数组

转换为新采样率的输入信号，指定为标量、向量、矩阵或 N 维数组。一些模块参数让您能够在数据完整性与确定性传输之间进行取舍，以实现更快的响应速度或更低的内存要求，要了解它们，请参阅转移处理行为。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
#### 输出

#### **Port\_1** — 输出信号 标量 | 向量 | 矩阵 | N 维数组

转换为您指定的采样率的输入信号。默认配置可确保安全且确定的数据传输。一些模块参数让您能够在数据完整性与确定性传输之间进行取舍，以实现更快的响应速度或更低的内存要求，要了解它们，请参阅转移处理行为。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### 参数

#### **确保数据传输的数据完整性** — 确保数据完整性 `on` (默认) | `off`

如果选择此参数，生成的代码可以在模块传输数据时确保数据的完整性。如果选中此参数，而传输是不确定的（请参阅**确保确定性数据传输**），根据输入速率和输出速率的优先级，生成的代码将使用正确的算法，使用一个或多个缓冲区来保护数据传输过程中的数据完整性。

否则，Rate Transition 模块要么会简化，要么通过使用复制操作执行数据传输来生成代码。这种不受保护的模式需要较少的内存。不过，复制操作可能会中断，从而导致数据传输过程中损失数据完整性。如果您希望生成的代码能够在运行时保证最大的响应性（即，不确定性传输）和保持数据完整性，请选择此参数。有关详细信息，请参阅Control Data Transfer Behavior in Generated Code (Simulink Coder)。

##### 编程用法

|  |
| --- |
| **模块参数**：`Integrity` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'on'` |

#### **确保确定性数据传输(最大延迟)** — 确保确定性数据传输 `on` (默认) | `off`

如果选择此参数，生成的代码将按照速率较慢的模块的采样率传输数据，即确定性传输。如果不选择此参数，则在源模块上有新数据且接收模块能够接收数据时，会发生数据传输。这样可以避免传输延迟，确保系统以最大的响应性运行。但是，传输的发生具有不可预测性，这在某些应用中是不希望出现的。有关详细信息，请参阅Control Data Transfer Behavior in Generated Code (Simulink Coder)。

##### 编程用法

|  |
| --- |
| **模块参数**：`Deterministic` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'on'` |

#### **初始条件** — 初始条件 `0` (默认) | 标量 | 向量 | 矩阵 | N 维数组

此参数仅适用于慢速到快速转移。它指定当慢速模块未提供输入信号而导致没有输出信号时，Rate Transition 模块在转移初期的初始输出。Simulink® 不允许此模块的初始输出为 `Inf` 或 `NaN`。您指定的值必须是标量，或者与输入信号具有相同的维度。

##### 编程用法

|  |
| --- |
| **模块参数**：`InitialCondition` |
| **类型：**字符向量 |
| **值：**有限标量 |
| **默认值：**`'0'` |

#### **输出端口采样时间选项** — 指定输出端口采样时间的模式 **指定** (默认) | **继承** | **输入端口采样时间的倍数**

指定用于设置输出端口采样时间的模式。

- **指定** - 使用**输出端口采样时间**参数来指定模块将输入速率转换成的输出速率。
- **继承** - 模块继承输出端口所连接到的模块的输出速率。
- **输入端口采样时间的倍数** - 使用**采样时间倍数 (>0)** 参数来指定模块的输出采样率是其输入速率的几倍。

如果您选择**继承**，而连接输出端口的模块也都继承采样时间，则会采用模型中最快的采样时间。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutPortSampleTimeOpt` |
| **类型：**字符向量 |
| **值：**`'Specify' | 'Inherit' | 'Multiple of input port sample time'` |
| **默认值：**`'Specify'` |

#### **输出端口采样时间** — 输出速率 `-1` (默认) | 标量 | 向量

请输入一个值，指定模块要将其输入速率转换成的输出速率。默认值 (`-1`) 指定 Rate Transition 模块继承输出端口所连接到的模块的输出速率。有关如何指定输出速率的信息，请参阅指定采样时间。

##### 依赖关系

要启用此参数，请将**输出端口采样时间选项**设置为**指定**。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutPortSampleTime` |
| **类型：**字符向量 |
| **值：**标量 | 向量 |
| **默认值：**`'-1'` |

#### **采样时间倍数 (>0)** — 采样时间倍数 `1` (默认) | 正标量

请输入一个正值，将输出速率指定为输入端口采样时间的倍数。默认值 (`1`) 指定输出速率与输入采样率相同。值 `0.5` 指定输出速率是输入速率的一半。值 `2` 指定输出速率是输入速率的两倍。

##### 依赖关系

要启用此参数，请将**输出端口采样时间选项**设置为**输入端口采样时间的倍数**。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutPortSampleTimeMultiple` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'1'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

- 在某些情况下，例如对于多维信号，生成的代码依赖 `memcpy` 或 `memset` 函数 (`string.h`)。
- 不要在触发子系统层次结构内使用 Rate Transition 模块。
- 并发程序的生成代码是特定于平台的，并假定部署平台和开发平台相同。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的配置选项。

**最佳做法**

- 当 Rate Transition 模块以快输入速率和慢输出速率运行时，最好在 Rate Transition 模块后跟一个单位延迟。这样做可以防止代码生成器在 HDL 代码中插入额外的旁路寄存器。另请参阅Multirate Model Requirements for HDL Code Generation (HDL Coder)。
- 要在不产生单位延迟的情况下对输入信号进行上采样，请按以下方式配置 Rate Transition 模块参数：

  - 清除**确保数据传输的数据完整性**。

    清除此参数会隐藏**确保确定性数据传输(最大延迟)** 参数。
  - 将模块的输出端口采样时间配置为输入端口采样时间的整数倍。为**采样时间倍数**指定分数值 `1/n`，其中 `n` 是整数。如果**采样时间倍数**使用值 `1/n`，您可以为模块参数**输出端口采样时间**选项选择任何值。

  **注意**

  对输入信号进行下采样时，请保持**确保数据传输的数据完整性**和**确保确定性数据传输(最大延迟)** 参数处于选中状态。此模式在 HDL 代码中生成额外的旁路寄存器。

  另请参阅Usage of Rate Change and Constant Blocks (HDL Coder)。

**限制**

- 模块输入或输出端口的采样率不能为 `0` 或 `Inf`。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |
| **AsyncRTAsWire** | 将异步速率转换映射为线。  当**输出端口采样时间**具有非整数值时，它被视为异步速率。启用 **AsyncRTAsWire** 选项，以便在 Rate Transition 模块出现此类异步速率时生成一条线。  **依赖关系：**仅当**确保数据传输的数据完整性**和**确保确定性数据传输**参数为 `off` 时，此选项才可用。  在使用异步速率转换作为线时，将**时钟输入**选项设置为**多个**。 |

**注意**

将异步速率转换映射为线时，您可能会看到 Simulink 和代码生成结果之间的数值不匹配。

**复数数据支持**

此模块支持复信号的代码生成。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Signal Attributes HDL Coder / Signal Attributes

## Description

The Rate Transition block transfers data from the output of a block
operating at one rate to the input of a block operating at a different rate. Use the block
parameters to trade data integrity and deterministic transfer for faster response or lower
memory requirements. To learn about data integrity and deterministic data transfer, see Data Transfer Considerations (Simulink Coder).

### Transition Handling Behaviors

| Behavior | Parameter Settings | Notes |
| --- | --- | --- |
| - Data integrity - Deterministic data transfer - Maximum latency | Select:  - **Ensure data integrity during data transfer** - **Ensure deterministic data transfer** | - Generated code transfers data so that the data bytes for the signal   (including elements of a wide signal) are from the same time step. - Relative sample time (delay) from which the data is transferred from one   rate to another is the same. - The code generator produces ANSI® C code only. - Target-specific critical-section protection is not needed. |
| - Data integrity - Nondeterministic data transfer - Minimum latency - Higher memory requirements | Select:  - **Ensure data integrity during data transfer**  Clear:  - **Ensure deterministic data transfer** | - Generated code transfers data so that data bytes for the signal (including   elements of a wide signal) are from the same time step. - Relative sample time (delay) for which the data is transferred can vary   from one transfer of data to the next. Code that reads and writes the data   runs more often than the case when you select **Ensure data integrity   during data transfer** and **Ensure deterministic data   transfer**. In the worst case scenario, the delay is equivalent to   when you select **Ensure data integrity during data   transfer** and **Ensure deterministic data   transfer**, but the delay can be less, which can be important for   some applications. - Supports data transfers to and from asynchronous rates. - The code generator produces ANSI C code only. - Target-specific critical-section protection is not needed. |
| - Potential loss of data integrity - Nondeterministic data transfer - Minimum latency - Lower memory requirements | Clear:  - **Ensure data integrity during data transfer** - **Ensure deterministic data transfer** | - Code generator does not generate code for the Rate   Transition block. - Acceptable for applications where atomic access of scalar data types is   guaranteed and when the relative temporal values of the data are not   important. - Delay is not introduced. |

The behavior of the Rate Transition block depends on:

- Sample times of the ports to which the block connects (see Effects of Synchronous Sample Times and Effects of Asynchronous Sample Times)
- Priorities of the tasks for the source and destination sample times (see Sample time properties)
- Whether the model specifies a fixed- or variable-step solver (see Compare Solvers)
- Setting of model configuration parameters **Device vendor** and
  **Device type** (see Effects of Device Configuration)

### Block Labels

When you update a model diagram, a label appears on the Rate Transition
block to indicate simulation behavior.

| Label | Block Behavior |
| --- | --- |
| `ZOH` | Acts as a zero-order hold |
| `1/z` | Acts as a unit delay |
| `Buf` | Copies input to output under semaphore control |
| `Db_buf` | Copies input to output by using double buffers |
| `3buf` | Copies input to output by using triple buffers |
| `Copy` | Unprotected copy of input to output |
| `NoOp` | No operation |
| `Mixed` | Expands to multiple blocks with different behaviors |
| `RT` | Indicates data transfer between partitions when using the Schedule Editor.  For more information, see Using the Schedule Editor. |
| `Memory` | Indicates memory mode. The block is in memory mode when **Ensure deterministic data transfer (maximum delay)** is cleared. |

The block behavior label shows the method that ensures safe transfer of data between
tasks operating at different rates. You can use the sample-time colors feature (see View Sample Time Information) to display the relative rates that the block
bridges. Consider this example model:

Model that includes Rate Transition blocks that handle a fast-to-slow rate transition and a slow-to-fast rate transition.

Sample-time colors and the block behavior labels show:

- The Rate Transition block at the top of the diagram acts as a
  zero-order hold in a fast-to-slow transition.
- The Rate Transition block at the bottom of the diagram acts as a unit
  delay in a slow-to-fast transition.

For more information, see Data Transfer Representation and Processing (Simulink Coder).

### Effects of Synchronous Sample Times

This table summarizes how each label appears when the sample times of the input and
output ports (`inTs` and `outTs`) are periodic, or
synchronous.

| Block Settings | | Block Label | | |
| --- | --- | --- | --- | --- |
| Rate Transition | Conditions for Rate Transition Block | With Data Integrity and Determinism | With Only Data Integrity | Without Data Integrity or Determinism |
| `inTs` = `outTs`  (Equal) | `inTsOffset` < `outTsOffset` | None (error) | `Buf` | `Copy` or `NoOp` (see note that follows the table) |
| `inTsOffset` = `outTsOffset` | `Copy` or `NoOp` (see note that follows the table) | `Copy` or `NoOp` (see note that follows the table) |
| `inTsOffset` > `outTsOffset` | None (error) | `Db_buf` |
| `inTs` < `outTs`  (Fast to slow) | `inTs` = `outTs / N`  `inTsOffset`, `outTsOffset` = 0 | `ZOH` | `Buf` |
| `inTs` = `outTs / N`  `inTsOffset` ≤ `outTsOffset` | None (error) |
| `inTs` = `outTs / N`  `inTsOffset` > `outTsOffset` | None (error) | `Db_buf` |
| `inTs` ≠ `outTs / N` | None (error) |
| `inTs` > `outTs`  (Slow to fast) | `inTs` = `outTs * N`  `inTsOffset`, `outTsOffset` = 0 | `1/z` | `Db_buf` |
| `inTs` = `outTs * N`  `inTsOffset` ≤ `outTsOffset` | None (error) |
| `inTs` = `outTs * N`  `inTsOffset` > `outTsOffset` | None (error) |
| `inTs` ≠ `outTs * N` | None (error) |
| **KEY**  - `inTs`, `outTs`: Sample times of input   and output ports, respectively - `inTsOffset`, `outTsOffset`: Sample time   offsets of input and output ports, respectively - `N`: Integer value > 1 | | | | |

**Note**

When you select model configuration parameter **Block reduction**,
`Copy` reduces to `NoOp`. No code generation occurs
for a Rate Transition block with a `NoOp` label. To
prevent a block from being reduced when block reduction is on, add a test point to the
block output (see Configure Signals as Test Points).

### Effects of Asynchronous Sample Times

This table summarizes how each label appears when the sample time of the input or output
port (`inTs` or `outTs`) is not periodic, or
asynchronous.

| Block Settings | | Block Label | | |
| --- | --- | --- | --- | --- |
| With Data Integrity and Determinism | With Only Data Integrity | Without Data Integrity or Determinism |
| `inTs` = `outTs` | | `Copy` | `Copy` | `Copy` |
| `inTs` ≠ `outTs` | | None (error) | `Db_buf` |
| **KEY**  - `inTs`, `outTs`: Sample times of input   and output ports, respectively | | | | |

### Effects of Device Configuration

If the settings of model configuration parameters **Device vendor**
and **Device type** specify hardware that supports atomic data load and
store operations, the code generator optimizes the generated rate transition code when the
target hardware supports atomic load and store operations for the data type of the signal
being transferred. The code generator takes advantage of the hardware data load and store
capability by replacing double-buffering code between asynchronous tasks with code that
performs a single memory copy.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix | N-D array

Input signal that transitions to a new sample rate, specified as a scalar, vector,
matrix, or N-D array. To learn about the block parameters that enable you to trade
data integrity and deterministic transfer for faster response or lower memory
requirements, see Transition Handling Behaviors.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### Output

### **Port\_1** — Output signal scalar | vector | matrix | N-D array

The input signal converted to the sample rate you specify. The default
configuration ensures safe and deterministic data transfer. To learn about the block
parameters that enable you to trade data integrity and deterministic transfer for
faster response or lower memory requirements, see Transition Handling Behaviors.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

### **Ensure data integrity during data transfer** — Ensure data integrity `on` (default) | `off`

Selecting this parameter results in generated code that ensures data integrity when
the block transfers data. If you select this parameter and the transfer is
nondeterministic (see **Ensure deterministic data transfer**),
depending on the priority of input rate and output rate, the generated code uses a
proper algorithm using single or multiple buffers to protect data integrity during data
transfer.

Otherwise, the Rate Transition block is reduced or generates code by
using a copy operation to affect the data transfer. This unprotected mode consumes less
memory. However, the copy operation is interruptible, which can lead to loss of data
integrity during data transfers. Select this parameter if you want the generated code to
operate with maximum responsiveness (that is, nondeterministically) and maintain data
integrity. For more information, see Control Data Transfer Behavior in Generated Code (Simulink Coder).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Integrity` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'on'` |

### **Ensure deterministic data transfer (maximum delay)** — Ensure deterministic data transfer `on` (default) | `off`

Selecting this parameter results in generated code that transfers data at the sample
rate of the slower block, that is, deterministically. If you do not select this
parameter, data transfers occur when new data is available from the source block and the
receiving block is ready to receive the data. You avoid transfer delays, thus ensuring
that the system operates with maximum responsiveness. However, transfers can occur
unpredictably, which is undesirable in some applications. For more information, see
Control Data Transfer Behavior in Generated Code (Simulink Coder).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Deterministic` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'on'` |

### **Initial conditions** — Initial conditions `0` (default) | scalar | vector | matrix | N-D array

This parameter applies only to slow-to-fast transitions. It specifies the initial
output of the Rate Transition block at the beginning of a transition,
when there is no output signal due to the absence of an input signal coming from the
slow block. Simulink® does not allow the initial output of this block to be
`Inf` or `NaN`. The value you specify must be a
scalar, or have the same dimensions as the input signal.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialCondition` |
| **Type:** character vector |
| **Values:** finite scalar |
| **Default:** `'0'` |

### **Output port sample time options** — Mode for specifying output port sample time `Specify` (default) | `Inherit` | `Multiple of input port sample time`

Specifies a mode for setting the output port sample time.

- `Specify` — Use the **Output port sample
  time** parameter to specify the output rate to which the block converts
  its input rate.
- `Inherit` —The block inherits an output rate
  from the block to which the output port is connected.
- `Multiple of input port sample time` — Use the
  **Sample time multiple (>0)** parameter to specify the block
  output rate as a multiple of its input rate.

If you select `Inherit` and blocks connected to the output
port also inherit sample time, the fastest sample time in the model applies.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutPortSampleTimeOpt` |
| **Type:** character vector |
| **Values:** `'Specify' | 'Inherit' | 'Multiple of input port sample time'` |
| **Default:** `'Specify'` |

### **Output port sample time** — Output rate `-1` (default) | scalar | vector

Enter a value that specifies the output rate to which the block converts its input
rate. The default value (`-1`) specifies that the Rate
Transition block inherits the output rate from the block to which the output
port is connected. See Specify Sample Time for information on
how to specify the output rate.

#### Dependencies

To enable this parameter, set **Output port sample time options**
to `Specify`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutPortSampleTime` |
| **Type:** character vector |
| **Values:** scalar | vector |
| **Default:** `'-1'` |

### **Sample time multiple (>0)** — Sample time multiple `1` (default) | positive scalar

Enter a positive value that specifies the output rate as a multiple of the input
port sample time. The default value (`1`) specifies that the output
rate is the same as the input rate. A value of `0.5` specifies that the
output rate is half of the input rate. A value of `2` specifies that
the output rate is twice the input rate.

#### Dependencies

To enable this parameter, set **Output port sample time options**
to `Multiple of input port sample time`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutPortSampleTimeMultiple` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'1'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

- Under certain conditions, such as for multidimensional signals, generated code
  relies on `memcpy` or `memset` functions
  (`string.h`).
- Do not use a Rate Transition block inside a triggered subsystem hierarchy.
- Generated code for concurrent programs is platform-specific and assumes that the
  deployment platform and development platform are the same.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides configuration options that affect HDL implementation and synthesized
logic.

**Best Practices**

- When the Rate Transition block is operating at a fast input rate
  and slow output rate, it is good practice to follow the Rate Transition
  block with a unit delay. Doing so prevents the code generator from inserting an extra
  bypass register in the HDL code. See also Multirate Model Requirements for HDL Code Generation (HDL Coder).
- To upsample the input signal without incurring a unit delay, configure
  Rate Transition block parameters as follows:

  - Clear **Ensure data integrity during data
    transfer**.

    Clearing this parameter hides the **Ensure deterministic data
    transfer (maximum delay)** parameter.
  - Configure the output port sample time of the block to be an integer multiple
    of the input port sample time. Specify a fractional value of
    `1/n` for **Sample time multiple**, where
    `n` is an integer. If **Sample time
    multiple** uses a value `1/n`, you can choose any
    value for the block parameter **Output port sample time**
    options.

  **Note**

  When downsampling the input signal, leave the **Ensure data integrity
  during data transfer** and **Ensure deterministic data transfer
  (maximum delay)** parameters selected. This mode generates an
  additional bypass register in the HDL code.

  See also Usage of Rate Change and Constant Blocks (HDL Coder).

**Restrictions**

- The sample rate cannot be `0` or `Inf` for
  block input or output ports.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **AsyncRTAsWire** | Map Asynchronous Rate Transition as Wire.  When **Output port sample time** has noninteger values, it is considered as an asynchronous rate. Enable the **AsyncRTAsWire** option to generate a wire when such asynchronous rates are present for the Rate Transition block.  **Dependencies:** This option is available only when the **Ensure data integrity during data transfer** and **Ensure deterministic data transfer** parameters are turned `off`.  When using asynchronous rate transition as wire, set **Clock inputs** option to `Multiple`. |

**Note**

While mapping the asynchronous rate transition as wire, you may see the numerical
mismatches between Simulink and Code Generation results.

**Complex Data Support**

This block supports code generation for complex signals.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
