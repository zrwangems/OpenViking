---
type: simulink-block
title: 'Matrix Interleaver'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Interleaving / Block'
documentation_page: 'matrixinterleaver'
documentation_source_path: 'ref/matrixinterleaver.html'
language: zh-CN
chinese_source: worker-translation
---

# Matrix Interleaver

## 端口

R2025b 中未提供文档。

## 参数

**行数**
:   模块在计算中使用的矩阵的行数。

**列数**
:   模块在计算中使用的矩阵的列数。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

通过按行填充矩阵并按列清空矩阵来置换输入符号

Matrix Interleaver 模块通过将输入符号逐行填入矩阵，然后逐列将矩阵内容发送到输出端口来执行块交织。

**行数** 和 **列数** 参数是模块内部用于计算的矩阵的维度。

此模块接受列向量输入信号。输入向量的元素数必须为 **行数** 与 **列数** 的乘积。

该模块接受以下数据类型：`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`boolean`、`single`、`double` 和 fixed-point。输出信号的数据类型继承自输入信号。
