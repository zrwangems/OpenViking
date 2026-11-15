---
type: simulink-block
title: 'CAN Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / CAN'
documentation_page: 'canreceive'
documentation_source_path: 'supportpkg/arduino_ref/canreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# CAN Receive

## 端口

### 输出

### **Data** — 消息数据向量 | 标量

该模块以 `uint8` 和 `CAN Msg` 格式输出消息。

- `uint8` – 要将消息输出为 `uint8` 向量数组，请选择 **Data is output as** 为 `Raw data`。
- `CAN Msg` – 要以 CAN 消息格式输出消息，请选择 **Data is output as** 为 `CAN Msg`。有关详细信息，请参阅 Data to be output as。

**数据类型：** `uint8` | `CAN Msg`

### **Status** — 接收消息的状态 标量

该端口输出消息接收状态。如果模块接收到新消息，则状态为 `1`；如果未接收到，则为 `0`。

**数据类型：** `uint8`

### **Error** — 接收消息中的错误 标量

该端口输出错误代码，您可以使用这些代码识别接收消息中的错误类型。有关详细信息，请参阅 Output Error。

#### 依赖关系

仅当您选择 **Output Error** 参数时，此端口才会出现。

### **Remote** — 远程消息使能 标量

该端口发送远程帧请求。

#### 依赖关系

仅当您选择 **Output Remote** 参数时，此端口才会出现。

## 参数

### **Data to be output as** — 数据输出类型 `Raw data`（默认值） | `CAN Msg`

选择接收消息的类型。

- `Raw data` – 要将消息接收为 1-by-*N* `uint8` 数组，请选择 **Data to be output as** 为 `Raw data`。
- `CAN Msg` – 要以 CAN 消息格式接收消息，请选择 **Data to be output as** 为 `CAN Msg`，然后执行以下步骤：

  1. 将 Vehicle Network Toolbox™ 中的 CAN Unpack 模块添加到您的模型。
  2. 将 CAN Receive 模块的输出连接到 CAN Unpack 模块的输入。
  3. 使用 CAN Unpack 模块的 **Data to be output as** 列表中的选项，指定您是要创建自己的消息，还是要上传 CAN 数据库文件。如果选择上传 CAN 数据库文件，则 CAN Unpack 会从上传的文件继承消息属性。

  **注意**

  要使用 CAN Unpack 模块，您必须具有 Vehicle Network Toolbox 许可证。

### **Message ID** — 消息标识符 100（默认值） | 长度为 11 或 29 bits 的数字标识符

消息标识符，对于标准帧大小为 11 bits，对于扩展帧大小为 29 bits，可采用十进制、二进制或十六进制指定。对于二进制和十六进制格式，请分别使用 `bin2dec(' ')` 和 `hex2dec(' ')` 转换该输入项。消息标识符会编码到发送到 CAN 总线的消息中。

#### 依赖关系

仅当您选择 **Data to be output as** 为 `Raw data` 时，此参数才会出现。要输出 `CAN Msg` 的标识符，请选择 CAN Unpack 模块的 **Output identifier**。

### **Identifier Type** — 消息标识符类型 `Standard (11-bit identifier)`（默认值） | `Extended (29-bit identifier)`

消息标识符的类型。

#### 依赖关系

仅当您选择 **Data to be output as** 为 `Raw data` 时，此参数才会出现。

### **Message Length** — 消息长度 8（默认值） | 小于或等于 8 的正整数

消息的长度，以 bytes 为单位。

#### 依赖关系

仅当您选择 **Data to be output as** 为 `Raw data` 时，此参数才会出现。要输出 `CAN Msg` 的长度，请选择 CAN Unpack 模块的 **Output length**。

### **Sample Time** — 读取消息的时间间隔 0.1（默认值） | -1 | 非负实数值

指定模块接收消息的频率，以 seconds 为单位。将此参数指定为 `-1` 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

### **Output Error** — 接收消息中的错误 `off`（默认值） | `on`

当您选择 **Output Error** 参数时，模块会配置一个输出端口 **Error**。该端口以 `uint8` 整数形式输出错误代码。代码中的每个 bit 对应接收消息中的错误类型。输出为 `0` 表示消息无错误。任何非 `0` 值表示消息是错误帧。

#### 依赖关系

仅当您选择 **Data to be output as** 为 `Raw data` 时，此参数才会出现。要输出 `CAN Msg` 中的错误，请选择 CAN Unpack 模块的 **Output error**。

### **Output Remote** — 启用远程消息 `off`（默认值） | `on`

当您选择 **Output Remote** 参数时，模块会配置一个输出端口 **Remote**。该端口输出消息的远程帧状态。

#### 依赖关系

仅当您选择 **Data to be output as** 为 `Raw data` 时，此参数才会出现。

## 所属库

Simulink Support Package for Arduino Hardware / Common

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019b 中引入**

## 描述

从 CAN 网络接收消息

CAN Receive 模块通过使用连接到硬件的 CAN 扩展板从控制器局域网 (CAN) 网络接收消息。CAN 扩展板连接到硬件上的串行外设接口 (SPI) 引脚。

点击 **View pin map** 打开 Arduino Pin Mapping 表。

要了解如何为该模块分配引脚，请参阅 Pin Mapping for Arduino Timer-Independent Blocks。

使用模块参数对话框指定消息类型及其属性。在 Configuration Parameters 对话框中指定模型的 CAN 属性。

此模块仅支持基于 MCP2515 的 CAN 扩展板。

如果在未连接硬件的情况下仿真包含 CAN Receive 模块的模型，则该模块输出零。有关详细信息，请参阅 Block Produces Zeros or Does Nothing in Simulation。
