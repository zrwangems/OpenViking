---
type: simulink-block
title: 'Windowed Integrator'
family: 'comm'
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
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters: []
```

**Integration period**
:   积分区间的长度，以采样点为单位。

**Input processing**
:   指定模块如何处理输入信号。您可以将此参数设置为以下选项之一：

    - `Columns as channels (frame based)` —
      选择此选项时，模块将输入的每一列视为独立通道。
    - `Elements as channels (sample based)` —
      选择此选项时，模块将输入的每个元素视为独立通道。

**Rounding mode**
:   选择定点运算的舍入模式。当定点计算结果无法精确映射为存储结果的数据类型和定标所能表示的数值时，模块使用 **Rounding mode**。滤波器系数不受此参数约束；它们始终舍入到 `Nearest`。有关详细信息，请参阅 Rounding Modes 或 Rounding Mode: Simplest (Fixed-Point Designer)。

**Saturate on integer overflow**
:   选择定点运算的溢出模式。滤波器系数不受此参数约束；它们始终饱和。

**Coefficients**
:   模块实现使用直接型 FIR 滤波器，所有抽头权重均设置为一。当输入数据为定点信号时，**Coefficients** 参数控制用哪种数据类型表示抽头（即 1）。

    选择如何指定滤波器系数（分子和/或分母）的字长和小数长度。

    - 当您选择 `Same word length as
      input` 时，滤波器系数的字长与模块输入的字长一致。在此模式下，系数的小数长度自动设置为仅二进制点定标，在给定系数值和字长的情况下为您提供尽可能最佳的精度。
    - 当您选择 `Specify word
      length` 时，您可以输入系数的字长（以位为单位）。在此模式下，系数的小数长度自动设置为仅二进制点定标，在给定系数值和字长的情况下为您提供尽可能最佳的精度。
    - 当您选择 `Binary point
      scaling` 时，您可以输入系数的字长和小数长度（以位为单位）。如适用，您可以为分子和分母系数输入各自的小数长度。
    - 当您选择 `Slope and bias
      scaling` 时，您可以输入字长（以位为单位）和系数的斜率。如适用，您可以为分子和分母系数输入各自的斜率。此模块要求斜率为 2 的幂且偏置为零。
    - 滤波器系数不受 **Rounding
      mode** 和 **Saturate on integer
      overflow** 参数约束；它们始终饱和并舍入到 `Nearest`。

    有关此模块中系数数据类型使用的更多信息和图示，请参阅 Discrete FIR Filter (Simulink) 模块的滤波器结构图。

**Product output**
:   使用此参数指定如何设定乘积输出的字长和小数长度。

    - 当您选择 `Same as input` 时，这些特性与模块输入的特性一致。
    - 当您选择 `Binary point
      scaling` 时，您可以输入乘积输出的字长和小数长度（以位为单位）。
    - 当您选择 `Slope and bias
      scaling` 时，您可以输入字长（以位为单位）和乘积输出的斜率。此模块要求斜率为 2 的幂且偏置为零。

    有关此模块中乘积输出数据类型使用的更多信息和图示，请参阅 Discrete FIR Filter (Simulink) 和 Multiplication Data Types。

**Accumulator**
:   使用此参数指定如何设定累加器的字长和小数长度。

    - 当您选择 `Same as input` 时，这些特性与模块输入的特性一致。
    - 当您选择 `Same as product
      output` 时，这些特性与乘积输出的特性一致。
    - 当您选择 `Binary point
      scaling` 时，您可以输入累加器的字长和小数长度（以位为单位）。
    - 当您选择 `Slope and bias
      scaling` 时，您可以输入字长（以位为单位）和累加器的斜率。此模块要求斜率为 2 的幂且偏置为零。

    有关此模块中累加器数据类型使用的更多信息和图示，请参阅 Discrete FIR Filter (Simulink) 和 Multiplication Data Types。

**Output**
:   选择如何指定输出的字长和小数长度：

    - 当您选择 `Same as input` 时，这些特性与模块输入的特性一致。
    - 当您选择 `Same as accumulator` 时，这些特性与累加器的特性一致。
    - 当您选择 `Binary point scaling` 时，您可以输入输出的字长和小数长度（以位为单位）。
    - 当您选择 `Slope and bias scaling` 时，您可以输入字长（以位为单位）和输出的斜率。此模块要求斜率为 2 的幂且偏置为零。

**Lock scaling against changes by the autoscaling tool**
:   选择此参数以防止在此模块封装中指定的任何定点定标被 Fixed-Point Tool 中的自动定标工具覆盖。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

在固定长度的时间窗口上积分

Windowed Integrator 模块在固定长度的滑动时间窗口上创建输入信号值的累积和。如果 **Integration period** 参数为 N，输入采样点表示为 x(1)、x(2)、x(3)、...，则第 n 个输出采样点是 k 在 n-N+1 到 n 之间的 x(k) 值之和。当 n-N+1 小于 1 时，模块使用初始条件 0 来表示这些采样点。

### 输入和输出信号

此模块接受标量、列向量和 *M*×*N* 矩阵输入信号。模块按如下方式对 *M*×*N* 输入矩阵进行滤波：

- 当您将 **Input processing** 参数设置为 `Columns as channels (frame based)` 时，模块将每一列视为独立通道。在此模式下，模块创建 *N* 个相同滤波器的实例，每个实例拥有独立的状态缓冲区。这 *N* 个滤波器中的每一个在每个 Simulink® 时间步处理 *M* 个输入采样点。
- 当您将 **Input processing** 参数设置为 `Elements as channels (sample based)` 时，模块将每个元素视为独立通道。在此模式下，模块创建 *M*\**N* 个相同滤波器的实例，每个实例拥有独立的状态缓冲区。每个滤波器在每个 Simulink 时间步处理一个输入采样点。

输出维度始终等于输入信号的维度。有关每个模块端口支持的数据类型的信息，请参阅本页的支持数据类型表。
