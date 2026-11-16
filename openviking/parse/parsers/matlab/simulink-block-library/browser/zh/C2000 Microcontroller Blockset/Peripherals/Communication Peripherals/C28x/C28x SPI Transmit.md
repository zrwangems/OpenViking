---
type: simulink-block
title: 'C28x SPI Transmit'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Communication Peripherals / C28x'
documentation_page: 'c28xspitransmit'
documentation_source_path: 'ref/c28xspitransmit.html'
language: zh-CN
chinese_source: worker-translation
---

# C28x SPI Transmit

## 端口

### 输入

### **Tx** — SPI 发送数据向量

通过 SPI 接口写入设备的数据。

**数据类型：** `uint16`

### 输出

### **Status** — SPI 发送状态 0 | 1 | 2

SPI 数据传输的状态。错误状态值表示：

- 0 — 无错误。
- 1 — 模块发送数据时发生超时。
- 2 — 发送的数据包含错误。

#### 依赖关系

仅当未选择 **Enable blocking mode** 时，此端口才会出现。

**数据类型：** `uint16`

## 参数

### 主要

### **SPI module** — 要写入数据的 SPI 模块 `SPI_A`（默认） | `SPI_B` | `SPI_C` | `SPI_D`

SPI 外设设备连接到的 SPI 模块。每个处理器的模块数量不同。

### **Clock polarity** — SPI 时钟极性 `Rising_edge`（默认） | `Falling_edge`

用于 SPI 通信模式的时钟极性。对于发送和接收模块，此参数必须相同。

### **Clock phase** — SPI 时钟相位 `No_delay`（默认） | `Delay_half_cycle`

用于 SPI 通信模式的时钟相位。对于发送和接收模块，此参数必须相同。

### **Enable blocking mode** — SPI 阻塞模式启用 `off`（默认） | `on`

选择此选项后，算法会等待数据发送完成，然后继续处理。

### 高级

### **Data bits** — SPI 传输中的位数 `8`（默认） | [1 16] 中的整数

每个发送或接收字符的位长度。例如，如果选择 `8`，使用 SPI 可发送的最大值为 28–1。如果发送的数据大于此值，缓冲区将溢出。对于发送和接收模块，此参数必须相同。

### **Chip select calling method** — 选择 SPI 外设设备的方法 `Provided by the SPI peripheral`（默认） | `Explicit GPIO calls`

SPI 控制器使用以下方法来选择 SPI 外设设备：

- `Provided by the SPI peripheral` —
  SPI 控制器使用 **Hardware Implementation** > **Target hardware resources** > **SPI** 中提供的 STE 引脚分配来选择外设设备。外设选择
  和取消选择由 SPI 外设处理。
- `Explicit GPIO calls` — SPI
  控制器使用通用输入/输出引脚，而不是 SPI 外设的 STE 引脚来选择/取消选择 SPI
  外设设备。SPI Transmit 模块
  在发送数据之前使用 GPIO 引脚选择外设。
  要取消选择外设，必须将 C28x SPI Receive 模块与 SPI Transmit 模块一起使用。仅在控制器模式下使用
  此选项。选择
  **Enable blocking mode** 选项，以确保在
  取消选择外设之前 SPI 传输已完成。

### **Chip select pin polarity** — SPI 片选引脚极性 `Active low`（默认） | `Active high`

片选引脚用于选择 SPI 外设设备所支持的电平逻辑。

- `Active low` — 设备在逻辑低电平时启用。当外设选择引脚设置为低电平时，SPI 外设设备被启用。
- `Active high` — 设备在逻辑高电平时启用。当外设选择引脚设置为高电平时，SPI 外设设备被启用。

#### 依赖关系

仅当 **Chip select calling method** 设置为 `Explicit GPIO calls` 时，此选项才会出现。

### **Chip select pin** — SPI 外设选择引脚 `0`（默认） | 正整数标量

用作 SPI 外设选择的通用输入/输出引脚。

#### 依赖关系

仅当 **Chip select calling method** 设置为 `Explicit GPIO calls` 时，此选项才会出现。

## 所属库

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C281x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32WBxx Based Boards

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

通过目标上的串行外设接口 (SPI) 发送数据

SPI Transmit 模块支持处理器与外部外设或其他控制器之间的同步串行外设输入/输出端口通信。该模块可在 外设 或 控制器 模式下运行。在控制器模式下，SPISIMO 引脚发送数据，SPISOMI 引脚接收数据。选择控制器模式时，SPI 通过发送串行时钟信号 (SPICLK) 启动数据传输，该信号用于整个串行通信链路。数据传输同步到此 SPICLK，这使控制器和外设能够同时发送和接收数据。时钟的最大频率为处理器时钟频率的四分之一。

SPI Transmit 模块将数据写入发送缓冲区，随后数据被发送到 SPI 设备。在控制器模式下，SPI Transmit 模块通过将数据写入 SPI 发送缓冲区来启动 SPI 传输。必须将 C28x SPI Receive 模块与 SPI Transmit 模块一起使用，以读取接收缓冲区中接收到的数据。在外设模式下，SPI Receive 模块用于读取接收缓冲区中的数据，该数据是从控制器接收的。然后，使用 SPI Transmit 模块将数据写入发送缓冲区。数据从发送缓冲区发送到控制器。

**注意**

要使用同一个 SPI 模块与多个外设通信，请使用具有相同模块的多个 SPI 模块实例，并为每个实例配置唯一的片选。

采样率继承自输入端口。支持的数据类型为 `uint16`。

配置 SPI 发送中断时，发送 FIFO 中断标志在 step 函数中清除，而不是在中断服务程序中清除。将数据放入发送缓冲区后，发送 FIFO 中断被置位，并且先前的发送中断 FIFO 标志被清除。通过导航到 **Hardware Implementation** > **Target hardware resources**，为特定硬件板配置 SPI 模块。验证这些设置是否满足您的应用要求。
