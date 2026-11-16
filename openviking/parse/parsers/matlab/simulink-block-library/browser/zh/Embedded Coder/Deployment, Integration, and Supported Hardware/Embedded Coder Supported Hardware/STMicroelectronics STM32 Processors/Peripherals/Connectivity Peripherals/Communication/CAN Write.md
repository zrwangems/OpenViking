---
type: simulink-block
title: 'CAN Write'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Connectivity Peripherals / Communication'
documentation_page: 'canwrite'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/canwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# CAN Write

## 端口

### 输入

### **Data** — 输入数据端口标量

该模块接受 `Raw` 数据格式的报文。要将报文接受为 uint8 数组，请将 Data Format 设置为 `Raw data`。

#### 依赖关系

要启用此端口，请将 **Data format** 设置为 `Raw data`。

**数据类型：** `uint8`

### **Msg** — 输入 CAN 报文标量

该模块接受 `CAN Message` 格式的报文。

您可以创建自己的报文，也可以将 CAN 数据库文件上传到 CAN Pack 模块。

#### 依赖关系

要启用此端口，请将 **Data format** 设置为 `CAN Message`。此外，在 **CAN Pack** 模块中将输出类型启用为 bus。

**数据类型：** `CAN Message`

### **Length** — CAN 报文长度标量

该端口接受要传输的 CAN 数据的长度，以 bytes 为单位。

#### 依赖关系

要启用此参数，请将 **Data format** 设置为 `Raw data`，并将 **Data length via** 设置为 `Inport`。

**数据类型：** `uint8`

### **ID** — CAN 报文标识符标量

该端口接受 CAN 报文标识符。ID 可以是：

- `0-2047`：用于 Standard（11-bit identifier）
- `0-536870911`：用于 Extended（29-bit identifier）

#### 依赖关系

要启用此参数，请将 **Data format** 设置为 `Raw data`，并将 **Identifier via** 设置为 `Inport`。

**数据类型：** `uint32`

### **ID Type** — CAN 报文标识符类型标量

该端口接受 CAN 报文标识符类型

- `0` - 如果它是 11-bit 标准标识符
- `1 or any value other than 0` - 如果它是 29-bit 标准标识符

#### 依赖关系

要启用此参数，请将 **Data format** 设置为 `Raw data`，并将 **Identifier type via** 设置为 `Inport`。

**数据类型：** `uint32`

### 输出

### **Status** — 接收报文的状态标量

该端口输出报文读取状态。

- 如果该模块读取到新报文，则状态为 `0`。
- 如果该模块未读取到新报文，则状态为 `1`。

#### 依赖关系

要启用此端口，请选择 **Output Status** 参数。

**数据类型：** `uint8`

### **FIFO Level** — FIFO 填充级别标量

该端口输出发送 FIFO 填充级别。

#### 依赖关系

要启用此参数，请选择 **Output transmit FIFO level** 参数。

## 参数

### **Module** — 用于通信的模块 `CAN1` (默认) | `CAN2` | `CAN3`

CAN 设备连接到的模块。

### **Operation mode** — 选择 CAN 读取操作模式 `Data` (默认) | `sleep` | `Wakeup`

选择 CAN 读取操作模式。

- `Data` - 要写入 CAN 数据/报文的数据
- `Sleep` - 选择以将 CAN 模块设置为休眠模式。在 Sleep 操作模式下，该模块接受逻辑值，以将 CAN 外设置于休眠模式。
- `Wakeup` - 选择以将 CAN 模块从休眠模式唤醒。在 Wakeup 操作模式下，该模块接受逻辑值，以使 CAN 外设进入唤醒状态。

### **Data format** — 数据输出类型 `Unpacked` (默认) | `Packed`

选择用于写入报文的输出类型。

- `RAW data` – 要将报文写入为 N-by-1 `uint8` 数组，请将 **Data format** 选择为 `Raw data`。
- `CAN Message` – 要以 CAN Message 格式写入报文，请将 **Data format** 选择为 `CAN Message`，并使用 CAN pack，确保将输出类型选择为 bus。

### **Identifier type via** — 报文标识符类型 `Dialog` (默认) | `Inport`

选择 Identifier Type via 为 `Dialog` 或 `input port`。

