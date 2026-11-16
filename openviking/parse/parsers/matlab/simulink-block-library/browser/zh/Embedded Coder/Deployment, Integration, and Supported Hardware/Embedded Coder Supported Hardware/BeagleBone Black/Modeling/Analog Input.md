---
type: simulink-block
title: 'Analog Input'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / BeagleBone Black / Modeling'
documentation_page: 'analoginput'
documentation_source_path: 'beaglebone/ref/analoginput.html'
language: zh-CN
chinese_source: worker-translation
---

# Analog Input

## 端口

### 输出

### **Port\_1** — 模拟输入引脚的电压 scalar

该模块输出模拟引脚相对于 BeagleBone 硬件上模拟输入参考电压的电压电平。该模块输出介于 0 (GND\_ADC) 和 1.8 (VDD\_ADC) 之间的电压值。输出的单位是 volts。

**数据类型：** `double`

## 参数

### **Pin** — 模拟输入引脚编号 `P9_39`（默认）| `P9_40` | `P9_37` | `P9_38` | `P9_33` | `P9_36` | `P9_35`

指定 BeagleBone 板的模拟输入引脚编号。要打开 BeagleBone 引脚映射表，请点击 **View pin map**。

### **Sample time** — 模块读取输入引脚值的时间间隔 `0.1`（默认）| scalar

指定该模块多久测量一次模拟输入引脚的电压，单位为 seconds。
输入一个大于零的值。当您将此参数指定为 `–1` 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。较小的值要求处理器在更短的时间内完成相同数量的指令，这可能导致任务超限。

## 所属库

Embedded Coder Support Package for BeagleBone Black Hardware

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2014b 中引入**

## 描述

测量模拟输入引脚的电压

使用 Analog Input 模块测量 BeagleBone® 板的模拟输入引脚的电压。
