---
type: simulink-block
title: 'Downsampler'
family: 'signal-operations'
product_id: 'dsphdl'
product_name: 'DSP HDL Toolbox'
documentation_release: R2025b
official_category: 'Signal Operations'
documentation_page: 'downsampler'
documentation_source_path: 'ref/downsampler.html'
language: zh-CN
chinese_source: worker-translation
---

# Downsampler

## 端口

### 输入

### **data** — 输入数据 标量 | 列向量

输入数据，指定为长度最多为 64 的标量或列向量。输入数据必须是整数或定点数，且字长小于或等于 128。**下采样因子 (K)** 参数必须是输入帧大小的整数倍。

`double` 和 `single` 数据类型支持仿真，但不支持 HDL 代码生成。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **valid** — 有效输入数据指示 `0` | `1`

控制信号，指示输入数据是否有效。当此值为 `1` 时，模块接受 **data** 输入端口上的值。当此值为 `0` 时，模块忽略 **data** 输入端口上的值。

**数据类型：** `Boolean`

### **reset** — 清除内部状态的选项 `0` | `1`

控制信号，用于清除内部状态。当此值为 `1` 时，模块停止当前计算并清除其内部状态。当此值为 `0` 且 **valid** 为 `1` 时，模块捕获数据以进行处理。

有关更多复位注意事项，请参阅硬件控制信号页面上的复位信号部分。

#### 依赖项

要启用此端口，请在**控制端口**选项卡上选择**启用 reset 输入端口**参数。

**数据类型：** `Boolean`
### 输出

### **data** — 下采样数据 标量 | 列向量

下采样数据，返回为长度为 1 到 64 的标量或列向量。

对于向量输入，如果向量大小小于或等于 **下采样因子 (K)**，则模块输出标量输出。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **valid** — 有效输出数据指示 `0` | `1`

控制信号，指示来自 **data** 输出端口的数据是否有效。当此值为 `1` 时，模块在 **data** 输出端口上返回有效数据。当此值为 `0` 时，**data** 输出端口上的值无效。

**数据类型：** `Boolean`

## 参数

### 主要

### **下采样因子 (K)** — 下采样因子 `2` (默认) | 范围 [1, 2.^16] 内的整数

指定模块降低输入采样率所采用的下采样因子。

### **采样偏移 (0 到 K-1)** — 采样偏移 `0` (默认) | 范围 [0, 2.^16 – 1] 内的整数

指定范围 [0, **下采样因子 (K)** – 1] 内的采样偏移。

### 控制端口

### **启用 reset 输入端口** — 启用 reset 输入端口的选项 `off` (默认) | `on`

选择此参数以启用 **reset** 输入端口。reset 信号实现数据路径寄存器的本地同步复位。

有关更多复位注意事项，请参阅提示。

## 所属库

DSP HDL Toolbox / Signal Operations

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2022b 中引入**

## 描述

通过移除输入采样之间的数据采样进行下采样

Downsampler 模块通过移除输入采样之间的 *K*–1 个数据采样来对输入信号进行下采样。该模块支持以下输入和输出数据组合。

- 标量输入和标量输出
- 向量输入和标量输出
- 向量输入和向量输出

该模块提供适用于 HDL 代码生成和硬件部署的架构。

**注意**

您还可以使用 DSP HDL IP Designer 应用为此硬件优化算法生成 HDL 代码，而无需创建 Simulink® 模型。该应用提供与 Simulink 模块相同的接口和配置选项。
