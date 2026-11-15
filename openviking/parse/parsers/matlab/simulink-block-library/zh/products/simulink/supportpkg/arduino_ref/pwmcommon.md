---
type: simulink-block
title: 'PWM Common'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / System Peripherals'
documentation_page: 'pwmcommon'
documentation_source_path: 'supportpkg/arduino_ref/pwmcommon.html'
language: zh-CN
chinese_source: worker-translation
---

# PWM Common

## 端口

### 输入

### **Data** — 决定方波脉冲宽度的输入值，范围 [0, 255] 内的正整数

发送到模块输入的值决定 Arduino 硬件在指定 PWM 引脚上输出的方波宽度，称为*占空比*。

例如：

- 向模块输入发送最大值 `255` 会产生 100% 占空比，从而使 PWM 引脚输出满功率。
- 向模块输入发送最小值 `0` 会产生 0% 占空比，从而使 PWM 引脚无功率输出。
- 向模块输入发送中间值会在 PWM 引脚上产生成比例的占空比和功率输出。例如，向模块输入发送 `204` 会产生 80% 占空比和功率（204/255 = 0.8）。
- 向模块输入发送超出范围的值（例如 `500` 或 `-500`）分别与发送最大值或最小值的效果相同。

模块输入端口继承上游模块的数据类型，并在内部将其转换为 `uint8`。

**数据类型：** `uint8`

## 参数

### **Pin number** — PWM 引脚编号 `5` (默认) | 标量

指定 PWM 输入信号连接到的 Arduino 硬件板引脚编号。单击 **View pin map** 以打开 Arduino 引脚映射表。有关如何分配引脚或查看 PWM 模块引脚的信息，请参阅 Arduino 定时器相关模块的引脚映射。

**注意**

不要将相同的引脚编号分配给模型中的多个模块。

### **Frequency** — PWM 输出频率 `Default` (默认) | `Specify`

配置 PWM 信号的频率。

当您将 **Frequency** 设置为：

- `Default` –– 模块生成具有默认频率的 PWM 信号。有关不同 Arduino 板上默认 PWM 频率和支持 PWM 的引脚的信息，请参阅 PWM 支持的引脚和频率 以及 Arduino 兼容的 Teensy 板上支持的默认 PWM 频率和引脚。
- `Specify` –– 使用此参数，您可以指定 PWM 信号的频率。使用此选项会启用 **Desired(Hz)** 和 **Achievable(Hz)** 参数。在 **Desired(Hz)** 参数中，指定 PWM 信号的期望频率。模块生成的 PWM 信号，其可实现频率最接近 **Desired(Hz)** 参数中指定的频率。

**注意**

在连接的 I/O 模式下，不能使用 `Specify` 选项。模块仅使用默认频率生成 PWM 信号。

### **Desired (Hz)** — 期望的 PWM 输出频率 `490.2` (默认) | 标量

指定 PWM 信号的期望输出频率。

#### 依赖项

要启用此参数，请将 **Frequency** 设置为 `Specify`。

### **Achievable (Hz)** — Arduino 板可实现的 PWM 输出频率 标量

模块生成的 PWM 信号频率最接近 **Desired(Hz)** 参数中指定的频率。

#### 依赖项

要启用此参数，请将 **Frequency** 设置为 `Specify`。

## 所属库

Simulink Support Package for Arduino Hardware / Common

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2012b 中引入**

## 描述

在模拟输出引脚上生成脉冲宽度调制信号

PWM 模块根据发送到 Arduino® 硬件引脚上的模块输入值，生成占空比变化的方波脉冲。此模块使数字输出能够提供一系列不同的功率水平，类似于模拟输出。

有关当您的 Simulink® 模型包含 PWM、Standard Servo Read、Standard Servo Write、Continuous Servo Write 和 Input Capture 模块时如何选择引脚的详细信息，请参阅 Arduino 定时器上的冲突引脚配置。

### 最大可实现 PWM 频率

下表列出了可在以下 Arduino 板的数字引脚上生成的最大 PWM 频率。

| Arduino 板类型 | 最大可实现 PWM 频率 |
| --- | --- |
| Uno, Nano 3.0, Mega 2560/ADK, Leonardo, Robot Control Board, Robot Motor Board, Micro | `4 MHz` |
| Nano 33 IoT, MKR Zero, MKR 1000 | `24 MHz` |
| Due | `21 MHz` |
| Arduino 兼容的 ESP32 WROOM 和 WROVER | `31.25 KHz` |
| Arduino Uno R4 Wi-Fi® 和 Arduino Uno R4 Minima | `1 MHz` |

### 限制

- 如果在 Simulink 模型中同时使用 PWM 模块以及 Serial Receive 和 Serial Transmit 模块，请使用更长的采样时间以避免超限。
- 下表列出了可在以下 Arduino 板的数字引脚上生成的输出频率上限。

  | Arduino 板类型 | Arduino 引脚编号 | 生成的 PWM 输出频率 (Hz) |
  | --- | --- | --- |
  | Uno, Nano 3.0 | `5`, `6` | `980.4` |
  | `3`, `11` | `31372.55`, `3921.16`, `980.4`, `490.2`, `245.1`, `122.55`, `30.64` |
  | Mega 2560/ADK | `4`, `13` | `980.4` |
  | `9`, `10` | `31372.55`, `3921.16`, `980.4`, `490.2`, `245.1`, `122.55`, `30.64` |
  | Leonardo, Robot Control Board, Robot Motor Board, Micro | `3`, `11` | `980.4` |
