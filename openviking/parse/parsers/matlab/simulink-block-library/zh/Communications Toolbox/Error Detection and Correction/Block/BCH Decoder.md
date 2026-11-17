---
type: simulink-block
title: 'BCH Decoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction / Block'
documentation_page: 'bchdecoder'
documentation_source_path: 'ref/bchdecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# BCH Decoder

## 端口

### 输入

### **In** — 编码消息二进制列向量

编码消息，指定为二进制列向量。编码消息是消息长度为 *K*、码字长度为（*N* – 删余数）的 BCH 码。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Era** — 删除向量二进制列向量

删除向量，指定为与 `In` 长度相同的二进制列向量。删除值为 1 对应于码字中相同位置的被删除比特。值为 0 对应于未被删除的比特。

#### 依赖关系

要启用此端口，请选择 **Enable erasures input port**。

**数据类型：** `double` | `Boolean`
### 输出

### **Out** — 解码消息二进制列向量

解码消息，以二进制列向量输入信号形式返回，其元素数量为 **Message length, K** 的整数倍；如果码被缩短，则为 **Shortened message length, S** 的整数倍。每组输入元素表示一个待解码的码字。输入和输出信号长度列于 BCH 模块的输入和输出信号长度表中。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Err** — 解码错误整数向量

解码错误，以整数向量形式返回，指示在码字解码期间检测到的错误数量。负整数表示该模块检测到的错误数量超过了使用该编码方案所能纠正的数量。

#### 依赖关系

要启用此端口，请选择 **Output number of corrected errors**。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

有关详细信息，请参阅支持的数据类型。

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### **Codeword length, N** — 码字长度 `15`（默认）| 整数

码字长度，指定为 *N* = 2*M*–1 形式的整数，其中 *M* 为 3 到 16 的整数。有关详细信息，请参阅提示。

### **Message length, K** — 消息长度 `5`（默认）| 整数

消息长度，指定为整数。（`N`、`K`）对必须生成窄义 BCH 码。

### **Shortened message length, S** — 缩短消息长度 `5`（默认）| 整数

缩短消息长度，指定为整数。指定此参数时，请提供完整长度的 *N* 和 *K* 值，以指定被缩短为（*N*–*K*+*S*、*S*）码的（*N*、*K*）码。

#### 依赖关系

要启用此参数，请选择 **Specify shortened message length**。

### **Generator polynomial** — 生成多项式 `'X^10 + X^8 + X^5 + X^4 + X^2 + X + 1'`（默认）| 多项式字符向量 | 二进制行向量 | 二进制伽罗瓦行向量

生成多项式，指定为以下之一：

- 多项式字符向量 — 有关详细信息，请参阅 Communications Toolbox 中的多项式表示。
- 二进制行向量，按降幂顺序表示生成多项式的系数。
- 二进制伽罗瓦行向量，按降幂顺序表示生成多项式的系数。

**示例：** `'X^10 + X^8 + X^5 + X^4 + X^2 + X + 1'`，等价于 `bchgenpoly(15,5)`

#### 依赖关系

要启用此参数，请选择 **Specify generator polynomial**。

### **Primitive polynomial** — 本原多项式 `'X^4 + X + 1'`（默认）| 多项式字符向量 | 二进制行向量

按降幂顺序表示的本原多项式。它是定义有限伽罗瓦域 GF(2) 的 *M* 阶多项式，指定为以下之一：

- 多项式字符向量 — 有关详细信息，请参阅 Communications Toolbox 中的多项式表示。
- 二进制行向量，按降幂顺序表示生成多项式的系数。

**示例：** `'X^4 + X + 1'`，这是用于 (15,5) 码的本原多项式，`ppoly = primpoly(4,'nodisplay'); int2bit(ppoly,ceil(log2(max(ppoly))))'`

#### 依赖关系

要启用此参数，请选择 **Specify primitive polynomial**。

### **Disable generator polynomial checking** — 禁用生成多项式检查的选项 on（默认）| off

选择此参数以禁用生成多项式检查。

每次模型初始化时，模块都会执行多项式检查。此检查验证 *X N* + 1 是否可被指定的生成多项式整除，其中 *N* 表示完整码字长度。对于较大的码，禁用该检查可加快仿真过程。

**提示**

在禁用此功能之前，请始终至少运行一次检查。

#### 依赖关系

要启用此参数，请选择 **Specify generator polynomial**。

### **Puncture vector** — 删余向量 `[ones(8,1); zeros(2,1)]`（默认）| 列向量

删余向量，指定为长度为 *N*–*K* 的二进制列向量。元素索引为 `1` 的位置表示原样通过模块的数据符号索引。元素索引为 `0` 的位置表示从数据流中被删余或移除的数据符号索引。有关详细信息，请参阅删余和删除。

#### 依赖关系

要启用此参数，请选择 **Puncture code**。

### **Enable erasures input port** — 启用删除输入端口的选项 off（默认）| on

选中此复选框将启用删除端口 `Era`。

通过该端口，您可以输入长度为码字输入 1/*M* 倍的二进制列向量。

删除值为 `1` 对应于位打包码字中相同位置的被删除符号。值为 `0` 对应于未被删除的符号。有关详细信息，请参阅删余和删除。

### **Output number of corrected errors** — 启用输出已纠正错误数端口的选项 off（默认）| on

选中此复选框将启用额外的输出端口 `Err`，它指示模块在输入码字中纠正的错误数量。

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

解码 BCH 码以恢复二进制向量数据

BCH Decoder 模块从二进制 BCH 码字向量中恢复二进制消息向量。为正确解码，此模块中的 **Codeword length, N** 和 **Message length, K** 参数值必须与对应的 BCH Encoder 模块中的参数匹配。*N* 和 *K* 的完整长度值必须生成有效的窄义 BCH 码。

如果编码器每帧处理多个码字，则相同的删余模式适用于所有码字。输入和输出信号长度列于 BCH 模块的输入和输出信号长度表中。

有关有效 *N* 值、有效（*N*,*K*）对以及给定 BCH 码的纠错能力的信息，请参阅提示。

如果解码失败，解码器输入的消息部分将原样返回作为解码器输出。

所有输入和输出信号的采样时间相等。

此图标显示了可选端口。
