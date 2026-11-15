---
type: simulink-block
title: 'PWM Output'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Timer Peripherals'
documentation_page: 'pwmoutputblock'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/pwmoutputblock.html'
language: zh-CN
chinese_source: worker-translation
---

# PWM Output

## 端口

### 输入

### **CH#** — 通道端口 `scalar`

输入端口考虑对应通道的占空比。

如果将 **Duty cycle units** 参数设置为 `Percentage`，请指定 `0` 到 `100` 之间的值范围。如果将占空比单位设置为 `Counts`，对于 32 位定时器，请指定 `0` 到 `0xFFFFFFFF` 之间的值范围；对于 16 位定时器，请指定 `0` 到 `0xFFFF` 之间的值范围。

#### 依赖关系

要启用此端口，请选择 **Enable channel** 参数。

**数据类型：** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **CC#E** — 捕获/比较使能输入端口 `scalar`

输入端口考虑对应通道的捕获/比较使能输入。

#### 依赖关系

要启用此端口，请选择 **Enable Capture/Compare Enable (CC#E) input** 参数。

**数据类型：** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **CC#NE** — 捕获/比较互补使能输入端口 `scalar`

输入端口考虑对应通道的捕获/比较互补使能输入。

#### 依赖关系

要启用此端口，请选择 **Enable Capture/Compare Complementary Enable (CC#NE) input** 参数。

**数据类型：** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **OC#M** — 输出比较模式输入端口 `scalar`

输入端口考虑对应通道的输出比较模式输入。

#### 依赖关系

要启用此端口，请选择 **Enable Output Compare Mode (OC#M) input** 参数。

**数据类型：** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **CEN** — 用于使能计数器的端口 `scalar`

使用此端口使能输入端口计数器。将此端口设置为以下值之一。

- `0` - 禁用计数器
- `1` - 使能计数器

#### 依赖关系

要启用此端口，请选择 **Enable input to enable/disable timer** 参数。

**数据类型：** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **MOE** — 主输出使能 `scalar`

一旦刹车输入有效，硬件会异步清除此主输出使能 (MOE) 位。

如果输入为 `1`，则将 MOE 位设置为 `1`。

#### 依赖关系

要启用此端口，请选择 **Enable main output enable (MOE) input** 参数。

**数据类型：** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **freq count** — 定时器频率计数 `scalar`

此端口处的输入决定计数器的频率。该值直接写入自动重载寄存器。

32 位定时器的频率计数介于 `0` 到 `0xFFFFFFFF` 之间，16 位定时器的频率计数介于 `0` 到 `0xFFFF` 之间。

#### 依赖关系

要启用此端口，请选择 **Enable frequency input** 参数。

**数据类型：** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **UG** — 生成更新事件的输入 `scalar`

使用此端口生成更新事件。当您指定值 `1` 时，该端口生成更新事件。

#### 依赖关系

要启用此端口，请选择 **Enable update generation event input** 参数。

**数据类型：** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **CC#G** — 捕获比较生成事件输入 `scalar`

使用此端口生成捕获比较生成事件。当您指定值 `1` 时，该端口生成捕获比较事件。

#### 依赖关系

要启用此端口，请选择 **Enable capture compare # generation event input** 参数。

**数据类型：** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **TG** — 触发生成 `scalar`

使用此端口生成触发事件。当您指定值 `1` 时，该端口生成触发事件。

#### 依赖关系

要启用此端口，请选择 **Enable trigger generation event input** 参数。

**数据类型：** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **BG** — 刹车生成 `scalar`

使用此端口生成刹车生成事件。当您指定值 `1` 时，该端口生成刹车生成事件。

#### 依赖关系

要启用此端口，请选择 **Enable break generation event input** 参数。

**数据类型：** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **B2G** — 刹车生成 2 事件 `scalar`

使用此端口生成刹车 2 生成事件。当您指定值 `1` 时，该端口生成刹车 2 生成事件，并清除 MOE 状态。

#### 依赖关系

要启用此端口，请选择 **Enable break generation 2 event input** 参数。

**数据类型：** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### 输出

### **direction** — 计数器方向输出 `scalar`

模块输出计数器的当前方向，如下之一：

- 0 - 向上计数器
- 1 - 向下计数器

#### 依赖关系

要启用此端口，请选择 **Enable timer counter direction output** 参数。

**数据类型：** `Boolean`

### **MOE status** — 主输出使能位状态 `scalar`

主输出使能 (MOE) 位的状态。

#### 依赖关系

要启用此端口，请选择 **Enable main output enable (MOE) status output** 参数。

**数据类型：** `Boolean`

### **msg CH *`n`*** — SoC Blockset™ 仿真消息 scalar | vector

仅用于仿真的消息输出端口在连接到 PWM Interface (SoC Blockset) 模块时充当直通，在仿真期间输出从 PWM Interface 模块的输出发出。

**注意**

- PWM Interface (SoC Blockset) 不使用此模块的频率输入，必须在 PWM Interface 模块掩码中手动设置。
- 对于基于 STM32F7xx、STM32H7xx 和 STM32G4xx 的板卡，仿真不支持通道 5 和通道 6。但是，所有通道都支持代码生成。

#### 依赖关系

要启用此端口，请选择 **Enable simulation port** 参数。

**数据类型：** `SoCData`

## 参数

### 主要

### **Timer module** — 选择定时器模块 `TIM1`（默认） | `TIM2` | `TIM3` | `TIM4` | `TIM5` | `TIM8` | `TIM9` | `TIM10` | `TIM11` | `TIM12` | `TIM13` | `TIM14`

选择定时器模块。可用的定时器模块数量因处理器而异。

**注意**

确保也在 STM32CubeMX 工程中配置 `Timer module`。

### **Duty cycle unit** — 选择占空比单位 `Percentage`（默认） | `Counts`

模块输入控制每个通道方波的占空比。

如果 **Duty Cycle unit** 为 `Percentage`，输入值 0 会产生 0% 占空比，输入值 100 会在对应通道上产生 100% 占空比的输出。如果 **Duty Cycle unit** 为 `Counts`，输入值会写入对应通道的捕获比较寄存器。

### **Enable channel #** — 选择通道 `Enable channel 1`（默认） | `Enable channel 2` | `Enable channel 3` | `Enable channel 4` | `Enable channel 5` | `Enable channel 6`

启用您希望模块生成 PWM 输出的通道。输入考虑对应通道的占空比。

每个 **Timer module** 可以有一到六个通道。可用通道数量因所选定时器模块而异。启用对应定时器支持的通道。默认情况下，模块启用 **channel 1**。

**注意**

确保在 STM32CubeMX 工程中将您要启用的通道配置为 PWM 生成。

#### 依赖关系

可用通道数量取决于您在 **Timer module** 参数中选择的模块。

### **Enable Capture/Compare # Enable (CC#E) input** — 通过输入端口启用捕获/比较 `off`（默认） | `on`

启用此参数以通过输入端口生成捕获/比较输入。

#### 依赖关系

要启用此参数，请选择对应的 **Enable channel#** 参数。

### **Enable Capture/Compare # Complementary Enable (CC#NE) input** — 通过输入端口启用捕获/比较互补 `off`（默认） | `on`

启用此参数以通过输入端口生成捕获/比较互补输入。

#### 依赖关系

要启用此参数，请选择对应的 **Enable channel#** 参数。

### **Enable Output Compare # Mode (OC#M) input** — 通过输入端口启用输出比较模式 `off`（默认） | `on`

启用此参数以通过输入端口生成输出比较模式输入。

#### 依赖关系

要启用此参数，请选择对应的 **Enable channel#** 参数。

### **Enable input to enable/disable timer** — 通过输入端口启用计数器 `off`（默认） | `on`

通过输入端口启用或禁用计数器。如果未选择此参数，则在模型初始化期间启用计数器。

### **Enable main output enable (MOE) input** — 通过输入端口启用主输出 `off`（默认） | `on`

启用此参数以设置主输出使能 (MOE) 位，从而从刹车中恢复。

#### 依赖关系

要启用此参数，请将 **Timer module** 参数设置为 `TIM1` 或 `TIM8`。

### **Enable frequency input** — 通过输入端口启用频率 `off`（默认） | `on`

启用此参数以设置定时器的频率。所有通道输出具有相同频率。

### **Set the repetition counter after counter is enabled** — 通过输入启用重复计数器 `off`（默认） | `on`

对于重复计数器中的奇数值，更新事件在下溢或上溢时发生，具体取决于您设置重复计数器的时间。

默认情况下，模块在您启用定时器计数器之前设置重复计数器，因此更新事件在下溢时发生。

如果启用此参数，模块在您启用定时器计数器之后设置重复计数器，因此更新事件在上溢时发生。

#### 依赖关系

要启用此参数，请将 **Timer module** 参数设置为 `TIM1` 或 `TIM8`。

### **Enable timer counter direction output** — 选择输出计数器方向 `off`（默认） | `on`

启用此参数以输出计数器的当前方向。

### **Enable main output enable (MOE) status output** — 选择主输出使能 `off`（默认） | `on`

启用此参数以输出主输出使能 (MOE) 位状态。

#### 依赖关系

要启用此参数，请将 **Timer module** 参数设置为 `TIM1` 或 `TIM8`。

### **Enable simulation port** — 为模块启用仿真端口 `off`（默认） | `on`

选择此参数以添加与 SoC Blockset 兼容的仿真输出端口。

### 事件

### **Enable update generation event input** — 生成更新事件 `off`（默认） | `on`

启用此参数以通过输入端口生成更新事件。

### **Enable capture compare # generation event input** — 生成捕获比较事件 `off`（默认） | `on`

启用此参数以通过输入端口生成捕获比较事件。

#### 依赖关系

可用的 **Enable capture compare # generation event input** 参数数量取决于您在 **Timer module** 中选择的模块。

### **Enable trigger generation event input** — 生成触发事件 `off`（默认） | `on`

启用此参数以通过输入端口生成触发事件。

### **Enable break generation event input** — 生成刹车事件 `off`（默认） | `on`

启用此参数以通过输入端口生成刹车事件。

#### 依赖关系

要启用此参数，请将 **Timer module** 参数设置为 `TIM1`、`TIM8`、`TIM15`、`TIM16`、`TIM17` 或 `TIM20`。

### **Enable break generation 2 event input** — 生成刹车 2 事件 `off`（默认） | `on`

启用此参数以通过输入端口生成刹车 2 事件。

#### 依赖关系

要启用此参数，请将 **Timer module** 参数设置为 `TIM1`、`TIM8` 或 `TIM20`。

### **Sample time** — 读取已启用输出端口的频率 `-1`（默认） | `non-negative real value`

如果未选择任何输入端口，请指定读取已启用输出端口状态的频率（以秒为单位）。输入大于零的值。将此参数指定为 -1 时，Simulink 会根据模型中的模块上下文确定模块的最佳采样时间。

#### 依赖关系

要启用 **Sample time** 参数，请取消选择所有输入端口。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32WBxx Based Boards

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

使用定时器模块在已启用通道上生成方波

使用 PWM Output 模块通过定时器模块在已启用通道上生成方波。

模块输入控制每个通道方波的占空比。

如果将 **Duty Cycle unit** 参数设置为 `Percentage`，输入值 0 产生 0% 占空比，输入值 100 在对应通道上产生 100% 占空比的输出。如果将 **Duty Cycle unit** 参数设置为 `Counts`，模块将输入值写入对应通道的捕获比较寄存器。

如果选择 **Enable frequency input**，模块将相应输入写入定时器的自动重载寄存器以设置计数器周期。

**注意**

您可以在基于 STM32 处理器的板卡上以 Connected IO 模式运行包含 PWM Output 模块的 Simulink® 模型。有关详细信息，请参阅 Communicate with Hardware Using Connected IO。
