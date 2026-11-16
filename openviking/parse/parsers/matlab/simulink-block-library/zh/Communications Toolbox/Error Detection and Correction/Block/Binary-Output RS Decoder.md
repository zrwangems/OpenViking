---
type: simulink-block
title: 'Binary-Output RS Decoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction / Block'
documentation_page: 'binaryoutputrsdecoder'
documentation_source_path: 'ref/binaryoutputrsdecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Binary-Output RS Decoder

## 端口

### 输入

### **In** — Reed-Solomon 码字二进制列向量

以 bits 表示的 Reed-Solomon 码字，指定为一个
(*N*C×(*N*
– *K* + *S* –
*P*)×*M*)-by-1 二进制列
向量。*N*C 是
码字数量，*N* 是 **Codeword length N
(symbols)**，*K* 是 **Message
length K (symbols)**，*S* 是
**Shortened message length S (symbols)**，
*P* 是每个码字的打孔数量，并且
*M* 是每个 symbol 的 bits 数量。

有关详细信息，请参阅 RS 模块中的输入和输出信号长度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `ufix(1)`

### **Era** — 擦除向量二进制列向量

以 symbols 为单位的擦除向量，指定为一个
(*N*C×(*N*
– *K* + *S* –
*P*))-by-1 二进制列向量。
*N*C 是
码字数量，*N* 是 **Codeword length N
(symbols)**，*K* 是 **Message
length K (symbols)**，*S* 是
**Shortened message length S (symbols)**，
*P* 是每个码字的打孔数量，并且
*M* 是每个 symbol 的 bits 数量。

擦除值 1 对应于码字中相同位置的已擦除 bits。值 0 对应于未擦除的 bits。有关
详细信息，请参阅打孔与擦除。

#### 依赖关系

要启用此端口，请选择 **Enable erasures input
port**。

**数据类型：** `double` | `Boolean`
### 输出

### **Out** — 解码消息二进制列向量

以 bits 表示的解码消息，返回为以下之一：

- 当没有消息缩短时，为一个
  (*N*C×*K*×*M*)-by-1
  二进制列向量。
- 当有消息缩短时，为一个
  (*N*C×*S*×*M*)-by-1
  二进制列向量。

*N*C 是
消息字数量，*K* 是 **Message
length K (symbols)**，*M* 是每个
symbol 的 bits 数量，并且 *S* 是 **Shortened
message length S (symbols)**。

**注意**

解码后的消息字数量等于码字数量。

有关详细信息，请参阅 RS 模块中的输入和输出信号长度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `ufix(1)`

### **Err** — 解码错误 integer 向量

符号解码错误，返回为具有
*N*C 个元素的 integer 向量，其中
*N*C 是
码字数量。此端口指示在解码每个码字期间检测到的符号错误数量。负整数表示
模块检测到的错误数量超过了使用指定编码方案所能纠正的错误数量。

**注意**

一个 (*N*,*K*) Reed-Solomon 码
最多可以在每个码字中纠正 `floor((N-K)/2)` 个符号错误
（不是 bit 错误）。当接收到的码字包含
超过 (*N*-*K*)/2 个符号
错误时，会发生解码失败。

#### 依赖关系

要启用此端口，请选择 **Output number of corrected
symbol errors**。

**数据类型：** `double`

有关详细信息，请参阅支持的数据类型。

## 参数

要以交互方式编辑模块参数，请使用
Property Inspector。在 Simulink® Toolstrip 中，在 **Simulation** 选项卡上的
**Prepare** 库中，选择 **Property
Inspector**。

### **Codeword length N (symbols)** — 码字长度 `7`（默认）| integer

以 symbols 为单位的码字长度，指定为 integer。

有关详细信息，请参阅 M 和码字长度 N 的限制以及 RS 模块中的输入和输出信号长度。

### **Message length K (symbols)** — 消息字长度 `3`（默认）| integer

以 symbols 为单位的消息字长度，指定为范围 [1,
*N*–2] 中的 integer，其中 *N* 是码字
长度。

### **Shortened message length S (symbols)** — 缩短消息字长度 `3`（默认）| integer

