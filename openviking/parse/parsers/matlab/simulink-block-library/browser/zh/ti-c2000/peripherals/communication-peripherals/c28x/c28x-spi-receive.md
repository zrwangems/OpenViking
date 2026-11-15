---
type: simulink-block
title: 'C28x SPI Receive'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Communication Peripherals / C28x'
documentation_page: 'c28xspireceive'
documentation_source_path: 'ref/c28xspireceive.html'
language: zh-CN
chinese_source: official
---

# C28x SPI Receive

## 端口

### 输出

### **Rx** — SPI 接收数据 向量

通过 SPI 接口从设备读取数据。

**数据类型:** `uint16`

### **Status** — SPI 接收状态 `0` | `1` | `2`

数据接收状态。错误状态值表示：

- 0 - 无错误。
- 1 - 由于溢出导致数据丢失。
- 2 - 数据未准备就绪。该模块在等待接收数据时发生超时。

#### 依赖关系

仅当未选择**启用阻塞模式**时才会显示此端口。

**数据类型:** `uint16`

## 参数

### 主要

### **SPI 模块** — 用于读取数据的 SPI 模块 **SPI\_A** (默认) | **SPI\_B** | **SPI\_C** | **SPI\_D**

SPI 模块，SPI 外设设备连接到该模块。每个处理器所包含的模块数量都不同。

### **时钟极性** — SPI 时钟极性 **Rising\_edge** (默认) | **Falling\_edge**

SPI 通信模式使用的时钟极性。发送模块和接收模块的此参数必须相同。

### **时钟相位** — SPI 时钟相位 **No\_delay** (默认) | **Delay\_half\_cycle**

SPI 通信模式使用的时钟相位。发送模块和接收模块的此参数必须相同。

### **输出数据长度** — SPI 输出数据长度 `1` (默认) | 正整数

接收到的数据是类型为 `uint16` 的向量，数据长度按此参数指定（不是字节）。

### **启用阻塞模式** — 启用 SPI 阻塞模式 `off` (默认) | `on`

选择此选项后，算法将等待接收到数据后再继续处理。

### **采样时间** — SPI 采样时间选择 `0.1` (默认) | `–1` | 标量

以秒为单位记录该模块的采样时间。要异步执行此模块，请将此参数设置为 `-1`。

### 高级

### **数据位** — SPI 传输中的位数 `8` (默认) | [1 16] 范围内的整数

每个已发送或已接收字符的长度（以比特为单位）。例如，如果您选择 `8`，则使用 SPI 可以传输的最大值是 28–1。如果发送的数据大于此值，则缓冲区溢出。发送模块和接收模块的此参数必须相同。

### **片选调用方法** — 选择 SPI 外围设备的方法 **由 SPI 外设提供** (默认) | **显式 GPIO 调用**

SPI 控制器使用以下方法选择 SPI 外围设备：

- **Provided by the SPI peripheral** - SPI 控制器使用 **硬件实现** > **Target hardware resources** > **SPI** 中提供的 STE 引脚分配来选择外设。外设的选择和取消选择由 SPI 外设处理。
- **Explicit GPIO calls** - SPI 控制器使用通用输入/输出引脚而不是 SPI 外设的 STE 引脚来选择/取消选择 SPI 外设设备。SPI Receive 模块在接收到数据后，使用 GPIO 引脚取消选择外设。要选择外设，必须将 C28x SPI Transmit 模块与 SPI Receive 模块一起使用。仅在控制器模式下使用此选项。选择**启用阻塞模式**选项，以确保在取消选择外设之前 SPI 传输已完成。

### **片选引脚极性** — SPI 外设选择引脚极性 **低电平有效** (默认) | **高电平有效**

外设选择引脚支持的逻辑电平，用于选择 SPI 外设设备。

- **ActiveLow** - 设备在逻辑低电平时启用。当 SPI 外设选择引脚设置为低电平时，该 SPI 外设将被启用。
- **Active high** - 设备在逻辑高电平时启用。当 SPI 外设选择引脚设置为高电平时，该 SPI 外设将被启用。

#### 依赖关系

仅当**片选调用方法**设置为 **Explicit GPIO calls** 时，才会显示此选项。

### **片选引脚** — SPI 外设选择引脚 `0` (默认) | 正整数标量

通用输入/输出引脚，用作 SPI 的外设选择引脚。

#### 依赖关系

仅当**片选调用方法**设置为 **Explicit GPIO calls** 时，才会显示此选项。

## 所属库

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C281x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32WBxx Based Boards

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2017b 中推出**

## 描述

通过目标设备上的串行外设接口 (SPI) 接收数据

SPI Receive 模块支持处理器与外部外设或其他控制器之间的同步串行外设输入/输出端口通信。该模块既可以运行在外设模式下，也可以运行在控制器模式下。在控制器模式下，SPISIMO 引脚发送数据，SPISOMI 引脚接收数据。选择控制器模式时，SPI 通过发送串行时钟信号 (SPICLK) 来启动数据传输，该信号用于整个串行通信链路。数据传输与此 SPICLK 同步，这使得控制器和外设能够同时发送和接收数据。时钟的最大频率是处理器时钟频率的四分之一。

SPI 设备接收数据并将数据放入接收缓冲区。SPI Receive 模块从接收缓冲区读取数据。在控制器模式下，C28x SPI Transmit 模块通过向发送缓冲区写入数据来启动 SPI 传输。然后，接收缓冲区中接收到的数据由 SPI Receive 模块读取。在外设模式下，SPI Receive 模块用于读取从控制器接收的接收缓冲区中的数据。然后，使用 SPI Transmit 模块将数据写入发送缓冲区。数据从发送缓冲区发送到控制器。

**注意**

要使用同一个 SPI 模块与多个外设通信，请使用同一个模块的多个 SPI 模块实例，并为每个实例配置唯一的片选信号。

通过导航至 **硬件实现** > **Target hardware resources** 为特定硬件板配置 SPI 模块。请确认这些设置符合您的应用程序要求。
