---
type: simulink-block
title: 'Quantizing Encoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Source Coding'
documentation_page: 'quantizingencoder'
documentation_source_path: 'ref/quantizingencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Quantizing Encoder

## 端口

R2025b 中未记录。

## 参数

**Quantization partition**
:   分区区间端点的向量。

**Quantization codebook**
:   分配给每个分区的输出值向量。

**索引输出数据类型**
:   选择输出数据类型。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用分区和码本对信号进行量化

Quantizing Encoder 模块根据 **Partition** 向量对输入信号进行量化，并根据 **Codebook** 向量对输入信号进行编码。该模块独立处理每个向量元素。输入必须是离散时间信号。该模块独立处理每个向量元素。有关每个模块端口支持的数据类型的信息，请参阅本页的支持数据类型表。

第一个输出是量化索引。第二个输出是量化信号。量化信号的值取自 **Codebook** 向量。

**Quantization partition** 参数 *P* 是长度为 n 的实数向量，其元素按严格升序排列。输入值 *x* 对应的量化索引（第二个输出信号值）为

- 0 若 *x* ≤ *P*(1)
- m 若 *P*(m) < *x* ≤ *P*(m+1)
- n 若 *P*(n) < *x*

**Quantization codebook** 参数的长度为 n+1，为量化中的每个分区规定一个值。**Quantization codebook** 的第一个元素是负无穷与 *P* 的第一个元素之间区间的值。该模块的第二个输出信号包含基于量化索引和规定值的输入信号的量化。

使用 `lloyds` 函数并以数据的代表性样本作为训练数据，以获得合适的分区参数和码本参数。
