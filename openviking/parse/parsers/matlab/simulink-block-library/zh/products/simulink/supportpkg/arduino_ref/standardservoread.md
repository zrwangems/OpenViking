---
type: simulink-block
title: 'Standard Servo Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Motors, Servo Motors, and Motor Drivers'
documentation_page: 'standardservoread'
documentation_source_path: 'supportpkg/arduino_ref/standardservoread.html'
language: zh-CN
chinese_source: worker-translation
---

# Standard Servo Read

## 端口

### 输出

### **Data** — 标准舵机轴旋转角，范围为 [`0`, `180`] 的正整数

该模块输出与 Arduino 硬件板连接的标准舵机的轴旋转角，从 `0` 到 `180` degrees。在没有硬件的情况下进行仿真时，该模块输出零。

**数据类型：** `uint8`

## 参数

### **引脚编号** — 标准舵机读取引脚编号 `2`（默认）| scalar

指定标准舵机读取电机输入信号所连接的 Arduino 硬件板引脚编号。

**注意**

不要将同一个引脚编号分配给 Simulink 模型中的多个模块。

有关如何分配引脚或查看 Standard Servo Read 模块的引脚的详细信息，请参阅 Arduino 定时器相关模块的引脚映射。

### **采样时间** — 模块读取轴旋转数据的时间间隔 `0.1`（默认）| scalar

输入该模块读取标准舵机轴旋转角的时间间隔，单位为 seconds。最小采样时间为 `0.000001`。

### **查看引脚映射** — 打开 Arduino 硬件板的引脚映射按钮

单击此按钮可查看与您选择的 Arduino 硬件板关联的引脚映射表。

## 所属库

Simulink Support Package for Arduino Hardware / Common

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2012a 中引入**

## 描述

以 degrees 为单位测量标准舵机的轴位置

Standard Servo Read 模块以 degrees 为单位测量与 Arduino® 硬件板连接的标准舵机的轴位置。

您可以在 Arduino 板上以 Connected IO 模式运行包含 Standard Servo Read 模块的 Simulink® 模型。

**注意**

如果在 Simulink 模型中同时使用 Standard Servo Read 模块以及 Serial Receive 和 Serial Transmit 模块，请使用更长的采样时间以避免溢出。

### 每个 Simulink 模型允许的最大 Servo 模块数

在 Simulink 模型中可使用的 Servo 模块（Standard Servo Read、Standard Servo Write 和 Continuous Servo Write）数量取决于 Arduino 硬件板上的定时器数量。Arduino 板上的每个定时器最多可支持 12 个 Servo 模块。

例如，考虑 Arduino Mega 2560/ADK 板。每个 Simulink 模型可使用的最大 Servo 模块数为 48。如果您的 Simulink 模型总共使用 48 个 Servo 模块，并且该板有 5 个定时器，则定时器 5 支持第一组 12 个（1 到 12）Servo 模块。类似地，定时器 1 支持下一组 12 个（13-24）Servo 模块，定时器 3 支持再下一组 12 个（25-36）Servo 模块，最后，定时器 `4` 支持最后一组 12 个（37-48）Servo 模块。

Servo 模块分组如下：

- **Set 1**：Servo 模块 1 到 12
- **Set 2**：Servo 模块 13 到 24
- **Set 3**：Servo 模块 25 到 36
- **Set 4**：Servo 模块 37 到 48
- **Set 5**：Servo 模块 49 到 60

此表显示了如何根据所使用的 Arduino 板将定时器分配给 Servo 模块。它还提供了每个 Simulink 模型可使用的最大 Servo 模块数。

| Arduino 板类型 | 定时器 | 每个 Simulink 模型的最大 Servo 模块数 |
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
| Uno R4 WiFi 和 Minima | FSP Timer | Set 1 |
| Arduino 兼容的 Teensy 4.0 和 4.1 | PIT0 | Set 4 |
| PIT1 |
| PIT2 |
| PIT3 |
| Arduino 兼容的 ESP32-WROOM 和 ESP32-WROVER | 0 | Set 4 |
| 1 |
| 2 |
| 3 |
| Arduino 兼容的 Pico 和 Pico W | 0 | Set 1 |
