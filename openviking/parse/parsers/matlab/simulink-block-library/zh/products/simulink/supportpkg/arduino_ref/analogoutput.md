---
type: simulink-block
title: 'Analog Output'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / System Peripherals'
documentation_page: 'analogoutput'
documentation_source_path: 'supportpkg/arduino_ref/analogoutput.html'
language: zh-CN
chinese_source: worker-translation
---

# Analog Output

## 端口

### 输入

### **Port\_1** — 输入电压标量

该模块输入数字电压。

**数据类型：** `uint16`

## 参数

### **DAC pin** — Arduino 板上的 DAC 引脚 `DAC0`（默认） | `DAC1` | `DAC2`

选择要在其上生成模拟电压的 DAC 引脚。

下表列出了该模块支持的 Arduino 板和 DAC 引脚配置。

| Arduino 板 | 支持的 DAC 引脚数 | 支持的 DAC 引脚 | DAC 引脚支持的位数 |
| --- | --- | --- | --- |
| Arduino Due | 两个 | DAC0, DAC1 | 12-bit |
| Arduino Nano 33 BLE Sense | 两个 | DAC0, DAC1 | 12-bit |
| Arduino MKR1000 | 一个 | DAC0 | 10-bit |
| Arduino MKR Wi-Fi 1010 | 一个 | DAC0 | 10-bit |
| Arduino MKR ZERO | 一个 | DAC0 | 10-bit |
| Arduino Nano 33 IoT | 一个 | DAC0 | 10-bit |
| Arduino Uno R4 Wi-Fi | 一个 | DAC0 | 12-bit |
| Arduino Uno R4 Minima | 一个 | DAC0 | 12-bit |
| Arduino compatible ESP32 – WROOM | 两个 | DAC1, DAC2 | 8-bit |
| Arduino compatible ESP32 – WROVER | 两个 | DAC1, DAC2 | 8-bit |

点击 **View pin map** 打开 Arduino Pin Mapping 表。要了解如何为该模块分配引脚，请参阅 Pin Mapping for Arduino Timer-Independent Blocks。

## 所属库

Simulink Support Package for Arduino Hardware / Common

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2014a 中引入**

## 描述

在指定的 DAC 引脚上生成电压

Analog Output 模块在板的指定 DAC 引脚上生成电压。

您可以在 Arduino® 板上以 Connected IO mode 运行包含 Analog Output 模块的 Simulink® 模型。

### 支持的 Arduino 板

- Arduino Due
- Arduino Nano 33 BLE Sense
- Arduino MKR 1000
- Arduino MKR Zero
- Arduino MKR Wi-Fi® 1010
- Arduino Nano 33 IoT
- Arduino compatible ESP32 – WROOM and ESP32 – WROVER
- Arduino Uno R4 Wi-Fi
- Arduino Uno R4 Minima

该模块在 DAC 引脚上输出电压（`Vout`），使得：

```
Vout = VrefX(input/2N-1)+ Voffset
```

下表解释了公式中的变量。

| 变量 | Arduino 板 | | | | 描述 |
| --- | --- | --- | --- | --- | --- |
| | Arduino Due, Arduino 33 BLE Sense | Arduino MKR1000, Arduino MKR Wi-Fi 1010, Arduino ZERO, Arduino Nano 33 IoT | Arduino Uno R4 Wi-Fi, Arduino Uno R4 Minima | Arduino Compatible ESP32 boards | |
| `Vref` | 2.2 | 3.27 | 5 | 3.3 | DAC 引脚的参考电压。 |
| `input` | 0 < `input` < 4095 | 0 < `input` < 1023 | 0 < `input` < 4095 | 0 < `input` < 255 | 模块的输入电压必须在此范围内。任何超出给定范围的值都会使 DAC 引脚上的电压输出饱和。 |
| `N` | 12 | 10 | 12 | 8 | DAC 通道上的位数。 |
| `Voffset` | 0.56 | 0.007 | 0 | 0 | Arduino 板上的偏移电压。 |
