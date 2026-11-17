---
type: simulink-block
title: 'LTE OFDM Modulator'
family: 'modulation'
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

### **data** — 输入数据标量

输入数据，指定为有符号实数或复数。
`double` 和 `single` 数据类型
支持仿真，但不支持 HDL 代码生成。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `signed fixed point`
**复数支持：** 是

### **valid** — 指示有效输入数据标量

控制信号，用于指示来自
**data** 输入端口的数据是否有效。当此值为
`1`（`true`）时，模块捕获
**data** 输入端口上的值。当此值为
`0`（`false`）时，模块忽略
**data** 输入端口上的值。

**数据类型：** `Boolean`

### **NDLRB** — 下行资源块数 `6` | `15` | `25` | `50` | `75` | `100`

下行资源块数，指定为 `6`、
`15`、`25`、`50`、
`75` 或 `100`。NDLRB 必须是
LTE 标准 TS 36.212 [1] 指定的这六个值之一。
该模块在每个子帧开始时对此端口采样，并忽略
子帧内的任何变化。

#### 依赖关系

要启用此端口，请将 **NDLRB source**
参数设置为 `Input port`。

**数据类型：** `uint8` | `uint16` | `uint32` | `fixdt(0,K,0), K >= 7` | `single` | `double`

### **cyclicPrefixType** — CP 类型标量

CP 类型，指定为 `Boolean` 标量。当此值为
`0`（false）时，模块选择 normal CP。当此值为
`1`（true）时，模块选择 extended CP。该模块在每个子帧开始时对此
端口采样，并忽略子帧内的任何变化。

#### 依赖关系

要启用此端口，请将 **Cyclic prefix source** 参数
设置为 `Input port`。

**数据类型：** `Boolean`

### **reset** — 清除内部状态标量

清除内部状态，指定为 `Boolean`
标量。当此值为 `1`
（`true`）时，模块停止当前计算并
清除所有内部状态。当此值为 `0`
（`false`）且 **valid** 输入
值为 `1`（`true`）时，模块
开始一个新子帧。

#### 依赖关系

要启用此端口，请选择 **Enable reset input
port** 参数。

**数据类型：** `Boolean`
### 输出

### **data** — 输出数据标量

输出数据，返回为有符号实数或复数。数据
类型与 **data** 输入
端口的数据类型相同。当您清除 **Divide butterfly outputs by
two** 参数时，在 inverse fast fourier transform (IFFT) 中，字长每
级增加 1 位。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `signed fixed point`
**复数支持：** 是

### **valid** — 指示有效输出数据标量

控制信号，用于指示来自
**data** 输出端口的数据是否有效。当
**data** 输出端口上存在调制样本时，模块将此
值设置为 `1`（`true`）。

**数据类型：** `Boolean`

### **ready** — 指示模块已就绪标量

控制信号，用于指示模块已准备好接收新的输入
数据。当此值为 `1`（`true`）时，
模块在下一个时间步接受输入数据。当此值为
`0`（`false`）时，模块在下一个时间步忽略
输入数据。

**数据类型：** `Boolean`

## 参数

### 主要

### **NDLRB source** — NDLRB 的来源 `Property`（默认）| `Input port`

您可以通过选择参数值或使用输入
端口来设置 NDLRB。要启用 **NDLRB** 参数，请选择
`Property`。要启用
**NDLRB** 端口，请选择 `Input
port`。

### **NDLRB** — 下行资源块数 `6`（默认）| `15` | `25` | `50` | `75` | `100`

下行资源块数，指定为 `6`、
`15`、`25`、`50`、
`75` 或 `100`。NDLRB 必须是
LTE 标准 TS 36.212 [1] 指定的这六个值之一。

#### 依赖关系

要启用此参数，请将 **NDLRB
source** 参数设置为
`Property`。

### **Cyclic prefix source** — 循环前缀的来源 `Property`（默认）| `Input port`

您可以通过选择参数值或使用
输入端口来设置循环前缀。要启用 **Cyclic prefix type**
参数，请选择 `Property`。要启用
**cyclicPrefixType** 端口，请选择
`Input port`。

### **Cyclic prefix type** — 循环前缀类型 `Normal`（默认）| `Extended`

循环前缀类型，指定为 `Normal`
或 `Extended`。

#### 依赖关系

要启用此参数，请将 **Cyclic prefix
source** 参数设置为
`Property`。

### **Windowing** — 频谱增长降低 `off`（默认）| `on`

