---
type: simulink-block
title: 'MCAN Transmit'
family: 'f280015x'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'F280015x'
documentation_page: 'mcantransmit'
documentation_source_path: 'ref/mcantransmit.html'
language: zh-CN
chinese_source: worker-translation
---

# MCAN Transmit

## 端口

### 输入

### **TX** — 输入数据端口向量 | 标量

该模块接受 `Raw data` 或 `CAN Msg` 格式的消息。

- `Raw data` – 若要以 `uint8` 向量数组形式接受消息，请将 **Data format** 设置为 `Raw data`。
- `CAN Msg` – 若要以 CAN 消息格式接受消息，请将 **Data format** 设置为 `CAN Msg`。您可以使用 CAN FD Pack 模块创建消息。

**数据类型：** `uint8` | `CAN Msg`
### 输出

### **Status** — CAN 消息传输状态标量

输出端口，用于显示 CAN 消息传输状态。Status 端口输出：

- `0` - 当 CAN 消息添加到发送 FIFO/Queue 时
- `1` - 当 CAN 消息未添加到发送 FIFO/Queue 时

#### 依赖项

要启用此端口，请选择 **Output Status** 参数。

## 参数

### **Data format** — 数据输出类型 `Raw data`（默认） | `CAN Msg`

选择一种类型以将消息写入发送 FIFO 或队列。此消息随后会传输到与硬件连接的 CAN 网络。

- `Raw data` – 若要将消息写为 1-by-*N* `uint8` 数组，请将 **Data Format** 选择为 `Raw data`。
- `CAN Msg` – 若要以 CAN 消息格式写入消息，请将 **Data Format** 选择为 `CAN Msg`，然后执行以下步骤：

  1. 将 C2000™ Microcontroller Blockset/Target Communication 库中的 CAN FD Pack 模块添加到您的模型。
  2. 将 CAN FD Pack 模块的输出连接到 **MCAN Transmit** 模块的输入
  3. 使用 CAN Pack 模块的 **Data to be input as** 列表中的选项，指定您要创建消息还是要上传 CAN 数据库文件。如果您选择上传 CAN 数据库文件，则 CAN FD Pack 模块会从上传的文件继承消息属性。

### **Frame format** — 帧格式类型 `CAN-FD`（默认） | `Classic CAN`

CAN 帧格式。

#### 依赖项

要启用此参数，请将 **Data Format** 设置为 `Raw data`。

### **Identifier Type** — 消息标识符类型 `Standard (11-bit identifier)`（默认） | `Extended (29-bit identifier)`

CAN 消息标识符类型。

#### 依赖项

要启用此参数，请将 **Data Format** 设置为 `Raw data`。

### **Identifier** — 消息标识符 `100`（默认） | `长度为 11 或 29 bits 的数字标识符`

标识符，对于标准帧大小为 11 bits 长，对于扩展帧大小为 29 bits 长，以十进制、二进制或十六进制格式指定。对于二进制和十六进制格式，分别使用 `bin2dec(' ')` 和 `hex2dec(' ')` 将输入转换为数值。该标识符用于创建传输到 CAN 总线的 CAN 消息。

#### 依赖项

要启用此参数，请将 **Data Format** 设置为 `Raw data`。

### **Length (bytes)** — 消息长度 `64`（默认） | `小于或等于 64(CAN-FD) 的正整数` | `小于或等于 8(Classic CAN) 的正整数`

CAN 消息中数据的长度，以 bytes 为单位。

对于 **Classic CAN** 帧格式，消息长度在 `0-8` bytes 之间，对于 **CAN-FD** 帧格式，范围为 `0-64`。当传输端口处的数据长度与您在此处指定的长度不匹配时，模块会显示错误。

#### 依赖项

要启用此参数，请将 **Data Format** 设置为 `Raw data`。

### **Remote Frame** — 启用远程消息 `off`（默认） | `on`

选择此参数可将 CAN 消息配置为远程消息。输入端口处的数据不会考虑用于传输。

#### 依赖项

要启用此参数，请将 **Data format** 设置为 `Raw data`，并将 **Frame format** 设置为 `Classic CAN`。

### **Enable bit rate switching** — 启用比特率切换消息 `off`（默认） | `on`

选择此参数可将 CAN 消息配置为比特率切换。CAN 消息中的数据将以您在硬件配置参数中指定的数据速率传输。

#### 依赖项

要启用此参数，请将 **Data format** 设置为 `Raw data`，并将 **Frame format** 设置为 `CAN-FD`。

### **Output Status** — 启用输出状态 `off`（默认） | `on`

当您选择 **Output Status** 参数时，模块会配置端口的 **Status**。该端口输出 CAN 消息传输状态。

## 所属库

C2000 Microcontroller Blockset / F2838x / M4 C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28p55x C2000 Microcontroller Blockset / F28p65x

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2021a 中引入**

## 描述

将串行数据发送到 CAN 总线

MCAN Transmit 模块将消息发送到连接到硬件的控制器局域网（CAN）。

在 Raw data 模式下，该模块接受 uint8 类型的 1-D 数组。在 CAN msg 模式下，该模块接受来自 CAN-FD Pack 模块的 Simulink® 总线信号。

**注意**

在 MCAN Transmit 模块中，如果发送 FIFO 已满，则数据不会被传输。

使用模块参数对话框指定 **Data Format** 及其属性。在 Configuration Parameters 中配置 CAN 模块的属性。有关更多信息，请参阅 Model Configuration Parameters for Texas Instruments C2000 Processors。
