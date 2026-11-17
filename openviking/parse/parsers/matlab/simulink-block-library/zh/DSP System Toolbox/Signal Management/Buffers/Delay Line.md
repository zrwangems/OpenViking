---
type: simulink-block
title: 'Delay Line'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Management / Buffers'
documentation_page: 'delayline'
documentation_source_path: 'ref/delayline.html'
language: zh-CN
chinese_source: worker-translation
---

# Delay Line

## 端口

### 输入

### **In** — 输入信号 向量 | 矩阵

将输入信号指定为大小为 *Mi*×*N* 的向量或矩阵。

在您选择 **Show En\_Out port for selectively enabling output** 参数之前，此端口是未命名的。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **En\_Out** — 线性化模块输出 `true` | `false`

指定是否线性化模块输出。

如果 **En\_Out** 端口的输入值为 `Boolean` `1`（或 `true`），则模块线性化输出，输出有效。此设置允许模块在不需要每个采样时刻都输出抽头延迟线结果时更加高效。

请注意，当 **En\_Out** 端口的输入值为 `Boolean` `0`（或 `false`）时，模块可能根据模型状态给出不同结果。结果可能看起来与有效结果一致，也可能无效，且无法预测。当 **En\_Out** 端口的输入为 `0` 时，在所有情况下都应忽略模块输出。

#### 依赖关系

要启用此端口，请选择 **Show En\_Out port for selectively enabling output** 参数。

**数据类型：** `Boolean`
### 输出

### **Out** — 重新缓冲的输出 向量 | 矩阵

重新缓冲的输出，返回为大小为 *Mo*×*N* 的向量或矩阵。

当 *Mo* > *Mi* 时，输出帧重叠为输出与输入帧大小之差，*Mo*−*Mi*。当 *Mo* < *Mi* 时，输出为欠重叠，Delay Line 模块丢弃每个输入帧的前 *Mi*−*Mo* 个采样，以便仅将最后 *Mo* 个采样缓冲到对应的输出帧中。当 *Mo* = *Mi* 时，输出数据与输入数据相同，但会延迟模块的延迟量。由于模块延迟，输出始终延迟一帧，其条目由 **Initial conditions** 参数指定。

输出帧周期等于输入帧周期（*Tfo*=*Tfi*）。因此，输出采样周期 *Tso* 等于 *Tfi*/*Mo*，或等价地，*Tsi*(*Mi*/*Mo*)

在最典型的用法中，每个输出与前一个输出仅相差一个采样，如下所示（标量输入）。

请注意，上例中模块的第一个输出全为零；这是因为 **Initial Conditions** 参数设置为零。

在您选择 **Show En\_Out port for selectively enabling output** 参数之前，此端口是未命名的。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

## 参数

### **Delay line size** — 延迟线大小 `64`（默认）| 正整数

将输出矩阵中的行数 *M*o 指定为正整数。

### **Initial conditions** — 初始条件 `0`（默认）| 标量 | 向量 | 矩阵

将模块初始输出的值指定为标量、向量或矩阵。Delay Line 模块缓冲区初始化为 **Initial conditions** 参数指定的值。模块在第一个仿真步（*t*=0）输出此缓冲区。

当模块输出向量时，**Initial conditions** 可以是相同大小的向量，或是在初始输出的所有元素中重复的标量值。当模块输出矩阵时，**Initial conditions** 可以是相同大小的矩阵、在初始输出的所有列中重复的向量（长度等于矩阵行数），或是在初始输出的所有元素中重复的标量。

### **Allow directfeedthrough** — 允许直接馈通 `off`（默认）| `on`

当您选中此复选框时，输入数据在输出缓冲区可用之前不会额外延迟一帧。相反，输入数据立即可在模块的输出端口获得。

### **Show En\_Out port for selectively enabling output** — 显示用于选择性启用输出的 En\_Out 端口 `off`（默认）| `on`

当您选中此复选框时，**En\_Out** 输入端口会出现在模块图标上。此模块内部使用循环缓冲区，即使输出是线性的。这意味着对于有效输出，循环缓冲区中的数据必须被线性化。**En\_Out** 端口根据其 `Boolean` 输入的值确定是否需要计算有效输出。如果 **En\_Out** 端口的输入值为 `1`，则模块输出被线性化，因此有效。否则，输出未被线性化，无效。这允许模块在不需要每个采样时刻都输出抽头延迟线结果时更加高效。

请注意，当 **En\_Out** 端口的输入值为 `0` 时，模块可能根据模型状态给出不同结果。结果可能看起来与有效结果一致，也可能无效，且无法预测。当 **En\_Out** 端口的输入为 `0` 时，在所有情况下都应忽略模块输出。

### **Hold previous value when the output is disabled** — 输出禁用时保持先前值 `off`（默认）| `on`

使用此参数指定在内部状态缓冲区未被线性化为有效输出数据的那些时间步的模块输出。

当您不选中此复选框时，模块内存可自由用于模型的其他部分，输出端口上的信号无效。当您选中此复选框时，最近的无效值将保持在输出端口上，模块会使用稍多的内存。

#### 依赖关系

要启用此参数，请选择 **Show En\_Out port for selectively enabling output**。

## 所属库

DSP System Toolbox / Signal Management / Buffers

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖 `memcpy` 或 `memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前引入**

## 描述

重新缓冲输入序列

Delay Line 模块将 *Mi*×*N* 矩阵输入序列重新缓冲为 *Mo*×*N* 矩阵输出序列，其中 *Mo* 是您在 **Delay line size** 参数中指定的输出帧大小。根据 *Mo* 是大于、小于还是等于输入帧大小 *Mi*，输出帧可以是欠重叠或重叠的。该模块始终执行基于帧的处理，并独立地重新缓冲 *N* 个输入通道中的每一个。