选择此参数可执行加窗操作，该操作可降低
频谱增长，并使用 **Window length per NDLRB** 参数指定的 NDRLB 窗长。清除此
参数可禁用加窗操作。

### **Window length per NDLRB** — NDRLB 窗长 [`4, 6, 4, 6, 8, 8`]（默认）| NDLRB 窗长的行向量

NDRLB 窗长，指定为非负整数行向量，
其元素分别对应 NDLRB
`6`、`15`、`25`、
`50`、`75` 和
`100` 的窗长。默认情况下，NDLRB 6、15、25、50、75 和 100 的窗长分别为 4、6、4、6、8 和 8。
每个 NDLRB 的窗长范围为 0 到
最小 CP 值。

- 对于 normal CP，NDLRB
  `6`、`15`、
  `25`、`50`、
  `75` 和 `100` 的最小 CP 值分别为 9、18、
  36、72、144 和 144。
- 对于 extended CP，NDLRB
  `6`、`15`、
  `25`、`50`、
  `75` 和 `100` 的最小 CP 值分别为 32、
  64、128、256、512 和 512。

#### 依赖关系

要启用此参数，请选择
**Windowing** 参数。

### **Enable reset input port** — 复位信号 `off`（默认）| `on`

选择此参数可启用模块图标上的 **reset** 端口。

### **Output data sample rate** — 输出采样率 `Use maximum output data sample rate`（默认）| `Match output data sample rate to NDLRB`

此参数指定模块为输出数据
选择的采样率类型。

- 要提供 30.72 MHz 的输出数据采样率，请选择
  `Use maximum output data sample
  rate`。
- 要提供基于
  **NDLRB** 参数的输出数据采样率，请选择
  `Match output data sample rate to
  NDLRB`。NDLRB
  `6`、`15`、
  `25`、`50`、
  `75` 和 `100` 的输出采样率分别为
  1.92 MHz、3.84 MHz、7.68 MHz、15.36 MHz、30.72 MHz 和
  30.72 MHz。

有关更多信息，请参阅 Base Rate Controller。

### IFFT 模块参数

### **Divide butterfly outputs by two** — 位宽控制 `on`（默认）| `off`

当您选择此参数时，LTE OFDM Modulator 模块中的
IFFT 模块通过将每个
蝶形乘法的输出除以二来实现总体
1/*N* 缩放因子。此调整使
IFFT 模块的输出保持与其输入相同的幅度范围。如果禁用此
参数，模块通过在每次蝶形乘法后将字长增加 1
位来避免溢出。

### **Rounding Method** — 内部定点计算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

此参数指定内部
定点计算的舍入模式类型。舍入适用于旋转因子
乘法和缩放操作。有关
舍入模式的更多信息，请参阅 Rounding
Modes。

当输入为任意整数或定点数据类型时，IFFT
算法在内部计算中使用定点算术。当输入数据的数据类型为
`single` 或 `double` 时，此
参数不适用。

## 所属库

Wireless HDL Toolbox / Modulation

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink® accelerator 和 rapid accelerator 模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL
实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计中移动现有延迟，在输出处放置的寄存器数。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

不能在 Resettable Synchronous
Subsystem (HDL Coder) 内为此模块生成 HDL。

## 版本历史

**在 R2019a 中引入**

## 描述

调制 LTE 资源网格并返回时域 OFDM 样本

LTE OFDM Modulator 模块实现了一种用于调制 LTE
标准 TS 36.212 [1] 指定的 LTE
资源网格样本的算法。该模块在其操作中使用
orthogonal frequency-division multiplexing (OFDM) 机制，并
将资源网格输入样本转换为等效的时域信号输出。
OFDM 对于高频选择性信道上的通信很有效，并
广泛用于 LTE 下行链路发射机的开发。该模块实现
加窗功能，以降低 OFDM 信号的频谱再增长或相邻信道泄漏比
(ACLR)。

该模块提供适用于 HDL 代码生成和
硬件部署的接口和架构。

如 LTE 标准所述，您可以选择下行资源块数 (NDLRB)，并选择 normal
或 extended cyclic prefix (CP)。从第一个输入样本到第一个输出样本的延迟取决于您对
NDLRB 的选择。

| NDLRB | 延迟 |
| --- | --- |
| 6 | 6268 |
| 15 | 6376 |
| 25 | 6496 |
| 50 | 6796 |
| 75 | 7096 |
| 100 | 7396 |
