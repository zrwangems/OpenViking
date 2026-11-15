---
type: simulink-block
title: 'DC Motor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Actuators'
documentation_page: 'dcmotor'
documentation_source_path: 'beagleboneblue/ref/dcmotor.html'
language: zh-CN
chinese_source: worker-translation
---

# DC Motor

## 端口

### 输入

### **Port\_1** — 输入信号标量

模块接受范围从 –100 到 100 的归一化值。

符号决定旋转方向，幅值决定提供给电机的功率。

- `1` 到 `100`：正向旋转，功率从最小到最大。
- `–1` 到 `–100`：反向旋转，功率从最小到最大。
- `0`：不提供功率

对于超出 –100 到 100 范围的输入值，模块的效果与发送最大或最小输入值相同。

**数据类型：** `uint8` | `int8`

## 参数

### **Motor Index** — 硬件上的端口索引 `1`（默认） | `2` | `3` | `4`

选择直流电机所连接硬件上的直流电机端口索引。

### **Stop Action** — 电机的停止行为 `Brake`（默认） | `Free Spin`

使用此参数，将电机配置为在模块接收到 `0`（停止）输入时制动或自由旋转。

- `Brake`：选择此选项时，会对电机施加反电动势，导致电机立即停止。
- `Free Spin`：选择此选项时，电机自由旋转，就像与车轮断开连接一样。

## 所属库

Simulink Coder Support Package for BeagleBone Blue Hardware / Actuators

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2017b 中引入**

## 描述

设置直流电机的功率、方向和停止动作

DC Motor 模块控制连接到 BeagleBone® Blue 的直流电机的功率、旋转方向和停止动作。将此模块与 Encoder 模块配合使用，以测量电机的增量位置。

输入信号决定提供给电机的功率以及电机的旋转方向。模块参数对话框的 **Stop action** 参数中指定的停止动作决定电机的停止行为。

在没有硬件的仿真期间，此模块不执行任何操作。请参阅 Block Produces Zeros or Does Nothing in Simulation。
