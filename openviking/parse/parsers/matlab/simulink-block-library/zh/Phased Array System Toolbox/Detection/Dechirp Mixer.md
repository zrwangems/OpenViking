---
type: simulink-block
title: 'Dechirp Mixer'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Detection'
documentation_page: 'dechirpmixer'
documentation_source_path: 'ref/dechirpmixer.html'
language: zh-CN
chinese_source: worker-translation
---

# Dechirp Mixer

## 端口

### 输入

### **RefX** — 参考信号，复数值 *M*×1 向量

参考信号，指定为复数值 *M*×1 向量。

**数据类型：** `single` | `double`
**复数支持：** 是

### **X** — 输入信号，复数值 *M*×*N* 矩阵

输入信号，指定为复数值 *M*×*N* 矩阵。`X` 的每一列都是一个独立信号，并分别与输入到 `RefX` 端口的信号进行混频。

**数据类型：** `single` | `double`
**复数支持：** 是
### 输出

### **Port\_1** — 去啁啾后的输出信号，*M*×*N* 矩阵

去啁啾后的信号，以 *M*×*N* 矩阵形式返回。`Port_1` 端口的每一列都是 `X` 对应列的混频输出。

**数据类型：** `single` | `double`
**复数支持：** 是

## 参数

R2025b 中未提供文档。

## 所属库

Phased Array System Toolbox / Detection

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

不支持可变大小的输入。

## 版本历史

**在 R2014b 中引入**

## 描述

对输入信号执行去啁啾运算

Dechirp 模块将来自 `X` 端口的输入信号与通过 `RefX` 端口输入的参考信号进行混频。这些信号可以是复基带信号。输入信号可以是矩阵，其中每一列都是一个独立通道。参考信号为向量。先对参考信号取复共轭，然后将其与每个信号列相乘，以计算输出。
