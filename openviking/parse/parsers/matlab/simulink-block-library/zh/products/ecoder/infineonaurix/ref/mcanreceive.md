---
type: simulink-block
title: 'MCAN Receive'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC4x / Peripheral Management / AURIX TC4x'
documentation_page: 'mcanreceive'
documentation_source_path: 'infineonaurix/ref/mcanreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# MCAN Receive

## 端口

### 输入

### **Buffer Number** — 用于 CAN 通信的缓冲区编号标量

指定缓冲区编号。

#### 依赖关系

要启用此端口，请将 **读取源** 参数设置为 `Buffers`，并选择 **启用缓冲区编号输入端口** 参数。

**数据类型：** `uint8`

### 输出

### **Msg** — CAN 消息向量 | 标量

该模块输出它从 Simulink 总线信号接收到的 CAN 消息（数据和报头）。

#### 依赖关系

要启用此端口，请将 **输出类型** 参数设置为 `Packed`。

**数据类型：** `CAN Message`

### **Data** — 消息数据向量 | 标量

该模块基于 **读取源** 参数的值，输出它从 FIFO 0 寄存器、FIFO 1 寄存器或缓冲区读取的数据。对于 `Classic CAN` 帧格式，数据的最大大小为 `8` bytes；对于 `CAN-FD` 帧格式，数据的最大大小为 `64` bytes。

#### 依赖关系

要启用此端口，请将 **输出类型** 参数设置为 `Unpacked`。

**数据类型：** `uint8`

### **Id** — CAN 消息标识符值标量

此端口输出接收到的 CAN 消息中的标准或扩展 ID 值。

#### 依赖关系

要启用此端口，请将 **输出类型** 设置为 `Unpacked`。

**数据类型：** `uint32`

### **Length** — CAN 消息长度标量

此端口输出接收到的 CAN 消息的数据长度，单位为 bytes。

#### 依赖关系

要启用此端口，请将 **输出类型** 设置为 `Unpacked`。

**数据类型：** `uint8`

### **Id Type** — CAN 消息标识符类型标量

此端口输出标识符类型，如下所示：

- `0` — 如果 ID 是 11 位标准标识符
- `1` — 如果 ID 是 29 位扩展标识符

#### 依赖关系

要启用此端口，请将 **输出类型** 参数设置为 `Unpacked`，并启用 **输出标识符类型** 参数。

**数据类型：** `Boolean`

### **Frame Type** — CAN 消息帧类型标量

此端口输出 CAN 帧数据格式，如下所示：

- `0` — 如果格式为 Classic CAN
- `1` — 如果格式为 CAN-FD

#### 依赖关系

要启用此端口，请将 **输出类型** 参数设置为 `Unpacked`，并启用 **输出帧类型**。

**数据类型：** `uint32`

### **Bitrate switching** — 位速率切换状态标量

此端口输出以下值之一作为状态：

- `0` — 当模块接收不带位速率切换的 CAN FD 帧时
- `1` — 当模块接收带位速率切换的帧时

#### 依赖关系

要启用此端口，请将 **帧格式** 参数设置为 `CAN-FD`，将 **输出类型** 参数设置为 `Unpacked`，并选择 **输出位速率切换** 参数。

**数据类型：** `uint8`

### **Remote** — 远程帧状态标量

此端口输出远程接收状态，如下所示：

- `1` — 如果接收到的 CAN 消息是远程帧
- `0` — 如果接收到的 CAN 消息是数据帧

#### 依赖关系

要启用此端口，请将 **帧格式** 设置为 `Classic CAN`，将 **输出类型** 参数设置为 `Unpacked`，并启用 **输出远程** 参数。

**数据类型：** `Boolean`

### **FIFO Level** — FIFO 填充级别标量

此端口输出接收的 FIFO 填充级别。

FIFO 级别指示模块读取消息后 FIFO 0 或 FIFO 1 寄存器的接收级别。Rx FIFO 指示 Rx FIFO 有多少为空。

#### 依赖关系

要启用此端口，请将 **读取源** 参数设置为 `FIFO 0` 或 `FIFO 1`，并启用 **输出接收 FIFO 级别** 参数。

**数据类型：** `uint8`

### **Status** — 接收消息的状态标量

此端口输出消息读取状态，如下所示：

- `1` — 如果读取的 CAN 消息无效
- `0` — 如果读取的 CAN 消息有效

#### 依赖关系

要启用此端口，请选择 **输出状态** 参数。

