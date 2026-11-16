---
type: simulink-block
title: 'APP Decoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Error Detection and Correction / Convolutional Coding'
documentation_page: 'appdecoder'
documentation_source_path: 'ref/appdecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# APP Decoder

## 端口

R2025b 中未提供文档。

## 参数

**网格结构**
:   包含卷积编码器网格描述的 MATLAB 结构体。

**终止方法**
:   `Truncated` 或 `Terminated`。此参数指示卷积编码器在帧的开始和结束时如何处理网格。

**算法**
:   `True APP`、`Max*` 或 `Max`。

**缩放位数**
:   介于 0 和 8 之间的整数，表示为避免精度损失，解码器对数据进行缩放的位数。仅当**算法**设置为 `Max*` 时，此字段才处于活动状态。

**禁用 L(c) 输出端口**
:   选中此复选框可禁用模块的第二个输出 L(c)。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2006a 之前引入**

## 描述

使用后验概率 (APP) 方法对卷积码进行解码

APP Decoder 模块对卷积码执行后验概率 (APP) 解码。

### 输入信号和输出信号

输入 *L*(*u*) 表示编码器输入比特的对数似然序列，而输入 *L*(*c*) 表示码比特的对数似然序列。输出 *L*(*u*) 和 *L*(*c*) 是根据编码器信息对这些序列进行更新后得到的版本。

如果卷积码使用包含 2*n* 个可能符号的符号集，则对于某个正整数 *Q*，此模块的 *L*(*c*) 向量的长度为 *Q*\**n*。同样，如果解码后的数据使用包含 2*k* 个可能输出符号的符号集，则此模块的 *L*(u) 向量的长度为 *Q*\**k*。

对于任意正整数 *Q*，此模块均接受列向量输入信号。

如果只需要输入 *L*(*c*) 和输出 *L*(*u*)，则可以将 Simulink Ground (Simulink) 模块连接到输入 *L*(*u*)，并将 Simulink® Terminator (Simulink) 模块连接到输出 *L*(*c*)。

此模块接受 `single` 和 `double` 数据类型。但是，两个输入必须具有相同的数据类型。输出数据类型与输入数据类型相同。

### 指定编码器

要定义生成编码输入的卷积编码器，请使用**网格结构**参数。此参数是一个 MATLAB® 结构体，其格式在“卷积码的网格描述”中进行了介绍。可以通过以下两种方式使用此参数字段：

- 如果 MATLAB 工作区中有包含网格结构的变量，请将其名称作为**网格结构**参数输入。这种方式更为可取，因为与下述用法相比，它可使 Simulink 在每次仿真开始时花费更少的时间更新框图。
- 如果要使用编码器的约束长度、生成多项式以及可能的反馈连接多项式来指定编码器，请在**网格结构**字段中使用 `poly2trellis` 命令。例如，要使用约束长度为 7、码生成多项式为 171 和 133（八进制数）、反馈连接为 171（八进制）的编码器，请将**网格结构**参数设置为

  `poly2trellis(7,[171 133],171)`

要指示编码器在每帧的开始和结束时如何处理网格，请将**终止方法**参数设置为 `Truncated` 或 `Terminated`。`Truncated` 选项表示编码器在每帧开始时重置为全零状态。`Terminated` 选项表示编码器强制网格在每帧结束时处于全零状态。如果使用 Convolutional Encoder 模块，并将其**操作模式**参数设置为 `Truncated (reset every frame)`，请在此模块中使用 `Truncated` 选项。如果使用 Convolutional Encoder 模块，并将其**操作模式**参数设置为 `Terminate trellis by appending bits`，请在此模块中使用 `Terminated` 选项。

### 指定算法的详细信息

可以使用**算法**参数控制解码算法的一部分。`True APP` 选项按照 [1] 第 V 节中的方程 20–23 实现后验概率解码。为提高速度，`Max*` 和 `Max` 选项均使用其他量来近似如下表达式：

log∑iexp(ai)

`Max` 选项使用 max(*a*i) 作为近似值，而 `Max*` 选项使用 max(*a*i) 加上由 ln(1+exp(−|ai−1−ai|)) [3] 给出的校正项。

`Max*` 选项会启用对话框中的**缩放位数**参数。此参数表示模块对内部处理的数据进行缩放的位数（将输入乘以 (2^`numScalingBits`)，并将输出前的结果除以相同的因子）。使用此参数可避免计算过程中的精度损失。
