---
type: simulink-block
title: 'FDCAN Read'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Connectivity Peripherals / Communication'
documentation_page: 'fdcanread'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/fdcanread.html'
language: zh-CN
chinese_source: worker-translation
---

# FDCAN Read

## 端口

### 输出

### **Data** — 消息数据向量 | 标量

该模块以 `uint8` 或 `CAN Msg` 格式输出消息。

数据最大大小为 `uint8` 格式的 [64x1]。长度中定义的 bytes 数表示输出的有效数据。

- 如果 **Output type** 设置为 `Unpacked`，则接收到的消息数据是 `uint8` 类型的 64×1 数组。
- 如果 **Output type** 设置为 `Packed`，则数据端口重命名为 **Msg**，接收到的消息数据作为 Simulink 总线信号输出。

如果接收到的 CAN 消息是远程帧，则此端口输出 `0`。

**数据类型：** `uint8` | `CAN Msg`

### **Restricted Mode** — 受限消息状态 标量

端口输出 FDCAN 模块状态。

- 如果 FDCAN 模块处于受限操作模式，则状态为 `1`。
- 如果 FDCAN 模块不处于受限操作模式，则状态为 `0`。

#### 依赖关系

要启用此参数，请将 operation mode 设置为 **Read restricted operation mode status**。

**数据类型：** `uint8`

### **Status** — 接收消息状态 标量

端口输出消息读取状态。

- 如果模块读取到新消息，则状态为 `0`。
- 如果模块未读取到新消息，则状态为 `1`。

#### 依赖关系

要启用此参数，请选中 **Output Status** 参数。

**数据类型：** `uint8`

### **Sleep** — FDCAN 模块状态 标量

端口输出 FDCAN 模块状态。

- 如果 FDCAN 模块处于 sleep 模式，则状态为 `1`。
- 如果 FDCAN 模块不处于 sleep 模式，则状态为 `0`。

#### 依赖关系

要启用此参数，请将 operation mode 设置为 **Read sleep status**。

**数据类型：** `uint8`

### **Msg** — 接收消息状态 标量

CAN 接收模块以 Simulink 总线信号形式输出 CAN 接收消息。要从 Simulink 总线信号中提取数据，请将其连接到 CAN FD Unpack 模块。

端口输出消息读取状态。

- 如果消息读取不成功，则状态为 `1`
- 如果消息读取成功，则状态为 `0`。

#### 依赖关系

要启用此参数，请将 **Output type** 设置为 `Packed`。

**数据类型：** `CAN Msg`

### **Length** — CAN 消息长度 标量

端口输出接收到的 CAN 消息的长度，以 bytes 为单位。

#### 依赖关系

要启用此参数，请将 **Output type** 设置为 `Unpacked`。

**数据类型：** `uint8`

### **ID** — CAN 消息标识符 标量

端口输出 CAN 消息标识符。

#### 依赖关系

要启用此参数，请将 **Output type** 设置为 `Unpacked`。

**数据类型：** `uint32`

### **ID Type** — CAN 消息标识符类型 标量

端口输出 CAN 消息标识符类型

- `0` - 如果是 11 位标准标识符
- `1` - 如果是 29 位标准标识符

#### 依赖关系

要启用此参数，请将 **Output type** 设置为 `Unpacked`。

**数据类型：** `uint32`

### **Remote** — 远程消息标志 标量

远程消息标志。如果接收到的 CAN 消息是远程帧，则端口输出 `1`。

#### 依赖关系

要启用此参数，请选中 **Output remote** 参数。

### **Frame Type** — 帧类型消息 标量

帧类型输出消息。如果接收到 FDCAN 消息帧，则端口输出 `1`；如果接收到 Classic 消息帧，则输出 `0`。

#### 依赖关系

要启用此参数，请选中 **Output frame type** 参数。

**数据类型：** `uint8`

### **Bitrate Switching** — 位速率切换消息 标量

位速率切换输出消息。

- `0` - 当 CAN FD 帧在无位速率切换的情况下传输时。
- `1` - 当 CAN FD 帧在位速率切换的情况下传输时。

#### 依赖关系

要启用此参数，请选中 **Output bitrate switching** 参数。

**数据类型：** `uint8`

### **FIFO Level** — FIFO 填充水平 标量

端口输出接收到的 FIFO 填充水平。

#### 依赖关系

要启用此参数，请选中 **Output receive FIFO level** 参数。

## 参数

### **Module** — 用于通信的模块 `FDCAN1` (默认) | `FDCAN2` | `FDCAN3`

FDCAN 设备连接到的模块。

### **Operation mode** — 选择 FDCAN 读取操作模式 `Data` (默认) | `Read sleep status` | `Read restricted operation mode status` | `Read last error code`

选择 CAN 读取操作模式。

- `Data` - 要读取 FDCAN 数据/消息的数据
- `Read sleep status` - 读取 FDCAN 模块的 sleep/电源状态。在 Read sleep status 操作模式下，如果 FDCAN 外设处于 sleep 模式，则模块输出逻辑状态。

  在此操作模式下，模块配置输出端口 `Sleep`。
