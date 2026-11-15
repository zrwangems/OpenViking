---
type: simulink-block
title: 'PWM AVR'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / System Peripherals'
documentation_page: 'pwmadvancedavr'
documentation_source_path: 'supportpkg/arduino_ref/pwmadvancedavr.html'
language: zh-CN
chinese_source: worker-translation
---

# PWM AVR

## 端口

### 输入

### **Data** — 输入值，用于确定方波脉冲的宽度 正整数，范围 [0, 255]

块输入端口的值确定方波的宽度，称为*占空比*，Arduino 硬件在指定 PWM 引脚上输出该方波。

例如：

- 将最大值 `255` 发送到块输入端口会产生 100% 的占空比，从而使 PWM 引脚处达到全功率。
- 将最小值 `0` 发送到块输入端口会产生 0% 的占空比，从而使 PWM 引脚处无功率。
- 将中间值发送到块输入端口会产生成比例的占空比和 PWM 引脚处的功率输出。例如，将值 `204` 发送到块输入端口会产生 80% 的占空比和 0.8 (204/255) 的功率。
- 将超出范围的值（例如 `500` 或 `-500`）发送到块输入端口，分别与发送最大值或最小值输入值的效果相同。

块输入端口继承上游模块的数据类型，并在内部将数据转换为 `uint8` 数据类型。

**数据类型：** `uint8`

## 参数

### **Pin number** — PWM 引脚编号 `9`（默认）| 标量

指定 PWM 输入信号连接到的 Arduino 硬件板引脚编号。单击 **查看引脚映射** 以打开 Arduino 引脚映射表。有关如何分配引脚或查看 PWM 模块引脚的更多信息，请参阅 Arduino 定时器相关模块的引脚映射。

**注意**

不要为模型中的多个模块分配相同的引脚编号。

### **Frequency** — 指定 PWM 频率 只读：`Specify`（默认）

此参数为只读。

此只读参数设置为 `Specify`。您可以在 **Desired(Hz)** 参数中指定 PWM 信号的频率。

### **Desired (Hz)** — 期望的 PWM 输出频率 `490.2`（默认）| 标量

指定 PWM 信号的期望输出频率。

### **Achievable (Hz)** — Arduino 板可实现的 PWM 输出频率 只读：标量

此参数为只读。

该模块生成频率最接近 **Desired(Hz)** 参数中指定频率的 PWM 信号。这是一个只读参数。

### **Enable compare match (MCx) interrupt** — 在比较匹配时生成中断的选项 `off`（默认）| `on`

选择此选项以在 Arduino 定时器的每次比较匹配时生成中断。

**注意**

在 Hardware Interrupt 模块的 Interrupt name 参数中选择适当的中断处理程序，以在每次定时器比较匹配时生成中断。

### **Enable overflow/underflow (OVF) interrupt** — 在定时器/计数器溢出/下溢时生成中断的选项 `off`（默认）| `on`

选择此选项以在向上计数期间定时器/计数器达到最大值 (TOP) 时，以及在向下计数期间定时器/计数器达到最小值 (ZERO) 时生成中断。对于定时器/计数器操作的双斜率模式，TOP 值由周期 (PER) 寄存器值定义。

**注意**

在此参数中配置与 PWM 模块中 Hardware Interrupt 模块的 Interrupt name 参数相同的中断处理程序。

## 所属库

Simulink Support Package for Arduino Hardware / Advanced / AVR

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024a 中引入**

## 描述

在 Arduino AVR 内核的模拟输出引脚上生成脉冲宽度调制信号

使用 PWM 模块在 Arduino® AVR 硬件引脚上生成占空比可变的方波脉冲。

**注意**

PWM 模块支持 C/C++ 代码生成。此功能允许您使用 Embedded Coder® 生成 C 和 C++ 代码。

### 支持的 Arduino 板

- Arduino Uno
- Arduino Mega 2560
- Arduino Mega ADK
- Arduino Leonardo
- Arduino Micro
