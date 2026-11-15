---
type: simulink-block
title: 'Standard Servo Write'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Motors, Servo Motors, and Motor Drivers'
documentation_page: 'standardservowrite'
documentation_source_path: 'supportpkg/arduino_ref/standardservowrite.html'
language: zh-CN
chinese_source: worker-translation
---

# Standard Servo Write

## 端口

### 输入

### **Data** — 确定标准旋转伺服电机的速度和方向的输入值，范围 [`0`, `255`] 内的正整数

在输入端口发送到模块的值确定与 Arduino 硬件开发板连接的标准旋转伺服电机的旋转速度和方向。例如：

- 向模块发送 `-90` 会产生一个方向的最大旋转速率。
- 向模块发送 `90` 会产生相反方向的最大旋转速率。
- 向模块发送 `0` 会停止伺服电机。
- 向模块发送超出范围的值（例如 `-95` 或 `300`）分别与发送最小或最大输入值的效果相同。

模块输入端口继承上游模块的数据类型，并在内部通过偏移量 `90` 将其转换为 `uint8`。

**数据类型：** `uint8`

## 参数

### **Pin number** — Standard Servo Write 引脚号 `9`（默认值） | scalar

指定标准旋转伺服写入电机输入信号连接到的 Arduino 硬件开发板引脚号。

**注意**

不要将同一引脚号分配给 Simulink 模型中的多个模块。

有关如何分配引脚或查看 Standard Servo Write 模块引脚的信息，请参阅 Pin Mapping for Arduino Timer-Dependent Blocks。

### **View Pin Map** — 用于打开 Arduino 硬件开发板引脚映射的按钮

单击此按钮可查看与您选择的 Arduino 硬件开发板关联的引脚映射表。

## 所属库

Simulink Support Package for Arduino Hardware / Common

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2012a 中引入**

## 描述

将标准伺服电机的轴位置设置为以 degrees 为单位指定的角度

Standard Servo Write 模块根据在 Arduino® 硬件引脚上发送到模块的输入值，将伺服电机的轴位置设置为从 `0` 到 `180` degrees。

您可以在 Arduino 开发板上以 Connected IO 模式运行包含 Standard Servo Write 模块的 Simulink® 模型。

**注意**

如果在 Simulink 模型中同时使用 Standard Servo Write 模块以及 Serial Receive 和 Serial Transmit 模块，请使用更长的采样时间以避免溢出。

### 每个 Simulink 模型允许的最大 Servo 模块数

您可以在 Simulink 模型中使用的 Servo 模块数（Standard Servo Read、Standard Servo Write 和 Continuous Servo Write）取决于 Arduino 硬件开发板上的定时器数量。Arduino 开发板上的每个定时器最多可支持 12 个 Servo 模块。

例如，考虑 Arduino Mega 2560/ADK 开发板。每个 Simulink 模型可使用的最大 Servo 模块数为 48。如果您的 Simulink 模型总共使用 48 个 Servo 模块，并且开发板有 5 个定时器，则定时器 5 支持第一组 12 个（1 到 12）Servo 模块。类似地，定时器 1 支持下一组 12 个（13-24）Servo 模块，定时器 3 支持再下一组 12 个（25-36）Servo 模块，最后，定时器 `4` 支持最后一组 12 个（37-48）Servo 模块。

Servo 模块分组如下：

- **Set 1**：Servo 模块 1 到 12
- **Set 2**：Servo 模块 13 到 24
- **Set 3**：Servo 模块 25 到 36
- **Set 4**：Servo 模块 37 到 48
- **Set 5**：Servo 模块 49 到 60

此表显示了如何根据您使用的 Arduino 开发板为 Servo 模块分配定时器。它还提供了每个 Simulink 模型可使用的最大 Servo 模块数。

| Arduino 开发板类型 | 定时器 | 每个 Simulink 模型的最大 Servo 模块数 |
| --- | --- | --- |
| Uno, Nano 3.0 | 1 | Set 1 |
| Mega 2560/ADK | 1 | Set 2 |
| 3 | Set 3 |
| 4 | Set 4 |
| 5 | Set 1 |
| Leonardo, Robot Control Board, Robot Motor Board, Micro | 1 | Set 1 |
| MKR 1000, MKR WiFi 1010, MKR Zero | TC4 | Set 1 |
| Nano 33 IoT | TC4 | Set 1 |
| Due | TC3\_CH0 | Set 1 |
| TC4\_CH1 | Set 2 |
| TC5\_CH2 | Set 3 |
| TC2\_CH2 | Set 4 |
| TC0\_CH0 | Set 5 |
| Uno R4 WiFi and Minima | FSP Timer | Set 1 |
| Arduino-compatible Teensy 4.0 and 4.1 | PIT0 | Set 4 |
| PIT1 |
| PIT2 |
| PIT3 |
| Arduino-compatible ESP32-WROOM and ESP32-WROVER | 0 | Set 4 |
| 1 |
| 2 |
| 3 |
| Arduino-compatible Pico and Pico W | 0 | Set 1 |
