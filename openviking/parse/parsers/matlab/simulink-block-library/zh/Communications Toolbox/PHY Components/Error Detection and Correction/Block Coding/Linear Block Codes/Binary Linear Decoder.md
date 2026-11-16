---
type: simulink-block
title: 'Binary Linear Decoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Error Detection and Correction / Block Coding / Linear Block Codes'
documentation_page: 'binarylineardecoder'
documentation_source_path: 'ref/binarylineardecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Binary Linear Decoder

## 端口

R2025b 中未提供文档。

## 参数

**Generator matrix**
:   码的生成矩阵；与 Binary Linear Encoder 模块中的相同。

**Decoding table**
:   一个 2N-K-by-N 矩阵，其中列出每个码字伴随式对应的纠错向量；或者为标量 0，此时模块默认使用与 **Generator matrix** 参数对应的表。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

对线性分组码进行解码以恢复二进制向量数据

Binary Linear Decoder 模块从线性分组码的二进制码字向量中恢复二进制消息向量。

**Generator matrix** 参数是分组码的生成矩阵。为了正确解码，该参数应与对应 Binary Linear Encoder 模块中的 **Generator matrix** 参数匹配。如果 *N* 是码的码字长度，则 **Generator matrix** 必须具有 *N* 列。如果 *K* 是码的消息长度，则 **Generator matrix** 参数必须具有 *K* 行。

此模块接受包含 *N* 个元素的列向量输入信号。此模块输出一个包含 *K* 个元素的列向量。

解码器尝试使用 **Decoding table** 参数纠正错误。如果 **Decoding table** 为标量 0，则模块默认使用 Communications Toolbox™ 函数 `syndtable` 生成的表。否则，**Decoding table** 必须是 2N-K-by-N 二进制矩阵。此矩阵的第 *r* 行是接收到的二进制码字的纠错向量，该码字的伴随式的十进制整数值为 *r*-1。接收码字的伴随式是该接收码字与奇偶校验矩阵转置的乘积。

有关每个模块端口支持的数据类型的信息，请参阅此页面上的 Supported Data Type 表。
