---
type: simulink-block
title: 'CCS811 Air Quality Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Sensors / Environmental Sensors'
documentation_page: 'ccs811airqualitysensor'
documentation_source_path: 'supportpkg/raspberrypi_ref/ccs811airqualitysensor.html'
language: zh-CN
chinese_source: worker-translation
---

# CCS811 Air Quality Sensor

## 端口

### 输出

### **eCO2** — 等效 CO2 标量

**eCO2** 端口输出室内空气等效 CO2 的值，单位为百万分率 (ppm)。

**数据类型：** `single` | `double`

### **eTVOC** — 总挥发性有机化合物浓度标量

**eTVOC** 端口输出室内空气的等效总挥发性有机化合物浓度，单位为十亿分率 (ppb)。

**数据类型：** `single` | `double`

### **Status** — 为 eCO2 和 eTVOC 读取的值的状态 `0` | `1`

值 `0` 的状态表示 eCO2 和 eTVOC 读取的数据是新数据，`1` 表示读取的数据不是新数据。

**数据类型：** `uint8`

## 参数

### **I2C 模块** — 用于 I2C 通信的特定模块 `1` (默认)

指定板上用于 I2C 通信的模块。

### **I2C 地址** — 传感器的 I2C 地址 `0x5A` (默认) | `0x5B`

CCS811 传感器的 I2C 地址，模块从中读取值。

CCS811 传感器的 I2C 地址，模块从中读取值。CCS811 传感器可以有两个 I2C 地址，具体取决于传感器引脚 ADDR 上的逻辑电平。

| 引脚名称 | 引脚状态 | I2C 地址 |
| --- | --- | --- |
| ADDR | Low | 0x5A |
| High | 0x5B |

### **数据采集间隔 (s)** — 数据采集的间隔 `1` (默认) | `0.25` | `10` | `60`

选择传感器读取数据的数据采集间隔（以秒为单位）。例如，如果选择值 `1`，则传感器每 `1` 秒读取一次值。

### **指定环境条件** — 环境条件 `Mask dialog` (默认) | `External sensor`

选择该选项以指定传感器在读取数据时环境输入的来源。

### **湿度 (%)** — 到 CCS811 传感器的湿度输入 `50` (默认) | `positive integer`

以百分比表示的湿度，作为连接到 Raspberry Pi® 板的 CCS811 传感器的输入提供。

#### 依赖关系

仅当为 **指定环境条件** 参数选择 `Mask dialog` 时，此参数才会出现。

### **温度 (oC)** — 到 CCS811 传感器的温度输入 `25` (默认) | `positive integer`

温度（以 ℃ 为单位），作为连接到 Raspberry Pi 板的 CCS811 传感器的输入提供。

#### 依赖关系

仅当为 **指定环境条件** 参数选择 `Mask dialog` 时，此参数才会出现。

### **启用数据就绪中断** — 数据就绪时启用中断 `off` (默认) | `on`

如果选择此选项，则数据就绪时会在传感器的引脚 nINT 上生成中断，从而允许您触发其他子系统执行任何操作。

### **数据类型** — 输出数据的类型 `single` (默认) | `double`

选择输出的数据类型。

### **采样时间** — 读取数据的时间间隔 `-1` (默认) | 正整数

指定此模块从 CCS811 传感器读取数据的频率。当将此参数设置为 -1 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Simulink Support Package for Arduino Hardware / Sensors Simulink Support Package for Raspberry Pi Hardware / Sensors / Environmental Sensors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2022b 中引入**

## 描述

测量等效 CO2 (eCO2) 和等效总挥发性有机化合物浓度 (eTVOC)

CCS811 Air Quality Sensor 模块测量用于室内空气质量监测的等效 CO2 (eCO2) 和等效总挥发性有机化合物浓度 (eTVOC)。该模块还提供用于提供温度和湿度数据的选项，以启用补偿（通过指定湿度值和温度值，或将 CCS811 与外部传感器连接）。
