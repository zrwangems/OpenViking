---
type: simulink-block
title: 'Integrate and Dump'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Comm Filters'
documentation_page: 'integrateanddump'
documentation_source_path: 'ref/integrateanddump.html'
language: zh-CN
chinese_source: worker-translation
---

# Integrate and Dump

## 端口

R2025b 中未记录。

## 参数

**Integration period**
:   两次复位之间的输入采样数。

**Offset**
:   一个非负整数向量或标量，指定在仿真开始时从输入数据的每一列中丢弃的输入采样数。

**输出中间值**
:   确定模块是否在连续复位之间输出中间累积和。

### 定点信号流图

### 定点属性

以下参数的设置仅在模块输入为定点信号时适用。

**Rounding mode**
:   使用此参数指定当定点计算结果无法精确映射为结果数据类型和定标所能表示的数值时要使用的舍入方法。

    有关详细信息，请参阅 Rounding Modes 或 Rounding Mode: Simplest (Fixed-Point Designer)。

**Saturate on integer overflow**
:   使用此参数指定当定点计算结果的幅值超出存储结果的数据类型和定标的范围时要使用的方法：

    - Saturate 将正溢出表示为所用范围内的最大正数，将负溢出表示为所用范围内的最大负数。
    - Wrap 使用模运算将溢出值强制转换回数据类型的可表示范围。有关详细信息，请参阅 Modulo Arithmetic (Fixed-Point Designer)。

**Accumulator—Mode**
:   使用 **Accumulator—Mode** 参数指定如何指定累加器的字长和小数长度：

    - 当选择 `Inherit via internal rule` 时，模块自动计算累加器输出的字长和小数长度。
    - 当选择 `Same as input` 时，这些特性与模块输入的特性相匹配。
    - 当选择 `Binary point scaling` 时，可以输入累加器的字长和小数长度（以位为单位）。
    - 当选择 `Slope and bias scaling` 时，可以输入累加器的字长（以位为单位）和斜率。

**Output**
:   使用 **Output** 参数选择如何指定模块输出的字长和小数长度：

    - 当选择 `Same as accumulator` 时，这些特性与累加器的特性相匹配。
    - 当选择 `Same as input` 时，这些特性与模块输入的特性相匹配。
    - 当选择 `Binary point scaling` 时，输入输出的字长和小数长度（以位为单位）。
    - 当选择 `Slope and bias scaling` 时，输入输出的字长（以位为单位）和斜率。

有关定点应用相关参数的更多信息，请参阅 Specify Fixed-Point Attributes for Blocks。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

对离散时间信号进行积分，并周期性地复位为零

Integrate and Dump 模块创建离散时间输入信号的累积和，同时按照固定时间表将和复位为零。当仿真开始时，模块丢弃 **Offset** 参数中指定的采样数。在此初始时段之后，模块沿列对输入信号求和，并每 *N* 个输入采样将和复位为零，其中 *N* 是 **Integration period** 参数值。复位在该时间步模块产生输出之后发生。

当系统的发射器使用简单的方波脉冲模型时，接收器模型通常使用积分清零操作。光纤和扩频通信系统（如 CDMA（码分多址）应用）也使用该操作。

此模块接受标量、列向量或矩阵输入信号。当输入信号不是标量值时，它必须包含 *k*·*N* 行，其中 *k* 为某个正整数。对于这些输入信号，模块独立处理每一列。

选中 **输出中间值** 会按如下方式影响内容、维度和采样时间：

- 如果清除该复选框，则模块在每个复位时刻输出累积和。

  - 如果输入是标量值，则输出采样时间是输入采样时间的 *N* 倍，并且模块经历一个持续时间为一个输出采样周期的延迟。在这种情况下，输出维度与输入维度匹配。
  - 如果输入是 (*k*·*N*)×*n* 矩阵，则输出为 *k*×*n*。在这种情况下，模块不经历延迟，输出周期与输入周期匹配。
- 如果选中该复选框，则模块在每个时间步输出累积和。输出具有与输入相同的采样时间和相同的矩阵维度。

### 瞬态与延迟

**Offset** 参数中的非零值会导致模块在初始时段丢弃输入采样时输出一个或多个零。如果输入是具有 *n* 列的矩阵，且 **Offset** 参数是长度为 *n* 的向量，则 **Offset** 向量的第 *m* 个元素是第 *m* 列数据的偏移量。如果 **Offset** 是标量，则模块对每一列数据应用相同的偏移量。由于非零 **Offset** 值而输出的初始零是瞬态效应，而不是持续延迟。

当清除 **输出中间值** 时，模块的输出在整个仿真过程中相对于其输入存在延迟：

- 如果输入是标量值，则在任何瞬态效应结束后，输出延迟一个采样。也就是说，在去除输入和输出中的瞬态后，可以看到第 *m* 个积分周期的结果出现在索引为 m+1 的输出采样中。
- 如果输入是列向量或矩阵，且 **Offset** 参数非零，则在瞬态效应结束后，每个积分周期的结果出现在与该积分周期*最后*一个输入采样对应的输出帧中。当某个积分周期跨越两个输入帧时，这比与该积分周期第一个输入采样对应的输出帧晚一帧。有关这种情况的示例，请参阅 Example of Transient and Delay。
