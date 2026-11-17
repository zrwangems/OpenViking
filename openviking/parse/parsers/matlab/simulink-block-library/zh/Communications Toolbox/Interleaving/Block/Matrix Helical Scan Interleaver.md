---
type: simulink-block
title: 'Matrix Helical Scan Interleaver'
family: 'comm'
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
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters: []
```

**Number of rows**
:   模块用于计算的矩阵的行数。

**Number of columns**
:   模块用于计算的矩阵的列数。

**Array step size**
:   模块读取的对角线的斜率。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

通过沿对角线选择矩阵元素来置换输入符号

Matrix Helical Scan Interleaver 模块通过逐行用输入符号填充矩阵，然后以螺旋方式将矩阵内容发送到输出端口来执行块交织。**Number of rows** 和 **Number of columns** 参数是模块内部用于计算的矩阵的维度。

螺旋方式意味着模块通过沿矩阵的对角线选择元素来选择输出符号。每条对角线上的元素数量与 **Number of columns** 参数匹配，必要时模块会在矩阵边缘处回绕。模块遍历对角线时行索引和列索引同时递增。第一条对角线之后的每条对角线都从前一条对角线的第一个元素下方一行开始。

**Array step size** 参数是每条对角线的斜率，即当列索引增加 1 时行索引增加的量。此参数必须是介于零和 **Number of rows** 参数之间的整数。如果 **Array step size** 参数为零，则模块不进行交织，输出与输入相同。

此模块接受列向量输入信号。输入向量的元素数量必须是 **Number of rows** 和 **Number of columns** 的乘积。

此模块接受以下数据类型：`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`boolean`、`single`、`double` 和定点。输出信号的数据类型继承自输入信号。
