---
type: simulink-block
title: 'Analog Input'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / System Peripherals'
documentation_page: 'analoginputcommon'
documentation_source_path: 'supportpkg/arduino_ref/analoginputcommon.html'
language: zh-CN
chinese_source: worker-translation
---

# Analog Input

## 端口

### 输出

### **Pin 1 value** — 模拟输入引脚的电压标量

该模块输出 Arduino 板模拟输入引脚上接收到的数字化转换后的电压值。

**数据类型：** `double`

## 参数

### **引脚编号** — ADC 引脚编号 `4`（默认）| Arduino 板引脚编号

指定 Arduino 板模拟输入引脚编号。要打开 Arduino 引脚映射表，请点击 **查看引脚映射**。要了解如何为该模块分配引脚，请参阅 Arduino Timer-Independent Blocks 的引脚映射。

### **采样时间** — 模块读取输入引脚值的时间间隔 `–1`（默认）| 标量

指定模块测量模拟输入引脚电压的时间间隔，以秒为单位。输入一个大于零的值。当将此参数指定为 `–1` 时，Simulink® 会根据模型中的模块上下文为该模块确定最佳采样时间。

## 所属库

Simulink Support Package for Arduino Hardware / Common

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014a 中引入**

## 描述

测量模拟输入引脚的电压

使用 Analog Input 模块测量 Arduino® 硬件上相对于模拟输入参考电压的模拟引脚电压。该模块将测量结果输出为范围在 `0` 到 `1023` 之间的值。

- 如果测得的电压等于接地电压，则模块输出为 `0`。
- 如果测得的电压等于模拟参考电压，则模块输出为 `1023`。

大多数 Arduino 板的模拟输入参考电压默认值为 5 V。要更改模型配置参数中的 **模拟输入参考电压** 参数，请导航到 **硬件实现** > **目标硬件资源** > **模拟输入通道属性**。

Arduino Due、Nano 33 IoT、MKR 板和 Nano 33 BLE Sense 板的模拟输入参考电压为 3.3 V。您无法更改此值。

**警告**

可施加到模拟输入引脚的电压范围取决于模拟输入参考电压。有关详细信息，请阅读 Arduino 硬件的文档。
