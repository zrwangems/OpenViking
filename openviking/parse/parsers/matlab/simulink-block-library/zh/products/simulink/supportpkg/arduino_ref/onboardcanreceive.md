---
type: simulink-block
title: 'On-board CAN Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / CAN'
documentation_page: 'onboardcanreceive'
documentation_source_path: 'supportpkg/arduino_ref/onboardcanreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# On-board CAN Receive

## 端口

### 输出

### **Data** — 来自 Arduino 板载 CAN 控制器的消息向量数据

该模块输出从 Arduino 板载 CAN 控制器读取的 CAN 数据。要将 CAN 数据输出为 `uint8`
消息向量，请将 Data to be output as 设置为
`Raw data`。要以 CAN 消息格式输出数据，请将
Data to be output as 设置为
`CAN Msg`。

#### 依赖项

- 要启用此端口，请将 Data to be output as 设置为
  `Raw data`。

**数据类型：** `uint8` | `CAN Msg`

### **Status** — 输入 CAN 消息的状态 `0` | `1`

该模块输出 CAN 消息读取状态。

- 如果该模块读取到新的 CAN
  消息，则状态为 `1`。
- 如果该模块未读取到新的 CAN
  消息，则状态为 `0`。

#### 依赖项

- 要启用此端口，请将 **Data to be output as** 设置为
  `Raw data`。

**数据类型：** `uint8`

### **Error** — CAN 消息的错误状态 `0` | `1`

该模块输出 CAN 消息错误状态。

- 如果输入 CAN 消息包含
  错误，则状态为 `1`。
- 如果输入到该模块的 CAN 消息
  没有错误，则状态为 `0`。

#### 依赖项

- 要启用此端口，请将 Data to be output as 设置为
  `Raw data`，并选择 **Output
  error**。

**数据类型：** `uint8`

### **Remote** — 远程帧状态标量

该模块输出远程消息帧状态。

- 如果传入的 CAN 数据是远程
  帧，则状态为 `1`。
- 如果传入的 CAN 数据不是远程
  帧，则状态为 `0`。

#### 依赖项

- 要启用此端口，请将 **Data to be output as** 设置为
  `Raw data`，并选择 **Output
  remote**。

**数据类型：** `uint8`

### **CAN Msg** — 接收到的 CAN 消息 `arduinoCANMsg` | bus

该模块将特定时间戳的 CAN 消息输出为信号总线或
`arduinoCANMsg`。

#### 依赖项

- 要启用此端口，请将 **Data to be output as** 设置为
  `CAN Msg`。

**数据类型：** `uint8` | `bus`

## 参数

### **CAN module** — CAN 控制器 `CAN0` (默认) | `CAN1` | `CAN2` | `CAN3`

根据您使用的 Arduino 开发板选择 CAN 控制器。

| Arduino Boards | Supported CAN Controller |
| --- | --- |
| Arduino Due | CAN0 和 CAN1 |
| Arduino compatible Teensy 4.0 and 4.1 | CAN1、CAN2 和 CAN3 |

有关如何为 On-board CAN Receive 模块分配或查看 Arduino 开发板引脚的更多信息，请点击
**查看引脚映射**。

### **Data to be output as** — 数据输出类型 `Raw data` (默认) | `CAN Msg`

选择输出消息类型。

- `Raw data` — 选择此选项可将消息读取为
  1-by-*N*
  `uint8` 数组。
- `CAN Msg` — 选择此选项可以 CAN
  消息格式读取消息。

  执行以下步骤以 CAN 消息格式读取消息。

  - 在您的 Simulink 模型中，从 Vehicle Network Toolbox™ 添加一个 CAN Unpack (Vehicle Network Toolbox)。
  - 将 On-board CAN Receive 模块的输出连接到
    CAN Unpack (Vehicle Network Toolbox) 模块的输入。
  - 使用 CAN Unpack (Vehicle Network Toolbox) 模块的 **Data to be output as** 列表
    中的选项，指定您是要创建消息还是要上传 CAN 数据库文件。如果
    选择上传 CAN 数据库文件，则 CAN Unpack 会从上传的文件继承消息
    属性。

On-board CAN Receive 和 CAN Unpack 模块连接

### **Identifier type** — CAN 标识符类型 `Standard (11-bit identifier)` (默认) | `Extended (29-bit identifier)`

指定 CAN 标识符类型。

- `Standard (11-bit identifier)` — 使用此选项可
  创建具有标准 11 位标识符的 CAN 消息。
- `Extended (29-bit identifier)` — 使用此选项可
  创建具有扩展 29 位标识符的 CAN 消息。

#### 依赖项

- 要启用此参数，请将 **Data to be output as** 设置为
  `Raw data`。

### **Message ID** — CAN 消息标识符 `100` (默认) | 长度为 `11` 或 `29` bits 的数字标识符

指定消息标识符，对于标准 CAN 帧大小，其长度为 11 bits；对于扩展 CAN 帧大小，其长度为 29 bits。您可以以十进制、二进制或十六进制指定该值。对于二进制和十六进制格式，分别使用 `bin2dec` 和 `hex2dec`。消息标识符会被编码到发送到 CAN 总线的消息中。

#### 依赖项

- 要启用此参数，请将 **Data to be output as** 设置为
  `Raw data`。

### **Message length** — CAN 消息长度 `8` (默认) | 正整数 [1, 8]

指定 CAN 消息的长度，以 bytes 为单位。

#### 依赖项

- 要启用此参数，请将 **Data to be output as** 设置为
  `Raw data`。

### **Sample time** — 模块读取 CAN 消息的频率 `-1` (默认) | 非负实数值

指定该模块从 Arduino 板载 CAN 控制器读取 CAN 消息的频率，以 seconds 为单位。

### 消息

要启用 **消息** 部分下的参数，请将
**Data to be output as** 设置为 `Raw data`。

### **Output error** — 请求错误状态 `off` (默认) | `on`

选择此选项可请求 CAN 消息的错误状态。要以 `CAN Msg` 消息类型输出错误，请在 CAN Unpack (Vehicle Network Toolbox) 模块中选择 **Output
error**。

### **Output remote** — 请求远程帧 `off` (默认) | `on`

选择此选项可从 CAN 节点请求数据。此选项会启用
**Remote** 输出端口

## 所属库

Simulink Support Package for Arduino Hardware / Communication

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024b 中引入**

## 描述

使用 Arduino 板载 CAN 控制器接收消息

使用 On-board CAN Receive 模块从 Arduino® 板载 CAN 控制器接收 CAN 消息。该模块以先进先出 (FIFO) 方式将输入消息存储在邮箱中。这些邮箱会在每个采样时间按排队顺序将 CAN 消息传递到您的 Simulink® 模型。

### 支持的 Arduino 开发板

- Arduino Due
- Arduino 兼容的 Teensy 4.0 和 4.1
