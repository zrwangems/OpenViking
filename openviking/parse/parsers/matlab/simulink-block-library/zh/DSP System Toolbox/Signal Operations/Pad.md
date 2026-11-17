---
type: simulink-block
title: 'Pad'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Operations'
documentation_page: 'pad'
documentation_source_path: 'ref/pad.html'
language: zh-CN
chinese_source: worker-translation
---

# Pad

## 端口
```yaml
ports:
- name: Input 1
  summary: 数据输入 标量 | 向量 | 矩阵 | *N* 维数组
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    bus
- name: Output 1
  summary: 填充或截断后的输出 标量 | 向量 | 矩阵 | *N* 维数组
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    bus
```

### 输入

### **Input 1** — 数据输入 标量 | 向量 | 矩阵 | *N* 维数组

将输入指定为标量、向量、矩阵或 *N* 维数组。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`
**复数支持：** 是
### 输出

### **Output 1** — 填充或截断后的输出 标量 | 向量 | 矩阵 | *N* 维数组

Pad 模块的输出。输出的大小和维度取决于模块是沿指定维度对输入进行了填充还是截断。输出的数据类型和复数特性与输入一致。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Pad over
  summary: 进行填充或截断的维度 Columns（默认） | Rows | Columns and rows | None | Specified dimensions
  group: ''
- name: Dimensions to pad
  summary: 指定进行填充或截断的维度 1（默认） | 标量 | 向量
  group: ''
- name: Pad value source
  summary: 填充值的来源 Specify via dialog（默认） | Input port
  group: ''
- name: Pad value
  summary: 填充值 0（默认） | 标量
  group: ''
- name: Output column mode
  summary: 指定列长度的模式 User-specified | Next power of two
  group: ''
- name: Column size
  summary: 输出的列长度 1 | 标量
  group: ''
- name: Output row mode
  summary: 指定行长度的模式 User-specified（默认） | Next power of two
  group: ''
- name: Row size
  summary: 输出的行长度 1 | 标量
  group: ''
- name: Specify
  summary: 指定输出大小或填充大小 Output size（默认） | Pad size
  group: ''
- name: Output size mode
  summary: 指定输出长度的模式 User-specified | Next power of two
  group: ''
- name: Output size
  summary: 沿指定维度的输出长度 1 | 标量 | 向量
  group: ''
- name: Pad size at beginning
  summary: 指定要添加到输入信号开头的值的数量 0 | 标量 | 向量
  group: ''
- name: Pad size at end
  summary: 指定要添加到输入信号末尾的值的数量 0 | 标量 | 向量
  group: ''
- name: Pad signal at
  summary: 指定在何处填充或截断信号 End（默认） | Beginning | Beginning and end
  group: ''
- name: Action when truncation occurs
  summary: 发生截断时采取的操作 None | Warning | Error
  group: ''
```

### **Pad over** — 进行填充或截断的维度 `Columns`（默认） | `Rows` | `Columns and rows` | `None` | `Specified dimensions`

指定进行填充或截断的维度：

- `Columns`
- `Rows`
- `Columns and rows`
- `None`
- `Specified dimensions`

### **Dimensions to pad** — 指定进行填充或截断的维度 `1`（默认） | 标量 | 向量

指定进行填充或截断的基于一的维度。此参数的值可以是标量或向量。例如，指定 `1` 以填充列。指定 `[1 2]` 以填充列和行。指定 `[1 3 5]` 以填充第一、第三和第五维度。

#### 依赖关系

此参数仅在将 **Pad over** 设置为 `Specified dimensions` 时显示。

### **Pad value source** — 填充值的来源 `Specify via dialog`（默认） | `Input port`

选择如何指定填充值。填充值可以来自对话框或来自输入端口：

- 如果选择 `Specify via dialog`，则显示 **Pad value** 参数。
- 如果选择 `Input port`，则模块图标上显示 `PVal` 端口。

### **Pad value** — 填充值 `0`（默认） | 标量

指定用于填充输入的常量标量值。

**可调：** 是

#### 依赖关系

此参数仅在将 **Pad value source** 设置为 `Specify via dialog` 时显示。

### **Output column mode** — 指定列长度的模式 `User-specified` | `Next power of two`

选择如何指定输出的列长度：

- 如果选择 `User-specified`，则显示 **Column size** 参数。
- 如果选择 `Next power of two`，模块将填充输出列，直到其长度为下一个最高的 2 的幂。如果列长度已经是 2 的幂，则模块不填充列。

#### 依赖关系

此参数仅在将 **Pad over** 设置为 `Columns` 或 `Columns and rows` 时显示。

### **Column size** — 输出的列长度 `1` | 标量

指定输出的列长度。如果指定的列长度大于输入列长度，模块将填充列。如果指定的列长度小于输入列长度，模块将截断列。

#### 依赖关系

此参数仅在将 **Output column mode** 设置为 `User-specified` 时显示。

### **Output row mode** — 指定行长度的模式 `User-specified`（默认） | `Next power of two`

选择如何指定输出的行长度：

- 如果选择 `User-specified`，则显示 **Row size** 参数。
- 如果选择 `Next power of two`，模块将填充输出行，直到其长度为下一个最高的 2 的幂。如果行长度已经是 2 的幂，则模块不填充行。

