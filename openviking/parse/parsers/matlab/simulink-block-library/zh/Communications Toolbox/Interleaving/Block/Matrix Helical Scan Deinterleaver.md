---
type: simulink-block
title: 'Matrix Helical Scan Deinterleaver'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Interleaving / Block'
documentation_page: 'matrixhelicalscandeinterleaver'
documentation_source_path: 'ref/matrixhelicalscandeinterleaver.html'
language: zh-CN
chinese_source: worker-translation
---

# Matrix Helical Scan Deinterleaver

## 端口

R2025b 中未记录。

## 参数

**Number of rows**
:   模块用于计算的矩阵的行数。

**Number of columns**
:   模块用于计算的矩阵的列数。

**Array step size**
:   模块写入的对角线的斜率。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

通过沿对角线填充矩阵来恢复输入符号的顺序

Matrix Helical Scan Deinterleaver 模块通过以螺旋方式将输入符号填入矩阵，然后逐行将矩阵内容发送到输出端口，来执行块解交织。**Number of rows** 和 **Number of columns** 参数指定模块内部用于计算的矩阵的维度。

螺旋方式是指模块沿矩阵的对角线放置输入符号。每条对角线中的元素数量与 **Number of columns** 参数值相等；必要时，模块会在越过矩阵边缘后进行回绕。模块按行索引和列索引均增大的方式遍历对角线。除第一条对角线外，每条对角线都从上一条对角线第一个元素的下一行开始。

**Array step size** 参数是每条对角线的斜率，即列索引每增加 1 时行索引增加的量。此参数必须是 0 到 **Number of rows** 参数值之间的整数。如果 **Array step size** 参数为 0，则模块不执行解交织，输出与输入相同。

此模块接受列向量输入信号。输入向量的元素数量必须等于 **Number of rows** 与 **Number of columns** 的乘积。

模块接受以下数据类型：`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`boolean`、`single`、`double` 和 fixed-point。输出信号的数据类型继承自输入信号。
