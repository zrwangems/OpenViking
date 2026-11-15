---
type: simulink-block
title: 'CAN Transmit'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / CAN'
documentation_page: 'cantransmit'
documentation_source_path: 'supportpkg/arduino_ref/cantransmit.html'
language: zh-CN
chinese_source: worker-translation
---

# CAN Transmit

## 端口

### 输入

### **Port1** — 消息数据向量 | 标量

该模块接受 `Raw data` 和 `CAN Msg` 格式的消息。

- `Raw data` – 要将消息作为 `uint8` 向量数组接受，请将 **Data is input as** 设置为 `Raw data`。
- `CAN Msg` – 要以 CAN 消息格式接受消息，请将 **Data is input as** 设置为 `CAN Msg`。您可以创建消息，也可以上传 CAN 数据库文件。有关详细信息，请参阅 Data is input as。

**数据类型：** `uint8` | `CAN Msg`

### 输出

### **Port1** — 数据传输状态 标量

输出端口，用于显示数据传输状态。有关详细信息，请参阅 Output Status。

#### 依赖关系

仅当选择 **Output Status** 参数时，此端口才会出现。

## 参数

### **Data is input as** — 数据输入类型 `Raw data` (默认) | `CAN Msg`

选择输入端口处消息的类型。

- `Raw data` – 要将消息作为 `uint8` 向量数组接受，请将 **Data is input as** 设置为 `Raw data`。
- `CAN Msg` – 要以 CAN 消息格式接受消息，请将 **Data is input as** 设置为 `CAN Msg`，然后执行以下步骤：

  1. 从 Vehicle Network Toolbox™ 向模型添加一个 CAN Pack (Vehicle Network Toolbox) 模块。
  2. 将 CAN Pack 模块的输出连接到 CAN Transmit 模块的输入端口。
  3. 使用 CAN Pack 模块的 **Data is input as** 列表中的选项，指定是要创建消息还是要上传 CAN 数据库文件。如果选择上传 CAN 数据库文件，则 CAN Pack 会从上传的文件继承消息属性。

  **注意**

  要使用 CAN Pack 模块，您必须拥有 Vehicle Network Toolbox 许可证。

### **Output Status** — 数据传输状态 `off` (默认) | `on`

选择 **Output Status** 参数时，该模块会配置一个输出端口。该端口以 `uint8` 整数形式输出数据传输状态。该整数中的每一位对应数据传输期间发生的错误类型。输出为 `0` 表示传输成功。

### **Wait until data sent** — 等待数据发送完成 `off` (默认) | `on`

- `on` — 选择此参数时，模块在 **阻塞模式** 下运行。如果上一个时间步接收到的消息已发送，则模块从输入端口接受消息。如果发送操作正在进行，模块会等待 **Time out in seconds** 参数指定的时间，然后从输入端口接受消息。

  如果计划开始下一次发送操作时，目标硬件仍在等待所请求的消息发送完成，则会发生任务超限。要修复超限：

  - 增加输入消息的采样时间。
  - 减少输入端口处消息的长度。

- `off` — 清除此参数时，模块在 **非阻塞模式** 下运行。如果上一个时间步接收到的消息传输仍在进行，则在给定时间步输入端口处的消息会被丢弃。

### **Time out in seconds** — 发送消息的等待时间 1 (默认) | 整数

指定发送消息的等待时间。超过指定时间后，模块将超时。

#### 依赖关系

仅当选择 **Wait until data sent** 参数时，此参数才会出现。

### **Message ID** — 消息标识符 100 (默认) | 长度为 11 位或 29 位的数字标识符

消息标识符，对于标准帧长度为 11 位，对于扩展帧长度为 29 位，以十进制、二进制或十六进制指定。对于二进制和十六进制格式，分别使用 `bin2dec(' ')` 和 `hex2dec(' ')` 转换输入。消息标识符会被编码到发送到 CAN 总线的消息中。

#### 依赖关系

仅当将 **Data is input as** 选择为 `Raw data` 时，此参数才会出现。对于 `CAN Msg`，**Message ID** 继承自 CAN Pack 模块中指定的标识符。

### **Identifier Type** — 消息标识符类型 `Standard (11-bit identifier)` (默认) | `Extended (29-bit identifier)`

消息标识符的类型。

#### 依赖关系

仅当将 **Data is input as** 选择为 `Raw data` 时，此参数才会出现。对于 `CAN Msg`，**Identifier Type** 继承自 CAN Pack 模块中指定的类型。

### **Message Length** — 消息长度 8 (默认) | 小于或等于 8 的正整数

消息长度，以字节为单位。

#### 依赖关系

仅当将 **Data is input as** 选择为 `Raw data` 时，此参数才会出现。对于 `CAN Msg`，**Message Length** 继承自 CAN Pack 模块的长度。

### **Request Remote Frame** — 启用远程消息 `off` (默认) | `on`

选择 **Request Remote Frame** 参数时，消息的远程帧设置为 1，表示模块正在请求传输特定标识符。

#### 依赖关系

仅当将 **Data is input as** 选择为 `Raw data` 时，此参数才会出现。对于 `CAN Msg`，**Request Remote Frame** 继承自 CAN Pack 模块中指定的请求。

## 所属库

Simulink Support Package for Arduino Hardware / Common

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2019b 中引入**

## 描述

将消息传输到 CAN 网络

CAN Transmit 模块通过使用 CAN 扩展板将消息传输到控制器局域网 (CAN) 网络。CAN 扩展板连接到硬件上的串行外设接口 (SPI) 引脚。

点击 **View pin map** 打开 Arduino 引脚映射表。

要了解如何为该模块分配引脚，请参阅 Arduino 定时器无关模块的引脚映射。

使用模块参数对话框指定消息类型及其属性。在配置参数对话框中指定模型的 CAN 属性。

此模块仅支持基于 MCP2515 的 CAN 扩展板。

如果在未连接硬件的情况下仿真包含 CAN Transmit 模块的模型，则该模块不执行任何操作。有关详细信息，请参阅模块在仿真中产生零值或不做任何事。
