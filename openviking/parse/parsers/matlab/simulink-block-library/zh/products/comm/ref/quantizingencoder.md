---
type: simulink-block
title: 'Quantizing Encoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Source Coding'
documentation_page: 'quantizingencoder'
documentation_source_path: 'ref/quantizingencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Quantizing Encoder

## 端口

R2025b 中未提供文档。

## 参数

**Quantization partition**
:   由分区区间端点构成的向量。

**Quantization codebook**
:   分配给每个分区的输出值向量。

**Index output data type**
:   选择输出数据类型。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

使用分区和码本对信号进行量化

Quantizing Encoder 模块根据 **Partition** 向量对输入信号进行量化，并根据 **Codebook** 向量对输入信号进行编码。该模块独立处理每个向量元素。输入必须是离散时间信号。该模块独立处理每个向量元素。有关每个模块端口支持的数据类型的信息，请参阅本页上的 Supported Data Type 表。

第一个输出是量化索引。第二个输出是量化信号。量化信号的值取自 **Codebook** 向量。

**Quantization partition** 参数 *P* 是一个长度为 n 的实向量，其元素按严格升序排列。与输入值 *x* 对应的量化索引（第二个输出信号值）为：

- 如果 *x* ≤ *P*(1)，则为 0
- 如果 *P*(m) < *x* ≤ *P*(m+1)，则为 m
- 如果 *P*(n) < *x*，则为 n

**Quantization codebook** 参数的长度为 n+1，用于为量化中的每个分区指定一个值。**Quantization codebook** 的第一个元素是负无穷大与 *P* 的第一个元素之间区间的值。该模块的第二个输出信号包含基于量化索引和指定值对输入信号进行量化所得的结果。

使用 `lloyds` 函数，并将数据的代表性样本作为训练数据，以获得适当的分区和码本参数。
