---
type: simulink-block
title: 'Quantizing Decoder'
family: 'source-coding'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Source Coding'
documentation_page: 'quantizingdecoder'
documentation_source_path: 'ref/quantizingdecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Quantizing Decoder

## 端口

未在 R2025b 中提供文档。

## 参数

**Quantization codebook**
:   一个实数向量，用于指定与输入的每个非负整数对应的输出值。

**Quantized output data type**
:   选择输出数据类型。

## 所属库

未在 R2025b 中提供文档。

## 模块特性

未在 R2025b 中提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

根据码本对量化索引进行解码

Quantizing Decoder 模块将量化索引转换为对应的码本值。**Quantization codebook** 参数是一个长度为 N 的向量，用于指定可能的输出值。如果输入是介于 0 和 N-1 之间的整数 k，则输出为 **Quantization codebook** 的第 (k+1) 个元素。

输入必须是离散时间信号。此模块独立处理每个向量元素。有关每个模块端口支持的数据类型的信息，请参阅本页上的 Supported Data Type 表。

**注意**

Quantizing Encoder 模块也使用 **Quantization codebook** 参数。该模块的第一个输出对应于 Quantizing Decoder 的输入，而该模块的第二个输出对应于 Quantizing Decoder 的输出。
