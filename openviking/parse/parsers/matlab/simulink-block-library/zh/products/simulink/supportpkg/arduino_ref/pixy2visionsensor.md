---
type: simulink-block
title: 'Pixy2 Vision Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Sensors / Vision Sensors'
documentation_page: 'pixy2visionsensor'
documentation_source_path: 'supportpkg/arduino_ref/pixy2visionsensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Pixy2 Vision Sensor

## 端口

### 输出

### **X** — 检测到的对象像素中心的 *x* 位置 | 标量

基于视场，由 Pixy2 视觉传感器检测到的最显著对象（色块）中心的 *x* 位置。

#### 依赖项

- 要启用此端口，请将 **Tracking mode** 参数设置为 `Color Signature`、`Color Code Signature` 或 `Color and Color Code Signature (Mixed)`。

**数据类型：** `uint16`

### **Y** — 检测到的对象像素中心的 *y* 位置 | 标量

基于视场，由 Pixy2 视觉传感器检测到的最显著对象（色块）中心的 *y* 位置。

#### 依赖项

- 要启用此端口，请将 **Tracking mode** 参数设置为 `Color Signature`、`Color Code Signature` 或 `Color and Color Code Signature (Mixed)`。

**数据类型：** `uint16`

### **Width** — 检测到的对象像素的宽度 | 标量

基于视场，由 Pixy2 视觉传感器检测到的最显著对象（色块）的宽度。

#### 依赖项

- 要启用此端口，请将 **Tracking mode** 参数设置为 `Color Signature`、`Color Code Signature` 或 `Color and Color Code Signature (Mixed)`。

**数据类型：** `uint16`

### **Height** — 检测到的对象像素的高度 | 标量

基于视场，由 Pixy2 视觉传感器检测到的最显著对象（色块）的高度。

#### 依赖项

- 要启用此端口，请将 **Tracking mode** 参数设置为 `Color Signature`、`Color Code Signature` 或 `Color and Color Code Signature (Mixed)`。

**数据类型：** `uint16`

### **Object Count** — 检测到的对象数，范围 [1, 255] 内的正整数

基于视场，由 Pixy2 视觉传感器检测到的对象（色块）数。

#### 依赖项

- 要启用此端口，请将 **Tracking mode** 参数设置为 `Color Signature`、`Color Code Signature` 或 `Color and Color Code Signature (Mixed)`。

**数据类型：** `uint8`

### **Signature** — 检测到的对象的颜色或颜色代码签名，范围 [1, 7] 内的正整数

基于视场，由 Pixy2 视觉传感器检测到的颜色或颜色代码对象（色块）的签名。

#### 依赖项

- 要启用此端口，请将 **Tracking mode** 参数设置为 `Color Code Signature` 或 `Color and Color Code Signature (Mixed)`。

**数据类型：** `uint16`

### **Angle** — 检测到的对象的角度，范围 [-180, +180] 内的整数

基于视场，由 Pixy2 视觉传感器检测到的对象（色块）的颜色或颜色代码签名的角度。

#### 依赖项

- 要启用此端口，请将 **Tracking mode** 参数设置为 `Color and Color Code Signature (Mixed)`。

**数据类型：** `int16`

### **X0** — 检测到的线像素的 *x* 坐标起点 | 标量

基于视场，由 Pixy2 视觉传感器检测到的最显著线的 *x* 坐标起点。

#### 依赖项

- 要启用此端口，请将 **Tracking mode** 参数设置为 `Line`。

**数据类型：** `uint16`

### **Y0** — 检测到的线像素的 *y* 坐标起点 | 标量

基于视场，由 Pixy2 视觉传感器检测到的最显著线的 *y* 坐标起点。

#### 依赖项

- 要启用此端口，请将 **Tracking mode** 参数设置为 `Line`。

**数据类型：** `uint16`

### **X1** — 检测到的线像素的 *x* 坐标终点 | 标量

基于视场，由 Pixy2 视觉传感器检测到的最显著线的 *x* 坐标终点。

#### 依赖项

- 要启用此端口，请将 **Tracking mode** 参数设置为 `Line`。

**数据类型：** `uint16`

### **Y1** — 检测到的线像素的 *y* 坐标终点 | 标量

基于视场，由 Pixy2 视觉传感器检测到的最显著线的 *y* 坐标终点。

#### 依赖项

- 要启用此端口，请将 **Tracking mode** 参数设置为 `Line`。

**数据类型：** `uint16`

### **IntFlag** — 相交线的存在情况 `1` (true) 或 `0` (false)

