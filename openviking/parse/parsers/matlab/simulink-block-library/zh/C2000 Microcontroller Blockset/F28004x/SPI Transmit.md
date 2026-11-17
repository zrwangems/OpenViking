---
type: simulink-block
title: 'SPI Transmit'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2802x'
documentation_page: 'spitransmit'
documentation_source_path: '../ecoder/stmicroelectronicsstm32f4discovery/ref/spitransmit.html'
language: zh-CN
chinese_source: worker-translation
---

# SPI Transmit

## 端口

### 输入

### **Tx** — SPI 发送数据向量

通过 SPI 接口写入设备的数据。

**数据类型：** `uint8` | `uint16` | `uint32`
### 输出

### **Status** — SPI 发送状态 0 | 1 | 2

SPI 数据传输的状态。错误状态值表示：

- 0 — 无错误。
- 1 — 模块在发送数据时发生超时。
- 2 — 发送的数据包含错误。

#### 依赖关系

要启用此端口，请选择 **Enable status
output** 参数。

**数据类型：** `uint8` | `uint16` | `uint32`

## 参数

### 主要

### **SPI module** — 要写入数据的 SPI 模块 `SPI1`（默认）| `SPI2` | `SPI3` | `SPI4` | `SPI5` | `SPI6`

SPI 外设设备所连接的 SPI 模块。每个处理器具有不同数量的模块。

### **Clock polarity** — SPI 时钟极性 `Low`（默认）| `High`

用于 SPI 通信模式的时钟极性。此参数对于发送和接收模块必须相同。

### **Clock phase** — SPI 时钟相位 `1 Edge`（默认）| `2 Edge`

用于 SPI 通信模式的时钟相位。此参数对于发送和接收模块必须相同。

### **Enable status output** — 启用 SPI 状态模式 `off`（默认）| `on`

当您选择 **Enable status
output** 参数时，模块将配置一个输出端口
**Status**。该端口输出 SPI
状态消息。

### **Enable blocking mode** — 启用 SPI 阻塞模式 `off`（默认）| `on`

当选择此选项时，算法会等待数据发送完成后再继续处理。

### 高级

### **Data bits** — SPI 传输中的位数 `8`（默认）| 5 到 32

每个发送或接收字符的长度（以位为单位）。例如，
如果您选择 `8`，则使用 SPI 可以发送的最大值为
28–1。如果您发送
大于此值的数据，缓冲区将溢出。此参数对于发送和接收模块必须
相同。

### **Chip select calling method** — 选择 SPI 外设设备的方法 `Provided by the SPI peripheral`（默认）| `Explicit GPIO calls`

SPI 控制器使用这些方法来选择 SPI 外设
设备：

- `Provided by the SPI peripheral` —
  SPI 控制器使用 SPI 外设提供的引脚。
  外设的选择和取消选择由 SPI
  外设处理。
- `Explicit GPIO calls` — SPI
  控制器使用通用输入/输出引脚而不是
  SPI 外设的 STE 引脚来选择/取消选择 SPI
  外设设备。SPI Transmit 模块
  在发送数据之前使用 GPIO 引脚选择外设。
  要取消选择外设，您必须将 SPI Receive 模块与 SPI Transmit 模块一起使用。仅在
  控制器模式下使用此选项。选择
  **Enable blocking mode** 选项以
  确保在取消选择外设之前 SPI 传输已完成。

### **Chip select pin polarity** — SPI 片选引脚极性 `Active low`（默认）| `Active high`

片选引脚用于选择 SPI
外设设备所支持的逻辑电平。

- `Active low` — 设备在逻辑低电平时
  使能。当 SPI 外设设备的片选引脚设置为低电平时，该设备
  使能。
- `Active high` — 设备在逻辑高电平时
  使能。当 SPI 外设设备的片选引脚设置为高电平时，该设备
  使能。

#### 依赖关系

此选项仅在 **Chip select calling
method** 设置为 `Explicit GPIO
calls` 时出现。

### **Chip select port name** — SPI 片选端口名称 `GPIOA`（默认）| `GPIOB` | `GPIOC`

选择用作 SPI 片选的通用端口名称。

#### 依赖关系

此选项仅在 **Chip select calling
method** 设置为 `Explicit GPIO
calls` 时出现。

### **Chip select pin** — SPI 外设选择引脚 `0`（默认）| 正整数标量

用作 SPI 片选的通用输入/输出引脚。

#### 依赖关系

此选项仅在 **Chip select calling
method** 设置为 `Explicit GPIO
calls` 时出现。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32WBxx Based Boards

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

通过目标上的串行外设接口 (SPI) 发送数据

SPI Transmit 模块接受 [Nx1] 或 [1xN] 数组形式的
`uint8`、`uint16` 或 `uint32`
数据类型的值。

SPI Transmit 模块支持处理器与外部外设或其他
控制器之间的同步串行外设
输入/输出端口通信。该模块可以在外设模式或控制器模式下运行。在控制器
模式下，SPI\_MOSI 引脚发送数据，SPI\_MISO 引脚接收数据。当
选择控制器模式时，SPI 通过发送串行
时钟信号 (SPICLK) 来启动数据传输，该信号用于整个串行通信链路。数据
传输与此 SPICLK 同步，这使得控制器和外设
能够同时发送和接收数据。

SPI Transmit 模块将数据写入发送缓冲区，数据
被发送到 SPI 设备。在控制器模式下，SPI Transmit
模块通过将数据写入 SPI 发送缓冲区来启动 SPI 传输。SPI
Receive 模块必须与 SPI Transmit 模块一起使用，以读取
接收缓冲区中接收到的数据。在外设模式下，SPI Receive 模块
用于读取接收缓冲区中的数据，该数据是从控制器接收的。
然后，使用 SPI Transmit
模块将数据写入发送缓冲区。从发送缓冲区，数据被发送到控制器。

采样率继承自输入端口。支持的数据类型为
`uint8`、`uint16` 和
`uint32`。

SPI 发送中断通过导航到 **Configuration Parameters** > **Hardware Implementation** > **Target hardware resources** 为特定硬件板进行配置。

SPI Module 在 STM32CubeMX 项目中进行配置。

- 启动 STM32CubeMX 项目。有关更多信息，请参阅 Configure STM32 Processor-Based Boards using STM32CubeMX with Simulink。
- 导航到 **Pinout & Configuration** > **Connectivity** > **SPI#**

验证这些设置是否满足您的应用需求。

**注意**

以下是 SPI 模块的限制：

- 发送到发送模块的数据字节数应
  小于 FIFO 长度。
- 在 Monitor & Tune 中运行 SPI Controller Transfer 模块时，
  您可能会观察到垃圾数据。要解决此问题，请重新连接并启动
  Monitor & Tune。
- 如果在模型中使用 SPI Controller Transfer 模块，请勿对同一模块使用
  SPI Transmit 和 SPI Receive 模块。
- 避免在多个任务中使用相同的 SPI 模块，这可能导致
  问题。
- SPI 模块不支持 STM32CubeMX 文件中 SPI 模式配置的
  Master Receive Only、Slave Receive Only、
  Master Transmit Only 和 Slave Transmit only。
