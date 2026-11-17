---
type: simulink-block
title: 'Merge'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Ports & Subsystems'
documentation_page: 'merge'
documentation_source_path: '../simulink/slref/merge.html'
language: zh-CN
chinese_source: worker-translation
---

# Merge

## 端口
```yaml
ports:
- name: Port_1
  summary: 第一个输入信号 标量 | 向量
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus | image
- name: Port_n
  summary: 第 *n* 个输入信号 标量 | 向量
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus | image
- name: Port_1
  summary: 输出信号 标量 | 向量
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus | image
```

### 输入

### **Port\_1** — 第一个输入信号 标量 | 向量

与其他输入信号合并的第一个输入信号。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

### **Port\_n** — 第 *n* 个输入信号 标量 | 向量

与其他输入信号合并的第 *n* 个输入信号。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

由输入信号合并而成的输出信号。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
## 参数
```yaml
parameters:
- name: 输入数量
  summary: 要合并的输入信号数量 2（默认）| 整数
  group: ''
  block_parameter: Inputs
  type: 字符向量
  values: 整数
  default: '''2'''
- name: 初始输出
  summary: 初始输出值 [ ]（默认）| 标量 | 向量
  group: ''
  block_parameter: InitialOutput
  type: 字符向量
  values: 标量 | 向量
  default: '''[ ]'''
- name: 允许不相等的端口宽度
  summary: 允许维度不相等的输入 off（默认）| on
  group: ''
  block_parameter: AllowUnequalInputPortWidths
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''off'''
- name: 输入端口偏移量
  summary: 输入信号的偏移量 [ ]（默认）| 向量
  group: ''
  block_parameter: InputPortOffsets
  type: 字符向量
  values: 标量 | 向量
  default: '''[ ]'''
```

### **输入数量** — 要合并的输入信号数量 `2`（默认）| `整数`

指定要合并的输入信号数量。该模块为每个输入信号创建一个端口。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Inputs` |
| **类型：** 字符向量 |
| **值：** 整数 |
| **默认值：** `'2'` |

### **初始输出** — 初始输出值 [ ]（默认）| 标量 | 向量

指定输出信号的初始值。如果未指定初始输出值，则初始输出取决于初始化模式和驱动模块。

在简化初始化模式下，对于未指定的（空矩阵 `[]`）**初始输出**值，该模块使用输出数据类型的默认初始值。有关默认初始值的信息，请参阅初始化信号值。在经典初始化模式下，对于未指定的（空矩阵 `[]`）**初始输出**值，该模块的初始输出等于驱动模块最近一次求值的初始输出。由于这些源的初始化顺序可能不同，因此模型的仿真和代码生成的初始化可能不一致。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InitialOutput` |
| **类型：** 字符向量 |
| **值：** 标量 | 向量 |
| **默认值：** `'[ ]'` |

### **允许不相等的端口宽度** — 允许维度不相等的输入 `off`（默认）| `on`

选择此参数以允许该模块接受彼此之间或与输出之间具有不同元素数量的输入。该模块允许您为每个输入信号指定相对于输出信号起始位置的偏移量。输出信号的宽度为

```
max(w1+o1, w2+o2, ... wn+on)
```

其中 `w1`、...、`wn` 是输入信号的宽度，`o1`、...、`on` 是输入信号的偏移量。

如果清除此参数，Merge 模块仅接受维度相等的输入，并输出与输入维度相同的信号。

**注意**

除非您的模型使用经典初始化模式，否则不要选择此参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `AllowUnequalInputPortWidths` |
| **类型：** 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **输入端口偏移量** — 输入信号的偏移量 `[ ]`（默认）| 向量

输入一个向量以指定每个输入信号相对于输出信号起始位置的偏移量。

#### 依赖关系

要启用此参数，请选择**允许不相等的端口宽度**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InputPortOffsets` |
| **类型：** 字符向量 |
| **值：** 标量 | 向量 |
| **默认值：** `'[ ]'` |
## 所属库

Simulink / Signal Routing HDL Coder / Ports & Subsystems

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `image` | `integer` | `single` | `string` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

在代码生成工作流中，当 Merge 模块接收到常量值和非恒定采样时间时，必须满足以下条件之一。否则 Simulink 会显示错误。

- 常量值的源是接地信号。
- 常量值的源是具有不可调参数的常量模块。

  - 只有一个常量模块馈入 Merge 模块。
  - 馈入 Merge 模块的所有其他输入信号均来自条件执行子系统。
  - Merge 模块以及所有条件执行子系统的输出端口模块未指定任何初始输出。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

当此模块在 For Each Subsystem 模块内部使用时，不支持代码生成。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

将多个信号合并为单个信号

Merge 模块将多个输入合并为单个输出。任意时刻的输出值等于其驱动模块最近一次计算的输出。通过设置**输入数量**参数来指定输入数量。

使用 Merge 模块将不同时间更新的输入信号交织成一个组合信号，其中交织的值保留其各自的身份和时间。要将同时更新的信号组合成数组或矩阵信号，请使用 Concatenate 模块。

### 使用 Merge 模块的准则

使用 Merge 模块时，请遵循以下准则：

- 始终使用条件执行子系统来驱动 Merge 模块，中间不得有任何其他模块。
- 确保在任何时间步最多只有一个驱动条件执行子系统执行。
- 确保所有输入信号具有相同的采样时间。
- 不要对输入到 Merge 模块的信号进行分支。
- 不要记录输入到 Merge 模块的信号。
- 不要指定 Merge 模块的模块执行优先级。有关更多信息，请参阅指定模块执行顺序、执行优先级和标签。
- 对于所有驱动 Merge 模块的条件执行子系统输出端口模块，将**禁用时输出**设置为 `held`。
- 如果 Model 模块的输出来自 MATLAB Function 模块或 Stateflow® 图，请不要将该输出端口连接到 Merge 模块的输入端口。
- Merge 模块支持将不同任务中的信号合并到根 Outport 模块。

对于 Merge 模块的每个输入，最顶层的非虚拟源必须是条件执行子系统（不包括 For Iterator 或 While Iterator 子系统）。

下图显示了有效的 Merge 模块用法，即合并来自两个条件执行子系统的信号。

### 总线支持

Merge 模块是支持总线的模块。输入可以是虚拟或非虚拟总线信号，但受以下限制：

- 输入数量必须大于一。
- **初始输出**必须为零、非零标量或有限数值结构体。
- 必须清除**允许不相等的端口宽度**复选框。
- 所有输入必须是总线，并且必须等效（所有元素具有相同的层次结构、相同的名称和属性）。

输入到 Merge 模块的非虚拟总线中的所有信号必须具有相同的采样时间。您可以使用 Rate Transition 模块来更改单个信号或总线中所有信号的采样时间。

### 合并 S-Function 输出

仅当用于存储 S-Function 模块输出的内存可复用时，Merge 模块才能合并来自 S-Function 模块的信号。如果您尝试更新或仿真将 S-Function 模块的不可复用端口连接到 Merge 模块的模型，Simulink® 会显示错误消息。请参阅 `ssSetOutputPortOptimOpts`。

### 多任务根输出

连接到根 Outport 模块的 Merge 模块允许合并不同任务中的信号，方法是允许这些信号同时写入根 Outport 模块。源的 Union 采样时间被分配给 Merge 模块。

Merge 模块中位于同一任务的所有源应位于条件执行子系统内，这些子系统不应在同一时间步同时输出。
