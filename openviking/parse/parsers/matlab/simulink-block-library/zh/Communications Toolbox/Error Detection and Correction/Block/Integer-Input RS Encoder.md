---
type: simulink-block
title: 'Integer-Input RS Encoder'
family: 'error-detection-and-correction'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction / Block'
documentation_page: 'integerinputrsencoder'
documentation_source_path: 'ref/integerinputrsencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Integer-Input RS Encoder

## 端口

### 输入

### **In** — 消息整数列向量

消息，指定为以下之一：

- 当没有消息缩短时，为 (*N*C×*K*)×1 整数列向量。
- 当存在消息缩短时，为 (*N*C×*S*)×1 整数列向量。

*N*C 是消息字数，*K* 是 **消息长度 K**，*S* 是 **缩短消息长度 S**。

**注意**

解码后的消息字数等于码字数。

有关详细信息，请参阅 RS 模块中的输入和输出信号长度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### 输出

### **Out** — Reed-Solomon 码字整数列向量

Reed-Solomon 码字，返回为 (*N*C×(*N* – *K* + *S* – *P*)×1 整数列向量。
*N*C 是码字数，*N* 是 **码字长度 N**，*K* 是 **消息长度 K**，*S* 是 **缩短消息长度 S**，*P* 是每个码字的删余数。

有关详细信息，请参阅 RS 模块中的输入和输出信号长度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

有关详细信息，请参阅支持的数据类型。

## 参数

要交互式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 中，在 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### **码字长度 N** — 码字长度 `7`（默认）| integer

码字长度，指定为整数。

有关详细信息，请参阅对 M 和码字长度 N 的限制以及 RS 模块中的输入和输出信号长度。

### **消息长度 K** — 消息字长度 `3`（默认）| integer

消息字长度，指定为范围 [1, *N*–2] 内的整数，其中 *N* 是码字长度。

### **缩短消息长度 S** — 缩短消息字长度 `3`（默认）| integer

缩短消息字长度，指定为整数，使得 *S* ≤ *K*。当 **缩短消息长度 S** < **消息长度 K** 时，Reed-Solomon 码被缩短。

你仍然为全长 (*N*, *K*) 码指定 *N* 和 *K* 值，但解码缩短为 (*N*–*K*+*S*, *S*) 码。

#### 依赖关系

要启用此参数，请选择 **指定缩短消息长度**。

### **生成多项式** — 生成多项式 `rsgenpoly(7, 3, [], [], 'double')`（默认）| polynomial character vector | binary row vector | binary Galois row vector

生成多项式，其值在范围 [0 到 2*M*–1] 内，按降幂顺序排列，指定为以下之一：

- 多项式字符向量。有关详细信息，请参阅 Communications Toolbox 中多项式的表示。
- 整数行向量，按降幂顺序表示生成多项式的系数。
- 整数 Galois 行向量，按降幂顺序表示生成多项式的系数。

每个系数是由本原多项式定义的 Galois 域中的一个元素。有关详细信息，请参阅指定生成多项式。

**示例：** `[1 3 1 2 3]`，等效于 `rsgenpoly(7,3)`

#### 依赖关系

要启用此参数，请选择 **指定生成多项式**。

### **本原多项式** — 本原多项式 `'X^3 + X + 1'`（默认）| polynomial character vector | binary row vector

本原多项式，按降幂顺序排列。此多项式为 *M* 阶，并定义与构成消息字和码字的整数相对应的有限 Galois 域 GF(2M)。将本原多项式指定为以下之一：

- 多项式字符向量。有关详细信息，请参阅 Communications Toolbox 中多项式的表示。
- 二进制行向量，表示生成多项式的系数。

有关详细信息，请参阅指定本原多项式。

**示例：** `'X^3 + X + 1'`，这是用于 (7,3) 码的本原多项式，`ppoly = primpoly(3,'nodisplay'); int2bit(ppoly,ceil(log2(max(ppoly))))'`

#### 依赖关系

要启用此参数，请选择 **指定本原多项式**。

### **删余向量** — 删余向量 `[ones(2,1); zeros(2,1)]`（默认）| binary column vector

删余向量，指定为 (*N*–*K*)×1 二进制列向量。元素索引为 `1` 的位置表示未经更改通过模块的数据*符号*索引。元素索引为 `0` 的位置表示从数据流中被删余或移除的数据*符号*索引。有关详细信息，请参阅删余和擦除。

**注意**

如果编码器每帧处理多个码字，则相同的删余模式适用于所有码字。

#### 依赖关系

要启用此参数，请选择 **删余码**。

## 所属库

Communications Toolbox / Error Detection and Correction / Block

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

从整数向量数据创建 Reed-Solomon 码

Integer-Input RS Encoder 模块创建 Reed-Solomon 码。

该码的符号是 0 到 2*M*-1 之间的整数，表示有限域 *GF*(2*M*) 的元素。*M* 的默认值是大于或等于 log2(*N*+1) 的最小整数，即 `ceil(log2(N+1))`。你可以通过为 *GF*(2*M*) 指定本原多项式来更改 *M* 的默认值，如下面的指定本原多项式所述。对 *M* 和 *N* 的限制在“对 M 和码字长度 N 的限制”中描述。

输入和输出是分别表示消息和码字的整数值信号。有关详细信息，请参阅 RS 模块中的输入和输出信号长度。

一个 (*N*, *K*) Reed-Solomon 码最多可以纠正每个码字中的 `floor((N-K)/2)` 个符号错误（不是位错误）。

假设 M = 3, N = 23-1 = 7, K = 5。那么消息是长度为 5 的向量，其元素是 0 到 7 之间的整数。对应的码字是长度为 7 的向量，其元素是 0 到 7 之间的整数。下图说明了当 **码字长度 N** 设置为 `7`、**消息长度 K** 设置为 `5`，并使用默认本原多项式和生成多项式时，此模块可能的输入和输出信号。
