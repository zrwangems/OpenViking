---
type: simulink-block
title: 'Binary-Input RS Encoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction / Block'
documentation_page: 'binaryinputrsencoder'
documentation_source_path: 'ref/binaryinputrsencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Binary-Input RS Encoder

## 端口

### 输入

### **In** — 消息二进制列向量

以 bits 表示的消息，指定为以下之一：

- 当没有消息缩短时，为
  (*N*C×*K*×*M*)×1
  二进制列向量。
- 当有消息缩短时，为
  (*N*C×*S*×*M*)×1
  二进制列向量。

*N*C 是消息字的数量，*K* 是 **消息长度 K (symbols)**，*M* 是每个 symbol 的 bits 数，*S* 是 **缩短消息长度 S (symbols)**。

**注意**

解码的消息字数量等于码字数量。

有关详细信息，请参阅 RS 模块中的输入和输出信号长度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `ufix(1)`
### 输出

### **Out** — Reed-Solomon 码字二进制列向量

以 bits 表示的 Reed-Solomon 码字，返回为
(*N*C×(*N*
– *K* + *S* –
*P*)×*M*)×1 二进制列
向量。*N*C 是码字数量，*N* 是 **码字长度 N (symbols)**，*K* 是 **消息长度 K (symbols)**，*S* 是 **缩短消息长度 S (symbols)**，*P* 是每个码字的打孔数量，*M* 是每个 symbol 的 bits 数。

有关详细信息，请参阅 RS 模块中的输入和输出信号长度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `ufix(1)`

有关详细信息，请参阅支持的数据类型。

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上的 **准备** 库中，选择 **属性检查器**。

### **码字长度 N (symbols)** — 码字长度 `7`（默认） | integer

以 symbols 为单位的码字长度，指定为整数。

有关详细信息，请参阅 M 和码字长度 N 的限制以及 RS 模块中的输入和输出信号长度。

### **消息长度 K (symbols)** — 消息字长度 `3`（默认） | integer

以 symbols 为单位的消息字长度，指定为 [1, *N*–2] 范围内的整数，其中 *N* 是码字长度。

### **缩短消息长度 S (symbols)** — 缩短消息字长度 `3`（默认） | integer

以 symbols 为单位的缩短消息字长度，指定为满足 *S* ≤ *K* 的整数。当 **缩短消息长度 S (symbols)** < **消息长度 K (symbols)** 时，Reed-Solomon 码被缩短。

对于全长 (*N*, *K*) 码，仍需指定 *N* 和 *K* 的值，但解码会缩短为 (*N*–*K*+*S*, *S*) 码。

#### 依赖关系

要启用此参数，请选择 **指定缩短消息长度**。

### **生成多项式** — 生成多项式 `rsgenpoly(7, 3, [], [], 'double')`（默认） | polynomial character vector | binary row vector | binary Galois row vector

生成多项式，其值从 0 到 2^M – 1，按降幂顺序，指定为以下之一：

- 多项式字符向量。有关详细信息，请参阅 Communications Toolbox 中的多项式表示。
- 表示生成多项式按降幂顺序排列的系数的整数行向量。
- 表示生成多项式按降幂顺序排列的系数的整数 Galois 行向量。

每个系数都是由本原多项式定义的 Galois 域的一个元素。有关详细信息，请参阅指定生成多项式。

**示例：** `[1 3 1 2 3]`，等效于 `rsgenpoly(7,3)`

#### 依赖关系

要启用此参数，请选择 **指定生成多项式**。

### **本原多项式** — 本原多项式 `'X^3 + X + 1'`（默认） | polynomial character vector | binary row vector

按降幂顺序的本原多项式。此多项式的阶数为 *M*，定义有限 Galois 域 GF(2^M)，该域对应于构成消息字和码字的整数。将本原多项式指定为以下之一：

- 多项式字符向量。有关详细信息，请参阅 Communications Toolbox 中的多项式表示。
- 表示生成多项式系数的二进制行向量。

有关详细信息，请参阅 M 和码字长度 N 的限制。

**示例：** `'X^3 + X + 1'`，这是用于 (7,3) 码的本原多项式，`ppoly = primpoly(3,'nodisplay'); int2bit(ppoly,ceil(log2(max(ppoly))))'`

#### 依赖关系

要启用此参数，请选择 **指定本原多项式**。

### **打孔向量** — 打孔向量 `[ones(2,1); zeros(2,1)]`（默认） | binary column vector

打孔向量，指定为 (*N*–*K*)×1 二进制列向量。元素索引为 `1` 的项表示未经更改通过模块的数据 *symbol* 索引。元素索引为 `0` 的项表示从数据流中被打孔（即移除）的数据 *symbol* 索引。有关详细信息，请参阅打孔和擦除。

#### 依赖关系

要启用此参数，请选择 **打孔编码**。

### **输出数据类型** — 模块的输出类型 `Same as input`（默认） | `boolean` | `double`

模块的输出类型，指定为 `Same as input`、`boolean` 或 `double`。

## 所属库

Communications Toolbox / Error Detection and Correction / Block

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed pointa` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
|  |  |
| --- | --- |
| a 仅 ufix(1)。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

从二进制向量数据创建 Reed-Solomon 码

Binary-Input RS Encoder 模块创建 Reed-Solomon 码。

该码的 symbols 是长度为 *M* 的二进制序列，对应于 Galois 域 *GF*(2^M) 的元素。每个 symbol 中的第一个 bit 是最高有效位。

假设 M = 3，N = 2^3-1 = 7，K = 2。则消息是长度为 2 的向量，其元素是 0 到 7 之间的整数。对应的码字是长度为 7 的向量，其元素是 0 到 7 之间的整数。下图说明了当码字长度 *N*=7 且消息字长度 *K*=2 时，此模块可能的输入和输出信号。由于 *N*=2^M–1，当 *N*=7 时，symbol 长度 *M*=3。

每个输入消息字是长度为 6 的二进制向量，表示 2 个三位整数。每个对应的输出码字是长度为 21 的二进制向量，表示 7 个三位整数。有关详细信息，请参阅 RS 模块中的输入和输出信号长度。
