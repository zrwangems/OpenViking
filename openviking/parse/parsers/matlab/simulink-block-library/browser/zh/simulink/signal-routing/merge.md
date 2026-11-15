---
type: simulink-block
title: 'Merge'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Signal Routing'
documentation_page: 'merge'
documentation_source_path: 'slref/merge.html'
language: zh-CN
chinese_source: official
---

# Merge

## 端口

### 输入

### **Port\_1** — 第一个输入信号 标量 | 向量

第一个输入信号与其他输入信号合并。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

### **Port\_n** — 第 *n* 个输入信号 标量 | 向量

第 *n* 个输入信号与其他输入信号合并。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

由输入信号合并而成的输出信号。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

## 参数

### **输入数目** — 要合并的输入信号的数量 `2` (默认) | `integer`

指定要合并的输入信号的数量。该模块为每个输入信号创建一个端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Inputs` |
| **类型：**字符向量 |
| **值：**整数 |
| **默认值：**`'2'` |

### **初始输出** — 初始输出值 [ ] (默认) | 标量 | 向量

指定输出信号的初始值。如果不指定初始输出值，初始输出将取决于初始化模式和驱动模块。

在 Simplified Initialization Mode 中，若未指定**初始输出**的值（空矩阵 `[]`），模块将使用输出数据类型的默认初始值。有关默认初始值的信息，请参阅初始化信号值。在 Classic Initialization Mode中，若未指定**初始输出**的值（空矩阵 `[]`），则模块的初始输出等于最近计算的驱动模块的初始输出。由于这些来源的初始化顺序可能不同，因此模型的仿真和代码生成的初始化可能不一致。

#### 编程用法

|  |
| --- |
| **模块参数**：`InitialOutput` |
| **类型：**字符向量 |
| **值：**标量 | 向量 |
| **默认值：**`'[ ]'` |

### **允许端口宽度不等** — 允许输入具有不同维度 `off` (默认) | `on`

选择此参数可允许模块接受元素数目彼此不同的输入，或接受与输出具有不同元素数目的输入。模块还允许您为每个输入信号指定相对于输出信号开始时的偏移量。输出信号的宽度为

```
max(w1+o1, w2+o2, ... wn+on)
```

其中 `w1`, ... `wn` 是输入信号的宽度，`o1`, ... `on` 是输入信号的偏移量。

如果清除该参数，Merge 模块只接受相同维度的输入，并输出与输入具有相同维度的信号。

**注意**

除非您的模型在使用经典初始化模式，否则不要选择此参数。

#### 编程用法

|  |
| --- |
| **模块参数**：`AllowUnequalInputPortWidths` |
| **类型：**字符向量 |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` |

### **输入端口偏移量** — 输入信号的偏移量 `[ ]` (默认) | 向量

输入向量以指定每个输入信号相对于输出信号开始时的偏移量。

#### 依赖关系

要启用此参数，请选择**允许端口宽度不等**。

#### 编程用法

|  |
| --- |
| **模块参数**：`InputPortOffsets` |
| **类型：**字符向量 |
| **值：**标量 | 向量 |
| **默认值：**`'[ ]'` |

## 所属库

Simulink / Signal Routing HDL Coder / Ports & Subsystems

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `image` | `integer` | `single` | `string` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

在代码生成工作流中，当 Merge 模块接收常数值和非常数采样时间时，必须满足以下条件之一。否则 Simulink 将显示错误。

- 常量值的来源是接地信号。
- 常量值的来源是具有不可调参数的常量模块。

  - 只有一个常量模块为 Merge 模块提供值。
  - Merge 模块的所有其他输入信号都来自条件执行子系统。
  - Merge 模块以及所有条件执行子系统的 Outport 模块不指定任何初始输出。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

当在 For Each Subsystem 模块中使用此模块时，不支持代码生成。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

将多个信号合并为一个信号

Merge 模块可将多个输入合并为单个输出。输出值始终等于其驱动模块最近计算的输出。通过设置**输入数目**参数来指定输入数目。

请将一个 Merge 模块用于将在不同时间更新的输入信号交叉成一个合并信号，交叉值在合并信号中保留其各自的身份和时间。要将同时更新的信号合并成数组或矩阵信号，请使用 Concatenate 模块。

### Merge 模块的使用原则

使用 Merge 模块时，请遵循以下原则：

- 始终使用条件执行子系统来驱动 Merge 模块，而不涉及任何中间模块。
- 确保在任何时间步都最多只有一个驱动条件执行子系统在执行中。
- 确保所有输入信号具有相同的采样时间。
- 不要为 Merge 模块的输入信号创建分支。
- 不要记录输入到 Merge 模块的信号。
- 不要指定 Merge 模块的模块执行优先级。有关详细信息，请参阅指定模块执行顺序、执行优先级和标记。
- 对于驱动 Merge 模块的所有条件执行子系统 Outport 模块，请将**禁用时的输出**设置为**保持**。
- 如果 Model 模块的输出来自 MATLAB Function 模块或 Stateflow® 图，不要将该输出端口连接到 Merge 模块的输入端口。
- Merge 模块支持将不同任务中的信号合并到一个根 Outport 模块。

对于一个 Merge 模块的每个输入，最顶层的非虚拟源必须为条件执行子系统（不包括 For Iterator 或 While Iterator 子系统）。

下一个图显示了有效的 Merge 模块用法，它合并来自两个条件执行子系统的信号。

### 总线支持

Merge 模块支持总线。输入可以是满足下列限制条件的虚拟或非虚拟总线信号：

- 输入数目必须大于一。
- **初始输出**必须为零、非零标量或有限数值结构体。
- 必须清除**允许端口宽度不等**复选框。
- 所有输入都必须为总线且必须相同（所有元素的层次结构相同，并具有相同的名称和属性）。

Merge 模块的非虚拟总线输入中的所有信号必须具有相同的采样时间。您可以使用 Rate Transition 模块更改总线中单个信号或所有信号的采样时间。

### 合并 S-Function 输出

对于来自 S-Function 模块的信号，仅当用来存储 S-Function 模块输出的内存可重用时，才能使用 Merge 模块合并该信号。如果某个模型将不可重用的 S-Function 模块端口连接到 Merge 模块，则当您尝试更新或仿真模型时，Simulink® 将显示错误消息。请参阅 `ssSetOutputPortOptimOpts`。

### 多任务根输出

连接到一个根 Outport 模块的 Merge 模块允许合并不同任务中的信号，方法是允许这些信号同时写入该根 Outport 模块。源的联合采样时间会赋给该 Merge 模块。

同一任务中的 Merge 模块的所有源均应在条件执行子系统中，且这些子系统不应在同一时间步中同时输出。
