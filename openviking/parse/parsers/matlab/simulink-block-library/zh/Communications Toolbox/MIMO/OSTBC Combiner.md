---
type: simulink-block
title: 'OSTBC Combiner'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'MIMO'
documentation_page: 'ostbccombiner'
documentation_source_path: 'ref/ostbccombiner.html'
language: zh-CN
chinese_source: worker-translation
---

# OSTBC Combiner

## 端口

### 输入

### **Rx** — 接收信号列向量 | 矩阵 | 3-D 数组

接收信号，指定为矩阵或 3-D 数组。有关详细信息，请参阅输入到输出维度。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** 是

### **cEst** — 信道估计矩阵 | 3-D 数组 | 4-D 数组

信道估计，指定为矩阵或 3-D 数组。有关详细信息，请参阅输入到输出维度。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** 是
### 输出

### **Out** — 输出数据矩阵 | 3-D 数组

输出数据，以矩阵或 3-D 数组形式返回。有关详细信息，请参阅输入到输出维度。

输出信号从输入信号继承数据类型。对于定点信号，复数共轭可能会导致溢出，必须使用 **Saturate on integer overflow** 定点参数进行管理。

此端口在模块图标上未命名。

**数据类型：** `single` | `double` | `fixed point`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 中，从 **Simulation** 选项卡的 **Prepare** 库中，选择 **Property Inspector**。

#### 主要

### **Number of transmit antennas** — 发射天线数量 `2` （默认） | `3` | `4`

发射天线数量，指定为 `2`、`3` 或 `4`。

### **Rate** — 符号速率 `3/4` （默认） | `1/2`

码的符号速率，指定为 `3/4` 或 `1/2`。当您将 **Number of transmit antennas** 设置为 `2` 时，符号速率为 `1`。

#### 依赖关系

要启用此参数，请将 **Number of transmit antennas** 设置为 `3` 或 `4`。

### **Number of receive antennas** — 接收天线数量 `1` （默认） | [1,8] 范围内的整数

接收天线数量，指定为 [1,8] 范围内的整数。

#### 数据类型

### **Rounding mode** — 定点计算的舍入模式 `Floor` （默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

定点计算的舍入模式，指定为 `Floor`、`Ceiling`、`Convergent`、`Nearest`、`Round`、`Simplest` 或 `Zero`。如果某个值无法用指定的数据类型和定标精确表示，模块将使用此参数指定的舍入方法将计算舍入为可表示的数字。有关详细信息，请参阅舍入 (Fixed-Point Designer)。

### **Saturate on integer overflow** — 整数溢出时饱和选项 off （默认） | on

对于定点计算，如果定点计算结果的幅值不适合存储结果的数据类型和定标的范围，请使用此参数指定要使用的方法。

- 要在整数溢出时饱和，请选择此参数。
- 要在整数溢出时绕回，请不要选择此参数。

有关详细信息，请参阅精度和范围。

**数据类型：** `Boolean`

### **Product Output** — 分集合并中分子部分的复数乘积 `Inherit: Inherit via internal rule` （默认） | `Inherit: Same as product output` | `fixdt(1,16,0)` | `<data type expression>`

分集合并中分子部分的复数乘积，指定为 `Inherit: Inherit via internal rule`、`Inherit: Same as product output`、`fixdt(1,16,0)` 或自定义 `<data type expression>`。有关详细信息，请参阅定点信号。

### **Accumulator** — 分集合并中分子部分的求和 `Inherit: Inherit via internal rule` （默认） | `Inherit: Same as product output` | `fixdt(1,16,0)` | `<data type expression>`

分集合并中分子部分的求和。必须保留求和结果以便进一步计算的定点模块通常允许您指定累加器的数据类型和定标。大多数此类模块在求和之前会转换为累加器数据类型：

显示每次加法结果仍保留在累加器数据类型中的过程

使用 **Accumulator >> Mode** 参数指定希望如何指定累加器的字长和小数长度：

- 当您选择 `Inherit via internal rule` 时，将自动为您计算累加器输出的字长和小数长度。有关详细信息，请参阅通过内部规则继承。
- 当您选择 `Same as product output` 时，这些特性与乘积输出的特性匹配。
- 当您选择 `Same as input` 时，这些特性与模块的第一个输入的特性匹配。
- 当您选择 `Binary point scaling` 时，可以输入累加器的字长和小数长度（以位为单位）。
- 当您选择 `Slope and bias scaling` 时，可以输入累加器的字长（以位为单位）和斜率。DSP System Toolbox™ 软件中所有信号的偏置均为零。

### **Energy product output** — 分母中的复数乘积 `Inherit: Inherit via internal rule` （默认） | `Inherit: Same as product output` | `fixdt(1,16,0)` | `<data type expression>`

用于计算 MIMO 信道中总能量的分母中的复数乘积，指定为 `Inherit: Inherit via internal rule`、`Inherit: Same as product output`、`fixdt(1,16,0)` 或自定义 `<data type expression>`。

### **Energy accumulator** — 用于计算 MIMO 信道中总能量的分母中的求和 `Inherit: Inherit via internal rule` （默认） | `Inherit: Same as accumulator` | `Inherit: Same as energy product output` | `fixdt(1,16,0)` | `<data type expression>`

用于计算 MIMO 信道中总能量的分母中的求和，指定为 `Inherit: Inherit via internal rule`、`Inherit: Same as accumulator`、`Inherit: Same as energy product output`、`fixdt(1,16,0)` 或自定义 `<data type expression>`

### **Division output** — 按 MIMO 信道总能量归一化的分集合并 `Inherit: Same as accumulator` | `fixdt(1,16,0)` | `<data type expression>`

按 MIMO 信道总能量归一化的分集合并，指定为 `Inherit: Same as accumulator`、`fixdt(1,16,0)` 或自定义 `<data type expression>`。

## 所属库

Communications Toolbox / MIMO

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed pointa` | `single` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
|  |  |
| --- | --- |
| a 仅限有符号。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009a 中引入**

## 描述

使用正交空时分组码合并输入

OSTBC Combiner 模块合并输入信号（来自所有接收天线）和信道估计信号，以提取由正交空时分组码 (OSTBC) 编码的符号的软信息。输入信道估计不需要恒定，并且每次运行模块时都可以变化。合并算法仅使用每个码字块第一个符号周期的估计。多输入多输出 (MIMO) 通信系统在 OSTBC 合并过程之后应用符号解调或解码。

该模块独立地对每个符号执行合并操作。合并算法取决于 OSTBC 的结构。有关详细信息，请参阅 OSTBC 合并算法。
