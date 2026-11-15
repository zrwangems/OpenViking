---
type: simulink-block
title: 'Digital Port Read'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / System Core'
documentation_page: 'digitalportread'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/digitalportread.html'
language: zh-CN
chinese_source: official
---

# Digital Port Read

## 端口

### 输入

### **Pin *`n`* msg** — SoC Blockset™ 仿真消息 标量

仿真专用消息输入端口，当连接到 Digital IO Interface (SoC Blockset) 模块时，该端口在仿真期间充当直通端口，即 Digital IO Interface 模块的输入由 Digital Port Read 模块的输出发出。当**以数组形式访问端口引脚**参数未选中时，将为**引脚编号**参数中的每个引脚生成一个仿真端口，否则引脚数组必须被视为标量。

#### 依赖关系

要启用此端口，请选中**启用仿真端口**参数。

**数据类型:** `SoCData`
### 输出

### **Pin(s)** — 包含逻辑值的输出端口 `scalar` | `vector`

该端口输出您在 **Pin number** 参数中指定的板上数字引脚的逻辑状态。

#### 依赖关系

要输出多个端口值，请选择 **Access port pins as array** 参数。

**数据类型:** `Boolean`

## 参数

### **Port name** — 用于读取 GPIO 引脚状态的端口 `GPIOA` (默认) | `GPIOB` | `GPIOC` | `GPIOD` | `GPIOE` | `GPIOF` | `GPIOG` | `GPIOH` | `GPIOI` | `GPIOJ` | `GPIOK`

选择 `GPIOA` 到 `GPIOK` 端口之一来获取指定 GPIO 端口的 GPIO 引脚状态。

### **引脚编号** — 用于读取逻辑状态的 GPIO 引脚 `0` (默认) | `scalar` | `vector`

指定用于读取逻辑状态的 GPIO 引脚。

当您指定 GPIO 引脚编号并启用 **Access port pins as array** 参数时，输出始终以引脚编号的递增顺序排列。

### **Access port pins as array** — 输出多个引脚值 `on` (默认) | `off`

选中此参数可输出多个端口引脚值。

### **采样时间** — 模块读取输入引脚值的频率 `-1` (默认) | `scalar` | `vector`

以秒为单位指定此模块读取引脚值的频率。

当您将此参数指定为 `-1` 时，Simulink 会根据模型中的模块上下文确定模块的最佳采样时间。

### **启用仿真端口** — 启用模块的仿真端口 `off` (默认) | `on`

选中此参数可添加 SoC Blockset 兼容的仿真输入端口。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32WBxx Based Boards

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2021b 中推出**

## 描述

读取 GPIO 引脚状态

读取 STM32 处理器的 GPIO 端口引脚的逻辑状态。

**注意**

您可以在基于 STM32 处理器的板上以连接 IO 模式运行包含 Digital Port Read 模块的 Simulink® 模型。有关详细信息，请参阅Communicate with Hardware Using Connected IO。
