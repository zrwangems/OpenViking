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

R2025b 中未记录。

## 参数

**Number of rows**
:   模块用于计算的矩阵的行数。

**Number of columns**
:   模块用于计算的矩阵的列数。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

通过按行填充矩阵并按列清空矩阵来置换输入符号

Matrix Interleaver 模块通过按行用输入符号填充矩阵，然后按列将矩阵内容发送到输出端口，从而执行块交织。

**Number of rows** 和 **Number of columns** 参数是模块内部用于计算的矩阵的维度。

该模块接受列向量输入信号。输入向量的元素数必须是 **Number of rows** 和 **Number of columns** 的乘积。

该模块接受以下数据类型：`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`boolean`、`single`、`double` 和定点。输出信号的数据类型继承自输入信号。
