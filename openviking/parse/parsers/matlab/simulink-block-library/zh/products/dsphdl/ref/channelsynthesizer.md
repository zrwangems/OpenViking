---
type: simulink-block
title: 'Channel Synthesizer'
family: 'dsphdl'
product_id: 'dsphdl'
product_name: 'DSP HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL-Optimized Filters and Transforms'
documentation_page: 'channelsynthesizer'
documentation_source_path: 'ref/channelsynthesizer.html'
language: zh-CN
chinese_source: worker-translation
---

# Channel Synthesizer

## 端口

### 输入

### **data** — 输入数据 实值行向量 | 复值行向量

输入数据，指定为实值或复值行向量。

向量长度必须是 2 的幂，并且在范围 [4, 64] 内。

您可以使用 `double` 和 `single` 数据类型进行仿真，但不能用于 HDL 代码生成。

**数据类型：** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
**复数支持：** 是

### **valid** — 指示输入数据有效的标量

控制信号，用于指示输入数据是否有效。当 **valid** 为 `1` (`true`) 时，模块捕获来自输入 **data** 端口的值。当 **valid** 为 `0` (`false`) 时，模块忽略来自输入 **data** 端口的值。

**数据类型：** `Boolean`

### **reset** — 清除内部状态的标量

控制信号，用于清除内部状态。当 **reset** 为 `1` (`true`) 时，模块停止当前计算并清除内部状态。当 **reset** 为 `0` (`false`) 且输入 **valid** 为 `1` (`true`) 时，模块捕获要处理的数据。

有关更多复位注意事项，请参阅硬件控制信号页面中的复位信号部分。

#### 依赖关系

要启用此端口，请在 **控制端口** 选项卡上选择 **启用复位输入端口** 参数。

**数据类型：** `Boolean`
### 输出

### **data** — 合成输出数据 复值列向量

合成输出数据，返回为复值列向量。

当输入数据类型为浮点类型时，输出数据继承输入数据的数据类型。当输入数据类型为整数类型或定点类型时，**数据类型** 选项卡上的 **输出** 参数控制输出数据类型。

输出大小与输入大小相同，并等于频带数量或 IFFT 长度。输出顺序为位自然序。输出数据类型取决于为避免溢出所需的 IFFT 位增长，以及在 **输出** 参数中设置的数据类型。

**数据类型：** `fixed point` | `single` | `double`
**复数支持：** 是

### **valid** — 指示输出数据有效的标量

控制信号，用于指示来自输出 **data** 端口的数据是否有效。当 **valid** 为 `1` (`true`) 时，模块从输出 **data** 端口返回有效数据。当 **valid** 为 `0` (`false`) 时，来自输出 **data** 端口的值无效。

**数据类型：** `Boolean`

## 参数

### 主要

### **滤波器系数** — 多相滤波器系数 `[-0.0329 0.1218 0.3183 0.4829 0.5469 0.4829 0.5469 0.4829 0.3183 0.1218 -0.0329]`（默认） | 复值向量

多相滤波器系数，指定为数值向量。如果系数数量不是频带数量或 IFFT 长度的倍数，则模块会对此向量补零。默认滤波器规格为升余弦 FIR 滤波器，`rcosdesign(0.25,2,4,'sqrt')`。您可以指定系数向量，或指定对返回系数值的滤波器设计函数的调用。默认情况下，模块会将系数转换为与输入相同的字长。

### **滤波器结构** — HDL 滤波器架构 `Direct form transposed`（默认） | `Direct form systolic`

将 HDL 滤波器架构指定为以下值之一：

- `Direct form transposed` — 此架构是适合 FPGA 和 ASIC 应用的完全并行实现。有关架构和性能详细信息，请参阅全并行转置架构。
- `Direct form systolic` — 此架构提供完全并行滤波器实现，可高效使用 Intel® 和 AMD® DSP 模块。有关架构和性能详细信息，请参阅全并行脉动架构。

### **复数乘法** — 复数乘法器的 HDL 实现 `Use 4 multipliers and 2 adders`（默认） | `Use 3 multipliers and 5 adders`

将复数乘法器的 HDL 实现指定为 `Use 4 multipliers and 2 adders` 或 `Use 3 multipliers and 5 adders`。乘法器的速度取决于您的综合工具和目标器件。

### **将蝶形输出除以二** — IFFT 缩放 `on`（默认） | `off`

选择此参数后，IFFT 会通过将每个流水线级的结果缩放 2 来实现总体 1/*N* 缩放因子，其中 *N* 是 IFFT 长度。此调整使 IFFT 的输出保持与其输入相同的幅度范围。如果禁用缩放，则 IFFT 会在每一级将字长增加一位，以避免溢出。

### 数据类型

### **舍入模式** — 输出类型转换的舍入模式 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

当输入为整数或定点数据类型时，对内部计算使用定点算术。当输入为 `single` 或 `double` 时，此选项不适用。有关更多详细信息，请参阅舍入模式。

### **整数溢出时饱和** — 输出类型转换的溢出处理 `off`（默认） | `on`

当输入为整数或定点数据类型时，对内部计算使用定点算术。当输入为 `single` 或 `double` 时，此选项不适用。将多相滤波器的系数和输出转换为您指定的数据类型。有关更多信息，请参阅溢出处理。

### **系数** — 系数的数据类型 `Inherit: Same word length as input`（默认） | `<data type expression>`

使用您指定的舍入和溢出设置，将多相滤波器系数转换为该数据类型。当您选择 `Inherit: Same word length as input`（默认）时，模块使用 `fixed point` 最佳精度规则选择二进制小数点。

### **输出** — 模块输出的数据类型 `Inherit: via internal rule`（默认） | `Inherit: Same as input` | `<data type expression>`

当您选择 `Inherit: via internal rule` 时，模块会考虑滤波器系数值和输入数据类型范围来选择最佳精度二进制小数点。当您选择 `Inherit: Same as input` 时，模块会使用您指定的舍入和溢出设置，将多相滤波器的输出转换为输入数据类型。

### 控制端口

### **启用复位输入端口** — 启用复位输入端口的选项 `off`（默认） | `on`

选择此参数以启用 **reset** 输入端口。复位信号实现对数据路径寄存器的本地同步复位。

## 所属库

DSP HDL Toolbox / Filtering

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持为 Simulink 加速模式和快速加速模式以及 DPI 组件生成进行 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2022a 中引入**

## 描述

将窄带信号合并为多通道信号

Channel Synthesizer 模块使用多相滤波器组技术将窄带信号合并为多通道信号。

该模块接受实值或复值行向量输入数据和控制信号，并输出合成后的列向量和控制信号。使用此模块，您可以实现每秒千兆采样 (GSPS) 吞吐量（也称为超采样率）。该模块实现一个多相滤波器，每个输入向量元素对应一个子滤波器。该模块支持 HDL 代码生成和硬件部署。

**注意**

您还可以使用 DSP HDL IP Designer app，在不创建 Simulink® 模型的情况下，为此硬件优化算法生成 HDL 代码。该应用提供与 Simulink 模块相同的接口和配置选项。
