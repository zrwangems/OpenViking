---
type: simulink-block
title: 'CAN Transmit'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Communication'
documentation_page: 'cantransmit'
documentation_source_path: 'supportpkg/raspberrypi_ref/cantransmit.html'
language: zh-CN
chinese_source: worker-translation
---

# CAN Transmit

## 端口

### 输入

### **Port1** — 消息数据向量 | 标量

该模块接受 `Raw data` 和 `CAN Msg` 格式的消息。

- `Raw data` — 要将消息接受为 `uint8` 向量数组，请将 **Data is input as** 设置为 `Raw data`。
- `CAN Msg` — 要以 CAN 消息格式接受消息，请将 **Data is input as** 设置为 `CAN Msg`。

**数据类型：** `uint8` | `CAN Msg`
### 输出

### **Port1** — 数据传输状态标量

用于显示数据传输状态的输出端口。有关更多信息，请参阅 Output Status。

#### 依赖关系

要启用此端口，请选中 **Output Status** 参数。

## 参数

### **CAN interface** — CAN 接口的名称 `can0` (default) | `char`

输入真实或虚拟 CAN 接口的名称。要查找 CAN 接口的名称，请在 Raspberry Pi 终端中执行 `ifconfig` 命令。要配置 CAN 接口，请参阅 CAN 属性。

### **Data is input as** — 数据输入类型 `Raw data` (default) | `CAN Msg`

用于传输消息的数据输入类型。

- `Raw data` — 要将消息接受为 `uint8` 向量数组，请将 **Data is input as** 设置为 `Raw data`。
- `CAN Msg` — 要以 CAN 消息格式接受消息，请将 **Data is input as** 设置为 `CAN Msg`，然后执行以下步骤：

  - 将 CAN Pack (Vehicle Network Toolbox) 模块添加到您的 Simulink® 模型中。
  - 将 CAN Pack (Vehicle Network Toolbox) 模块的输出连接到 CAN Transmit 模块的输入端口。
  - 使用 CAN Pack (Vehicle Network Toolbox) 模块的 **Data is input as** 列表中的选项，指定您是要创建消息还是要上传 CAN 数据库文件。如果选择上传 CAN 数据库文件，则 CAN Pack (Vehicle Network Toolbox) 会从上传的文件继承消息属性。

**注意**

要使用 CAN Pack (Vehicle Network Toolbox) 模块，您必须拥有 Vehicle Network Toolbox 许可证。

### **Wait until data sent** — 等待数据发送 `off` (default) | `on`

选中后，模块会在传输数据之前等待 **Time out in seconds** 参数指定的时间。

- `on` — 选中此参数时，模块在 **阻塞模式** 下运行。如果上一时间步接收到的消息已发送，则模块从输入端口接受消息。如果发送操作正在进行，则模块等待 **Time out in seconds** 参数指定的时间，然后从输入端口接受消息。

  如果目标硬件在计划开始下一次发送操作时仍在等待所请求的消息发送，则会发生任务超限。要修复超限：

  - 增大输入消息的采样时间。
  - 减小输入端口处消息的长度。
- `off` — 清除此参数时，模块在 **非阻塞模式** 下运行。如果上一时间步接收到的消息仍在传输中，则在给定时步输入端口处的消息将被丢弃。

### **Time out in seconds** — 发送数据的等待时间 1 (default) | integer

指定发送消息的等待时间。超过指定时间后，模块将超时。

#### 依赖关系

要启用此参数，请选中 **Wait until data sent**。

### **Output Status** — 消息传输的输出状态 off (default) | on

选择此选项可指示消息传输的状态。状态端口在成功传输时输出 `0`，失败时输出错误代码。错误代码列于此表中。

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 00 | 00 | ABTF | MLOA | TXERR | TXBO | TXEP | TXWAR |
| bit7 | bit6 | bit5 | bit4 | bit3 | bit2 | bit1 | bit0 |

ABTF：消息中止标志位

MLOA：消息仲裁丢失位

TXERR：检测到传输错误位

TXBO：Bus-Off 错误标志位

TXEP：发送错误被动标志位

TXWAR：发送错误警告标志位

### **Identifier Type** — 消息标识符类型 `Standard (11-bit identifier)` (default) | `Extended (29-bit identifier)`

消息标识符类型。

#### 依赖关系

要启用此参数，请将 **Data is input as** 设置为 `Raw data`。

### **Message ID** — 消息标识符 100 (default) | 长度为 11 位或 29 位的数字标识符

消息标识符，对于标准帧为 11 位长，对于扩展帧为 29 位长，可以用十进制、二进制或十六进制指定。对于二进制和十六进制格式，请分别使用 `bin2dec(' ')` 和 `hex2dec(' ')` 来转换输入项。消息标识符会被编码到发送至 CAN 总线的消息中。

#### 依赖关系

要启用此参数，请将 **Data is input as** 设置为 `Raw data`。对于 `CAN Msg`，消息标识符继承自在 CAN Pack (Vehicle Network Toolbox) 模块中指定的标识符。

### **Message Length** — 消息长度的值 8 (default) | 小于或等于 8 的正整数

消息的长度，以字节为单位。

#### 依赖关系

要启用此参数，请将 **Data is input as** 设置为 `Raw data`。对于 `CAN Msg`，消息长度继承自 CAN Pack (Vehicle Network Toolbox) 模块的长度。

### **Request Remote Frame** — 启用远程消息 off (default) | on

选中此参数时，消息的远程帧设置为 1，指示该模块正在请求传输特定标识符。

#### 依赖关系

要启用此参数，请将 **Data is input as** 设置为 `Raw data`。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Communication

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2019b 中引入**

## 描述

将消息传输到 CAN 网络

CAN Transmit 模块将消息传输到 CAN 网络。该模块使用 SocketCAN，这是一个与设备无关的驱动程序，用于实现支持所有 CAN 扩展板的 CAN 接口。

CAN Transmit 模块支持 `Raw data` 和 `CAN Msg` 作为输入类型。要使用 CANdb (CAN 数据库) 文件或手动指定信号，请使用 `CAN Msg` 输入类型和 CAN Pack 模块。CAN Pack 模块可从 Vehicle Network Toolbox™ 获得。有关 CAN Pack 模块的更多信息，请参阅 CAN Pack (Vehicle Network Toolbox)。

有关如何启用 SPI 接口以及为 CAN 通信配置 MCP2515 CAN 控制器的更多信息，请参阅使用 MCP2515 CAN 控制器为 SPI 和 CAN 通信启用并配置 Raspberry Pi。

您可以使用 CAN Transmit 模块与真实或虚拟 CAN 接口交互。要在 Raspberry Pi® 上启动 CAN 接口，请参阅您的 CAN 扩展板的用户指南。有关如何设置虚拟 CAN 接口的更多信息，请参阅设置虚拟 CAN 接口。

**注意**

要为该模块生成 C/C++ 代码，您必须拥有 Embedded Coder® 许可证。
