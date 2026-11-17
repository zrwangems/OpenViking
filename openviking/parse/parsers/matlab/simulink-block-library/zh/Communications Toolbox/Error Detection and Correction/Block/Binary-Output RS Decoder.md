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
```yaml
ports:
- name: In
  summary: 里德-所罗门码字二进制列向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | ufix(1)
- name: Era
  summary: 删除向量二进制列向量
  direction: input
  data_types: double | Boolean
- name: Out
  summary: 解码消息二进制列向量
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | ufix(1)
- name: Err
  summary: 解码错误整数向量
  direction: output
  data_types: double
```

### 输入

### **In** — 里德-所罗门码字二进制列向量

以比特表示的里德-所罗门码字，指定为
(*N*C×(*N*
– *K* + *S* –
*P*)×*M*)×1 二进制列
向量。*N*C 是
码字数量，*N* 是 **Codeword length N
(symbols)**，*K* 是 **Message
length K (symbols)**，*S* 是
**Shortened message length S (symbols)**，
*P* 是每个码字的删余数，*M* 是每个符号的比特数。

有关详细信息，请参阅 Input and Output Signal Length in RS Blocks。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `ufix(1)`

### **Era** — 删除向量二进制列向量

以符号表示的删除向量，指定为
(*N*C×(*N*
– *K* + *S* –
*P*))×1 二进制列向量。
*N*C 是
码字数量，*N* 是 **Codeword length N
(symbols)**，*K* 是 **Message
length K (symbols)**，*S* 是
**Shortened message length S (symbols)**，
*P* 是每个码字的删余数，*M* 是每个符号的比特数。

删除值为 1 对应于码字中相同位置的已删除比特。值为 0 对应于未删除的比特。有关
详细信息，请参阅 Puncturing and Erasures。

#### 依赖关系

要启用此端口，请选择 **Enable erasures input
port**。

**数据类型：** `double` | `Boolean`
### 输出

### **Out** — 解码消息二进制列向量

以比特表示的解码消息，返回为以下之一：

- 当没有消息缩短时，返回
  (*N*C×*K*×*M*)×1
  二进制列向量。
- 当有消息缩短时，返回
  (*N*C×*S*×*M*)×1
  二进制列向量。

*N*C 是
消息字数量，*K* 是 **Message
length K (symbols)**，*M* 是每个符号的
比特数，*S* 是 **Shortened
message length S (symbols)**。

**注意**

解码消息字的数量等于码字的数量。

有关详细信息，请参阅 Input and Output Signal Length in RS Blocks。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `ufix(1)`

### **Err** — 解码错误整数向量

符号解码错误，返回为具有
*N*C 个元素的整数向量，其中
*N*C 是码字数量。此端口指示在解码每个码字期间检测到的符号错误数。负整数表示该
模块检测到的错误数超过了使用指定编码方案所能纠正的错误数。

**注意**

(*N*,*K*) 里德-所罗门码
在每个码字中最多可纠正 `floor((N-K)/2)` 个符号错误
（不是比特错误）。当接收到的码字包含
超过 (*N*-*K*)/2 个符号
错误时，会发生解码失败。

#### 依赖关系

要启用此端口，请选择 **Output number of corrected
symbol errors**。

**数据类型：** `double`

有关详细信息，请参阅 Supported Data Types。
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
  summary: 生成多项式 rsgenpoly(7, 3, [], [], 'double')（默认）| 多项式字符向量 | 二进制行向量 | 二进制伽罗瓦行向量
  group: ''
- name: Primitive polynomial
  summary: 本原多项式 'X^3 + X + 1'（默认）| 多项式字符向量 | 二进制行向量
  group: ''
- name: Puncture vector
  summary: 删余向量 [ones(2,1); zeros(2,1)]（默认）| 二进制列向量
  group: ''
- name: Enable erasures input port
  summary: 启用删除输入端口 off（默认）| on
  group: ''
- name: Output number of corrected symbol errors
  summary: 启用端口以输出已纠正符号错误数 off（默认）| on
  group: ''
- name: Output data type
  summary: 模块的输出类型 Same as input（默认）| boolean | double
  group: ''
