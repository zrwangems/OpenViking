---
type: simulink-block
title: 'Binary Linear Encoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction / Block'
documentation_page: 'binarylinearencoder'
documentation_source_path: 'ref/binarylinearencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Binary Linear Encoder

## 端口

R2025b 中未记录。

## 参数

**Generator matrix**
:   一个 *K*×*N* 矩阵，其中
    *K* 是消息长度，*N* 是
    码字长度。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

从二进制向量数据创建线性分组码

Binary Linear Encoder 模块使用您指定的生成矩阵创建二进制线性分组码。如果 *K* 是该码的消息长度，则 **Generator matrix** 参数必须具有 *K* 行。如果 *N* 是该码的码字长度，则 **Generator matrix** 必须具有 *N* 列。

此模块接受包含 *K* 个元素的列向量输入信号。此模块输出长度为 *N* 个元素的列向量。有关每个模块端口支持的数据类型的信息，请参阅 Supported Data Type。
