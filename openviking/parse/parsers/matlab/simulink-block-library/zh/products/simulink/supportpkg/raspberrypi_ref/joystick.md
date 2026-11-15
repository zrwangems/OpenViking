---
type: simulink-block
title: 'Joystick'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Sense HAT'
documentation_page: 'joystick'
documentation_source_path: 'supportpkg/raspberrypi_ref/joystick.html'
language: zh-CN
chinese_source: worker-translation
---

# Joystick

## 端口

### 输出

### **Port\_1** — 用于返回 Joystick 按钮标量值的输出端口

这是输出端口，返回在 Joystick 上按下的按钮的值。

**数据类型：** `uint8`

## 参数

### **View Position information** — 查看 Joystick 按钮位置的位置

单击此按钮可了解所按下按钮的位置。
图片显示了 Joystick 按钮的位置以及 SenseHAT 板上其他传感器的位置。

### **Sample time** — 从压力传感器读取数据的频率 0.1（默认） | 标量

指定此模块从压力传感器读取数据的频率。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Sense HAT

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2017a 中引入**

## 描述

读取五位置 Joystick 的状态

读取五位置 Joystick 的状态。该模块根据按下的 Joystick 按钮输出 0-5 之间的值。显示了 Joystick 按钮位置。

与模块输出的五个值对应的 Joystick 位置如下：

0- 当您未按下按钮时

1- 当您按下中间按钮时

2- 当您按下左侧按钮时

3- 当您按下顶部按钮时

4- 当您按下右侧按钮时

5- 当您按下底部按钮时。
