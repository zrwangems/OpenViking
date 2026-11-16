---
type: simulink-block
title: 'MCAN Transmit'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC4x / Peripheral Management / AURIX TC4x'
documentation_page: 'mcantransmit'
documentation_source_path: 'infineonaurix/ref/mcantransmit.html'
language: zh-CN
chinese_source: worker-translation
---

# MCAN Transmit

## Ports

### Input

### **Data** — 输入数据端口向量 | 标量

在此端口以原始数据格式指定消息。

#### 依赖关系

要启用此端口，请将 **Data format** 参数设置为 `Raw data`，并禁用 **Remote transmit** 参数。

**数据类型：** `uint8`

### **Remote Request** — 远程传输请求标量

在此端口将远程传输请求指定为：

- `1 —` 激活远程传输请求
- `0 —` 停用远程传输请求

#### 依赖关系

要启用此端口，请将 **Data format** 参数设置为 `Raw data`，将 **Frame format** 参数设置为 `Classic CAN`，并启用 **Remote transmit parameter**。

**数据类型：** `Boolean`

### **ID** — CAN 消息标识符标量

在此端口将 CAN 消息标识符指定为下列值之一：

- `0-0x7ff —` 用于标准（11 位）标识符
- `0-0x1fffffff —` 用于扩展（29 位）标识符

#### 依赖关系

要启用此参数，请将 **Data format** 参数设置为 `Raw data`，并选择 **Enable input port for identifier** 参数。

**数据类型：** `uint32`

### **ID Type** — CAN 消息标识符类型标量

在此端口将 CAN 消息标识符类型指定为下列值之一：

- `0 —` 如果标识符是 11 位标准标识符
- `1` 或任何非 `0` 的值 — 如果标识符是 29 位标准标识符

#### 依赖关系

要启用此参数，请将 **Data format** 参数设置为 `Raw data`，并选择 **Enable input port for identifier type** 参数。

**数据类型：** `uint8`

### **Length** — CAN 消息长度标量

在此端口指定所传输 CAN 消息的长度（以字节为单位）。

**注意**

**Length** 值决定要通过 CAN 总线传输的数据大小。如果 **Length** 端口的值大于 **Data** 端口值的大小，则 Simulink 优先使用 **Data** 值而非 **Length** 值。

#### 依赖关系

要启用此参数，请将 **Data format** 参数设置为 `Raw data`，并选择 **Enable input port for data length** 参数。

**数据类型：** `uint8`

### **Msg** — 输入 CAN 消息向量 | 标量

以 CAN 消息格式指定消息。

您可以根据 **Frame format** 参数中的值，创建自己的消息，或从 CAN Pack 或 CAN FD Pack 模块上传 CAN 数据库文件。

**注意**

要使用 CAN Pack 模块创建 CAN 消息，请在 CAN Pack 模块中启用 **Output as bus** 参数。

#### 依赖关系

要启用此端口，请将 **Data format** 参数设置为 `CAN message`。

**数据类型：** `CAN message`

### **Buffer Number** — 缓冲传输模式下的缓冲区数量标量

指定用于 CAN 传输的缓冲区数量。

#### 依赖关系

要启用此端口，请将 **Data format** 参数设置为 `CAN message`，将 **Mode** 参数设置为 `Buffer`，并选择 **Enable input port for buffer number** 参数。

**数据类型：** `uint8`

### Output

### **Status** — 数据传输状态标量

在此端口将数据传输状态指定为下列值之一：

- `0` — CAN 数据传输无错误
- `1` — 由于超时导致 CAN 数据传输错误
- `2` — 由于无效的缓冲区配置导致 CAN 数据传输错误

#### 依赖关系

要启用此端口，请选择 **Enable status port** 参数。

**数据类型：** `uint8`

### **FIFO Level** — FIFO 寄存器填充级别标量

用于显示 FIFO 寄存器级别的输出端口。

#### 依赖关系

要启用此参数，请将 **Mode** 参数设置为 `FIFO or Queue`，并选择 **Output FIFO transmit free level** 参数。

## Parameters

### **Data format** — 数据输出类型 `Raw data` (默认) | `CAN message`

将所传输消息的数据类型设置为下列值之一：

- `Raw data` — 将消息作为 1-by-*N* `uint8` 数组传输。
- `CAN message` — 以 CAN 消息格式传输消息。根据 **Frame format** 参数的值，使用 CAN Pack 或 CAN FD Pack 模块以及 MCAN Transmit 模块打包 CAN 消息。

**注意**

要使用 CAN Pack 模块创建 CAN 消息，请在 CAN Pack 模块中启用 **Output as bus** 参数。

### **Frame format** — 帧格式类型 `CAN-FD` (默认) | `Classic CAN`

选择所传输消息的帧格式。

### **Remote transmit** — 启用远程消息传输的选项 `off` (默认) | `on`

选择此参数以在 CAN 消息中传输远程帧。

#### 依赖关系

