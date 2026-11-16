---
type: simulink-block
title: 'C2000 Ramp Generator'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Optimization / C28x DMC'
documentation_page: 'c2000rampgenerator'
documentation_source_path: 'ref/c2000rampgenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# C2000 Ramp Generator

## 端口

R2025b 中未记录。

## 参数

**Maximum step angle**
:   最大步长，它决定输出的变化率（即，斜坡信号的最小周期）。

    当您为 IQ Math 模块中的参数输入双精度浮点值时，软件会将其转换为与 c28x 处理器上的行为兼容的单精度值。

**Maximum step angle**
:   最大步长，它决定输出的变化率（即，斜坡信号的最小周期）。

    当您为 IQ Math 模块中的参数输入双精度浮点值时，软件会将其转换为与 c28x 处理器上的行为兼容的单精度值。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

R2025b 中未记录。

## 描述

生成斜坡输出

# C2000 Ramp Generator

生成斜坡输出

将现有 DMC 模块替换为 MCB 模块，以提高可用性和未来兼容性。建议您使用 Control Algorithm Design (Motor Control Blockset) 中的模块。虽然这些模块不是一对一替代，但它们使您能够实现相同的功能。

| C28x DMC lib | MCB 中的 C28x DMC lib 等效项 |
| --- | --- |
| C2000 Clarke Transformation | Clarke Transform (Motor Control Blockset) |
| C2000 Inverse Park Transformation | Inverse Park Transform (Motor Control Blockset) |
| C2000 Park Transformation | Park Transform (Motor Control Blockset) |
| C2000 PID Controller | PI Controller (Motor Control Blockset) |
| C2000 Ramp Control | Position Generator (Motor Control Blockset) |
| C2000 Ramp Generator | Position Generator (Motor Control Blockset) |
| C2000 Space Vector Generator | PWM Reference Generator (Motor Control Blockset) |
| C2000 Speed Measurement | Speed Measurement (Motor Control Blockset) |

此模块根据斜坡信号的斜率（`gain`）、斜坡信号中的直流偏移（`offset`）以及斜坡信号的频率（`freq`）输入生成斜坡输出（`out`）。所有输入和输出都是 32-bit 定点数，Q 值介于 1 和 29 之间。
