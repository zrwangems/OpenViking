---
type: simulink-block
title: 'FIL Frame To Samples'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL Code Generation, Verification, and Deployment'
documentation_page: 'filframetosamples'
documentation_source_path: 'ref/filframetosamples.html'
language: zh-CN
chinese_source: worker-translation
---

# FIL Frame To Samples

## 端口

### 输入

### **frame** — 输入样本帧列向量

输入样本的帧，指定为列向量。向量中的所有样本都被视为有效。每帧必须具有相同大小。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### 输出

### **sampleN** — 样本流向量

样本流，以表示整个帧的向量形式返回。输出流包括模块参数中指定的样本之间和帧之间的空闲周期。

如果设置 **Output size** 大于 1，则该模块为每个输出值显示一个端口。在这种情况下，单个样本由 N 个值表示，例如由 1 个系统值和 2 个校验值表示的 Turbo 编码样本。对于每个端口，输出数据是一个向量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **start** — 帧起始向量

帧起始，以 `Boolean` 向量形式返回，该向量为帧中的每个样本包含一个值。对于对应于该帧第一个有效样本的一个时间步，此信号为 1（true）。

**数据类型：** `Boolean`

### **end** — 帧结束向量

帧结束，以 `Boolean` 向量形式返回，该向量为帧中的每个样本包含一个值。对于对应于该帧最后一个有效样本的一个时间步，此信号为 1（true）。

**数据类型：** `Boolean`

### **valid** — 样本有效性向量

样本有效性，以 `Boolean` 向量形式返回，该向量为帧中的每个样本包含一个值。对于对应于有效样本的时间步，此信号为 1（true）。

**数据类型：** `Boolean`

## 参数

### **Idle cycles between samples** — 每个样本后插入的空闲周期数 `0`（默认）| 整数

每个样本后插入的空闲周期数，指定为标量整数。对于每个空闲周期，该模块在每个 **sampleN** 端口上返回零，并将所有控制信号设置为 0（`false`）。

### **Idle cycles between frames** — 每帧末尾插入的空闲周期数 `0`（默认）| 整数

每帧末尾插入的空闲周期数，指定为标量整数。对于每个空闲周期，该模块在每个 **sampleN** 端口上返回零，并将所有控制信号设置为 0（`false`）。

### **Output size** — 表示每个样本的值个数 `1`（默认）| 正整数

表示每个样本的值个数，指定为正整数标量。该模块具有 **Output size** 个输出样本端口。控制信号适用于所有 **sampleN** 端口。

例如，您可以使用此参数来串行化 Turbo 编码样本。在 LTE 标准中，Turbo 码率为 1/3，因此每个样本由一个系统值和两个校验值表示：*S\_n*、*P1\_n* 和 *P2\_n*。在这种情况下，将 **Output size** 设置为 `3`。

### **Compose output from interleaved input samples** — 输出样本相对于输入顺序的顺序 off（默认）| on

当多个值表示每个样本时，输出样本相对于输入顺序的顺序。

例如，对于 1/3 Turbo 编码样本，输入帧可以排序为 `[S_1 P1_1 P2_1 S_2 P1_2 P2_2]` 或 `[S_1 S_2 P1_1 P1_2 P2_1 P2_2]`。在第一种情况下，输出是两个向量：`[S_1 P1_1 P2_1]` 和 `[S_2 P1_2 P2_2]`。要在第二种情况下获得相同的输出，请选择 **Compose output from interleaved input samples**。

#### 依赖项

此参数在 **Output size** 大于 1 时适用。

## 所属库

Wireless HDL Toolbox / I/O Interfaces

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持针对 Simulink 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

## 版本历史

**在 R2017b 中引入**

## 描述

为 FPGA-in-the-loop 将基于帧的数据转换为样本流

FIL Frame To Samples 模块执行与 Frame To Samples 模块相同的帧到样本转换。它以整个样本帧的向量形式返回输出数据。该模块返回与样本数据宽度相同的控制信号向量。在使用 FPGA-in-the-loop (FIL) 时，此优化可更高效地利用 FPGA 板与您的 Simulink® 仿真之间的通信链路。要运行 FPGA-in-the-loop，您必须拥有 HDL Verifier™ 许可证。

当您在 Simulink 中为 FIL 目标生成编程文件时，该工具会创建一个模型，以将 FIL 仿真与您的 Simulink 设计进行比较。对于 Wireless HDL Toolbox™ 设计，该模型中的 FIL 模块会复现样本流接口，以一次一个样本发送到 FPGA。您可以修改自动生成的模型，以使用 FIL Frame To Samples 和 FIL Samples To Frame 模块，通过一次发送一帧来提高与 FPGA 板的通信带宽。有关如何修改自动生成的模型，请参阅 FPGA-in-the-Loop。
