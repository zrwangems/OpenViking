---
type: simulink-block
title: 'Helical Interleaver'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Interleaving / Convolutional'
documentation_page: 'helicalinterleaver'
documentation_source_path: 'ref/helicalinterleaver.html'
language: zh-CN
chinese_source: worker-translation
---

# Helical Interleaver

## 端口

R2025b 中未记录。

## 参数

**Number of columns in helical array**
:   螺旋阵列中的列数 C。

**Group size**
:   每组输入符号的大小 N。输入宽度为 C 乘以 N。

**Helical array step size**
:   连续输入组在螺旋阵列各自列中的行间隔数。

**Initial conditions**
:   一个标量，用于在放置第一个输入之前填充阵列。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

使用螺旋阵列对输入符号进行置换

Helical Interleaver 模块通过以螺旋方式将输入信号中的符号放入阵列，然后将阵列的行发送到输出端口，从而对输入信号中的符号进行置换。

该模块在内部使用阵列进行计算。如果 *C* 是 **Number of columns in helical array** 参数，则阵列具有 *C* 列和无限行。如果 *N* 是 **Group size** 参数，则该模块在每个时间步接受长度为 *C*·*N* 的输入，并将输入划分为连续的 *N* 个符号组。从仿真开始计数，该模块将第 *k* 组沿列 *k* mod *C* 放入阵列。由于对 *C* 取模，并且第 *k* 组中的第一个符号位于行 1+(*k*-1)· *s*，其中 *s* 是 **Helical array step size** 参数，因此放置是螺旋的。阵列中不包含输入符号的位置具有由 **Initial condition** 参数指定的默认内容。

该模块通过依次读取接下来的 *N* 行，将 *C*·*N* 个符号从阵列发送到输出端口。在给定时间步，输出符号可能是 **Initial condition** 参数值、来自该时间步输入向量的符号，或前一时间步留在阵列中的符号。

该模块接受包含 *C*·*N* 个元素的列向量输入信号。

该模块可以接受数据类型 `int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`boolean`、`single`、`double` 和定点。此输出的数据类型将与输入信号的数据类型相同。
