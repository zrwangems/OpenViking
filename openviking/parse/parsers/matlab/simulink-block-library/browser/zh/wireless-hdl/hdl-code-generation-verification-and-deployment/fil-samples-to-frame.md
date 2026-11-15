---
type: simulink-block
title: 'FIL Samples To Frame'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL Code Generation, Verification, and Deployment'
documentation_page: 'filsamplestoframe'
documentation_source_path: 'ref/filsamplestoframe.html'
language: zh-CN
chinese_source: worker-translation
---

# FIL Samples To Frame

## 端口

### 输入

### **sampleN** — 样本流向量

样本流，指定为表示整个帧的向量。该流可以包含样本之间以及帧之间的空闲周期。空闲样本会被丢弃。

如果将 **Number of input samples** 设置为大于一，则模块为每个输入值显示一个端口。在这种情况下，单个样本由 N 个值表示，例如由 1 个系统值和 2 个奇偶校验值表示的 turbo 编码样本。输入数据为每个端口一个向量。控制信号应用于所有 **sampleN** 端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **start** — 帧起始向量

帧起始，指定为一个 `Boolean` 向量，其中包含帧中每个样本的一个值。对于帧的第一个有效样本所对应的时间步，该信号为 1（true）。

**数据类型：** `Boolean`

### **end** — 帧结束向量

帧结束，指定为一个 `Boolean` 向量，其中包含帧中每个样本的一个值。对于帧的最后一个有效样本所对应的时间步，该信号为 1（true）。

**数据类型：** `Boolean`

### **validIn** — 样本有效性向量

样本有效性，指定为一个 `Boolean` 向量，其中包含帧中每个样本的一个值。在对应于有效样本的时间步上，该信号为 1（true）。

**数据类型：** `Boolean`

### 输出

### **frame** — 输出样本帧列向量

输出样本帧，返回为列向量。每帧的大小相同。如果输入帧小于 **Output size**，则模块用零填充该帧。如果输出帧大于 **Output size**，则模块使用前 **Output size** 个样本构成帧。您可以选择在 **len** 端口上输出每帧中有效样本的数量。

### **validOut** — 输出帧有效性标量

输出帧有效性，返回为 `Boolean` 标量。当 **frame** 和 **len**（可选）端口上的值有效时，该端口返回 `1`（`true`）。

**数据类型：** `Boolean`

### **len** — 输出帧中有效样本数整数

输出帧中有效样本数，返回为整数。输入样本流可以具有不同大小的帧。模块在 **frame** 端口上返回恒定大小的向量，当输入帧小于 **Output size** 时用零填充。**len** 端口指示输出帧中有多少个有效样本。如果输出帧大于 **Output size**，则模块使用前 **Output size** 个样本构成帧。

**数据类型：** `double`

## 参数

### **Number of input samples** — 表示每个样本的值数量 1（默认） | 正整数

表示每个样本的值数量，指定为正整数标量。模块为每个值提供一个 **sampleN** 端口。控制信号应用于所有 **sampleN** 端口。例如，您可以将此参数用于 turbo 编码样本。在 LTE 标准中，turbo 码率为 1/3，因此每个样本由 1 个系统值和 2 个奇偶校验值表示：*S\_n*、*P1\_n* 和 *P2\_n*。在这种情况下，将 **Number of input samples** 设置为 `3`。

### **Output size** — 每帧最大样本数 1024（默认） | 正整数

每帧最大样本数，指定为整数。输入样本流可以具有不同大小的帧。模块返回恒定大小的向量；如果帧小于 **Output size**，则用零填充。如果模块接收到大于 **Output size** 的帧，则会截断该帧。

### **Compose output from interleaved input samples** — 输出样本相对于输入顺序的顺序 off（默认） | on

当多个值表示每个样本时，输出样本相对于输入顺序的顺序。例如，1/3 turbo 编码样本由 `[S_1 P1_1 P2_1]` 和 `[S_2 P1_2 P2_2]` 表示。默认输出顺序为 `[S_1 P1_1 P2_1 S_2 P1_2 P2_2]`。要将样本重新排序，使系统值和奇偶校验值分组在一起，请选择 **Compose output from interleaved input samples**。此时输出顺序为 `[S_1 S_2 P1_1 P1_2 P2_1 P2_2]`。

### **Enable frame length output port** — 输出有效样本数 off（默认） | on

启用帧长度输出端口。选择此选项可返回每个输出帧中有效样本的数量。长度在 **len** 端口上返回，并由 **valid** 信号限定。当样本流具有可变大小帧，或下游模块需要帧大小作为输入（例如 LTE Turbo Decoder）时，请使用此选项。

## 所属库

Wireless HDL Toolbox / I/O Interfaces

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

## 版本历史

**在 R2017b 中引入**

## 描述

将来自 FPGA-in-the-loop 的样本流转换为基于帧的数据

FIL Samples To Frame 模块执行与 Samples To Frame 模块相同的样本到帧转换。它接受输入数据为整个样本帧的向量。该模块期望控制信号输入向量的宽度与样本数据相同。在使用 FPGA-in-the-loop 时，此优化可加速 FPGA 板与您的 Simulink® 仿真之间的通信链路。要运行 FPGA-in-the-loop，您必须拥有 HDL Verifier™ 许可证。

当您在 Simulink 中为 FIL 目标生成编程文件时，该工具会创建一个模型，以将 FIL 仿真与您的 Simulink 设计进行比较。对于 Wireless HDL Toolbox™ 设计，该模型中的 FIL 模块会复制样本流式传输接口，以一次一个样本发送到 FPGA。您可以修改自动生成的模型，以使用 FIL Frame To Samples 和 FIL Samples To Frame 模块，通过一次发送一帧来提高与 FPGA 板的通信带宽。有关如何修改自动生成的模型，请参阅 FPGA-in-the-Loop。
