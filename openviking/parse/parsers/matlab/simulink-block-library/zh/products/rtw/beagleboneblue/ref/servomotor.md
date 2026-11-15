---
type: simulink-block
title: 'Servo Motor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Actuators'
documentation_page: 'servomotor'
documentation_source_path: 'beagleboneblue/ref/servomotor.html'
language: zh-CN
chinese_source: worker-translation
---

# Servo Motor

## 端口

### 输入

### **Port\_1** — 用于设置伺服电机轴位置的输入信号，标量

输入范围介于 `0` 和 `180` 之间。对于 `0` 输入，轴位于 0 degrees；而对于 `180` 输入，轴位于 180 degrees。超出范围的值（例如 `-5` 或 `200`）输入到模块时，其效果与发送最小或最大输入值相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## 参数

### **电机通道** — 选择伺服电机的电机通道 1（默认） | `1` 到 `10`

选择 BeagleBone Blue 硬件上连接到伺服电机的电机通道或引脚。

要打开引脚映射，请点击 **查看引脚映射** 按钮。

为模型中的多个 Servo Motor 模块分配唯一的通道编号。

## 所属库

Simulink Coder Support Package for BeagleBone Blue Hardware / Actuators

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2018b 中引入**

## 描述

设置伺服电机的轴位置

Servo Motor 模块表示连接到 BeagleBone® Blue 硬件上指定电机通道的伺服电机。将伺服电机的轴位置设置为 `0` 到 `180` degrees。
