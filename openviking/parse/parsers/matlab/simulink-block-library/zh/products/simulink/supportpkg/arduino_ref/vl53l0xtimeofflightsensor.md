---
type: simulink-block
title: 'VL53L0X Time of Flight Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Sensors / Motor and Vehicle Sensors'
documentation_page: 'vl53l0xtimeofflightsensor'
documentation_source_path: 'supportpkg/arduino_ref/vl53l0xtimeofflightsensor.html'
language: zh-CN
chinese_source: official
---

# VL53L0X Time of Flight Sensor

## 端口

### 输出

### **Distance** — 对象距离 向量

**距离**端口以毫米为单位输出目标对象距离

**数据类型:** `uint16`

## 参数

### **I2C module** — I2C 通信模块 `0` (默认) | 标量

指定 Arduino® 硬件上的 I2C 模块以便与传感器外设进行通信。有关硬件板支持的 Arduino 引脚映射和模块的详细信息，请参阅Pin Mapping for Arduino Timer-Independent Blocks。

### **I2C address** — 传感器的 I2C 地址 `0x29` (默认)

VL53L0X 传感器的 I2C 地址，模块从该地址读取值。您可以配置此值。I2C 地址的范围是从 `0x08` 到 `0x77`。

### **Ranging Mode** — VL53L0X 传感器的测距模式 `Default` (默认) | `High accuracy` | `Long range` | `High speed`

选择测距模式以测量到目标对象的距离。下表显示四种可用的测距模式。

| 测距模式 | 时间预算 | 典型最大范围 | 典型应用 |
| --- | --- | --- | --- |
| 默认值 | 30 毫秒 | 1.2 米 | 标准 |
| 高准确度 | 200 毫秒 | 2 米 | 精确测量 |
| 远程 | 33 毫秒 | 1.2 米 | 黑暗条件下的远程测距 |
| 高速 | 20 毫秒 | 1.2 米 | 准确性不重要的高速测距 |

时间预算是传感器执行一次距离测量所花费的时间。

### **采样时间** — 读取数据的时间间隔 `-1` (默认) | 正整数

指定此模块从 VL53L0X 传感器读取数据的频率。当您将此参数设置为 `-1` 时，Simulink 会根据模型中的模块上下文确定模块的最佳采样时间。

## 所属库

Simulink Support Package for Arduino Hardware / Sensors Simulink Support Package for Raspberry Pi Hardware / Sensors

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2022a 中推出**

## 描述

测量到目标对象的距离

VL53L0X Time of Flight Sensor 模块测量完整视野中到目标对象的距离（FOV = 25 度）。此模块还提供选项以便根据您的需求选择四种测距模式之一。

**注意**

VL53L0X 传感器需要 XSHUT 连接。将 XSHUT 引脚连接到 vcc。

**注意**

如果 VL53L0X 传感器连接到内存较低的板（例如 Arduino Uno），则不支持使用监控和调节动作（外部模式）来调节 Simulink 模型的参数值。
