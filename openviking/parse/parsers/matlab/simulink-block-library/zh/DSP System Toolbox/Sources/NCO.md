---
type: simulink-block
title: 'NCO'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Operations'
documentation_page: 'nco'
documentation_source_path: 'ref/nco.html'
language: zh-CN
chinese_source: worker-translation
---

# NCO

## 端口

### 输入

### **inc** — 相位增量 标量 | 向量

相位增量信号，指定为实值标量或向量。输入必须具有整数数据类型，或小数长度为 0 的定点数据类型。相位增量信号的维度取决于您如何指定 **Phase offset** 参数：

- 当您在模块对话框中指定 **Phase offset** 时，**Phase increment** 必须是标量或与 **Phase offset** 值长度相同的向量。模块将向量的每个元素应用于不同的通道，因此向量长度定义了输出通道的数量。
- 当您通过输入端口指定 **Phase offset** 时，**offset** 端口将输入的每一列视为独立通道。**Phase increment** 的长度必须等于 **offset** 端口输入的列数。

#### 依赖关系

要启用此端口，请将 **Phase increment source** 设置为 `Input port`。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **offset** — 相位偏移 标量 | 向量 | 矩阵

相位偏移信号，指定为实值标量、向量或完整矩阵。输入必须具有整数数据类型，或小数长度为 0 的定点数据类型。模块将 offset 端口输入的每一列视为独立通道。相位偏移中的通道数必须与数据输入中的通道数匹配。对于输入的每一帧，模块可以对每个采样和通道应用不同的相位偏移。

#### 依赖关系

要启用此端口，请将 **Phase offset source** 设置为 `Input port`。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **sin** — 正弦输出 标量 | 向量 | 矩阵

正弦输出信号，指定为标量、向量或矩阵。您可以使用 **Output** 数据类型参数指定信号的数据类型。

#### 依赖关系

要启用此端口，请将 **Output signal** 设置为 `Sine` 或 `Sine and cosine`。

**数据类型：** `single` | `double` | `fixed point`

### **cos** — 余弦输出 标量 | 向量 | 矩阵

余弦输出信号，指定为标量、向量或矩阵。您可以使用 **Output Data Type** 参数指定信号的数据类型。

#### 依赖关系

要启用此端口，请将 **Output signal** 设置为 `Cosine` 或 `Sine and cosine`。

**数据类型：** `single` | `double` | `fixed point`

### **exp** — 复指数 标量 | 向量 | 矩阵

复指数输出，指定为标量、向量或矩阵。您可以使用 **Output Data Type** 参数指定信号的数据类型。

#### 依赖关系

要启用此端口，请将 **Output signal** 设置为 `Complex exponential`。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** 是

### **Qerr** — 相位量化误差 标量 | 向量 | 矩阵

相位量化误差，指定为标量、向量或矩阵。

#### 依赖关系

要启用此端口，请选中 **Show phase quantization error port** 复选框。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### 主要

#### 相位加法器参数

### **Phase increment source** — 相位增量值的来源 `Specify via dialog` | `Input port`

选择您如何指定相位增量。相位增量可以来自输入端口或对话框参数。

- 如果选择 `Input port`，**inc** 输入端口将出现在模块图标上。
- 如果选择 `Specify via dialog`，**Phase increment** 参数将出现。

#### 依赖关系

当模块来自 Signal Operations 库时，**Phase increment Source** 参数的默认值为 `Input port`。

当模块来自 Sources 库时，**Phase increment Source** 参数的默认值为 `Specify via dialog`。

### **Phase increment** — 相位增量值 `100`（默认）| 标量 | 向量

将相位增量指定为整数值标量或向量。仅允许整数数据类型，包括小数长度为 0 的定点数据类型。相位增量的维度取决于相位偏移的维度：

- 当您在模块对话框中指定相位偏移时，相位增量必须是标量或与相位偏移长度相同的向量。模块将向量的每个元素应用于不同的通道，因此向量长度定义了输出通道的数量。
- 当您通过输入端口指定相位偏移时，offset 端口将输入的每一列视为独立通道。相位增量的长度必须等于 offset 端口输入的列数。

#### 依赖关系

要启用此参数，请将 **Phase increment source** 设置为 `Specify via dialog`。

### **Phase offset source** — 相位偏移的来源 `Specify via dialog`（默认）| `Input port`

选择您如何指定相位偏移。相位偏移可以来自输入端口或对话框。

- 如果选择 `Input port`，**offset** 端口将出现在模块图标上。
- 如果选择 `Specify via dialog`，**Phase offset** 参数将出现。

### **Phase offset** — 相位偏移值 `0`（默认）| 标量 | 向量

将相位偏移指定为整数值标量或向量。仅允许整数数据类型，包括小数长度为 0 的定点数据类型。当您使用此对话框参数指定相位偏移时，它必须是标量或与相位增量长度相同的向量。标量将扩展为与相位增量长度相同的向量。相位偏移向量的每个元素应用于输入的不同通道，因此向量长度定义了输出通道的数量。

#### 依赖关系

要启用此参数，请将 **Phase offset source** 设置为 `Specify via dialog`。

### **Add internal dither** — 添加内部抖动 `on`（默认）| `off`

选择以向 NCO 算法添加内部抖动。抖动使用 Communications Toolbox™ 产品中的 PN Sequence Generator (Communications Toolbox) 添加。

### **Number of dither bits** — 抖动位数 `4`（默认）| 正整数

将抖动位数指定为正整数。

#### 依赖关系

要启用此端口，请选中 **Add internal dither** 复选框。

### **Quantize phase** — 启用累积相位量化 `on`（默认）| `off`

要启用累积相位量化，请选中此复选框。

