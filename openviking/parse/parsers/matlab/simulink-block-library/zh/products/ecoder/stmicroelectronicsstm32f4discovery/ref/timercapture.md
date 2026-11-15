---
type: simulink-block
title: 'Timer Capture'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Timer Peripherals'
documentation_page: 'timercapture'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/timercapture.html'
language: zh-CN
chinese_source: worker-translation
---

# Timer Capture

## 端口

### 输出

### **CH#** — 通道端口 `scalar`

通道端口输出对应所选通道的捕获比较寄存器值。

**数据类型：** `uint16` | `uint32`

### **Status** — 溢出状态 `scalar`

输出在读取捕获比较寄存器期间是否发生溢出。

- `1` - 发生溢出
- `0` - 无溢出

#### 依赖项

要启用此端口，请选择 **Output status** 参数。

**数据类型：** `uint8`

### **Dir** — 计数器方向输出 `scalar`

模块输出计数器的当前方向，如下之一：

- `0` - 向上计数器
- `1` - 向下计数器

#### 依赖项

要启用此端口，请选择 **Enable timer counter direction output** 参数。

**数据类型：** `Boolean`

### **Length** — 读取数据的长度 `scalar`

该端口输出从所选通道的捕获比较寄存器读取的数据长度。

#### 依赖项

要启用此端口，请选择 **Output data length** 参数。

**数据类型：** `uint32`

## 参数

### 主要

### **Timer module** — 选择定时器模块 `TIM1` (默认) | `TIM2` | `TIM3` | `...`

选择定时器模块。可用的定时器模块数量因处理器而异。

**注意**

确保在 STM32CubeMX 项目中也配置了 `Timer module`。

### **Channel #** — 选择通道 `CH1` (默认) | `CH2` | `CH3` | `CH4`

选择要读取其捕获比较寄存器值的通道。

**注意**

- 确保要启用的通道已在 STM32CubeMX 项目中配置为 `Input mode`。

  在 STM32CubeMX 中，转到 **Timers** > **TIM#** > **Mode** > **Channel#**
- 可以根据需求将所选通道输入模式配置为以下之一：

  - Input Capture direct mode 或 Input Capture indirect mode 或 Input Capture triggered by TRC（用于通道 1-4）
  - PWM input on CH1 或 CH2（1 和 2）
  - XOR ON/Hall sensor mode（通道 1-3）

  在 STM32CubeMX 中，转到 **Timers** > **TIM#** > **Mode** > **Channel#**

### **Capture data length** — 指定要从捕获比较寄存器读取的数据长度 `off` (默认) | `on`

要从捕获比较寄存器读取的数据长度。

- 如果长度为 `1`，则以轮询模式读取捕获比较寄存器。
- 如果长度大于 `1`，则使用 DMA 从捕获比较寄存器读取指定数据长度。

确保在 STM32CubeMX 项目中配置 **DMA**。在 STM32CubeMX 中，转到 **Timers** > **TIM#** > **Configuration** > **DMA settings** 并为所选通道添加 DMA。

.

### **Enable timer counter direction output** — 选择以启用定时器计数器方向输出端口 `off` (默认) | `on`

启用此参数以输出计数器的当前方向。

### **Output data length** — 选择以输出长度端口 `off` (默认) | `on`

选择此参数以输出读取数据的长度。

当您选择 Output data length 参数时，模块会配置一个输出端口 Length。

### **Output status** — 选择以启用输出状态端口 `off` (默认) | `on`

选择此参数以输出读取数据的状态。状态输出 `1` 表示溢出错误。

当您选择 Output Status 参数时，模块会配置一个输出端口 Status。

### **Sample time** — 读取已启用输出端口的频率 `-1` (默认) | `non-negative real value`

指定在未选择输入端口时读取已启用输出端口状态的频率（以 seconds 为单位）。输入大于零的值。当您将此参数指定为 -1 时，Simulink® 会根据模型中的模块上下文确定模块的最佳采样时间。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32WBxx Based Boards

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

## 描述

输出捕获比较寄存器值

当配置为输入模式时，输出所选定时器模块和通道的捕获比较寄存器值。

在 **Capture data length** 中指定要从捕获比较寄存器读取的数据长度。对于大于 `1` 的数据长度，必须在 STM32CubeMX 项目中为所选定时器模块和通道添加 DMA。

- 选择 **Output data length** 以输出读取数据的长度。
- 选择 **Output status** 以输出读取数据的状态。状态输出 `1` 表示溢出错误。
- 选择 **Output direction** 以输出计数器方向。

为避免在读取捕获比较寄存器值时发生溢出错误，您可以将 Timer Capture 模块放置在连接到 Hardware Interrupt 模块的函数调用子系统中，并使用以下事件之一。

- `Capture compare event of the selected timer and channel`
  - 如果要读取的捕获比较数据长度等于 `1`。这确保当所选定时器模块和通道的捕获比较事件中断发生时，模块输出数据。

  确保在 **Configuration Parameters** > **timers** > **show TIM#** > **Configurations** 中配置捕获比较事件的中断
- `Transfer complete event of the DMA configured for selected timer
  and channel` - 如果要读取的捕获比较数据长度大于 `1`。这确保一旦 DMA 从捕获比较寄存器读取指定长度的数据并生成传输完成事件中断，模块就输出数据。