```

要以交互方式编辑模块参数，请使用
Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在
**Prepare** 库中，选择 **Property
Inspector**。

### **Codeword length N (symbols)** — 码字长度 `7`（默认）| 整数

以符号表示的码字长度，指定为整数。

有关详细信息，请参阅 Restrictions on M and Codeword Length N and Input and Output Signal Length in RS Blocks。

### **Message length K (symbols)** — 消息字长度 `3`（默认）| 整数

以符号表示的消息字长度，指定为范围 [1,
*N*–2] 内的整数，其中 *N* 是码字
长度。

### **Shortened message length S (symbols)** — 缩短的消息字长度 `3`（默认）| 整数

以符号表示的缩短消息字长度，指定为整数，满足
*S* ≤ *K*。当 **Shortened
message length S (symbols)** < **Message length K
(symbols)** 时，里德-所罗门码被缩短。

您仍需为全长 (*N*, *K*) 码指定 *N* 和 *K* 值，但
解码会缩短为
(*N*–*K*+*S*,
*S*) 码。

#### 依赖关系

要启用此参数，请选择 **Specify shortened message
length**。

### **Generator polynomial** — 生成多项式 `rsgenpoly(7, 3, [], [], 'double')`（默认）| 多项式字符向量 | 二进制行向量 | 二进制伽罗瓦行向量

生成多项式，其值从 0 到
2*M*–1，按降幂顺序排列，指定为以下之一：

- 多项式字符向量。有关详细信息，请参阅 Representation of Polynomials in Communications Toolbox。
- 表示生成多项式按降幂顺序排列的系数的
  整数行向量。
- 表示生成多项式按降幂顺序排列的系数的
  整数伽罗瓦行向量。

每个系数都是由本原多项式定义的伽罗瓦域的元素。有关详细信息，请参阅 Specify the Generator Polynomial。

**示例：** `[1 3 1 2 3]`，等效于
`rsgenpoly(7,3)`

#### 依赖关系

要启用此参数，请选择 **Specify generator
polynomial**。

### **Primitive polynomial** — 本原多项式 `'X^3 + X + 1'`（默认）| 多项式字符向量 | 二进制行向量

按降幂顺序排列的本原多项式。此多项式为
*M* 阶，定义了与构成消息字和码字的整数相对应的有限伽罗瓦域
GF(2M)。将本原多项式指定为以下之一：

- 多项式字符向量。有关详细信息，请参阅 Representation of Polynomials in Communications Toolbox。
- 表示生成多项式系数的
  二进制行向量。

有关详细信息，请参阅 Restrictions on M and Codeword Length N。

**示例：** `'X^3 + X + 1'`，这是用于 (7,3) 码的本原
多项式，`ppoly = primpoly(3,'nodisplay');
int2bit(ppoly,ceil(log2(max(ppoly))))'`

#### 依赖关系

要启用此参数，请选择 **Specify primitive
polynomial**。

### **Puncture vector** — 删余向量 `[ones(2,1); zeros(2,1)]`（默认）| 二进制列向量

删余向量，指定为
(*N*–*K*)×1 二进制列向量。
元素索引为 `1` 的位置表示通过该模块
原样传递的数据
*符号*索引。元素索引为 `0` 的位置表示从数据流中
删余或移除的数据
*符号*索引。有关详细信息，请参阅 Puncturing and Erasures。

#### 依赖关系

要启用此参数，请选择 **Punctured
code**。

### **Enable erasures input port** — 启用删除输入端口 off（默认）| on

选中此复选框将启用删除端口
**Era**。有关详细信息，请参阅 Puncturing and Erasures。

### **Output number of corrected symbol errors** — 启用端口以输出已纠正符号错误数 off（默认）| on

选中此复选框将启用一个额外的输出端口
**Err**，它指示该模块在输入码字中纠正的符号错误数。

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

**在 R2006a 之前推出**

## 描述

解码里德-所罗门码以恢复二进制向量数据

Binary-Output RS Decoder 模块从二进制里德-所罗门码字向量中恢复二进制消息向量。为了正确解码，
此模块中的参数值必须与对应的 Binary-Input RS Encoder 模块中的参数值匹配。

该码的符号是长度为 *M* 的二进制序列，
对应于伽罗瓦域
*GF*(2*M*) 的元素。每个符号中的
第一个比特是最高有效位。

此图显示了码字长度
*N*=7 和消息字长度 *K*=2 时解码器的输入-输出字长度。由于
*N*=2*M*–1，当
*N*=7 时，符号长度 *M*=3。

每个输入码字是长度为 21 的二进制向量，表示 7 个三位
整数。每个对应的输出消息字是长度为 6 的二进制向量，表示
2 个三位整数。有关详细信息，请参阅 Input and Output Signal Length in RS Blocks。

此图标显示了所有端口，包括可选端口：
