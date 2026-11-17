---
type: simulink-block
title: 'Hamming Encoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction / Block'
documentation_page: 'hammingencoder'
documentation_source_path: 'ref/hammingencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Hamming Encoder

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters: []
```

**Codeword length N**
:   码字长度，也是输出向量长度。

**Message length K, or M-degree primitive polynomial**
:   消息长度，也是输入向量长度，或者是一个二进制向量，表示 GF(2M) 的本原多项式，或者是一个多项式字符向量。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

从二进制向量数据创建汉明码

Hamming Encoder 模块创建具有消息长度 *K* 和码字长度 *N* 的汉明码。数字 *N* 必须具有 2M-1 的形式，其中 *M* 是大于或等于 3 的整数。然后 *K* 等于 *N*-*M*。

此模块接受长度为 *K* 的列向量输入信号。输出信号是长度为 *N* 的列向量。

该编码方案使用有限域 GF(2M) 的元素。您可以指定算法应使用的本原多项式，也可以依赖默认设置：

- 要使用默认本原多项式，只需分别输入 *N* 和 *K* 作为第一个和第二个对话框参数。该算法使用 `gfprimdf(M)` 作为 GF(2M) 的本原多项式。
- 要指定本原多项式，请输入 *N* 作为第一个参数，并输入一个二进制向量作为第二个参数。该向量通过按指数升序列出其系数来表示本原多项式。您可以使用 Communications Toolbox™ 的 `gfprimfd` 函数创建本原多项式。
- 此外，您可以将本原多项式指定为字符向量，例如 `'D^3 + D + 1'`。

有关每个模块端口支持的数据类型的信息，请参阅此页面上的 Supported Data Type 表。
