---
type: simulink-block
title: 'General Block Interleaver'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Interleaving / Block'
documentation_page: 'generalblockinterleaver'
documentation_source_path: 'ref/generalblockinterleaver.html'
language: zh-CN
chinese_source: worker-translation
---

# General Block Interleaver

## 端口

R2025b 中未记录。

## 参数

**Permutation vector source**
:   一个选择项，用于指定置换向量的来源。来源可以是 `Dialog` 或 `Input
    port`。默认值为
    `Dialog`。

**Permutation vector**
:   一个长度为 N 的向量，列出了输出元素来自输入向量的索引。此参数仅在
    **Permutation vector source** 设置为
    `Dialog` 时可用。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

对输入向量中的符号重新排序

General Block Interleaver 模块重新排列其输入向量的元素，不重复也不省略任何元素。如果输入包含 *N* 个元素，则 **Permutation vector** 参数是一个长度为 *N* 的列向量。该列向量按顺序指示构成长度为 *N* 的输出向量的输入元素的索引；即，

输出(*k*) = 输入(**Permutation
vector**(k))

对于 1 到 *N* 之间的每个整数 *k*。**Permutation vector** 的内容必须是 1 到 N 之间的整数，且不得有重复。

输入和 **Permutation vector** 参数都必须是列向量信号。

此模块可以输出在仿真期间长度变化的序列。有关长度变化的序列或可变大小信号的更多信息，请参阅 Variable-Size Signal Basics (Simulink)。

此模块接受以下数据类型：`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`boolean`、`single`、`double` 和定点。输出信号从输入信号继承其数据类型。
