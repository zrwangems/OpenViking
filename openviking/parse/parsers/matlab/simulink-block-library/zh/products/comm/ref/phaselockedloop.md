---
type: simulink-block
title: 'Phase-Locked Loop'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Synchronization and Receiver Design'
documentation_page: 'phaselockedloop'
documentation_source_path: 'ref/phaselockedloop.html'
language: zh-CN
chinese_source: worker-translation
---

# Phase-Locked Loop

## 端口

R2025b 中未提供文档。

## 参数

**低通滤波器分子**
:   低通滤波器传递函数的分子，表示为一个向量，该向量按 *s* 的降幂顺序列出系数。

**低通滤波器分母**
:   低通滤波器传递函数的分母，表示为一个向量，该向量按 *s* 的降幂顺序列出系数。

**VCO 输入灵敏度 (Hz/V)**
:   该值对 VCO 的输入进行缩放，并因此缩放相对于 **VCO 静态频率** 值的频率偏移。**VCO 输入灵敏度** 的单位为 Hertz per volt。

**VCO 静态频率 (Hz)**
:   当施加到 VCO 的电压为零时，VCO 信号的频率。该值应与输入信号的载波频率匹配。

**VCO 初始相位 (rad)**
:   VCO 信号的初始相位。

**VCO 输出幅值**
:   VCO 信号的幅值。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

### R2024a: 已删除

Phase-Locked Loop 已被删除。要设计压控振荡器 (VCO) 和锁相环 (PLL)，请使用 Phase-Locked Loops (Mixed-Signal Blockset) 模块。

## 描述

（已删除）实现锁相环 (PLL)，以恢复输入信号的相位

Phase-Locked Loop 模块是一个反馈控制系统，可自动调整本地生成信号的相位，使其与输入信号的相位匹配。此模块最适用于输入为窄带信号的情况。

此 PLL 包含以下三个组件：

- 用作鉴相器的乘法器。
- 滤波器。您可以使用 **低通滤波器分子** 和 **低通滤波器分母** 参数指定滤波器传递函数。每个参数都是一个向量，按 *s* 的降幂顺序给出相应多项式的系数。

  要设计滤波器，您可以使用 `butter`、`cheby1` 和 `cheby2` 等函数。默认滤波器是切比雪夫 II 型滤波器，其传递函数由以下命令生成。

  `[num, den] = cheby2(3,40,100,'s')`
- 压控振荡器 (VCO)。您可以使用 **VCO 静态频率**、**VCO 初始相位** 和 **VCO 输出幅值** 参数指定 VCO 的特性。

此模块接受基于采样的标量输入信号。输入信号表示接收到的信号。三个输出端口分别输出：

- 滤波器的输出
- 鉴相器的输出
- VCO 的输出
