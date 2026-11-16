---
type: simulink-block
title: 'Differential Encoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Source Coding'
documentation_page: 'differentialencoder'
documentation_source_path: 'ref/differentialencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Differential Encoder

## 端口

R2025b 中未提供文档。

## 参数

**初始条件**
:   该值与初始输入值进行逻辑异或，形成初始输出值。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

使用差分编码对二进制信号进行编码

Differential Encoder 模块对信道中的二进制输入信号进行编码。输出是当前输入元素与前一输出元素的逻辑差。更具体地说，输入和输出之间的关系为：

d(i0) = m(i0) XOR
**初始条件**参数值

d(ik) = d(ik-1) XOR
m(ik)

其中：

- m 是输入消息。
- d 是差分编码后的输出。
- ik 是第 k 个元素。
- XOR 是逻辑异或运算符。

此模块接受标量或列向量输入信号，并将各列视为信道。
