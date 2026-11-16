---
type: simulink-block
title: 'SoC Bus Selector'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Hardware Logic Connectivity'
documentation_page: 'socbusselector'
documentation_source_path: 'ref/socbusselector.html'
language: zh-CN
chinese_source: worker-translation
---

# SoC Bus Selector

## 端口

### 输入

### **ctrlBus** — 输入控制总线 bus

输入控制总线，指定为总线。

输入控制总线的数据类型取决于 **Control protocol** 和 **Control type** 参数的值。

| 参数配置 | 输入数据类型 |
| --- | --- |
| 将 **Control protocol** 设置为 `Data stream`，将 **Control type** 设置为 `Valid`。 | `StreamM2SBusObj` |
| 将 **Control protocol** 设置为 `Data stream`，将 **Control type** 设置为 `Ready`。 | `StreamS2MBusObj` |
| 将 **Control protocol** 设置为 `Pixel stream`，将 **Control type** 设置为 `Valid`。 | `pixelcontrol` |
| 将 **Control protocol** 设置为 `Pixel stream`，将 **Control type** 设置为 `Ready`。 | `StreamVideoS2MBusObj` |
| 将 **Control protocol** 设置为 `Random access read`，将 **Control type** 设置为 `Valid`。 | `ReadControlS2MBusObj` |
| 将 **Control protocol** 设置为 `Random access write`，将 **Control type** 设置为 `Ready`。 | `WriteControlS2MBusObj` |

**数据类型：** `StreamM2SBusObj` | `StreamS2MBusObj` | `pixelcontrol` | `StreamVideoS2MBusObj` | `ReadControlS2MBusObj` | `WriteControlS2MBusObj`
### 输出

### **valid** — 有效控制信号 boolean scalar

有效控制信号，以标量形式返回。此端口仅可用于 data stream 和 pixel stream 协议。

#### 依赖关系

要启用此端口，请将 **Control protocol** 参数设置为 `Data stream` 或 `Pixel stream`，并将 **Control type** 参数设置为 `Valid`。

**数据类型：** `Boolean`

### **tlast** — 数据包结束指示 boolean scalar

数据包结束的指示，以 Boolean 标量形式返回。

#### 依赖关系

要启用此端口，请将 **Control protocol** 参数设置为 `Data stream`，并将 **Control type** 参数设置为 `Valid`。

**数据类型：** `Boolean`

### **ready** — 就绪控制信号 boolean scalar

就绪控制信号，以 Boolean 标量形式返回。此端口可用于 `Data stream` 和 `Pixel stream` 控制协议。

#### 依赖关系

要启用此端口，请将 **Control protocol** 参数设置为 `Data stream` 或 `Pixel stream`，并将 **Control type** 参数设置为 `Ready`。

**数据类型：** `Boolean`

### **hStart** — 帧的水平行中的第一个像素 boolean scalar

帧的水平行中的第一个像素，以 Boolean 标量形式返回。

#### 依赖关系

要启用此端口，请将 **Control protocol** 参数设置为 `Pixel stream`，并将 **Control type** 参数设置为 `Valid`。

**数据类型：** `Boolean`

### **hEnd** — 帧的水平行中的最后一个像素 boolean scalar

帧的水平行中的最后一个像素，以 Boolean 标量形式返回。

#### 依赖关系

要启用此端口，请将 **Control protocol** 参数设置为 `Pixel stream`，并将 **Control type** 参数设置为 `Valid`。

**数据类型：** `Boolean`

### **vStart** — 帧的第一行（顶部）中的第一个像素 boolean scalar

帧的第一行（顶部）中的第一个像素，以 Boolean 标量形式返回。

#### 依赖关系

要启用此端口，请将 **Control protocol** 参数设置为 `Pixel stream`，并将 **Control type** 参数设置为 `Valid`。

**数据类型：** `Boolean`

### **vEnd** — 帧的最后一行（底部）中的最后一个像素 boolean scalar

帧的最后一行（底部）中的最后一个像素，以 Boolean 标量形式返回。

#### 依赖关系

要启用此端口，请将 **Control protocol** 参数设置为 `Pixel stream`，并将 **Control type** 参数设置为 `Valid`。

**数据类型：** `Boolean`

### **rd\_aready** — 接受读请求 boolean scalar

接受读请求，以标量形式返回。它指示何时接受读请求。

#### 依赖关系

