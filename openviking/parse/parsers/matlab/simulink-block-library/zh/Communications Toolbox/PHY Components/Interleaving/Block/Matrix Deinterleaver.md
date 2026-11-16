---
type: simulink-block
title: 'Matrix Deinterleaver'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Interleaving / Block'
documentation_page: 'matrixdeinterleaver'
documentation_source_path: 'ref/matrixdeinterleaver.html'
language: zh-CN
chinese_source: worker-translation
---

# Matrix Deinterleaver

## 端口

R2025b 中未提供文档。

## 参数

**行数**
:   模块用于计算的矩阵中的行数。

**列数**
:   模块用于计算的矩阵中的列数。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

通过按列填充矩阵并按行清空矩阵来置换输入符号

Matrix Deinterleaver 模块通过以下方式执行块解交织：将输入符号逐列填充到矩阵中，然后逐行将矩阵内容发送到输出端口。**行数**和**列数**参数指定模块内部用于计算的矩阵维度。

此模块接受列向量输入信号。输入向量的长度必须等于**行数**乘以**列数**。

该模块接受以下数据类型：`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`boolean`、`single`、`double` 和 fixed-point。输出信号的数据类型继承自输入信号。