#### 依赖关系

此参数仅在将 **Pad over** 设置为 `Rows` 或 `Columns and rows` 时显示。

### **Row size** — 输出的行长度 `1` | 标量

指定输出的行长度。如果指定的行长度大于输入行长度，模块将填充行。如果指定的行长度小于输入行长度，模块将截断行。

#### 依赖关系

此参数仅在将 **Output row mode** 设置为 `User-specified` 时显示。

### **Specify** — 指定输出大小或填充大小 `Output size`（默认） | `Pad size`

选择是通过指定输出大小还是填充大小来控制指定维度的输出长度。

#### 依赖关系

此参数仅在将 **Pad over** 设置为 `Specified dimensions` 时显示。

### **Output size mode** — 指定输出长度的模式 `User-specified` | `Next power of two`

选择如何指定指定维度的输出长度：

- 如果选择 `User-specified`，则显示 **Output size** 参数。
- 如果选择 `Next power of two`，模块将填充指定维度，直到其长度为下一个最高的 2 的幂。如果维度长度已经是 2 的幂，则模块不在该维度上进行填充。

#### 依赖关系

此参数仅在将 **Pad over** 设置为 `Specified dimensions` 且将 **Specify** 参数设置为 `Output size` 时显示。

### **Output size** — 沿指定维度的输出长度 `1` | 标量 | 向量

指定指定维度的输出长度。此参数必须是标量或与 **Dimensions to pad** 参数具有相同元素数的向量。**Output size** 向量中的每个元素给出 **Dimensions to pad** 向量中对应维度的输出长度。如果指定长度大于给定维度的输入长度，模块将填充该维度。如果指定长度小于给定维度的输入长度，模块将截断该维度。

#### 依赖关系

此参数仅在将 **Pad over** 设置为 `Specified dimensions` 且将 **Specify** 参数设置为 `Output size` 时显示。

### **Pad size at beginning** — 指定要添加到输入信号开头的值的数量 `0` | 标量 | 向量

指定沿指定维度要添加到输入信号开头的值的数量。此参数必须是标量或与 **Dimensions to pad** 参数具有相同元素数的向量。**Pad size at beginning** 参数中的每个元素给出 **Dimensions to pad** 参数中对应维度开头的填充长度。此参数的值必须是非负整数。

#### 依赖关系

此参数仅在将 **Pad over** 设置为 `Specified dimensions` 且将 **Specify** 参数设置为 `Pad size` 时显示。

### **Pad size at end** — 指定要添加到输入信号末尾的值的数量 `0` | 标量 | 向量

指定沿指定维度要添加到输入信号末尾的值的数量。此参数必须是标量或与 **Dimensions to pad** 参数具有相同元素数的向量。**Pad size at end** 参数中的每个元素给出 **Dimensions to pad** 参数中对应维度末尾的填充长度。此参数的值必须是非负整数。

#### 依赖关系

此参数仅在将 **Pad over** 设置为 `Specified dimensions` 且将 **Specify** 参数设置为 `Pad size` 时显示。

### **Pad signal at** — 指定在何处填充或截断信号 `End`（默认） | `Beginning` | `Beginning and end`

指定是在指定维度的 `Beginning`、`End` 还是 `Beginning and end` 处填充或截断信号。当选择 `Beginning and end` 时，一半的填充长度添加到信号的开头，另一半添加到信号的末尾。对于奇数填充长度，额外的值添加到信号的末尾。当在此模式下指定截断信号时，从信号的开头和末尾截断相等数量的值。在奇数截断长度的情况下，额外的值从信号的末尾移除。

#### 依赖关系

此参数仅在将 **Pad over** 设置为 `Columns`、`Rows` 和 `Columns and rows` 时显示。

### **Action when truncation occurs** — 发生截断时采取的操作 `None` | `Warning` | `Error`

指定模块在截断输入时采取的操作。

- `None` —— 输入被截断时模块不发出通知。
- `Warning` —— 输入被截断时模块显示警告。
- `Error` —— 输入被截断时模块显示错误消息并终止仿真。

#### 依赖关系

此参数仅在将 **Pad over** 设置为 `Columns`、`Rows` 和 `Columns and rows` 时显示。
## 所属库

DSP System Toolbox / Signal Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前推出**

## 描述

填充或截断指定维度

Pad 模块通过沿其列、行、列和行，或沿您指定的任何其他维度进行填充或截断，来扩展或裁剪输入信号的维度。当您指定的输出维度小于对应的输入维度时，模块会截断输入。如果输入和输出长度相同，则模块充当直通。

您可以在模块掩码中输入填充值，也可以通过输入端口输入。您可以在模块掩码中输入输出大小，或者让模块填充指定维度，直到其长度为下一个最高的 2 的幂。**Pad signal at** 参数控制模块是在开头、末尾还是同时在两端填充或截断输入信号维度。对于奇数填充或截断长度，额外的填充或截断值应用于信号的末尾。当模块处于 `Specified dimensions` 模式时，您可以指定输出大小或填充大小。

您可以使用 **Action when truncation occurs** 参数将模块配置为在输入信号被截断时发出警告或错误。
