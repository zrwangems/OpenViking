---
type: simulink-block
title: 'Scrambler'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Signal Operations'
documentation_page: 'scrambler'
documentation_source_path: 'ref/scrambler.html'
language: zh-CN
chinese_source: worker-translation
---

# Scrambler

## 端口

### 输入

### **In** — 输入数据信号向量

输入数据信号，指定为 *N*S-by-1 向量。*N*S 表示输入信号中的样本数。输入值必须是从 `0` 到 `Calculation base` – `1` 的整数。

**数据类型：** `double` | `Boolean` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Rst** — 复位加扰器标量

复位加扰器，指定为标量。如果向该端口施加非零输入，则复位加扰器。

#### 依赖关系

要启用此端口，请将 `Initial states source` 设置为 `Dialog Parameter`，并选择 `Reset on nonzero input via port`。

### **ISt** — 初始状态向量

仿真开始时加扰器寄存器的初始状态，指定为非负整数向量。**ISt** 的长度必须等于 `Scramble polynomial` 参数的阶数。向量元素值必须是从 `0` 到 `Calculation base` – `1` 的整数。

#### 依赖关系

要启用此端口，请将 `Initial states source` 设置为 `Input port`。

### 输出

### **Out** — 输出加扰数据向量

输出加扰数据，以 *N*S-by-1 向量形式返回。*N*S 等于输入信号中的样本数。

**数据类型：** `double`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink Toolstrip 的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### **Calculation base** — 计算基数 `4`（默认）| 非负整数

用于加扰器中的模运算的计算基数，指定为非负整数。此模块的输入和输出是从 `0` 到 **Calculation base** – `1` 的整数。

### **Scramble polynomial** — 定义加扰器中连接的多项式 `'1 + x^-1 + x^-2 + x^-4'`（默认）| 字符向量 | 整数向量 | 二进制向量

定义加扰器中连接的多项式，指定为字符向量、整数向量或二进制向量。**Scramble polynomial** 参数定义加扰器中每个开关是 on 还是 off。将多项式指定为：

- 字符向量，例如 `'1 + x^-6 + x^-8'`。有关以这种方式指定多项式的更多详细信息，请参阅 Representation of Polynomials in Communications Toolbox。
- 整数向量，例如 `[0 -6 -8]`，按 *x*-1 的降幂顺序列出解扰器系数，其中 *p*(*x*-1) = 1 + *p1x*-1 + *p2x*-2 + ...
- 二进制向量，例如 `[1 0 0 0 0 0 1 0 1]`，列出多项式中系数为 1 的 *x* 的幂。在这种情况下，加扰多项式的阶数比二进制向量长度小一。

**示例：** `'1 + x^-6 + x^-8'`、`[0 -6 -8]` 和 `[1 0 0 0 0 0 1 0 1]` 都表示以下多项式：

*p*(*x*-1) = 1 + *x*-6 + *x*-8

### **Initial states source** — 设置加扰器初始状态的来源 `Dialog Parameter`（默认）| `Input port`

- `Dialog Parameter` – 使用 `Initial states` 参数指定加扰器初始状态。
- `Input port` – 使用 `ISt` 端口指定加扰器初始状态。

### **Initial states** — 加扰器寄存器的初始状态 `[0 1 2 3]`（默认）| 非负整数向量

仿真开始时加扰器寄存器的初始状态，指定为非负整数向量。**Initial states** 的长度必须等于 `Scramble polynomial` 参数的阶数。向量元素值必须是从 `0` 到 `Calculation base` – `1` 的整数。

#### 依赖关系

当 `Initial states source` 设置为 `Dialog Parameter` 时，此参数可用。

### **Reset on nonzero input via port** — 通过输入端口复位加扰器 off（默认）| on

选择此参数以通过输入端口 `Rst` 复位 Scrambler 模块。

#### 依赖关系

当 `Initial states source` 设置为 `Dialog Parameter` 时，此参数可用。

## 所属库

Communications Toolbox / Sequence Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `integer` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

对输入信号进行加扰

Scrambler 模块对输入数据应用乘法加扰。

加扰的一个目的是减少传输信号中连续 0 或 1 的长度。长序列的 0 或 1 可能导致传输同步问题。此示意图展示了加扰器操作。所有加法器执行模 *N* 加法，其中 *N* 是由 `Calculation base` 参数指定的值。

在每个时间步，输入使寄存器内容依次移位。使用 `Scramble polynomial` 参数，您可以指定加扰器中每个开关的 on 或 off 状态。

为实现可重复的加扰器初始条件，您可以使用以下可选输入端口之一：

- 选择 `Reset on nonzero input via port` 参数，并使用 `Rst` 复位加扰器。
- 将 `Initial states source` 参数设置为 `Input port`，并使用 `ISt` 提供初始状态。

此模块可以在仿真期间接受长度可变的输入序列。有关长度可变序列的更多信息，请参阅 Variable-Size Signal Basics (Simulink)。

**注意**

要对输入数据应用加法加扰，您可以使用 PN Sequence Generator 模块和配置为 XOR 逻辑运算符的 Logical Operator (Simulink) 模块。有关示例，请参阅 Additive Scrambling of Input Data in Simulink。
