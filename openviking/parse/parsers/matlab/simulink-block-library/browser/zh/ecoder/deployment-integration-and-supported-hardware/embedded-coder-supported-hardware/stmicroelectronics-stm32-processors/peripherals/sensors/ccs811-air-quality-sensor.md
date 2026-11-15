---
type: simulink-block
title: 'CCS811 Air Quality Sensor'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Sensors'
documentation_page: 'ccs811airqualitysensor'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/ccs811airqualitysensor.html'
language: zh-CN
chinese_source: worker-translation
---

# CCS811 Air Quality Sensor

## 端口

### 输出

### **eCO2** — 等效 CO2 标量

**eCO2** 端口输出室内空气等效 CO2 的值，以百万分之一 (ppm) 为单位。

**数据类型：** `single` | `double`

### **eTVOC** — 总挥发性有机化合物浓度标量

**eTVOC** 端口输出室内空气的等效总挥发性有机化合物浓度，以十亿分之一 (ppb) 为单位。

**数据类型：** `single` | `double`

### **Status** — eCO2 和 eTVOC 读取值的状态 `0` | `1`

状态值 `0` 表示 eCO2 和 eTVOC 的读取数据是新数据，`1` 表示读取的数据不是新数据。

**数据类型：** `uint8`

## 参数

### **I2C 模块** — 用于 I2C 通信的特定模块 `I2C1`（默认）

指定板上用于 I2C 通信的模块。

### **I2C 地址** — 传感器的 I2C 地址 `0x5A`（默认） | `0x5B`

该模块从中读取值的 CCS811 传感器的 I2C 地址。

该模块从中读取值的 CCS811 传感器的 I2C 地址。CCS811 传感器可以有两个 I2C 地址，具体取决于传感器 ADDR 引脚上的逻辑电平。

| 引脚名称 | 引脚状态 | I2C 地址 |
| --- | --- | --- |
| ADDR | Low | 0x5A |
| High | 0x5B |

### **数据采集间隔 (s)** — 数据采集的间隔 `1`（默认） | `0.25` | `10` | `60`

选择传感器读取数据的数据采集间隔（以秒为单位）。例如，如果选择值 `1`，则传感器每 `1` 秒读取一次值。

### **指定环境条件** — 环境条件 `Mask dialog`（默认） | `External sensor`

选择该选项以指定传感器在读取数据时的环境输入源。

### **湿度 (%)** — CCS811 传感器的湿度输入 `50`（默认） | `positive integer`

提供给连接到 STM32 Processors 的 CCS811 传感器的湿度百分比。

#### 依赖关系

仅当为 **指定环境条件** 参数选择 `Mask dialog` 时，此参数才会显示。

### **温度 (oC)** — CCS811 传感器的温度输入 `25`（默认） | `positive integer`

提供给连接到 STM32 Processors 的 CCS811 传感器的温度（以 ℃ 为单位）。

#### 依赖关系

仅当为 **指定环境条件** 参数选择 `Mask dialog` 时，此参数才会显示。

### **启用数据就绪中断** — 数据就绪时启用中断 `off`（默认） | `on`

如果选择此选项，则当数据就绪时，传感器的 nINT 引脚上会生成中断，从而允许您触发其他子系统执行任何操作。

### **数据类型** — 输出数据的类型 `single`（默认） | `double`

选择输出的数据类型。

### **采样时间** — 读取数据的时间间隔 `-1`（默认） | 正整数

指定此模块从 CCS811 传感器读取数据的频率。将此参数设置为 -1 时，Simulink 将根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / Sensors / Environmental Sensors Simulink Support Package for Arduino Hardware / Sensors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

测量等效 CO2 (eCO2) 和等效总挥发性有机化合物浓度 (eTVOC)

CCS811 Air Quality Sensor 模块测量用于室内空气质量监测的等效 CO2 (eCO2) 和等效总挥发性有机化合物浓度 (eTVOC)。此模块还提供选项来提供温度和湿度数据以启用补偿（通过指定湿度与温度值，或将 CCS811 与外部传感器连接）。
