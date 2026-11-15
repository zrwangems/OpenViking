---
type: simulink-block
title: 'MCAN Receive'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC3x / Peripheral Management / AURIX TC3x'
documentation_page: 'mcanreceive'
documentation_source_path: 'infineonaurixtc3x/ref/mcanreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# MCAN Receive

## 端口

### 输入

### **Buffer Number** — 用于 CAN 通信的缓冲区编号 标量

指定缓冲区编号。

#### 依赖关系

要启用此端口，请将 **Read source** 参数设置为 `Buffers`，并选择 **Enable input port for buffer number** 参数。

**数据类型：** `uint8`
### 输出

### **Msg** — CAN Message 向量 | 标量

该模块输出它从 Simulink 总线信号接收到的 CAN 消息（数据和标头）。

#### 依赖关系

要启用此端口，请将 **Output type** 设置为 `Packed`。

**数据类型：** `CAN Message`

### **Data** — 消息数据 向量 | 标量

该模块根据 **Read Source** 参数的值，输出它从 FIFO 0 register、FIFO 1 register 或 buffer 读取的数据。对于 `Classic CAN` 帧格式，数据最大大小为 `8` bytes；对于 `CAN-FD` 帧格式，数据最大大小为 `64` bytes。

#### 依赖关系

要启用此端口，请将 **Output type** 参数设置为 `Unpacked`。

**数据类型：** `uint8`

### **Id** — CAN 消息标识符值 标量

此端口从接收到的 CAN 消息输出标准或扩展 ID 值。

#### 依赖关系

要启用此端口，请将 **Output type** 设置为 `Unpacked`。

**数据类型：** `uint32`

### **Length** — CAN 消息长度 标量

此端口输出接收到的 CAN 消息的数据长度，以 bytes 为单位。

#### 依赖关系

要启用此端口，请将 **Output type** 设置为 `Unpacked`。

**数据类型：** `uint8`

### **Id Type** — CAN 消息标识符类型 标量

此端口输出标识符类型，如下：

- `0` — 如果 ID 是 11-bit standard identifier
- `1` — 如果 ID 是 29-bit extended identifier

#### 依赖关系

要启用此端口，请将 **Output type** 参数设置为 `Unpacked`，并启用 **Output identifier type** 参数。

**数据类型：** `Boolean`

### **Frame Type** — CAN 消息帧类型 标量

此端口输出 CAN 帧数据格式，如下：

- `0` — 如果格式为 Classic CAN
- `1` — 如果格式为 CAN-FD

#### 依赖关系

要启用此端口，请将 **Output type** 参数设置为 `Unpacked`，并启用 **Output frame type**。

**数据类型：** `uint32`

### **Bitrate switching** — Bit rate switching 状态 标量

此端口输出状态，为以下值之一：

- `0` — 当模块接收到不带位速率切换的 CAN FD 帧时
- `1` — 当模块接收到带位速率切换的帧时

#### 依赖关系

要启用此端口，请将 **Frame format** 参数设置为 `CAN-FD`，将 **Output type** 参数设置为 `Unpacked`，并选择 **Output bit rate switching** 参数。

**数据类型：** `uint8`

### **Remote** — 远程帧状态 标量

此端口输出远程接收状态，如下：

- `1` — 如果接收到的 CAN 消息是远程帧
- `0` — 如果接收到的 CAN 消息是数据帧

#### 依赖关系

要启用此端口，请将 **Frame format** 设置为 `Classic CAN`，将 **Output type** 参数设置为 `Unpacked`，并启用 **Output remote** 参数。

**数据类型：** `Boolean`

### **FIFO Level** — FIFO 填充级别 标量

此端口输出接收 FIFO 填充级别。

FIFO 级别指示模块读取消息后 FIFO 0 或 FIFO 1 寄存器的接收级别。Rx FIFO 指示 Rx FIFO 中有多少为空。

#### 依赖关系

要启用此端口，请将 **Read source** 参数设置为 `FIFO 0` 或 `FIFO 1`，并启用 **Output receive FIFO level** 参数。

**数据类型：** `uint8`

### **Status** — 接收消息的状态 标量

此端口输出消息读取状态，如下：

- `1` — 如果读取的 CAN 消息无效
- `0` — 如果读取的 CAN 消息有效

#### 依赖关系

要启用此端口，请选择 **Output Status** 参数。

**数据类型：** `uint8`

## 参数