要启用此参数，请将 **Data format** 参数设置为 `Raw data`，并将 **Frame format** 参数设置为 `Classic CAN`。

#### CAN FD

### **Enable bit rate switching** — 启用标称位速率与数据位速率之间切换的选项 `off` (默认) | `on`

选择此参数以启用标称位速率与数据位速率之间的切换。

#### 依赖关系

要启用此参数，请将 **Data Format** 参数设置为 `Raw data`，并将 **Frame format** 设置为 `CAN-FD`。

#### 标识符类型

### **Enable input port for identifier type** — 启用标识符类型输入端口的选项 `off` (默认) | on

选择此参数以启用用于指定标识符类型的输入端口。

#### 依赖关系

要启用此参数，请将 **Data format** 参数设置为 `Raw data`。

### **Identifier type** — 消息标识符类型 `Standard (11-bit identifier)` (默认) | `Extended (29-bit identifier)`

指定消息标识符的类型。

#### 依赖关系

要启用此参数，请将 **Data Format** 参数设置为 `Raw data`，并禁用 **Enable input port for identifier type** 参数。

#### 标识符

### **Enable input port for identifier** — 启用标识符输入端口的选项 `on` (默认) | off

选择以启用标识符输入端口。

#### 依赖关系

要启用此参数，请将 **Data format** 参数设置为 `Raw data`。

### **Identifier** — 消息标识符 `100` (默认) | 标准帧的标量，范围为 (0,0x7ff) | 扩展帧的标量，范围为 (0,0x1fffffff)

为标准帧大小指定 11 位标识符，或为扩展帧大小指定 29 位标识符。可以将标识符指定为十进制、二进制或十六进制值。对于二进制和十六进制格式，请分别使用 `bin2dec` 和 `hex2dec` 转换该值。该模块将标识符编码到消息中，并将其发送到 CAN 总线。

#### 依赖关系

要启用此参数，请将 **Data format** 参数设置为 `Raw data`，并禁用 **Enable input port for identifier type** 参数。

#### 数据长度

### **Enable input port for data length** — 启用数据长度输入端口的选项 `on` (默认) | off

选择此参数以启用用于指定数据长度的输入端口。

#### 依赖关系

要启用此参数，请将 **Data format** 设置为 `Raw data`。

### **Data length** — 长度（bytes） `8` (默认) | 范围 (0,8) 内的标量 | `12` | `16` | `20` | `24` | `32` | `48` | `64`

指定以 bytes 为单位的数据长度。

#### 依赖关系

要启用此参数，请将 **Data format** 设置为 `Raw data`，并禁用 **Enable input port for data length** 参数。

#### 节点

### **Number of nodes** — CAN 节点数量 `1` (默认) | 范围 (0 到 20) 内的标量

指定用于数据传输的 CAN 节点数量。

**注意**

**Number of nodes** 参数的选择决定必须在 Hardware Mapping 工具中配置多少个节点（请参见 MCAN Transmit Peripheral Configuration）。

### **Mode** — 消息传输模式 `FIFO or Queue` (默认) | `Buffer`

选择 CAN 数据传输的模式。

#### Buffer

### **Enable input port for buffer number** — 启用缓冲区编号输入端口的选项 `off` (默认) | on

选择此参数以启用模块中的 **Buffer Number** 输入端口。

#### 依赖关系

要启用此参数，请将 **Mode** 参数设置为 `Buffer`。

### **Buffer number (0 - 31)** — 用于数据传输的缓冲区数量 `0` (默认) | 范围 (0,31) 内的标量

指定用于传输 CAN 数据的缓冲区数量。

#### 依赖关系

要启用此参数，请将 **Mode** 参数设置为 `Buffer`，并禁用 **Enable input port for buffer number** 参数。

#### 超时

### **Timeout(s) in seconds** — 完成写操作的等待时间 `0` (默认) | 范围 (0,2147480) 内的标量

指定传输 CAN 数据的最大等待时间（以 seconds 为单位）。

### **Output FIFO transmit free level** — 启用输出 FIFO 传输空闲级别的选项 `off` (默认) | `on`

选择此参数以启用 **FIFO level** 端口，该端口输出已传输 FIFO 消息级别。

#### 依赖关系

要启用此参数，请将 **Mode** 参数设置为 `FIFO or Queue`。

### **Enable status port** — 启用输出状态端口的选项 `off` (默认) | `on`

选择此参数以启用 **Status** 端口，该端口输出数据传输状态。

## 所属库

Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / AURIX TC4x

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2024b 中引入**

## 描述

将数据写入 CAN 总线

MCAN Receive 模块是一种 Modular CAN (MCAN)，用于将数据写入控制器局域网 (CAN) 总线。

当将数据格式设置为 `Raw data` 时，该模块接受 `uint8` 类型的一维数组。如果将数据格式设置为 `CAN Message`，则该模块接受来自 CAN Pack 或 CAN FD Pack 模块的 Simulink® 总线信号，具体取决于帧格式。