以 symbols 为单位的缩短消息字长度，指定为 integer，使得
*S* ≤ *K*。当 **Shortened
message length S (symbols)** < **Message length K
(symbols)** 时，Reed-Solomon 码被缩短。

仍然为
全长度 (*N*, *K*) 码指定 *N* 和 *K* 值，但
解码会缩短为
(*N*–*K*+*S*,
*S*) 码。

#### 依赖关系

要启用此参数，请选择 **Specify shortened message
length**。

### **Generator polynomial** — 生成多项式 `rsgenpoly(7, 3, [], [], 'double')`（默认）| polynomial character vector | binary row vector | binary Galois row vector

生成多项式，其值从 0 到
2*M*–1，按
降幂顺序，指定为以下之一：

- 多项式字符向量。有关详细信息，请参阅 Communications Toolbox 中的多项式表示。
- 一个 integer 行向量，按降幂顺序表示
  生成多项式的系数。
- 一个 integer Galois 行向量，按降幂顺序表示
  生成多项式的系数。

每个系数是由
primitive polynomial 定义的 Galois 域的一个元素。有关详细信息，请参阅指定生成多项式。

**示例：** `[1 3 1 2 3]`，等效于
`rsgenpoly(7,3)`

#### 依赖关系

要启用此参数，请选择 **Specify generator
polynomial**。

### **Primitive polynomial** — 本原多项式 `'X^3 + X + 1'`（默认）| polynomial character vector | binary row vector

按降幂顺序的 primitive polynomial。此多项式的
阶数为 *M*，并定义与
形成消息字和码字的整数相对应的有限 Galois 域
GF(2M)。将 primitive polynomial 指定为以下
之一：

- 多项式字符向量。有关详细信息，请参阅 Communications Toolbox 中的多项式表示。
- 一个二进制行向量，表示
  生成多项式的系数。

有关详细信息，请参阅 M 和码字长度 N 的限制。

**示例：** `'X^3 + X + 1'`，这是用于 (7,3) 码的 primitive
polynomial，`ppoly = primpoly(3,'nodisplay');
int2bit(ppoly,ceil(log2(max(ppoly))))'`

#### 依赖关系

要启用此参数，请选择 **Specify primitive
polynomial**。

### **Puncture vector** — 打孔向量 `[ones(2,1); zeros(2,1)]`（默认）| binary column vector

打孔向量，指定为一个
(*N*–*K*)-by-1 二进制列向量。
带有 `1` 的元素索引表示未经更改
通过模块的数据 *symbol* 索引。带有 `0` 的元素索引表示
从数据流中被打孔（即移除）的数据
*symbol* 索引。有关详细信息，请参阅打孔与擦除。

#### 依赖关系

要启用此参数，请选择 **Punctured
code**。

### **Enable erasures input port** — 启用擦除输入端口 off（默认）| on

选中此复选框会启用擦除端口
**Era**。有关详细信息，请参阅打孔与擦除。

### **Output number of corrected symbol errors** — 启用端口以输出已纠正符号错误数量 off（默认）| on

选中此复选框会启用一个附加输出端口
**Err**，它指示模块在输入码字中纠正的符号错误数量。

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

解码 Reed-Solomon 码以恢复二进制向量数据

Binary-Output RS Decoder 模块从二进制 Reed-Solomon 码字向量中
恢复二进制消息向量。为正确解码，此模块中的参数值
必须与对应的 Binary-Input RS Encoder 模块中的参数值匹配。

该码的 symbols 是长度为 *M* 的二进制序列，
对应于 Galois 域
*GF*(2*M*) 的元素。每个
symbol 中的第一个 bit 是最高有效位。

此图显示了码字长度
*N*=7 和消息字长度 *K*=2 时解码器的输入-输出字长度。由于
*N*=2*M*–1，当
*N*=7 时，symbol 长度 *M*=3。

每个输入码字是长度为 21 的二进制向量，表示 7 个三 bit
整数。每个对应的输出消息字是长度为 6 的二进制向量，
表示 2 个三 bit 整数。有关详细信息，请参阅 RS 模块中的输入和输出信号长度。

此图标显示了所有端口，包括可选端口：
