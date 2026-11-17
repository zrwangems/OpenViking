---
type: simulink-block
title: 'Random Deinterleaver'
family: 'comm'
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

R2025b 中未记录。

## 参数

**Number of elements**
:   输入向量中的元素数量。

**Initial seed**
:   随机数生成器的初始种子值。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用随机置换恢复输入符号的顺序

Random Deinterleaver 模块使用随机置换重新排列其输入向量的元素。**Initial seed** 参数用于初始化该模块用来确定置换的随机数生成器。如果此模块和 Random Interleaver 模块的 **Initial seed** 具有相同的值，则这两个模块互为逆操作。

此模块接受列向量输入信号。**Number of elements** 参数指示输入向量中有多少个数字。

此模块接受以下数据类型 `int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`boolean`、`single`、`double` 和定点。输出信号的数据类型继承自输入信号。
