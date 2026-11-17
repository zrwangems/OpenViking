---
type: simulink-block
title: 'GMSK Modulator'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Modulation'
documentation_page: 'gmskmodulator'
documentation_source_path: 'ref/gmskmodulator.html'
language: zh-CN
chinese_source: worker-translation
---

# GMSK Modulator

## 端口

### 输入

### **data** — 数据位 标量

数据位，指定为布尔标量或 `ufix1`。

对于 HDL 代码生成，输入数据类型必须为 `ufix1` 或 `Boolean`，该模块支持的最大输出字长为 16 位。

**数据类型：** `Boolean` | `fixdt(0,1,0)`

### **valid** — 指示有效输入数据 标量

指示有效输入数据，指定为布尔标量。

此端口是一个控制信号，用于指示 **data** 输入端口上的样本何时有效。当该值为 `1` 时，模块采集 **data** 输入端口上的值。当该值为 `0` 时，模块忽略 **data** 输入端口上的值。

**数据类型：** `Boolean`

### **reset** — 清除内部状态 标量

清除内部状态，指定为布尔标量。当该值为 `1` 时，模块停止当前计算并清除所有内部状态。

#### 依赖关系

要启用此端口，请选中 **Enable reset input port** 参数。

**数据类型：** `Boolean`
### 输出

### **data** — 调制后的复数输出数据符号 复数标量 | 复数列向量

调制后的复数输出数据符号，以复值标量或列向量形式返回。

- 当您将 **Output type** 参数设置为 `Vector` 时，输出为每个符号的样本数组成的向量。
- 当您将 **Output type** 参数设置为 `Scalar` 时，输出为标量。

**数据类型：** `signed fixed point`
**复数支持：** 是

### **valid** — 指示有效输出数据 标量

指示有效输出数据，以标量形式返回。

此端口是一个控制信号，用于指示 **data** 输出端口何时有效。当 **data** 输出端口上有数据样本可用时，模块将此值设置为 `1`。

**数据类型：** `Boolean`

### **ready** — 指示模块已就绪 标量

指示模块已就绪，以标量形式返回。

这是一个控制信号，用于指示模块何时准备好接收新的输入数据。当该值为 `1` 时，模块在下一个时间步接受输入数据。当该值为 `0` 时，模块在下一个时间步忽略输入数据。

#### 依赖关系

要启用此端口，请将 **Output type** 参数设置为 `Scalar`。

**数据类型：** `Boolean`

## 参数

### 主要

### **Bandwidth time product** — 高斯脉冲形状的带宽与符号时间的乘积 `0.3`（默认值） | 正标量值

高斯脉冲形状的信号带宽与符号时间的乘积，指定为正标量值。

### **Pulse length** — 脉冲长度 `8`（默认值） | 范围从 1 到 16 的正整数

脉冲长度，指定为正整数。脉冲长度值表示高斯脉冲形状以符号间隔为单位的长度。

### **Symbol prehistory** — 符号先验历史 `1`（默认值） | `-1` | 长度为 *L* – 1 的由 –1 或 1 组成的向量

符号先验历史，指定为模块在仿真开始前使用的由 –1 或 1 组成的标量或向量。

- 对于标量值，模块将其扩展为长度为 *L* – 1 的向量，其中 *L* 表示脉冲长度。您可以使用 **Pulse length** 参数指定 *L* 值。

  例如，如果您指定标量值 `-1`，并且 **Pulse length** 参数设置为 `4`，则模块将此值扩展为 `[-1 -1 -1]`。
- 对于向量值，模块按时间逆序考虑向量中的元素。向量长度必须为 *L* – 1。

  例如，如果您指定向量值 `[-1 1 1]`，并且 **Pulse length** 参数设置为 `4`，则模块将此值视为 `[1 1 -1]`。

### **Phase offset (rad)** — 调制波形的相位偏移 `0`（默认值） | 范围从 -2\*π 到 2\*π 的数值标量。

调制波形的相位偏移，以弧度为单位，指定为范围从 –2\*π 到 2\*π 的数值标量。

### **Number of samples per symbol** — 每个符号的采样数 `4`（默认）| 范围 1 到 64

每个符号的采样数，指定为范围 1 到 64 的正整数。每个符号的采样数表示从输入采样到输出采样的上采样因子。

### **Number of data points** — 数据点数 `1024`（默认）| 范围 65,536 内的正整数且为 2 的幂

从查找表（LUT）中检索的数据点数，指定为正整数且为 2 的幂。该模块支持的最大值为 65,536。

### **Output type** — 输出类型 `Vector`（默认）| `Scalar`

将输出类型指定为 `Vector` 或 `Scalar`。

### 数据类型

### **Output word length** — 输出字长 `16`（默认）| 字长小于 16 的正标量值

输出字长，指定为字长小于 16 的正标量。

### Control Port

### **Enable reset input port** — 复位信号 `off`（默认）| `on`

选择此参数以启用 **reset** 输入端口。

## 所属库

Wireless HDL Toolbox / Modulation

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink® 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

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

**限制**

无法在可复位同步子系统 (HDL Coder) 内为此模块生成 HDL。

## 版本历史

**在 R2024a 中引入**

## 描述

使用高斯最小频移键控（GMSK）方法调制数据位

GMSK Modulator 模块使用高斯最小频移键控（GMSK）方法调制数据位。该模块支持标量输入，并输出调制的复值标量或列向量数据符号，同时附带 valid 和 ready 控制信号。该模块使您能够更有效地使用带宽，并有助于减少由多径衰落和信号失真引起的问题。

您可以在全球移动通信系统（GSM）、卫星通信、蓝牙、军事通信、战术无线电、无人机控制/指挥和导弹通信等应用中使用此模块。该模块提供适合 HDL 代码生成和硬件部署的接口和架构。
