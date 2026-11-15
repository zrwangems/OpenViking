---
type: simulink-block
title: 'Analog to Digital Converter'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F4-Discovery Board Blocks'
documentation_page: 'analogtodigitalconverter'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/analogtodigitalconverter.html'
language: zh-CN
chinese_source: worker-translation
---

# Analog to Digital Converter

## 端口

### 输入

### **Trigger** — 用于触发转换的标量端口

将 ADC 输入引脚上的模拟信号转换为数字信号。

#### 依赖

要启用此端口，请将 **Block action** 参数设置为 `Trigger via input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

### 输出

### **Data** — ADC 数字数据标量

模块输出模拟通道的转换后数字数据。

#### 依赖

要启用此端口，请将 **Block action** 参数设置为 `Trigger, wait and read results`。

**数据类型：** `uint16`

## 参数

Analog to Digital Converter 对话框包含三个选项卡：

- **配置** — 标识模块的配置设置。
- **通道选择** — 指定用于转换的通道详细信息。
- **中断和状态标志** — 设置中断和标志状态。

### 配置

### **ADC module** — 用于转换的 ADC 模块 `ADC1` (default) | `ADC2` | `ADC3`

选择用于转换的 ADC 模块。

### **ADC conversion group** — ADC 转换选项 `Injected group` (default) | `Regular group`

选择以下转换选项之一。

- `Injected group` — 您最多可以转换 4 个模拟信号。在此模式下，您可以在常规组通道转换期间“注入”ADC 转换。
- `Regular group` — 您最多可以转换 16 个模拟信号。

### **Block configuration** — 触发模数转换的选项 `Software start of conversion` (default) | `External start of conversion` | `Trigger start of conversion after regular group (JAUTO)` | `Only read results`

选择以下转换选项之一。

- `Software start of conversion` – 选择此选项可基于软件请求启动 ADC 转换。
- `External start of conversion` – 选择此选项可基于外部事件启动 ADC 转换。
- `Trigger start of conversion after regular group (JAUTO)` – 选择此选项可在常规组通道完成后启动注入组转换。仅当您在 **ADC conversion group** 中选择 `Injected group` 时，此选项可用。
- `Only read results` — 在此模式下，模块输出仅发出所选模拟通道的模数转换结果。模块不配置所选的 ADC 模块。

### **Block action** — 用于在 'Block configuration' 参数中的 ‘Software start of conversion’ 选项下触发 ADC 转换的选项 `Trigger, wait and read results` (default) | `Trigger via input port`

选择用于在 'Block configuration' 参数中的 ‘Software start of conversion’ 选项下触发 ADC 转换的选项。

- `Trigger, wait and read results` — 选择此选项可在每个采样时间触发 ADC 转换。模块输出会等待转换完成并发出结果。当您在 'Block configuration' 参数中选择 ‘Software start of conversion’ 时，此选项启用。
- `Trigger via input port` — 选择此选项可在输入 'Trigger' 上触发 ADC 转换。当输入为 true 时触发 ADC 转换。由于 ADC 模块不发出转换结果，请使用另一个 ADC 模块，并在 'Block configuration' 参数中选择 'Only read results'。此选项有助于在触发或使能子系统中读取 ADC 转换结果。

### **Enable continuous conversion** — 将 ADC 配置为连续转换模式的选项 off (default) | on

ADC 配置为连续转换模式。仅当您为 **ADC conversion group** 选择 `Regular group` 时，此选项可用。

### **Enable EOC signal at the end of each channel conversion** — 用于指示每个通道转换后转换结束的选项 off (default) | on

您选择用于指示每个通道转换后转换结束的选项。仅当您为 **ADC conversion group** 选择 `Regular group` 时，此选项可用。

### **External trigger event selection** — 用于转换的 ADC 模块 Timer 1 CC1 (default) | Timer 1 CC2 | Timer 1 CC3 | Timer 2 CC2 | Timer 2 CC3 | Timer 2 CC4 | Timer 2 TRGO | Timer 3 CC1 | Timer 3 TRGO | Timer 4 CC4 | Timer 5 CC1 | Timer 5 CC2 | Timer 5 CC3 | Timer 8 CC1 | Timer 8 TRGO | EXTI line 11

选择触发 ADC 所基于的外部事件的极性。

### **Sample time** — 模块读取引脚值的频率 -1 (default)

指定此模块读取引脚值的频率，以 seconds 为单位。输入大于零的值。

### 通道选择

### **Number of channels to be converted** — 用于转换的通道数 1 (default) | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16

选择用于转换的通道数。

### **1st Conversion** — 用于第一次转换的通道 ADC Channel 0 (default) | ADC Channel 1 | ADC Channel 2 | ADC Channel 3 | ADC Channel 4 | ADC Channel 5 | ADC Channel 6 | ADC Channel 7 | ADC Channel 8 | ADC Channel 9 | ADC Channel 10 | ADC Channel 11 | ADC Channel 12 | ADC Channel 13 | ADC Channel 14 | ADC Channel 15 | ADC Channel 16 (Temp. sensor) | ADC Channel 17 (V\_REFINT) | ADC Channel 18 (V\_BAT)

选择用于第一次转换的通道。

### **2nd Conversion** — 用于第二次转换的通道 ADC Channel 0 (default) | ADC Channel 1 | ADC Channel 2 | ADC Channel 3 | ADC Channel 4 | ADC Channel 5 | ADC Channel 6 | ADC Channel 7 | ADC Channel 8 | ADC Channel 9 | ADC Channel 10 | ADC Channel 11 | ADC Channel 12 | ADC Channel 13 | ADC Channel 14 | ADC Channel 15 | ADC Channel 16 (Temp. sensor) | ADC Channel 17 (V\_REFINT) | ADC Channel 18 (V\_BAT)

选择用于第二次转换的通道。如果 **Number of channels to be converted** 大于 1，您可以选择用于第二次转换的 ADC 通道。

### **nth Conversion** — 用于第 n 次转换的通道 ADC Channel 0 (default) | ADC Channel 1 | ADC Channel 2 | ADC Channel 3 | ADC Channel 4 | ADC Channel 5 | ADC Channel 6 | ADC Channel 7 | ADC Channel 8 | ADC Channel 9 | ADC Channel 10 | ADC Channel 11 | ADC Channel 12 | ADC Channel 13 | ADC Channel 14 | ADC Channel 15 | ADC Channel 16 (Temp. sensor) | ADC Channel 17 (V\_REFINT) | ADC Channel 18 (V\_BAT)

选择用于第 n 次转换的通道，其中对于 Injected group，n = 4；对于 Regular group，n = 16。如果 **Number of channels to be converted** 大于 1，您可以选择用于第 n 次转换的 ADC 通道。

### 中断和状态标志

### **Post over run interrupt** — 发出溢出状态的选项 off (default) | on

选择在模块输出中发出溢出状态的选项。

### **Post watchdog interrupt** — 发出看门狗中断的选项 off (default) | on

选择发出看门狗中断的选项。

### **Post end of conversion interrupt** — 发出转换结束中断的选项 off (default) | on

选择发出转换结束中断的选项。

### **Output over run status** — 发出溢出状态的选项 off (default) | on

选择发出溢出状态的选项。

### **Output watchdog status** — 发出超出看门狗阈值的转换状态的选项

选择发出关于转换超出看门狗阈值的状态的选项。

### **Output start of conversion status** — 发出关于转换开始状态的选项 off (default) | on

选择发出关于转换开始状态的选项。

### **Output end of conversion status** — 发出关于转换结束状态的选项 off (default) | on

选择发出关于转换结束状态的选项。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32WBxx Based Boards

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

## 描述

将 ADC 输入引脚上的模拟信号转换为数字信号

测量模拟引脚相对于 STM32F4-Discovery™ 板上模拟输入参考电压的电压。模块输出根据在 Configuration parameters > Hardware Implementation > Hardware board > Target hardware resources > ADCx > Conversion resolution 中为 ADC 选择的转换分辨率，发出不同范围的模拟电压。

**注意**

ADC 通道的转换时间根据 **Configuration parameters** > **Hardware Implementation** > **Hardware board** > **Target hardware resources** > **ADCx** 中指定的 ADC 分辨率和采样时间进行配置。

例如：当您为 ADC1 选择 12-bits 作为分辨率时，模块输出发出范围为 0 到 4095 的模拟电压。如果测得的电压等于地电压，模块输出发出 0。如果测得的电压等于模拟参考电压，模块输出发出 4095。

您可以在 single、continuous、scan 或 discontinuous 模式下从 ADC1、ADC2 或 ADC3 模块读取最多 16 个通道的模拟信号。

该表显示了 ADC 模块各通道对应的模拟引脚，这些引脚可用于测量电压。

例如，对应于通道 12 的 ADC 模块 1、2 和 3 可以使用 PC2 引脚测量电压。这里，PC2 指端口 C 上的引脚 2。

ADC 引脚映射
