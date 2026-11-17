---
type: simulink-block
title: 'Variable Selector'
family: 'signal-management'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Management / Indexing'
documentation_page: 'variableselector'
documentation_source_path: 'ref/variableselector.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable Selector

## 端口

### 输入

### **InN** — 第 *N* 个输入信号 标量 | 向量 | 矩阵

第 *N* 个输入信号，其中 *N* 是在 Number of input signals 参数中指定的输入数量。

当输入为未定向向量时，Select 参数被忽略，输出是长度为 *L* 的未定向向量，其中包含由长度为 *L* 的索引向量指定的那些元素。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
**复数支持：** Yes

### **Idx** — 索引向量 标量 | 向量

指定一个标量值或向量，其中包含出现在输出矩阵中的输入行或列的索引。

#### 依赖关系

仅当将 Selector mode 设置为 `Variable` 时，此端口才会出现。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
### 输出

### **OutN** — 第 *N* 个输出信号 标量 | 向量 | 矩阵

第 *N* 个输出信号，对应于第 *N* 个输入信号，其中 *N* 是在 Number of input signals 参数中指定的输入数量。输出以标量、向量或矩阵形式返回，其类型、大小和复/实性与对应输入相同。

对于 variable 和 fixed 索引模式，行选择操作等效于

```
y = u(idx,:)						% Equivalent MATLAB code
```

列选择操作等效于

```
y = u(:,idx)						% Equivalent MATLAB code
```

其中 `idx` 是长度为 *L* 的索引向量。行选择输出大小为 *L*×*N*，列选择输出大小为 *M*×*L*。输入行或列可以在输出中出现任意次数，或者完全不出现。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

## 参数

### **Number of input signals** — 输入数量 `1` (默认) | 正整数

将输入信号数指定为正整数。模块会为每个输入信号创建一个输入端口。

### **Select** — 选择维度 `Rows` (默认) | `Columns`

指定要选择的输入维度，`Rows` 或 `Columns`。

当 **Select** 设置为：

- `Rows` –– 模块从每个输入矩阵中提取行。
- `Columns` –– 模块从每个输入矩阵中提取列。

当输入为未定向向量时，**Select** 参数被忽略。输出是长度为 *L* 的未定向向量，其中包含由长度为 *L* 的索引向量指定的那些元素。

### **Selector mode** — 索引模式 `Variable` (默认) | `Fixed`

指定要执行的索引操作类型，`Variable` 或 `Fixed`。

当 **Selector mode** 设置为：

- `Variable` –– Idx 端口接收的长度为 *L* 的向量输入选择每个输入的 *L* 行或列传递到输出。您可以在每个采样时间更新索引向量的元素，但向量长度在整个仿真过程中必须保持不变。
- `Fixed` –– **Idx** 端口被禁用。您在 Elements 参数中指定的长度为 *L* 的向量选择每个输入的 *L* 行或列传递到输出。**Elements** 参数可调，因此您可以在仿真期间随时更改索引向量元素的值，但向量长度必须保持不变。

### **Elements** — 选定的元素 `[1 3]` (默认) | 标量 | 向量

指定一个向量，其中包含出现在输出矩阵中的输入行或列的索引。

**可调：** Yes

#### 依赖关系

仅当将 Selector mode 设置为 `Fixed` 时，此参数才会出现。

### **Index mode** — 索引模式 `Zero-based` (默认) | `One-based`

当设置为 `One-based` 时，索引值 `1` 指输入的第一行或第一列。当设置为 `Zero-based` 时，索引值 `0` 指输入的第一行或第一列。

### **Invalid index** — 错误处理 `Clip Index` (默认) | `Clip and Warn` | `Generate Error`

指定模块如何处理无效索引值。您可以选择以下选项之一：

- `Clip index` — 将索引裁剪到最近的有效值，并且不发出警报。

  例如，如果模块接收 `64`×`4` 输入，并且 Select 参数设置为：

  - `Rows` –– 模块将索引 `72` 裁剪到 `64`。
  - `Columns` –– 模块将索引 `72` 裁剪到 `4`。

  在两种情况下，模块将索引 `-2` 裁剪到 `1`。
- `Clip and warn` — 将索引裁剪到最近的有效值，并在 MATLAB® 命令行显示警告消息。
- `Generate error` — 显示错误对话框并终止仿真。

**可调：** Yes

### **Fill empty spaces in outputs (for logical indexing)** — 填充输出中的空位 `on` (默认) | `off`

当索引向量元素为 Boolean 数据类型时，模块执行逻辑索引。逻辑索引可能导致输出中出现空位。选择此参数可指定要在 Fill values 参数中追加到输出的值。

### **Fill values** — 填充值 `0` (默认) | 标量值 | 整数

指定模块执行逻辑索引时的填充值。

#### 依赖关系

仅当选择 Fill empty spaces in outputs (for logical indexing) 参数时，此参数才会出现。

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

生成的代码在某些条件下依赖 `memcpy` 或 `memset` 函数（`string.h`）。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出处放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线阶段数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线阶段数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**复数数据支持**

此模块支持复数信号的代码生成。

## 版本历史

**在 R2006a 之前引入**

## 描述

从输入中选择行或列的子集

Variable Selector 模块在每个输入端口从 *M*×*N* 输入矩阵 `u` 中提取行或列的子集。您在 **Number of input signals** 参数中指定输入和输出端口的数量。

当索引向量的元素引用输入中不存在的行或列时，模块实现您通过 **Invalid index** 参数指定的操作。

当索引向量元素为 Boolean 数据类型时，模块执行逻辑索引。选择 **Fill empty spaces in outputs (for logical indexing)** 以访问 **Fill values** 参数。这些值会追加到输出，使其与输入元素一样长。

**注意**

Variable Selector 模块始终将选定的输入行或列复制到连续内存块（不同于 Simulink® Selector 模块）。
