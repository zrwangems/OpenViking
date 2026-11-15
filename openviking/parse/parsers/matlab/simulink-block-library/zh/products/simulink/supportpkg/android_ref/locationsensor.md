---
type: simulink-block
title: 'Location Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Sensors'
documentation_page: 'locationsensor'
documentation_source_path: 'supportpkg/android_ref/locationsensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Location Sensor

## 端口

### 输出

### **Lat** — 设备的纬度数据标量

该模块输出设备的纬度数据。

**数据类型：** `double`

### **Lon** — 设备的经度数据标量

该模块输出设备的经度数据。

**数据类型：** `double`

### **Alt** — 设备的海拔数据标量

该模块输出设备的海拔数据。

**数据类型：** `double`

## 参数

### **Sample time** — 采样时间间隔 `0.1`（默认） | 非负标量

指定一个离散时间间隔（以 seconds 为单位），模块按此间隔读取设备的 GPS 传感器并输出数据。

**注意**

较小的 **Sample time** 值要求处理器在更短时间内完成相同数量的指令，这可能导致任务超限。

## 所属库

Simulink Support Package for Android Devices / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014a 中引入**

## 描述

测量全球定位系统数据

使用 Location Sensor 模块读取设备的 GPS 数据并输出其纬度、经度和海拔。

GPS 测量值参考 World Geodetic System (WGS84) 的最新修订版。GPS 传感器精度通常以 meters 为单位。将纬度和经度从 decimal degrees 转换为 meters 时，decimal degree 值仅视为精确到 6 位小数。例如，在赤道，0.000001 degrees 约等于 11.1 centimeters。

**注意**

GPS 必须在设备上启用。如果出现以下任一条件，此模块输出零。

- GPS 在设备上已禁用。
- 设备不包含 GPS 传感器。
- 在没有设备的情况下仿真

有关详细信息，请参阅 Block Produces Zeros or Does Nothing in Simulation。
