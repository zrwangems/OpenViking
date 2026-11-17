---
type: simulink-block
title: 'LTE OFDM Modulator'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Modulation'
documentation_page: 'lteofdmmodulator'
documentation_source_path: 'ref/lteofdmmodulator.html'
language: zh-CN
chinese_source: worker-translation
---

# LTE OFDM Modulator

## 端口

### 输入

### **data** — 输入数据 标量

输入数据，指定为有符号实数或复数。仿真支持 `double` 和 `single` 数据类型，但不支持 HDL 代码生成。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `signed fixed point`
**复数支持：** 是

### **valid** — 指示输入数据有效 标量

控制信号，用于指示来自 **data** 输入端口的数据是否有效。当该值为 `1`（`true`）时，模块采集 **data** 输入端口上的值。当该值为 `0`（`false`）时，模块忽略 **data** 输入端口上的值。

**数据类型：** `Boolean`

### **NDLRB** — 下行资源块数量 `6` | `15` | `25` | `50` | `75` | `100`

下行资源块数量，指定为 `6`、`15`、`25`、`50`、`75` 或 `100`。NDLRB 必须是 LTE 标准 TS 36.212 [1] 规定的这六个值之一。模块在每个子帧开始时对该端口进行采样，并忽略子帧内的任何变化。

#### 依赖关系

要启用此端口，请将 **NDLRB source** 参数设置为 `Input port`。

**数据类型：** `uint8` | `uint16` | `uint32` | `fixdt(0,K,0), K >= 7` | `single` | `double`

### **cyclicPrefixType** — CP 类型 标量

CP 类型，指定为 `Boolean` 标量。当该值为 `0`（false）时，模块选择常规 CP。当该值为 `1`（true）时，模块选择扩展 CP。模块在每个子帧开始时对该端口进行采样，并忽略子帧内的任何变化。

#### 依赖关系

要启用此端口，请将 **Cyclic prefix source** 参数设置为 `Input port`。

**数据类型：** `Boolean`

### **reset** — 清除内部状态 标量

清除内部状态，指定为 `Boolean` 标量。当该值为 `1`（`true`）时，模块停止当前计算并清除所有内部状态。当该值为 `0`（`false`）且 **valid** 输入值为 `1`（`true`）时，模块开始一个新的子帧。

#### 依赖关系

要启用此端口，请选择 **Enable reset input port** 参数。

**数据类型：** `Boolean`
### 输出

### **data** — 输出数据 标量

输出数据，以有符号实数或复数形式返回。数据类型与 **data** 输入端口的数据类型相同。当您清除 **Divide butterfly outputs by two** 参数时，在逆快速傅里叶变换（IFFT）中每级字长增加 1 位。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `signed fixed point`
**复数支持：** 是

### **valid** — 指示输出数据有效 标量

控制信号，用于指示来自 **data** 输出端口的数据是否有效。当 **data** 输出端口上有调制样本可用时，模块将该值设置为 `1`（`true`）。

**数据类型：** `Boolean`

### **ready** — 指示模块已就绪 标量

控制信号，用于指示模块已准备好接收新的输入数据。当该值为 `1`（`true`）时，模块在下一个时间步接受输入数据。当该值为 `0`（`false`）时，模块在下一个时间步忽略输入数据。

**数据类型：** `Boolean`

## 参数

### 主

### **NDLRB source** — NDLRB 的来源 `Property`（默认） | `Input port`

您可以通过选择参数值或使用输入端口来设置 NDLRB。要启用 **NDLRB** 参数，请选择 `Property`。要启用 **NDLRB** 端口，请选择 `Input port`。

### **NDLRB** — 下行资源块数量 `6`（默认） | `15` | `25` | `50` | `75` | `100`

下行资源块数量，指定为 `6`、`15`、`25`、`50`、`75` 或 `100`。NDLRB 必须是 LTE 标准 TS 36.212 [1] 规定的这六个值之一。

#### 依赖关系

要启用此参数，请将 **NDLRB source** 参数设置为 `Property`。

### **Cyclic prefix source** — 循环前缀 `Property`（默认）| `Input port` 的来源

您可以通过选择参数值或使用输入端口来设置循环前缀。要启用 **Cyclic prefix type** 参数，请选择 `Property`。要启用 **cyclicPrefixType** 端口，请选择 `Input port`。

### **Cyclic prefix type** — 循环前缀类型 `Normal`（默认）| `Extended`

