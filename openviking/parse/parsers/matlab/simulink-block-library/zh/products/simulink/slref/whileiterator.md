---
type: simulink-block
title: 'While Iterator'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Modeling / Design Model Behavior / Iterator Subsystems'
documentation_page: 'whileiterator'
documentation_source_path: 'slref/whileiterator.html'
language: zh-CN
chinese_source: official
---

# While Iterator

## 端口

### 输入

### **cond** — 逻辑条件信号 标量

从逻辑条件计算出结果的信号。由于子系统在时间步内不是通过外部触发的，因此结果为 true (`1`) 或 false (`0`) 的条件计算必须在子系统内进行。

信号的数据类型和值可以是：

- 逻辑（布尔）值 - true (`1`) 或 false (`0`)。
- 数值 - true（任何正数或负数）或 false (`0`)。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **IC** — 初始逻辑条件 标量

带有初始逻辑条件的信号。在每个时间步的开始：

- 如果 `IC` 为 false (`0`)，则子系统在时间步内不执行。
- 如果 `IC` 为 true（值不等于 `0`），则子系统开始执行并且只要 `cond` 信号为 true 就继续重复执行。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
### 输出参量

### **Iteration number** — 带有迭代次数的信号 标量

带有 While Iterator Subsystem 模块在每个时间步内执行次数的信号。

**数据类型:** `double` | `int8` | `int16` | `int32`

## 参数

### **最大迭代次数** — 指定最大迭代次数 `-1` (默认) | 整数

指定在一个时间步内允许的最大迭代次数。

`-1`
:   只要 `cond` 信号为 true（值不等于 `0`），则允许任意迭代次数。如果您指定 `-1` 并且 `cond` 信号永不变为 false (`0`)，则仿真以无限循环方式运行。在这种情况下，停止仿真的唯一方法就是终止 MATLAB®。

整数
:   一个时间步内的最大迭代次数。

#### 编程用法

|  |
| --- |
| **模块参数**：`MaxIters` |
| **类型**：字符向量 |
| **值**：`'5'` | `'-1'` | 用引号引起来的整数 |
| **默认值**：`'5'` |

### **while 循环类型** — 选择模块类型 **while** (默认) | **do-while**

选择模块类型。

**while**
:   While Iterator 模块有两种输入：`cond`（逻辑条件）输入和 `IC`（初始逻辑条件）输入。`IC` 信号的信源必须在 While Iterator Subsystem 模块的外部。

    在每个时间步的开始：

    - 如果 `IC` 输入为 true（值不等于 `0`），则在 `cond` 输入为 true 时子系统中的模块将重复执行。只要 `cond` 输入为 true 且迭代次数小于或等于**最大迭代次数**，此过程就会在时间步内继续。
    - 如果 `IC` 输入为 false，则 While Iterator 模块不执行子系统的内容。

**do-while**
:   While Iterator 模块有一个输入，即 `cond`（while 条件）输入。

    在每个时间步中，只要 `cond` 输入为 true（值不等于 `0`），子系统中的模块就会重复执行。只要 `cond` 输入为 true，且迭代次数小于或等于**最大迭代次数**，此过程就会一直继续。

#### 编程用法

|  |
| --- |
| **模块参数**：`WhileBlockType` |
| **类型**：字符向量 |
| **值**：`'while'` | `'do-while'` |
| **默认值**：`'while'` |

### **开始时的状态** — 选择时间步之间的模块状态 **保持** (默认) | **重置**

选择如何处理时间步之间的模块状态。

**保持**
:   在时间步之间保持模块状态。模块状态值跨时间步保持不变。

**重置**
:   在每个时间步的开始和第一个迭代循环之前，将模块状态重置为其初始值。

#### 编程用法

|  |
| --- |
| **模块参数**：`ResetStates` |
| **类型**：字符向量 |
| **值**：`'held'` | `'reset'` |
| **默认值**：`'held'` |

### **显示迭代序号端口** — 控制输出端口的显示 `off` | `on`

控制是否为带有模块执行次数的信号显示输出端口。来自此端口的信号的值从 `1` 开始，随后每次迭代递增 `1`。

off
:   删除输出端口。

on
:   为带有迭代序号的信号显示输出端口。

#### 依赖关系

选择此参数将启用**输出数据类型**参数。

#### 编程用法

|  |
| --- |
| **模块参数**：`ShowIterationPort` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **输出数据类型** — 选择当前迭代序号的输出数据类型 **int32** (默认) | **uint32** | **int16** | **uint16** | **int8** | **uint8** | **double**

选择迭代序号信号的输出数据类型。此信号的值是在一个时间步内的迭代次数以及在时间步结束时的总迭代次数。信号允许的最大值由**输出数据类型**参数确定。例如，如果您将**输出数据类型**设置为 **int8**，则信号允许的最大值为 27-1。但是，如果将**输出数据类型**设置为 **uint32** 或 **double**，则信号允许的最大值将限制为有符号 32 位整数 (`int32`) 的最大正值。有关不同整数类的值范围的详细信息，请参阅整数。

**int32**
:   有符号 32 位整数。

**uint32**
:   无符号 32 位整数。

**int16**
:   有符号 16 位整数。

**uint16**
:   无符号 16 位整数。

**int8**
:   有符号 8 位整数。

**uint8**
:   无符号 8 位整数。

**double**
:   双精度浮点。

#### 依赖关系

选中**显示迭代序号端口**复选框可启用此参数。

#### 编程用法

|  |
| --- |
| **模块参数**：`OutputDataType` |
| **类型**：字符向量 |
| **值**：`'int32'` | `'unt32'`|`'int16'` | `'uint16'`|`'int8'` | `'uint8'`|`'double'` |
| **默认值**：`'int32'` |

## 所属库

R2025b 官方文档未提供。

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2006a 之前推出**

### R2024b: 将信号断点和端口值标签添加到迭代子系统中的迭代序号输出

现在，您可以在迭代子系统的特定迭代上暂停仿真，方法是将信号断点添加到由以下各项产生的信号中：

- While Iterator Subsystem 模块内 While Iterator 模块的迭代序号输出端口
- For Iterator Subsystem 模块内 For Iterator 模块的迭代器值输出端口
- For Each Subsystem 模块内 For Each 模块的分区索引输出端口

在以前的版本中，您可以在这些位置添加断点，但断点不会暂停仿真，并且在模块图中显示为无效。

相同位置的端口值标签现在显示迭代序号。在以前的版本中，这些位置的端口值标签显示 `inaccessible`。

有关示例，请参阅Debug Simulation of Iterator Subsystem。

## 描述

While Iterator 子系统的控制模块

将 While Iterator 模块置于 Subsystem 模块中时，它将在输入条件的值为 true 或 `1` 时在当前时间步中重复执行子系统的内容。使用此模块实现与编程语言中的 `while` 循环等效的模块图。

While Iterator Subsystem 模块使用 While Iterator 模块进行了预配置。将 While Iterator 模块放置在 Subsystem 模块中会使其成为原子子系统。
