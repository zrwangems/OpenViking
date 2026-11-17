---
type: simulink-block
title: 'Binary Cyclic Decoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction / Block'
documentation_page: 'binarycyclicdecoder'
documentation_source_path: 'ref/binarycyclicdecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Binary Cyclic Decoder

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
:   码字长度 *N*，同时也是输入向量长度。

**Message length K, or generator polynomial**
:   消息长度（同时也是输入向量长度）、多项式字符向量，或表示该码生成多项式的二进制向量。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

将系统循环码解码以恢复二进制向量数据

Binary Cyclic Decoder 模块从二进制系统循环码的码字向量中恢复消息向量。为正确解码，此模块中的参数值应与对应的 Binary Cyclic Encoder 模块中的参数值匹配。

此模块接受包含 *N* 个元素的列向量输入信号，其中 *N* 是码字长度。输出信号是包含 *K* 个元素的列向量，其中 *K* 是循环码的消息长度。

您可以通过以下两种方式之一确定系统循环编码方案：

- 要创建 [N,K] 码，请分别输入 *N* 和 *K* 作为第一个和第二个对话框参数。该模块会计算适当的生成多项式，即 `cyclpoly(N,K,'min')`。
- 要创建码字长度为 N 且具有特定 (N-K) 次二进制*生成多项式*的码，请输入 *N* 作为第一个参数，并输入多项式字符向量或二进制向量作为第二个参数。该向量通过按指数升序列出系数来表示生成多项式。您可以使用 Communications Toolbox™ 的 `cyclpoly` 函数创建循环生成多项式。

有关每个模块端口支持的数据类型的信息，请参阅本页的 Supported Data Type 表。
