---
type: simulink-block
title: 'C28x CAN Transmit'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Communication Peripherals / C28x'
documentation_page: 'c28xcantransmit'
documentation_source_path: 'ref/c28xcantransmit.html'
language: zh-CN
chinese_source: official
---

# C28x CAN Transmit

## 端口

### 输入

### **Msg** — 消息数据 标量

输入消息数据。

**数据类型:** `uint8` | `uint16` | `uint32` | `CAN_MESSAGE_TYPE`

## 参数

### **模块** — 模块配置的 CAN 模块 **CAN\_A** (默认) | **CAN\_B**

确定此 CAN Transmit 模块实例配置的 CAN 模块。

### **邮箱编号(0–31)** — 设置邮箱号码寄存器 (MBNR) 的值 `1` (默认) | [0 31] 范围内的整数

标准 CAN 模式的唯一编号为 0 到 15，增强型 CAN 模式的唯一编号为 0 到 31。该数字指的是 RAM 中的一个邮箱区域。在标准模式下，邮箱号码决定优先级。

**注意**

在一个模型中，多个 CAN Transmit 模块可以具有相同的 `Mailbox number`。但是同一个邮箱号码不能被 CAN Receive 模块使用。

### **消息标识符** — 消息标识符寄存器 (MID) 的值 bin2dec('111000111') (默认) | 长度为 11 位或 29 位的数字标识符

对于标准帧大小，消息标识符长度为 11 位；对于扩展帧大小，消息标识符长度为 29 位，以十进制、二进制或十六进制表示。对于二进制和十六进制格式，分别使用 `bin2dec(' ')` 和 `hex2dec(' ')` 来转换条目。消息标识符被编码到发送到 CAN 总线的消息中。

**注意**

当与 C28x CAN Transmit 模块一起使用创建 CAN 消息时，CAN 消息使用 CAN Pack 模块中的消息标识符参数的值进行传输。

### **消息类型** — 消息标识符类型 **标准(11 位标识符)** (默认) | **扩展(29 位标识符)**

消息标识符类型。

### **启用阻塞模式** — 设置阻塞模式 `off` (默认) | `on`

如果选中，CAN 模块将无限期地等待发送 (XMT) 确认。如果未选中，CAN 模块不会等待发送 (XMT) 确认，这在硬件无法确认传输时非常有用。

### **消息传输时发出中断** — 消息传输时会发出异步中断 `off` (默认) | `on`

选中此模块后，数据传输时会发出异步中断。

### **中断线** — 异步中断的中断线 **0** (默认) | **1**

异步中断使用的中断线。此参数的值会设置全局中断掩码寄存器 (CANGIM) 中的第 2 位 (GIL)：

- **1** 将全局中断映射到 CAN1INT 线。
- **0** 将全局中断映射到 CAN0INT 线。

**注意**

有关设置 CAN 模块定时参数的信息，请参阅 Configuring Timing Parameters for CAN Blocks。

#### 依赖关系

仅当选择**消息传输时会发出中断**时才会显示此参数。

## 所属库

C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C281x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28p65x

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

R2025b 官方文档未提供。

## 描述

增强型控制器局域网传输邮箱

CAN Transmit 模块生成源代码，用于通过 CAN 邮箱传输增强型控制器局域网 (CAN) 消息。处理器上的 CAN 模块提供串行通信功能，并有 32 个可配置为接收或发送的邮箱。该模块支持标准格式或扩展格式的 CAN 数据帧。

**注意**

此模块不支持定点输入。

该模块支持 CAN 或 DCAN，具体取决于 C2000 处理器的类型。

通过导航至 **硬件实现** > **Target hardware resources**，为特定硬件板配置 CAN 模块。请确认这些设置符合您的应用程序要求。
