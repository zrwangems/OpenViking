---
type: simulink-block
title: 'Hamming Encoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Error Detection and Correction / Block Coding / Linear Block Codes'
documentation_page: 'hammingencoder'
documentation_source_path: 'ref/hammingencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Hamming Encoder

## 端口

在 R2025b 中未提供文档。

## 参数

**码字长度 N**
:   码字长度，也是输出向量的长度。

**消息长度 K，或 M 次本原多项式**
:   消息长度（也是输入向量的长度），或表示 GF(2M) 本原多项式的二进制向量，或表示多项式的字符向量。

## 所属库

在 R2025b 中未提供文档。

## 模块特性

在 R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

根据二进制向量数据创建 Hamming 码

Hamming Encoder 模块创建消息长度为 *K*、码字长度为 *N* 的 Hamming 码。数值 *N* 必须采用 2M-1 的形式，其中 *M* 是大于或等于 3 的整数。因此，*K* 等于 *N*-*M*。

此模块接受长度为 *K* 的列向量输入信号。输出信号是长度为 *N* 的列向量。

该编码方案使用有限域 GF(2M) 的元素。您可以指定算法应使用的本原多项式，也可以使用默认设置：

- 要使用默认本原多项式，只需分别将 *N* 和 *K* 作为第一个和第二个对话框参数输入。算法使用 `gfprimdf(M)` 作为 GF(2M) 的本原多项式。
- 要指定本原多项式，请将 *N* 作为第一个参数输入，并将二进制向量作为第二个参数输入。该向量按指数升序列出系数，以此表示本原多项式。您可以使用 Communications Toolbox™ 的 `gfprimfd` 函数创建本原多项式。
- 此外，您可以将本原多项式指定为字符向量，例如 `'D^3 + D + 1'`。

有关每个模块端口支持的数据类型的信息，请参阅本页中的“支持的数据类型”表。
