---
type: simulink-block
title: 'TPC Decoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction / Block'
documentation_page: 'tpcdecoder'
documentation_source_path: 'ref/tpcdecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# TPC Decoder

## 端口

### 输入

### **In** — 对数似然比列向量

对数似然比，指定为列向量。

- 对于全长输入消息，列向量的长度是 Number of rows in code, Nr 和 Number of columns in code, Nc 的乘积。
- 对于缩短的输入消息，列向量的长度是
  (*N*R–*K*R+*S*R)
  和
  (*N*C–*K*C+*S*C) 的乘积，其中：

  - *N*R 是 Number of rows in code, Nr 的值。
  - *K*R 是 Number of rows in message, Kr 的值。
  - *S*R 是 Number of rows in shortened message, Sr 的值。
  - *N*C 是 Number of columns in code, Nc 的值。
  - *K*C 是 Number of columns in message, Kc 的值。
  - *S*C 是 Number of columns in shortened message, Sc 的值。

**数据类型:** `double` | `single`
### 输出

### **Out** — TPC 解码消息列向量

TPC 解码消息，返回为二进制值的列向量。

- 对于全长输入消息，列向量的长度是 Number of rows in message, Kr 和 Number of columns in message, Kc 的乘积。
- 对于缩短的输入消息，列向量的长度是 Number of rows in shortened message, Sr 和 Number of columns in shortened message, Sc 的乘积。

**数据类型:** `Boolean`

### **Iter** — 实际解码迭代次数正整数

实际解码迭代次数，返回为正整数。

#### 依赖关系

要启用此端口，请选择 Output number of iterations executed。

**数据类型:** `double`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

#### 行 TPC 参数

### **Extended codes** — TPC 行参数的扩展码指示符 `on` (默认) | `off`

- 当选择 Extended codes 时，Number of rows in code, Nr 和 Number of rows in message, Kr 的列表包含扩展单个码对 (*N*R,*K*R) 的有效值。
- 当清除 Extended codes 时，Number of rows in code, Nr 和 Number of rows in message, Kr 的列表包含非扩展单个码对 (*N*R,*K*R) 的有效值。

### **Number of rows in code, Nr** — 乘积码矩阵的行数 `16` (默认) | 整数

乘积码矩阵的行数，*N*R。整数列表的值取决于 Extended codes 的设置。

### **Number of rows in message, Kr** — 消息矩阵的行数 `11` (默认) | 整数

消息矩阵的行数，*K*R。整数列表的值取决于 Extended codes 和 Number of rows in code, Nr 的设置。

### **Specify shortened message length** — 指定行的缩短消息长度 `off` (默认) | `on`

选择 **Specify shortened message length** 以指定 Number of rows in shortened message, Sr 的值。

### **Number of rows in shortened message, Sr** — 缩短消息矩阵的行数 `9` (默认) | 整数

缩短消息矩阵的行数，*S*R，指定为小于或等于 *K*R 的整数。当您指定此参数时，提供全长 *N*R 和 *K*R 值以指定 (*N*R,*K*R) 码对。然后此码对被缩短为 (*N*R–*K*R+*S*R,*S*R) 码对，其中：

- *N*R 是 Number of rows in code, Nr 的值。
- *K*R 是 Number of rows in message, Kr 的值。
- *S*R 是 Number of rows in shortened message, Sr 的值。

#### 依赖关系

要启用此参数，请选择 Specify shortened message length。

#### 列 TPC 参数

### **Extended codes** — TPC 列参数的扩展码指示符 `on` (默认) | `off`

- 当选择 Extended codes 时，Number of columns in code, Nc 和 Number of columns in message, Kc 的列表包含扩展单个码对 (*N*C,*K*C) 的有效值。
- 当清除 Extended codes 时，Number of columns in code, Nc 和 Number of columns in message, Kc 的列表包含非扩展单个码对 (*N*C,*K*C) 的有效值。

### **Number of columns in code, Nc** — 乘积码矩阵的列数 `32` (默认) | 整数

乘积码矩阵的列数，*N*C。整数列表的值取决于 Extended codes 的设置。

### **Number of columns in message, Kc** — 消息矩阵的列数 `26` (默认) | 整数

消息矩阵的列数，*K*C。整数列表的值取决于 Extended codes 和 Number of columns in code, Nc 的设置。

### **Specify shortened message length** — 指定列的缩短消息长度 `off` (默认) | `on`

选择 **Specify shortened message length** 以指定 Number of columns in shortened message, Sc 的值。

### **Number of columns in shortened message, Sc** — 缩短消息矩阵的列数 `22` (默认) | 整数

缩短消息矩阵的列数，*S*C，指定为整数。当您指定此参数时，提供全长 *N*C 和 *K*C 值以指定 (*N*C,*K*C) 码对。然后此码对被缩短为 (*N*C–*K*C+*S*C, *S*C) 码对，其中：

- *N*C 是 Number of columns in code, Nc 的值。
- *K*C 是 Number of columns in message, Kc 的值。
- *S*C 是 Number of columns in shortened message, Sc 的值。

#### 依赖关系

要启用此参数，请选择 Specify shortened message length。

### **Maximum number of iterations** — 最大解码迭代次数 `4` (默认) | 正整数

最大解码迭代次数，指定为正整数。

### **Stop iterating when code converges** — 基于分量码的计算伴随式或奇偶校验停止解码 `on` (默认) | `off`

选择 **Stop iterating when code converges** 以在最大迭代次数之前，如果分量码的计算伴随式或奇偶校验评估为零，则提前终止解码。

### **Output number of iterations executed** — 输出执行的迭代次数 `off` (默认) | `on`

选择此参数以添加 `Iter` 输出端口，并输出执行的 TPC 解码迭代的实际次数。

### **Simulate using** — 要运行的仿真类型 `Code generation` (默认) | `Interpreted execution`

要运行的仿真类型，指定为 `Code generation` 或 `Interpreted execution`。

- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。除非模型更改，否则模型在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度比使用 `Interpreted execution` 选项更快。
- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项缩短了启动时间，但后续仿真的速度比使用 `Code generation` 选项更慢。在此模式下，您可以调试模块的源代码。

有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。

## 所属库

Communications Toolbox / Error Detection and Correction / Block

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

Turbo 乘积码 (TPC) 解码器

TPC Decoder 模块使用 Chase-Pyndiah 算法，对乘积码对应的软输入 LLR 迭代执行二维 Turbo 乘积码 (TPC) 解码。乘积码是线性分组码的二维拼接。线性分组码可以是奇偶校验码、汉明码或能够纠正两个错误的 BCH 码。扩展码和缩短码可以独立应用于每个维度。有关二维 TPC 解码的描述，请参阅 Turbo Product Code Decoding。

有关有效码对以及每个有效码对的纠错能力的信息，请参阅 Component Code Pairs。
