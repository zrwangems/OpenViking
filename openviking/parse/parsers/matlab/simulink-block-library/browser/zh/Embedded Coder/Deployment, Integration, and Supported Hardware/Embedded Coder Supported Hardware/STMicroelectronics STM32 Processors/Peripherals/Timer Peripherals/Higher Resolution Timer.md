---
type: simulink-block
title: 'Higher Resolution Timer'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Timer Peripherals'
documentation_page: 'higherresolutiontimer'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/higherresolutiontimer.html'
language: zh-CN
chinese_source: worker-translation
---

# Higher Resolution Timer

## 端口

### 输入

### **CMP#** — 计数器比较端口 `scalar`

使用此端口启用输入端口计数器比较。

#### 依赖关系

要启用此端口，请在 **计数器比较** 选项卡下选择 **启用比较# (CMP#) 输入** 参数。

**数据类型：** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **PER** — 定时器的频率计数 `scalar`

此端口处的输入决定计数器的频率。根据 STM32CubeMX 的预装载配置，该值要么直接写入活动寄存器，要么写入预装载寄存器。

16 位定时器的频率计数介于 `0` 到 `0xFFFF` 之间。

#### 依赖关系

要启用此端口，请在 **主** 选项卡下选择 **启用频率输入** 参数。

**数据类型：** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **CEN** — 用于启用计数器的端口 `scalar`

使用此端口启用输入端口计数器。将此端口设置为以下值之一。

- `0` - 禁用计数器
- `1` - 启用计数器

#### 依赖关系

要启用此端口，请在 **主** 选项卡下选择 **启用输入以启用/禁用计数器** 参数。

**数据类型：** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **CAL** — 用于启用校准输入的端口 `scalar`

使用此端口启用校准输入。

#### 依赖关系

要启用此端口，请在 **主** 选项卡下选择 **启用延迟锁定环(DLL)校准输入** 参数。

**数据类型：** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **SWU** — 用于生成更新事件的输入 `scalar`

使用此端口生成更新事件。当指定值为 `1` 时，该端口生成更新事件。

#### 依赖关系

要启用此端口，请在 **事件** 选项卡下选择 **启用更新生成事件输入** 参数。

**数据类型：** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **SST#** — 软件置位触发 `scalar`

使用此端口进行软件置位触发事件输入。当指定值为 `1` 时，该端口生成软件置位触发事件。

#### 依赖关系

要启用此端口，请在 **事件** 选项卡下选择 **启用通道#软件置位触发(SST#)事件输入** 参数。

**数据类型：** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### **SRT#** — 软件复位触发 `scalar`

使用此端口进行软件复位触发事件输入。当指定值为 `1` 时，该端口生成软件复位触发事件。

#### 依赖关系

要启用此端口，请在 **事件** 选项卡下选择 **启用通道#软件复位触发(SRT#)事件输入** 参数。

**数据类型：** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

### 输出

### **ODS#** — 通道输出的状态 `scalar`

输出所选通道的状态。

#### 依赖关系

要启用此端口，请在 **主** 选项卡下选择 **启用通道#状态输出** 参数。

**数据类型：** `Boolean` | `uint16` | `uint32` | `int8` | `uint8` | `int16` | `int32` | `uint64` | `int64` | `single` | `double`

## 参数

### 主

### **定时器模块** — 选择定时器模块 `TIMERA`（默认） | `TIMERB` | `TIMERC` | `TIMERD` | `TIMERE` | `TIMERF` | `MAINTIMER`

选择定时器模块。

**注意**

确保 `Timer module` 也在 STM32CubeMX 项目中配置。

### **启用通道#** — 选择通道 `Enable channel 1`（默认） | `Enable channel 2`

启用希望模块在其上生成 PWM 输出的通道。输入会考虑相应通道的占空比。根据启用的计数器比较输入以及用于匹配事件的输出置位/复位 STM32CubeMX 配置，可以在 channel1 或 channel2 或两者上生成高分辨率脉宽调制波形。

每个 **定时器模块** 可以有一到六个通道。可用通道数因所选定时器模块而异。启用相应定时器支持的通道。默认情况下，模块启用 **channel 1**。

**注意**

确保要启用其通道的定时器模块已在 STM32CubeMX 项目中配置。

### **启用频率输入** — 通过输入端口启用频率 `off`（默认） | `on`

启用此参数以设置定时器的频率。所有通道输出具有相同的频率。

当选择 **启用频率输入** 参数时，模块配置一个输入端口 PER。

**注意**

HRTIM 模块支持通过模块输入更新周期寄存器。对于给定的预分频器设置，可生成的最小频率存在限制。有关详细信息，请参阅 STM32H7xx TRM 手册。

### **启用输入以启用/禁用计数器** — 通过输入端口启用计数器 `off`（默认） | `on`

通过输入端口启用或禁用计数器。如果未选择此参数，则在模型初始化期间启用计数器。

当选择 **启用输入以启用/禁用计数器** 参数时，模块配置一个输入端口 CEN。

### **启用通道#状态输出** — 启用以配置通道输出状态端口 `off`（默认） | `on`

选择此参数以输出通道状态。状态输出 `1` 表示溢出错误。

当选择 **启用通道#状态输出** 参数时，模块配置一个输出端口 ODS。该端口输出通道输出消息的状态。

### **启用延迟锁定环 (DLL) 校准输入** — 启用以配置输出状态端口 `off`（默认） | `on`

选择此参数以输出读取数据的状态。状态输出 `1` 表示溢出错误。

当选择 **启用延迟锁定环 (DLL) 校准输入** 参数时，模块配置一个输入端口 CAL。

### 计数器比较

### **CMP 单位** — 比较寄存器使用的单位 `Counts`（默认） | `Percentage`

选择比较寄存器使用的 `Counts` 或 `Percentage` 单位。

### **启用比较# (CMP#) 输入** — 生成更新事件 `off`（默认） | `on`

启用此参数以启用计数器比较输入端口。

当选择 **启用比较# (CMP#) 输入** 参数时，模块配置一个输入端口 CMP#。

### 事件

### **启用更新生成事件输入** — 生成更新事件 `off`（默认） | `on`

启用此参数以通过输入端口生成更新事件。

当选择 **启用更新生成事件输入** 参数时，模块配置一个输入端口 SWU。

### **启用通道#软件置位触发(SST#)事件输入** — 软件置位触发 `off`（默认） | `on`

启用此参数以设置通道软件置位触发事件输入。

当选择 **启用通道#软件置位触发(SST#)事件输入** 参数时，模块配置一个输入端口 SST#。

### **启用通道#软件复位触发(SRT#)事件输入** — 软件复位触发 `off`（默认） | `on`

启用此参数以复位通道软件触发事件输入。

当选择 **启用通道#软件复位触发(SRT#)事件输入** 参数时，模块配置一个输入端口 SRT#。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

## 描述

生成高分辨率脉宽调制波形

使用高分辨率定时器模块在已启用的输出上生成高分辨率脉宽调制波形。

Higher Resolution Timer 模块的输入控制每个输出方波的频率和占空比（通过比较输入）。

**注意**

某些 HRTIM 寄存器启用了预装载。如果启用了预装载，请确保至少配置一个更新事件，以启用将预装载寄存器复制到活动寄存器。
