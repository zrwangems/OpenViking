---
type: simulink-block
title: 'Variable Selector'
family: 'dsp-system-toolbox-hdl-support'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Management'
documentation_page: 'variableselector'
documentation_source_path: 'ref/variableselector.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable Selector

## 端口
```yaml
ports:
- name: InN
  summary: 第 *N* 个输入信号 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated
- name: Idx
  summary: 索引向量 标量 | 向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated
- name: OutN
  summary: 第 *N* 个输出信号 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated
```

### 输入

### **InN** — 第 *N* 个输入信号 标量 | 向量 | 矩阵

第 *N* 个输入信号，其中 *N* 是在 Number of input signals 参数中指定的输入数量。

当输入为非定向向量时，Select 参数被忽略，输出为长度为 *L* 的非定向向量，其中包含由长度为 *L* 的索引向量指定的那些元素。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
**复数支持：** 是

### **Idx** — 索引向量 标量 | 向量

指定一个标量值或向量，其中包含出现在输出矩阵中的输入行或列的索引。

#### 依赖关系

此端口仅在将 Selector mode 设置为 `Variable` 时出现。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
### 输出

### **OutN** — 第 *N* 个输出信号 标量 | 向量 | 矩阵

第 *N* 个输出信号，对应于第 *N* 个输入信号，其中 *N* 是在 Number of input signals 参数中指定的输入数量。输出以标量、向量或矩阵形式返回，其类型、大小和复杂度与对应的输入相同。

对于可变和固定索引模式，行选择操作等效于

```
y = u(idx,:)						% Equivalent MATLAB code
```

列选择操作等效于

```
y = u(:,idx)						% Equivalent MATLAB code
```

其中 `idx` 是长度为 *L* 的索引向量。行选择的输出大小为 *L*×*N*，列选择的输出大小为 *M*×*L*。输入行或列可以在输出中出现任意次数，也可以不出现。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
## 参数
```yaml
parameters:
- name: Number of input signals
  summary: 输入数量 1（默认）| 正整数
  group: ''
- name: Select
  summary: 选择维度 Rows（默认）| Columns
  group: ''
- name: Selector mode
  summary: 索引模式 Variable（默认）| Fixed
  group: ''
- name: Elements
  summary: 选定的元素 [1 3]（默认）| 标量 | 向量
  group: ''
- name: Index mode
  summary: 索引模式 Zero-based（默认）| One-based
  group: ''
- name: Invalid index
  summary: 错误处理 Clip Index（默认）| Clip and Warn | Generate Error
  group: ''
- name: Fill empty spaces in outputs (for logical indexing)
  summary: 填充输出中的空白空间 on（默认）| off
  group: ''
- name: Fill values
  summary: 填充值 0（默认）| 标量值 | 整数
  group: ''
```

### **Number of input signals** — 输入数量 `1`（默认）| 正整数

将输入信号数量指定为正整数。每个输入信号在模块上创建一个输入端口。

### **Select** — 选择维度 `Rows`（默认）| `Columns`

指定要选择的输入维度，`Rows` 或 `Columns`。

当 **Select** 设置为：

- `Rows` —— 模块从每个输入矩阵中提取行。
- `Columns` —— 模块从每个输入矩阵中提取列。

当输入为非定向向量时，**Select** 参数被忽略。输出为长度为 *L* 的非定向向量，其中包含由长度为 *L* 的索引向量指定的那些元素。

### **Selector mode** — 索引模式 `Variable`（默认）| `Fixed`

指定要执行的索引操作类型，`Variable` 或 `Fixed`。

当 **Selector mode** 设置为：

- `Variable` —— Idx 端口的长度为 *L* 的向量输入选择每个输入的 *L* 行或列传递到输出。您可以在每个采样时间更新索引向量的元素，但向量长度在整个仿真过程中必须保持不变。
- `Fixed` —— **Idx** 端口被禁用。您在 Elements 参数中指定的长度为 *L* 的向量选择每个输入的 *L* 行或列传递到输出。**Elements** 参数是可调的，因此您可以在仿真过程中的任何时间更改索引向量元素的值，但向量长度必须保持不变。

### **Elements** — 选定的元素 `[1 3]`（默认）| 标量 | 向量

指定一个向量，其中包含出现在输出矩阵中的输入行或列的索引。

**可调：** 是

#### 依赖关系

此参数仅在将 Selector mode 设置为 `Fixed` 时出现。

### **Index mode** — 索引模式 `Zero-based`（默认）| `One-based`

当设置为 `One-based` 时，索引值 `1` 指代输入的第一行或第一列。当设置为 `Zero-based` 时，索引值 `0` 指代输入的第一行或第一列。

### **Invalid index** — 错误处理 `Clip Index`（默认）| `Clip and Warn` | `Generate Error`

指定模块如何处理无效索引值。您可以选择以下选项之一：

- `Clip index` —— 将索引裁剪到最近的有效值，并且不发出警报。

  例如，如果模块接收 `64`×`4` 的输入，并且 Select 参数设置为：

  - `Rows` —— 模块将索引 `72` 裁剪为 `64`。
  - `Columns` —— 模块将索引 `72` 裁剪为 `4`。

  在这两种情况下，模块将索引 `-2` 裁剪为 `1`。
- `Clip and warn` —— 将索引裁剪到最近的有效值，并在 MATLAB® 命令行显示警告消息。
- `Generate error` —— 显示错误对话框并终止仿真。

**可调：** 是

### **Fill empty spaces in outputs (for logical indexing)** — 填充输出中的空白空间 `on`（默认）| `off`

当索引向量元素为布尔数据类型时，模块执行逻辑索引。逻辑索引可能导致输出中出现空白空间。选择此参数以指定要追加到输出中的值，在 Fill values 参数中设置。

### **Fill values** — 填充值 `0`（默认）| 标量值 | 整数

指定模块执行逻辑索引时的填充值。

#### 依赖关系

此参数仅在您选择 Fill empty spaces in outputs (for logical indexing) 参数时出现。
## 所属库

DSP System Toolbox / Signal Management / Indexing DSP System Toolbox HDL Support / Signal Management

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**复数数据支持**

此模块支持复数信号的代码生成。

## 版本历史

**在 R2006a 之前引入**

## 描述

从输入中选择行或列的子集

Variable Selector 模块在每个输入端口从 *M*×*N* 输入矩阵 `u` 中提取行或列的子集。您在 **Number of input signals** 参数中指定输入和输出端口的数量。

当索引向量的元素引用输入中不存在的行或列时，模块执行您通过 **Invalid index** 参数指定的操作。

当索引向量元素为布尔数据类型时，模块执行逻辑索引。选择 **Fill empty spaces in outputs (for logical indexing)** 以访问 **Fill values** 参数。这些值被追加到输出中，使其与输入元素一样长。

**注意**

Variable Selector 模块始终将选定的输入行或列复制到连续的内存块（与 Simulink® Selector 模块不同）。
