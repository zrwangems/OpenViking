---
type: simulink-block
title: 'Scalar Quantizer Encoder'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Quantizers'
documentation_page: 'scalarquantizerencoder'
documentation_source_path: 'ref/scalarquantizerencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Scalar Quantizer Encoder

## 端口

### 输入

### **U** — 输入数据值 向量 | 矩阵

将输入数据值指定为向量或矩阵。

输入数据、边界点、码本值、量化输出值和量化误差在存在时必须具有相同的数据类型。

如果输入为定点，则它必须是有符号整数，或具有 2 的幂斜率且零偏置的有符号定点值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **B** — 边界点 向量

将边界点指定为长度为 *N* 的向量。必须按升序输入边界点。

输入数据、边界点、码本值、量化输出值和量化误差在存在时必须具有相同的数据类型。

#### 依赖关系

要启用此端口，请从 **Source of quantizer parameters** 列表中选择 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **C** — 码本值 向量

输入与每个索引值对应的量化输出值向量。码本向量的长度必须为 *N*−1，其中 *N* 是边界点向量的长度。

输入数据、边界点、码本值、量化输出值和量化误差在存在时必须具有相同的数据类型。

#### 依赖关系

要启用此端口，请从 **Source of quantizer parameters** 列表中选择 `Input port`，并且选择 **Output codeword** 或 **Output quantization error** 复选框。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### 输出

### **I** — 索引值 向量 | 矩阵

索引值，返回为与输入数据大小相同的向量或矩阵。

此端口的数据类型取决于 **Index output data type** 参数的设置。

**数据类型：** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Q(U)** — 量化输出值 向量 | 矩阵

量化输出值，返回为与输入数据大小相同的向量或矩阵。这些是与每个索引值对应的码字值。

输入数据、边界点、码本值、量化输出值和量化误差在存在时必须具有相同的数据类型。

#### 依赖关系

要启用此端口，请选择 **Output codeword** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **Err** — 量化误差 向量 | 矩阵

量化误差，返回为与输入数据大小相同的向量或矩阵。量化误差是输入值与量化输出值之间的差。

输入数据、边界点、码本值、量化输出值和量化误差在存在时必须具有相同的数据类型。

#### 依赖关系

要启用此端口，请选择 **Output quantization error** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **S** — 削波状态 向量 | 矩阵

削波状态值，返回为与输入数据大小相同的布尔值向量或矩阵。只要输入值超出 **Boundary points** 参数定义的范围，模块就会在 **S** 端口输出 1。当该值在范围内时，模块输出 0。

#### 依赖关系

要启用此端口，请选择 **Output clipping status** 复选框。

**数据类型：** `Boolean`

## 参数

### 主选项卡

### **Source of quantizer parameters** — 量化器参数的来源 `Specify via dialog`（默认） | `Input port`

将量化器参数的来源指定为以下之一：

- `Specify via dialog` –– 使用对话框中的参数输入边界点和码本值。
- `Input port` –– 使用模块输入端口指定参数。分别使用端口 **B** 和 **C** 输入边界点和码本值。

### **Partitioning** — 分区方法 `Bounded`（默认） | `Unbounded`

指定以下分区方法之一来解释输入的边界点：

- `Bounded` –– 选择此选项可创建有界量化器。

  例如，当输入以下边界点时：

  ```
  [0 0.5 3.7 5.8 6.0 11]
  ```

  模块将 0 到 0.5 之间的任何输入值分配给索引 0，将 0.5 到 3.7 之间的输入值分配给索引 1，依此类推。模块将小于 0 的任何值分配给索引 0，即最低索引值。模块将大于 11 的任何值分配给索引 4，即最高索引值。
- `Unbounded` –– 选择此选项可创建无界量化器。

  例如，当输入以下边界点时：

  ```
  [0 0.5 3.7 5.8 6.0 11]
  ```

  模块将 0 到 0.5 之间的任何输入值分配给索引 1，将 0.5 到 3.7 之间的输入值分配给索引 2，依此类推。模块将小于 0 的任何输入值分配给索引 0，将大于 11 的任何值分配给索引 6。

### **Boundary points** — 边界点 `[1:10]`（默认） | vector

输入按升序排列的值向量，这些值表示量化器区域的边界点。这些值用于将输入数字集合划分为区域。每个区域由索引号指定。

令 *N* 为量化区域的数量。当码本定义为 `[c1 c2 c3 ... cN]`，并且 **Boundary points** 参数定义为 `[p0 p1 p2 p3 ... pN]` 时，则对于规则量化器，`p0<c1<p1<c2 ... p(N-1)<cN<pN`。当量化器为有界时，从 **Partitioning** 列表中选择 `Bounded`。需要指定 *N*+1 个边界点，即 `[p0 p1 p2 p3 ... pN]`。当量化器为无界时，从 **Partitioning** 列表中选择 `Unbounded`。需要指定 *N*−1 个边界点，即`[p1 p2 p3 ... p(N-1)]`。模块将 `p0` 设置为 −`inf`，将 `pN` 设置为 `inf`。

