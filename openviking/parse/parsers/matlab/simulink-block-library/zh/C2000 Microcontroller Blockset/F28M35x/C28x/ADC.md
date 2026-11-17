---
type: simulink-block
title: 'ADC Type 3-5'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'F280013x'
documentation_page: 'adctype35'
documentation_source_path: 'ref/adctype35.html'
language: zh-CN
chinese_source: worker-translation
---

# ADC Type 3-5

## 端口
```yaml
ports:
- name: Data
  summary: ADC 数据向量
  direction: output
  data_types: uint16
```

### 输出

### **Data** — ADC 数据向量

ADC 的输出是一个 `uint16` 值向量。

**数据类型：** `uint16`
## 参数
```yaml
parameters:
- name: ADC Module
  summary: 选择要使用的模块 A（默认）| B | A and B
  group: SOC 触发
- name: ADC Resolution
  summary: 选择 12 位或 16 位分辨率 12-bit (Single-ended input)（默认）| 16-bit (Differential inputs)
  group: SOC 触发
- name: ADC mode
  summary: 选择 ADC 模式 Single-ended input（默认）| Differential inputs
  group: SOC 触发
- name: Sampling mode
  summary: 选择采样类型 Single（默认）| Simultaneous
  group: SOC 触发
- name: SOC trigger number
  summary: 转换启动编号 SOC0（默认）| SOC1 | SOC2 | …
  group: SOC 触发
- name: SOCx acquisition window
  summary: 采集周期的长度 7（默认）| 8 | ...
  group: SOC 触发
- name: SOCx trigger source
  summary: 触发转换启动的源 Software（默认）| EVA | External pin
  group: SOC 触发
- name: ADCINT will trigger SOCx
  summary: 使用 ADC 中断触发 SOC No ADCINT（默认）| ADCINT1 | ADCINT2
  group: SOC 触发
- name: Sample time
  summary: 模块读取数据的间隔 0.1（默认）
  group: SOC 触发
- name: Data type
  summary: 选择输出数据类型 uint16（默认）| double | single | int8 | uint8 | int16 | int32 | uint32
  group: SOC 触发
- name: Post interrupt at EOC trigger
  summary: 在 ADC 触发时发送中断 Off（默认）| on
  group: SOC 触发
- name: Interrupt selection
  summary: ADC 中断选择 ADCINT1（默认）| ADCINT2
  group: SOC 触发
- name: ADC# continuous mode
  summary: 生成 ADC 中断 ADCINT1（默认）| ADCINT2
  group: SOC 触发
- name: Conversions channel
  summary: 选择此 ADC 转换所应用的 ADC 通道 ADCINA0（默认）| ADCINA1 | ADCINA2 | …
  group: 输入通道
```

### SOC 触发

### **ADC Module** — 选择要使用的模块 `A`（默认）| `B` | `A and B`

选择 ADC 模块 1 或 ADC 模块 2 进行转换。

对于支持 Type 4 ADC 的处理器，选择 ADC 模块 A 到 D。

**注意**

**ADC Module** 参数仅适用于支持 Type 3、Type 4 或 Type 5 ADC 的 Texas Instruments C2000 处理器。

### **ADC Resolution** — 选择 12 位或 16 位分辨率 `12-bit (Single-ended input)`（默认）| `16-bit (Differential inputs)`

选择 12 位（单端输入）或 16 位（差分输入）ADC 分辨率选项。

在 12 位模式下，仅支持单端输入。在 16 位模式下，转换器的输入电压通过一对输入引脚采样，这意味着两个通道之间的差分输入被转换。

**注意**

- 此参数仅支持 Texas Instruments C2000 F2837xD、F2838x、F2837xS 和 F28p55x 处理器。
- 在大多数处理器中，16 位（差分输入）ADC 模式默认未启用。
- 对于 TI F29H85x 处理器，您可以为单端或差分 ADC 输入选择 12 位或 16 位分辨率。

### **ADC mode** — 选择 ADC 模式 `Single-ended input`（默认）| `Differential inputs`

选择 `Single-ended input` 或 `Differential inputs` 作为 ADC 模式。此参数仅支持 Texas Instruments F29H85x 处理器。

### **Sampling mode** — 选择采样类型 `Single`（默认）| `Simultaneous`

用于信号的采样类型：

- `Single` — 依次采样所选通道。
- `Simultaneous` — 同时采样模块 1 和模块 2 的对应通道。硬件允许同时采样一对信号中的每个信号。

