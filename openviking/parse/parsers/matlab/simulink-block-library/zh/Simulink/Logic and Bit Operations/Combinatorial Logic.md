---
type: simulink-block
title: 'Combinatorial Logic'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'combinatoriallogic'
documentation_source_path: 'slref/combinatoriallogic.html'
language: zh-CN
chinese_source: worker-translation
---

# Combinatorial Logic

## 端口

### 输入

### **Port\_1** — 输入信号向量

输入信号，指定为向量。Combinatorial Logic 模块接受的信号类型取决于您是否选择了 Boolean logic signals 选项（请参阅 Implement logic signals as Boolean data (vs. double)）。如果启用此选项，该模块接受类型为 `Boolean` 或 `double` 的实数信号。

**数据类型：** `double` | `Boolean`
### 输出

### **Port\_2** — 输出信号 标量 | 向量

输出信号，如果真值表包含类型为 `double` 的非布尔值，则为 `double`；否则为 `Boolean`。输出的类型与输入的类型相同，除非输入为 `Boolean` 且真值表包含非布尔值，此时模块输出 `double`。

**数据类型：** `double` | `Boolean`

## 参数

### **Truth table** — 输出矩阵 矩阵

您需要指定一个矩阵，将所有可能的模块输出定义为 **Truth table** 参数。矩阵的每一行包含不同输入元素组合对应的输出。您必须为每一种输入组合指定输出。列数即为模块输出的数量。

**Truth table** 参数可以具有任意数据类型的布尔值（0 或 1），包括定点数据类型。如果表包含非布尔值，则表的数据类型必须为 `double`。

输入数量与行数之间的关系为：

`number of rows = 2(number of inputs)`

Simulink® 通过根据输入向量元素计算行的索引来返回矩阵的某一行。Simulink 通过构建一个二进制数来计算索引，其中值为零的输入向量元素为 0，非零值的元素为 1，然后在结果上加 1。对于包含 `m` 个元素的输入向量 `u`：

`row index = 1 + u(m)*2`0 `+ u(m-1)*2`1 `+ ... + u(1)*2`m-1

#### 编程使用

|  |
| --- |
| **模块参数**：`TruthTable` |
| **类型**：character vector |
| **值**：matrix |
| **默认值**：`'[0 0;0 1;0 1;1 0;0 1;1 0;1 0;1 1]'` |

## 所属库

Simulink / Logic and Bit Operations

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

实现真值表

Combinatorial Logic 模块实现标准真值表，用于对可编程逻辑阵列（PLA）、逻辑电路、决策表和其他布尔表达式进行建模。您可以将此模块与 Memory 模块结合使用，以实现有限状态机或触发器。

**提示**

要以编程方式将此模块添加到名为 `untitled` 的模型中，请使用如下命令：

```
open_system(new_system);
add_block(sprintf('simulink/Logic and Bit\nOperations/Combinatorial \nLogic'),...
'untitled/Combinatorial Logic');
```
