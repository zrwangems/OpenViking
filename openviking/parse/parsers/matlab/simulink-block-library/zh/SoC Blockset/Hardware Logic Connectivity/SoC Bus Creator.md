---
type: simulink-block
title: 'SoC Bus Creator'
family: 'hardware-logic-connectivity'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Hardware Logic Connectivity'
documentation_page: 'socbuscreator'
documentation_source_path: 'ref/socbuscreator.html'
language: zh-CN
chinese_source: worker-translation
---

# SoC Bus Creator

## 端口

### 输入

### **valid** — Valid 控制信号 boolean 标量

Valid 控制信号，指定为标量。仅可将此端口用于数据流和像素流协议。

#### 依赖项

要启用此端口，请将 **Control protocol** 参数设置为 `Data stream` 或 `Pixel stream`，并将 **Control type** 参数设置为 `Valid`。

**数据类型：** `Boolean`

### **tlast** — 数据包结束指示 boolean 标量

数据包结束指示，指定为 Boolean 标量。

#### 依赖项

要启用此端口，请将 **Control protocol** 参数设置为 `Data stream`，并将 **Control type** 参数设置为 `Valid`。

**数据类型：** `Boolean`

### **ready** — Ready 控制信号 boolean 标量

Ready 控制信号，指定为 Boolean 标量。此端口可用于 `Data stream` 和 `Pixel stream` 控制协议。

#### 依赖项

要启用此端口，请将 **Control protocol** 参数设置为 `Data stream` 或 `Pixel stream`，并将 **Control type** 参数设置为 `Ready` 或 `Ready with frame sync`。

**数据类型：** `Boolean`

### **hStart** — 帧水平线中的第一个像素 boolean 标量

帧的水平线中的第一个像素，指定为 Boolean 标量。

#### 依赖项

要启用此端口，请将 **Control protocol** 参数设置为 `Pixel stream`，并将 **Control type** 参数设置为 `Valid`。

**数据类型：** `Boolean`

### **hEnd** — 帧水平线中的最后一个像素 boolean 标量

帧的水平线中的最后一个像素，指定为 Boolean 标量。

#### 依赖项

要启用此端口，请将 **Control protocol** 参数设置为 `Pixel stream`，并将 **Control type** 参数设置为 `Valid`。

**数据类型：** `Boolean`

### **vStart** — 帧第一（顶部）行中的第一个像素 boolean 标量

帧的第一（顶部）行中的第一个像素，指定为 Boolean 标量。

#### 依赖项

要启用此端口，请将 **Control protocol** 参数设置为 `Pixel stream`，并将 **Control type** 参数设置为 `Valid`。

**数据类型：** `Boolean`

### **vEnd** — 帧最后（底部）行中的最后一个像素 boolean 标量

帧的最后（底部）行中的最后一个像素，指定为 Boolean 标量。

#### 依赖项

要启用此端口，请将 **Control protocol** 参数设置为 `Pixel stream`，并将 **Control type** 参数设置为 `Valid`。

**数据类型：** `Boolean`

### **fsync** — 帧同步 boolean 标量

帧同步，指定为 Boolean 标量。

#### 依赖项

要启用此端口，请将 **Control protocol** 参数设置为 `Pixel stream`，并将 **Control type** 参数设置为 `Ready with frame sync`。

**数据类型：** `Boolean`

### **rd\_addr** — 读取器地址标量

读取器地址，指定为标量。它是在事务的第一个周期采样的读取事务的起始地址。

#### 依赖项

要启用此端口，请将 **Control protocol** 参数设置为 `Random access read`。

**数据类型：** `uint32`

### **rd\_len** — 读取器数据长度标量

读取器数据长度，指定为标量。它表示要读取的数据值数量，在事务的第一个周期采样。

#### 依赖项

要启用此端口，请将 **Control protocol** 参数设置为 `Random access read`。

**数据类型：** `uint32`

### **rd\_avalid** — 读取器有效状态 boolean 标量

读取器有效状态，指定为 Boolean 标量。它指示读取请求是否有效。

#### 依赖项

要启用此端口，请将 **Control protocol** 参数设置为 `Random access read`。

**数据类型：** `Boolean`

### **rd\_dready** — 读取器就绪状态 boolean 标量

读取器就绪状态，指定为 Boolean 标量。它指示硬件逻辑何时可以开始接受数据。

#### 依赖项

要启用此端口，请将 **Control protocol** 参数设置为 `Random access read`。

**数据类型：** `Boolean`

### **wr\_addr** — 写入器地址标量

指定硬件写入的起始地址。

#### 依赖项

要启用此端口，请将 **Control protocol** 参数设置为 `Random access write`。

**数据类型：** `uint32`

### **wr\_len** — 写入器数据长度标量

指定写事务中的数据元素数量。

#### 依赖项

要启用此端口，请将 **Control protocol** 参数设置为 `Random access write`。

**数据类型：** `uint32`

