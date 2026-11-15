---
type: simulink-block
title: 'OV2640 Camera Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Sensors / Vision Sensors'
documentation_page: 'ov2640camerasensor'
documentation_source_path: 'supportpkg/arduino_ref/ov2640camerasensor.html'
language: zh-CN
chinese_source: worker-translation
---

# OV2640 Camera Sensor

## 端口

### 输入

### **Capture trigger** — 启动图像捕获 `0` | `1`

向模块发送以启动图像捕获的信号输入。

**数据类型：** `uint8`
### 输出

### **Data** — 原始 JPEG 图像数据向量

原始 JPEG 图像数据，其值范围为 0—255。图像大小取决于 JPEG 编码压缩比，并小于实际分辨率。

**数据类型：** `uint8`

### **Data length** — 数据大小的 scalar

原始 JPEG 图像数据的大小。

**数据类型：** `uint16`

### **Status** — 捕获结果状态 scalar

**Status** 端口输出捕获操作的状态。
每个值对应特定的数据输出。

| 场景 | 状态值 | 数据输出 |
| --- | --- | --- |
| 有效输出 | `0` | 有效原始图像数据 |
| 实际图像数据的大小超过最大图像缓冲区大小 | `1` | `0` |
| 无效输出 | `2` | `0` |
| 传感器初始化错误 | `3` | `0` |
| 捕获超时 | `4` | `0` |

**数据类型：** `uint8`

## 参数

### **I2C module** — I2C 通信模块 `0`（默认）| scalar

指定 Arduino 硬件上用于与传感器外设通信的 I2C 模块。有关 Arduino 引脚映射以及硬件开发板支持的模块的详细信息，请参阅 Pin Mapping for Arduino Timer-Independent Blocks。

### **I2C address** — 用于与摄像头传感器通信的外设地址 `0x30`（默认）| scalar

OV2640 摄像头传感器与 Arduino 硬件通信的外设地址。

### **SPI module** — SPI 通信模块 `0`（默认）| scalar

指定 Arduino 硬件上用于与 SPI 外设通信的 SPI 模块。有关 Arduino 引脚映射以及硬件开发板支持的模块的详细信息，请参阅 Pin Mapping for Arduino Timer-Independent Blocks。

### **Chip select pin** — Arduino 开发板的片选引脚 `10`（默认）| 目标硬件引脚

要将带有 OV2640 传感器的 ArduCam Mini 2MP Plus 摄像头模块连接到 Arduino 开发板，请输入 Arduino 开发板的片选引脚。有关 Arduino 开发板片选引脚的详细信息，请参阅 Pin Mapping for Arduino Timer-Independent Blocks。

### **Product ID** — 传感器的 Product ID `0x41`（默认）| `0x42`

选择传感器的 Product ID。

### **Image Resolution** — 图像尺寸 `160x120`（默认）| `176x144` | `320x240` | `352x288` | `640x480` | `800x600` | `1024x768` | `1280x1024` | `1600x1200`

选择要捕获的图像的尺寸，以 pixels 为单位。

有关支持的开发板可用的图像分辨率列表，请参阅支持的开发板。

### **Max image buffer size** — 图像最大大小 `3500`（默认）| 任意非负值

输入图像的最大大小，以 bytes 为单位。对于所选分辨率，图像大小必须由您使用的硬件支持。

**注意**

`max image buffer size` 不得大于所选 `image resolution` 的乘积。

### **Capture timeout** — Capture timeout 的持续时间 `1`（默认）| 任意非负值

指定 capture timeout，以 seconds 为单位。Capture timeout 允许传感器模块以取决于此值的速率捕获图像数据。此参数还可确保捕获操作在此时长过后超时。在此期间，摄像头处于忙碌状态，无法执行任何其他操作。

**注意**

为避免溢出，请将 `capture timeout` 输入设置为小于模块采样时间的值，该模块是您在确定 `capture trigger` 输入时选择的模块。

### 支持的开发板

此列表显示支持的开发板及对应的图像分辨率。

| Arduino 开发板 | 支持的分辨率 |
| --- | --- |
| Arduino Mega 2560a | `160x120`, `176x144`, `320x240` |
| Arduino Mega ADK | `160x120`, `176x144`, `320x240` |
| Arduino Due | `160x120`, `176x144`, `320x240` |
| Arduino MKR1000 | `160x120`, `176x144`, `320x240`, `352x288` |
| Arduino MKR WiFi1010 | `160x120`, `176x144`, `320x240`, `352x288` |
| Arduino MKR Zero | `160x120`, `176x144`, `320x240`, `352x288` |
| Arduino Nano 33 IoT | `160x120`, `176x144` |
| Arduino Nano 33 BLE SENSE | `160x120`, `176x144` |
| ESP32-DevKitV1 | `160x120`, `176x144`, `320x240`, `352x288`, `640x480`, `800x600` |
| ESP32-DevKitC | `160x120`, `176x144`, `320x240`, `352x288`, `640x480`, `800x600` |
| a Arduino Mega 2560 开发板仅在 Simulink 中执行 'Build, Deploy and Start' 时支持 `176x144` 和 `320x240` 分辨率，而在 'Monitor and Tune' 时不支持。 | |

## 所属库

Simulink Support Package for Arduino Hardware / Sensors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2023b 中引入**

## 描述

使用带有 OV2640 传感器的 ArduCam 2MP Mini Plus 摄像头模块捕获 JPEG 图像

OV2640 Camera Sensor 模块使用带有 OV2640 传感器的 ArduCam Mini 2MP Plus 摄像头模块捕获 JPEG 格式的图像。摄像头连接到 Arduino® 开发板。该模块是复合传感器模块，同时使用 SPI 和 I2C 模块。

有关支持 OV2640 Camera Sensor 模块的开发板列表，请参阅支持的开发板。

**注意**

无法向一个模型中添加多个 OV2640 Camera Sensor 模块。
