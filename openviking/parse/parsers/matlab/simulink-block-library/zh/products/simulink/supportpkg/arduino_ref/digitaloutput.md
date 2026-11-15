---
type: simulink-block
title: 'Digital Output'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / System Peripherals'
documentation_page: 'digitaloutput'
documentation_source_path: 'supportpkg/arduino_ref/digitaloutput.html'
language: zh-CN
chinese_source: worker-translation
---

# Digital Output

## 端口

### 输入

### **Port\_1** — Arduino 数字输出引脚上的输入信号电压，标量

模块将此值设置到 **Pin number** 参数中指定的数字输出引脚。

- 向模块发送 `1`，以将数字引脚的逻辑值设置为 HIGH，即 5 V 或 3.3 V，具体取决于板电压。
- 向模块发送 `0`，以将数字引脚的逻辑值设置为 LOW，即 0 V。

**数据类型：** `double`

## 参数

### **Pin number** — Arduino 引脚编号 `9`（默认）| Arduino 板引脚编号

输入 Arduino 板的数字输出引脚编号。要打开 Arduino 引脚映射表，请点击 **查看引脚映射**。有关如何为 Digital Output 模块分配引脚的详细信息，请参阅 Arduino 定时器无关模块的引脚映射。

## 所属库

Simulink Support Package for Arduino Hardware / Common

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2012a 中引入**

## 描述

设置 Arduino 上数字输出引脚的逻辑状态

使用 Digital Output 模块设置 Arduino® 板上指定数字引脚的逻辑状态，该引脚在 **Pin number** 参数中指定。

在外部模式仿真期间，模块将值设置到 **Pin number** 参数中指定的引脚。在所有其他模式的仿真期间，模块不执行任何操作。
