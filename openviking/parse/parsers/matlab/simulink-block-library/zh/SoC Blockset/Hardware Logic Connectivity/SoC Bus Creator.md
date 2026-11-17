---
type: simulink-block
title: 'SoC Bus Creator'
family: 'soc'
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

### **valid** — 有效控制信号 布尔标量

有效控制信号，指定为标量。您只能将此端口用于数据流和像素流协议。

#### 依赖

要启用此端口，请将 **Control protocol** 参数设置为 `Data stream` 或 `Pixel stream`，并将 **Control type** 参数设置为 `Valid`。

**数据类型：** `Boolean`

### **tlast** — 数据包结束指示 布尔标量

数据包结束指示，指定为布尔标量。

#### 依赖

要启用此端口，请将 **Control protocol** 参数设置为 `Data stream`，并将 **Control type** 参数设置为 `Valid`。

**数据类型：** `Boolean`

### **ready** — 就绪控制信号 布尔标量

就绪控制信号，指定为布尔标量。此端口可用于 `Data stream` 和 `Pixel stream` 控制协议。

#### 依赖

要启用此端口，请将 **Control protocol** 参数设置为 `Data stream` 或 `Pixel stream`，并将 **Control type** 参数设置为 `Ready` 或 `Ready with frame sync`。

**数据类型：** `Boolean`

### **hStart** — 帧水平行中的第一个像素 布尔标量

帧水平行中的第一个像素，指定为布尔标量。

#### 依赖

要启用此端口，请将 **Control protocol** 参数设置为 `Pixel stream`，并将 **Control type** 参数设置为 `Valid`。

**数据类型：** `Boolean`

### **hEnd** — 帧水平行中的最后一个像素 布尔标量

帧水平行中的最后一个像素，指定为布尔标量。

#### 依赖

要启用此端口，请将 **Control protocol** 参数设置为 `Pixel stream`，并将 **Control type** 参数设置为 `Valid`。

**数据类型：** `Boolean`

### **vStart** — 帧第一（顶部）行中的第一个像素 布尔标量

帧第一（顶部）行中的第一个像素，指定为布尔标量。

#### 依赖

要启用此端口，请将 **Control protocol** 参数设置为 `Pixel stream`，并将 **Control type** 参数设置为 `Valid`。

**数据类型：** `Boolean`

### **vEnd** — 帧最后（底部）行中的最后一个像素 布尔标量

帧最后（底部）行中的最后一个像素，指定为布尔标量。

#### 依赖

要启用此端口，请将 **Control protocol** 参数设置为 `Pixel stream`，并将 **Control type** 参数设置为 `Valid`。

**数据类型：** `Boolean`

### **fsync** — 帧同步 布尔标量

帧同步，指定为布尔标量。

#### 依赖

要启用此端口，请将 **Control protocol** 参数设置为 `Pixel stream`，并将 **Control type** 参数设置为 `Ready with frame sync`。

**数据类型：** `Boolean`

### **rd\_addr** — 读取器地址 标量

读取器地址，指定为标量。它是读事务的起始地址，在事务的第一个周期采样。

#### 依赖

要启用此端口，请将 **Control protocol** 参数设置为 `Random access read`。

**数据类型：** `uint32`

### **rd\_len** — 读取器数据长度 标量

读取器数据长度，指定为标量。它表示您要读取的数据值数量，在事务的第一个周期采样。

#### 依赖

要启用此端口，请将 **Control protocol** 参数设置为 `Random access read`。

**数据类型：** `uint32`

### **rd\_avalid** — 读取器有效状态 布尔标量

读取器有效状态，指定为布尔标量。它指示读请求是否有效。

#### 依赖

要启用此端口，请将 **Control protocol** 参数设置为 `Random access read`。

**数据类型：** `Boolean`

### **rd\_dready** — 读取器就绪状态 布尔标量

读取器就绪状态，指定为布尔标量。它指示硬件逻辑何时可以开始接受数据。

#### 依赖

