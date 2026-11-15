---
type: simulink-block
title: 'C2000 Space Vector Generator'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Optimization / C28x DMC'
documentation_page: 'c2000spacevectorgenerator'
documentation_source_path: 'ref/c2000spacevectorgenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# C2000 Space Vector Generator

## 端口

R2025b 中未记录。

## 参数

R2025b 中未记录。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

R2025b 中未记录。

## 描述

定子参考电压的占空比

# C2000 Space Vector Generator

定子参考电压的占空比

将现有 DMC 模块替换为 MCB 模块，以提高可用性和未来兼容性。建议使用 Control Algorithm Design (Motor Control Blockset) 中的模块。虽然这些模块并非一一对应的替代模块，但它们使您能够实现相同的功能。

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

此模块使用空间矢量 PWM 技术计算可生成给定定子参考电压的占空比。空间矢量脉宽调制是三相电压源逆变器三个上桥臂功率器件的开关序列，用于交流感应电机和永磁同步电机驱动等应用。该开关方案在定子相中产生三个伪正弦电流。此技术通过组合与基本空间矢量对应的开关模式来逼近给定的定子参考电压矢量。

此模块的输入为

- Alpha component — 直轴静止参考坐标系上的参考定子电压矢量（`Ua`）
- Beta component — 直轴正交参考坐标系上的参考定子电压矢量（`Ub`）

alpha 和 beta 分量通过反 Clarke 方程进行变换，并投影为参考相电压。这些电压在输出中表示为 PWM1 (`Ta`)、PWM3 (`Tb`) 和 PWM5 (`Tc`) 的占空比。

**注意**

此模块的实现不会在代码生成期间调用对应的 Texas Instruments® 库函数。TI 函数使用全局 Q 设置，而此模块使用的 MathWorks® 代码会根据模块输入动态调整 Q 格式。有关更多信息，请参阅 Using the IQmath Library。

- C2000 Space Vector Generator 模块
