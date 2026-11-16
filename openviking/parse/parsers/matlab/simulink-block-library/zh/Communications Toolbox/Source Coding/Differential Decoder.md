---
type: simulink-block
title: 'Differential Decoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Source Coding'
documentation_page: 'differentialdecoder'
documentation_source_path: 'ref/differentialdecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Differential Decoder

## 端口

在 R2025b 中未提供文档。

## 参数

**初始条件**
:   该值与初始输入值进行逻辑异或，形成初始输出值。

## 所属库

在 R2025b 中未提供文档。

## 模块特性

在 R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用差分编码对二进制信号进行解码

Differential Decoder 模块对二进制输入信号进行解码。输出是通道内连续输入元素之间的逻辑差。更具体地说，模块的输入和输出关系如下：

m(i0) = d(i0) XOR
**初始条件**参数值

m(ik) = d(ik) XOR
d(ik-1)

其中：

- d 是经过差分编码的输入。
- m 是输出消息。
- ik 是第 k 个元素。
- XOR 是逻辑异或运算符。

此模块接受标量、列向量或矩阵输入信号，并将列视为通道。
