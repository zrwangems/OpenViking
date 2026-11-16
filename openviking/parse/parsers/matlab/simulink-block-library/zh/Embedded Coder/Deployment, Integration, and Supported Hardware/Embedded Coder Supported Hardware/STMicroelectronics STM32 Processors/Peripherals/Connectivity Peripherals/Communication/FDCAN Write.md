---
type: simulink-block
title: 'FDCAN Write'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Connectivity Peripherals / Communication'
documentation_page: 'fdcanwrite'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/fdcanwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# FDCAN Write

## 端口

### 输入

### **Data** — 输入数据端口 向量 | 标量

模块接受 `Raw` 数据格式的消息。要将消息接受为 uint8 向量数组，请将 Data Format 设置为 `Raw data`。

#### 依赖项

要启用此端口，请将 **Data format** 设置为 `Raw data`。

**数据类型：** `uint8`

### **Msg** — 输入 FDCAN 消息 向量 | 标量

模块接受 `CAN Message` 格式的消息。

您可以创建消息，也可以将 CAN 数据库文件上传到 FDCAN Pack 模块。

#### 依赖项

要启用此端口，请将 **Data format** 设置为 `CAN Message`。

**数据类型：** `CAN Message`

### **Length** — CAN 消息长度 标量

该端口接受接收到的 CAN 消息长度，以 bytes 为单位。

#### 依赖项

要启用此参数，请将 **Data format** 设置为 `Raw data`，并将 **Data length via** 设置为 `Inport`。

**数据类型：** `uint8`

### **ID** — FDCAN 消息标识符 标量

该端口接受 FDCAN 消息标识符。ID 可以是：

- `0-2047`：用于 Standard (11-bit identifier)
- `0-536870911`：用于 Extended (29-bit identifier)

#### 依赖项

要启用此参数，请将 **Data format** 设置为 `Raw data`，并将 **Identifier via** 设置为 `Inport`。

**数据类型：** `uint32`

### **ID Type** — CAN 消息标识符类型 标量

该端口接受 CAN 消息标识符类型

- `0` - 如果它是 11-bit standard identifier
- `1 or any value other than 0` - 如果它是 29-bit standard identifier

#### 依赖项

要启用此参数，请将 **Data format** 设置为 `Raw data`，并将 **Identifier type via** 设置为 `Inport`。

**数据类型：** `uint8`

### **Sleep** — FDCAN 处于 sleep 状态 标量

该端口接受一个逻辑值，以将 FDCAN 外设置于 sleep 模式。

#### 依赖项

要启用此端口，请将 **Operation mode** 设置为 `sleep`。

**数据类型：** `uint8`

### **Wakeup** — FDCAN 处于 wakeup 状态 标量

该端口接受一个逻辑值，以将 FDCAN 外设置于 wakeup 模式。

#### 依赖项

要启用此端口，请将 **Operation mode** 设置为 `wakeup`。

**数据类型：** `uint8`

### **Restricted Mode** — FDCAN 处于 restricted mode 标量

该端口接受一个逻辑值，以将 FDCAN 外设置于 restricted mode。

#### 依赖项

要启用此端口，请将 **Operation mode** 设置为 `Exit restricted operation mode`。

**数据类型：** `uint8`
### 输出

### **Status** — 接收消息的状态 标量

该端口输出消息读取状态。

- 如果模块读取到新消息，则状态为 `0`。
- 如果模块未读取到新消息，则状态为 `1`。

#### 依赖项

要启用此端口，请选择 **Output Status** 参数。

**数据类型：** `uint8`

### **FIFO Level** — FIFO 填充级别 标量

该端口输出接收 FIFO 填充级别。

#### 依赖项

要启用此参数，请选择 **Output transmit FIFO level** 参数。

## 参数

### **Module** — 用于通信的模块 `FDCAN1`（默认） | `FDCAN2` | `FDCAN3`

FDCAN 设备连接到的模块。

### **Operation mode** — 选择 FDCAN 读取操作模式 `Data`（默认） | `sleep` | `Wakeup` | `Exit restricted operation mode`

选择 FDCAN 读取操作模式。

- `Data` - 用于写入 FDCAN 数据/消息的数据
- `Sleep` - 选择以将 FDCAN 模块设置为 sleep 模式。在 Sleep 操作模式下，模块接受一个逻辑值，以将 FDCAN 外设置于 sleep 模式。当您将 operation mode 设置为 sleep 时，它会启用输入端口 `Sleep`。
- `Wakeup` - 选择以将 FDCAN 模块从 sleep 模式唤醒。在 Wakeup 操作模式下，模块接受一个逻辑值，以使 FDCAN 外设进入 wakeup 状态。当您将 operation mode 设置为 wakeup 时，它会启用输入端口 `Wakeup`。
- `Exit restricted operation mode` - 选择以使 FDCAN 模块退出 restricted mode。在 Exit restricted operation mode 下，模块接受一个逻辑值，以使 FDCAN 外设退出 restricted operation mode。当您将 operation mode 设置为 exit restricted operation mode 时，它会启用输入端口 `Restricted Mode`。

### **Data format** — 数据输出类型 `Unpacked`（默认） | `Packed`

选择用于写入消息的输出类型。

