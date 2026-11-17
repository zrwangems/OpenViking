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
```yaml
ports:
- name: In
  summary: 消息二进制列向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | ufix(1)
- name: Out
  summary: Reed-Solomon 码字二进制列向量
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | ufix(1)
```

### 输入

### **In** — 消息二进制列向量

以比特表示的消息，指定为以下之一：

- 当没有消息缩短时，一个
  (*N*C×*K*×*M*)-by-1
  二进制列向量。
- 当有消息缩短时，一个
  (*N*C×*S*×*M*)-by-1
  二进制列向量。

*N*C 是消息字的数量，*K* 是 **Message
length K (symbols)**，*M* 是每个符号的比特数，*S* 是 **Shortened
message length S (symbols)**。

**注意**

解码后的消息字数量等于码字的数量。

有关更多信息，请参阅 Input and Output Signal Length in RS Blocks。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `ufix(1)`
### 输出

### **Out** — Reed-Solomon 码字二进制列向量

以比特表示的 Reed-Solomon 码字，返回为一个
(*N*C×(*N*
– *K* + *S* –
*P*)×*M*)-by-1 二进制列
向量。*N*C 是码字的数量，*N* 是 **Codeword length N
(symbols)**，*K* 是 **Message
length K (symbols)**，*S* 是
**Shortened message length S (symbols)**，
*P* 是每个码字的删余数，*M* 是每个符号的比特数。

有关更多信息，请参阅 Input and Output Signal Length in RS Blocks。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `ufix(1)`

有关更多信息，请参阅 Supported Data Types。
## 参数
```yaml
parameters:
- name: Codeword length N (symbols)
  summary: 码字长度 7（默认）| 整数
  group: ''
- name: Message length K (symbols)
  summary: 消息字长度 3（默认）| 整数
  group: ''
- name: Shortened message length S (symbols)
  summary: 缩短的消息字长度 3（默认）| 整数
  group: ''
- name: Generator polynomial
  summary: 生成多项式 rsgenpoly(7, 3, [], [], 'double')（默认）| 多项式字符向量 | 二进制行向量 | 二进制 Galois 行向量
  group: ''
- name: Primitive polynomial
  summary: 本原多项式 'X^3 + X + 1'（默认）| 多项式字符向量 | 二进制行向量
  group: ''
- name: Puncture vector
  summary: 删余向量 [ones(2,1); zeros(2,1)]（默认）| 二进制列向量
  group: ''
- name: Output data type
  summary: 模块的输出类型 Same as input（默认）| boolean | double
  group: ''
```

要以交互方式编辑模块参数，请使用
Property Inspector。在 Simulink® Toolstrip 中，在 **Simulation** 选项卡上，在
**Prepare** 库中，选择 **Property
Inspector**。

### **Codeword length N (symbols)** — 码字长度 `7`（默认）| 整数

以符号表示的码字长度，指定为整数。

有关更多信息，请参阅 Restrictions on the M and the Codeword Length N 和 Input and Output Signal Length in RS Blocks。

### **Message length K (symbols)** — 消息字长度 `3`（默认）| 整数

以符号表示的消息字长度，指定为范围 [1,
*N*–2] 内的整数，其中 *N* 是码字
长度。

### **Shortened message length S (symbols)** — 缩短的消息字长度 `3`（默认）| 整数

以符号表示的缩短消息字长度，指定为整数，满足
*S* ≤ *K*。当 **Shortened
message length S (symbols)** < **Message length K
(symbols)** 时，Reed-Solomon 码被缩短。

您仍然为全长 (*N*, *K*) 码指定 *N* 和 *K* 值，但
解码被缩短为
(*N*–*K*+*S*,
*S*) 码。

#### 依赖关系

要启用此参数，请选择 **Specify shortened message
length**。

### **Generator polynomial** — 生成多项式 `rsgenpoly(7, 3, [], [], 'double')`（默认）| 多项式字符向量 | 二进制行向量 | 二进制 Galois 行向量

生成多项式，其值从 0 到
2*M*–1，按降幂顺序，指定为以下之一：

- 一个多项式字符向量。有关更多信息，请参阅 Representation of Polynomials in Communications Toolbox。
- 一个整数行向量，按降幂顺序表示生成多项式的系数。
- 一个整数 Galois 行向量，按降幂顺序表示生成多项式的系数。

每个系数是由本原多项式定义的 Galois 域的
元素。有关更多信息，请参阅 Specify the Generator Polynomial。

**示例：** `[1 3 1 2 3]`，等价于
`rsgenpoly(7,3)`

#### 依赖关系

要启用此参数，请选择 **Specify generator
polynomial**。

### **Primitive polynomial** — 本原多项式 `'X^3 + X + 1'`（默认）| 多项式字符向量 | 二进制行向量

按降幂顺序的本原多项式。此多项式为
*M* 阶，并定义有限 Galois 域
GF(2M)，对应于构成消息字和码字的整数。将本原多项式指定为以下之一：

- 一个多项式字符向量。有关更多信息，请参阅 Representation of Polynomials in Communications Toolbox。
- 一个二进制行向量，表示生成多项式的系数。

有关更多信息，请参阅 Restrictions on the M and the Codeword Length N。

**示例：** `'X^3 + X + 1'`，这是用于 (7,3) 码的本原
多项式，`ppoly = primpoly(3,'nodisplay');
int2bit(ppoly,ceil(log2(max(ppoly))))'`

#### 依赖关系

要启用此参数，请选择 **Specify primitive
polynomial**。

### **Puncture vector** — 删余向量 `[ones(2,1); zeros(2,1)]`（默认）| 二进制列向量

删余向量，指定为一个
(*N*–*K*)-by-1 二进制列向量。
元素索引为 `1` 的位置表示通过该模块
原样传递的数据
*符号* 索引。元素索引为 `0` 的位置表示从数据流中被删余或移除的数据
*符号* 索引。有关更多信息，请参阅 Puncturing and Erasures。

#### 依赖关系

要启用此参数，请选择 **Puncture
code**。

### **Output data type** — 模块的输出类型 `Same as input`（默认）| `boolean` | `double`

模块的输出类型，指定为 `Same as
input`、`boolean` 或
`double`。
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

Binary-Input RS Encoder 模块创建一个 Reed-Solomon 码。

该码的符号是长度为 *M* 的二进制序列，
对应于 Galois 域
*GF*(2*M*) 的元素。每个符号中的
第一个比特是最高有效位。

假设 M = 3，N = 23-1 = 7，K = 2。那么消息是一个
长度为 2 的向量，其元素是 0 到 7 之间的整数。相应的码字
是一个长度为 7 的向量，其元素是 0 到 7 之间的整数。下图
说明了当码字长度
*N*=7 且消息字长度 *K*=2 时该模块可能的输入和输出信号。由于
*N*=2*M*–1，当
*N*=7 时，符号长度 *M*=3。

每个输入消息字是一个长度为 6 的二进制向量，表示 2 个三位
整数。每个相应的输出码字是一个长度为 21 的二进制向量，表示 7 个三位整数。有关更多信息，请参阅 Input and Output Signal Length in RS Blocks。
