---
type: simulink-block
title: 'Algebraic Deinterleaver'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Interleaving / Block'
documentation_page: 'algebraicdeinterleaver'
documentation_source_path: 'ref/algebraicdeinterleaver.html'
language: zh-CN
chinese_source: worker-translation
---

# Algebraic Deinterleaver

## 端口

R2025b 中未提供文档。

## 参数

**类型**
:   模块用于解交织的置换表类型。
    选项为 `Takeshita-Costello` 和
    `Welch-Costas`。

**元素个数**
:   输入向量中的元素个数 *N*。

**乘法因子**
:   模块用于计算对应交织器的循环向量的因子。仅当将 **类型** 设置为
    `Takeshita-Costello` 时，才会显示此字段。

**循环移位**
:   模块在创建对应交织器的置换表时对索引进行移位的量。仅当将 **类型** 设置为
    `Takeshita-Costello` 时，才会显示此字段。

**本原元**
:   有限域 GF(N+1) 中阶为 *N* 的元素。仅当 **类型** 设置为
    `Welch-Costas` 时，才会显示此字段。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

使用通过代数方法导出的置换恢复输入符号的顺序

Algebraic Deinterleaver 模块可恢复使用 Algebraic Interleaver 模块交织的序列的原始顺序。在典型用法中，两个模块的参数设置为相同的值。

**元素个数** 参数 *N* 指示输入向量中包含的数值个数。此模块接受列向量输入信号。

此模块接受以下数据类型：`int8`、
`uint8`、`int16`、`uint16`、
`int32`、`uint32`、`boolean`、
`single`、`double` 和 fixed-point。输出信号的数据类型继承自输入信号。

**类型** 参数指示模块用于生成相应置换表的代数方法。选项为
`Takeshita-Costello` 和
`Welch-Costas`。每种方法都有其特定的参数和限制；这些参数和限制在
Algebraic Interleaver 模块的参考页面上进行了说明。
