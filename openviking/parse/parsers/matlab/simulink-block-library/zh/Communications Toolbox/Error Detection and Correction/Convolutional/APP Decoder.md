---
type: simulink-block
title: 'APP Decoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction / Convolutional'
documentation_page: 'appdecoder'
documentation_source_path: 'ref/appdecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# APP Decoder

## 端口

R2025b 中未记录。

## 参数

**Trellis structure**
:   包含卷积编码器网格描述的 MATLAB 结构体。

**Termination method**
:   `Truncated` 或 `Terminated`。此参数指示卷积编码器如何处理帧开头和结尾处的网格。

**Algorithm**
:   `True APP`、`Max*` 或 `Max`。

**Number of scaling bits**
:   一个介于 0 和 8 之间的整数，指示解码器为避免丢失精度而对数据进行缩放的位数。仅当 **Algorithm** 设置为 `Max*` 时，此字段才处于活动状态。

**禁用 L(c) 输出端口**
:   选中此复选框可禁用次级模块输出 L(c)。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

使用后验概率 (APP) 方法解码卷积码

APP Decoder 模块对卷积码执行后验概率 (APP) 解码。

### 输入信号和输出信号

输入 *L*(*u*) 表示编码器输入比特的对数似然序列，而输入 *L*(*c*) 表示码比特的对数似然序列。输出 *L*(*u*) 和 *L*(*c*) 是基于编码器信息对这些序列的更新版本。

如果卷积码使用包含 2*n* 个可能符号的字母表，则此模块的 *L*(*c*) 向量长度为 *Q*\**n*，其中 *Q* 为某个正整数。类似地，如果解码数据使用包含 2*k* 个可能输出符号的字母表，则此模块的 *L*(u) 向量长度为 *Q*\**k*。

此模块接受列向量输入信号，其中 *Q* 可为任意正整数。

如果您只需要输入 *L*(*c*) 和输出 *L*(*u*)，可以将 Simulink Ground (Simulink) 模块连接到输入 *L*(*u*)，并将 Simulink® Terminator (Simulink) 模块连接到输出 *L*(*c*)。

此模块接受 `single` 和 `double` 数据类型。但是，两个输入必须具有相同类型。输出数据类型与输入数据类型相同。

### 指定编码器

要定义生成编码输入的卷积编码器，请使用 **Trellis structure** 参数。此参数是一个 MATLAB® 结构体，其格式在 Trellis Description of a Convolutional Code 中描述。您可以通过两种方式使用此参数字段：

- 如果 MATLAB 工作区中有一个包含网格结构体的变量，请输入其名称作为 **Trellis structure** 参数。这种方式更可取，因为与接下来描述的用法相比，它使 Simulink 在每次仿真开始时花费更少时间更新图。
- 如果要使用约束长度、生成多项式和可能的反馈连接多项式来指定编码器，请在 **Trellis structure** 字段中使用 `poly2trellis` 命令。例如，要使用约束长度为 7、码生成多项式为 171 和 133（八进制数）以及反馈连接为 171（八进制）的编码器，请将 **Trellis structure** 参数设置为

  `poly2trellis(7,[171 133],171)`

要指示编码器如何处理每帧开头和结尾处的网格，请将 **Termination method** 参数设置为 `Truncated` 或 `Terminated`。`Truncated` 选项指示编码器在每帧开头重置为全零状态。`Terminated` 选项指示编码器强制网格在每帧结束时处于全零状态。如果您使用 Convolutional Encoder 模块并将 **Operation mode** 参数设置为 `Truncated (reset every frame)`，请在此模块中使用 `Truncated` 选项。如果您使用 Convolutional Encoder 模块并将 **Operation mode** 参数设置为 `Terminate trellis by appending bits`，请在此模块中使用 `Terminated` 选项。

### 指定算法细节

您可以使用 **Algorithm** 参数控制部分解码算法。`True APP` 选项按照 [1] 第 V 节中的方程 20–23 实现后验概率解码。为了提高速度，`Max*` 和 `Max` 选项都会用其他量近似如下表达式

log∑iexp(ai)

`Max` 选项使用 max(*a*i) 作为近似值，而 `Max*` 选项使用 max(*a*i) 加上由 ln(1+exp(−|ai−1−ai|)) 给出的修正项 [3]。

`Max*` 选项会启用对话框中的 **Scaling bits** 参数。此参数是模块在内部处理数据时对数据进行缩放的位数（将输入乘以 (2^`numScalingBits`)，并将输出前结果除以相同因子）。使用此参数可避免在计算过程中丢失精度。