**注意**

此参数仅支持 Texas Instruments C2000 F28M3x 处理器。

### **SOC trigger number** — 转换启动编号 `SOC0`（默认）| `SOC1` | `SOC2` | `…`

通过编号标识转换启动触发器。在单采样模式下，您可以选择单个触发器。在同时采样模式下，您可以成对选择触发器。

### **SOCx acquisition window** — 采集周期的长度 `7`（默认）| `8` | `...`

以 ADC 时钟周期为单位定义采集周期的长度。此参数的值取决于 SYSCLK 和最小 ADC 采样时间。SOC 采集窗口的值减 1 后设置到 ADC 寄存器的 ACQPS 字段。有关详细信息，请参阅 *TMS320x2802x, 2803x Piccolo Analog-to-Digital Converter (ADC) and Comparator Reference Guide* 的 ADC Acquisition (Sample and Hold) Window 部分。

### **SOCx trigger source** — 触发转换启动的源 `Software`（默认）| `EVA` | `External pin`

选择触发转换启动的源。可用的输入类型如下：

- `Software`。
- `CPU Timers 0/1/2 interrupts`。
- `XINT2 SOC`。
- `ePWMx SOCA and SOCB`。

如果将 **SOCx trigger source** 设置为 `XINT2_XINT2SOC`，请使用 **Hardware Implementation** > **Target hardware resources** 下的 **Input5 pin assignment** 参数来定义触发转换启动的外部 GPIO 引脚。

**注意**

SOCx 触发源输入 **ePWMx SOCA and SOCB** 的范围将根据所选处理器而变化。

### **ADCINT will trigger SOCx** — 使用 ADC 中断触发 SOC `No ADCINT`（默认）| `ADCINT1` | `ADCINT2`

在转换结束时，使用 ADCINT1 或 ADCINT2 中断触发转换启动（SOC）。此循环创建连续的转换序列。默认选择 No ADCINT 会禁用此参数。要设置中断，请选择 Post interrupt at EOC trigger 选项，并选择适当的中断。

### **Sample time** — 模块读取数据的间隔 `0.1`（默认）

为所选 ADC 通道转换的连续采样集之间的时间（以秒为单位）。这是从结果寄存器读取值的速率。要异步执行此模块，请将 **Sample Time** 设置为 `-1`，并选中 **Post interrupt at the end of conversion** 复选框。

### **Data type** — 选择输出数据类型 `uint16`（默认）| `double` | `single` | `int8` | `uint8` | `int16` | `int32` | `uint32`

输出数据的数据类型。

### **Post interrupt at EOC trigger** — 在 ADC 触发时发送中断 `Off`（默认）| `on`

在 ADC 触发 EOC 脉冲时发送中断。当您选择此选项时，对话框将显示 **Interrupt selection** 和 **ADCINT# continuous mode** 选项。

**注意**

对于新处理器，Interrupt selection 提供 **ADCA#, ADCB#** 等选项。

### **Interrupt selection** — ADC 中断选择 `ADCINT1`（默认）| `ADCINT2`

选择 ADC 在触发 EOC 脉冲后发送哪个中断。

#### 依赖关系

要启用此参数，请选择 **Post interrupt at EOC trigger** 参数。

### **ADC# continuous mode** — 生成 ADC 中断 `ADCINT1`（默认）| `ADCINT2`

当 ADC 生成转换结束（EOC）信号时，无论之前的中断标志是否已被确认，都生成 ADCINT# 中断。

#### 依赖关系

要启用此参数，请选择 **Post interrupt at EOC trigger** 参数。

### 输入通道

### **Conversions channel** — 选择此 ADC 转换所应用的 ADC 通道 `ADCINA0`（默认）| `ADCINA1` | `ADCINA2` | `…`

选择此 ADC 转换所应用的输入通道。对于 Type 4 ADC，如果您选择 16 位（差分输入）模式，则两个通道之间的差分电压被转换。
## 所属库

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x C2000 Microcontroller Blockset / F29H85x

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016b 中引入**

## 描述

配置 ADC 以采样模拟引脚并输出数字数据

配置 Type 3 到 Type 5 ADC 以输出从 DSP 上的 ADC 引脚收集的恒定数据流。有关 ADC 类型的详细信息，请参阅 C2000 Real-Time Control Peripheral Reference Guide。

一个 ADC 模块允许读取一个 ADC 通道。使用多个 ADC 模块可读取多个 ADC 通道。
