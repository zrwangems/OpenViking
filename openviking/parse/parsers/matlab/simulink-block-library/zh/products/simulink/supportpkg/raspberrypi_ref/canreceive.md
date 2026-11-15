---
type: simulink-block
title: 'CAN Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Communication'
documentation_page: 'canreceive'
documentation_source_path: 'supportpkg/raspberrypi_ref/canreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# CAN Receive

## 端口

### 输出

### **Data** — 消息数据端口 向量 | 标量

接收到的消息数据，以向量或标量形式返回。

**数据类型：** `uint8` | `CAN Msg`

### **Status** — 输出消息的状态 标量

接收到的输出消息的状态。

**数据类型：** `uint8`

### **Error** — 错误代码 标量

错误代码。

#### 依赖项

要启用此参数，请选择 **Output Error**。

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 00 | 00 | 00 | 00 | 00 | RXWAR | RXEP | RXOVR |
| bit7 | bit6 | bit5 | bit4 | bit3 | bit2 | bit1 | bit0 |

RXOVR：接收缓冲区溢出标志位

RXEP：接收错误被动标志位

RXWAR：接收错误警告标志位

### **Remote** — 远程消息标志 标量

远程消息标志。

#### 依赖项

要启用此参数，请选择 **Output Remote**。

## 参数

### **CAN interface** — CAN 接口的名称 `can0`（默认） | `char`

输入真实或虚拟 CAN 接口的名称。要查找 CAN 接口的名称，请在 Raspberry Pi 终端中执行 `ifconfig` 命令。要配置 CAN 接口，请参阅 CAN 属性。

### **Data to be output as** — 数据输出类型 `Raw data`（默认） | `CAN Msg`

选择用于接收消息的类型。

- `Raw data` – 要将消息接收为 1-by-*N* `uint8` 数组，请将 **Data to be output as** 选择为 `Raw data`。
- `CAN Msg` – 要以 CAN 消息格式接收消息，请将 **Data to be output as** 选择为 `CAN Msg`，然后执行以下步骤：

  1. 将 CAN Unpack (Vehicle Network Toolbox) 模块添加到您的 Simulink® 模型中。
  2. 将 CAN Receive 模块的输出连接到 CAN Unpack (Vehicle Network Toolbox) 模块的输入。
  3. 使用 CAN Unpack (Vehicle Network Toolbox) 模块的 **Data to be output as** 列表中的选项，指定您要创建消息还是上传 CAN 数据库文件。如果您选择上传 CAN 数据库文件，则 CAN Unpack (Vehicle Network Toolbox) 会从上传的文件继承消息属性。

  **注意**

  要使用 CAN Unpack (Vehicle Network Toolbox) 模块，您必须具有 Vehicle Network Toolbox 许可证。

### **Identifier Type** — 消息标识符类型 `Standard (11-bit identifier)`（默认） | `Extended (29-bit identifier)`

消息标识符的类型。

#### 依赖项

仅当您将 **Data to be output as** 选择为 `Raw data` 时，此参数才会出现。

### **Message ID** — 消息标识符 100（默认） | 长度为 11 或 29 bits 的数字标识符

消息标识符，对于标准帧，长度为 11 bits；对于扩展帧，长度为 29 bits；可使用十进制、二进制或十六进制指定。对于二进制和十六进制格式，请分别使用 `bin2dec(' ')` 和 `hex2dec(' ')` 转换输入项。消息标识符会被编码到发送到 CAN 总线的消息中。

#### 依赖项

仅当您将 **Data to be output as** 选择为 `Raw data` 时，此参数才会出现。要输出 `CAN Msg` 的标识符，请选择 CAN Unpack 模块的 **Output identifier**。

### **Message Length** — 消息长度 8（默认） | 小于或等于 8 的正整数

消息长度，单位为 bytes。

#### 依赖项

仅当您将 **Data to be output as** 选择为 `Raw data` 时，此参数才会出现。要输出 `CAN Msg` 的长度，请选择 CAN Unpack 模块的 **Output length**。

### **Sample Time** — 读取消息的时间间隔 0.1（默认） | -1 | 非负实数值

指定模块接收消息的频率，单位为 seconds。当您将此参数指定为 `-1` 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。

### **Output Error** — 接收消息中的错误 `off`（默认） | `on`

当您选择 **Output Error** 参数时，模块会配置一个输出端口 **Error**。该端口以 `uint8` 整数形式输出错误代码。代码中的每个 bit 对应于接收消息中的错误类型。输出 `0` 表示消息无错误。任何非 `0` 的值表示该消息是错误帧。

#### 依赖项

仅当您将 **Data to be output as** 选择为 `Raw data` 时，此参数才会出现。要输出 `CAN Msg` 中的错误，请选择 CAN Unpack 模块的 **Output error**。

### **Output Remote** — 启用远程消息 off（默认） | on

选择此参数以启用 **Remote** 输出端口。该端口输出消息远程帧状态。

#### 依赖项

要启用此参数，请将 **Data to be output as** 设置为 `Raw data`。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Communication

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019b 中引入**

## 描述

从 CAN 网络接收消息

CAN Receive 模块从 CAN 网络接收消息。此模块使用 SocketCAN，这是一个独立于设备的驱动程序，用于实现支持所有 CAN 扩展板的 CAN 接口。

CAN Receive 模块支持 `Raw data` 和 `CAN Msg` 作为输出类型。要使用 CANdb（CAN 数据库）文件或手动指定信号，请使用 `CAN Msg` 输出类型和 CAN Unpack 模块。CAN Unpack 模块可从 Vehicle Network Toolbox™ 获取。有关 CAN Unpack 模块的详细信息，请参阅 CAN Unpack (Vehicle Network Toolbox)。

有关如何启用 SPI 接口以及为 CAN 通信配置 MCP2515 CAN 控制器的详细信息，请参阅启用和配置 Raspberry Pi 以使用 MCP2515 CAN 控制器进行 SPI 和 CAN 通信。

您可以使用 CAN Receive 模块与真实或虚拟 CAN 接口交互。要在 Raspberry Pi® 上启用 CAN 接口，请参阅您的 CAN 扩展板的用户指南。有关如何设置虚拟 CAN 接口的详细信息，请参阅设置虚拟 CAN 接口。

**注意**

要为该模块生成 C/C++ 代码，您必须具有 Embedded Coder® 许可证。