### **Frame format** — 帧格式类型 `CAN-FD` (default) | `Classic CAN`

选择要接收消息的帧类型。

### **Read source** — 接收到的 CAN 消息的来源 `FIFO 0` (default) | `FIFO 1` | `Buffers`

将读取来源指定为 FIFO 或缓冲区。

**注意**

该模块根据您设置的过滤器配置从 FIFO 0、FIFO 1 或缓冲区读取消息（请参阅 MCAN Receive Peripheral Configuration）。

### **Buffer number** — 用于 CAN 数据接收的缓冲区编号 `0` (default) | 范围 (0-63) 内的标量

指定 MCAN Receive 模块用于读取接收到的 CAN 消息的缓冲区编号。

#### 依赖关系

要启用此参数，请将 **Read source** 设置为 `Buffers`，并禁用 **Enable input port for buffer number** 参数。

### **Enable input port for buffer number** — 用于启用缓冲区编号输入端口的选项 `off` (default) | `on`

选择此参数以启用用于指定缓冲区编号的输入端口。

#### 依赖关系

要启用此参数，请将 **Read source** 设置为 `Buffers`，并选择 **Enable input port for buffer number** 参数。

### **Output Type** — 消息输出类型 `Packed` (default) | `Unpacked`

将模块的消息输出类型指定为 `Packed` 或 `Unpacked`。

对于 unpacked 消息，模块输出 unpacked CAN 消息的不同字段。

对于 packed 消息，模块输出 Simulink 总线信号。要从 Simulink 总线信号中提取数据，如果帧格式是 Classic CAN，请使用 CAN Unpack 模块；如果帧格式是 CAN-FD，请使用 CAN FD Unpack 模块。

### **Output identifier type** — 用于启用输出标识符类型的选项 `off` (default) | `on`

选择此参数以启用 **Id Type** 端口，该端口输出标准或扩展消息状态。

#### 依赖关系

要启用此参数，请将 **Output type** 参数设置为 `Unpacked`。

### **Output frame type** — 用于启用输出帧类型的选项 `off` (default) | `on`

选择此参数以启用 **Frame Type** 端口，该端口输出消息帧类型。

#### 依赖关系

要启用此参数，请将 **Output type** 参数设置为 `Unpacked`。

### **Output bitrate switching** — 用于启用输出 bitrate switching 的选项 `off` (default) | `on`

选择此参数以启用 **Bitrate Switching** 端口，该端口输出位速率切换的状态。

#### 依赖关系

要启用此参数，请将 **Frame format** 参数设置为 `CAN-FD`，并将 **Output type** 参数设置为 `Unpacked`。

### **Output remote** — 用于启用输出帧类型的选项 `off` (default) | `on`

选择此参数以启用 **Remote** 端口，该端口输出消息远程帧状态。

#### 依赖关系

要启用此参数，请将 **Frame format** 参数设置为 `Classic CAN`，并将 **Output type** 参数设置为 `Unpacked`。

### **Output receive FIFO level** — 启用接收 FIFO 填充级别 `off` (default) | `on`

选择此参数以启用 **FIFO level** 端口，该端口输出接收到的 FIFO 消息级别。

#### 依赖关系

要启用此参数，请将 **Read source** 参数设置为 `FIFO 0` 或 `FIFO 1`。

### **Output status** — 用于启用输出状态的选项 `off` (default) | `on`

选择此参数以启用 **Status** 端口，该端口输出读取状态。

### **Sample Time** — 读取消息的时间间隔 -1 (default) | 非负实数

指定模块接收消息的频率，以 seconds 为单位。当您将此参数指定为 `-1` 时，Simulink 会根据模块在模型中的上下文确定该模块的最佳采样时间。

## 所属库

Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / AURIX TC3x

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2025a 中引入**

## 描述

从 CAN 总线读取数据

MCAN Receive 模块是一种 Modular CAN (MCAN)，用于从控制器局域网 (CAN) 总线读取数据。

对于 unpacked 消息，对于 CAN-FD 帧格式，模块将接收到的值输出为 64-by-1 数组；对于 Classic CAN 帧格式，输出为 8-by-1 数组。

对于 packed 消息，模块输出 Simulink® 总线信号。要从 Simulink 总线信号中提取数据，如果帧格式是 Classic CAN，请使用 CAN Unpack 模块；如果帧格式是 CAN-FD，请使用 CAN FD Unpack 模块。