**可调：** 是

#### 依赖关系

要启用此参数，请从 **Source of quantizer parameters** 列表中选择 `Specify via dialog`。

### **Searching method** — 搜索方法 `Linear`（默认） | `Binary`

指定模块用于确定输入值所在区域（量化器索引）的搜索方法：

- `Linear` –– 模块将输入值与由前两个边界点定义的第一个区域进行比较。当输入值不在此区域内时，模块接着将输入值与下一个区域进行比较。此过程持续进行，直到确定输入值位于某个区域内并关联到相应的索引值。此过程的计算成本为 *P* 阶，其中 *P* 是边界点的数量。
- `Binary` –– 模块将输入值与边界点向量的中间值进行比较。当输入值大于此边界点时，模块丢弃低于此中间值的边界点。然后，模块将输入值与由剩余边界点定义的新范围的中间边界点进行比较。此过程持续进行，直到输入值关联到相应的索引值。此过程的计算成本为 log2*P* 阶，其中 *P* 是边界点的数量。在大多数情况下，`Binary` 选项比 `Linear` 选项更快。

### **Tie-breaking rule** — 当输入值与边界点相同时的操作 `Choose the lower index`（默认） | `Choose the higher index`

指定当输入值与边界点相同时要采取的以下操作之一。此参数确定将该值分配到哪个区域。

- `Choose the lower index` –– 模块将输入值分配到索引较低的区域。
- `Choose the higher index` –– 模块将输入值分配到索引较高的区域。

### **Output codeword** — 输出码字 `off`（默认） | `on`

选择此复选框可在端口 **Q(U)** 输出与每个索引值对应的码字值。

### **Output quantization error** — 输出量化误差 `off`（默认） | `on`

选择此复选框可在端口 **Err** 输出每个输入值的量化误差。量化误差是输入值与量化输出值之间的差。

### **Codebook** — 量化输出值 `[1.5:9.5]`（默认） | vector

输入与每个索引值对应的量化输出值向量。

如果将 **Partitioning** 参数设置为 `Bounded`，并且边界点向量的长度为 *N*，则必须指定长度为 *N*−1 的码本。如果将 **Partitioning** 参数设置为 `Unbounded`，并且边界点向量的长度为 *N*，则必须指定长度为 *N*+1 的码本。

**可调：** 是

#### 依赖关系

要启用此参数，请从 **Source of quantizer parameters** 列表中选择 `Specify via dialog`，并选择 **Output codeword** 或 **Output quantization error** 复选框。

### **Output clipping status** — 输出削波状态 `off`（默认） | `on`

指定端口 **S** 上的输出削波状态。只要输入值超出 **Boundary points** 参数定义的范围，模块就会在此端口输出 1。当该值在范围内时，模块输出 0。

#### 依赖关系

要启用此参数，请将 **Partitioning** 参数设置为 `Bounded`。

### **Action for out of range input** — 超出范围输入的操作 `Clip` | `Clip and warn` | `Error`

指定当输入值超出 **Boundary points** 参数定义的范围时模块必须采取的以下操作之一：

- `Clip`
- `Clip and warn`
- `Error`

假设有界量化器的边界点定义为 `[p0 p1 p2 p3 ... pN]`，可能的索引值定义为 `[i0 i1 i2 ... i(N-1)]`，其中 `i0=0` 且 `i0<i1<i2<...<i(N-1)`。当希望将小于 `p0` 的任何输入值分配给索引值 `i0`，并将大于 `pN` 的任何输入值分配给索引值 `i(N-1)` 时，选择 `Clip`。当希望在发生削波时得到警告时，选择 `Clip and warn`。当希望在索引值超出范围时停止仿真并让模块显示错误时，选择 `Error`。

#### 依赖关系

要启用此参数，请将 **Partitioning** 参数设置为 `Bounded`。

### **Index output data type** — 索引输出数据类型 `int32`（默认） | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `Inherit via back propagation`

将端口 **I** 上来自模块的索引输出的数据类型指定为以下之一：

- `int8`
- `uint8`
- `int16`
- `uint16`
- `int32`
- `uint32`
- `Inherit via back propagation`

### 数据类型选项卡

### **Rounding mode** — 舍入模式 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

将定点运算的舍入模式指定为以下之一：

- `Floor`
- `Ceiling`
- `Convergent`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

有关更多详细信息，请参阅舍入模式。

### **Saturate on integer overflow** — 整数溢出时饱和 `off`（默认） | `on`

当选择此参数时，模块将对其定点运算的结果进行饱和处理。当清除此参数时，模块将对其定点运算的结果进行环绕处理。有关 `saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出模式。

## 所属库

DSP System Toolbox / Quantizers

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

通过将每个输入值与量化区域的索引值关联来编码每个输入值

Scalar Quantizer Encoder 模块通过将输入值与 **Boundary points** 参数中定义的量化器边界点进行比较，将每个输入值映射到量化区域。模块输出关联区域的从零开始的索引。
