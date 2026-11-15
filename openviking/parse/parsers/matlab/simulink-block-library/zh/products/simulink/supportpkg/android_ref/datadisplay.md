---
type: simulink-block
title: 'Data Display'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / User Interface'
documentation_page: 'datadisplay'
documentation_source_path: 'supportpkg/android_ref/datadisplay.html'
language: zh-CN
chinese_source: worker-translation
---

# Data Display

## 端口

### 输入

### **Port\_1** — 要显示的数值向量数据

该模块输入可变长度的一维向量数据，以在小组件的应用程序屏幕上显示。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

### **Format** — 数据格式值 `Float`（默认）| `Integer` | `Scientific` | `Octal` | `Hex`

选择要在应用程序屏幕上显示的数据值的格式。

**注意**

对于数据类型为 `single` 或 `double` 的输入信号，Data Display 模块无法以 `Octal` 和 `Hex` 格式显示。在这种情况下，**Format** 参数默认为 `Float`。

### **Precision** — 数据精度值 `6`（默认）| 非负标量

指定要为给定数据值显示的小数点后的位数。

#### 依赖项

- 要启用此参数，请将 **Format** 设置为
  `Float`。

## 所属库

Simulink Support Package for Android Devices / User Interface

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2016b 中引入**

## 描述

在设备屏幕上显示数值数据

使用 Data Display 模块在小组件的应用程序屏幕上显示数值数据。模块标签指定小组件标签。
