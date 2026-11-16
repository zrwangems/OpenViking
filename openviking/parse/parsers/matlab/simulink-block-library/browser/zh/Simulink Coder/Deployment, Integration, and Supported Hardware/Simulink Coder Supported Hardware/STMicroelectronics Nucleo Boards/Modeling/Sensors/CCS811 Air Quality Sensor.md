---
type: simulink-block
title: 'CCS811 Air Quality Sensor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / Sensors'
documentation_page: 'ccs811airqualitysensor'
documentation_source_path: 'nucleo/ref/ccs811airqualitysensor.html'
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

### **Status** — eCO2 和 eTVOC 读取值的状态 `0` | `1`

值状态 `0` 表示 eCO2 和 eTVOC 的读取数据为新数据，`1` 表示读取数据不是新数据。

**数据类型：** `uint8`

## 参数

### **I2C address** — 传感器的 I2C 地址 `0x5A`（默认） | `0x5B`

模块从中读取值的 CCS811 传感器的 I2C 地址。

模块从中读取值的 CCS811 传感器的 I2C 地址。CCS811 传感器根据传感器 ADDR 引脚上的逻辑电平可具有两个 I2C 地址。

| 引脚名称 | 引脚状态 | I2C 地址 |
| --- | --- | --- |
| ADDR | Low | 0x5A |
| High | 0x5B |

### **Data acquisition interval (s)** — 数据采集间隔 `1`（默认） | `0.25` | `10` | `60`

选择传感器读取数据的数据采集间隔（以秒为单位）。例如，如果选择值 `1`，则传感器每 `1` 秒读取一次值。

### **Specify environmental conditions** — 环境条件 `Mask dialog`（默认） | `External sensor`

选择该选项以指定传感器在读取数据时环境输入的来源。

### **Humidity (%)** — CCS811 传感器的湿度输入 `50`（默认） | `positive integer`

提供给连接到 Arduino® 硬件的 CCS811 传感器的湿度百分比。

#### 依赖关系

仅当为 **Specify environmental conditions** 参数选择 `Mask dialog` 时，此参数才会出现。

### **Temperature (oC)** — CCS811 传感器的温度输入 `25`（默认） | `positive integer`

提供给连接到 Arduino 硬件的 CCS811 传感器的温度（以 ℃ 为单位）。

#### 依赖关系

仅当为 **Specify environmental conditions** 参数选择 `Mask dialog` 时，此参数才会出现。

### **Enable data ready interrupt** — 数据就绪时启用中断 `off`（默认） | `on`

如果选择此选项，则当数据就绪时，会在传感器的 nINT 引脚上生成中断，从而允许您触发其他子系统执行任何操作。

### **Data type** — 输出数据的类型 `double`（默认） | `single`

选择输出的数据类型。

### **Sample time** — 读取数据的时间间隔 `-1`（默认） | positive integer

指定此模块从 CCS811 传感器读取数据的频率。将此参数设置为 -1 时，Simulink 会根据模型中的模块上下文确定模块的最佳采样时间。

## 所属库

Simulink Coder Support Package for STMicroelectronics Nucleo Boards/ Sensors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2023b 中引入**

## 描述

测量等效 CO 2 (eCO 2 ) 和等效总挥发性有机化合物浓度 (eTVOC)

CCS811 Air Quality Sensor 模块测量用于室内空气质量监测的等效 CO2 (eCO2) 和等效总挥发性有机化合物浓度 (eTVOC)。此模块还提供输入温度与湿度数据以启用补偿的选项（可通过指定湿度和温度值，或通过将 CCS811 与外部传感器连接）。
