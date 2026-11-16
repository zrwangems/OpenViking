---
type: simulink-block
title: 'CAN Receive'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / STM32F7'
documentation_page: 'canreceive'
documentation_source_path: 'nucleo/ref/canreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# CAN Receive

## 端口

### 输出

### **Id** — CAN 消息标识符标量

该端口输出 CAN 消息标识符。

#### 依赖关系

要启用此端口，请将 **Output type** 设置为 `Unpacked`。

**数据类型：** `uint32`

### **Length** — CAN 消息长度标量

该端口输出所接收 CAN 消息的长度，以 bytes 为单位。

#### 依赖关系

要启用此端口，请将 **Output type** 设置为 `Unpacked`。

**数据类型：** `uint8`

### **Data** — 消息数据 `vector` | `scalar`

该模块输出所接收 CAN 消息中的数据。数据的最大大小为 `uint8` 格式的 `[1x8]`。

长度中定义的 bytes 数表示输出的有效数据。

#### 依赖关系

要启用此端口，请将 **Output type** 设置为 `Unpacked`。

**数据类型：** `uint8`

### **Status** — 所接收消息的状态标量

该端口输出消息读取状态。

- 如果模块接收到新消息，则状态为 `1`。
- 如果模块未接收到新消息，则状态为 `0`。

#### 依赖关系

要启用此端口，请选择 **Output Status** 参数。

**数据类型：** `uint8`

### **Id Type** — CAN 消息标识符类型标量

该端口输出：

- `0` - 如果为 11-bit 标准标识符
- `1` - 如果为 29-bit 扩展标识符

#### 依赖关系

要启用此端口，请选择 **Output Id Type** 参数。

**数据类型：** `uint8`

### **Remote** — 输出远程消息标量

如果所接收的 CAN 消息是远程帧，则该端口输出 1。

#### 依赖关系

要启用此端口，请选择 **Output Remote** 参数。

### **Msg** — CAN Message 向量 | 标量

CAN Receive 模块以 Simulink 总线信号形式输出 CAN 接收消息。要从 Simulink 总线信号中提取数据，请将其连接到 CAN Unpack 模块。从总线接收的 CAN 消息将存储在 FIFO 中。

#### 依赖关系

要启用此端口，请将 **Output type** 设置为 `Packed`。

**数据类型：** `CAN Msg`

## 参数

### **Module** — 用于通信的模块 `1` (默认) | `Any integer value`

用于通信的 CAN 模块。

**注意**

- 模块上的 CAN 0 Module 表示硬件上的 CAN 1 外设。
- 模块上的 CAN 1 Module 表示硬件上的 CAN 2 外设。

### **Output Type** — 消息输出类型 `unpacked` (默认) | `packed`

CAN Receive 模块的输出类型为 `Packed` 或 `Unpacked`。

在 Unpacked 模式下，该模块输出解包 CAN 消息的不同字段。在 unpacked 模式下，CAN Receive 模块具有 `6 (Id, Id Type, status, Length, Remote, Data)` 个输出端口。

在 Packed 模式下，该模块输出 Simulink 总线信号。要从 Simulink 总线信号中提取数据，请将其连接到 CAN Unpack 模块。

### **Read source** — CAN 接收消息源 `FIFO 0` (默认) | `FIFO 1`

CAN Receive 模块从读取源输出 CAN 消息。您可以在硬件配置参数中设置读取源滤波器配置。

### **Sample Time** — 读取消息的时间间隔 -1 (默认) | 0.1 | 非负实数值

指定该模块接收消息的频率，以 seconds 为单位。当您将此参数指定为 `-1` 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。

### **Output Id Type** — 启用标识符类型 `off` (默认) | `on`

当您选择 **Output Id Type** 参数时，该模块会配置一个输出端口 **Id Type**。该端口输出标准或扩展消息状态。

#### 依赖关系

要启用此参数，请将 **Output type** 设置为 `unpacked`。

### **Output Remote** — 输出远程状态 `off` (默认) | `on`

当您选择 **Output Remote** 参数时，该模块会配置一个输出端口 **Remote**。该端口输出消息远程帧状态。

#### 依赖关系

要启用此参数，请将 **Output type** 设置为 `unpacked`。

### **Output Status** — 启用输出状态 `off` (默认) | `on`

当您选择 **Output Status** 参数时，该模块会配置一个输出端口 **Status**。该端口输出 CAN 消息的状态。

## 所属库

Simulink Coder Support Package for STMicroelectronics Nucleo Boards / STM32F7

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

从 CAN 网络接收消息

CAN Receive 模块从连接到硬件的 Controller Area Network (CAN) 网络接收消息。

在 Unpacked 模式下，该模块输出解包 CAN 消息的不同字段。

在 Packed 模式下，该模块输出 Simulink® 总线信号。要从 Simulink 总线信号中提取数据，请将其连接到 CAN Unpack 模块。

CAN Receive 模块从 CAN 接收消息，并将其传送到 Simulink 模型。它会根据模块参数在每个时间步输出一条消息。CAN Receive 模块将从总线接收的 CAN 消息存储在先入先出 (FIFO) 中。FIFO 在每个时间步按排队顺序将消息传送到您的模型。

在 Configuration Parameters 中配置 FIFO 以及 CAN 模块的其他属性。

**注意**

- **CAN Receive** 模块目前仅支持 STM32 Nucleo F767ZI 处理器。
- STM32 Nucleo F767ZI 处理器不支持 CAN 3 外设。请仅使用 CAN 1 或 CAN 2 外设。
