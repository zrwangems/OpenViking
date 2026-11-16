---
type: simulink-block
title: 'BCH Encoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction / Block'
documentation_page: 'bchencoder'
documentation_source_path: 'ref/bchencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# BCH Encoder

## 端口

### 输入

### **In** — 要编码的消息，二进制列向量

要编码的消息，指定为二进制列向量输入信号，其元素数为 **消息长度，K** 的整数倍；如果码被缩短，则为 **缩短的消息长度，S** 的整数倍。每组输入元素表示一个要编码的消息字。输入和输出信号长度在 BCH 模块中的输入和输出信号长度中列出。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### 输出

### **Out** — 编码后的消息，二进制列向量

编码后的消息，以二进制列向量形式返回。编码后的消息是消息长度为 *K*、码字长度为（*N* – 打孔数）的 BCH 码。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

有关详细信息，请参阅支持的数据类型。

## 参数

要交互式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上，在 **准备** 库中选择 **属性检查器**。

### **码字长度，N** — 码字长度 `15`（默认） | integer

码字长度，指定为 *N* = 2*M*–1 形式的整数，其中 *M* 是 3 到 16 的整数。有关详细信息，请参阅提示。

### **消息长度，K** — 消息长度 `5`（默认） | integer

消息长度，指定为整数。(`N`, `K`) 对必须生成狭义 BCH 码。

### **缩短的消息长度，S** — 缩短的消息长度 `5`（默认） | integer

缩短的消息长度，指定为整数。指定此参数时，请提供全长 *N* 和 *K* 值，以指定缩短为 (*N*–*K*+*S*, *S*) 码的 (*N*, *K*) 码。

#### 依赖关系

要启用此参数，请选择 **指定缩短消息长度**。

### **生成多项式** — 生成多项式 `'X^10 + X^8 + X^5 + X^4 + X^2 + X + 1'`（默认） | polynomial character vector | binary row vector | binary Galois row vector

生成多项式，指定为下列之一：

- 多项式字符向量 — 有关详细信息，请参阅 Communications Toolbox 中的多项式表示。
- 按降幂顺序表示生成多项式系数的二进制行向量。
- 按降幂顺序表示生成多项式系数的二进制伽罗瓦行向量。

**示例：** `'X^10 + X^8 + X^5 + X^4 + X^2 + X + 1'`，等效于 `bchgenpoly(15,5)`

#### 依赖关系

要启用此参数，请选择 **指定生成多项式**。

### **本原多项式** — 本原多项式 `'X^4 + X + 1'`（默认） | polynomial character vector | binary row vector

按降幂顺序表示的本原多项式。它是定义有限伽罗瓦域 GF(2) 的 *M* 阶多项式，指定为下列之一：

- 多项式字符向量 — 有关详细信息，请参阅 Communications Toolbox 中的多项式表示。
- 按降幂顺序表示生成多项式系数的二进制行向量。

**示例：** `'X^4 + X + 1'`，这是用于 (15,5) 码的本原多项式，`ppoly = primpoly(4,'nodisplay');
int2bit(ppoly,ceil(log2(max(ppoly))))'`

#### 依赖关系

要启用此参数，请选择 **指定本原多项式**。

### **禁用生成多项式检查** — 禁用生成多项式检查的选项 on（默认） | off

选择此参数可禁用生成多项式检查。

每次模型初始化时，该模块都会执行多项式检查。此检查验证 *X N* + 1 能否被指定的生成多项式整除，其中 *N* 表示完整码字长度。对于较大的码，禁用该检查可加快仿真过程。

**提示**

在禁用此功能之前，请务必至少运行一次检查。

#### 依赖关系

要启用此参数，请选择 **指定生成多项式**。

### **打孔向量** — 打孔向量 `[ones(8,1); zeros(2,1)]`（默认） | binary column vector

打孔向量，指定为长度为 *N*–*K* 的二进制列向量。带有 `1` 的元素索引表示未经更改通过模块的数据符号索引。带有 `0` 的元素索引表示从数据流中打孔（即移除）的数据符号索引。有关详细信息，请参阅缩短、打孔和擦除。

**注意**

对于打孔向量和擦除向量，`1` 和 `0` 的含义正好相反。对于擦除向量，`1` 表示该数据符号将被替换为擦除符号，`0` 表示该数据符号未经更改通过模块。此约定适用于编码器和解码器。

#### 依赖关系

要启用此参数，请选择 **打孔码**。

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

**在 R2006a 之前引入**

## 描述

从二进制向量数据创建 BCH 码

BCH Encoder 模块创建具有消息长度 *K* 和码字长度（*N* – 打孔数）的 BCH 码。

如果编码器每帧处理多个码字，则同一打孔模式适用于所有码字。输入和输出信号长度在 BCH 模块中的输入和输出信号长度中列出。

有关有效 *N* 值、有效 (*N,K*) 对以及给定 BCH 码的纠错能力的信息，请参阅提示。