### **Number of quantized accumulator bits** — 量化累加器位数 `12`（默认）| 整数标量

将量化累加器位数指定为大于 1 且小于累加器字长的标量整数。此值确定查找表中的条目数。

#### 依赖关系

要启用此端口，请选中 **Quantize phase** 复选框。

### **Show phase quantization error port** — 输出量化误差 `off`（默认）| `on`

选择以输出相位量化误差。当您选中此复选框时，**Qerr** 端口将出现在模块图标上。

#### 依赖关系

要启用此参数，请选中 **Quantize phase** 复选框。

#### 输出参数

### **Output signal** — 输出信号 `Sine`（默认）| `Cosine` | `Complex exponential` | `Sine and cosine`

选择模块输出 `Sine`、`Cosine`、`Complex exponential` 还是同时输出 `Sine and cosine` 信号。如果选择 `Sine and cosine`，两个信号将在不同端口输出。

### **Sample time** — 输出采样周期 `1`（默认）| 正标量

当模块作为源时，将采样时间指定为以秒为单位的正标量。

#### 依赖关系

要启用此参数，**Phase increment source** 和 **Phase offset source** 都必须设置为 `Specify via dialog`。当相位增量或相位偏移通过模块输入端口传入时，采样时间将被继承，此参数不可见。

### **Samples per frame** — 每帧采样数 `1`（默认）| 正整数

将每帧采样数指定为正整数。当该值大于 1 时，相位增量和相位偏移可以因通道和帧而异，但在给定帧中沿每个通道保持不变。

当相位偏移输入端口存在时，它具有与任何存在的输出端口相同的帧状态。当相位增量输入端口存在时，它不支持帧。

#### 依赖关系

要启用此参数，请将 **Phase increment source** 和/或 **Phase offset source** 设置为 `Specify via dialog`。

### 数据类型

### **Rounding mode** — 舍入方法 只读：`Floor`（默认）

此参数为只读。

当输入为定点时，NCO 模块始终使用舍入模式 `Floor`。

### **Overflow mode** — 溢出方法 只读：`Wrap`（默认）

此参数为只读。

当输入为定点时，NCO 模块始终使用溢出模式 `Wrap`。

### **Accumulator Word Length** — 累加器字长 `16`（默认）| 2 到 128 的整数

将 **Accumulator** 的 **Word length** 指定为 2 到 128 的正整数。**Data Type** 始终为 `Binary point scaling`，**Fraction length** 始终为 `0`。

### **Output Data Type** — 输出数据类型 `double`（默认）| `single` | `Binary point scaling`

为模块 **Output** 指定 **Data Type**。

- 选择 `double` 或 `single` 以实现浮点实现。
- 当您选择 `Binary point scaling` 时，可以输入输出的字长和小数长度（以位为单位）。

**注意**

此模块的查找表由双精度浮点值构建。因此，您可以在输出中实现的最大精度为 53 位。将 **Output** 数据类型的字长设置为大于 53 位的值不会提高输出的精度。

### **Output Word Length** — 输出字长 `16`（默认）| 2 到 128 的整数

将模块 **Output** 的 **Word length** 指定为 2 到 128 的正整数。

#### 依赖关系

要启用此参数，请将 **Output** 的 **Data Type** 设置为 `Binary point scaling`。

### **Output Fraction Length** — 输出小数长度 `14`（默认）| 整数

将模块 **Output** 的 **Fraction length** 指定为标量整数。

#### 依赖关系

要启用此参数，请将 **Output** 的 **Data Type** 设置为 `Binary point scaling`。

### NCO 特性

**NCO Characterization** 窗格为您提供模块当前实现的 NCO 信号的只读详细信息：

### **Number of data points for lookup table** — 查找表中的点数 无默认值

查找表实现为四分之一波正弦表。查找表数据点数定义为

2number of quantized accumulator bits−2+1

**示例：** 1025

### **Quarter wave sine lookup table size** — 四分之一波正弦查找表大小 无默认值

四分之一波正弦查找表大小定义为

(查找表的数据点数量)⋅(输出字长)8 字节

**示例：** 2050 bytes

### **Theoretical spurious free dynamic range** — 无杂散动态范围 无默认值

对于具有 2P 个条目的查找表，无杂散动态范围 (SFDR) 计算如下：

SFDR=(6P) dB           无抖动SFDR=(6P+12) dB    有抖动

**示例：** 84 dBc

### **Frequency resolution** — 频率分辨率 无默认值

频率分辨率是频率的最小可能增量变化，定义为：

Δf=1Ts⋅2NHz

**示例：** 15.2588 uHz

#### 依赖关系

频率分辨率仅在您将 **Phase increment source** 和 **Phase offset source** 设置为 `Specify via dialog` 时出现。

## 所属库

DSP System Toolbox / Signal Operations DSP System Toolbox / Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `fixed point` | `integer` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

NCO 模块的 HDL 支持将在未来版本中移除。请改用 NCO (DSP HDL Toolbox) 模块。DSP HDL Toolbox™ 模块提供经过 HDL 优化的算法，具有硬件友好的控制信号，并在 Simulink® 中模拟 HDL 算法的延迟。

## 版本历史

**在 R2006a 之前引入**

## 描述

生成实数或复数正弦信号

NCO 模块生成多通道实数或复数正弦信号，每个输出通道具有独立的频率和相位。所创建信号的幅度始终为 `1`。NCO 模块仅支持实数输入。除 `Complex exponential` 模式下的输出信号外，所有输出均为实数。有关模块如何计算输出的详细信息，请参阅算法。

要生成多通道输出，请为 **Phase increment** 和 **Phase offset** 参数指定向量量。两个参数必须具有相同的长度，该长度定义了输出通道的数量。每个向量的每个元素应用于不同的输出通道。
