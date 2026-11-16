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

R2025b 中未提供文档。

## 参数

**螺旋阵列中的列数**
:   螺旋阵列中的列数 C。

**组大小**
:   每个输入符号组的大小 N。输入宽度为 C 乘以
    N。

**螺旋阵列步长**
:   连续输入组在螺旋阵列各自列中相隔的行数。

**初始条件**
:   在放置第一个输入之前用于填充阵列的标量。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2006a 之前推出**

## 描述

使用螺旋阵列对输入符号进行置换

Helical Interleaver 模块通过将输入信号中的符号以螺旋方式放入阵列，然后将阵列的各行发送到输出端口，从而对这些符号进行置换。

模块在内部使用该阵列进行计算。如果 *C* 是 **螺旋阵列中的列数** 参数，则该阵列有 *C* 列，且行数不限。如果 *N* 是 **组大小** 参数，则模块在每个时间步接受长度为 *C*·*N* 的输入，并将输入划分为连续的组，每组包含 *N* 个符号。从仿真开始计数，模块将第 *k* 组沿第 *k* mod *C* 列放置到阵列中。由于对 *C* 取模，并且第 *k* 组中的第一个符号位于第 1+(*k*-1)· *s* 行，因此这种放置方式呈螺旋状，其中 *s* 是 **螺旋阵列步长** 参数。阵列中不包含输入符号的位置，其默认内容由 **初始条件** 参数指定。

模块通过依次读取接下来的 *N* 行，将阵列中的 *C*·*N* 个符号发送到输出端口。在给定时间步，输出符号可能是 **初始条件** 参数值、该时间步输入向量中的符号，或者是先前时间步遗留在阵列中的符号。

此模块接受包含 *C*·*N* 个元素的列向量输入信号。

该模块可接受 `int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`boolean`、`single`、`double` 和 fixed-point 数据类型。此输出的数据类型将与输入信号的数据类型相同。
