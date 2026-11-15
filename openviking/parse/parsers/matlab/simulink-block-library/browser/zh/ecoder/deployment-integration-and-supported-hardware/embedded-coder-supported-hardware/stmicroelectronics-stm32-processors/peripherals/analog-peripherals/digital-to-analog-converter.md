---
type: simulink-block
title: 'Digital to Analog Converter'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Analog Peripherals'
documentation_page: 'digitaltoanalogconverter'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/digitaltoanalogconverter.html'
language: zh-CN
chinese_source: worker-translation
---

# Digital to Analog Converter

## 端口

### 输入

### **dln/dInCh#** — 数据输入端口标量

该端口接受以下输入范围：

- `0-4095` - 12 位数据长度且数据右对齐。
- `0-65520` - 12 位数据长度且数据左对齐
- `0-255` - 8 位数据长度

选择 dual channel 会启用 2 个 **dInCh#** 输入端口。

#### 依赖项

若要启用此端口，请将 `Mode` 设置为 **Write only** 或 **Write and trigger** 参数。

**数据类型：** `uint8` | `uint16`

### **baseValue** — 基值标量

此端口设置 DAC 通道的偏移值。

#### 依赖项

若要启用此端口，请将 **Mode** 设置为 `Trigger only`，并将 **Waveform type** 设置为 `Noise/Triangular`。

**数据类型：** `uint16`

### **stepData** — 步进数据标量

此端口以 `12.4` 位格式设置锯齿波的步进值。

#### 依赖项

若要启用此端口，请将 **Mode** 设置为 `Trigger only`，并将 **Waveform type** 设置为 `Sawtooth`。

**数据类型：** `uint16`

### **trigln/trigInCh#** — 触发输入端口布尔

在指定通道上触发转换。

选择 dual channel 会启用 2 个 **trigInCh#** 输入端口。

#### 依赖项

若要启用此端口，请将 `Mode` 设置为 **Write and trigger** 或 **Trigger only** 参数。

**数据类型：** `Boolean`

### **stepTrigIn/stepTrigInCh#** — 软件步进触发布尔

此端口通过 step data 中指定的值触发 DAC 输出的变化。

选择 dual channel 会启用 2 个 **stepTrigInCh#** 输入端口。

#### 依赖项

若要启用此端口，请选择 **Enable software step trigger (Trigger 2)** 参数。确保将 **Mode** 设置为 `Trigger only` 参数，并将 **Waveform type** 设置为 `sawtooth`。

**数据类型：** `Boolean`

### **rstTrigIn/rstTrigInCh#** — 软件复位步进触发布尔

此端口将 DAC 值复位为 STM32 CubeMX 工程中指定的值。

选择 dual channel 会启用 2 个 **rstTrigInCh#** 输入端口。

#### 依赖项

若要启用此端口，请选择 **Enable software reset trigger (Trigger 1)** 参数。确保将 **Mode** 设置为 `Trigger only` 参数，并将 **Waveform type** 设置为 `sawtooth`。

**数据类型：** `Boolean`

### **dacEnable** — DAC 使能布尔

此端口允许用户在运行时使能和禁用 DAC。

#### 依赖项

若要启用此端口，请选择 **Control input for DAC enable** 参数。

**数据类型：** `Boolean`
### 输出

### **Status** — DAC 状态布尔

使用 DAC 模块后，DAC 模块现在可以在使能后被禁用。此外，状态输出现在有三种状态，分别表示：

- `0` - DAC 已使能并按预期运行
- `1` - DAC 已成功禁用
- `2` - 命令执行期间发生错误

#### 依赖项

若要启用此端口，请选择 **Output status** 参数。

**数据类型：** `uint8`

## 参数

### **DAC module** — 用于转换的 DAC 模块 `DAC1`（默认） | `DAC2` | `DAC3` | `DAC4`

选择用于转换的数模转换器模块。

### **Mode** — 触发 DAC 开始转换的选项 `Write only`（默认） | `Write and trigger` | `Trigger only`

选择转换模式。

- `Write only` — `Write only` 选项允许用户将数据写入 DAC 的数据保持寄存器。

  - 在没有任何触发参与的情况下将数据转换为模拟值。这要求触发源为 `None`。
  - 将数字值写入由内部触发源触发的通道。这要求 trig source 为 STM32 CubeMX 工程中可用的基于定时器的触发源之一。

  此选项还会启用输入端口 **dIn**。
- `Write and trigger` — `Write and trigger` 允许用户将数据写入 DAC 的 DHR 并控制转换点。这要求触发源设置为 software。

  此选项启用输入端口 **TrigIn** 和 **dIn**。
