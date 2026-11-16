---
type: simulink-block
title: 'MCAN Receive'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'F280015x'
documentation_page: 'mcanreceive'
documentation_source_path: 'ref/mcanreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# MCAN Receive

## 端口

### 输出

### **Msg** — CAN 消息 向量 | 标量

MCAN Receive 模块输出接收到的 CAN 消息（数据和标头）作为 Simulink 总线信号。从总线接收到的 CAN 消息将存储在 FIFO 或缓冲区中。

#### 依赖项

要启用此端口，请将 **Output type** 设置为 `Packed`。

**数据类型：** `CAN Msg`

### **Data** — 消息数据 向量 | 标量

该模块输出接收到的 CAN 消息中的数据。数据的最大大小为 `64`，格式为 `uint8`。

#### 依赖项

要启用此端口，请将 **Output type** 设置为 `Unpacked`。

**数据类型：** `uint8`

### **Status** — 接收消息的状态 标量

该端口输出消息读取状态。如果读取到新消息，该模块输出状态 `0`；如果未读取到，则输出 `1`。

#### 依赖项

要启用此端口，请选择 **Output Status** 参数。

**数据类型：** `uint8`

### **CAN identifier(ID)** — CAN 消息标识符 标量

该端口从接收到的 CAN 消息中输出标准或扩展标识符。

#### 依赖项

要启用此端口，请将 **Output type** 设置为 `Unpacked`。

**数据类型：** `uint32`

### **Length(LEN)** — CAN 消息长度 标量

该端口以 bytes 为单位输出接收到的 CAN 消息的长度。

#### 依赖项

要启用此端口，请将 **Output type** 设置为 `Unpacked`。

**数据类型：** `uint8`

### **Remote transmission request(RTR)** — 远程帧状态 标量

该端口将远程传输状态输出为以下值之一。

- `1` - 如果接收到的 CAN 消息是远程帧
- `0` - 如果接收到的 CAN 消息是数据帧

#### 依赖项

要启用此端口，请将 **Output type** 设置为 `Unpacked`。

**数据类型：** `uint8`

### **Bit rate switch(BRS)** — 位速率切换状态 标量

该端口输出：

- `0` - 当 CAN FD 帧在未进行位速率切换的情况下传输时
- `1` - 当 CAN FD 帧在进行位速率切换的情况下传输时

#### 依赖项

要启用此端口，请将 **Output type** 设置为 `Unpacked`。

**数据类型：** `uint8`

### **Extended identifier(XTD)** — 扩展或标准标识符 标量

该端口输出：

- `0` - 如果是 11 位标准标识符
- `1` - 如果是 29 位扩展标识符

#### 依赖项

要启用此端口，请将 **Output type** 设置为 `Unpacked`。

**数据类型：** `uint8`

### **Frame data format(FDF)** — CAN 帧数据格式 标量

该端口输出 CAN 帧数据格式，如下：

- `0` - 经典 CAN
- `1` - CAN-FD

#### 依赖项

要启用此端口，请将 **Output type** 设置为 `Unpacked`。

**数据类型：** `uint8`

## 参数

### **MCAN module** — CAN 模块 `A`（默认） | `B`

选择要从中读取数据的 MCAN 模块。

### **Read source** — CAN 接收消息源 `Buffers`（默认） | `FIFO 0` | `FIFO 1`

从总线接收到的 CAN 消息将存储在 FIFO 或缓冲区中。

MCAN Receive 模块根据你在硬件配置参数中设置的滤波器配置，将消息存储在 FIFO0、FIFO1 或缓冲区中。

### **Buffer number (0-63)** — 缓冲区编号 `0`（默认） | `1` | `2``...`

指定希望 MCAN Receive 模块存储接收到的 CAN 消息的缓冲区编号。

#### 依赖项

要启用此参数，请将 **Read source** 设置为 `Buffers`。

### **Output Type** — 消息输出类型 `Packed`（默认） | `Unpacked`

MCAN Receive 模块的输出类型为 `Packed` 或 `Unpacked`。

在 Unpacked 模式下，该模块输出解包 CAN 消息的不同字段。在 unpacked 模式下，MCAN Receive 模块具有 `7 (ID, XTD, FDF, BRS, LEN, RTR, Data)` 个输出端口。

在 Packed 模式下，该模块输出 Simulink 总线信号。要从 Simulink 总线信号中提取数据，请将其连接到 CAN-FD Unpack 模块。

### **Output Status** — 启用输出状态 `off`（默认） | `on`

选择 **Output Status** 参数时，该模块配置 **Status** 输出端口。该端口输出读取状态。

### **Sample Time** — 读取消息的时间间隔 0.1（默认） | -1 | 非负实数值

指定模块接收消息的频率，以 seconds 为单位。将此参数指定为 `-1` 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

C2000 Microcontroller Blockset / F2838x / M4 C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28p55x C2000 Microcontroller Blockset / F28p65x

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2021a 中引入**

## 描述

从 CAN 总线读取数据

MCAN Receive 模块从连接到硬件的控制器局域网（CAN）读取消息。

在 Unpacked 模式下，该模块输出解包 CAN 消息的不同字段。

在 Packed 模式下，该模块输出 Simulink® 总线信号。要从 Simulink 总线信号中提取数据，请将其连接到 CAN-FD Unpack 模块。

MCAN Receive 模块从 CAN 接收消息并将其传递到 Simulink 模型。它根据模块参数在每个时间步输出一条消息或所有消息。MCAN Receive 模块将从总线接收到的 CAN 消息存储在先入先出（FIFO）或缓冲区中。FIFO 或缓冲区在每个时间步按排队顺序将消息传递到你的模型。

**注意**

- 对于 MCAN Receive 模块，如果数据不可用，输出状态显示之前接收到的数据。
- 当 **Output type** 为 packed 且 MCAN Receive 模块连接到 CAN FD Unpack 模块时，接收消息的 `error`、`error state indicator (ESI)`、`reserved` 和 `timestamp` 字段的值设置为 `0`，并且这些值会反映在 CAN FD Unpack 模块的输出上。

在接收输出状态中，我们应说明当数据不可用时当前的行为。当数据不可用时，输出数据将保持为其之前接收到的值。

FIFO 中可存储的元素数量在配置参数中配置。对于缓冲区，除非读取旧数据，否则不会存储新数据。

FIFO、阻塞或覆写模式设置在 MCAN 中配置。

使用模块参数对话框指定 **Output type** 及其属性。在 Configuration Parameters 中配置 CAN 模块的其他属性。更多信息请参阅 Model Configuration Parameters for Texas Instruments C2000 Processors。
