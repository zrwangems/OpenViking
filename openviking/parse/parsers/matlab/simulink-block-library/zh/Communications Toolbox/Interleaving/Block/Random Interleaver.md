---
type: simulink-block
title: 'Random Interleaver'
family: 'interleaving'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Interleaving / Block'
documentation_page: 'randominterleaver'
documentation_source_path: 'ref/randominterleaver.html'
language: zh-CN
chinese_source: worker-translation
---

# Random Interleaver

## 端口

R2025b 中未提供文档。

## 参数

**Number of elements**
:   输入向量中的元素数量。

**Initial seed**
:   随机数生成器的初始种子值。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

使用随机置换对输入符号重新排序

Random Interleaver 模块使用随机置换重新排列其输入向量中的元素。该模块接受列向量输入信号。**Number of elements** 参数指示输入向量中包含多少个数值。

该模块接受以下数据类型：`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`boolean`、`single`、`double` 和 fixed-point。输出信号的数据类型继承自输入信号。

**Initial seed** 参数用于初始化模块确定置换时所用的随机数生成器。给定种子时，该模块生成的置换是可预测的，但不同的种子会产生不同的置换。
