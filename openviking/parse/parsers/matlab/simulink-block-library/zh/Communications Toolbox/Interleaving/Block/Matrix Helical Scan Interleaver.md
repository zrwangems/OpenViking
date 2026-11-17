---
type: simulink-block
title: 'Matrix Helical Scan Interleaver'
family: 'interleaving'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Interleaving / Block'
documentation_page: 'matrixhelicalscaninterleaver'
documentation_source_path: 'ref/matrixhelicalscaninterleaver.html'
language: zh-CN
chinese_source: worker-translation
---

# Matrix Helical Scan Interleaver

## 端口

R2025b 中未提供文档。

## 参数

**行数**
:   模块在计算中使用的矩阵的行数。

**列数**
:   模块在计算中使用的矩阵的列数。

**数组步长**
:   模块读取的对角线的斜率。

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

通过沿对角线选择矩阵元素来置换输入符号

Matrix Helical Scan Interleaver 模块通过以下方式执行块交织：将输入符号逐行填入矩阵，然后以螺旋方式将矩阵内容发送到输出端口。**行数** 和 **列数** 参数定义了模块在内部计算时使用的矩阵的维度。

螺旋方式是指模块通过沿矩阵的对角线选择元素来选择输出符号。每条对角线中的元素数与 **列数** 参数一致，必要时模块会在矩阵边缘处回绕。模块遍历对角线时，行索引和列索引均递增。第一条对角线之后的每条对角线都从上一条对角线第一个元素的下一行开始。

**数组步长** 参数是每条对角线的斜率，即列索引每增加 1 时行索引的增加量。此参数必须是介于零和 **行数** 参数之间的整数。如果 **数组步长** 参数为零，则模块不执行交织，输出与输入相同。

此模块接受列向量输入信号。输入向量的元素数必须为 **行数** 与 **列数** 的乘积。

模块接受以下数据类型：`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`boolean`、`single`、`double` 和定点。输出信号的数据类型继承自输入信号。
