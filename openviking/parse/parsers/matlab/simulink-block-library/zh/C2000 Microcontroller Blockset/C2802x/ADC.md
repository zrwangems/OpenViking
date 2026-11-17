---
type: simulink-block
title: 'ADC Type 1-2'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2802x'
documentation_page: 'adctype12'
documentation_source_path: 'ref/adctype12.html'
language: zh-CN
chinese_source: worker-translation
---

# ADC Type 1-2

## 端口

### 输出

### **Data** — ADC 数据向量

C281x ADC 的输出是一个 `uint16` 值的向量。由于 C281x ADC 是 12 位转换器，输出值范围为 0 到 4095。

**数据类型：** `uint16`

## 参数

### ADC 控制

### **Module** — 选择要使用的模块 `A`（默认）| `B` | `A and B`

指定要使用的 DSP 模块：

- `A` — 显示模块 A 中的 ADC 通道（ADCINA0 到 ADCINA7）。
- `B` — 显示模块 B 中的 ADC 通道（ADCINB0 到 ADCINB7）。
- `A and B` — 显示模块 A 和 B 中的 ADC 通道（ADCINA0 到 ADCINA7 以及 ADCINB0 到 ADCINB7）

### **Conversion mode** — 选择转换类型 `Sequential`（默认）| `Simultaneous`

用于信号的采样类型：

- `Sequential` — 按顺序采样所选通道
- `Simultaneous` — 同时采样模块 A 和 B 的对应通道

### **Start of conversion** — 选择转换启动方式 `Software`（默认）| `ePWMxA` | `ePWMxB` | `XINT1_ADCSOC`

指定触发转换的信号类型：

触发转换开始的信号类型：

- `Software` — 来自软件的信号。转换值在每个采样时间更新。
- `ePWM#A` / `ePWM#B` / `ePWM#A_ePWM#B` — 转换启动由用户定义的 PWM 事件控制。
- `XINT2_ADCSOC` — 转换启动由 `XINT2_ADCSOC` 外部信号引脚控制。

**Start of conversion** 中可用的选项取决于 **Module** 设置。下表总结了可用的选项。对于每组 **Start of conversion** 选项，默认值列在最前面。

| Module 设置 | Start of Conversion 选项 |
| --- | --- |
| `A` | `Software`、`ePWM#A`、`XINT2_ADCSOC` |
| `B` | `ePWM#B`、`Software` |
| `A and B` | `Software`、`ePWM#A`、`ePWM#B`、`ePWM#A_ePWM#B`、`XINT2_ADCSOC` |

### **Sample time** — 模块读取数据的间隔 `0.1`（默认）

为所选 ADC 通道转换的连续采样组之间的时间（以秒为单位）。这是从结果寄存器读取值的速率。要异步执行此模块，请将 **Sample Time** 设置为 `-1`，并勾选 **Post interrupt at the end of conversion** 复选框。

要为不同的 ADC 通道组设置不同的采样时间，您必须在模型中添加单独的 C281x ADC 模块，并为每个模块设置所需的采样时间。

### **Data type** — 选择输出数据类型 `uint16`（默认）| `double` | `single` | `int8` | `uint8` | `int16` | `int32` | `uint32`

输出的数据类型。

### **Post interrupt at end of conversion** — 启用以在转换结束时发送异步中断 `Off`（默认）| `on`

勾选此复选框可在每次转换结束时发送异步中断。中断在转换结束时发送。

要异步执行此模块，请将 **Sample Time** 设置为 `-1`。

### **Use DMA (with C28x3x)** — 启用以发送异步中断 `Off`（默认）| `on`

勾选此复选框可在每次转换结束时发送异步中断。中断在转换结束时发送。

要异步执行此模块，请将 **Sample Time** 设置为 `-1`。

### 输入通道

### **Conversions no. #** — 为每个转换编号选择 ADC 通道 `ADCINA# and ADCINB#`（默认）| `ADCINA#` | `…`

要与每个转换编号关联的特定 ADC 通道。

在过采样模式下，给定 ADC 通道上的信号可以在单个转换序列期间被多次采样。要进行过采样，请为多个转换指定相同的通道。转换后的采样作为单个向量输出。

### **Use multiple output ports** — 启用以输出多个端口 `on`（默认）| `off`

如果使用多个 ADC 通道进行转换，您可以为每个输出使用单独的端口，并在模块上显示输出端口。如果使用多个通道但未使用多个输出端口，则数据以单个向量输出。

## 所属库

C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C2833x

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016b 中引入**

## 描述

模数转换器（ADC）

ADC 模块配置 ADC 以对连接到所选 ADC 输入引脚的信号执行模数转换。ADC 模块输出表示模拟输入信号的数字值，并将转换后的值存储在数字信号处理器的结果寄存器中。您可以使用此模块捕获来自外部源（如信号发生器、频率发生器或音频设备）的模拟信号并将其数字化。使用 C2833x 时，您可以配置 ADC 使用处理器 DMA 模块将数据直接移动到内存，而无需使用 CPU。这释放了 CPU 来执行其他任务，并提高了整体系统容量。
