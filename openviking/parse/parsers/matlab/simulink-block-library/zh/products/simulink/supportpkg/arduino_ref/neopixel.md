---
type: simulink-block
title: 'NeoPixel'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / System Peripherals'
documentation_page: 'neopixel'
documentation_source_path: 'supportpkg/arduino_ref/neopixel.html'
language: zh-CN
chinese_source: worker-translation
---

# NeoPixel

## 端口

### 输入

### **LEDPosition** — 要闪烁的 NeoPixel LED 位置矩阵

使用此端口指定 NeoPixel 灯带上要闪烁的 LED。将 LED 位置输入为 *N*×1 矩阵，其中 *N* 的范围为 `0` 到（像素数 - `1`）。确保输入到此端口的值必须介于 `0` 到 No. of pixel 之间。模块会忽略超出此范围的任何输入值。

**数据类型：** `uint16`

### **RGBColor** — NeoPixel LED 灯带的 RGB 分量矩阵

使用此端口指定 NeoPixel LED 灯带的 RGB 分量。将这些分量指定为 *N*×3 矩阵。每个像素的 R、G 和 B 值必须介于 `0` 到 `255` 之间。

#### 依赖关系

要启用此端口，请将 **Color format of pixel** 设置为 `GRB`、`RGB`、`RBG` 或 `BRG`。

**数据类型：** `uint8`

### **RGBWColor** — NeoPixel LED 灯带的 RGBW 分量矩阵

使用此端口指定 NeoPixel LED 灯带的 RGBW 分量。将这些分量指定为 *N*×4 矩阵。每个像素的 R、G、B 和 W 值必须介于 `0` 到 `255` 之间。

#### 依赖关系

要启用此端口，请将 **Color format of pixel** 设置为 `RGBW`、`RBGW`、`WRGB`、`WGRB`、`WRBG`、`WBGR`、`GRBW`、`GBRW`、`BRGW` 或 `BGRW`。

**数据类型：** `uint8`

### **Brightness** — 调整每个 LED 像素的亮度，范围 [0, 255] 中的正整数

使用此端口调整每个 NeoPixel LED 的亮度。输入值 255 表示最大 LED 亮度，而输入值 0 表示最小 LED 亮度

**数据类型：** `uint8`

### **Reset** — 重置 NeoPixel LED 灯带像素值的选项 `0` | `1`

使用此端口重置或接受 NeoPixel LED 灯带的像素值。

- `0` — 模块接受 NeoPixel LED 灯带的 RGB 和 RGBW 分量。
- `1` — 模块重置 NeoPixel LED 灯带的所有像素。

**数据类型：** `Boolean`

## 参数

### **Digital pin (Din)** — Arduino 开发板上的数字引脚 `6`（默认） | Arduino 开发板引脚编号

指定 NeoPixel 灯带所连接的 Arduino 开发板的数字引脚编号。单击 **View pin map** 打开 Arduino 引脚映射表。有关如何分配引脚或查看 NeoPixel 模块引脚的详细信息，请参阅 Pin Mapping for Arduino Timer-Independent Blocks。

### **No. of pixel** — LED 像素数 `24`（默认） | 范围 [0, 1023] 中的正整数

指定 NeoPixel 灯带中连续 LED 像素的数量。

### **Color format of pixel** — NeoPixel 颜色格式 `GRB`（默认） | `RGB` | `RBG` | `BRG` | `RGBW` | `RBGW` | `WRGB` | `WGRB` | `WRBG` | `WBGR` | `GRBW` | `GBRW` | `BRGW` | `BGRW`

设置 NeoPixel 颜色顺序格式。

### **Frequency of pixel** — NeoPixel 比特流频率 `800KHz`（默认） | `400KHz`

选择 NeoPixel LED 灯带从 Arduino 开发板接收数据的频率。

**注意**

对于使用 800 kHz 比特流频率的 NeoPixel 灯带，在 Arduino 开发板向灯带发送最后一个像素数据后，流式传输必须停止至少 50 μsec，以便新颜色锁存到 LED 灯带上。

## 所属库

Simulink Support Package for Arduino Hardware / Common

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024a 中引入**

## 描述

控制 RGB 和 RGBW Adafruit NeoPixel LED 灯带的颜色和亮度

使用 NeoPixel 模块控制 RGB 或 RGBW Adafruit® NeoPixel LED 灯带的颜色和亮度。使用该模块，可以为三色格式（红–绿–蓝）或四色格式（红–绿–蓝–白）的 NeoPixel 灯带设置单个像素的颜色。该模块支持在 NeoPixel LED 灯带上配置最多 1024 个像素。

### 限制

- NeoPixel 模块目前不支持 Arduino® Nano 33 BLE Sense 开发板。
- 在一个 Simulink® 模型中最多可以使用 `10` 个 NeoPixel 模块，并将该模型部署到 Arduino 开发板。
- 如果在 Simulink 模型中同时使用 NeoPixel 模块与 Input Capture、Servo Write、Standard Servo Read、SAMD Hardware Interrupt、AVR Hardware Interrupt、External Interrupt 或 Encoder 模块，NeoPixel 模块可能无法按预期工作。
