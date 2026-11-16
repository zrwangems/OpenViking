---
type: simulink-block
title: 'Baseband PLL'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Synchronization and Receiver Design'
documentation_page: 'basebandpll'
documentation_source_path: 'ref/basebandpll.html'
language: zh-CN
chinese_source: worker-translation
---

# Baseband PLL

## 端口

在 R2025b 中未记录。

## 参数

**低通滤波器分子**
:   低通滤波器传递函数的分子，表示为一个向量，该向量按 *s* 的降幂顺序列出系数。

**低通滤波器分母**
:   低通滤波器传递函数的分母，表示为一个向量，该向量按 *s* 的降幂顺序列出系数。

**VCO 输入灵敏度 (Hz/V)**
:   该值对 VCO 的输入进行缩放，进而决定 VCO 的频率相对于其静态频率的偏移量。

## 所属库

在 R2025b 中未记录。

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**于 R2006a 之前推出**

### R2024a: 已移除

Baseband PLL 已被移除。要设计压控振荡器 (VCO) 和锁相环 (PLL)，请使用 Phase-Locked Loops (Mixed-Signal Blockset) 模块。

## 描述

(已移除) 实现基带锁相环

Baseband PLL（锁相环）模块是一个反馈控制系统，可自动调整本地生成信号的相位，使其与输入信号的相位相匹配。此模块采用基带方法，不依赖于载波频率。

此 PLL 由以下三个组件组成：

- 用作鉴相器的积分器。
- 滤波器。使用 **低通滤波器分子** 和 **低通滤波器分母** 参数指定滤波器的传递函数。每个参数都是一个向量，按 *s* 的降幂顺序给出相应多项式的系数。

  要设计滤波器，可以使用 `cheby1` 和 `cheby2` 函数。默认滤波器为 II 型切比雪夫滤波器，其传递函数由以下命令生成。

  `[num, den] = cheby2(3,40,100,'s')`
- 压控振荡器 (VCO)。使用 **VCO 输入灵敏度** 参数指定 VCO 信号对其输入的灵敏度。此参数以 Hertz per volt 为单位，是一个缩放因子，用于确定 VCO 的频率偏离其静态频率的程度。

此模块接受基于采样的标量信号。输入信号表示接收到的信号。三个输出端口分别输出：

- 滤波器的输出
- 鉴相器的输出
- VCO 的输出
