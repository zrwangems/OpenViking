---
type: simulink-block
title: 'Hamming Decoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Error Detection and Correction / Block Coding / Linear Block Codes'
documentation_page: 'hammingdecoder'
documentation_source_path: 'ref/hammingdecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Hamming Decoder

## 端口

R2025b 中未提供文档。

## 参数

**码字长度 N**
:   码字长度 *N*，同时也是输入向量的长度。

**消息长度 K，或 M 次本原多项式**
:   消息长度，同时也是输入向量长度；或者是一个二进制向量，用于表示
    GF(2M) 的本原多项式；或者是一个多项式字符向量。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

对汉明码进行解码以恢复二进制向量数据

Hamming Decoder 模块从二进制汉明码字向量中恢复二进制消息向量。为了正确解码，此模块中的参数值应与相应 Hamming Encoder 模块中的参数值一致。

如果汉明码的消息长度为 *K*，码字长度为 *N*，则对于某个大于或等于 3 的整数 *M*，*N* 必须具有 2M-1 的形式。此外，*K* 必须等于 *N*-*M*。

此模块接受长度为 *N* 的列向量输入信号。输出信号是长度为 *K* 的列向量。

该编码方案使用有限域 GF(2M) 的元素。您可以指定算法应使用的本原多项式，也可以采用默认设置：

- 要使用默认本原多项式，只需分别输入 *N* 和 *K* 作为第一个和第二个对话框参数。算法使用 `gfprimdf(M)` 作为 GF(2M) 的本原多项式。
- 要指定本原多项式，请输入 *N* 作为第一个参数，并输入一个二进制向量作为第二个参数。该向量通过按指数升序列出本原多项式的系数来表示该多项式。您可以使用 Communications Toolbox™ 的 `gfprimfd` 函数创建本原多项式。
- 此外，您还可以将本原多项式指定为字符向量，例如 `'D^3 + D + 1'`。

有关每个模块端口支持的数据类型的信息，请参阅本页中的“支持的数据类型”表。
