---
type: simulink-block
title: 'Environment Controller'
family: signal-routing
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'environmentcontroller'
---

# Environment Controller

(Removed) Create branches of block diagram that apply only to simulation or only to code generation

## 中文

（已移除）创建仅适用于仿真或仅适用于代码生成的框图分支

### 库

Simulink / Signal Routing

### 描述

Environment Controller 模块仅当包含它的模型正在仿真时，才在其 **Sim** 端口输出信号。仅当从该模型生成代码时，才在其 **Coder** 端口输出信号。此选项使您能够创建仅适用于仿真或代码生成的框图分支。下表描述了 **Sim** 或 **Coder** 端口适用的各种场景。

| 场景 | 输出 |
| --- | --- |
| 正常模式仿真 | **Sim** |
| 加速模式仿真 | **Sim** |
| 快速加速模式仿真 | **Sim** |
| 在正常或加速模式下仿真被引用模型 | **Sim** |
| 在 processor-in-the-loop (PIL) 模式下仿真被引用模型 | **Coder**（使用为被引用模型生成的相同代码） |
| 外部模式仿真 | **Coder** |
| 标准代码生成 | **Coder** |
| 被引用模型的代码生成 | **Coder** |

Simulink® Coder™ 软件在满足以下条件时，不会为连接到 **Sim** 端口的模块生成代码：

- 在 Configuration Parameters 对话框的 **Code Generation > Optimization** 窗格中，将 **Default parameter behavior** 设置为 `Inlined`。
- 连接到 **Sim** 端口的模块没有外部信号。
- **Sim** 端口输入路径不包含 S-function 或 Interpreted MATLAB Function 模块。

如果启用 Block reduction 优化，Simulink 在为仿真编译模型时会消除连接到 **Coder** 端口的分支中的模块。有关详细信息，请参阅 Block reduction。

**注意**

Simulink Coder 代码生成仅当仿真分支与代码生成分支具有相同的信号维度时，才会消除连接到仿真分支的模块。无论是否消除仿真分支，Simulink Coder 都会使用仿真分支以及代码生成分支上的采样时间来确定生成代码的基本采样时间，并且在某些情况下，可能会生成仅适用于仿真分支上指定的采样时间的采样时间处理代码。

### 端口

#### 输入

#### **Sim** — 仿真输入 标量 | 向量 | 矩阵

仿真输入值，指定为标量、向量或矩阵。输入信号必须与 **Coder** 端口的输入具有相同的宽度。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

#### **Coder** — 代码生成输入 标量 | 向量 | 矩阵

代码生成输入值，指定为标量、向量或矩阵。输入信号必须与 **Sim** 端口的输入具有相同的宽度。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

#### 输出

#### **Out** — 来自仿真或代码生成输入端口的值 标量 | 向量 | 矩阵

来自 **Sim** 或 **Coder** 输入端口的值，具体取决于当前环境。有关该模块在各种仿真和代码生成模式下输出的详细信息，请参阅描述。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

### 扩展功能

#### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

不推荐用于生产代码。涉及嵌入式系统中常见的资源限制以及对速度和内存的限制。生成的代码可能包含动态内存分配和释放、递归、额外内存开销以及变化很大的执行时间。虽然代码在功能上有效，并且在资源丰富的环境中通常可接受，但较小的嵌入式目标往往无法支持此类代码。通常，模块会逐渐演变为适合生产代码。因此，适合生产代码的模块仍然适合。

#### 定点转换
使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史

**在 R2006a 之前引入**

#### R2021b：Environment Controller 模块已被移除

Environment Controller 模块已从 Signal Routing 库中移除。使用此模块的现有模型将继续工作，但会发出警告。请改用 Variant Source 模块，并将 **Variant control mode** 参数设置为 `sim codegen switching`。您可以使用 Model Advisor 或 Upgrade Advisor 自动识别所有 Environment Controller 模块实例，并将其替换为 Variant Source 模块。有关 Model Advisor 检查的信息，请参阅识别 Environment Controller 模块并将其替换为 Variant Source 模块。

Variant 模块相比 Environment Controller 模块具有以下优势：

- 将 Variant Source 模块的 **Variant control mode** 参数设置为 `sim codegen switching`，可让您在仿真和代码生成工作流之间自动切换。在此模式下，Variant Source 模块支持以下激活时间：

  | Variant 激活时间 | 行为 |
  | --- | --- |
  | `update diagram` | Simulink 在更新图期间、信号属性传播之前设置活动选择。非活动选择在信号属性传播之前被移除，因此生成的代码仅包含活动选择。 |
  | `update diagram analyze all choices` | Simulink 在更新图期间、信号属性传播之后设置活动选择。信号属性会传播到活动选择和非活动选择，以检查一致性。非活动选择在模型启动之前、更新图结束时被移除。生成的代码仅包含活动选择。 |

- Variant Sink 模块支持在输出侧（信号的目标）进行分支。
- Variant 模块在仿真和代码生成期间高亮显示活动 variant 选择的路径。
- 与 Environment Controller 模块相比，Variant Source 模块提供最优的代码生成。Environment Controller 模块可能会在生成的代码中保留连接到 **Sim** 端口的模块。
- 可以使用 Variant Manager 工具集中管理 Variant 模块，该工具提供以下关键功能：

  - 可视化 variant 模型层次结构。
  - 定义并验证模型的多个 variant 配置。
  - 使用 Variant Reducer 工具为某个 variant 配置生成简化模型。对于将 **Variant control mode** 参数设置为 `sim codegen switching` 的 variant 模块，您可以选择在简化模型中保留仿真分支或代码生成分支。
  - 使用 Variant Configuration Analysis 工具比较 variant 配置。

  有关详细信息，请参阅 Variant Manager for Simulink。

