---
type: simulink-block
title: 'Encoder'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Timer Peripherals'
documentation_page: 'encoder'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/encoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Encoder

## 描述

以计数为单位测量编码器的旋转

以计数为单位测量编码器的旋转。

`Count` 端口将定时器计数器值输出为 `uint32` 数据。

## 端口

### 输入

### **Reset** — 用于复位定时器计数器的输入端口 `scalar`

使用此端口复位定时器计数器。

提供输入 `1` 时，它会将计数器值设置为：

- `0` - 如果定时器计数器正在向上计数
- `AutoReload Register (ARR) value` - 如果定时器计数器正在向下计数。

#### 依赖关系

要启用此端口，请选择 **启用定时器计数器复位输入** 参数。

**数据类型:** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### 输出

### **Count** — 定时器计数器输出 `scalar`

`Count` 端口输出当前定时器计数器值，数据类型为 `uint32`。

**数据类型:** `uint32`

### **Dir** — 计数器方向输出 `scalar`

模块将计数器的当前方向输出为以下之一：

- 0 - 向上计数器
- 1 - 向下计数器

#### 依赖关系

要启用此端口，请选择 **启用定时器计数器方向输出** 参数。

**数据类型:** `Boolean`

### **Status** — 编码器状态 `scalar`

如果检测到任何索引错误或转换错误，该端口会输出。

- `0` - 未检测到错误
- `1` - 检测到转换错误
- `2` - 检测到索引错误
- `3` - 同时检测到索引错误和转换错误

当 `TIMx_SR` 状态寄存器中的 `IERRF` 标志置位时，检测到索引错误；当 `TERRF` 标志置位时，检测到转换错误。有关详细信息，请参阅 STM32G4xx 参考手册中的 Encoder error management 节。

**注意**

`Status` 端口仅适用于基于 STM32G4xx 的板卡。

#### 依赖关系

要启用此端口，请选择 **输出状态** 参数。

**数据类型:** `uint8`

### **Index Recvd** — 索引脉冲状态 `scalar`

在接收到第一个索引脉冲之前输出 `0`。

- `0` - 直到接收到第一个索引脉冲
- `1` - 接收到第一个索引脉冲之后

**注意**

- `Index Recvd` 端口仅适用于基于 STM32G4xx 的板卡。
- 仅当在 STM32CubeMX 工程（Timer > TIM# > Mode > Combined Channels）中将 **Encoder Mode + index** 设置为 `Combined Channels` 模式时，才启用此端口。

#### 依赖关系

要启用此端口，请选择 **如果接收到第一个索引脉冲则输出** 参数。

**数据类型:** `Boolean`

## 参数

### **定时器模块** — 选择定时器模块 `TIM1` (default) | `TIM2` | `TIM3` | `TIM4` | `TIM5` | `TIM8` | `TIM20`

选择定时器模块。

**注意**

- 确保在 STM32CubeMX 工程中也配置了 `Timer module`。
- 确保 STM32CubeMX 工程中的 **Combined channels mode**（Timer > TIM# > Mode > Combined Channels）为：

  - `Encoder Mode` - 适用于 STM32H7xx、F7xx 和 F4xx 板卡
  - `Encoder Mode or Encoder Mode + Index` - 适用于 STM32G4xx 板卡

### **启用定时器计数器复位输入** — 启用用于复位计数器的输入 `off` (default) | `on`

启用用于复位计数器的输入。

启用此选项会添加一个输入端口 **Reset**，可用于复位定时器计数器值。

### **启用定时器计数器方向输出** — 选择输出计数器方向 `off` (default) | `on`

启用此参数以输出计数器的当前方向。

### **仅在接收到第一个索引脉冲后显示编码器计数** — 选择仅在接收到第一个索引脉冲后显示编码器计数 `off` (default) | `on`

启用此参数以仅在接收到第一个索引脉冲后显示编码器计数。

如果选择此参数，则 counts 端口在接收到第一个索引脉冲之前输出 `0`。接收到第一个索引脉冲后，counts 端口输出当前定时器计数器值。

**注意**

- 此参数仅适用于基于 STM32G4xx 的板卡。
- 仅当在 STM32CubeMX 工程（Timer > TIM# > Mode > Combined Channels）中将 **Encoder Mode + index** 设置为 `Combined Channels` 模式时，才启用此端口。

### **如果接收到第一个索引脉冲则输出** — 选择以显示已接收到第一个索引脉冲 `off` (default) | `on`

当选择 `Output if first index pulse is received` 参数时，模块会配置一个输出端口 `Index Recvd`。此端口在接收到第一个索引脉冲之前输出 `0`。

**注意**

- 此参数仅适用于基于 STM32G4xx 的板卡。
- 仅当在 STM32CubeMX 工程（Timer > TIM# > Mode > Combined Channels）中将 **Encoder Mode + index** 设置为 `Combined Channels` 模式时，才启用此端口。

### **输出状态** — 启用以配置输出状态端口 `off` (default) | `on`

选择此参数以输出读取数据的状态。状态输出 `1` 表示溢出错误。

当选择输出状态参数时，模块会配置一个输出端口 Status。如果检测到任何索引错误或转换错误，该端口会输出。

### **采样时间** — 读取已启用输出端口的频率 `-1` (default) | `non-negative real value`

如果未选择任何输入端口，请指定读取已启用输出端口状态的频率（以秒为单位）。输入大于零的值。当将此参数指定为 -1 时，Simulink® 会根据模型中的模块上下文确定模块的最佳采样时间。

#### 依赖关系

要启用此端口，请取消选择 **启用定时器计数器复位输入** 参数。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32WBxx Based Boards

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**
