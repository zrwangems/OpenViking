---
type: simulink-block
title: 'Digital Port Write'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / System Core'
documentation_page: 'digitalportwrite'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/digitalportwrite.html'
language: zh-CN
chinese_source: official
---

# Digital Port Write

## 端口

### 输入

### **Pin(s)** — 设置 GPIO 引脚状态 `scalar` | `vector`

以递增顺序设置 GPIO 引脚状态的输入端口。

- 0 - 对应的引脚设置为低值。
- 非 0 - 引脚为低电平或高电平。

#### 依赖关系

要读取多个端口值，请选择**以数组形式访问端口引脚**参数。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **msg Pin *`n`*** — SoC Blockset™ 仿真消息 标量 | 向量

仅限仿真的消息输出端口，当连接到 Digital IO Interface (SoC Blockset) 模块时，该端口在仿真期间充当直通端口，其输出由 Digital IO Interface 模块发出。当**以数组形式访问端口引脚**参数未选中时，将为**引脚编号**参数中的每个引脚生成一个仿真端口，否则引脚数组必须被视为标量。

#### 依赖关系

要启用此端口，请选择**启用仿真端口**参数。

**数据类型:** `SoCData`

## 参数

### **Port name** — 用于写入 GPIO 引脚状态的端口 `GPIOA` (默认) | `GPIOB` | `GPIOC` | `GPIOD` | `GPIOE` | `GPIOF` | `GPIOG` | `GPIOH` | `GPIOI` | `GPIOJ` | `GPIOK`

选择 `GPIOA` 到 `GPIOK` 端口之一来设置指定 GPIO 端口的 GPIO 引脚状态。

### **引脚编号** — 用于设置 GPIO 引脚状态的 GPIO 端口 `0` (默认) | `any range between 1 to 15`

指定 GPIO 数字引脚来设置逻辑状态。

### **Access port pins as array** — 输入多个引脚值 `on` (默认) | `off`

选择此参数以读取多个端口引脚值。

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

设置 GPIO 引脚状态

写入 STM32 处理器的 GPIO 端口引脚的逻辑状态。

**注意**

您可以在基于 STM32 处理器的板上以连接 IO 模式运行包含 Digital Port Write 模块的 Simulink® 模型。有关详细信息，请参阅Communicate with Hardware Using Connected IO。
