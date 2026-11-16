---
type: simulink-block
title: 'HRCAP'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2803x'
documentation_page: 'hrcap'
documentation_source_path: 'ref/hrcap.html'
language: zh-CN
chinese_source: worker-translation
---

# HRCAP

## 端口

### 输出

### **Rise[0,1]** — 输出捕获值向量

该模块输出两个连续的 **On** 时间值。On 时间值对应于上升沿和下降沿之间的时间。

#### 依赖关系

要启用此端口，请将 **HRCAP mode** 参数设置为 `Normal`。

**数据类型：** `uint16`

### **Fall[0,1]** — 输出捕获值向量

该模块输出两个连续的 **Off** 时间值。Off 时间值对应于下降沿和上升沿之间的时间。

#### 依赖关系

要启用此端口，请将 **HRCAP mode** 参数设置为 `Normal`。

**数据类型：** `uint16`

### **CounterOverflow** — 溢出状态标量

`0` 值表示计数器未溢出。`1` 表示计数器已从最高值溢出到 `0`。

#### 依赖关系

要启用此端口，请将 HRCAP mode 设置为 **Normal**，并选择 **Enable counter overflow output** 参数。

**数据类型：** `uint16`

### **Period** — 输出捕获数据标量

该模块输出波形的周期值。这是 On 和 Off 时间之和。

#### 依赖关系

要启用此端口，请将 **HRCAP mode** 参数设置为 `High resolution`，并将 HRCAP output 设置为 `Period only` 或 `All above(Period, On, Off)`。

**数据类型：** `Fixed point[0,16,16]` | `uint32`

### **On** — 输出捕获数据标量

该模块连续输出 **On** 的值。On 时间值对应于上升沿和下降沿之间的时间。

#### 依赖关系

要启用此端口，请将 **HRCAP mode** 参数设置为 `High resolution`，并将 HRCAP output 设置为 `On time only` 或 `All above(Period, On, Off)`。

**数据类型：** `Fixed point[0,16,16]` | `uint32`

### **Off** — 输出捕获数据标量

该模块连续输出 **Off** 的值。Off 时间值对应于下降沿和上升沿之间的时间。

#### 依赖关系

要启用此端口，请将 **HRCAP mode** 参数设置为 `High resolution`，并将 HRCAP output 设置为 `Off time only` 或 `All above(Period, On, Off)`。

**数据类型：** `Fixed point[0,16,16]` | `uint32`

## 参数

### **HRCAP module** — 选择 HRCAP 模块 `HRCAP1`（默认） | `HRCAP2` | `HRCAP3` | `HRCAP4`

选择捕获输入信号的 HRCAP 模块。

### **HRCAP mode** — 选择 HRCAP 模式 `Normal`（默认） | `High resolution`

选择 HRCAP 模式。

您可以在 normal 或 high resolution 模式下操作 HRCAP 模块。在 high resolution 模式下，校准功能在内部使用额外的 HRCAP 模块和 ePWM 模块中的 HRPWM。

未使用的 HRCAP 模块用于校准，并且最高实例的 HRPWM 用于校准。

为了校准，该模块使用未使用的 HRCAP 模块和最大实例的 HRPWM 模块。此外，该校准过程在后台连续执行。

### **HRCAP clock** — 选择 HRCAP 时钟 `SYSCLKOUT`（默认） | `PLL clock`

为 normal HRCAP 模式选择 HRCAP 时钟。在设置为 normal 模式时，您可以选择 `SYSCLKOUT` 或 `PLL clock`。

PLL clock 是 high resolution 模式下唯一支持的时钟，并根据处理器使用 PLLCLK 或 PLL2CLK。

#### 依赖关系

要启用此参数，请将 **HRCAP mode** 参数设置为 `Normal`。

### **Enable rising edge interrupt** — 检测到上升沿时启用中断 `on`（默认） | `off`

当为 HRCAP 模块检测到上升沿中断时，选择此参数。

### **Enable falling edge interrupt** — 检测到下降沿时启用中断 `on`（默认） | `off`

当为 HRCAP 模块检测到下降沿中断时，选择此参数。

### **Enable counter overflow interrupt** — 检测到计数器溢出时启用中断 `off`（默认） | `on`

当为 HRCAP 模块检测到计数器溢出中断时，选择此参数。

### **Output type** — 选择输出数据类型 `HRCAPCLK cycles`（默认） | `Microseconds` | `uint32` | `fixdt(0,16,16)`

选择 normal 模式和 high resolution 模式下 HRCAP 的输出类型。当您将 Output type 设置为 uint32 时，数据为 Q16 格式。

### **Enable counter overflow output** — 选择以捕获 HCCOUNTER 溢出 `off`（默认） | `on`

启用计数器溢出中断。该模块在 **CounterOverflow** 输出端口输出 HCCOUNTER 溢出状态。

#### 依赖关系

要启用此参数，请将 **HRCAP mode** 参数设置为 `Normal`。

### **HRCAP output** — 高分辨率 HRCAP 输出 `Period only`（默认） | `ON time only` | `Off time only` | `On and Off time` | `All above(Period, On time, Off time )`

选择所需的高分辨率输出。HRCAP output 参数将配置端口 **Period**、**On**、**Off** 或 **All above (Period, On time, Off time)**。

#### 依赖关系

要启用此参数，请将 **HRCAP mode** 参数设置为 `High resolution`。

### **Sample time** — 模块从 HRCAP 读取数据的频率 `0.1`（默认）

使用此参数指定采样之间的时间间隔。要从上游模块继承采样时间，请将此参数设置为 -1。

## 所属库

C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2806x

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023b 中引入**

## 描述

捕获 F2803x 和 F2806x 处理器在 normal 或 high resolution 模式下的脉冲宽度

使用高分辨率捕获 (HRCAP) 模块捕获 normal 或 high resolution 模式下的脉冲宽度，并执行传统和高分辨率 delta 时间测量。该模块对 F2803x 和 F2806x 处理器使用 HRCAP type 0 模块。

**注意**

对于 TI F28002x、F28003x、F28004x、F2838x、F28P55x 和 F28P65x 处理器，您可以使用 eCAP 模块启用 high resolution 模式（HRCAP mode）。有关更多信息，请参阅 C28x eCAP

您可以在 normal 或 high resolution 模式下操作该模块。在 high resolution 模式下，校准功能在 ePWM 模块内部使用额外的 HRCAP 和 HRPWM 模块。该模块在 high resolution 模式下仅支持 PLL clock，并根据处理器使用 PLLCLK 或 PLL2CLK 作为 PLL clock 源。

该模块在 high resolution 模式下不支持 SYSCLK。为使该模块校准输出，时钟频率必须高于 98 MHz，并且 F2806x 的最大 SYSCLK 频率为 90MHz，F2803x 板为 60MHz。

对于 high resolution 模式，仅支持 PLL clock，并且为了校准，时钟频率应在 98 到 120 MHz 范围内。

在 high resolution 模式下，输出将以 Q16 格式的 HCCAPCLK（16-bit HRCAP clock）周期计数表示；在 normal 模式下，输出将是 rise (0,1) 和 fall (0,1) 信号的向量输出，其可以以 microseconds 或 HRCAPCLK cycles 表示。
