---
type: simulink-block
title: 'TPC Encoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction / Block'
documentation_page: 'tpcencoder'
documentation_source_path: 'ref/tpcencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# TPC Encoder

## 端口

### 输入

### **In** — 待编码的消息 列向量

待编码的输入消息比特，指定为列向量。

- 对于全长输入消息，列向量的长度必须为 Number of rows in message, Kr 与 Number of columns in message, Kc 的乘积。
- 对于缩短输入消息，列向量的长度必须为 Number of rows in shortened message, Sr 与 Number of columns in shortened message, Sc 的乘积。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### 输出

### **Out** — TPC 编码后的消息 列向量

TPC 编码后的消息，返回为与输入信号具有相同数据类型的列向量。

- 对于全长输入消息，列向量的长度为 Number of rows in code, Nr 与 Number of columns in code, Nc 的乘积。
- 对于缩短输入消息，列向量的长度为
  (*N*R–*K*R+*S*R)
  与
  (*N*C–*K*C+*S*C) 的乘积，其中：

  - *N*R 是 Number of rows in code, Nr 的值。
  - *K*R 是 Number of rows in message, Kr 的值。
  - *S*R 是 Number of rows in shortened message, Sr 的值。
  - *N*C 是 Number of columns in code, Nc 的值。
  - *K*C 是 Number of columns in message, Kc 的值。
  - *S*C 是 Number of columns in shortened message, Sc 的值。

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

#### 行 TPC 参数

### **Extended codes** — TPC 行参数的扩展码指示符 `on`（默认）| `off`

- 选中 Extended codes 时，Number of rows in code, Nr 和 Number of rows in message, Kr 的列表包含扩展单个码对 (*N*R,*K*R) 的有效值。
- 清除 Extended codes 时，Number of rows in code, Nr 和 Number of rows in message, Kr 的列表包含非扩展单个码对 (*N*R,*K*R) 的有效值。

### **Number of rows in code, Nr** — 乘积码矩阵中的行数 `16`（默认）| 整数

乘积码矩阵中的行数，*N*R。整数值列表因 Extended codes 的设置而异。

### **Number of rows in message, Kr** — 消息矩阵中的行数 `11`（默认）| 整数

消息矩阵中的行数，*K*R。整数值列表因 Extended codes 和 Number of rows in code, Nr 的设置而异。

### **Specify shortened message length** — 指定行的缩短消息长度 `off`（默认）| `on`

选择 **Specify shortened message length** 可为 Number of rows in shortened message, Sr 指定值。

### **Number of rows in shortened message, Sr** — 缩短消息矩阵中的行数 `9`（默认）| 整数

缩短消息矩阵中的行数，*S*R，指定为小于或等于 *K*R 的整数。指定此参数时，请提供全长 *N*R 和 *K*R 值以指定 (*N*R,*K*R) 码对。此码对随后被缩短为 (*N*R–*K*R+*S*R,*S*R) 码对，其中：

- *N*R 是 Number of rows in code, Nr 的值。
- *K*R 是 Number of rows in message, Kr 的值。
- *S*R 是 Number of rows in shortened message, Sr 的值。

#### 依赖关系

要启用此参数，请选择 Specify shortened message length。

#### 列 TPC 参数

### **Extended codes** — TPC 列参数的扩展码指示符 `on`（默认）| `off`

- 选中 Extended codes 时，Number of columns in code, Nc 和 Number of columns in message, Kc 的列表包含扩展单个码对 (*N*C,*K*C) 的有效值。
- 清除 Extended codes 时，Number of columns in code, Nc 和 Number of columns in message, Kc 的列表包含非扩展单个码对 (*N*C,*K*C) 的有效值。

### **Number of columns in code, Nc** — 乘积码矩阵中的列数 `32`（默认）| 整数

乘积码矩阵中的列数，*N*C。整数值列表因 Extended codes 的设置而异。

### **Number of columns in message, Kc** — 消息矩阵中的列数 `26`（默认）| 整数

消息矩阵中的列数，*K*C。整数值列表因 Extended codes 和 Number of columns in code, Nc 的设置而异。

### **Specify shortened message length** — 指定列的缩短消息长度 `off`（默认）| `on`

选择 **Specify shortened message length** 可为 Number of columns in shortened message, Sc 指定值。

### **Number of columns in shortened message, Sc** — 缩短消息矩阵中的列数 `22`（默认）| 整数

缩短消息矩阵中的列数，*S*C，指定为整数。指定此参数时，请提供全长 *N*C 和 *K*C 值以指定 (*N*C,*K*C) 码对。此码对随后被缩短为 (*N*C–*K*C+*S*C, *S*C) 码对，其中：

- *N*C 是 Number of columns in code, Nc 的值。
- *K*C 是 Number of columns in message, Kc 的值。
- *S*C 是 Number of columns in shortened message, Sc 的值。

#### 依赖关系

要启用此参数，请选择 Specify shortened message length。

### **Simulate using** — 要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

要运行的仿真类型，指定为 `Code generation` 或 `Interpreted execution`。

- `Code generation` — 通过使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。除非模型发生变化，否则模型会在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度快于 `Interpreted execution` 选项。
- `Interpreted execution` — 通过使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但后续仿真的速度慢于 `Code generation` 选项。在此模式下，您可以调试模块的源代码。

有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。

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

**在 R2018b 中引入**

## 描述

Turbo 乘积码 (TPC) 编码器

TPC Encoder 模块对输入消息执行二维 Turbo 乘积码 (TPC) 编码。乘积码是线性分组码的二维级联。线性分组码可以是奇偶校验码、汉明码或能够纠正两个错误的 BCH 码。扩展码和缩短码可以独立应用于每个维度。有关二维 TPC 编码的描述，请参阅 Turbo Product Code Construction。

有关有效码对以及每个有效码对的纠错能力的信息，请参阅 Component Code Pairs。