要启用此端口，请将 **Control protocol** 参数设置为 `Random access read`。

**数据类型：** `Boolean`

### **wr\_addr** — 写入地址标量

指定硬件写入的起始地址。

#### 依赖关系

要启用此端口，请将 **Control protocol** 参数设置为 `Random access write`。

**数据类型：** `uint32`

### **wr\_len** — 写入数据长度标量

指定写入事务中的数据元素数量。

#### 依赖关系

要启用此端口，请将 **Control protocol** 参数设置为 `Random access write`。

**数据类型：** `uint32`

### **wr\_valid** — 写入有效数据布尔标量

写入有效数据，指定为标量。它指示在输出端采样的数据信号是有效的。

#### 依赖关系

要启用此端口，请将 **Control protocol** 参数设置为 `Random access write`。

**数据类型：** `Boolean`
### 输出

### **ctrlBus** — 输出控制总线 总线

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

### **Control protocol** — 协议接口选择 `Data stream`（默认）| `Pixel stream` | `Random access read` | `Random access write`

将协议接口指定为以下值之一：

- `Data stream` — 如果需要 AXI4 数据流，请使用此协议。
- `Pixel stream` — 如果需要 AXI4 视频流，请使用此协议。
- `Random access read` — 如果需要 AXI4 读取，请使用此协议。
- `Random access write` — 如果需要 AXI4 写入，请使用此协议。

模块的输入端口因所选的 **Control protocol** 和 **Control type** 类型而异。有关更多详细信息，请参阅描述。

### **Control type** — 控制类型选择 `Valid`（默认）| `Ready` | `Ready with frame sync`

指定控制类型。

要启用 `Ready with frame sync` 选项，请将 **Control protocol** 参数设置为 `Pixel stream`。

模块的输入端口因所选的 **Control protocol** 和 **Control type** 类型而异。有关更多详细信息，请参阅描述。

## 所属库

SoC Blockset / Hardware Logic Connectivity

## 模块特性

R2025b 中未记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

要为您的设计自动生成 HDL 代码，并在 SoC 设备上执行，请使用 **SoC Builder** 工具。请参阅 Use SoC Builder to Generate SoC Design。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2019a 中引入**

## 描述

将控制信号转换为总线

SoC Bus Creator 模块将一组信号组合成一条总线。该模块接受控制信号并输出一条总线。

您可以配置此模块以支持多种协议接口类型。此模块的参数和端口配置因所需的协议接口类型和工作模式而异，如下表所示。

| 协议接口类型 | 工作模式 | 参数配置 | 启用的输入端口 |
| --- | --- | --- | --- |
| 数据流 | 读数据流 | 将 **Control protocol** 设置为 `Data stream`，将 **Control type** 设置为 `Ready`。 | **ready** |
| 写数据流 | 将 **Control protocol** 设置为 `Data stream`，将 **Control type** 设置为 `Valid`。 | **valid** |
| **tlast** |
| 像素流 | 读视频流 | 将 **Control protocol** 设置为 `Pixel stream`，将 **Control type** 设置为 `Ready`。 | **ready** |
| 写视频流 | 将 **Control protocol** 设置为 `Pixel stream`，将 **Control type** 设置为 `Valid`。 | **hStart** |
| **hEnd** |
| **vStart** |
| **vEnd** |
| **valid** |
| 带帧同步的读视频流 | 将 **Control protocol** 设置为 `Pixel stream`，将 **Control type** 设置为 `Ready frame with sync`。 | **ready** |
| **fsync** |
| 随机访问读 | 读数据 | 将 **Control protocol** 设置为 `Random access read`，将 **Control type** 设置为 `Ready`。 | **rd\_addr** |
| **rd\_len** |
| **rd\_avalid** |
| **rd\_dready** |
| 随机访问写 | 写数据 | 将 **Control protocol** 设置为 `Random access write`，将 **Control type** 设置为 `Valid`。 | **wr\_addr** |
| **wr\_len** |
| **wr\_valid** |