- `RAW data` – 要将消息写入为 8-by-1 `uint8` 数组，请将 **Data format** 选择为 `Raw data`。
- `CAN Message` – 要以 CAN Message 格式写入消息，请将 **Data format** 选择为 `CAN Message`。

### **Frame format** — 帧格式类型 `CAN-FD`（默认） | `CAN`

选择用于写入消息的输出类型。

- `RAW data` – 要将消息写入为 8-by-1 `uint8` 数组，请将 **Data format** 选择为 `Raw data`。
- `CAN Message` – 要以 CAN Message 格式写入消息，请将 **Data format** 选择为 `CAN Message`。

### **Identifier type via** — 消息标识符类型 `Dialog`（默认） | `Inport`

选择 Identifier Type via 为 `Dialog` 或 `input port`。

- 当您将 Identifier Type via 选择为 `inport` 时，模块会配置一个输入端口 `Id Type`。
- 当您将 Identifier Type via 选择为 `Dialog` 时，模块接受 CAN 消息。

#### 依赖项

要启用此参数，请将 **Data format** 设置为 `Raw data`。

### **Identifier type** — 消息标识符类型 `Standard (11-bit identifier)`（默认） | `Extended (29-bit identifier)`

消息标识符的类型。

#### 依赖项

要启用此参数，请将 **Identifier type via** 设置为 `Dialog`。

### **Identifier via** — 消息标识符类型 `Standard (11-bit identifier)`（默认） | `Extended (29-bit identifier)`

消息标识符的类型。

- `0-2047`：用于 Standard (11-bit identifier)
- `0-536870911`：用于 Extended (29-bit identifier)

#### 依赖项

要启用此参数，请将 **Data format** 设置为 `Raw data`。

### **Identifier** — 消息标识符 `100`（默认） | `numeric identifier of length 11 or 29 bits`

标识符，对于标准帧大小长度为 11 bits，对于扩展帧大小长度为 29 bits，以十进制、二进制或十六进制指定。对于二进制和十六进制格式，分别使用 bin2dec(' ') 和 hex2dec(' ') 转换输入项。该标识符会被编码到发送到 CAN 总线的消息中。

#### 依赖项

要启用此参数，请将 **Data Format** 设置为 `Raw data`。要输出 `CAN Msg` 的标识符，请选择 CAN Unpack 模块的 **Output identifier**。

### **Data length via** — 启用远程消息 `Inport`（默认） | `Dialog`

选择 **Data length via** 为 Inport 或 Dialog。

- 当您将 Data length via 选择为 `inport` 时，模块会配置一个输入端口 `Length`。
- 当您将 Data length via 选择为 `Dialog` 时，模块接受指定的输入数据大小。

#### 依赖项

要启用此参数，请将 **Data format** 设置为 `Raw data`。

### **Length (bytes)** — 以 bytes 为单位的长度 `8`（默认） | `1-8`

消息的长度，以 bytes 为单位，通过输入提供。

#### 依赖项

要启用此参数，请将 **Data length via** 设置为 `Dialog`。

### **Enable bitrate switching** — FDCAN 比特率切换 `off`（默认） | `on`

选择此参数以启用比特率切换。

#### 依赖项

要启用此参数，请将 **Data Format** 设置为 `Raw data`，将 **Operation mode** 设置为 `Data`，并将 **Frame format** 设置为 `CAN-FD`。

### **Transmit remote frame** — 输出远程消息 `off`（默认） | `on`

如果选择此参数，模块会在 CAN 消息中发送远程帧。输入端口处的数据不会在 CAN 消息中发送。

#### 依赖项

要启用此参数，请将 **Data Format** 设置为 `Raw data`，并将 **Frame format** 设置为 `CAN`。对于 CAN Msg，Remote Frame 继承自 CAN Pack 模块中指定的请求。

### **Output receive FIFO fill level** — 启用接收 FIFO 填充级别 `off`（默认） | `on`

当您选择 **Output receive FIFO fill level** 参数时，模块会配置一个输出端口 **FIFO level**。该端口输出接收 FIFO 消息级别。

### **Output Status** — 启用输出状态 `off`（默认） | `on`

当您选择 **Output Status** 参数时，模块会配置一个输出端口 **Status**。该端口输出状态消息。

### **Sample Time** — 读取消息的时间间隔 `-1`（默认） | `0.1` | `non-negative real value`

指定模块接收消息的频率，以 seconds 为单位。当您将此参数指定为 `-1` 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。

### **Timeout** — 指定完成读取操作的等待时间 `0.001`（默认） | 0.1 | non-negative real value

指定以 seconds 为单位的时间，以阻塞 CAN 读取。对于非阻塞，设置为 `0`。您将 Timeout 配置为等待完成读取操作的最大时间（以 seconds 为单位）。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

将数据写入 FDCAN 总线

FDCAN Write 模块将消息写入连接到硬件的 Controller Area Network (CAN) 网络。

当 operation mode 设置为 `Data` 时，FDCAN Write 模块接受需要发送的 CAN 数据。当 data format 设置为 `Raw data` 时，模块接受 `uint8` 类型的 1-D 数组。

当 data format 设置为 `CAN Message` 时，模块接受输入为 Simulink® bus 信号。要从 Simulink bus 信号中提取数据，请将其连接到 FDCAN pack 模块。

使用模块参数对话框选择 Operation mode 及其属性。在配置参数中配置 FDCAN 模块的属性。
