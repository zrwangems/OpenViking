---
type: simulink-block
title: 'Combinatorial Logic'
family: logic-and-bit-operations
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'combinatoriallogic'
language: zh-CN
chinese_source: official
---

# Combinatorial Logic

实现真值表

## 所属库

Simulink / Logic and Bit Operations

## 描述

Combinatorial Logic 模块实现一个标准真值表，用于建模可编程逻辑数组 (PLA)、逻辑电路、决策表和其他布尔表达式。您可以将此模块与 Memory 模块一起使用，以实现有限状态机或触发器。

**提示**

要以编程方式将此模块添加到名为 `untitled` 的模型，请使用命令，例如：

```
open_system(new_system);
add_block(sprintf('simulink/Logic and Bit\nOperations/Combinatorial \nLogic'),...
'untitled/Combinatorial Logic');
```

## 端口

### 输入

### **Port\_1** — 输入信号 向量

输入信号，指定为向量。Combinatorial Logic 模块接受的信号类型取决于您是否选择了“布尔逻辑信号”选项（请参阅将逻辑信号实现为布尔数据(而不是双精度数据)）。如果启用了此选项，则模块接受 `Boolean` 或 `double` 类型的实信号。

**数据类型:** `double` | `Boolean`
### 输出

### **Port\_2** — 输出信号 标量 | 向量

输出信号，如果真值表中包含 `double` 类型的非布尔值，则类型为 `double`；否则类型为 `Boolean`。如果输入为 `Boolean` 且真值表包含非布尔值，则输出的类型与输入相同，除非模块输出 `double`。

**数据类型:** `double` | `Boolean`

## 参数

### **真值表** — 输出矩阵 矩阵

您指定一个矩阵，将所有可能的模块输出定义为**真值表**参数。此矩阵的每一行包含一个不同输入元素组合的输出。您必须为每个输入组合指定输出。列数等于模块输出数。

**真值表**参数可以具有任何数据类型的布尔值（0 或 1），包括定点数据类型。如果表中包含非布尔值，表的数据类型必须是 `double`。

输入数目与行数之间的关系为：

`number of rows = 2(number of inputs)`

Simulink® 通过计算来自输入向量元素的行索引，返回矩阵的一行。Simulink 通过生成一个二进制数字（具有零值的输入向量元素为 0，具有非零值的元素为 1），然后将结果加上 1 来计算索引。对于输入向量，`m` 元素的 `u` 为：

`row index = 1 + u(m)*2`0 `+ u(m-1)*2`1 `+ ... + u(1)*2`m-1

#### 编程用法

|  |
| --- |
| **模块参数**：`TruthTable` |
| **类型**：字符向量 |
| **值**：矩阵 |
| **默认值**：`'[0 0;0 1;0 1;1 0;0 1;1 0;1 0;1 1]'` |

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` |
| **直接馈通** | `是` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史记录

**在 R2006a 之前推出**