Pixy2 视觉传感器的视场中是否存在相交线。`1` 表示存在相交线。

#### 依赖项

- 要启用此端口，请将 **Tracking mode** 参数设置为 `Line`。

**数据类型：** `uint8`

## 参数

### **Interface** — 接口类型 `I2C`（默认）| `SPI with CS` | `Serial`

选择 Arduino 板上的接口类型，以建立与 Pixy2 视觉传感器的连接。

### **I2C module** — I2C 通信模块 `0`（默认）| 标量

指定 Arduino 硬件上用于与传感器外设通信的 I2C 模块。有关 Arduino 引脚映射以及硬件板支持的模块的详细信息，请参阅 Arduino 定时器无关模块的引脚映射。

#### 依赖项

要启用此参数，请将 **Interface** 设置为 `I2C`。

### **Pixy2 I2C address** — Arduino 板的 I2C 地址 `0x54`（默认）| 范围 [`0` 到 `127`] 内的地址

要使用 I2C 通信协议将 Pixy2 视觉传感器连接到 Arduino 板，请输入 Arduino 板的 I2C 地址。

#### 依赖项

要启用此参数，请将 **Interface** 设置为 `I2C`。

### **SPI module** — SPI 通信模块 `0`（默认）| 标量

指定 Arduino 硬件上用于与 SPI 外设通信的 SPI 模块。有关 Arduino 引脚映射以及硬件板支持的模块的详细信息，请参阅 Arduino 定时器无关模块的引脚映射。

#### 依赖项

要启用此参数，请将 **Interface** 设置为 `SPI with CS`。

### **Chip select pin** — Arduino 板的片选引脚 `4`（默认）| 目标硬件引脚

要使用 SPI 通信协议将 Pixy2 视觉传感器连接到 Arduino 板，请输入 Arduino 板的片选引脚。有关 Arduino 板片选引脚的详细信息，请参阅 Arduino 定时器无关模块的引脚映射。

#### 依赖项

- 要启用此参数，请将 **Interface** 设置为 `SPI with CS`。

### **Serial** — Arduino 板的串行端口号 `0`（默认）| 目标硬件端口

要使用串行通信将 Pixy2 视觉传感器连接到 Arduino 板，请输入 Arduino 板的串行端口号。有关 Arduino 板串行端口号的详细信息，请参阅 Arduino 定时器无关模块的引脚映射。

#### 依赖项

- 要启用此参数，请将 **Interface** 设置为 `Serial`。

### **Tracking mode** — 选择跟踪模式 `Color Signature`（默认）| `Color Code Signature` | `Color and Color Code Signature (Mixed)` | `Line`

选择跟踪模式，以检测与 PixyMon 实用工具中配置的颜色签名或颜色代码签名匹配的对象。对于 `Color Signature`、`Color Code Signature` 和 `Color and Color Code Signature (Mixed)` 跟踪模式，检测到的对象的 *xy* 坐标、宽度和高度保持不变。

### **Color signature** — 要跟踪的对象的颜色签名 `1`（默认）| 范围 [1, 7] 内的正整数 | `ALL`

选择要在 PixyMon 实用工具中配置的待跟踪对象的颜色签名。选择 `ALL` 可跟踪所有已配置的颜色签名。

### **Sample time** — 时间采样间隔 `0.1`（默认）| 范围 [0.001, 1] 内的正标量

输入模块从 Pixy2 视觉传感器读取值的时间间隔。

## 所属库

Simulink Support Package for Arduino Hardware / Sensors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2023a 中引入**

## 描述

表示已连接的 CMUcam5 Pixy2 视觉传感器并跟踪对象（色块）

使用 Pixy2 Vision Sensor 模块读取与 Arduino® 板连接的 Pixy2 视觉传感器检测到的对象（色块）的坐标。您可以使用 SPI、I2C 或串行通信协议将 Pixy2 视觉传感器连接到 Arduino 板。

### 功能模式

Pixy2 Vision Sensor 模块有四种功能模式：

- Color Signature：检测与 PixyMon 实用工具中配置的颜色签名匹配的对象。
- Color Code Signature：检测与 PixyMon 实用工具中配置的颜色代码签名匹配的对象。
- Color and Color Code Signature (Mixed)：检测与 PixyMon 实用工具中配置的颜色和颜色代码签名匹配的对象。
- Line：检测并跟踪线。

### 启动 PixyMon

如果您已安装 Arduino 硬件的支持包，并按照“安装 Arduino 硬件支持”中所述完成了额外的硬件设置，则 PixyMon 实用工具将自动启动。
