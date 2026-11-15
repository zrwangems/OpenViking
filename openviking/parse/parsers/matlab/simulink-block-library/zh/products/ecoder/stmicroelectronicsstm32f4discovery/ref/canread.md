---
type: simulink-block
title: 'CAN Read'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Connectivity Peripherals / Communication'
documentation_page: 'canread'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/canread.html'
language: zh-CN
chinese_source: worker-translation
---

# CAN Read

## 端口

### 输出

### **Data** — 消息数据标量

该模块以 `uint8` 或 `CAN Msg` 格式输出消息。

数据的最大大小为 uint8 格式的 [8x1]。length 中定义的 bytes 数量表示输出的有效数据。

- 如果 **Output type** 设置为 `Unpacked`，则接收到的消息数据是 `uint8` 类型的 8-by-1 数组。
- 如果 **Output type** 设置为 `Packed`，则数据端口重命名为 **Msg**，并且接收到的消息数据作为 Simulink 总线信号输出。

如果接收到的 CAN 消息是远程帧，则该端口输出 `0`。

**数据类型：** `uint8` | `CAN Msg`

### **Status** — 接收消息状态标量

该端口输出消息读取状态。

- `1` - 不成功。
- `0` - 成功。

#### 依赖项

要启用此参数，请选择 **Output Status** 参数。

**数据类型：** `uint8`

### **Length** — CAN 消息长度标量

该端口输出接收到的 CAN 消息的长度，单位为 bytes。

#### 依赖项

要启用此参数，请将 **Output type** 设置为 `Unpacked`。

**数据类型：** `uint8`

### **Id** — CAN 消息标识符标量

该端口输出 CAN 消息标识符。

#### 依赖项

要启用此参数，请将 **Output type** 设置为 `Unpacked`。

**数据类型：** `uint32`

### **ID Type** — CAN 消息标识符类型标量

该端口输出 CAN 消息标识符类型

- `0` - 如果是 11 位标准标识符
- `1` - 如果是 29 位标准标识符

#### 依赖项

要启用此参数，请将 **Output type** 设置为 `Unpacked`。

**数据类型：** `uint32`

### **Remote** — 远程消息标志标量

远程消息标志。如果接收到的 CAN 消息是远程帧，则该端口输出 `1`。

#### 依赖项

要启用此参数，请选择 **Output remote** 参数。

### **FIFO Level** — FIFO 填充水平标量

该端口输出接收 FIFO 填充水平。

FIFO 水平提供读取消息后的 RX FIFO 水平。TX FIFO 提供 TX FIFO 的空闲量。

#### 依赖项

要启用此参数，请选择 **Output receive FIFO level** 参数。

## 参数

### **Module** — 用于通信的模块 `CAN1` (default) | `CAN2` | `CAN3`

CAN 设备连接到的模块。

### **Operation mode** — 选择 CAN 读取操作模式 `Data` (default) | `Read sleep status` | `Read last error code`

选择 CAN 读取操作模式。

- `Data` - 用于读取 CAN 消息的数据
- `Read sleep status` - 读取 CAN 模块的睡眠状态。在 Read sleep status 操作模式下，如果 CAN 外设处于睡眠模式，则模块输出逻辑状态。
- `Read last error code` - 提供硬件为 CAN 总线上最后发送或接收的消息设置的状态。

  以下是错误码及其各自状态。

  - `000` - 无错误
  - `001` - 填充错误
  - `010` - 格式错误
  - `011` - 确认错误
  - `100` - 位隐性错误
  - `101` - 位显性错误
  - `110` - CRC 错误
  - `111` - 由软件设置

### **Output type** — 数据输出类型 `Unpacked` (default) | `Packed`

选择用于读取消息的输出类型。

- `Unpacked` – 在 Unpacked 输出类型中，模块将接收到的值输出为 uint8 类型的 [8x1] 数组。对于 CAN Read 模块的 unpacked 类型，您可以启用所有输出端口(ID、ID type、Data、Status、Remote、Length、FIFO level)。
- `Packed` – 在 Packed 输出类型中，模块输出 Simulink 总线信号。

### **Read source** — CAN 消息读取源 `FIFO 0` (default) | `FIFO 1`

CAN Read 模块从读取源输出 CAN 消息。您可以在配置参数中配置读取源筛选器配置。

### **Output Identifier Type** — 启用标识符类型 `off` (default) | `on`

当您选择 Output Identifier Type 参数时，模块配置一个输出端口 `Id Type`。该端口输出标准或扩展消息状态。

#### 依赖项

要启用此参数，请将 **Output type** 设置为 `unpacked`。

### **Output Remote** — 启用远程消息 `off` (default) | `on`

当您选择 **Output Remote** 参数时，模块配置一个输出端口 **Remote**。该端口输出消息远程帧状态。

#### 依赖项

要启用此参数，请将 **Output type** 设置为 `unpacked`。

### **Output receive FIFO fill level** — 启用接收 FIFO 填充水平 `off` (default) | `on`

当您选择 **Output receive FIFO fill level** 参数时，模块配置一个输出端口 **FIFO level**。该端口输出接收 FIFO 消息水平。

### **Output Status** — 启用输出状态 `off` (default) | `on`

当您选择 **Output Status** 参数时，模块配置一个输出端口 **Status**。该端口输出状态消息。

### **Sample Time** — 读取消息的时间间隔 `-1` (default) | `0.1` | `non-negative real value`

指定模块接收消息的频率，单位为 seconds。当您将此参数指定为 `-1` 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。

### **Timeout** — 指定完成读取操作的等待时间 `0.001` (default) | 0.1 | non-negative real value

指定阻塞 CAN 读取的时间，单位为 seconds。对于非阻塞，请设置为 `0`。您将 Timeout 配置为等待完成读取操作的最长时间（单位为 seconds）。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Simulink Coder Support Package for STMicroelectronics Nucleo Boards / STM32H7

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

从 CAN 网络读取消息

CAN Read 模块从连接到硬件的控制器局域网 (CAN) 网络读取消息。

当 operation mode 设置为 `Data` 时，CAN Read 模块输出 CAN 数据。当 output type 设置为 `Unpacked` 时，模块将接收到的值输出为 `uint8` 类型的 `[8x1]` 数组。

当 output type 设置为 `Packed` 时，模块输出 Simulink® 总线信号。要从 Simulink 总线信号中提取数据，请将其连接到 CAN Unpack 模块。CAN Unpack 模块可从 Vehicle Network Toolbox™ 获取。

使用模块参数对话框选择 Operation mode 及其属性。在 Model Configuration Parameters for STM32 Processor Based Boards 中配置 CAN 模块的属性。
