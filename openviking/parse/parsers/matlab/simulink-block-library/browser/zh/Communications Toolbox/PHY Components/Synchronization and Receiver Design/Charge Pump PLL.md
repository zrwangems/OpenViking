---
type: simulink-block
title: 'Charge Pump PLL'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Synchronization and Receiver Design'
documentation_page: 'chargepumppll'
documentation_source_path: 'ref/chargepumppll.html'
language: zh-CN
chinese_source: worker-translation
---

# Charge Pump PLL

## 端口

R2025b 中未记录。

## 参数

**低通滤波器分子**
:   低通滤波器传递函数的分子，表示为一个向量，该向量按 *s* 的降幂顺序列出系数。

**低通滤波器分母**
:   低通滤波器传递函数的分母，表示为一个向量，该向量按 *s* 的降幂顺序列出系数。

**VCO 输入灵敏度 (Hz/V)**
:   该值用于缩放 VCO 的输入，并因此影响相对于 **VCO 静态频率** 值的偏移量。**VCO 输入灵敏度** 的单位为 Hertz per volt。

**VCO 静态频率 (Hz)**
:   施加到 VCO 的电压为零时 VCO 信号的频率。该频率应与输入信号的频率相匹配。

**VCO 初始相位 (rad)**
:   VCO 信号的初始相位。

**VCO 输出幅值**
:   VCO 信号的幅值。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

### R2024a: 已移除

Charge Pump PLL 已移除。要设计压控振荡器 (VCO) 和锁相环 (PLL)，请使用 Phase-Locked Loops (Mixed-Signal Blockset) 模块。

## 描述

（已移除）使用数字鉴相器实现电荷泵锁相环

Charge Pump PLL（锁相环）模块会自动调整本地生成信号的相位，使其与输入信号的相位相匹配。该模块适用于数字信号。

此 PLL 包含以下三个组件：

- 时序逻辑鉴相器，也称为数字鉴相器或鉴相/鉴频器。
- 滤波器。您可以使用 **低通滤波器分子** 和 **低通滤波器分母** 参数指定滤波器传递函数。每个参数都是一个向量，按 *s* 的降幂顺序给出相应多项式的系数。

  要设计滤波器，请使用 `butter`、`cheby1` 和 `cheby2` 等函数。默认滤波器为 II 型切比雪夫滤波器，其传递函数由以下命令生成。

  ```
  [num, den] = cheby2(3,40,100,'s')
  ```
- 压控振荡器 (VCO)。您可以使用 **VCO 输入灵敏度**、**VCO 静态频率**、**VCO 初始相位** 和 **VCO 输出幅值** 参数指定 VCO 的特性。

此模块接受基于采样的标量输入信号。输入信号表示接收到的信号。三个输出端口分别输出：

- 滤波器的输出
- 鉴相器的输出
- VCO 的输出

时序逻辑鉴相器根据信号波形的过零点工作。输入信号与 VCO 信号之间相位差的平衡点等于 π。时序逻辑检测器可以补偿 VCO 与输入信号之间可能存在的任何频率差。因此，时序逻辑鉴相器可用作频率检测器。
