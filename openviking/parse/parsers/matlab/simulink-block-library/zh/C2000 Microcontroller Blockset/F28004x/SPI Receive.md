---
type: simulink-block
title: 'SPI Receive'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2802x'
documentation_page: 'spireceive'
documentation_source_path: '../ecoder/stmicroelectronicsstm32f4discovery/ref/spireceive.html'
language: zh-CN
chinese_source: worker-translation
---

# SPI Receive

## 端口

### 输出

### **Rx** — SPI 接收数据向量

通过 SPI 接口从设备读取的数据。

**数据类型：** `uint8` | `uint16` | `uint32`

### **Status** — SPI 接收状态 `0` | `1` | `2`

数据接收状态。错误状态值表示：

- 0 — 无错误。
- 1 — 由于溢出发生数据丢失。
- 2 — 数据未就绪。模块在等待接收数据时发生超时。

#### 依赖关系

要启用此端口，请选择 **Enable status output** 参数。

**数据类型：** `uint8` | `uint16` | `uint32`

## 参数

### 主

### **SPI module** — 用于读取数据的 SPI 模块 `SPI1`（默认）| `SPI2` | `SPI3` | `SPI4` | `SPI5` | `SPI6`

SPI 外设设备连接到的 SPI 模块。每个处理器具有不同数量的模块。

### **Clock polarity** — SPI 时钟极性 `Low`（默认）| `High`

用于 SPI 通信模式的时钟极性。对于发送和接收模块，此参数必须相同。

### **Clock phase** — SPI 时钟相位 `1 Edge`（默认）| `2 Edge`

用于 SPI 通信模式的时钟相位。对于发送和接收模块，此参数必须相同。

### **Output data length** — SPI 输出数据长度 `1`（默认）| 正整数

接收的数据是 `uint8`、`uint16` 或 `uint32` 类型的向量，数据长度如本参数中所指定（不是字节）。

### **Enable status output** — 启用 SPI 状态模式 `off`（默认）| `on`

当您选择 **Enable status output** 参数时，模块配置一个输出端口 **Status**。该端口输出 SPI 状态消息。

### **Enable blocking mode** — 启用 SPI 阻塞模式 `off`（默认）| `on`

选择此选项后，算法会等待直到接收到数据，然后继续处理。

### **Sample time** — SPI 采样时间选择 `–1`（默认）| `0.1` | 标量

模块的采样时间，以 seconds 为单位。要异步执行此模块，请将此参数设置为 `-1`。

### 高级

### **Data bits** — SPI 传输中的 bits 数量 `4`（默认）| 5 到 32

每个发送或接收字符的长度，以 bits 为单位。例如，如果选择 `8`，使用 SPI 可以传输的最大值为 28–1。如果发送的数据大于此值，缓冲区将溢出。对于发送和接收模块，此参数必须相同。

### **Chip select calling method** — 选择 SPI 外设设备的方法 `Provided by the SPI peripheral`（默认）| `Explicit GPIO calls`

SPI 控制器使用以下方法来选择 SPI 外设设备：

- `Provided by the SPI peripheral` — SPI 控制器使用由 SPI 外设提供的引脚。外设选择和取消选择由 SPI 外设处理。
- `Explicit GPIO calls` — SPI 控制器使用通用输入/输出引脚而不是 SPI 外设的 STE 引脚来选择/取消选择 SPI 外设设备。SPI Receive 模块在接收数据后使用 GPIO 引脚取消选择外设。要选择外设，必须将 SPI Transmit 模块与 SPI Receive 模块一起使用。仅在控制器模式下使用此选项。选择 **Enable blocking mode** 选项以确保在取消选择外设之前 SPI 传输已完成。

### **Chip select pin polarity** — SPI 芯片选择引脚极性 `Active low`（默认）| `Active high`

芯片选择引脚支持用于选择 SPI 外设设备的逻辑电平。

- `Active low` — 设备在逻辑低电平时使能。当 SPI 外设设备的芯片选择引脚设置为低电平时，该 SPI 外设设备被使能。
- `Active high` — 设备在逻辑高电平时使能。当 SPI 外设设备的芯片选择引脚设置为高电平时，该 SPI 外设设备被使能。

#### 依赖关系

仅当 **Chip select calling method** 设置为 `Explicit GPIO calls` 时，此选项才会出现。

### **Chip select port name** — SPI 芯片选择端口名称 `GPIOA`（默认）| `GPIOB` | `GPIOC`

选择用作 SPI 芯片选择的通用端口名称。

#### 依赖关系

仅当 **Chip select calling method** 设置为 `Explicit GPIO calls` 时，此选项才会出现。

### **Chip select pin** — SPI 芯片选择引脚 `0`（默认）| 正整数标量

用作 SPI 外设选择的通用输入/输出引脚。

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

在目标上通过串行外设接口 (SPI) 接收数据

SPI Receive 模块将接收到的值输出为 `uint8`、`uint16` 或 `uint32` 数据类型的 `[Nx1]` 数组。

SPI Receive 模块支持处理器与外部外设或其他控制器之间的同步串行外设输入/输出端口通信。该模块可在外设模式或控制器模式下运行。在控制器模式下，SPI\_MOSI 引脚发送数据，SPI\_MISO 引脚接收数据。选择控制器模式时，SPI 通过发送串行时钟信号 (SPICLK) 发起数据传输，该信号用于整个串行通信链路。数据传输同步到该 SPICLK，这使得控制器和外设能够同时发送和接收数据。时钟的最大频率为处理器时钟频率的四分之一。

SPI 设备接收数据并将数据放入接收缓冲区。SPI Receive 模块从接收缓冲区读取数据。在控制器模式下，SPI Transmit 模块通过将数据写入发送缓冲区来发起 SPI 传输。然后，接收缓冲区中接收到的数据由 SPI Receive 模块读取。在外设模式下，SPI Receive 模块用于读取接收缓冲区中的数据，该数据是从控制器接收的。然后，使用 SPI Transmit 模块将数据写入发送缓冲区。数据从发送缓冲区发送到控制器。

通过导航到 **Configuration Parameters** > **Hardware Implementation** > **Target hardware resources**，为特定硬件板配置 SPI 接收中断。

SPI 模块在 STM32CubeMX 项目中配置。

- 启动 STM32CubeMX 项目。有关详细信息，请参阅 Configure STM32 Processor-Based Boards using STM32CubeMX with Simulink。
- 导航到 **Pinout & Configuration** > **Connectivity** > **SPI#**

验证这些设置是否满足您的应用需求。

**注意**

以下是 SPI 模块的限制：

- 发送到发送模块的数据字节数应小于 FIFO 长度。
- 在 Monitor & Tune 中运行 SPI Controller Transfer 模块时，您可能会观察到垃圾数据。要解决此问题，请重新连接并启动 Monitor & Tune。
- 如果在模型中使用 SPI Controller Transfer 模块，请勿对同一模块使用 SPI Transmit 和 SPI Receive 模块。
- 避免在多个任务中使用相同的 SPI 模块，这可能导致问题。
- 对于 STM32CubeMX 文件中的 SPI 模式配置，SPI 模块不支持 Master Receive Only、Slave Receive Only、Master Transmit Only 和 Slave Transmit only。
