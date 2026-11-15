---
type: simulink-block
title: 'LDPC Decoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Error Detection and Correction / Block Coding / LDPC Codes'
documentation_page: 'ldpcdecoder'
documentation_source_path: 'ref/ldpcdecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# LDPC Decoder

## 端口

### 输入

### **In** — 对数似然比列向量

对数似然比，指定为 *N*×1 列向量，包含来自解调的软判决输出。*N* 是调制前 LDPC 码字中的比特数。每个元素是接收比特的对数似然比，如果对数似然比为正，则该值更可能为 `0`。前 *K* 个元素对应于输入消息的信息部分。

**数据类型：** `double`
### 输出

### **Out** — 解码数据列向量

解码数据，以列向量形式返回。**判决类型** 参数指定该模块输出硬判决还是软判决（对数似然比）。

- 如果 **输出格式** 参数设置为 `Information part`，则输出仅包含接收码字的信息部分。
- 如果 **输出格式** 参数设置为 `Whole codeword`，则输出包含整个对数似然比向量。

**数据类型：** `double` | `Boolean`

### **Iter** — 已执行的解码迭代次数 正整数

已执行的解码迭代次数，以正整数形式返回。

#### 依赖关系

要启用此端口，请选择 **输出已执行的迭代次数** 参数。

**数据类型：** `double`

### **ParChk** — 最终奇偶校验 列向量

解码输入 LDPC 码后的最终奇偶校验，以 (*N*-*K*)×1 列向量形式返回。*N* 是调制前 LDPC 码字中的比特数。*K* 是未编码消息的长度。

#### 依赖关系

要启用此端口，请选择 **输出最终奇偶校验** 参数。

## 参数

要交互式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上，在 **准备** 库中选择 **属性检查器**。

### **奇偶校验矩阵（稀疏二进制 (N-K)×N 矩阵）** — 奇偶校验矩阵 `ldpcDecoderConfig().ParityCheckMatrix`（默认）| 稀疏二进制矩阵 | 非稀疏索引矩阵

奇偶校验矩阵，指定为稀疏 (*N* – *K*)×*N* 二进制值矩阵。*N* 是接收信号的长度，必须在范围 (0, 231) 内。*K* 是未编码消息的长度，必须小于 *N*。奇偶校验矩阵中的最后 (*N* – *K*) 列必须是阶为 2 的伽罗瓦域 `gf`(2) 中的可逆矩阵。

您还可以将奇偶校验矩阵指定为两列非稀疏索引矩阵 `I`，它定义奇偶校验矩阵中 `1` 的行索引和列索引，使得 `sparse(I(:,1),I(:,2),1)`。

此参数接受数值数据类型。当您将此参数设置为稀疏二进制矩阵时，此参数还接受 `Boolean` 数据类型。

**示例：** `ldpcDecoderConfig().ParityCheckMatrix` 将二进制矩阵配置为 108×648 稀疏逻辑矩阵。

### **输出格式** — 输出值格式 `Information part`（默认）| `Whole codeword`

输出值格式，指定为以下值之一：

- `Information part` — 该模块输出 *K*×1 列向量，仅包含接收对数似然比向量的信息部分。*K* 是未编码消息的长度。
- `Whole codeword` — 该模块输出 *N*×1 列向量，包含整个对数似然比向量。*N* 是接收信号的长度。

  *N* 和 *K* 必须与 (*N*–*K*)×*K* 奇偶校验矩阵的维度一致。

### **判决类型** — 判决方法 `Hard decision`（默认）| `Soft decision`

用于解码的判决方法，指定为以下值之一：

- `Hard decision` — 该模块输出数据类型为 `double` 或 `boolean` 的解码数据。使用 **输出数据类型** 参数指定此数据类型。
- `Soft decision` — 该模块输出数据类型为 `double` 的对数似然比。

### **输出数据类型** — 输出值数据类型 `double`（默认）| `boolean`

输出值数据类型，指定为 `double` 或 `boolean`。

#### 依赖关系

要启用此参数，请将 **判决类型** 参数设置为 `Hard decision`。

### **迭代次数** — 最大解码迭代次数 `50`（默认）| 正整数

最大解码迭代次数，指定为正整数。

### **当所有奇偶校验均满足时停止迭代** — 迭代终止条件 `off`（默认）| `on`

选择此参数可在所有奇偶校验均满足后终止解码。如果并非所有奇偶校验均满足，则解码在 **迭代次数** 参数指定的迭代次数后终止。

### **输出已执行的迭代次数** — 输出已执行的迭代次数 `off`（默认）| `on`

选择此参数以启用 **Iter** 输出端口。

### **输出最终奇偶校验** — 输出已执行的迭代次数 `off`（默认）| `on`

选择此参数以启用 **ParChk** 输出端口。

## 所属库

Communications Toolbox / Error Detection and Correction / Block

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

### R2024b：更改默认奇偶校验矩阵

通过此更新，LDPC Decoder 模块的默认奇偶校验矩阵现在是 `ldpcDecoderConfig().ParityCheckMatrix`，而不是 `dvbs2ldpc(1/2)`。

## 描述

解码二进制低密度奇偶校验（LDPC）码

LDPC Decoder 模块使用置信传播算法解码二进制 LDPC 码，该码以解调后的软判决输出（接收比特的对数似然比）形式输入到模块。该模块解码通用二进制 LDPC 码，其中假设奇偶校验矩阵中没有模式。有关更多信息，请参阅 Belief Propagation Decoding。

输入和输出是离散时间信号。输出采样时间与输入采样时间的比值为：

- 当仅解码码字的信息部分时为 *N/K*
- 当解码整个码字时为 1

*N* 是接收信号的长度，必须在范围 (0, 231) 内。*K* 是未编码消息的长度，必须小于 *N*。

此图标显示 LDPC Decoder 模块的所有端口，包括可选端口。
