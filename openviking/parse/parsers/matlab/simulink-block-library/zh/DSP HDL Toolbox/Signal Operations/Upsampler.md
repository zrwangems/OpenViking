---
type: simulink-block
title: 'Upsampler'
family: 'dsphdl'
product_id: 'dsphdl'
product_name: 'DSP HDL Toolbox'
documentation_release: R2025b
official_category: 'Signal Operations'
documentation_page: 'upsampler'
documentation_source_path: 'ref/upsampler.html'
language: zh-CN
chinese_source: worker-translation
---

# Upsampler

## 端口

### 输入

### **data** — 输入数据 标量 | 列向量

输入数据，指定为标量或长度最多为 64 的列向量。输入数据必须为整数或字长小于等于 128 的定点值。

`double` 和 `single` 数据类型支持仿真，但不支持 HDL 代码生成。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **valid** — 有效输入数据指示 `0` | `1`

控制信号，指示输入数据是否有效。当该值为 `1` 时，模块接受 **data** 输入端口上的值。当该值为 `0` 时，模块忽略 **data** 输入端口上的值。

**数据类型：** `Boolean`

### **reset** — 清除内部状态的选项 `0` | `1`

控制信号，用于清除内部状态。当该值为 `1` 时，模块停止当前计算并清除其内部状态。当该值为 `0` 且 **valid** 为 `1` 时，模块捕获数据以进行处理。

有关更多复位注意事项，请参阅 Hardware Control Signals 页面中的 Reset Signal 部分。

#### 依赖关系

要启用此端口，请在 **Control Ports** 选项卡上选择 **Enable reset input port** 参数。

**数据类型：** `Boolean`
### 输出

### **data** — 上采样数据 标量 | 列向量

上采样数据，以标量或长度最多为 1 到 128 的列向量形式返回。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **valid** — 有效输出数据指示 `0` | `1`

控制信号，指示 **data** 输出端口的数据是否有效。当该值为 `1` 时，模块在 **data** 输出端口上返回有效数据。当该值为 `0` 时，**data** 输出端口上的值无效。

**数据类型：** `Boolean`

### **ready** — 模块就绪指示 `0` | `1`

控制信号，指示模块是否已准备好在下个周期接收新的输入数据。当该值为 `1` 时，您可以为下个时间步指定 **data** 和 **valid** 输入。当该值为 `0` 时，模块忽略下个时间步的任何输入数据。

#### 依赖关系

要启用此端口，请在 **Control Ports** 选项卡上选择 **Enable ready output port** 参数。

**数据类型：** `Boolean`

## 参数

### 主

### **Upsample factor (L)** — 上采样因子 `3`（默认）| [1, 2.^16] 范围内的整数

指定模块提高输入采样率的上采样因子。

### **Sample offset (0 to L-1)** — 采样偏移 `0`（默认）| [0, 2.^16 – 1] 范围内的整数

将采样偏移指定为 [0, **Upsample factor (L)** – 1] 范围内的整数。

### **Minimum number of cycles between valid input samples** — 有效输入采样之间的最小周期数 `1`（默认）| **Upsample factor (L)** 的因子或倍数 | [1, Inf] 范围内的整数

根据输入和输出数据的类型，将有效输入采样之间的最小周期数指定为 **Upsample factor (L)** 的因子或倍数，或 [1, Inf] 范围内的整数。

| 输入数据 | 输出数据 | 有效输入采样之间的最小周期数 |
| --- | --- | --- |
| 标量 | 标量 | 大于等于 **Upsample factor (L)** |
| 标量 | 向量 | **Upsample factor (L)** 的因子 |
| 向量 | 向量 | [1, Inf] 范围内的整数 |

### 控制端口

### **Enable reset input port** — 启用复位输入端口的选项 `off`（默认）| `on`

选择此参数以启用 **reset** 输入端口。复位信号实现数据路径寄存器的本地同步复位。

有关更多复位注意事项，请参阅提示。

### **Enable ready output port** — 启用就绪输出端口的选项 off（默认）| on

选择此参数以启用 **ready** 输出端口。此端口指示模块是否已准备好接收新的输入数据。

## 所属库

DSP HDL Toolbox / Signal Operations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2022b 中引入**

## 描述

通过在输入采样之间添加零进行上采样

Upsampler 模块通过在输入采样之间添加 *L*–1 个零来对输入信号进行上采样，其中 *L* 为上采样因子。该模块支持以下输入和输出数据组合。

- 标量输入和标量输出
- 标量输入和向量输出
- 向量输入和向量输出

该模块提供适用于 HDL 代码生成和硬件部署的架构。

**注意**

您还可以使用 DSP HDL IP Designer 应用为该硬件优化算法生成 HDL 代码，而无需创建 Simulink® 模型。该应用提供与 Simulink 模块相同的接口和配置选项。