**数据类型：** `uint8`

## 参数

### **帧格式** — 帧格式类型 `CAN-FD`（默认）| `Classic CAN`

选择用于接收消息的帧类型。

### **读取源** — 接收的 CAN 消息源 `FIFO 0`（默认）| `FIFO 1` | `Buffers`

将读取源指定为 FIFO 或缓冲区。

**注意**

该模块根据你设置的滤波器配置从 FIFO 0、FIFO 1 或缓冲区读取消息（参见 MCAN Receive Peripheral Configuration）。

### **缓冲区编号** — 用于 CAN 数据接收的缓冲区编号 `0`（默认）| 范围 (0—63) 内的标量

指定该模块用于读取接收到的 CAN 消息的缓冲区编号。

#### 依赖关系

要启用此参数，请将 **读取源** 设置为 `Buffers`，并禁用 **启用缓冲区编号输入端口** 参数。

### **启用缓冲区编号输入端口** — 启用缓冲区编号输入端口的选项 `off`（默认）| `on`

选择此参数以启用用于指定缓冲区编号的输入端口。

#### 依赖关系

要启用此参数，请将 **读取源** 设置为 `Buffers`，并选择 **启用缓冲区编号输入端口** 参数。

### **输出类型** — 消息输出类型 `Packed`（默认）| `Unpacked`

将模块的消息输出类型指定为 `Packed` 或 `Unpacked`。

对于未打包消息，该模块输出未打包 CAN 消息的不同字段。

对于打包消息，该模块输出 Simulink 总线信号。要从 Simulink 总线信号中提取数据，如果帧格式为 Classic CAN，则使用 CAN Unpack 模块；如果帧格式为 CAN-FD，则使用 CAN FD Unpack 模块。

### **输出标识符类型** — 启用输出标识符类型的选项 `off`（默认）| `on`

选择此参数以启用 **Id Type** 端口，该端口输出标准或扩展消息状态。

#### 依赖关系

要启用此参数，请将 **输出类型** 参数设置为 `Unpacked`。

### **输出帧类型** — 启用输出帧类型的选项 `off`（默认）| `on`

选择此参数以启用 **Frame Type** 端口，该端口输出消息帧类型。

#### 依赖关系

要启用此参数，请将 **输出类型** 参数设置为 `Unpacked`。

### **输出位速率切换** — 启用输出位速率切换的选项 `off`（默认）| `on`

选择此参数以启用 **Bitrate Switching** 端口，该端口输出位速率切换的状态。

#### 依赖关系

要启用此参数，请将 **帧格式** 参数设置为 `CAN-FD`，并将 **输出类型** 参数设置为 `Unpacked`。

### **输出远程** — 启用输出帧类型的选项 `off`（默认）| `on`

选择此参数以启用 **Remote** 端口，该端口输出消息远程帧状态。

#### 依赖关系

要启用此参数，请将 **帧格式** 参数设置为 `Classic CAN`，并将 **输出类型** 参数设置为 `Unpacked`。

### **输出接收 FIFO 级别** — 启用接收 FIFO 填充级别 `off`（默认）| `on`

选择此参数以启用 **FIFO level** 端口，该端口输出接收的 FIFO 消息级别。

#### 依赖关系

要启用此参数，请将 **读取源** 参数设置为 `FIFO 0` 或 `FIFO 1`。

### **输出状态** — 启用输出状态的选项 `off`（默认）| `on`

选择此参数以启用 **Status** 端口，该端口输出读取状态。

### **采样时间** — 读取消息的时间间隔 -1（默认）| 非负实数值

指定模块接收消息的频率，以 seconds 为单位。将此参数指定为 `-1` 时，Simulink 会根据模块在模型中的上下文确定该模块的最佳采样时间。

## 所属库

Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / AURIX TC4x

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024b 中引入**

## 描述

从 CAN 总线读取数据

MCAN Receive 模块是一个模块化 CAN (MCAN)，它从控制器局域网 (CAN) 总线读取数据。

对于未打包消息，该模块在 CAN-FD 帧格式下将接收到的值输出为 64-by-1 数组，在 Classic CAN 帧格式下输出为 8-by-1 数组。

对于打包消息，该模块输出 Simulink® 总线信号。要从 Simulink 总线信号中提取数据，如果帧格式为 Classic CAN，则使用 CAN Unpack 模块；如果帧格式为 CAN-FD，则使用 CAN FD Unpack 模块。
