---
type: simulink-block
title: 'Quantizing Decoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Source Coding'
documentation_page: 'quantizingdecoder'
documentation_source_path: 'ref/quantizingdecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Quantizing Decoder

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters: []
```

**Quantization codebook**
:   一个实数向量，指定与输入的每个非负整数对应的输出值。

**量化输出数据类型**
:   选择输出数据类型。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

根据码本对量化索引进行解码

Quantizing Decoder 模块将量化索引转换为对应的码本值。**Quantization codebook** 参数是一个长度为 N 的向量，指定了可能的输出值。如果输入是 0 到 N-1 之间的整数 k，则输出是 **Quantization codebook** 的第 (k+1) 个元素。

输入必须是离散时间信号。该模块独立处理每个向量元素。有关每个模块端口支持的数据类型的信息，请参阅本页的“支持的数据类型”表。

**注意**

Quantizing Encoder 模块也使用 **Quantization codebook** 参数。该模块的第一个输出对应于 Quantizing Decoder 的输入，而该模块的第二个输出对应于 Quantizing Decoder 的输出。
