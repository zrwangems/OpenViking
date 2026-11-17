---
type: simulink-block
title: 'Sphere Decoder'
family: 'mimo'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'MIMO'
documentation_page: 'spheredecoder'
documentation_source_path: 'ref/spheredecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Sphere Decoder

## 端口

R2025b 中未记录。

## 参数

**信号星座图**
:   指定比特所映射到的信号星座图中的点数。此值必须为复数列向量。向量的长度必须为 2 的幂。
    模块对每个发射天线使用相同的星座图。默认设置为平均功率为 1 的 QPSK 星座图。

**每个星座点的比特映射**
:   指定模块对每个星座点使用的比特映射。此值必须为数值矩阵。矩阵大小必须为 [ConstellationLength bitsPerSymbol]，其中
    ConstellationLength 表示 **信号星座图** 参数值的长度，bitsPerSymbol 表示每个符号编码的比特数。
    默认矩阵为 [0 0; 0 1; 1 0; 1 1]，与 **信号星座图** 属性的默认值相匹配。

**初始搜索半径**
:   将解码算法的初始搜索半径指定为 `Infinity` 或 `ZF solution`。

    选择 `Infinity` 时，模块将初始搜索半径设置为 Inf。选择 `ZF solution` 时，模块将初始搜索半径设置为迫零解。
    解码时，通过输入信道的伪逆计算迫零解。对于大型星座图和/或大量天线，初始减小搜索半径可能带来益处。
    但在大多数情况下，`ZF Solution` 的额外计算并不会带来益处。

**判决方法**
:   将解码判决方法指定为 `Soft` 或 `Hard`。选择 `Soft` 时，模块输出对数似然比 (LLRs)，即软比特。
    选择 `Hard` 时，模块将软 LLR 转换为比特。硬判决输出的逻辑数组遵循以下映射：负 LLR 映射为 `0`，所有其他值映射为 `1`。

**仿真方式**
:   指定模块使用 `Code generation` 还是 `Interpreted execution` 进行仿真。默认值为 `Interpreted execution`。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

## 描述

使用球形解码器对输入进行解码

此模块使用球形解码算法对通过 `Nt` 根天线发送的符号进行解码。

### 数据类型

有关每个模块端口支持的数据类型的信息，请参阅本页上的“支持的数据类型”表。输出信号继承输入的数据类型。

### 算法

此模块实现 `comm.SphereDecoder` System object™ 模块参考页面上所述的算法、输入和输出。对象属性与模块参数相对应。