循环前缀类型，指定为 `Normal` 或 `Extended`。

#### 依赖关系

要启用此参数，请将 **Cyclic prefix source** 参数设置为 `Property`。

### **Windowing** — 频谱增长抑制 `off`（默认）| `on`

选择此参数可执行加窗操作，从而减少频谱增长，并使用由 **Window length per NDLRB** 参数指定的 NDRLB 窗长。清除此参数可禁用加窗操作。

### **Window length per NDLRB** — NDRLB 窗长 [`4, 6, 4, 6, 8, 8`]（默认）| NDLRB 窗长的行向量

NDRLB 窗长，指定为非负整数的行向量，其元素分别对应 NDRLB `6`、`15`、`25`、`50`、`75` 和 `100` 的窗长。默认情况下，NDRLB 6、15、25、50、75 和 100 的窗长分别为 4、6、4、6、8 和 8。每个 NDLRB 的窗长范围可以为 0 到最小 CP 值。

- 对于 normal CP，NDRLB `6`、`15`、`25`、`50`、`75` 和 `100` 的最小 CP 值分别为 9、18、36、72、144 和 144。
- 对于 extended CP，NDRLB `6`、`15`、`25`、`50`、`75` 和 `100` 的最小 CP 值分别为 32、64、128、256、512 和 512。

#### 依赖关系

要启用此参数，请选择 **Windowing** 参数。

### **Enable reset input port** — 复位信号 `off`（默认）| `on`

选择此参数可在模块图标上启用 **reset** 端口。

### **Output data sample rate** — 输出采样率 `Use maximum output data sample rate`（默认）| `Match output data sample rate to NDLRB`

此参数指定模块为输出数据选择的采样率类型。

- 要提供 30.72 MHz 的输出数据采样率，请选择 `Use maximum output data sample rate`。
- 要基于 **NDLRB** 参数提供输出数据采样率，请选择 `Match output data sample rate to NDLRB`。NDLRB `6`、`15`、`25`、`50`、`75` 和 `100` 的输出采样率分别为 1.92 MHz、3.84 MHz、7.68 MHz、15.36 MHz、30.72 MHz 和 30.72 MHz。

有关详细信息，请参阅 Base Rate Controller。

### IFFT 模块参数

### **Divide butterfly outputs by two** — 位宽控制 `on`（默认）| `off`

当您选择此参数时，LTE OFDM Modulator 模块中的 IFFT 模块通过将每个蝶形乘法的输出除以二来实现总体 1/*N* 比例因子。此调整使 IFFT 模块的输出保持与其输入相同的幅度范围。如果您禁用此参数，则该模块通过在每次蝶形乘法后将字长增加 1 位来避免溢出。

### **Rounding Method** — 内部定点计算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

此参数指定内部定点计算的舍入模式类型。舍入适用于旋转因子乘法和缩放操作。有关舍入模式的详细信息，请参阅 Rounding Modes。

当输入为任何整数或定点数据类型时，IFFT 算法使用定点算术进行内部计算。当输入数据为 `single` 或 `double` 数据类型时，此参数不适用。

## 所属库

Wireless HDL Toolbox / Modulation

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持针对 Simulink® 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

无法为可复位同步子系统 (HDL Coder) 内的此模块生成 HDL。

## 版本历史

**在 R2019a 中引入**

## 描述

调制 LTE 资源网格并返回时域 OFDM 采样

LTE OFDM Modulator 模块实现了用于调制由 LTE 标准 TS 36.212 [1] 指定的 LTE 资源网格采样的算法。该模块在其操作中使用正交频分复用 (OFDM) 机制，并将资源网格输入采样转换为等效的时域信号输出。OFDM 对于在高频选择性信道上的通信非常有效，并广泛用于 LTE 下行链路发射机的开发。该模块实现了加窗功能，以减少 OFDM 信号的频谱再生或相邻信道泄漏比 (ACLR)。

该模块提供了适用于 HDL 代码生成和硬件部署的接口和架构。

您可以选择下行链路资源块数量 (NDLRB)，并选择常规或扩展循环前缀 (CP)，如 LTE 标准中所述。从第一个输入采样到第一个输出采样的延迟取决于您对 NDLRB 的选择。

| NDLRB | 延迟 |
| --- | --- |
| 6 | 6268 |
| 15 | 6376 |
| 25 | 6496 |
| 50 | 6796 |
| 75 | 7096 |
| 100 | 7396 |
