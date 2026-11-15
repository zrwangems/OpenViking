---
type: simulink-block
title: 'GPIO Read'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F4-Discovery Board Blocks'
documentation_page: 'gpioread'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/gpioread.html'
language: zh-CN
chinese_source: official
---

# GPIO Read

## 端口

### 输出

### **Port\_1** — 包含逻辑值的输出端口 标量

包含数字引脚逻辑值的输出端口。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **GPIO port** — 用于读取 GPIO 引脚状态的 GPIO 端口 GPIOA (默认) | GPIOA | GPIOB | GPIOC | GPIOD | GPIOE | GPIOF | GPIOG | GPIOH | GPIOI

选择 GPIOA 至 GPIOI 端口之一来获得 GPIO 引脚状态。

### **引脚编号** — 用于读取逻辑状态的 GPIO 引脚 0 (默认) | 标量

选择一个用于读取逻辑状态的 GPIO 引脚。

### **采样时间** — 读取引脚值的时频 -1 (默认) | 标量

指定此模块读取引脚值的频率，以秒为单位。请输入大于零的值。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4-Discovery

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2013b 中推出**

## 描述

读取 GPIO 引脚状态

读取 STM32F4-Discovery™ 板的数字引脚的逻辑值。
