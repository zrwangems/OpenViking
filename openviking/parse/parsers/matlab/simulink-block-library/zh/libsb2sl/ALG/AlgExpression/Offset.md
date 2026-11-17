---
type: simulink-block
title: 'Offset'
family: 'signal-operations'
product_id: 'libsb2sl'
product_name: 'libsb2sl'
documentation_release: R2025b
official_category: 'Signal Operations'
documentation_page: 'offset'
documentation_source_path: '../dsp/ref/offset.html'
language: zh-CN
chinese_source: worker-translation
---

# Offset

## 端口

### 输入

### **In1** — 第一个输入数据 标量 | 向量

将第一个输入数据指定为标量或向量。**In** 端口（**In1**、**In2**、…）的输入必须具有相同的大小和数据类型。

如果输入为 fixed point，则它必须是带符号整数或具有 2 的幂斜率和零偏置的带符号 fixed point 值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** Yes

### **O1** — 第一个偏移值 整数

将模块用于截断第一个输入数据的偏移值指定为整数。偏移值确定模块在第一个数据的开头或末尾移除或保留的样本数。

**O** 端口（**O1**、**O2**、…）的输入必须具有相同的数据类型。模块将任何非整数偏移值舍入为最接近的整数。如果偏移值超出 [0 *N*] 范围，则 **Action for out of range offset value** 参数决定模块的行为。*N* 是输入向量长度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **In2** — 第二个输入数据 标量 | 向量

将第二个输入数据指定为标量或向量。**In** 端口（**In1**、**In2**、…）的输入必须具有相同的大小和数据类型。

如果输入为 fixed point，则它必须是带符号整数或具有 2 的幂斜率和零偏置的带符号 fixed point 值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** Yes

### **O2** — 第二个偏移值 整数

将模块用于截断第二个输入数据的偏移值指定为整数。偏移值确定模块在第二个数据的开头或末尾移除或保留的样本数。

**O** 端口（**O1**、**O2**、…）的输入必须具有相同的数据类型。模块将任何非整数偏移值舍入为最接近的整数。如果偏移值超出 [0 *N*] 范围，则 **Action for out of range offset value** 参数决定模块的行为。*N* 是输入向量长度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### 输出

### **Out1** — 第一个截断数据 标量 | 向量

模块将截断数据作为标量或向量返回。截断数据的长度取决于 **Output port length** 和 **Output length** 参数。如果 **Output port length** 设置为 `Same as input`，则截断数据与输入数据具有相同的大小。如果 **Output port length** 设置为 `User-defined`，则 **Output length** 参数确定输出数据的长度。

每对 **In** 和 **O** 端口都有一个输出端口。

截断输出与输入数据具有相同的数据类型。当输出为 fixed-point 时，它仅为带符号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** Yes

### **Out2** — 第二个截断数据 标量 | 向量

模块将截断数据作为标量或向量返回。截断数据的长度取决于 **Output port length** 和 **Output length** 参数。如果 **Output port length** 设置为 `Same as input`，则截断数据与输入数据具有相同的大小。如果 **Output port length** 设置为 `User-defined`，则 **Output length** 参数确定输出数据的长度。

每对 **In** 和 **O** 端口都有一个输出端口。

截断输出与输入数据具有相同的数据类型。当输出为 fixed-point 时，它仅为带符号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** Yes

## 参数

### **Mode** — 指定丢弃哪些值以及保留哪些值 `Remove beginning samples`（默认）| `Remove ending samples` | `Keep beginning samples` | `Keep ending samples`

使用此参数指定模块从输入向量中丢弃哪些值以及保留哪些值。

从以下选项中选择：

- `Remove beginning samples` –– 丢弃
  向量的初始值。
- `Remove ending samples` –– 丢弃
  向量的最终值。
- `Keep beginning samples` –– 保留
  向量的初始值。
- `Keep ending samples` –– 保留
  向量的最终值。

### **Number of input data-offset pairs** — 输入数据-偏移对的数量 `2`（默认）| 正整数

使用 **Number of input data-offset pairs** 参数指定模块的输入数量。输入端口数量是您在此参数中指定的标量值的两倍。例如，如果输入 `3`，模块上会出现输入端口 **In1**、**O1**、**In2**、**O2**、**In3** 和 **O3**。

### **Output port length** — 指定输出端口长度的模式 `Same as input`（默认）| `User-defined`

使用此参数指定输出向量的长度。如果选择 `Same as input`，则输出向量与输入向量具有相同长度。如果选择 `User-defined`，则可以在 **Output length** 参数中输入所需长度。

### **Output length** — 输出向量的所需长度 `9`（默认）| 正整数

输入一个标量，表示输出向量的所需长度。如果您指定的所需输出长度大于模块从输入向量中提取的值的数量，则模块会在向量末尾补零以达到您指定的长度。

#### 依赖关系

仅当将 **Output port length** 参数设置为 `User-defined` 时，此参数才可见。

### **Action for out of range offset value** — 超出范围偏移值的操作 `Clip`（默认）| `Clip and warn` | `Error`

使用此参数确定当偏移值不在 0 ≤ 偏移值 ≤ *N* 范围内时模块的行为，其中 *N* 是输入向量长度。

- `Clip` –– 小于 0 的偏移值设置为 0，大于 *N* 的偏移值设置为 *N*。
- `Clip and warn` –– 小于 0 的偏移值设置为 0，大于 *N* 的偏移值设置为 *N*。此外，模块显示警告消息。
- `Error` –– 当偏移值超出范围时，仿真停止，模块显示错误。

## 所属库

DSP System Toolbox / Signal Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖 `memcpy` 或 `memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前引入**

## 描述

通过移除或保留开头或结尾的值来截断向量

Offset 模块从输入向量的开头或末尾移除或保留值。要移除或保留的值的数量由通过 **O** 端口（**O1**、**O2**、…）指定的偏移值确定。截断向量的长度由 **Output port length** 和 **Output length** 参数确定。**Number of input data-offset pairs** 参数确定输入数据-偏移对的数量。
