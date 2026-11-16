---
type: simulink-block
title: 'C28x SPI Controller Transfer'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Communication Peripherals / C28x'
documentation_page: 'c28xspicontrollertransfer'
documentation_source_path: 'ref/c28xspicontrollertransfer.html'
language: zh-CN
chinese_source: official
---

# C28x SPI Controller Transfer

## 端口

### 输入

### **Tx** — 写入 SPI 外围设备 (MOSI) 寄存器的数据 向量

该模块通过 SPI 接口向外围设备的寄存器写入数据。

**数据类型:** `uint16`
### 输出

### **Rx** — 从 SPI 外围设备 (MISO) 寄存器读取的数据 向量

该模块通过 SPI 接口从外围设备的寄存器读取数据。

**数据类型:** `uint16`

## 参数

### 主要

### **SPI 模块** — SPI 模块用于写入和读取数据 **SPI\_A** (默认) | **SPI\_B** | **SPI\_C** | **SPI\_D**

SPI 外设模块，SPI 外设设备连接到该模块。每个处理器所包含的模块数量都不同。

### **时钟极性** — SPI 时钟极性 **Rising\_edge** (默认) | **Falling\_edge**

SPI 通信模式的时钟极性 (CPOL)。

### **时钟相位** — SPI 时钟相位 **No\_delay** (默认) | **Delay\_half\_cycle**

SPI 通信模式的时钟相位 (CPHA)。

### **启用寄存器地址** — 启用 SPI 寄存器地址 `on` (默认) | `off`

启用**寄存器地址**参数。

### **寄存器地址** — SPI 寄存器地址 `0` (默认) | 正整数标量 | 正整数向量

该模块从中读取数据的外设寄存器地址。

例如，如果我们考虑 使用 SPI 对 SPI EEPROM 进行数据读写 示例，要通过地址 `32 (0x0020)` 和写入命令 2 写入 EEPROM 存储器，则条目可以是 `[2 0 32]`，它对应于写入命令后跟 16 位地址和输入端口的数据。

这里地址被拆分为 `0x00 (0)` 和 `0x20 (32)` 两个 8 位数字，并输入到寄存器地址中。将其拆分为两个 8 位数字的原因是 `Advanced` 选项卡中 `Data bits` 参数的设置。由于此值设置为 8 位，因此向量格式中的数据不应被视为超过 8 位。如果选择参数为 `16`，则 `0` 和 `32` 对应于 32 位地址 `(0x00000020)` 而不是 16 位地址。

#### 依赖关系

此参数仅在选择 **Enable register address** 时显示。

### 高级

### **数据位** — SPI 传输中的位数 `8` (默认) | [1 16] 范围内的整数

每个已发送或已接收字符的长度（以比特为单位），在 [1 16] 中指定为整数。例如，如果您选择 `8`，则使用 SPI 可以传输的最大值是 28 – 1。如果发送的数据值大于此值，则缓冲区溢出。

### **片选调用方法** — 选择 SPI 外围设备的方法 **由 SPI 外设提供** (默认) | **显式 GPIO 调用**

SPI 控制器使用这些方法来选择 SPI 外围设备。

- **Provided by the SPI peripheral** - SPI 控制器使用 **硬件实现** > **Target Hardware Resources** > **SPI** 中的 **STE pin assignment** 参数来选择外设。外设的选择和取消选择由 SPI 外设处理。
- **Explicit GPIO calls** - SPI 控制器明确使用通用输入/输出引脚来选择/取消选择 SPI 外围设备。SPI controller Transfer 模块在数据传输之前选择外设，并在使用 GPIO 引脚接收数据之后取消选择外设。

### **片选引脚极性** — SPI 外设选择引脚极性 **低电平有效** (默认) | **高电平有效**

外设选择引脚支持的逻辑电平，用于选择 SPI 外设设备。

- **ActiveLow** - 设备在逻辑低电平时启用。当 SPI 外设选择引脚设置为低电平时，该 SPI 外设将被启用。
- **Active high** - 设备在逻辑高电平时启用。当 SPI 外设选择引脚设置为高电平时，该 SPI 外设将被启用。

#### 依赖关系

只有当**片选调用方法**设置为 **Explicit GPIO calls** 时，此参数才会出现。

### **片选引脚** — SPI 外设选择引脚 `1` (默认) | 正整数标量

用作 SPI 外设选择器的通用输入/输出引脚。

#### 依赖关系

只有当**片选调用方法**设置为 **Explicit GPIO calls** 时，此参数才会出现。

## 所属库

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C281x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32WBxx Based Boards Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common Simulink Support Package for Raspberry Pi Hardware / Communication

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2017b 中推出**

## 描述

向 SPI 外设写入数据和从 SPI 外设读取数据

C28x SPI Controller Transfer 模块通过串行外设接口 (SPI) 向外围设备写入数据和从外围设备读取数据。该模块以控制器模式运行。该模块输出一个与输入值大小和数据类型相同的数组。您可以将此块与 Byte Pack 和 Byte Unpack 模块一起使用，以进行异构数据类型传输。

**注意**

要使用同一个 SPI 模块与多个外设通信，请使用同一个模块的多个 SPI 模块实例，并为每个实例配置唯一的片选信号。

通过导航至 **硬件实现** > **Target hardware resources**，为特定硬件板配置 SPI 模块。请确认这些设置符合您的应用程序要求。

使用此模块，您可以访问 SPI 设备来测量温度和压力等量。