要启用此端口，请将 **Control protocol** 参数设置为 `Random access read`。

**数据类型：** `Boolean`

### **rd\_dvalid** — 读请求有效 boolean scalar

读请求有效，以 Boolean 标量形式返回。它是控制信号，指示从读请求返回的数据有效。

#### 依赖关系

要启用此端口，请将 **Control protocol** 参数设置为 `Random access read`。

**数据类型：** `Boolean`

### **wr\_ready** — 写就绪信号 boolean scalar

写就绪信号，以 Boolean 标量形式返回。它对应于来自从 IP 核或外部存储器的背压。当此值为 `1`（`high`）时，指示可以发送数据。当此值为 `0`（`low`）时，指示硬件逻辑必须在一个时钟周期内停止发送数据。

#### 依赖关系

要启用此端口，请将 **Control protocol** 参数设置为 `Random access write`。

**数据类型：** `Boolean`

### **wr\_bvalid** — 写有效信号 boolean scalar

写有效信号，以 Boolean 标量形式返回。它是来自从 IP 核的响应信号，可用于诊断目的。在 AXI4 互连接受每个突发事务后，此值变为 `1`（`high`）。

#### 依赖关系

要启用此端口，请将 **Control protocol** 参数设置为 `Random access write`。

**数据类型：** `Boolean`

### **wr\_complete** — 写事务完成 boolean scalar

写事务完成，指定为 Boolean 标量。它是这样一种控制信号：当其保持高电平一个时钟周期时，指示写事务已完成。此信号在突发的最后一个 `wr_bvalid` 时置位。

#### 依赖关系

要启用此端口，请将 **Control protocol** 参数设置为 `Random access write`。

**数据类型：** `Boolean`

## 参数

### **Control protocol** — 协议接口选择 `Data stream`（默认） | `Pixel stream` | `Random access read` | `Random access write`

将协议接口指定为以下值之一：

- `Data stream` — 如果需要 AXI4 数据流，请使用此协议。
- `Pixel stream` — 如果需要 AXI4 视频流，请使用此协议。
- `Random access read` — 如果需要 AXI4 读取，请使用此协议。
- `Random access write` — 如果需要 AXI4 写入，请使用此协议。

模块的输出端口根据所选的 **Control protocol** 和 **Control type** 类型而变化。有关更多详细信息，请参阅描述。

### **Control type** — 控制类型选择 `Valid`（默认） | `Ready`

指定控制类型。

模块的输出端口根据所选的 **Control protocol** 和 **Control type** 类型而变化。有关更多详细信息，请参阅描述。

## 所属库

SoC Blockset / Hardware Logic Connectivity

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

要为您的设计自动生成 HDL 代码，并在 SoC 设备上执行，请使用 **SoC Builder** 工具。请参阅使用 SoC Builder 生成 SoC 设计。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2019a 中引入**

## 描述

将总线转换为控制信号

SoC Bus Selector 模块从总线中转换出一组控制信号。该模块接受一个总线并输出控制信号。

您可以配置此模块以支持多种协议接口类型。此模块的参数和端口配置根据您所需的协议接口类型和操作模式而变化，如下表所述。

| 协议接口类型 | 操作模式 | 参数配置 | 启用的输出端口 |
| --- | --- | --- | --- |
| Data stream | 读取流数据 | 将 **Control protocol** 设置为 `Data stream`，将 **Control type** 设置为 `Valid`。 | **valid** |
| **tlast** |
| 写入流数据 | 将 **Control protocol** 设置为 `Data stream`，将 **Control type** 设置为 `Ready`。 | **ready** |
| Pixel stream | 读取视频流 | 将 **Control protocol** 设置为 `Pixel stream`，将 **Control type** 设置为 `Valid`。 | **hStart** |
| **hEnd** |
| **vStart** |
| **vEnd** |
| **valid** |
| 写入视频流 | 将 **Control protocol** 设置为 `Pixel stream`，将 **Control type** 设置为 `Ready`。 | **ready** |
| Random access read | 读取数据 | 将 **Control protocol** 设置为 `Random access read`，将 **Control type** 设置为 `Valid`。 | **rd\_aready** |
| **rd\_dvalid** |
| Random access write | 写入数据 | 将 **Control protocol** 设置为 `Random access write`，将 **Control type** 设置为 `Ready`。 | **wr\_ready** |
| **wr\_bvalid** |
| **wr\_complete** |