### **wr\_valid** — 写入器有效数据 boolean 标量

写入器有效数据，指定为标量。它指示输出处采样的数据信号有效。

#### 依赖项

要启用此端口，请将 **Control protocol** 参数设置为 `Random access write`。

**数据类型：** `Boolean`

### 输出

### **ctrlBus** — 输出控制总线 bus

输出控制总线，以总线形式返回。

输出控制总线的数据类型取决于 **Control protocol** 和 **Control type** 参数的值。

| 参数配置 | 输出数据类型 |
| --- | --- |
| 将 **Control protocol** 设置为 `Data stream`，将 **Control type** 设置为 `Ready`。 | `StreamS2MBusObj` |
| 将 **Control protocol** 设置为 `Data stream`，将 **Control type** 设置为 `Valid`。 | `StreamM2SBusObj` |
| 将 **Control protocol** 设置为 `Pixel stream`，将 **Control type** 设置为 `Ready`。 | `StreamVideoS2MBusObj` |
| 将 **Control protocol** 设置为 `Pixel stream`，将 **Control type** 设置为 `Valid`。 | `pixelcontrol` |
| 将 **Control protocol** 设置为 `Pixel stream`，将 **Control type** 设置为 `Ready frame with sync`。 | `StreamvideoFsyncS2MBusObj` |
| 将 **Control protocol** 设置为 `Random access read`，将 **Control type** 设置为 `Ready`。 | `ReadControlM2SBusObj` |
| 将 **Control protocol** 设置为 `Random access write`，将 **Control type** 设置为 `Valid`。 | `WriteControlM2SBusObj` |

**数据类型：** `StreamS2MBusObj` | `StreamM2SBusObj` | `StreamVideoS2MBusObj` | `pixelcontrol` | `StreamvideoFsyncS2MBusObj` | `ReadControlM2SBusObj` | `WriteControlM2SBusObj`

## 参数

### **Control protocol** — 协议接口选择 `Data stream`（默认） | `Pixel stream` | `Random access read` | `Random access write`

将协议接口指定为以下值之一：

- `Data stream` — 如果需要 AXI4 数据流，请使用此协议。
- `Pixel stream` — 如果需要 AXI4 视频流，请使用此协议。
- `Random access read` — 如果需要 AXI4 读取，请使用此协议。
- `Random access write` — 如果需要 AXI4 写入，请使用此协议。

模块的输入端口根据所选 **Control protocol** 和 **Control type** 的类型而变化。有关更多详细信息，请参阅描述。

### **Control type** — 控制类型选择 `Valid`（默认） | `Ready` | `Ready with frame sync`

指定控制类型。

要启用 `Ready with frame sync` 选项，请将 **Control protocol** 参数设置为 `Pixel stream`。

模块的输入端口根据所选 **Control protocol** 和 **Control type** 的类型而变化。有关更多详细信息，请参阅描述。

## 所属库

SoC Blockset / Hardware Logic Connectivity

## 模块特性

R2025b 中未记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

要为您的设计自动生成 HDL 代码，并在 SoC 设备上执行，请使用 **SoC Builder** 工具。请参阅使用 SoC Builder 生成 SoC 设计。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**R2019a 中引入**

## 描述

将控制信号转换为总线

SoC Bus Creator 模块将一组信号组合成总线。该模块接受控制信号并输出总线。

您可以配置此模块以支持多种协议接口类型。此模块的参数和端口配置根据所需的协议接口类型和操作模式而变化，如下表所述。

| 协议接口类型 | 操作模式 | 参数配置 | 启用的输入端口 |
| --- | --- | --- | --- |
| Data stream | 读取数据流 | 将 **Control protocol** 设置为 `Data stream`，将 **Control type** 设置为 `Ready`。 | **ready** |
| 写入数据流 | 将 **Control protocol** 设置为 `Data stream`，将 **Control type** 设置为 `Valid`。 | **valid** |
| **tlast** |
| Pixel stream | 读取视频流 | 将 **Control protocol** 设置为 `Pixel stream`，将 **Control type** 设置为 `Ready`。 | **ready** |
| 写入视频流 | 将 **Control protocol** 设置为 `Pixel stream`，将 **Control type** 设置为 `Valid`。 | **hStart** |
| **hEnd** |
| **vStart** |
| **vEnd** |
| **valid** |
| 带帧同步的读取视频流 | 将 **Control protocol** 设置为 `Pixel stream`，将 **Control type** 设置为 `Ready frame with sync`。 | **ready** |
| **fsync** |
| Random access read | 读取数据 | 将 **Control protocol** 设置为 `Random access read`，将 **Control type** 设置为 `Ready`。 | **rd\_addr** |
| **rd\_len** |
| **rd\_avalid** |
| **rd\_dready** |
| Random access write | 写入数据 | 将 **Control protocol** 设置为 `Random access write`，将 **Control type** 设置为 `Valid`。 | **wr\_addr** |
| **wr\_len** |
| **wr\_valid** |
