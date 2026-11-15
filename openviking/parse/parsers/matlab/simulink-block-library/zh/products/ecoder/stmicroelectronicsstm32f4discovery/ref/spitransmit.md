---
type: simulink-block
title: 'SPI Transmit'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Connectivity Peripherals / Communication'
documentation_page: 'spitransmit'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/spitransmit.html'
language: zh-CN
chinese_source: worker-translation
---

# SPI Transmit

## 端口

### 输入

### **Tx** — SPI Transmit 数据向量

通过 SPI 接口写入设备的数据。

**数据类型：** `uint8` | `uint16` | `uint32`
### 输出

### **Status** — SPI 发送状态 0 | 1 | 2

SPI 数据传输的状态。错误状态值表示：

- 0 — 无错误。
- 1 — 模块发送数据时发生超时。
- 2 — 发送的数据包含错误。

#### 依赖关系

要启用此端口，请选择 **Enable status output** 参数。

**数据类型：** `uint8` | `uint16` | `uint32`

## 参数

### 主要

### **SPI module** — 要写入数据的 SPI 模块 `SPI1` (默认) | `SPI2` | `SPI3` | `SPI4` | `SPI5` | `SPI6`

SPI 外设设备连接到的 SPI 模块。每个处理器具有不同数量的模块。

### **Clock polarity** — SPI 时钟极性 `Low` (默认) | `High`

用于 SPI 通信模式的时钟极性。对于发送和接收模块，此参数必须相同。

### **Clock phase** — SPI 时钟相位 `1 Edge` (默认) | `2 Edge`

用于 SPI 通信模式的时钟相位。对于发送和接收模块，此参数必须相同。

### **Enable status output** — 启用 SPI 状态模式 `off` (默认) | `on`

选择 **Enable status output** 参数后，该模块会配置一个输出端口 **Status**。该端口输出 SPI 状态消息。

### **Enable blocking mode** — 启用 SPI 阻塞模式 `off` (默认) | `on`

选择此选项后，算法会等待数据发送完成，然后再继续处理。

### 高级

### **Data bits** — SPI 传输中的位数 `8` (默认) | 5 到 32

每个发送或接收字符的长度（以位为单位）。例如，如果选择 `8`，使用 SPI 可传输的最大值为 2^8–1。如果发送的数据大于此值，缓冲区会溢出。对于发送和接收模块，此参数必须相同。

### **Chip select calling method** — 选择 SPI 外设设备的方法 `Provided by the SPI peripheral` (默认) | `Explicit GPIO calls`

SPI 控制器使用以下方法来选择 SPI 外设设备：

- `Provided by the SPI peripheral` — SPI 控制器使用 SPI 外设提供的引脚。外设选择和取消选择由 SPI 外设处理。
- `Explicit GPIO calls` — SPI 控制器使用通用输入/输出引脚，而不是 SPI 外设的 STE 引脚，来选择/取消选择 SPI 外设设备。SPI Transmit 模块在发送数据之前使用 GPIO 引脚选择外设。要取消选择外设，必须将 SPI Receive 模块与 SPI Transmit 模块一起使用。仅在控制器模式下使用此选项。选择 **Enable blocking mode** 选项以确保在取消选择外设之前 SPI 传输已完成。

### **Chip select pin polarity** — SPI 片选引脚极性 `Active low` (默认) | `Active high`

选择 SPI 外设设备时片选引脚支持的电平逻辑。

- `Active low` — 设备在逻辑低电平时启用。当 SPI 外设设备的片选引脚设置为低电平时，该设备启用。
- `Active high` — 设备在逻辑高电平时启用。当 SPI 外设设备的片选引脚设置为高电平时，该设备启用。

#### 依赖关系

仅当 **Chip select calling method** 设置为 `Explicit GPIO calls` 时，此选项才会出现。

### **Chip select port name** — SPI 片选端口名称 `GPIOA` (默认) | `GPIOB` | `GPIOC`

选择用作 SPI 片选的通用端口名称。

#### 依赖关系

仅当 **Chip select calling method** 设置为 `Explicit GPIO calls` 时，此选项才会出现。

### **Chip select pin** — SPI 外设选择引脚 `0` (默认) | 正整数标量

用作 SPI 片选的通用输入/输出引脚。

#### 依赖关系

仅当 **Chip select calling method** 设置为 `Explicit GPIO calls` 时，此选项才会出现。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32WBxx Based Boards

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

在目标上通过串行外设接口 (SPI) 发送数据

SPI Transmit 模块接受值为 [Nx1] 或 [1xN] 数组，数据类型为 `uint8`、`uint16` 或 `uint32`。

SPI Transmit 模块支持处理器与外部外设或其他控制器之间的同步串行外设输入/输出端口通信。该模块可以运行在外设模式或控制器模式下。在控制器模式下，SPI\_MOSI 引脚发送数据，SPI\_MISO 引脚接收数据。当选择控制器模式时，SPI 通过发送串行时钟信号 (SPICLK) 来启动数据传输，该信号用于整个串行通信链路。数据传输同步到该 SPICLK，使控制器和外设能够同时发送和接收数据。

SPI Transmit 模块将数据写入发送缓冲区，然后数据被发送到 SPI 设备。在控制器模式下，SPI Transmit 模块通过将数据写入 SPI 发送缓冲区来启动 SPI 传输。必须将 SPI Receive 模块与 SPI Transmit 模块一起使用，以读取接收缓冲区中接收到的数据。在外设模式下，使用 SPI Receive 模块读取接收缓冲区中从控制器接收到的数据。然后，使用 SPI Transmit 模块将数据写入发送缓冲区。数据从发送缓冲区发送到控制器。

采样率继承自输入端口。支持的数据类型为 `uint8`、`uint16` 和 `uint32`。

通过导航到 **配置参数** > **硬件实现** > **目标硬件资源**，为特定硬件板配置 SPI 发送中断。

SPI 模块在 STM32CubeMX 项目中配置。

- 启动 STM32CubeMX 项目。有关详细信息，请参阅使用 STM32CubeMX 与 Simulink 配置基于 STM32 处理器的板。
- 导航到 **引脚排列与配置** > **连接** > **SPI#**

验证这些设置是否满足您的应用需求。

**注意**

以下是 SPI 模块的限制：

- 发送到发送模块的数据字节数应小于 FIFO 长度。
- 在监视和调优中运行 SPI Controller Transfer 模块时，您可能会观察到垃圾数据。要解决此问题，请重新连接并启动监视和调优。
- 如果模型中使用了 SPI Controller Transfer 模块，则不要对同一模块使用 SPI Transmit 和 SPI Receive 模块。
- 避免在多个任务中使用相同的 SPI 模块，这可能会导致问题。
- 对于 STM32CubeMX 文件中的 SPI 模式配置，SPI 模块不支持 Master Receive Only、Slave Receive Only、Master Transmit Only 和 Slave Transmit only。
