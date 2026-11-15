---
type: simulink-block
title: 'On-board CAN Transmit'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / CAN'
documentation_page: 'onboardcantransmit'
documentation_source_path: 'supportpkg/arduino_ref/onboardcantransmit.html'
language: zh-CN
chinese_source: worker-translation
---

# On-board CAN Transmit

## 端口

### 输入

### **Message** — 发送的 CAN 消息的消息向量

该模块接受原始或 CAN 消息格式的 CAN 消息。

- Raw data — 要将消息作为 `uint8` 向量数组接受，请将 Data is input as 设置为 `Raw data`。
- CAN 消息 — 要以 CAN 消息格式接受消息，请将 Data is input as 设置为 `CAN Msg`。

**数据类型：** `uint8` | `CAN Msg`
### 输出

### **Status** — 输出 CAN 消息的状态标量

该模块输出 CAN 消息发送状态。

Arduino Due 开发板使用这些发送状态。

- `1` — CAN 控制器成功将数据传输到 CAN 网络。
- `0` — CAN 控制器无法成功将数据传输到 CAN 网络，或者发送 CAN 邮箱已满。

Arduino Teensy 开发板使用这些发送状态。

- `-2` — 由于 CAN 控制器故障或发送错误累积，发送错误计数器 (TEC) 中的值 >= 96。
- `-1` — CAN 控制器无法成功将数据传输到 CAN 网络，或者没有可用于将数据传输到 CAN 网络的发送邮箱。
- `0` — 没有可用的发送队列。
- `1` — CAN 控制器成功将数据传输到 CAN 网络。

#### 依赖关系

- 要启用此端口，请选中 **Output status**。

**数据类型：** `uint8`

## 参数

### **CAN module** — CAN 控制器 `CAN0`（默认） | `CAN1` | `CAN2` | `CAN3`

根据所使用的 Arduino 开发板选择 CAN 控制器。

| Arduino 开发板 | 支持的 CAN 控制器 |
| --- | --- |
| Arduino Due | CAN0 和 CAN1 |
| Arduino 兼容的 Teensy 4.0 和 4.1 | CAN1、CAN2 和 CAN3 |

有关如何为 On-board CAN Receive 模块分配或查看 Arduino 开发板引脚的详细信息，请点击 **View pin map**。

### **Data is input as** — 数据输入类型 `Raw data`（默认） | `CAN Msg`

选择输入消息类型。

- `Raw data` — 选择此选项可将输入消息作为 1-by-*N* `uint8` 数组接受。
- `CAN Msg` — 选择此选项可以 CAN 消息格式接受输入消息。

  执行以下步骤以 CAN 消息格式接受消息。

  - 将来自 Vehicle Network Toolbox™ 的 CAN Pack (Vehicle Network Toolbox) 添加到您的 Simulink® 模型。
  - 将 CAN Pack (Vehicle Network Toolbox) 的输出连接到 On-board CAN Transmit 模块的输入端口。
  - 使用 CAN Pack (Vehicle Network Toolbox) 模块的 **Data is input as** 列表中的选项，指定是要创建消息还是要上传 CAN 数据库文件。如果选择上传 CAN 数据库文件，则 CAN Pack 会从上传的文件继承消息属性。

On-board CAN Transmit 和 CAN Pack 模块连接

### **Output status** — 数据传输状态 `off`（默认） | `on`

选择此选项以请求 CAN 消息发送状态。

### Message

要启用 **Message** 部分下的参数，请将 **Data is input as** 设置为 `Raw data`。

### **Identifier type** — CAN 标识符类型 `Standard (11-bit identifier)`（默认） | `Extended (29-bit identifier)`

指定 CAN 标识符类型。

- `Standard (11-bit identifier)` — 使用此选项发送具有标准 11-bit 标识符的 CAN 消息。
- `Extended (29-bit identifier)` — 使用此选项发送具有扩展 29-bit 标识符的 CAN 消息。

### **Message ID** — CAN 消息标识符 `100`（默认） | 长度为 `11` 或 `29` bits 的数字标识符

指定消息标识符，对于标准 CAN 帧大小，其长度为 11 bits；对于扩展 CAN 帧大小，其长度为 29 bit。您可以用十进制、二进制或十六进制指定该值。对于二进制和十六进制格式，分别使用 `bin2dec` 和 `hex2dec`。消息标识符会被编码到发送至 CAN 总线的消息中。

### **Message length** — CAN 消息长度 `8`（默认） | 正整数 [1, 8]

以 bytes 为单位指定 CAN 消息的长度。

### **Remote frame** — 标识远程帧 `off`（默认） | `on`

选择此选项以标识该模块在 CAN 网络上发送的数据帧是否为远程帧。

## 所属库

Simulink Support Package for Arduino Hardware / Communication

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2024b 中引入**

## 描述

使用板载 Arduino CAN 控制器向 CAN 网络发送消息

使用 On-board CAN Transmit 模块从板载 Arduino® CAN 控制器发送 CAN 消息。该模块在每个采样时间以先进先出方法将消息从邮箱发送到 CAN 网络。

### 支持的 Arduino 开发板

- Arduino Due
- Arduino 兼容的 Teensy 4.0 和 4.1
