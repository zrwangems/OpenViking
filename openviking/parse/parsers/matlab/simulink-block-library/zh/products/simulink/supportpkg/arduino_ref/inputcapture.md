---
type: simulink-block
title: 'Input Capture'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / System Peripherals'
documentation_page: 'inputcapture'
documentation_source_path: 'supportpkg/arduino_ref/inputcapture.html'
language: zh-CN
chinese_source: worker-translation
---

# Input Capture

## 端口

### 输出

### **Frequency** — 外部输入信号的频率 scalar

模块以 Hertz 为单位输出外部输入信号的频率。

**数据类型：** `uint32`

### **Duty Cycle** — 外部输入信号的占空比 `1` 到 `100`

模块以百分比形式输出外部输入信号的占空比。

**数据类型：** `uint8`

## 参数

### **Input capture pin number** — 外部输入信号连接到的引脚 `48` (默认) | scalar

输入外部输入信号连接到的 Arduino 硬件板引脚编号。

**注意**

不要将同一引脚编号分配给模型中的多个模块。

要详细了解如何分配引脚或查看 Input Capture 模块的固定引脚，请参阅 Arduino 定时器相关模块的引脚映射。

### **Sample Time** — 读取外部输入信号的时间间隔 `0.1` (默认) | scalar

输入时间间隔（以 seconds 为单位），模块按该间隔从指定的引脚编号读取外部输入信号。

## 所属库

Simulink Support Package for Arduino Hardware / Common

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2020b 中引入**

## 描述

测量外部输入信号的频率和占空比

Input Capture 模块测量 Arduino® 硬件板数字引脚上外部输入信号的频率和占空比。该模块利用 Arduino 硬件板上可用的定时器计数器以及中断服务例程来计算外部输入信号的频率和占空比。

您可以在 Arduino 板上以 Connected IO 模式运行包含 Input Capture 模块的 Simulink® 模型。

有关使用 PWM、Standard Servo Read、Standard Servo Write、Continuous Servo Write 和 Input Capture 模块的一种或多种组合的 Simulink 模型中数字引脚冲突使用的更多信息，请参阅“Arduino 定时器上的冲突引脚配置”小节。

### 限制

下表列出了 Arduino 板的最大可测量频率及其对应的可测量占空比范围。

| Arduino 板架构 | 最大可测量频率 | 可测量占空比范围 |
| --- | --- | --- |
| AVR | `50`KHz | `20`% 到 `80`% |
| SAMD | `400`KHz |
| SAM | `400`KHz |
| Nano 33 BLE Sense | `50`KHz |

下表列出了使用 Arduino 兼容的 Teensy 4.0 和 4.1 板可测量的最大和最小频率及占空比。

| Arduino 板架构 | CPU 频率 (MHz) | 最小和最大可测量频率范围 | 可测量占空比范围 |
| --- | --- | --- | --- |
| Teensy 4.0 and 4.1 | 1008 | 1.2KHz - 1MHz | `20`% 到 `80`% |
| 960 |
| 912 |
| 816 |
| 720 |
| 600 |
| 528 |
| 450 |
| 396 | 1.2KHz - 500KHz |
| 150 | 1.2KHz - 250KHz |
| 24 | 200Hz - 5KHz |
