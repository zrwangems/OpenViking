---
type: simulink-block
title: 'Analog to Digital Converter'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Analog Peripherals'
documentation_page: 'analogtodigitalconverterblock'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/analogtodigitalconverterblock.html'
language: zh-CN
chinese_source: official
---

# Analog to Digital Converter

## 端口

### 输入

### **Trigger** — 触发转换的端口 标量

将 ADC 输入引脚上的模拟信号转换为数字信号。

触发 ADC 输入引脚进行转换。

- `1` - 已触发 ADC 开始转换
- `0` - 未触发 ADC 开始转换

#### 依赖关系

要启用此端口，请将**触发模式**参数设置为 `Trigger only`。

**数据类型:** `Boolean`

### **msg** — SoC Blockset™ 仿真消息 标量

仿真专用消息输入端口，当连接到 ADC Interface (SoC Blockset) 模块时，该端口在仿真期间充当直通端口，即 ADC Interface 模块的输入由 Analog to Digital Converter Block 模块的输出发出。

#### 依赖关系

要启用此端口，请启用**启用仿真端口**参数。

**数据类型:** `SoCData`
### 输出

### **Cnts** — 计数 标量

该模块将从模数转换器 (ADC) 转换的选定模拟通道的数字值输出为 1×N 向量，其中 N 为转换次数。

#### 依赖关系

要启用此端口，请将**触发模式**参数设置为 `Trigger and read` 或 `Read results only`。

**数据类型:** `uint16`

### **Status** — ADC 的状态 标量

该模块输出 ADC 模块状态。

当触发模式为**触发并读取**或**仅读取结果**时，模块输出以下状态：

- `0` - 输出计数有效
- `1` - 输出计数不可用或设置了超限标志。

当触发模式为**仅触发**时，模块输出以下状态：

- `0` - 当 ADC 触发时
- `1` - 当 ADC 未触发时

#### 依赖关系

要启用此端口，请选择**输出状态**参数。

**数据类型:** `uint16`

## 参数

### **ADC 模块** — 用于转换的 ADC 模块 **ADC1** (默认) | **ADC2** | **ADC3**

选择用于转换的 ADC 模块。

### **转换组** — 用于 ADC 转换的选项 **常规组** (默认) | **注入组**

选择以下转换选项之一：

- **注入组** - 您最多可以转换四个模拟信号。在此模式下，可以在常规组通道转换期间注入 ADC 转换。
- **常规组** - 您最多可以转换 16 个模拟信号。

### **触发模式** — 用于触发 ADC 开始转换的选项 **触发并读取** (默认) | **仅触发** | **仅读取结果**

选择以下选项之一来触发转换。

- **触发并读取** - 选择此选项可在每个采样时间触发 ADC 开始转换。模块输出等待转换完成，并发出结果。此选项启用输出端口 **Cnts**。
- **仅触发** - 使用此选项读取触发子系统或使能子系统中的 ADC 转换结果。由于模块在此模式下不显示转换结果，请使用另一个 Analog to Digital Converter 模块（“触发模式”参数设置为**仅读取结果**）以显示转换结果。
- **仅读取结果** - 选择此选项读取新转换的 ADC 数据。如果没有新数据可用，则模块将状态输出为 `1`。此选项还会启用输出端口 **Cnts**。

### **转换次数** — ADC 转换次数 `1` (默认) | `1 to 4 for Inject group` | `1 to 16 for Regular group`

根据您在**转换组**参数中选择的转换组设置 ADC 转换次数。

- `Inject group` - 指定 1 到 4 之间的一个数字。
- `Regular group` - 指定 1 到 16 之间的一个数字。

### **输出状态** — 启用输出状态 `off` (默认) | `on`

当您选择此参数时，模块会配置**状态**输出端口。状态端口输出 ADC 转换的状态。

#### 依赖关系

要启用**输出状态**参数，请将**触发模式**参数设置为**任一项的参数**或**仅读取结果**。

### **采样时间** — 模块读取引脚值的频率 `-1` (默认) | `non-negative real value`

指定模块读取引脚值的频率（以秒为单位）。请输入大于零的值。当您将此参数指定为 -1 时，Simulink 根据模型中的模块上下文确定模块的最佳采样时间。

#### 依赖关系

要启用**采样时间**参数，请将**触发模式**参数设置为**触发并读取**或**仅读取结果**。

### **启用仿真端口** — 启用模块的仿真端口 `off` (默认) | `on`

选择此参数以添加 SoC Blockset 兼容的仿真输出端口。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32WBxx Based Boards

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2021b 中推出**

## 描述

将 ADC 输入引脚上的模拟信号转换为数字信号

使用 Analog to Digital Converter 模块将 ADC 输入引脚上的模拟值转换为数字值。模块输出是一个 1×N 行向量，N 是转换次数。该模块测量模拟引脚的电压，该电压是相对于基于 STM32 处理器的板上的模拟输入参考电压而言的。

ADC 通道的转换时间在 STM32CubeMX 工程中配置。

对于**基于 STM32H7xx 的板**和**基于 STM32G4xx 的板**，ADC 模块的输入通道可以在 STM32CubeMX 工程中配置为**差分模式**或**单端**。用户可以在 STM32CubeMX 工程中指定选定通道的偏移值。

有关详细信息，请参阅处理基于 STM32H7xx 和 STM32G4xx 的板的 ADC 数据。

**注意**

在模型中，仅使用基于 STM32H7xx 的板库模块和基于 STM32H7xx 的目标硬件板。当运行具有映射到基于 STM32H7xx 的目标的 STM32 库模块的模型时，会出现一条错误消息。

**注意**

您可以在基于 STM32 处理器的板上以连接 IO 模式运行包含 Analog to Digital Converter 模块的 Simulink® 模型。有关详细信息，请参阅Communicate with Hardware Using Connected IO。
