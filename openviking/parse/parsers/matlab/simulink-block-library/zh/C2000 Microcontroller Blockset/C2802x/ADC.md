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
chinese_source: official
---

# ADC Type 1-2

## 端口

### 输出

### **Data** — ADC 数据 向量

C281x ADC 的输出是一个 **uint16** 值的向量。由于 C281x ADC 是 12 位转换器，因此输出值范围为 0 到 4095。

**数据类型:** `uint16`

## 参数

### ADC 控制

### **模块** — 选择要使用的模块 `A` (默认) | `B` | `A and B`

指定要使用的 DSP 模块：

- **A** - 显示模块 A 中的 ADC 通道（ADCINA0 到 ADCINA7）。
- **B** - 显示模块 B 中的 ADC 通道（ADCINB0 到 ADCINB7）。
- **A and B** - 显示模块 A 和 B 中的 ADC 通道（ADCINA0 至 ADCINA7 和 ADCINB0 至 ADCINB7）

### **转换模式** — 选择转换类型 `Sequential` (默认) | `Simultaneous`

信号采样类型：

- **顺序** - 按顺序对选定的通道进行采样
- **同时** - 同时对模块 A 和 B 的对应通道进行采样

### **转换开始** — 选择转换开始 `Software` (默认) | `ePWMxA` | `ePWMxB` | `XINT1_ADCSOC`

指定触发转换的信号类型：

触发转换开始的信号类型：

- **软件** - 来自软件的信号。每次采样时都会更新转换值。
- **ePWM#A** / **ePWM#B** / **ePWM#A\_ePWM#B** - 转换的开始由用户定义的 PWM 事件控制。
- **XINT2\_ADCSOC** - 转换的开始由 **XINT2\_ADCSOC** 外部信号引脚控制。

**Start of conversion** 中可用的选项取决于**模块**的设置。下表总结了可供选择的方案。对于每一组 **Start of conversion** 选择，首先给出默认值。

| 模块设置 | 转换开始选项 |
| --- | --- |
| **A** | **软件**、**ePWM#A**、**XINT2\_ADCSOC** |
| **B** | **ePWM#B**，**软件** |
| **A 和 B** | **软件**、**ePWM#A**、**ePWM#B**、**ePWM#A\_ePWM#B**、**XINT2\_ADCSOC** |

### **采样时间** — 模块读取数据的时间间隔 `0.1` (默认)

所选 ADC 通道转换的连续样本组之间的时间间隔（以秒为单位）。这是从结果寄存器读取值的速率。要异步执行此模块，请将**采样时间**设置为 `-1`，并选中**转换结束时发出中断**复选框。

要为不同的 ADC 通道组设置不同的采样时间，您必须向模型中添加单独的 C281x ADC 模块，并为每个模块设置所需的采样时间。

### **数据类型** — 选择输出数据类型 `uint16` (默认) | `double` | `single` | `int8` | `uint8` | `int16` | `int32` | `uint32`

输出数据的日期类型。

### **会话结束时发出中断** — 启用此功能以发布异步中断 `Off` (默认) | `on`

启用此复选框可在每次转换结束时发布异步中断。中断发生在转换结束时。

要异步执行此模块，请将**采样时间**设置为 `-1`。

### **使用 DMA（结合 C28x3x）** — 启用此功能以发布异步中断 `Off` (默认) | `on`

启用此复选框可在每次转换结束时发布异步中断。中断发生在转换结束时。

要异步执行此模块，请将**采样时间**设置为 `-1`。

### 输入通道

### **转换次数** — 为每个转换次数选择 ADC 通道 `ADCINA# and ADCINB#` (默认) | `ADCINA#` | `…`

每个转换次数对应一个特定的 ADC 通道。

在过采样模式下，给定 ADC 通道的信号可以在单个转换序列期间被多次采样。要进行过采样，请为多个转换指定同一个通道。转换后的样本以单个向量的形式输出。

### **使用多个输出端口** — 启用以输出多个端口 `on` (默认) | `off`

如果使用多个 ADC 通道进行转换，则可以为每个输出使用单独的端口，并在模块上显示输出端口。如果使用多个通道但不使用多个输出端口，则数据将以单个向量的向量输出。

## 所属库

C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C2833x

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2016b 中推出**

## 描述

模数转换器 (ADC)

ADC 模块配置 ADC 对连接到选定 ADC 输入引脚的信号执行模数转换。ADC 模块输出代表模拟输入信号的数字值，并将转换后的值存储在数字信号处理器的结果寄存器中。您可以使用此模块捕获和数字化来自外部源（例如信号发生器、频率发生器或音频设备）的模拟信号。使用 C2833x，您可以将 ADC 配置为使用处理器 DMA 模块将数据直接移动到内存，而无需使用 CPU。这样可以释放 CPU 以执行其他任务，并提高系统整体性能。