- 当您选择 Identifier Type via 为 `inport` 时，该模块配置一个输入端口 `Id Type`。
- 当您选择 Identifier Type via 为 `Dialog` 时，该模块通过 Dialog 接受 CAN 标识符类型。

#### 依赖关系

要启用此参数，请将 **Data format** 设置为 `Raw data`。

### **Identifier type** — 报文标识符类型 `Standard (11-bit identifier)` (默认) | `Extended (29-bit identifier)`

报文标识符的类型。

#### 依赖关系

要启用此参数，请将 **Identifier type via** 设置为 `Dialog`。

### **Identifier via** — 报文标识符类型 `Inport` (默认) | `Dialog`

报文标识符的类型。

- `0-2047`：用于 Standard（11-bit identifier）
- `0-536870911`：用于 Extended（29-bit identifier）

#### 依赖关系

要启用此参数，请将 **Data format** 设置为 `Raw data`。

### **Identifier** — 报文标识符 `100` (默认) | `numeric identifier of length 11 or 29 bits`

标识符，对于标准帧大小为 11 bits 长，对于扩展帧大小为 29 bits 长，可采用十进制、二进制或十六进制指定。对于二进制和十六进制格式，请分别使用 bin2dec(' ') 和 hex2dec(' ') 转换输入项。该标识符会编码到发送至 CAN 总线的报文中。

#### 依赖关系

要启用此参数，请将 **Data Format** 设置为 `Raw data`。

### **Data length via** — 启用远程报文 `Inport` (默认) | `Dialog`

选择 **Data length via** 为 Inport 或 Dialog。

- 当您选择 Data length via 为 `inport` 时，该模块配置一个输入端口 `Length`。
- 当您选择 Data length via 为 `Dialog` 时，该模块接受指定的输入数据大小。

#### 依赖关系

要启用此参数，请将 **Data format** 设置为 `Raw data`。

### **Length (bytes)** — 以 bytes 表示的长度 `8` (默认) | `1-8`

报文的长度，以 bytes 为单位，通过输入提供。

#### 依赖关系

要启用此参数，请将 **Data length via** 设置为 `Dialog`。

### **Transmit remote frame** — 输出远程报文 `off` (默认) | `on`

如果选择此参数，该模块将在 CAN 报文中发送远程帧。输入端口处的数据不会在 CAN 报文中发送。

#### 依赖关系

要启用此参数，请将 **Data Format** 设置为 `Raw data`。对于 CAN Msg，Remote Frame 继承自 CAN Pack 模块中指定的请求。

### **Output receive FIFO fill level** — 启用接收 FIFO 填充级别 `off` (默认) | `on`

当您选择 **Output receive FIFO fill level** 参数时，该模块配置一个输出端口 **FIFO level**。该端口输出发送 FIFO 报文级别。

### **Output Status** — 启用输出状态 `off` (默认) | `on`

当您选择 **Output Status** 参数时，该模块配置一个输出端口 **Status**。该端口输出状态消息。

### **Sample Time** — 读取报文的时间间隔 `-1` (默认) | `0.1` | `non-negative real value`

指定该模块接收报文的频率，以 seconds 为单位。当您将此参数指定为 `-1` 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。

### **Timeout** — 指定完成读取操作的等待时间 `0.001` (默认) | 0.1 | non-negative real value

指定阻塞 CAN 读取的时间，以 seconds 为单位。对于非阻塞，设置为 `0`。您将 Timeout 配置为完成读取操作所需等待的最长时间（以 seconds 为单位）。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Simulink Coder Support Package for STMicroelectronics Nucleo Boards / STM32H7

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

将数据写入 CAN 总线

CAN Write 模块将报文写入连接到硬件的控制器局域网（CAN）网络。

当操作模式设置为 `Data` 时，CAN Write 模块接受需要发送的 CAN 数据。当数据格式设置为 `Raw data` 时，该模块接受 `uint8` 类型的一维数组。

当数据格式设置为 `CAN Message` 时，该模块接受 Simulink® bus 信号作为输入。要从 Simulink bus 信号中提取数据，请将其连接到 CAN pack 模块。

**注意**

当数据长度（输入数组）与长度（输入标量）不同时，通过 CAN 模块传输的数据数量为数据长度或输入长度中的最小值。

使用模块参数对话框选择 Operation mode 及其属性。在 Model Configuration Parameters for STM32 Processor Based Boards 中配置 CAN 模块的属性。
