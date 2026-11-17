---
type: simulink-block
title: 'Sphere Decoder'
family: 'comm'
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
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters: []
```

**Signal constellation**
:   指定比特所映射到的信号星座中的点数。
    该值必须为复数列向量。向量的长度必须为 2 的幂。
    该模块对每个发射天线使用相同的星座。默认设置为平均功率为 1 的 QPSK
    星座。

**Bit mapping per constellation point**
:   指定该模块对每个星座点使用的比特映射。该值必须
    为数值矩阵。矩阵大小必须为 [ConstellationLength bitsPerSymbol]，其中
    ConstellationLength 表示 **Signal constellation**
    参数值的长度，bitsPerSymbol 表示每个符号编码的比特数。
    默认矩阵大小为 [0 0; 0 1; 1 0; 1 1]，与
    **Signal constellation** 属性的默认值匹配。

**Initial search radius**
:   将解码算法的初始搜索半径指定为
    `Infinity` 或 `ZF solution`。

    当您选择 `Infinity` 时，该模块将初始搜索
    半径设置为 Inf。当您选择 `ZF solution` 时，该模块将
    初始搜索半径设置为迫零解。迫零解在解码时通过
    输入信道的伪逆计算得出。较大的星座和/或天线
    数量可以从搜索半径的初始缩减中受益。但在大多数情况下，
    `ZF Solution` 的额外计算不会带来好处。

**Decision method**
:   将解码判决方法指定为 `Soft` 或
    `Hard`。当您选择 `Soft` 时，该模块
    输出对数似然比（LLR），即软比特。当您设置为
    `Hard` 时，该模块将软 LLR 转换为比特。硬判决
    输出逻辑数组遵循以下映射：负 LLR 为 `0`，
    所有其他值为 `1`。

**使用仿真**
:   指定该模块是使用 `Code generation` 还是
    `Interpreted execution` 进行仿真。默认值为 `Interpreted
    execution`。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

## 描述

使用球译码器解码输入

该模块使用球译码算法解码通过 `Nt` 个天线发送的符号。

### 数据类型

有关每个模块端口支持的数据类型的信息，请参阅本页上的 Supported Data Type 表。输出信号从
输入继承数据类型。

### 算法

该模块实现 `comm.SphereDecoder`
System object™ 模块参考页面上描述的算法、输入和输出。对象属性对应于模块参数。
