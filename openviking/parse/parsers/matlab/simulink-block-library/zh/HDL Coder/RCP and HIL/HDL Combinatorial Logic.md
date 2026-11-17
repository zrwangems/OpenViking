---
type: simulink-block
title: 'HDL Combinatorial Logic'
family: 'rcp-and-hil'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'RCP and HIL'
documentation_page: 'hdlcombinatoriallogic'
documentation_source_path: 'ref/hdlcombinatoriallogic.html'
language: zh-CN
chinese_source: worker-translation
---

# HDL Combinatorial Logic

## 端口

### 输入

### **u** — 输入信号向量

输入信号，指定为向量。HDL Combinatorial Logic 模块接受的信号类型取决于您是否选择了 Boolean logic signals 选项（参见 Implement logic signals as Boolean data (vs. double)）。如果启用此选项，该模块接受 `Boolean` 或 `double` 类型的实数信号。

**数据类型：** `double` | `Boolean`
### 输出

### **v** — 输出信号标量 | 向量

输出信号，如果由 **Input table** 和 **Output table** 表示的真值表包含 `double` 类型的非 Boolean 值，则返回为 `double` 标量或向量；否则返回为 `Boolean` 标量或向量。输出类型与输入类型相同，但以下情况除外：如果输入为 `Boolean` 且真值表包含非 Boolean 值，则该模块输出 `double`。

**数据类型：** `double` | `Boolean`

## 参数

### **Input table** — 输入排列矩阵 matrix

**Input table** 参数可以具有任何数据类型的 Boolean 值（0 或 1），包括 fixed-point 数据类型。如果表中包含非 Boolean 值，则该表的数据类型必须为 `double`。

输入数量与行数之间的关系为：

number of rows = 2(number of inputs)

Simulink® 基于输入向量元素计算数值，从而返回由 **Output table** 指定的输出矩阵的一行。Simulink 通过构造一个二进制数来计算索引，其中值为零的输入向量元素为 0，非零值的元素为 1，然后将结果加 1。对于包含 `m` 个元素的输入向量 `u`：

row index = 1 +
*u*(*m*)×20+
*u*(*m*-1)×21+ ... +
*u*(1)×2m-1

#### 编程用法

|  |
| --- |
| **模块参数**: `inputTable` |
| **类型**: character vector |
| **值**: matrix |
| **默认值**: `logical([0 1; 1 0; 1 1])` |

### **Output table** — 输出矩阵 matrix

**Output table** 参数可以具有任何数据类型的 Boolean 值（0 或 1），包括 fixed-point 数据类型。如果表中包含非 Boolean 值，则该表的数据类型必须为 `double`。

#### 编程用法

|  |
| --- |
| **模块参数**: `outputTable` |
| **类型**: character vector |
| **值**: matrix |
| **默认值**: `logical([1 0; 1 0; 1 1])` |

## 所属库

HDL Coder / RCP and HIL

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### HDL 代码生成：使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

实现真值表

HDL Combinatorial Logic 模块实现标准真值表，用于对可编程逻辑阵列 (PLAs)、逻辑电路、决策表和其他 Boolean 表达式进行建模。您可以将此模块与 Memory 模块结合使用，以实现有限状态机或触发器。
