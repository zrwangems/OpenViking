---
type: simulink-block
title: 'Barometer'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Sensors'
documentation_page: 'barometer'
documentation_source_path: 'beagleboneblue/ref/barometer.html'
language: zh-CN
chinese_source: worker-translation
---

# Barometer

## 端口

### 输出

### **Pressure** — 气压计周围的气压向量

**Pressure** 端口输出硬件上 BMP280 气压计周围的气压。气压以 1-by-1 数组形式输出，单位为 pascal。

**数据类型：** `double`

## 参数

### **采样时间** — 从气压计读取值的时间间隔 `0.1` (默认) | `-1` | 非负实数值

指定模块从气压计读取值的频率，以 seconds 为单位。
将此参数指定为 `-1` 时，Simulink® 会根据模型中模块的上下文确定该模块的最佳采样时间。

### 传感器设置

### **过采样率** — 对值进行采样的速率 `8` (默认) | `1` | `2` | `4` | `16`

选择气压计对气压值进行采样的速率，以 Hertz 为单位。

### **IIR 滤波器系数** — IIR 滤波器的系数 `4` (默认) | `Off` | `2` | `8` | `16`

选择无限脉冲响应 (IIR) 滤波器的系数，以降低采样值中与噪声相关的误差。

## 所属库

Simulink Coder Support Package for BeagleBone Blue Hardware / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

测量 BMP280 传感器周围的气压

Barometer 模块测量 BeagleBone® Blue 硬件上 BMP280 气压计周围的气压，单位为 pascal。该模块以 `double` 数据类型的 1-by-1 数组输出压力。

如果在未连接硬件的情况下仿真包含 Barometer 模块的模型，则该模块输出零。有关详细信息，请参阅模块在仿真中产生零或不执行任何操作。
