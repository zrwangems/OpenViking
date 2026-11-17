---
type: simulink-block
title: 'Descrambler'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Sequence Operations'
documentation_page: 'descrambler'
documentation_source_path: 'ref/descrambler.html'
language: zh-CN
chinese_source: worker-translation
---

# Descrambler

## 端口
```yaml
ports:
- name: In
  summary: 输入数据信号向量
  direction: input
  data_types: double | Boolean | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: Rst
  summary: 重置扰码器标量
  direction: input
- name: ISt
  summary: 初始状态标量
  direction: input
- name: Out
  summary: 输出解扰数据向量
  direction: output
  data_types: double
```

### 输入

### **In** — 输入数据信号向量

输入数据信号，指定为 *N*S×1 向量。*N*S 表示输入信号中的样本数。输入值必须为从 `0` 到 `Calculation base` – `1` 的整数。

**数据类型：** `double` | `Boolean` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Rst** — 重置扰码器标量

重置扰码器，指定为标量。如果向该端口施加非零输入，则重置扰码器。

#### 依赖关系

要启用此端口，请将 `Initial states source` 设置为 `Dialog Parameter`，并选择 `Reset on nonzero input via port`。

### **ISt** — 初始状态标量

仿真开始时解扰器寄存器的初始状态，指定为非负整数向量。**ISt** 的长度必须等于 `Scramble polynomial` 参数的阶数。向量元素值必须为从 `0` 到 `Calculation base` – `1` 的整数。

#### 依赖关系

要启用此端口，请将 `Initial states source` 设置为 `Input port`。
### 输出

### **Out** — 输出解扰数据向量

输出解扰数据，以 *N*S×1 向量形式返回。*N*S 等于输入信号中的样本数。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Calculation base
  summary: 计算基数 4（默认）| 非负整数
  group: ''
- name: Scramble polynomial
  summary: 定义解扰器中连接关系的多项式 '1 + x^-1 + x^-2 + x^-4'（默认）| 字符向量 | 整数向量 | 二进制向量
  group: ''
- name: Initial states source
  summary: 设置解扰器初始状态的来源 Dialog Parameter（默认）| Input port
  group: ''
- name: Initial states
  summary: 解扰器寄存器的初始状态 [0 1 2 3]（默认）| 非负整数向量
  group: ''
- name: Reset on nonzero input via port
  summary: 通过输入端口重置解扰器 off（默认）| on
  group: ''
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### **Calculation base** — 计算基数 `4`（默认）| 非负整数

解扰器中用于模运算的计算基数，指定为非负整数。此模块的输入和输出为从 `0` 到 **Calculation base** – `1` 的整数。

### **Scramble polynomial** — 定义解扰器中连接关系的多项式 `'1 + x^-1 + x^-2 + x^-4'`（默认）| 字符向量 | 整数向量 | 二进制向量

定义解扰器中连接关系的多项式，指定为字符向量、整数向量或二进制向量。**Scramble polynomial** 参数定义解扰器中每个开关是开启还是关闭。按以下方式指定多项式：

- 字符向量，例如 `'1 + x^-6 + x^-8'`。有关以这种方式指定多项式的更多详细信息，请参阅 Representation of Polynomials in Communications Toolbox。
- 整数向量，例如 `[0 -6 -8]`，按 *x*-1 的降幂顺序列出解扰器系数，其中 *p*(*x*-1) = 1 + *p1x*-1 + *p2x*-2 + ...
- 二进制向量，例如 `[1 0 0 0 0 0 1 0 1]`，列出多项式中系数为 1 的 *x* 的幂。在这种情况下，解扰多项式的阶数比二进制向量长度小一。

**示例：** `'1 + x^-6 + x^-8'`、`[0 -6 -8]` 和 `[1 0 0 0 0 0 1 0 1]` 都表示以下多项式：

*p*(*x*-1) = 1 + *x*-6 + *x*-8

### **Initial states source** — 设置解扰器初始状态的来源 `Dialog Parameter`（默认）| `Input port`

- `Dialog Parameter` – 使用 `Initial states` 参数指定解扰器初始状态。
- `Input port` – 使用 `ISt` 端口指定解扰器初始状态。

### **Initial states** — 解扰器寄存器的初始状态 `[0 1 2 3]`（默认）| 非负整数向量

仿真开始时解扰器寄存器的初始状态，指定为非负整数向量。**Initial states** 的长度必须等于 `Scramble polynomial` 参数的阶数。向量元素值必须为从 `0` 到 `Calculation base` – `1` 的整数。

#### 依赖关系

当 `Initial states source` 设置为 `Dialog Parameter` 时，此参数可用。

### **Reset on nonzero input via port** — 通过输入端口重置解扰器 off（默认）| on

选择此参数可通过输入端口 `Rst` 重置 Descrambler 模块。

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

**在 R2006a 之前推出**

## 描述

对输入信号进行解扰

Descrambler 模块对输入数据应用乘法解扰。它执行发射机中使用的 Scrambler 模块的逆操作。

此示意图展示了乘法解扰操作。加法器和减法器按模 *N* 运算，其中 *N* 是 `Calculation base` 参数指定的值。

在每个时间步，输入使寄存器内容依次移位。使用 `Scramble polynomial` 参数，您可以指定解扰器中每个开关的开启或关闭状态。要使 Descrambler 模块反转 Scrambler 模块的操作，请在两个模块中使用相同的参数设置。如果扰码器和解扰器之间没有信号延迟，则两个模块中的 **Initial states** 必须相同。

要实现可重复的初始解扰器条件，您可以使用以下可选输入端口之一：

- 选择 `Reset on nonzero input via port` 参数，并使用 `Rst` 重置扰码器。
- 将 `Initial states source` 参数设置为 `Input port`，并使用 `ISt` 提供初始状态。

此模块可以接受在仿真期间长度变化的输入序列。有关长度变化序列的更多信息，请参阅 Variable-Size Signal Basics (Simulink)。

**注意**

要对输入数据应用加法解扰，您可以使用 PN Sequence Generator 模块和配置为 XOR 逻辑运算符的 Logical Operator (Simulink) 模块。有关示例，请参阅 Additive Scrambling of Input Data in Simulink。
