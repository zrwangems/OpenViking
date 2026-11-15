---
type: simulink-block
title: 'PWM SAMD'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / System Peripherals'
documentation_page: 'pwmadvancedsamd'
documentation_source_path: 'supportpkg/arduino_ref/pwmadvancedsamd.html'
language: zh-CN
chinese_source: worker-translation
---

# PWM SAMD

## 端口

### 输入

### **Data** — 决定方波脉冲宽度的输入值，范围为 [0, 255] 的正整数

模块输入端口处的值决定 Arduino 硬件在指定 PWM 引脚上输出的方波宽度，称为*占空比*。

例如：

- 将最大值 `255` 发送到模块输入端口会产生 100% 的占空比，这会在 PWM 引脚上产生满功率。
- 将最小值 `0` 发送到模块输入端口会产生 0% 的占空比，这会在 PWM 引脚上产生无功率。
- 将中间值发送到模块输入端口会产生成比例的占空比和 PWM 引脚输出功率。例如，将值 `204` 发送到模块输入端口会产生 80% 的占空比和功率（204/255 = 0.8）。
- 将超出范围的值（例如 `500` 或 `-500`）发送到模块输入端口，其效果分别与发送最大或最小输入值相同。

模块输入端口继承上游模块的数据类型，并在内部将数据转换为 `uint8` 数据类型。

**数据类型：** `uint8`

## 参数

### **Pin number** — PWM 引脚编号 `5`（默认）| 标量

指定 PWM 输入信号连接到的 Arduino 硬件板引脚编号。点击 **View pin map** 以打开 Arduino 引脚映射表。有关如何分配引脚或查看 PWM 模块引脚的信息，请参阅 Arduino 定时器相关模块的引脚映射。

**注意**

不要将同一个引脚编号分配给模型中的多个模块。

### **Frequency** — PWM 输出频率 `Specify`（默认）

此只读参数显示 PWM 信号的输出频率。

### **Desired (Hz)** — 期望的 PWM 输出频率 `490.2`（默认）| 标量

指定 PWM 信号的期望输出频率。

### **Achievable (Hz)** — Arduino 板可实现的 PWM 输出频率 标量

模块生成 PWM 信号时采用的频率最接近 **Desired(Hz)** 参数中指定的频率。

### **Wave generation mode** — 定时器/计数器波形生成模式 `Dual-slope, interrupt/event at TOP (DSTOP)`（默认）| `Dual-slope, interrupt/event at ZERO (DSBOTTOM)` | `Dual-slope, interrupt/event at TOP and ZERO (DSBOTH)`

选择以下选项之一，以确定模块何时生成双斜坡定时器波形。

- `Dual-slope, interrupt/event at TOP (DSTOP)` — 当定时器/计数器值达到最大值时，模块生成 PWM 中断/事件。
- `Dual-slope, interrupt/event at ZERO (DSBOTTOM)` — 当定时器/计数器值达到最小值时，模块生成 PWM 中断/事件。
- `Dual-slope, interrupt/event at TOP and ZERO (DSBOTH)` — 当定时器/计数器值同时达到最大值和最小值时，模块生成 PWM 中断/事件。

### **Enable compare match (MCx) interrupt** — 启用定时器/计数器匹配或比较中断 `off`（默认）| `on`

选择此选项可在 Arduino 定时器每次比较匹配时生成中断。

### **Enable overflow/underflow (OVF) interrupt** — 启用定时器/计数器溢出/下溢中断 `on`（默认）| `off`

选择此选项可在向上计数期间定时器/计数器达到最大值 (TOP) 时，以及在向下计数期间定时器/计数器达到最小值 (ZERO) 时生成中断。对于定时器/计数器的双斜坡操作模式，TOP 值由 Period (PER) 寄存器值定义。

### **Invert output polarity** — 反转 PWM 输出波形的极性 `off`（默认）| `on`

选择此选项可反转 PWM 模块输出波形的极性。

## 所属库

Simulink Support Package for Arduino Hardware / Advanced / SAMD

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023b 中引入**

## 描述

在 Arduino SAMD21 内核的模拟输出引脚上生成脉宽调制信号

使用 PWM 模块在 Arduino® SAMD 21 硬件引脚上生成占空比可变的方波脉冲。

**注意**

PWM 模块支持 C/C++ 代码生成。此功能允许您使用 Embedded Coder® 生成 C 和 C++ 代码。

### 支持的 Arduino 板

- Arduino MKR 1000
- Arduino MKR ZERO
- Arduino MKR Wi-Fi® 1010
- Arduino Nano 33 IoT
