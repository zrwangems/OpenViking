---
type: simulink-block
title: 'Continuous-Time VCO'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Synchronization and Receiver Design'
documentation_page: 'continuoustimevco'
documentation_source_path: 'ref/continuoustimevco.html'
language: zh-CN
chinese_source: worker-translation
---

# Continuous-Time VCO

## 端口

R2025b 中未提供文档。

## 参数

**输出幅值**
:   输出信号的幅值。

**静态频率**
:   输入信号为零时振荡器输出的频率。

**输入灵敏度**
:   该值用于缩放输入电压，从而也缩放相对于 **静态频率** 值的频率偏移。
    **输入灵敏度** 的单位为 Hertz per volt。

**初始相位**
:   振荡器的初始相位，单位为 radians。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

### R2024a: 已移除

Continuous-Time VCO 已被移除。要设计压控振荡器 (VCO) 和锁相环 (PLL)，请使用 Phase-Locked Loops (Mixed-Signal Blockset) 模块。

## 描述

(已移除) 实现压控振荡器 (VCO)

Continuous-Time VCO 模块生成一个信号，其频率相对于 **静态频率** 参数的偏移量与输入信号成正比。输入信号被解释为电压。如果输入信号为 *u*(*t*)，则输出信号为

y(t)=Accos(2πfct+2πkc∫0tu(τ)dτ+φ)

其中，*A*c 是 **输出幅值** 参数，*f*c 是 **静态频率** 参数，*k*c 是 **输入灵敏度** 参数，φ 是 **初始相位** 参数。

此模块使用连续时间积分器来实现上述方程。

输入和输出均为基于采样的标量信号。
