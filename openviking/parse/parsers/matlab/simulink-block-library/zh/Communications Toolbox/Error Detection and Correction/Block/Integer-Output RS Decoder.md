---
type: simulink-block
title: 'Integer-Output RS Decoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction / Block'
documentation_page: 'integeroutputrsdecoder'
documentation_source_path: 'ref/integeroutputrsdecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Integer-Output RS Decoder

## 端口

### 输入

### **In** — 里德-所罗门码字整数列向量

里德-所罗门码字，指定为
(*N*C×(*N*
– *K* + *S* –
*P*)-by-1 整数列向量。
*N*C 是码字数量，*N* 是 **Codeword length
N**，*K* 是 **Message length
K**，*S* 是 **Shortened
message length S**，*P* 是每个码字的删余数。

有关详细信息，请参阅 RS 模块中的输入和输出信号长度。

**数据类型：** `single` | `double` | `integer`

### **Era** — 擦除向量二进制列向量

擦除向量，指定为与输入里德-所罗门码字大小相同的二进制列向量输入信号。

擦除值为 1 对应于码字中相同位置的擦除位。值为 0 对应于未擦除的位。有关详细信息，请参阅删余和擦除。

#### 依赖关系

要启用此端口，请选择 **Enable erasures input
port**。

**数据类型：** `double` | `Boolean`
### 输出

### **Out** — 解码消息整数列向量

解码消息，返回为以下之一：

- 当没有消息缩短时，为
  (*N*C×*K*)-by-1
  整数列向量。
- 当有消息缩短时，为
  (*N*C×*S*)-by-1
  整数列向量。

*N*C 是消息字的数量，*K* 是 **Message
length K (symbols)**，*S* 是
**Shortened message length S (symbols)**。

**注意**

解码消息字的数量等于码字的数量。

有关详细信息，请参阅 RS 模块中的输入和输出信号长度。

### **Err** — 解码错误整数向量

符号解码错误，返回为具有
*N*C 个元素的整数向量，其中
*N*C 是码字数量。此端口指示每个码字解码期间检测到的符号错误数量。负整数表示该块检测到的错误数量超过了使用指定编码方案所能纠正的数量。

**注意**

(*N*,*K*) 里德-所罗门码在每个码字中最多可以纠正 `floor((N-K)/2)` 个符号错误（不是位错误）。当接收到的码字包含超过 (*N*-*K*)/2 个符号错误时，会发生解码失败。

#### 依赖关系

要启用此端口，请选择 **Output number of corrected
symbol errors**。

**数据类型：** `double`

有关详细信息，请参阅支持的数据类型。

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### **Codeword length N** — 码字长度 `7`（默认）| 整数

码字长度，指定为整数。

有关详细信息，请参阅 M 和码字长度 N 的限制以及 RS 模块中的输入和输出信号长度。

### **Message length K** — 消息字长度 `3`（默认）| 整数

消息字长度，指定为范围 [1, *N*–2] 内的整数，其中 *N* 是码字长度。

### **Shortened message length S** — 缩短的消息字长度 `3`（默认）| 整数

缩短的消息字长度，指定为整数，使得 *S* ≤ *K*。当 **Shortened message length S** < **Message length K** 时，里德-所罗门码被缩短。

您仍然为全长 (*N*, *K*) 码指定 *N* 和 *K* 值，但解码被缩短为 (*N*–*K*+*S*, *S*) 码。

#### 依赖关系

要启用此参数，请选择 **Specify shortened message length**。

### **Generator polynomial** — 生成多项式 `rsgenpoly(7, 3, [], [], 'double')`（默认）| 多项式字符向量 | 二进制行向量 | 二进制伽罗瓦行向量

生成多项式，其值在范围 [0, 2*M*–1] 内，按降幂顺序排列，指定为以下之一：

- 多项式字符向量。有关详细信息，请参阅 Communications Toolbox 中的多项式表示。
- 表示生成多项式系数的整数行向量，按降幂顺序排列。
- 表示生成多项式系数的整数伽罗瓦行向量，按降幂顺序排列。

每个系数是由本原多项式定义的伽罗瓦域的元素。有关详细信息，请参阅指定生成多项式。

**示例：** `[1 3 1 2 3]`，等价于 `rsgenpoly(7,3)`

#### 依赖关系

要启用此参数，请选择 **Specify generator polynomial**。

### **Primitive polynomial** — 本原多项式 `'X^3 + X + 1'`（默认）| 多项式字符向量 | 二进制行向量

本原多项式，按降幂顺序排列。此多项式为 *M* 阶，定义了与构成消息字和码字的整数相对应的有限伽罗瓦域 GF(2M)。将本原多项式指定为以下之一：

- 多项式字符向量。有关详细信息，请参阅 Communications Toolbox 中的多项式表示。
- 表示生成多项式系数的二进制行向量。

有关详细信息，请参阅指定本原多项式。

**示例：** `'X^3 + X + 1'`，这是用于 (7,3) 码的本原多项式，`ppoly = primpoly(3,'nodisplay'); int2bit(ppoly,ceil(log2(max(ppoly))))'`

#### 依赖关系

要启用此参数，请选择 **Specify primitive polynomial**。

### **Puncture vector** — 删余向量 `[ones(2,1); zeros(2,1)]`（默认）| 二进制列向量

删余向量，指定为 (*N*–*K*)-by-1 二进制列向量。元素索引为 `1` 的位置表示原样通过该块的数据*符号*索引。元素索引为 `0` 的位置表示从数据流中被删余或移除的数据*符号*索引。有关详细信息，请参阅删余和擦除。

**注意**

如果编码器每帧处理多个码字，则相同的删余模式适用于所有码字。

#### 依赖关系

要启用此参数，请选择 **Puncture code**。

### **Enable erasures input port** — 启用擦除输入端口 关（默认）| 开

选中此复选框将启用擦除端口 **Era**。有关详细信息，请参阅删余和擦除。

### **Output number of corrected symbol errors** — 启用端口以输出已纠正符号错误数量 关（默认）| 开

选中此复选框将启用一个额外的输出端口 **Err**，它指示该块在输入码字中纠正的符号错误数量。

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

解码里德-所罗门码以恢复整数向量数据

Integer-Output RS Decoder 模块从里德-所罗门码字向量中恢复消息向量。为了正确解码，此模块中的参数值必须与相应的 Integer-Input RS Encoder 模块中的参数值匹配。

里德-所罗门码具有消息长度 *K* 和码字长度 *N* – *删余数*。您可以直接在模块对话框中指定 *N* 和 *K*。该码的符号是范围 [0, 2*M*-1] 内的整数，表示有限域 *GF*(2*M*) 的元素。*M* 和 *N* 的限制在下面的 M 和码字长度 N 的限制中描述。

此图标显示了可选端口。

输入和输出分别是表示码字和消息的整数值信号。有关详细信息，请参阅 RS 模块中的输入和输出信号长度。该模块从输入数据类型继承输出数据类型。有关每个模块端口支持的数据类型的信息，请参阅支持的数据类型。

有关表示里德-所罗门码数据的详细信息，请参阅整数格式（仅限里德-所罗门）一节。

如果解码器每帧处理多个码字，则相同的删余模式适用于所有码字。

M 的默认值为 `ceil(log2(N+1))`，即大于或等于 log2(N+1) 的最小整数。您可以通过为 GF(2M) 指定本原多项式来更改 M 的默认值，如下面的指定本原多项式所述。

您还可以指定里德-所罗门码的生成多项式，如下面的指定生成多项式所述。

(*N*, *K*) 里德-所罗门码在每个码字中最多可以纠正 `floor((N-K)/2)` 个符号错误（*不是*位错误）。

如果解码失败，解码器输入的消息部分将原样返回作为解码器输出。

输入和输出信号的采样时间相等。
