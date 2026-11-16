---
type: simulink-block
title: 'ADC Type 3-5'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Analog System'
documentation_page: 'adctype35'
documentation_source_path: 'ref/adctype35.html'
language: zh-CN
chinese_source: official
---

# ADC Type 3-5

## 端口

### 输出

### **Data** — ADC 数据 向量

ADC 的输出是一个 **uint16** 值的向量。

**数据类型:** `uint16`

## 参数

### SOC 触发器

### **ADC 模块** — 选择要使用的模块 `A` (默认) | `B` | `A and B`

选择 ADC 模块 1 或 ADC 模块 2 进行转换。

对于支持 4 型 ADC 的处理器，请选择 ADC 模块 A 至 D。

**注意**

**ADC 模块**参数仅适用于支持 Type 3、Type 4 或 Type 5 ADC 的 Texas Instruments C2000 处理器。

### **ADC 分辨率** — 选择 12 位或 16 位分辨率 `12-bit (Single-ended input)` (默认) | `16-bit (Differential inputs)`

选择 12 位（单端输入）或 16 位（差分输入）ADC 分辨率选项。

在 12 位模式下，仅支持单端输入。在 16 位模式下，转换器的输入电压通过一对输入引脚进行采样，这意味着两个通道之间的差分输入将被转换。

**注意**

- 此参数仅支持 Texas Instruments C2000 F2837xD、F2838x、F2837xS 和 F28p55x 处理器。
- 大多数处理器默认情况下未启用 16 位（差分输入）ADC 模式。
- 对于 TI F29H85x 处理器，您可以选择 12 位或 16 位分辨率作为单端或差分 ADC 输入。

### **ADC 模式** — 选择 ADC 模式 `Single-ended input` (默认) | `Differential inputs`

选择 `Single-ended input` 或 `Differential inputs` 作为 ADC 模式。此参数仅适用于 Texas Instruments F29H85x 处理器。

### **采样模式** — 选择采样类型 `Single` (默认) | `Simultaneous`

信号采样类型：

- **单视图** - 按顺序对选定的通道进行采样。
- **同时** - 同时对模块 1 和 2 的对应通道进行采样。该硬件允许同时对一对信号中的每个信号进行采样。

**注意**

此参数仅适用于 Texas Instruments C2000 F28M3x 处理器。

### **SOC 触发器编号** — 转换开始编号 `SOC0` (默认) | `SOC1` | `SOC2` | `…`

通过编号识别转化开始触发因素。在单次采样模式下，您可以选择单个触发器。在同步采样模式下，您可以成对选择触发器。

### **SOCx 采集窗口** — 收购期长度 `7` (默认) | `8` | `...`

以 ADC 时钟周期为单位定义采集周期的长度。该参数的值取决于 SYSCLK 和最小 ADC 采样时间。SOC 采集窗口的值减去 1，并设置到 ADC 寄存器中的 ACQPS 字段。有关更多信息，请参阅 *TMS320x2802x、2803x Piccolo 模数转换器 (ADC) 和比较器参考指南*中的 ADC 采集（采样保持）窗口部分。

### **SOCx 触发器源** — 触发转化开始的来源 `Software` (默认) | `EVA` | `External pin`

选择触发转化的来源。可输入以下几种类型的数据：

- **软件**。
- **CPU 计时器 0/1/2 中断**。
- **XINT2 SOC**。
- **ePWMx SOCA 和 SOCB**。

如果将 **SOCx 触发源**设置为 `XINT2_XINT2SOC`，则使用**硬件实现** > **目标硬件资源**中的**输入 5 引脚分配**参数来定义触发转换开始的外部 GPIO 引脚。

**注意**

SOCx 触发源输入 **ePWMx SOCA 和 SOCB** 范围将根据所选处理器而变化。

### **ADCINT 将触发 SOCx** — 使用 ADC 中断触发 SoC `No ADCINT` (默认) | `ADCINT1` | `ADCINT2`

转换结束时，使用 ADCINT1 或 ADCINT2 中断触发转换开始 (SOC)。此循环会产生连续的转换序列。默认选择“无 ADCINT”会禁用此参数。要设置中断，请选择“EOC 触发后中断”选项，然后选择相应的中断。

### **采样时间** — 模块读取数据的时间间隔 `0.1` (默认)

所选 ADC 通道转换的连续样本组之间的时间间隔（以秒为单位）。这是从结果寄存器读取值的速率。要异步执行此模块，请将**采样时间**设置为 `-1`，并选中**转换结束时发出中断**复选框。

### **数据类型** — 选择输出数据类型 `uint16` (默认) | `double` | `single` | `int8` | `uint8` | `int16` | `int32` | `uint32`

输出数据的日期类型。

### **在 EOC 触发时发出中断** — ADC 触发时发出中断 `Off` (默认) | `on`

当 ADC 触发 EOC 脉冲时，发出中断。选择此选项后，对话框将显示**中断选择**和 **ADCINT#连续模式**选项。

**注意**

对于新处理器，中断选择提供选项 **ADCA#, ADCB#**等等。

### **中断选择** — ADC 中断选择 `ADCINT1` (默认) | `ADCINT2`

选择触发 EOC 脉冲后 ADC 后置中断的中断方式。

#### 依赖关系

要启用此参数，请选择 **Post interrupt at EOC trigger** 参数。

### **ADC# 连续模式** — 生成 ADC 中断 `ADCINT1` (默认) | `ADCINT2`

当 ADC 产生转换结束 (EOC) 信号时，无论之前的中断标志是否已被确认，都会生成 ADCINT# 中断。

#### 依赖关系

要启用此参数，请选择 **Post interrupt at EOC trigger** 参数。

### 输入通道

### **转换通道** — 选择此 ADC 转换适用的 ADC 通道 `ADCINA0` (默认) | `ADCINA1` | `ADCINA2` | `…`

选择此 ADC 转换所适用的输入通道。对于 4 型 ADC，如果选择 16 位（差分输入）模式，则会转换两个通道之间的差分电压。

## 所属库

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x C2000 Microcontroller Blockset / F29H85x

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2016b 中推出**

## 描述

配置 ADC 以对模拟引脚进行采样并输出数字数据

配置 3 型至 5 型 ADC 输出从 DSP 上的 ADC 引脚收集的持续数据流。有关 ADC 类型的更多信息，请参阅 C2000 实时控制外设参考指南。

ADC 模块允许读取一个 ADC 通道。使用多个 ADC 模块读取多个 ADC 通道。
