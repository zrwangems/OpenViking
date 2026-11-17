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

R2025b 中未记录。

## 参数

**Number of columns in helical array**
:   螺旋阵列中的列数 *C*。

**Group size**
:   每组符号的大小 *N*。输入宽度为 *C* 乘以 *N*。

**Helical array step size**
:   当模块从螺旋阵列的各自列中选择连续输出组时，这些输出组之间相隔的行数。

**Initial conditions**
:   一个标量，用于在放置第一个输入之前填充阵列。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

恢复被螺旋交织器置换的符号顺序

Helical Deinterleaver 模块通过将输入信号中的符号逐行放入阵列，然后以螺旋方式选择组发送到输出端口，从而对输入信号中的符号进行置换。

该模块在内部使用阵列进行计算。如果 *C* 是 **Number of columns in helical array** 参数，则阵列具有 *C* 列和无限行。如果 *N* 是 **Group size** 参数，则该模块在每个时间步接受长度为 *C*·*N* 的输入，并将它们插入阵列接下来的 *N* 行中。该模块还会将 **Initial condition** 参数放入阵列顶部若干行的某些位置（不仅是为了适应螺旋模式，也是为了保留依次通过 Helical Interleaver 和 Helical Deinterleaver 模块的符号的向量索引）。

输出由连续的 *N* 个符号组组成。从仿真开始算起，该模块从列 *k* mod *C* 中选择阵列中的第 k 个输出组。由于对 C 取模，并且第 *k* 组中的第一个符号位于行 1+(*k*-1)\*s，其中 *s* 是 **Helical array step size** 参数，因此该选择是螺旋式的。

该模块接受包含 *C*·*N* 个元素的列向量输入信号。

该模块可以接受数据类型 `int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`boolean`、`single`、`double` 和定点。此输出的数据类型将与输入信号的数据类型相同。

### 交织器-解交织器对的延迟

在使用 Helical Interleaver 模块和 Helical Deinterleaver 模块处理一条消息后，解交织数据滞后于原始消息

CN⌈s(C−1)N⌉

个采样。在此延迟过去之前，解交织器输出要么是 Helical Deinterleaver 模块中的 **Initial condition** 参数，要么是 Helical Interleaver 模块中的 **Initial condition** 参数。

如果您的模型在交织器输出和解交织器输入之间产生额外延迟，则恢复序列滞后于原始序列的量等于额外延迟与上述公式中量之和。为了正确同步，交织器和解交织器之间的延迟必须为 m·
*C* · *N*，其中 *m* 为某个非负整数。如有必要，您可以使用 DSP System Toolbox™
Delay 模块手动调整延迟。
