---
type: simulink-block
title: 'CCS811 Air Quality Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Sensors / Environmental Sensors'
documentation_page: 'ccs811airqualitysensor'
documentation_source_path: 'supportpkg/arduino_ref/ccs811airqualitysensor.html'
language: zh-CN
chinese_source: worker-translation
---

# CCS811 Air Quality Sensor

## 端口

### 输出

### **eCO2** — 等效 CO2 标量

**eCO2** 端口输出室内空气的等效 CO2 值，单位为百万分率 (ppm)。

**数据类型：** `single` | `double`

### **eTVOC** — 总挥发性有机化合物浓度标量

**eTVOC** 端口输出室内空气的等效总挥发性有机化合物浓度，单位为十亿分率 (ppb)。

**数据类型：** `single` | `double`

### **Status** — 为 eCO2 和 eTVOC 读取的值的状态 `0` | `1`

值的状态：`0` 表示读取的 eCO2 和 eTVOC 数据是新数据，`1` 表示读取的数据不是新数据。

**数据类型：** `uint8`

## 参数

### **I2C 模块** — I2C 通信模块 `0`（默认）| 标量

指定 Arduino® 硬件上用于与传感器外设通信的 I2C 模块。有关 Arduino 引脚映射以及硬件板支持的模块的详细信息，请参阅 Pin Mapping for Arduino Timer-Independent Blocks。

### **I2C 地址** — 传感器的 I2C 地址 `0x5A`（默认）| `0x5B`

CCS811 传感器的 I2C 地址，模块从该地址读取值。

CCS811 传感器的 I2C 地址，模块从该地址读取值。根据传感器 ADDR 引脚上的逻辑电平，CCS811 传感器可以有两个 I2C 地址。

| 引脚名称 | 引脚状态 | I2C 地址 |
| --- | --- | --- |
| ADDR | Low | 0x5A |
| High | 0x5B |

### **数据采集间隔 (s)** — 数据采集间隔 `1`（默认）| `0.25` | `10` | `60`

选择传感器读取数据的数据采集间隔，以秒为单位。例如，如果选择值 `1`，则传感器每 `1` 秒读取一次值。

### **指定环境条件** — 环境条件 `Mask dialog`（默认）| `External sensor`

选择该选项以指定传感器在读取数据时环境输入的来源。

### **湿度 (%)** — 输入到 CCS811 传感器的湿度 `50`（默认）| `positive integer`

提供给连接到 Arduino 硬件的 CCS811 传感器的湿度百分比。

#### 依赖关系

仅当为 **指定环境条件** 参数选择 `Mask dialog` 时，此参数才会出现。

### **温度 (oC)** — 输入到 CCS811 传感器的温度 `25`（默认）| `positive integer`

提供给连接到 Arduino 硬件的 CCS811 传感器的温度（以 ℃ 为单位）。

#### 依赖关系

仅当为 **指定环境条件** 参数选择 `Mask dialog` 时，此参数才会出现。

### **启用数据就绪中断** — 数据就绪时启用中断 `off`（默认）| `on`

如果选择此选项，当数据就绪时，传感器的 nINT 引脚会生成中断，使您能够触发其他子系统执行任何操作。

### **数据类型** — 输出数据的类型 `double`（默认）| `single`

选择输出的数据类型。

### **采样时间** — 读取数据的时间间隔 `-1`（默认）| 正整数

指定此模块从 CCS811 传感器读取数据的频率。将此参数设置为 -1 时，Simulink 会根据模型中的模块上下文确定模块的最佳采样时间。

## 所属库

Simulink Support Package for Arduino Hardware / Sensors Simulink Support Package for Raspberry Pi Hardware / Sensors / Environmental Sensors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2022a 中引入**

## 描述

测量等效 CO 2 (eCO 2 ) 和等效总挥发性有机化合物浓度 (eTVOC)

CCS811 Air Quality Sensor 模块测量等效 CO2 (eCO2) 和等效总挥发性有机化合物浓度 (eTVOC)，用于室内空气质量监测。此模块还提供用于提供温度和湿度数据的选项，以实现补偿（可以通过指定湿度和温度值，或将 CCS811 与外部传感器连接）。
