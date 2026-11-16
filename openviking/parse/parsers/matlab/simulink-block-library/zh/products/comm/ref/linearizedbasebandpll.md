---
type: simulink-block
title: 'Linearized Baseband PLL'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Synchronization and Receiver Design'
documentation_page: 'linearizedbasebandpll'
documentation_source_path: 'ref/linearizedbasebandpll.html'
language: zh-CN
chinese_source: worker-translation
---

# Linearized Baseband PLL

## 端口

未在 R2025b 中记录。

## 参数

**低通滤波器分子**
:   低通滤波器传递函数的分子，以向量形式表示，该向量按 *s* 的降幂次序列出各项系数。

**低通滤波器分母**
:   低通滤波器传递函数的分母，以向量形式表示，该向量按 *s* 的降幂次序列出各项系数。

**VCO 输入灵敏度 (Hz/V)**
:   该值对 VCO 的输入进行缩放，进而决定 VCO 相对于其静止频率的频移。

## 所属库

未在 R2025b 中记录。

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2006a 之前推出**

### R2024a: 已移除

Linearized Baseband PLL 已被移除。要设计压控振荡器 (VCO) 和锁相环 (PLL)，请使用 Phase-Locked Loops (Mixed-Signal Blockset) 模块。

## 描述

（已移除）实现基带锁相环的线性化版本

Linearized Baseband PLL 模块是一个反馈控制系统，可自动调整本地生成信号的相位，使其与输入信号的相位相匹配。该模块采用基带建模方法，并使用 *x* 近似 sin(*x*) 来简化计算。基带 PLL 模型取决于传入信号的幅度，但不取决于载波频率。

此 PLL 由以下三个组件组成：

- 一个用作鉴相器的积分器。
- 一个滤波器。您可以使用 **低通滤波器分子** 和 **低通滤波器分母** 参数指定滤波器的传递函数。每个参数都是一个向量，按 *s* 的降幂顺序给出相应多项式的系数。

  要设计滤波器，您可以使用 `butter`、`cheby1` 和 `cheby2` 等函数。默认滤波器是切比雪夫 II 型滤波器，其传递函数由以下命令生成。

  `[num, den] = cheby2(3,40,100,'s')`
- 一个压控振荡器 (VCO)。您可以使用 **VCO 输入灵敏度** 参数指定 VCO 信号对其输入的灵敏度。该参数以赫兹/伏特为单位，是一个比例因子，用于确定 VCO 偏离其静止频率的程度。

该模块接受基于采样的标量输入信号。输入信号表示接收到的信号。三个输出端口分别产生：

- 滤波器的输出
- 鉴相器的输出
- VCO 的输出
