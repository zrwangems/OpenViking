---
type: simulink-block
title: 'Helical Deinterleaver'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Interleaving / Convolutional'
documentation_page: 'helicaldeinterleaver'
documentation_source_path: 'ref/helicaldeinterleaver.html'
language: zh-CN
chinese_source: worker-translation
---

# Helical Deinterleaver

## 端口

R2025b 中未提供文档。

## 参数

**螺旋阵列中的列数**
:   螺旋阵列中的列数 *C*。

**组大小**
:   每个符号组的大小 *N*。输入宽度为 *C* 乘以 *N*。

**螺旋阵列步长**
:   模块从螺旋阵列的相应列中选择连续输出组时，这些输出组之间相隔的行数。

**初始条件**
:   在放入第一个输入之前用于填充阵列的标量。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

恢复经螺旋交织器置换的符号顺序

Helical Deinterleaver 模块通过将输入信号中的符号逐行放入阵列，然后以螺旋方式选择符号组并发送至输出端口，来对这些符号进行置换。

该模块在内部使用阵列进行计算。如果 *C* 为 **螺旋阵列中的列数** 参数，则该阵列有 *C* 列，且行数不受限制。如果 *N* 为 **组大小** 参数，则该模块在每个时间步接受长度为 *C*·*N* 的输入，并将这些符号插入阵列的接下来 *N* 行中。该模块还将 **初始条件** 参数的值放入阵列顶部几行中的某些位置（不仅是为了适应螺旋模式，也是为了保留依次经过 Helical Interleaver 和 Helical Deinterleaver 模块的符号的向量索引）。

输出由连续的符号组构成，每组包含 *N* 个符号。从仿真开始起计数，模块从阵列的 *k* mod *C* 列中选择第 *k* 个输出组。这种选择方式之所以是螺旋式的，是因为进行了模 C 归约，并且第 *k* 组中的第一个符号位于第 1+(*k*-1)\*s 行，其中 *s* 为 **螺旋阵列步长** 参数。

此模块接受包含 *C*·*N* 个元素的列向量输入信号。

该模块可接受 `int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`boolean`、`single`、`double` 和 fixed-point 数据类型。此输出的数据类型将与输入信号的数据类型相同。

### 交织器-解交织器对的延迟

使用 Helical Interleaver 模块和 Helical Deinterleaver 模块处理消息后，解交织数据比原始消息滞后

CN⌈s(C−1)N⌉

个采样点。在此延迟结束之前，解交织器的输出为 Helical Deinterleaver 模块中的 **初始条件** 参数值，或 Helical Interleaver 模块中的 **初始条件** 参数值。

如果您的模型在交织器输出与解交织器输入之间引入了额外延迟，则恢复后的序列相对于原始序列的滞后量，等于该额外延迟与上述公式中的延迟量之和。为了实现正确同步，对于某个非负整数 *m*，交织器与解交织器之间的延迟必须为 m· *C* · *N*。必要时，可以使用 DSP System Toolbox™ 的 Delay 模块手动调整延迟。
