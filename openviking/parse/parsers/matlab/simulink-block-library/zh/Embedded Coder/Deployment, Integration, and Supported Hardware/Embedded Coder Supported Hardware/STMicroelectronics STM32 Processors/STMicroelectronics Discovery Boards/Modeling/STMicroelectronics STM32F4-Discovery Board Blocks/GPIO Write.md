---
type: simulink-block
title: 'GPIO Write'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F4-Discovery Board Blocks'
documentation_page: 'gpiowrite'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/gpiowrite.html'
language: zh-CN
chinese_source: official
---

# GPIO Write

## 端口

### 输入

### **Port\_1** — 设置 GPIO 引脚状态 标量

用于设置 GPIO 引脚状态的输入端口。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **GPIO port** — 用于设置 GPIO 引脚状态的 GPIO 端口 GPIOA (默认) | GPIOA | GPIOB | GPIOC | GPIOD | GPIOE | GPIOF | GPIOG | GPIOH | GPIOI

选择 GPIOA 至 GPIOI 端口之一来设置 GPIO 引脚状态。

### **引脚编号** — 用于设置 GPIO 引脚状态的 GPIO 端口 1 (默认)

选择一个 GPIO 引脚来写入逻辑状态。

### **初始设置 GPIO 引脚** — 用于设置模型初始化期间 GPIO 引脚状态的选项 off (默认) | on

选择此选项可设置模型初始化期间的 GPIO 引脚状态。

### **当输入为 true 时切换引脚** — 当输入为 true 时启用 GPIO 引脚切换的选项 off (默认) | on

选择此选项可在输入为 true 时启用 GPIO 引脚切换。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4-Discovery

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2013b 中推出**

## 描述

设置 GPIO 引脚状态

设置 STM32F4-Discovery™ 板的数字引脚的逻辑值。
