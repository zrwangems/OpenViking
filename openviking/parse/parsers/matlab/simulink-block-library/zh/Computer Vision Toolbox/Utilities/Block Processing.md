---
type: simulink-block
title: 'Block Processing'
family: 'utilities'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'blockprocessing'
documentation_source_path: 'ref/blockprocessing.html'
language: zh-CN
chinese_source: worker-translation
---

# Block Processing

## 端口

### 输入

### **I** — 输入信号矩阵

输入信号，指定为 *M*×*N* 矩阵。除非您选择 **Add port to supply subsystem parameters** 参数或将 **Number of inputs** 参数设置为 `2` 或更大，否则此端口未命名。如果选择 **Add port to supply subsystem parameters** 参数，则端口名称变为 **I**。如果将 **Number of inputs** 设置为大于 `1` 的值 *n*，则该模块具有从 **I** 到 **In** 的 *n* 个输入端口。子系统的内容决定输入数据的数据类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**复数支持：** 是

### **P** — 用于供给子系统参数的附加输入 标量 | 向量 | 矩阵 | 数组

用于供给子系统参数的附加输入，指定为标量、向量、矩阵或数组。子系统的内容决定输入数据的数据类型。

#### 依赖关系

要启用此端口，必须选择 **Add port to supply subsystem parameters** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `string`
### 输出

### **Port\_1** — 输出信号矩阵

输出数据，以矩阵形式返回。**Number of outputs** 的值决定输出端口的数量。子系统的内容决定输出数据的数据类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**复数支持：** 是

## 参数

### **Number of inputs** — 输入数量 `1` (默认) | 正标量

将 Block Processing 模块的输入端口数量指定为正标量。

### **Add port to supply subsystem parameters** — 子系统参数输入端口 `off` (默认) | `on`

选择此参数可向 Block Processing 模块添加一个附加输入端口，用于供给子系统参数。

### **Number of outputs** — 输出数量 `1` (默认) | 正标量

将 Block Processing 模块上的输出端口数量指定为正标量。

### **Block size** — 块大小 `{[8 8]}` (默认) | 元胞数组

将每个块的大小指定为包含二元素向量的元胞。元胞数组必须包含单个元胞或针对每个输入端口的一个元胞。如果模块有一个输入端口，则只输入一个向量。如果模块有多个输入端口，则可以输入一个向量以用于所有输入，也可以为每个输入指定单独的向量。模块按您输入向量的顺序使用这些向量。

### **Overlap** — 块重叠 `{[0 0]}` (默认) | 元胞数组

将每个块的重叠指定为包含二元素向量的元胞。元胞数组必须包含单个元胞或针对每个输入端口的一个元胞。如果模块有一个输入端口，则只输入一个向量。如果模块有多个输入端口，则可以输入一个向量以用于所有输入，也可以为每个输入指定单独的向量。模块按您输入向量的顺序使用这些向量。

### **Traverse order** — 块提取顺序 `Row-wise` (默认) | `Column-wise`

指定 Block Processing 模块从输入矩阵中提取子矩阵时采用的遍历顺序。如果选择 `Row-wise`，模块通过横向移动各行来提取子矩阵。如果选择 `Column-wise`，模块通过向下移动各列来提取子矩阵

**子系统**

要配置 Block Processing 模块的子系统。

- 点击 **Open Subsystem** 打开 Block Processing
  子系统。
- 将模块拖入此子系统，以定义该模块对子矩阵执行的处理操作。

## 所属库

Computer Vision Toolbox / Utilities

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Booleana` | `doublea` | `fixed pointa` | `integera` | `singlea` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
|  |  |
| --- | --- |
| a 子系统内的模块决定此模块支持的数据类型。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

对输入矩阵的块重复用户指定的操作

Block Processing 模块从输入矩阵中提取子矩阵（即 *块*），将每个块传递给执行用户指定操作的子系统。然后，它重新组装处理后的块以形成输出矩阵。您可以使用此模块逐块处理图像，而不是一次处理整个图像。矩阵块处理按以下顺序进行：从输入矩阵到提取的块，然后到子系统，然后将处理后的块重新组合为输出矩阵。
