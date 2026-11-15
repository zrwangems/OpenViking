---
type: simulink-block
title: 'Button'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / User Interface'
documentation_page: 'button'
documentation_source_path: 'supportpkg/android_ref/button.html'
language: zh-CN
chinese_source: worker-translation
---

# Button

## 端口

### 输出

### **Port\_1** — 按钮状态输出 Boolean 标量

该模块输出按钮状态，以 Boolean 标量形式返回。如果按钮状态为 `Pressed`，该模块输出 `1`。
如果按钮状态为 `Not Pressed`，该模块输出 `0`。

**数据类型：** `Boolean`

## 参数

### **按钮状态** — 按钮的初始状态 `Not pressed`（默认）| `Pressed`

选择 Android 应用启动时按钮的初始状态。

### **采样时间** — 采样时间间隔 `0.1`（默认）| 非负标量

指定一个离散时间间隔（以 seconds 为单位），该模块按此间隔读取按钮状态并输出数据。

**注意**

较小的**采样时间**值要求处理器在更短时间内完成相同数量的指令，这可能导致任务超限。

## 所属库

Simulink Support Package for Android Devices / User Interface

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2015a 中引入**

## 描述

在设备屏幕上显示按钮小组件

Button 模块在 Android® 应用中显示一个按钮小组件。该按钮有两种状态：*pressed* 和
*not-pressed*。点按该按钮会切换按钮的状态。**按钮状态**参数决定 Android 应用启动时的按钮状态。

**注意**

在未连接硬件的仿真期间，此模块不执行任何操作。有关详细信息，请参阅 Block Produces Zeros or Does Nothing in Simulation。
