---
type: simulink-block
title: 'Binary Cyclic Encoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction / Block'
documentation_page: 'binarycyclicencoder'
documentation_source_path: 'ref/binarycyclicencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Binary Cyclic Encoder

## 端口

R2025b 中未记录。

## 参数

**Codeword length N**
:   码字长度，也是输出向量长度。

**Message length K, or generator polynomial**
:   消息长度，也是输入向量长度，可以是多项式字符向量，或表示该码的生成多项式的二进制向量。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

从二进制向量数据创建系统循环码

Binary Cyclic Encoder 模块创建消息长度为 *K*、码字长度为 *N* 的系统循环码。

该模块接受包含 *K* 个元素的列向量输入信号。输出信号是包含 *N* 个元素的列向量。

您可以通过以下两种方式之一确定系统循环编码方案：

- 要创建 [N,K] 码，请分别将 N 和 K 作为第一个和第二个对话框参数输入。该模块会计算适当的生成多项式，即 `cyclpoly(N,K,'min')`。
- 要创建码字长度为 *N* 且具有特定次数为 (N-K) 的二进制*生成多项式*的码，请将 *N* 作为第一个参数输入，并将多项式字符向量或二进制向量作为第二个参数输入。该向量通过按指数升序列出其系数来表示生成多项式。您可以使用 Communications Toolbox™ 的 `cyclpoly` 函数创建循环生成多项式。

有关每个模块端口支持的数据类型的信息，请参阅本页上的 Supported Data Type 表。
