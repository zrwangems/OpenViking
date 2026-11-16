---
type: simulink-block
title: 'Discrete-Time VCO'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Synchronization and Receiver Design'
documentation_page: 'discretetimevco'
documentation_source_path: 'ref/discretetimevco.html'
language: zh-CN
chinese_source: worker-translation
---

# Discrete-Time VCO

## 端口

在 R2025b 中未提供文档。

## 参数

**输出幅度**
:   输出的幅度。

**静态频率 (Hz)**
:   输入信号为零时振荡器输出的频率。

**输入灵敏度**
:   该值对输入电压进行缩放，进而对相对于 **静态频率** 值的偏移量进行缩放。**输入灵敏度** 的单位为 Hertz per volt。

**初始相位 (rad)**
:   振荡器的初始相位，以 rad 为单位。

**采样时间**
:   计算的采样时间。

## 所属库

在 R2025b 中未提供文档。

## 模块特性

在 R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

### R2024a：将被移除

Discrete-Time VCO 将被移除。要设计压控振荡器 (VCO) 和锁相环 (PLL)，请使用 Phase-Locked Loops (Mixed-Signal Blockset) 模块。

## 描述

（将被移除）在离散时间下实现压控振荡器 (VCO)

Discrete-Time VCO 模块生成一个信号，该信号的频率相对于 **静态频率** 参数的偏移量与输入信号成正比。输入信号被解释为电压。如果输入信号为 *u*(*t*)，则输出信号为

y(t)=Accos(2πfct+2πkc∫0tu(τ)dτ+φ)

其中，*A*c 为 **输出幅度**，*f*c 为 **静态频率**，*k*c 为 **输入灵敏度**，φ 为 **初始相位**。

此模块使用离散时间积分器来计算上述方程。

此模块接受数据类型为 `single` 或 `double` 的标量输入信号。输出信号的数据类型继承自输入信号。对于代码生成，此模块仅支持双精度。