- `Trigger only` — 当您想要触发转换时选择此选项。

  - 当数据由某种内部机制写入 DHR，并且用户需要控制触发点时。
  - 用于波形生成

  此选项启用输入端口 **Stepdata**

### **Channel select** — 选择 DAC 通道 `Channel1`（默认） | `Channel2` | `Dual channel`

选择应在其上执行转换的数模转换器模块通道。选择 dual channel 选项可一起控制模块的两个通道。

选择 dual channel 会启用 2 个 **dIn/dInCh#** 输入端口。

### **Trigger configuration** — 选择触发配置 `Independent`（默认） | `Simultaneous`

触发配置指定两个通道需要同时触发还是独立触发。

#### 依赖项

若要启用此参数，请将 **Mode** 设置为 `Write and trigger` 或 `Trigger only`，并将 **Channel select** 设置为 `Dual channel`。

### **Waveform generation enable** — 启用波形生成 `off`（默认） | `on`

选择以在所选通道上启用波形生成。如果未选择 **waveform generation enable** 参数且未启用 **software trigger**，则 `dacEnable` 端口将是默认端口。

#### 依赖项

若要启用此参数，请将 **Mode** 设置为 `Trigger only`。

### **Waveform type** — 选择 DAC 波形类型 `Noise/Triangular`（默认） | `Sawtooth`

选择要在 DAC 通道上生成的波形类型。

- 选择 `Noise/Triangular` 波形类型会启用 **baseValue** 作为默认端口。
- 选择 `sawtooth` 波形类型会启用 **stepData** 作为默认端口。

选择 dual channel 以进行独立或同时转换。

#### 依赖项

若要启用此参数，请将 **Mode** 设置为 `Trigger only`。

### **Enable software trigger (Trigger 1)** — 选择软件触发 `on`（默认） | `off`

选择以通过软件触发来触发 DAC 转换。当您选择此参数时，模块会配置一个输入端口 **TrigIn/TriInCh#**。

#### 依赖项

若要启用此参数，请将 **Mode** 设置为 `Trigger only`，并将 **Waveform type** 设置为 `Noise/Triangular`。

### **Software step trigger enable** — 启用软件步进触发 `on`（默认） | `off`

当选择 sawtooth 波形时，使用 step data 中指定的值触发 DAC 通道上的转换。

当您选择此参数时，模块会配置一个输入端口 **stepTrigIn/stepTrigInCh#**。

#### 依赖项

若要启用此参数，请将 **Mode** 设置为 `Trigger only`，并将 **Waveform type** 设置为 `Sawtooth`。

### **Software reset trigger enable** — 启用软件复位触发 `off`（默认） | `on`

选择以启用软件复位触发数模转换器模块。当您选择此参数时，模块会配置一个输入端口 **rstTrigIn/rstTrigInCh#**。

#### 依赖项

若要启用此参数，请将 **Mode** 设置为 `Trigger only`，并将 **Waveform type** 设置为 `Sawtooth`。

### **Data length** — 选择 DAC 的数据长度 `12`（默认） | `8`

选择数模转换器模块的数据长度。

#### 依赖项

若要启用此参数，请将 **Mode** 设置为 `Write only` 或 `Write and Trigger`。

### **Data alignment** — 选择 DAC 的数据对齐方式 `Right alignment`（默认） | `Left alignment`

选择数模转换器模块的数据对齐方式。对于 8 位数据长度，right alignment 是默认选项。

如果数据长度和对齐方式选择为：

- 12 位且 right alignment，输入范围为 `0-4095`
- 12 位且 left alignment，输入范围为 `0-65520`
- 8 位，输入范围为 `0-255`

#### 依赖项

若要启用此参数，请将 **Mode** 设置为 `Write only` 或 `Write and Trigger`。

### **Output Status** — 启用输出状态 `off`（默认） | `on`

当您选择 **Output Status** 参数时，模块会配置一个输出端口 **Status**。该端口输出状态消息。

### **Control input for DAC enable** — DAC 使能输入 `off`（默认） | `on`

当您选择 **Control input for DAC enable** 参数时，模块会配置一个输出端口 **dacEnable**。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

配置 DAC 以在指定的 DAC 通道上生成模拟电压

Digital to Analog Converter 模块将数字值转换为模块对应通道上的等效模拟电压。

对于 **STM32xx based board**，DAC 模块的输入通道可以在 STM32CubeMX 工程中配置。

**注意**

DAC 不支持 DMA 功能。
