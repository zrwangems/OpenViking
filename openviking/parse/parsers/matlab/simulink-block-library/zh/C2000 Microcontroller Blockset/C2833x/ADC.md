---
type: simulink-block
title: 'ADC Type 0'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C280x'
documentation_page: 'adctype0'
documentation_source_path: 'ref/adctype0.html'
language: zh-CN
chinese_source: worker-translation
---

# ADC Type 0

## 端口

### 输出

### **Data** — ADC 数据向量

C281x ADC 的输出是一个 `uint16` 值的向量。由于 C281x ADC 是 12 位转换器，输出值的范围为 0 到 4095。

**数据类型：**

## 参数

### ADC 控制

### **Module** — 选择要使用的模块 `A`（默认）| `B` | `A and B`

指定要使用的 DSP 模块：

- `A` — 显示模块 A 中的 ADC 通道（ADCINA0 至 ADCINA7）。
- `B` — 显示模块 B 中的 ADC 通道（ADCINB0 至 ADCINB7）。
- `A and B` — 显示模块 A 和 B 中的 ADC 通道（ADCINA0 至 ADCINA7 以及 ADCINB0 至 ADCINB7）

然后，使用复选框选择所需的 ADC 通道。

### **Conversion mode** — 选择转换类型 `Sequential`（默认）| `Simultaneous`

用于信号的采样类型：

- `Sequential` — 按顺序采样所选通道
- `Simultaneous` — 同时采样模块 A 和 B 的对应通道

### **Start of conversion** — 选择转换启动方式 `Software`（默认）| `EVA` | `External pin`

指定触发转换的信号类型：

- `Software` — 来自软件的信号
- `EVA` — 来自事件管理器 A 的信号（仅适用于模块 A）
- `EVB` — 来自事件管理器 B 的信号（仅适用于模块 B）
- `External` — 来自外部硬件的信号

### **Sample time** — 模块读取数据的间隔 `0.1`（默认）

为所选 ADC 通道转换的连续采样组之间的时间（以秒为单位）。这是从结果寄存器读取值的速率。要异步执行此模块，请将 **Sample Time** 设置为 `-1`，并勾选 **Post interrupt at the end of conversion** 复选框。

要为不同的 ADC 通道组设置不同的采样时间，必须向模型中添加单独的 C281x ADC 模块，并为每个模块设置所需的采样时间。

### **Data type** — 选择输出数据类型 `uint16`（默认）| `double` | `single` | `int8` | `uint8` | `int16` | `int32` | `uint32`

输出的数据类型。

### **Post interrupt at end of conversion** — 启用以在转换结束时发送异步中断 `Off`（默认）| `on`

勾选此复选框可在每次转换结束时发送异步中断。中断在转换结束时发送。

### 输入通道

### **Number of conversions** — 选择用于转换的 ADC 通道数 `1`（默认）| `2` | `3` | `…`

用于模数转换的 ADC 通道数。

### **Conversions no. #** — 为每个转换编号选择 ADC 通道 `1`（默认）| `2` | `3` | `…`

要与每个转换编号关联的特定 ADC 通道。

在过采样模式下，给定 ADC 通道上的信号可以在单个转换序列期间被多次采样。要进行过采样，请为多个转换指定相同的通道。转换后的采样作为单个向量输出。

### **Use multiple output ports** — 启用以输出多个端口 `off`（默认）| `on`

如果使用多个 ADC 通道进行转换，可以为每个输出使用单独的端口，并在模块上显示输出端口。如果使用多个通道但未使用多个输出端口，则数据以单个向量输出。

## 所属库

C2000 Microcontroller Blockset / C281x

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016b 中引入**

## 描述

模数转换器（ADC）

C281x ADC 模块配置 C281x ADC，对连接到所选 ADC 输入引脚的信号执行模数转换。ADC 模块输出表示模拟输入信号的数字值，并将转换后的值存储在数字信号处理器的结果寄存器中。您可以使用此模块捕获并数字化来自外部源（如信号发生器、频率发生器或音频设备）的模拟信号。
