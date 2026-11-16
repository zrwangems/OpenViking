---
type: simulink-block
title: 'Timer'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Timer Peripherals'
documentation_page: 'timer'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/timer.html'
language: zh-CN
chinese_source: worker-translation
---

# Timer

## 端口

### 输入

### **freq count** — 定时器的频率计数 `scalar`

此端口处的输入决定计数器的频率。此值直接写入自动重载寄存器。

32 位定时器的频率计数介于 `0` 到 `0xFFFFFFFF` 之间，16 位定时器介于 `0` 到 `0xFFFF` 之间。

#### 依赖关系

要启用此端口，请选择 **Enable frequency input** 参数。

**数据类型：** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **CEN** — 用于启用定时器计数器的端口 `scalar`

使用此端口启用或禁用定时器计数器。将此端口设置为以下值之一。

- `0` - 禁用计数器
- `1` - 启用计数器

#### 依赖关系

要启用此端口，请选择 **Enable input to enable/disable timer** 参数。

**数据类型：** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **MOE** — 主输出使能 `scalar`

一旦 break 输入有效，硬件会异步清除此主输出使能 (MOE) 位。

如果输入为 `1`，则 MOE 位设置为 `1`。

#### 依赖关系

要启用此端口，请选择 **Enable main output enable (MOE) input** 参数。

**数据类型：** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **UG** — 用于生成更新事件的输入 `scalar`

使用此端口生成更新事件。当指定值为 `1` 时，该端口生成更新事件。

#### 依赖关系

要启用此端口，请选择 **Enable update generation event input** 参数。

**数据类型：** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **CC#G** — 捕获比较生成事件输入 `scalar`

使用此端口生成捕获比较生成事件。当指定值为 `1` 时，该端口生成捕获比较事件。

#### 依赖关系

要启用此端口，请选择 **Enable capture compare # generation event input** 参数。

**数据类型：** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **TG** — 触发生成 `scalar`

使用此端口生成触发事件。当指定值为 `1` 时，该端口生成触发事件。

#### 依赖关系

要启用此端口，请选择 **Enable trigger generation event input** 参数。

**数据类型：** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **BG** — Break 生成 `scalar`

使用此端口生成 break 生成事件。当指定值为 `1` 时，该端口生成 break 生成事件。

#### 依赖关系

要启用此端口，请选择 **Enable break generation event input** 参数。

**数据类型：** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **B2G** — Break 生成 2 事件 `scalar`

使用此端口生成 break 2 生成事件。当指定值为 `1` 时，该端口生成 break 2 生成事件，并且清除 MOE 状态。

#### 依赖关系

要启用此端口，请选择 **Enable break generation 2 event input** 参数。

**数据类型：** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **COMG** — 捕获比较控制更新生成 `scalar`

使用此端口生成捕获比较控制更新生成事件。当指定值为 `1` 时，该端口生成捕获比较控制更新。

#### 依赖关系

要启用此端口，请选择 **Enable COM generation event input** 参数。

**数据类型：** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### 输出

### **CNT** — 当前定时器计数器值 `scalar`

计数器端口为所选定时器模块提供当前定时器计数器值作为输出。

**数据类型：** `uint32`

### **Dir** — 定时器计数器方向输出 `scalar`

该模块将定时器计数器的当前方向输出为以下之一：

- 0 - 向上计数器
- 1 - 向下计数器

#### 依赖关系

要启用此端口，请选择 **Enable timer counter direction output** 参数。

**数据类型：** `Boolean`

### **MOE status** — 主输出使能位的状态 `scalar`

主输出使能 (MOE) 位的状态。

#### 依赖关系

要启用此端口，请选择 **Enable main output enable (MOE) status output** 参数。

**数据类型：** `Boolean`

## 参数

### 主要

### **Timer module** — 选择定时器模块 `TIM1`（默认） | `TIM2` | `TIM3` | `...`

选择定时器模块。可用的定时器模块数量因处理器而异。

**注意**

确保在 STM32CubeMX 项目中也配置了 `Timer module`。

### **Enable input to enable/disable timer** — 通过输入端口启用计数器 `off`（默认） | `on`

默认情况下，配置参数中的 `Start timer during model initialization` 参数处于启用状态。这会在模型初始化期间启动定时器计数器。

如果要在运行时启动定时器计数器，请禁用配置参数中的 `Start timer during model initialization` 参数。

**注意**

如果 `Enable input to enable/disable timer parameter (block)` 和 `Start timer during model initialization (Configuration Parameter)` 两个参数均未启用，则不会启动定时器计数器。

