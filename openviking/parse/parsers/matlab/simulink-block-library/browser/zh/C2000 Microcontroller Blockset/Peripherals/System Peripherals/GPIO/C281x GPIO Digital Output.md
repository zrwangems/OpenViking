---
type: simulink-block
title: 'C281x GPIO Digital Output'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / System Peripherals / GPIO'
documentation_page: 'c281xgpiodigitaloutput'
documentation_source_path: 'ref/c281xgpiodigitaloutput.html'
language: zh-CN
chinese_source: worker-translation
---

# C281x GPIO Digital Output

## 端口

R2025b 中未记录。

## 参数

**IO Port**
:   选择要使用的输入/输出端口：`GPIOPA`、
    `GPIOPB`、`GPIOPD`、
    `GPIOPE`、`GPIOPF` 或
    `GPIOPG`，并选择要为数字
    输入启用的 I/O Port 位。（C281x 上没有 GPIOPC 端口。）如果
    选择多个位，则预期为向量输入。清零的位可用于
    外设功能。多个 GPIO DO 模块不能共享同一个 I/O
    端口。

    **注意**

    数字 I/O 的输入功能以及到相关
    外设的输入路径在板上启用。如果将某个引脚配置为数字 I/O，则
    相应的外设功能不能使用。

以下表格显示共享引脚。

**GPIO A MUX**

| 位 | 外设名称   (Bit =1) | GPIO 名称   (Bit = 0) |
| --- | --- | --- |
| 0 | PWM1 | GPIOA0 |
| 1 | PWM2 | GPIOA1 |
| 2 | PWM3 | GPIOA2 |
| 3 | PWM4 | GPIOA3 |
| 4 | PWM5 | GPIOA4 |
| 5 | PWM6 | GPIOA5 |
| 8 | QEP1/CAP1 | GPIOA8 |
| 9 | QEP2/CAP2 | GPIOA9 |
| 10 | CAP3 | GPIOA10 |

**GPIO B MUX**

| 位 | 外设名称   (Bit =1) | GPIO 名称   (Bit = 0) |
| --- | --- | --- |
| 0 | PWM7 | GPIOB0 |
| 1 | PWM8 | GPIOB1 |
| 2 | PWM9 | GPIOB2 |
| 3 | PWM10 | GPIOB3 |
| 4 | PWM11 | GPIOB4 |
| 5 | PWM12 | GPIOB5 |
| 8 | QEP3/CAP4 | GPIOB8 |
| 9 | QEP4/CAP5 | GPIOB9 |
| 10 | CAP6 | GPIOB10 |

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

R2025b 中未记录。

## 描述

用于数字输出的通用 I/O 引脚

此模块配置通用 I/O (GPIO) 寄存器，这些寄存器控制用于数字输出的 GPIO 共享引脚。每个 I/O 端口都有一个 MUX 寄存器，用于选择外设操作或数字 I/O 操作。

**注意**

此模块不支持定点输入。

**注意**

为避免丢失新设置，请在更改 **IO Port** 参数之前点击 **Apply**。
