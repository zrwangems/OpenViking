---
type: simulink-block
title: 'Random Deinterleaver'
family: 'interleaving'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Interleaving / Block'
documentation_page: 'randomdeinterleaver'
documentation_source_path: 'ref/randomdeinterleaver.html'
language: zh-CN
chinese_source: worker-translation
---

# Random Deinterleaver

## 端口

R2025b 中未提供文档。

## 参数

**元素个数**
:   输入向量中的元素个数。

**初始种子**
:   随机数生成器的初始种子值。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2006a 之前推出**

## 描述

使用随机置换恢复输入符号的顺序

Random Deinterleaver 模块使用随机置换重新排列其输入向量中的元素。**初始种子**参数用于初始化该模块确定置换时所用的随机数生成器。如果此模块与 Random Interleaver 模块的**初始种子**值相同，则这两个模块互为逆模块。

此模块接受列向量输入信号。**元素个数**参数指示输入向量中包含的数值个数。

该模块接受以下数据类型：`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`boolean`、`single`、`double` 和 fixed-point。输出信号的数据类型继承自输入信号。
