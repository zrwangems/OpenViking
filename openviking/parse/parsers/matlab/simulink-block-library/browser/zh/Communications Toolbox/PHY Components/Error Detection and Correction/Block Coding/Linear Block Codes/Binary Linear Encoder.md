---
type: simulink-block
title: 'Binary Linear Encoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Error Detection and Correction / Block Coding / Linear Block Codes'
documentation_page: 'binarylinearencoder'
documentation_source_path: 'ref/binarylinearencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Binary Linear Encoder

## 端口

在 R2025b 中未记录。

## 参数

**生成矩阵**
:   一个 *K* 行 *N* 列的矩阵，其中
    *K* 是消息长度，*N* 是码字长度。

## 所属库

在 R2025b 中未记录。

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

根据二进制向量数据创建线性分组码

Binary Linear Encoder 模块使用您指定的生成矩阵创建二进制线性分组码。如果 *K* 是码的消息长度，则**生成矩阵**参数必须有 *K* 行。如果 *N* 是码的码字长度，则**生成矩阵**必须有 *N* 列。

此模块接受包含 *K* 个元素的列向量输入信号。此模块输出一个包含 *N* 个元素的列向量。有关每个模块端口支持的数据类型的信息，请参阅“支持的数据类型”。
