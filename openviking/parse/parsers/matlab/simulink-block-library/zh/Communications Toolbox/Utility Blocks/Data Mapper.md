---
type: simulink-block
title: 'Data Mapper'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Utility Blocks'
documentation_page: 'datamapper'
documentation_source_path: 'ref/datamapper.html'
language: zh-CN
chinese_source: worker-translation
---

# Data Mapper

## 端口

### 输入

### **In** — 输入信号 标量 | 列向量 | 矩阵

输入信号，指定为整数标量、向量或矩阵。
输入信号的元素必须为非负值。该模块将非整数值截断为整数值。当输入为
矩阵时，各列被视为独立通道。

**数据类型：** `double` | `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### 输出

### **Out** — 输出信号 标量 | 列向量 | 矩阵

输出信号，以标量、列向量或矩阵形式返回。输出信号的
维度与输入信号的维度一致。

**数据类型：** `double` | `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## 参数

要以交互方式编辑模块参数，请使用
属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在
**Prepare** 库中，选择 **Property
Inspector**。

### **Mapping mode** — 映射模式 `Binary to Gray`（默认）| `Gray to Binary` | `User Defined` | `Straight through`

映射模式，指定为 `Binary to Gray`、
`Gray to Binary`、`User
Defined` 或 `Straight through`。
此表显示了输入在范围 [0, 7] 内时 `Binary to
Gray` 和 `Gray to Binary`
模式的映射。

| Binary to Gray 模式 | | Gray to Binary 模式 | |
| --- | --- | --- | --- |
| 输入 | 输出 | 输入 | 输出 |
| 0 | 0 *(000)* | 0 *(000)* | 0 |
| 1 | 1 *(001)* | 1 *(001)* | 1 |
| 2 | 3 *(011)* | 2 *(010)* | 3 |
| 3 | 2 *(010)* | 3 *(011)* | 2 |
| 4 | 6 *(110)* | 4 *(100)* | 7 |
| 5 | 7 *(111)* | 5 *(101)* | 6 |
| 6 | 5 *(101)* | 6 *(110)* | 4 |
| 7 | 4 *(100)* | 7 *(111)* | 5 |

当您选择 `User Defined` 模式时，您可以通过提供一个向量来指定输出
顺序，从而使用任意映射。当您选择 `Straight through`
模式时，输出等于输入。

### **Symbol set size (M)** — 符号集大小 `8`（默认）| 正整数

符号集大小，指定为正整数。此参数将
输入和输出限制为范围 [0, (M – 1)] 内的整数。

### **Mapping vector** — 将输入元素映射到输出元素 `[0 1 3 2 7 6 4 5]`（默认）| 向量

映射向量，指定为非负整数向量，其长度
等于输入端口 **In** 处输入信号的长度。此参数定义
输入和输出整数之间的关系。例如，向量 `[1 5 0 4 2 3]` 定义以下
映射：

0→11→52→03→44→25→3

## 所属库

Communications Toolbox / Utility Blocks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

将整数符号从一种编码方案映射到另一种编码方案

Data Mapper 模块接受整数输入并将其映射为整数
输出。映射类型包括：二进制到格雷码、格雷码到二进制以及用户
定义。此外，还提供直通选项。

格雷编码是二进制数的一种排序方式，使得所有相邻数字仅相差
一位。
