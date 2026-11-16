---
type: simulink-block
title: 'OFDM Equalizer'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Modulation'
documentation_page: 'ofdmequalizer'
documentation_source_path: 'ref/ofdmequalizer.html'
language: zh-CN
chinese_source: worker-translation
---

# OFDM Equalizer

## 端口

### 输入

### **data** — OFDM 数据标量

OFDM 数据，指定为复值标量。

该软件支持 `double` 和
`single` 数据类型用于仿真，但不支持 HDL 代码生成。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `signed fixed point`

### **hEst** — 信道估计数据标量

信道估计数据，指定为复值标量。

输入数据类型必须为
`fixdt(1,k,m)`，其中
*k* 小于或等于 30，且 *m* 小于
*k*。

该软件支持 `double` 和
`single` 数据类型用于仿真，但不支持 HDL 代码生成。

**数据类型：** `single` | `double` | `int8` | `int16` | `fixed point`

### **valid** — 用于指示有效输入数据的控制标量

用于指示有效输入数据的控制，指定为布尔标量。

此端口是一个控制信号，用于指示输入
**data** 和 **hEst** 端口值何时有效。当
此值为 `1` 时，模块捕获 **data** 和 **hEst** 输入端口上的值。当此值为
`0` 时，模块忽略 **data**
和 **hEst** 输入端口上的值。

**数据类型：** `Boolean`

### **hEstLen** — 每个符号的估计信道长度标量

每个符号的估计信道长度，指定为范围
从 2 到 65,536 的标量。

为了支持每个符号的最小子载波数，此数据类型必须为
`fixdt(0,k,0)`，其中 *k*
大于或等于 2。

该软件支持 `double` 和
`single` 数据类型用于仿真，但不支持 HDL 代码生成。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **loadhEst** — 信道估计控制标量

信道估计控制，指定为布尔标量。

当此值为 `1` 时，模块加载信道估计，
直到 **hEstLen**
输入端口指定的信道估计长度。**hEstLen** 在
**loadhEst** 时采样。

当此值为 `0`，且输入为 `1` 时，
模块使用先前采样的
**hEstLen** 输入和存储的 **hEst** 输入
值执行均衡。如果先前采样的 **hEstLen** 值不可用，
模块使用瞬时输入
**data**、**hEst** 和 **nVar**
执行均衡。
有关更多信息，请参阅算法。

**数据类型：** `Boolean`

### **nVar** — 噪声方差标量

噪声方差，指定为标量。

当输入 **valid** 为 `1` 时，模块
采样 **nVar** 端口。此值的数据类型必须为
`fixdt(0,k,m)`，其中
*k* 小于或等于 16，且 *m* 小于
或等于 *k*。

该软件支持 `double` 和
`single` 数据类型用于仿真，但不支持 HDL 代码生成。

#### 依赖项

要启用此端口，请将 **均衡方法** 参数
设置为 `MMSE`。

**数据类型：** `single` | `double` | `uint8` | `uint16` | `fixed point`

### **reset** — 复位内部状态标量

将模块的内部状态复位以使用新数据开始，指定为
标量。

#### 依赖项

要启用此端口，请选择 **启用复位输入端口**
参数。

**数据类型：** `Boolean`
### 输出

### **data** — 复输出数据标量

复输出数据，以标量形式返回。输出数据类型与
输入数据类型相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `signed fixed point`

### **valid** — 指示有效输出数据标量

指示有效输出数据，以布尔标量形式返回。

此端口是一个控制信号，用于指示 **data**
输出端口何时有效。当 **data**
输出端口上有可用数据样本时，模块将此输出
**valid** 值设置为 `1`。

**数据类型：** `Boolean`

## 参数

### **均衡方法** — 均衡方法 `ZF`（默认）| `MMSE`

选择均衡方法。有关均衡方法的更多信息，
请参阅算法。

### **每个符号的信道估计最大长度** — 每个符号的信道估计最大长度 `52`（默认）| 范围从 2 到 65,536 的整数

指定每个符号的信道估计最大长度。

为了支持每个符号的最小子载波数（即 2），**hEstLen** 输入的数据类型
必须为
`fixdt(0,k,0)`，其中 *k*
大于或等于 2。

### **启用复位输入端口** — 复位信号 `off`（默认）| `on`

选择此参数以启用 **reset** 输入端口。

## 所属库

Wireless HDL Toolbox / Modulation

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink® 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和
综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

不能在 Resettable Synchronous Subsystem (HDL Coder) 内为此模块生成 HDL。

## 版本历史

**在 R2021a 中引入**

## 描述

使用信道估计对 OFDM 数据进行均衡

OFDM Equalizer 模块使用信道估计对 OFDM 数据进行均衡。
该模块支持频域信道均衡的迫零（ZF）和最小均方误差（MMSE）算法。该模块接受数据符号、估计
信道（**hEst**）和每个符号的估计信道长度
（**hEstLen**）数据端口，以及 **valid** 和
**loadhEst** 控制端口。该模块输出一个均衡后的数据端口和一个
**valid** 控制端口。

您可以使用此模块均衡不同通信标准中的信道效应，
例如长期演进（LTE）[1]、5G 新空口（NR）标准
TS 38.212 [2] 和无线局域网
（WLAN）[3]。

该模块提供适用于 HDL 代码生成和
硬件部署的接口和架构。