- `Read restricted operation mode status` - 读取 CAN 模块是否处于受限模式。在 `Read restricted operation mode status` 操作模式下，如果 FDCAN 外设处于受限操作模式，则模块输出逻辑状态。

  在此操作模式下，模块配置输出端口 `Restricted mode`。
- `Read last error code` - 提供硬件为 CAN 总线上最后发送或接收的消息设置的状态。在 Read last error code 操作模式下，如果 CAN 外设处于唤醒状态，则模块输出逻辑状态。

  以下是错误代码及其对应状态。

  - `000` - 无错误
  - `001` - 填充错误
  - `010` - 格式错误
  - `011` - 确认错误
  - `100` - 位隐性错误
  - `101` - 位显性错误
  - `110` - CRC 错误
  - `111` - 由软件设置

### **Output type** — 数据输出类型 `Unpacked` (默认) | `Packed`

选择输出类型以读取消息。

- `Unpacked` – 在 Unpacked 输出类型中，模块输出接收到的值，形式为 uint8 类型的 [8x1] 数组。在 FDCAN Read 模块的 unpacked 类型中，可以启用所有输出端口（ID、ID type、Data、Status、Remote、Frame type、bitrate switching、Length、FIFO level）。
- `Packed` – 在 Packed 输出类型中，模块输出 Simulink 总线信号。要从 Simulink 总线信号中提取数据，请将其连接到 CAN Unpack 模块。

### **Read source** — FDCAN 消息读取源 `FIFO 0` (默认) | `FIFO 1` | `Buffers`

CAN Read 模块从读取源输出 CAN 消息。您可以在配置参数中配置读取源滤波器配置。

### **Buffer number** — 指定缓冲区编号 `0` (默认) |

指定 FDCAN Read 模块缓冲区编号。

#### 依赖关系

要启用此参数，请将 **read source** 设置为 `Buffers`。

### **Output Identifier Type** — 启用标识符类型 `off` (默认) | `on`

当您选中 Output Identifier Type 参数时，模块配置输出端口 `Id Type`。该端口输出标准或扩展消息状态。

#### 依赖关系

要启用此参数，请将 **Output type** 设置为 `unpacked`。

### **Output Remote** — 启用远程消息 `off` (默认) | `on`

当您选中 **Output Remote** 参数时，模块配置输出端口 **Remote**。该端口输出消息远程帧状态。

#### 依赖关系

要启用此参数，请将 **Output type** 设置为 `unpacked`。

### **Output frame type** — 启用帧类型消息 `off` (默认) | `on`

当您选中 **Output Remote** 参数时，模块配置输出端口 **Frame Type**。该端口输出 `0` (Classic) 或 `1` (FD) 消息状态。

#### 依赖关系

要启用此参数，请将 **Output type** 设置为 `unpacked`。

### **Output bit rate switching** — 启用位速率切换 `off` (默认) | `on`

当您选中 **Output bit rate switching** 参数时，模块配置输出端口 **Bitrate switching**。该端口输出 `0` (禁用) 或 `1` (启用) 消息状态。

#### 依赖关系

要启用此参数，请将 **Output type** 设置为 `unpacked`。

### **Output receive FIFO fill level** — 启用接收 FIFO 填充水平 `off` (默认) | `on`

当您选中 **Output receive FIFO fill level** 参数时，模块配置输出端口 **FIFO level**。该端口输出接收到的 FIFO 水平消息。

### **Output Status** — 启用输出状态 `off` (默认) | `on`

当您选中 **Output Status** 参数时，模块配置输出端口 **Status**。该端口输出状态消息。

### **Sample Time** — 读取消息的时间间隔 `-1` (默认) | `0.1` | `non-negative real value`

指定模块接收消息的频率，以 seconds 为单位。当您将此参数指定为 `-1` 时，Simulink 将根据模型中的模块上下文确定模块的最佳采样时间。

### **Timeout** — 指定等待完成读取操作的时间 `0.001` (默认) | 0.1 | non-negative real value

指定阻塞 FDCAN 读取的时间，以 seconds 为单位。对于非阻塞，设置为 `0`。您将 Timeout 配置为等待完成读取操作的最大时间（以 seconds 为单位）。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2023a 中引入**

## 描述

从 CAN FD 总线读取数据

FDCAN Read 模块从连接到硬件的控制器局域网 (CAN) 网络读取消息。

当 operation mode 设置为 `Data` 时，FDCAN Read 模块输出 CAN 数据。当 output type 设置为 `Unpacked` 时，模块输出接收到的值，形式为 `uint8` 类型的 `[64x1]` 数组。

当 output type 设置为 `Packed` 时，模块输出 Simulink® 总线信号。要从 Simulink 总线信号中提取数据，请将其连接到 CAN FD Unpack 模块。

使用模块参数对话框选择 Operation mode 及其属性。在配置参数中配置 FDCAN 模块的属性。
