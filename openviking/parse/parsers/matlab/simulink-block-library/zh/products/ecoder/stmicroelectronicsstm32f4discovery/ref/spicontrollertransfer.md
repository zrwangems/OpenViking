---
type: simulink-block
title: 'SPI Controller Transfer'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Connectivity Peripherals / Communication'
documentation_page: 'spicontrollertransfer'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/spicontrollertransfer.html'
language: zh-CN
chinese_source: worker-translation
---

# SPI Controller Transfer

## 端口

### 输入

### **Tx** — 写入 SPI 外设设备寄存器的数据，串行数据输出 (SDO) 向量

模块通过 SPI 接口写入外设设备寄存器的数据。

**数据类型：** `uint8` | `uint16` | `uint32`

### 输出

### **Rx** — 从 SPI 外设设备寄存器读取的数据，串行数据输入 (SDI) 向量

模块通过 SPI 接口从外设设备寄存器读取的数据。

**数据类型：** `uint8` | `uint16` | `uint32`

## 参数

### 主要

### **SPI 模块** — 用于写入和读取数据的 SPI 模块 `SPI1`（默认） | `SPI2` | `SPI3` | `SPI4` | `SPI5` | `SPI6`

SPI 外设设备所连接的 SPI 外设模块。每个处理器具有不同数量的模块。

### **时钟极性** — SPI 时钟极性 `Low`（默认） | `High`

SPI 通信模式的时钟极性 (CPOL)。

### **时钟相位** — SPI 时钟相位 `1 Edge`（默认） | `2 Edge`

SPI 通信模式的时钟相位 (CPHA)。

### **启用寄存器地址** — 启用 SPI 寄存器地址 `on`（默认） | `off`

启用 **寄存器地址** 参数。

### **寄存器地址** — SPI 寄存器地址 `0`（默认） | 正整数标量 | 正整数向量

模块从中读取数据的外设寄存器地址。

**注意**

正整数向量指定为 `[2 0 32]`（用于 Write Data to Memory）和 `[3 0 32]`（用于 Read Data from Memory）。有关详细信息，请参阅示例 Using SPI to Read and Write Data to SPI EEPROM (C2000 Microcontroller Blockset)。

#### 依赖关系

仅当您选择 **启用寄存器地址** 时，此参数才会出现。

### 高级

### **数据位数** — SPI 传输中的位数 `4`（默认） | 范围 [1 32] 内的整数

每个发送或接收字符的长度（以位为单位），指定为 [1 32] 中的整数。例如，如果选择 `8`，则使用 SPI 可传输的最大值为 `2^8 – 1`。如果发送大于此值的数据值，则缓冲区溢出。

### **芯片选择调用方法** — 选择 SPI 外设设备的方法 `Provided by the SPI peripheral`（默认） | `Explicit GPIO calls`

SPI 控制器使用这些方法来选择 SPI 外设设备。

- `Provided by the SPI peripheral` — SPI 控制器使用由 SPI 外设提供的引脚。外设选择和取消选择由 SPI 外设处理。
- `Explicit GPIO calls` — SPI 控制器显式使用通用输入/输出引脚来选择/取消选择 SPI 外设设备。SPI Controller Transfer 模块在发送数据之前选择外设，并在使用 GPIO 引脚接收数据后取消选择外设。

### **芯片选择引脚极性** — SPI 外设选择引脚极性 `Active low`（默认） | `Active high`

芯片选择引脚为选择 SPI 外设设备所支持的电平。

- `Active low` — 设备在逻辑低电平时启用。当 SPI 外设设备的芯片选择引脚设置为低电平时，该设备启用。
- `Active high` — 设备在逻辑高电平时启用。当 SPI 外设设备的芯片选择引脚设置为高电平时，该设备启用。

#### 依赖关系

仅当 **芯片选择调用方法** 设置为 `Explicit GPIO calls` 时，此参数才会出现。

### **芯片选择端口名称** — SPI 芯片选择端口名称 `GPIOA`（默认） | `GPIOB` | `GPIOC`

选择用作 SPI 芯片选择的通用端口名称。

#### 依赖关系

仅当 **芯片选择调用方法** 设置为 `Explicit GPIO calls` 时，此选项才会出现。

### **芯片选择引脚** — SPI 外设选择引脚 `1`（默认） | 正整数标量

用作 SPI 芯片选择的通用输入/输出引脚。

#### 依赖关系

仅当 **芯片选择调用方法** 设置为 `Explicit GPIO calls` 时，此参数才会出现。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

向 SPI 外设设备写入数据并从中读取数据

SPI Controller Transfer 模块接受一个 1-D 数组，并输出一个大小相同、数据类型为 `uint8`、`uint16` 或 `uint32` 的数组

SPI Controller Transfer 模块通过串行外设接口 (SPI) 向外设设备写入数据并从中读取数据。该模块以控制器模式运行。该模块输出一个与输入值大小和数据类型相同的数组。您可以将此模块与 Byte Pack 和 Byte Unpack 模块一起使用，以进行异构数据类型传输。

使用此模块，您可以访问 SPI 设备以测量温度和压力等量。

通过导航到 **Configuration Parameters** > **Hardware Implementation** > **Target hardware resources**，可为特定硬件板配置 SPI 接收中断。

SPI 模块在 STM32CubeMX 项目中配置。

- 启动 STM32CubeMX 项目。有关详细信息，请参阅 Configure STM32 Processor-Based Boards using STM32CubeMX with Simulink。
- 导航到 **Pinout & Configuration** > **Connectivity** > **SPI#**

验证这些设置是否满足您的应用需求。

**注意**

以下是 SPI 模块的限制：

- 发送到发送模块的数据字节数应小于 FIFO 长度。
- 在 Monitor & Tune 中运行 SPI Controller Transfer 模块时，您可能会观察到垃圾数据。要解决此问题，请重新连接并启动 Monitor & Tune。
- 如果模型中使用 SPI Controller Transfer 模块，请勿对同一模块使用 SPI Transmit 和 SPI Receive 模块。
- 避免在多个任务中使用相同的 SPI 模块，这可能会导致问题。
- SPI 模块在 STM32CubeMX 文件中的 SPI 模式配置下不支持 Master Receive Only、Slave Receive Only、Master Transmit Only 和 Slave Transmit only。
