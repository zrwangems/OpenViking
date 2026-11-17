---
type: simulink-block
title: 'Binary Cyclic Decoder'
family: 'error-detection-and-correction'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction / Block'
documentation_page: 'binarycyclicdecoder'
documentation_source_path: 'ref/binarycyclicdecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Binary Cyclic Decoder

## 端口

R2025b 中未提供文档。

## 参数

**码字长度 N**
:   码字长度 *N*，同时也是输入向量的长度。

**消息长度 K，或生成多项式**
:   可以是消息长度（同时也是输入向量长度）、多项式字符向量，也可以是表示该码生成多项式的二进制向量。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

对系统循环码进行解码以恢复二进制向量数据

Binary Cyclic Decoder 模块从二进制系统循环码的码字向量中恢复消息向量。为实现正确解码，此模块中的参数值应与相应的 Binary Cyclic Encoder 模块中的参数值相匹配。

此模块接受包含 *N* 个元素的列向量输入信号，其中 *N* 为码字长度。输出信号为包含 *K* 个元素的列向量，其中 *K* 为循环码的消息长度。

可以通过以下两种方式之一确定系统循环编码方案：

- 要创建 [N,K] 码，请分别输入 *N* 和 *K* 作为第一个和第二个对话框参数。该模块会计算适当的生成多项式，即
  `cyclpoly(N,K,'min')`。
- 要创建码字长度为 N 且使用特定 (N-K) 次二进制 *生成多项式* 的码，请将 *N* 作为第一个参数输入，并将多项式字符向量或二进制向量作为第二个参数输入。该向量按指数升序列出其系数，以此来表示生成多项式。可以使用 Communications Toolbox™ 的
  `cyclpoly` 函数创建循环生成多项式。

有关各模块端口支持的数据类型的信息，请参阅本页中的“支持的数据类型”表。
