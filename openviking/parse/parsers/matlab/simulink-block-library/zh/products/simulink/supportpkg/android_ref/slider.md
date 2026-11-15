---
type: simulink-block
title: 'Slider'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / User Interface'
documentation_page: 'slider'
documentation_source_path: 'supportpkg/android_ref/slider.html'
language: zh-CN
chinese_source: worker-translation
---

# Slider

## 端口

### 输出

### **Port\_1** — Slider 值 数值标量

该模块输出与其位置对应的 Slider 值。

**数据类型：** `single`

## 参数

### **Minimum** — 滑块的最小值 `-5`（默认）| 数值标量

指定滑块控件可以输出的最小值。

### **Initial value** — 滑块的初始值 `0`（默认）| 数值标量

指定滑块控件可以输出的初始值。

### **Maximum** — 滑块的最大值 `5`（默认）| 数值标量

指定滑块控件可以输出的最大值。

### **Resolution** — 滑块的分辨率 `0.1`（默认）| 数值标量

指定滑块控件可以输出的最小离散变化。

### **Sample time** — 采样时间间隔 `0.1`（默认）| 非负标量

指定一个离散时间间隔（以 seconds 为单位），模块按此间隔读取滑块位置并输出数据。

**注意**

**Sample time** 的较小值要求处理器在更短时间内完成相同数量的指令，这可能导致任务超限。

## 所属库

Simulink Support Package for Android Devices / User Interface

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2015a 中引入**

## 描述

显示滑块控件

使用 Slider 模块在设备屏幕上显示滑块控件。

Slider 模块输出单精度值。输出值取决于滑块在滑动条长度方向上的位置。当您将滑块滑到左侧位置时，模块输出 **Minimum** 参数的值。当您将滑块滑到最右侧位置时，模块输出 **Maximum** 参数的值。

**注意**

在未连接硬件的情况下进行仿真时，此模块输出初始状态。
