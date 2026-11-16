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

未在 R2025b 中记录。

## 参数

**置换向量源**
:   用于指定置换向量来源的选项。来源可以是 `Dialog` 或
    `Input port`。默认值为 `Dialog`。

**置换向量**
:   长度为 N 的向量，列出输出元素所对应的输入元素索引。仅当
    **置换向量源**设置为 `Dialog` 时，此参数才可用。

## 所属库

未在 R2025b 中记录。

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2006a 之前推出**

## 描述

重新排列输入向量中的符号

General Block Interleaver 模块重新排列其输入向量的元素，不会重复或遗漏任何元素。如果输入包含 *N* 个元素，则**置换向量**参数是长度为 *N* 的列向量。该列向量按顺序指示用于构成长度为 *N* 的输出向量的输入元素索引；即：

Output(*k*) = Input(**Permutation
vector**(k))

其中，*k* 是 1 到 *N* 之间的每个整数。**置换向量**的内容必须是 1 到 N 之间的整数，且不得重复。

输入和**置换向量**参数都必须是列向量信号。

此模块可以输出长度在仿真过程中发生变化的序列。有关长度可变的序列或可变大小信号的详细信息，请参阅可变大小信号基础 (Simulink)。

此模块接受以下数据类型：`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`boolean`、`single`、`double` 和 fixed-point。输出信号的数据类型继承自输入信号。