## Libraries

Simulink / Signal Routing

## Description

The Environment Controller block outputs the signal at its
**Sim** port only if the model that contains it is being simulated.
It outputs the signal at its **Coder** port only if code is being
generated from the model. This option enables you to create branches of a block diagram
that apply only to simulation or code generation. This table describes various scenarios
where either the **Sim** or **Coder** port
applies.

| Scenario | Output |
| --- | --- |
| Normal mode simulation | **Sim** |
| Accelerator mode simulation | **Sim** |
| Rapid accelerator mode simulation | **Sim** |
| Simulation of a referenced model in normal or accelerator modes | **Sim** |
| Simulation of a referenced model in processor-in-the-loop (PIL) mode | **Coder**  (uses the same code generated for a referenced model) |
| External mode simulation | **Coder** |
| Standard code generation | **Coder** |
| Code generation of a referenced model | **Coder** |

Simulink®
Coder™ software does not generate code for blocks connected to the
**Sim** port if these conditions hold:

- On the **Code Generation > Optimization** pane of the
  Configuration Parameters dialog box, you set **Default parameter
  behavior** to `Inlined`.
- The blocks connected to the **Sim** port do not have external
  signals.
- The **Sim** port input path does not contain an S-function or
  an Interpreted MATLAB Function block.

If you enable block reduction optimization, Simulink eliminates blocks in the branch connected to the
**Coder** port when compiling the model for simulation. For more
information, see Block reduction.

**Note**

Simulink
Coder code generation eliminates the blocks connected to the simulation
branch only if the simulation branch has the same signal dimensions as the code
generation branch. Regardless of whether it eliminates the simulation branch,
Simulink
Coder uses the sample times on the simulation branch as well as the code
generation branch to determine the fundamental sample time of the generated code and
might, in some cases, generate sample-time handling code that applies only to sample
times specified on the simulation branch.

## Ports

### Input

### **Sim** — Simulation input scalar | vector | matrix

Simulation input values, specified as a scalar, vector, or matrix.
Input signal must have the same width as the input to the
**Coder** port.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **Coder** — Code generation input scalar | vector | matrix

Code generation input values, specified as a scalar, vector, or
matrix. Input signal must have the same width as the input to the
**Sim** port.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### Output

### **Out** — Values from simulation or code generation input port scalar | vector | matrix

Values from the **Sim** or **Coder**
input port, depending on the current environment. For more information
on what the block outputs in various simulation and code generation
modes, see Description.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production code. Relates to resource limits and restrictions on speed
and memory often found in embedded systems. Generated code can contain dynamic
allocation and freeing of memory, recursion, additional memory overhead, and
widely-varying execution times. While the code is functionally valid and generally
acceptable in resource-rich environments, smaller embedded targets often cannot
support such code. Usually, blocks evolve toward being suitable for production code.
Thus, blocks suitable for production code remain suitable.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2021b: Environment Controller block has been removed

The Environment Controller block has been removed from the Signal
Routing library. Existing models that use this block continue to work with a
warning. Use the Variant Source block with the
**Variant control mode** parameter set to `sim codegen
switching` instead. You can use Model Advisor or Upgrade Advisor to
automatically identify and replace all instances of the Environment
Controller block with the Variant Source block. For
information on the Model advisor check, see Identify Environment Controller Blocks and Replace Them with Variant Source Blocks.

Variant blocks offer these advantages over the Environment
Controller block:

- Variant Source block with the **Variant control
  mode** parameter set to `sim codegen
  switching` allows you to automatically switch between
  simulation and code generation workflows. In this mode, Variant
  Source block supports these activation times:

  | Variant activation time | Behavior |
  | --- | --- |
  | `update diagram` | Simulink sets the active choice during update diagram before the propagation of signal attributes. Inactive choices are removed prior to propagation of signal attributes, so the generated code contains only the active choice. |
  | `update diagram analyze all choices` | Simulink sets the active choice during update diagram after the propagation of signal attributes. Signal attributes are propagated to both active and inactive choices to check for consistency. Inactive choices are removed at the end of update diagram before model start occurs. The generated code contains only active choices. |
- Variant Sink block enables branching on the output side
  (destination of a signal).
- Variant blocks highlight the path of the active variant choice during
  simulation and code generation.
- Variant Source block offers optimal code generation
  compared to the Environment Controller block. The
  Environment Controller block can retain blocks
  connected to the **Sim** port in the generated
  code.
- Variant blocks can be centrally managed using the Variant Manager
  tool, which offers these key capabilities:

  - Visualize the variant model hierarchy.
  - Define and validate multiple variant configurations of the
    model.
  - Generate a simplified model for a variant configuration
    using the Variant Reducer tool. For variant blocks with the
    **Variant control mode** parameter set
    to `sim codegen switching`, you can choose
    to retain the simulation branch or the code generation
    branch in the reduced model.
  - Compare variant configurations using the Variant
    Configuration Analysis tool.

  For more information, see Variant Manager for Simulink.