### **Enable main output enable (MOE) input** — 通过输入端口启用主输出 `off`（默认） | `on`

启用此参数可设置主输出使能 (MOE) 位，以从 break 恢复。

#### 依赖关系

要启用此参数，请将 **Timer module** 参数设置为 `TIM1`、`TIM8`、`TIM8`、`TIM16`、`TIM17` 或 `TIM20` 之一。

### **Enable frequency input** — 通过输入端口设置 AutoReload 寄存器 `off`（默认） | `on`

启用此参数可在运行时设置定时器的 AutoReload 寄存器 (ARR) 值。

### **Set the repetition counter after timer counter is enabled** — 通过输入启用重复计数器 `off`（默认） | `on`

对于重复计数器中的奇数值，更新事件会在下溢或上溢时发生，具体取决于你设置重复计数器的时间。

默认情况下，该模块在启用定时器计数器之前设置重复计数器，因此更新事件在下溢时发生。

如果启用此参数，该模块在启用定时器计数器之后设置重复计数器，因此更新事件在上溢时发生。

#### 依赖关系

要启用此参数，请将 **Timer module** 参数设置为 `TIM1`、`TIM8`、`TIM8`、`TIM16`、`TIM17` 或 `TIM20` 之一。

### **Enable timer counter direction output** — 选择以启用定时器计数器方向输出端口 `off`（默认） | `on`

启用此参数可输出定时器计数器的当前方向。

### **Enable main output enable (MOE) status output** — 选择以启用 MOE 状态端口 `off`（默认） | `on`

启用此参数可输出主输出使能 (MOE) 位状态。

#### 依赖关系

要启用此参数，请将 **Timer module** 参数设置为 `TIM1`、`TIM8`、`TIM8`、`TIM16`、`TIM17` 或 `TIM20` 之一。

### 事件

### **Enable update generation event input** — 选择以启用生成更新事件输入端口 `off`（默认） | `on`

启用此参数可通过输入端口生成更新事件。

### **Enable capture compare # generation event input** — 选择以启用捕获比较生成事件输入 `off`（默认） | `on`

启用此参数可通过输入端口生成捕获比较事件。

#### 依赖关系

可用的 **Enable capture compare # generation event input** 参数数量取决于你在 **Timer module** 中选择的模块。

### **Enable trigger generation event input** — 选择以启用触发生成事件输入 `off`（默认） | `on`

启用此参数可通过输入端口生成触发事件。

### **Enable break generation event input** — 选择以启用 break 生成事件输入 `off`（默认） | `on`

启用此参数可通过输入端口生成 break 事件。

#### 依赖关系

要启用此参数，请将 **Timer module** 参数设置为模块 `TIM1`、`TIM8`、`TIM8`、`TIM16`、`TIM17` 或 `TIM20` 中的任意一个。

### **Enable break generation 2 event input** — 选择以启用 break 生成 2 事件输入 `off`（默认） | `on`

启用此参数可通过输入端口生成 break 2 事件。

#### 依赖关系

要启用此参数，请将 **Timer module** 参数设置为模块 `TIM1`、`TIM8`、`TIM8`、`TIM16`、`TIM17` 或 `TIM20` 中的任意一个。

### **Enable COM generation event input** — 选择以启用捕获比较生成事件输入 `off`（默认） | `on`

启用此参数可通过输入端口生成捕获比较事件。

#### 依赖关系

要启用此参数，请将 **Timer module** 参数设置为模块 `TIM1`、`TIM8`、`TIM8`、`TIM16`、`TIM17` 或 `TIM20` 中的任意一个。

### **Sample time** — 读取已启用输出端口的频率 `-1`（默认） | `non-negative real value`

如果未选择任何输入端口，请指定读取已启用输出端口状态的频率（以 seconds 为单位）。输入大于零的值。当将此参数指定为 -1 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

#### 依赖关系

要启用 **Sample time** 参数，请取消选择所有输入端口。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32WBxx Based Boards

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

## 描述

启动定时器计数器并提供当前计数值

启动定时器计数器，并为所选定时器模块提供当前计数值作为输出。还会启用配置参数中选择的中断。

仅当在配置参数中选择了 `Start Timer during model initialization` 参数时，计数器才会在模型初始化期间启动。

要在运行时启动/停止计数器，请在配置参数中取消选择 `Start Timer during model initialization` 参数，并在模块中选择 `Enable input to enable/disable timer` 选项。向相应输入端口输入 `1` 将启动计数器，输入 `0` 将停止计数器。
