---
type: simulink-block
title: 'Hamming Decoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction / Block'
documentation_page: 'hammingdecoder'
documentation_source_path: 'ref/hammingdecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Hamming Decoder

## 端口

R2025b 中未记录。

## 参数

**Codeword length N**
:   码字长度 *N*，同时也是输入向量长度。

**Message length K, or M-degree primitive polynomial**
:   消息长度，同时也是输入向量长度，或者一个表示 GF(2M) 本原多项式的二进制向量，或者一个多项式字符向量。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

解码汉明码以恢复二进制向量数据

Hamming Decoder 模块从二进制汉明码码字向量中恢复二进制消息向量。为了正确解码，此模块中的参数值应与对应的 Hamming Encoder 模块中的参数值匹配。

如果汉明码的消息长度为 *K*，码字长度为 *N*，则 *N* 必须具有 2M-1 的形式，其中 *M* 为大于或等于 3 的整数。此外，*K* 必须等于 *N*-*M*。

此模块接受长度为 *N* 的列向量输入信号。输出信号是长度为 *K* 的列向量。

该编码方案使用有限域 GF(2M) 的元素。您可以指定算法应使用的本原多项式，也可以依赖默认设置：

- 要使用默认本原多项式，只需分别输入 *N* 和 *K* 作为第一个和第二个对话框参数。该算法使用 `gfprimdf(M)` 作为 GF(2M) 的本原多项式。
- 要指定本原多项式，请输入 *N* 作为第一个参数，并输入一个二进制向量作为第二个参数。该向量通过按指数升序列出其系数来表示本原多项式。您可以使用 Communications Toolbox™ 的 `gfprimfd` 函数创建本原多项式。
- 此外，您可以将本原多项式指定为字符向量，例如 `'D^3 + D + 1'`。

有关每个模块端口支持的数据类型的信息，请参阅本页上的 Supported Data Type 表。
