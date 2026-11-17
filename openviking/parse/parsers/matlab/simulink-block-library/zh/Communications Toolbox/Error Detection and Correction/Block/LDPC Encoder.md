---
type: simulink-block
title: 'LDPC Encoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction / Block'
documentation_page: 'ldpcencoder'
documentation_source_path: 'ref/ldpcencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# LDPC Encoder

## 端口

### 输入

### **In** — 输入消息二进制列向量

输入消息，指定为包含二值元素的 *K*×1 列向量。*K* 是未编码消息的长度。

**数据类型：** `double` | `Boolean`
### 输出

### **Out** — LDPC 码字列向量

LDPC 码字，以 *N*×1 列向量形式返回。*N* 是 LDPC 码字中的比特数。输出信号的数据类型继承自输入信号。LDPC 码字输出是奇偶校验方程的解。输入消息构成 LDPC 码字输出的前 *K* 个比特，奇偶校验构成剩余的 (*N* – *K*) 个比特。

**数据类型：** `double` | `Boolean`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### **Parity-check matrix (sparse binary (N-K)-by-N matrix)** — 奇偶校验矩阵 `ldpcEncoderConfig().ParityCheckMatrix`（默认）| 稀疏二值矩阵 | 非稀疏索引矩阵

奇偶校验矩阵，指定为稀疏 (*N* – *K*)×*N* 二值矩阵。*N* 是输出 LDPC 码字的长度，必须在范围 (0, 231) 内。*K* 是未编码消息的长度，必须小于 *N*。奇偶校验矩阵中的最后 (*N* – *K*) 列必须是阶为 2 的伽罗瓦域 `gf`(2) 中的可逆矩阵。

您也可以将奇偶校验矩阵指定为两列非稀疏索引矩阵 `I`，它定义奇偶校验矩阵中 `1` 的行索引和列索引，使得 `sparse(I(:,1),I(:,2),1)`。

此参数接受数值数据类型。当您将此参数设置为稀疏二值矩阵时，此参数也接受 `Boolean` 数据类型。

**注意**

- 当奇偶校验矩阵的最后 (*N* – *K*) 列构成三角矩阵时，执行前向或后向代入以求解奇偶校验方程。
- 当奇偶校验矩阵的最后 (*N* – *K*) 列不构成三角矩阵时，执行矩阵求逆以求解奇偶校验方程。如果需要求逆的矩阵很大，初始化或更新会花费更多时间。

**示例：** `ldpcEncoderConfig().ParityCheckMatrix` 将二值矩阵配置为 108×648 稀疏逻辑矩阵。

## 所属库

Communications Toolbox / Error Detection and Correction / Block

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

### R2024b：更改默认奇偶校验矩阵

通过此更新，LDPC Encoder 模块的默认奇偶校验矩阵现在是 `ldpcEncoderConfig().ParityCheckMatrix`，而不是 `dvbs2ldpc(1/2)`。

## 描述

编码二进制低密度奇偶校验（LDPC）码

LDPC Encoder 模块对二进制输入消息应用 LDPC 编码。LDPC 码是具有稀疏奇偶校验矩阵和长块长度的线性差错控制码，其性能可以接近香农限。

输入和输出是离散时间信号。输出采样时间与输入采样时间之比为 *K/N*，其中：

- *N* 是接收信号的长度，必须在范围 (0, 231) 内。
- *K* 是未编码消息的长度，必须小于 *N*。
