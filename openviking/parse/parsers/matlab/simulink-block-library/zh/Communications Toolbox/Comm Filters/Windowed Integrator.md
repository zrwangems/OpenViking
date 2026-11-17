---
type: simulink-block
title: 'Windowed Integrator'
family: 'comm-filters'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Comm Filters'
documentation_page: 'windowedintegrator'
documentation_source_path: 'ref/windowedintegrator.html'
language: zh-CN
chinese_source: worker-translation
---

# Windowed Integrator

## 端口

R2025b 中未提供文档。

## 参数

**积分周期**
:   积分区间的长度，以采样数计。

**输入处理**
:   指定模块处理输入信号的方式。您可以将此参数设置为以下选项之一：

    - `Columns as channels (frame based)` —
      选择此选项时，模块将输入的每一列视为一个独立通道。
    - `Elements as channels (sample based)` —
      选择此选项时，模块将输入的每个元素视为一个独立通道。

**舍入模式**
:   选择定点运算的舍入模式。当定点计算结果无法精确映射为由存储该结果的数据类型和定标所能表示的数字时，模块会使用**舍入模式**。滤波器系数不受此参数影响；它们始终采用 `Nearest` 舍入。有关详细信息，请参阅“舍入模式”或“舍入模式：最简单 (Fixed-Point Designer)”。

**整数溢出时饱和**
:   选择定点运算的溢出模式。滤波器系数不受此参数影响；它们始终进行饱和处理。

**系数**
:   模块实现使用直接型 FIR 滤波器，所有抽头权重均设置为 1。当输入数据为定点信号时，**系数**参数控制用于表示抽头（即 1）的数据类型。

    选择指定滤波器系数（分子和/或分母）的字长和小数长度的方式。

    - 选择 `Same word length as input` 时，滤波器系数的字长与模块输入的字长匹配。在此模式下，系数的小数长度会自动设置为仅二进制小数点定标，该定标根据系数的值和字长提供尽可能高的精度。
    - 选择 `Specify word length` 时，您可以输入系数的字长，单位为 bits。在此模式下，系数的小数长度会自动设置为仅二进制小数点定标，该定标根据系数的值和字长提供尽可能高的精度。
    - 选择 `Binary point scaling` 时，您可以输入系数的字长和小数长度，单位为 bits。如果适用，您可以分别为分子和分母系数输入不同的小数长度。
    - 选择 `Slope and bias scaling` 时，您可以输入系数的字长（单位为 bits）和斜率。如果适用，您可以分别为分子和分母系数输入不同的斜率。此模块要求斜率为 2 的幂，且偏置为 0。
    - 滤波器系数不受**舍入模式**和**整数溢出时饱和**参数影响；它们始终进行饱和处理并采用 `Nearest` 舍入。

    有关此模块中系数数据类型用法的更多信息和图示，请参阅 Discrete FIR Filter (Simulink) 模块的滤波器结构图。

**乘积输出**
:   使用此参数指定如何设置乘积输出的字长和小数长度。

    - 选择 `Same as input` 时，这些特性与模块输入的相应特性一致。
    - 选择 `Binary point scaling` 时，您可以输入乘积输出的字长和小数长度，单位为 bits。
    - 选择 `Slope and bias scaling` 时，您可以输入乘积输出的字长（单位为 bits）和斜率。此模块要求斜率为 2 的幂，且偏置为 0。

    有关此模块中乘积输出数据类型用法的更多信息和图示，请参阅 Discrete FIR Filter (Simulink) 和“乘法数据类型”。

**累加器**
:   使用此参数指定如何设置累加器的字长和小数长度。

    - 选择 `Same as input` 时，这些特性与模块输入的相应特性一致。
    - 选择 `Same as product output` 时，这些特性与乘积输出的相应特性一致。
    - 选择 `Binary point scaling` 时，您可以输入累加器的字长和小数长度，单位为 bits。
    - 选择 `Slope and bias scaling` 时，您可以输入累加器的字长（单位为 bits）和斜率。此模块要求斜率为 2 的幂，且偏置为 0。

    有关此模块中累加器数据类型用法的更多信息和图示，请参阅 Discrete FIR Filter (Simulink) 和“乘法数据类型”。

**输出**
:   选择指定输出字长和小数长度的方式：

    - 选择 `Same as input` 时，这些特性与模块输入的相应特性一致。
    - 选择 `Same as accumulator` 时，这些特性与累加器的相应特性一致。
    - 选择 `Binary point scaling` 时，您可以输入输出的字长和小数长度，单位为 bits。
    - 选择 `Slope and bias scaling` 时，您可以输入输出的字长（单位为 bits）和斜率。此模块要求斜率为 2 的幂，且偏置为 0。

**锁定定标以防止自动定标工具更改**
:   选择此参数，以防止 Fixed-Point Tool 中的自动定标工具覆盖您在此模块封装中指定的任何定点定标。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

对固定长度的时间窗口进行积分

Windowed Integrator 模块对固定长度滑动时间窗口内的输入信号值进行累积求和。如果**积分周期**参数为 N，输入采样表示为 x(1)、x(2)、x(3)、...，则第 n 个输出采样是 k 介于 n-N+1 和 n 之间时 x(k) 值的总和。对于 n-N+1 小于 1 的情况，模块使用初始条件 0 来表示这些采样。

### 输入和输出信号

此模块接受标量、列向量和 *M*×*N* 矩阵输入信号。模块按如下方式对 *M*×*N* 输入矩阵进行滤波：

- 当您将**输入处理**参数设置为 `Columns as channels (frame based)` 时，模块将每一列视为一个独立通道。在此模式下，模块会创建 *N* 个相同滤波器的实例，每个实例都有自己独立的状态缓冲区。在每个 Simulink® 时间步，这 *N* 个滤波器中的每一个都处理 *M* 个输入采样。
- 当您将**输入处理**参数设置为 `Elements as channels (sample based)` 时，模块将每个元素视为一个独立通道。在此模式下，模块会创建 *M*\**N* 个相同滤波器的实例，每个实例都有自己独立的状态缓冲区。每个滤波器在每个 Simulink 时间步处理一个输入采样。

输出维度始终等于输入信号的维度。有关每个模块端口支持的数据类型的信息，请参阅本页上的“支持的数据类型”表。
