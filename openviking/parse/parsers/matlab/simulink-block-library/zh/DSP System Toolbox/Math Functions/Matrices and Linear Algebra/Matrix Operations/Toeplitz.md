---
type: simulink-block
title: 'Toeplitz'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Matrix Operations'
documentation_page: 'toeplitz'
documentation_source_path: 'ref/toeplitz.html'
language: zh-CN
chinese_source: worker-translation
---

# Toeplitz

## 端口
```yaml
ports:
- name: Input
  summary: 输入向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
- name: Toep Col
  summary: 非对称 Toeplitz 矩阵的第一列 向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
- name: Toep Row
  summary: 非对称 Toeplitz 矩阵的第一行 向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
- name: Output
  summary: Toeplitz 矩阵 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
```

### 输入

### **Input** — 输入向量

当您选中 **Symmetric** 复选框时，模块根据输入 `u` 生成对称（或 Hermitian）Toeplitz 矩阵。该单一输入同时定义 Toeplitz 矩阵的第一行和第一列。

以下是等效的 MATLAB® 代码。

```
y = toeplitz(u)
```

输出 *y* 的维度为 [`length`(`u`) `length`(`u`)]。例如，由输入向量 `[1 2 3 4]` 生成的 Toeplitz 矩阵为

[1234212332124321]

#### 依赖关系

要启用此端口，请选中 **Symmetric** 复选框。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**复数支持：** 是

### **Toep Col** — 非对称 Toeplitz 矩阵的第一列 向量

非对称 Toeplitz 矩阵的第一列，指定为向量。

#### 依赖关系

要启用此端口，请清除 **Symmetric** 复选框。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**复数支持：** 是

### **Toep Row** — 非对称 Toeplitz 矩阵的第一行 向量

非对称 Toeplitz 矩阵的第一行，指定为向量。

#### 依赖关系

要启用此端口，请清除 **Symmetric** 复选框。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**复数支持：** 是
### 输出

### **Output** — Toeplitz 矩阵 矩阵

Toeplitz 矩阵，以矩阵形式返回。模块根据 **Symmetric** 复选框的设置生成此矩阵。

当您选中 **Symmetric** 复选框时，模块根据定义矩阵第一行和第一列的单一输入 `u` 生成对称（或 Hermitian）Toeplitz 矩阵。

以下是等效的 MATLAB 代码。

```
y = toeplitz(u)
```

输出的维度为 [`length`(`u`) `length`(`u`)]。例如，由输入向量 `[1 2 3 4]` 生成的 Toeplitz 矩阵为

[1234212332124321]

当您未选中 **Symmetric** 复选框时，Toeplitz 模块根据定义第一列和第一行的输入生成 Toeplitz 矩阵。顶部输入（`Toep Col`）是包含要放置在矩阵第一列中的值的向量，底部输入（`Toep Row`）是包含要放置在矩阵第一行中的值的向量。

以下是等效的 MATLAB 代码。

```
y = toeplitz(Toep Col,Toep Row)
```

矩阵的其他元素遵循以下关系：

```
y(i,j) = y(i-1,j-1)
```

输出的维度为 [`length`(`Toep Col`) `length`(`Toep Row`)]。*y*(1,1) 元素继承自 `Toep Col` 输入。例如，以下输入

```
Toep Col = [1 2 3 4 5]
```

```
Toep Row = [7 7 3 3 2 1 3]
```

生成 Toeplitz 矩阵

[17332132173321321733243217335432173]

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Symmetric
  summary: 对称 Toeplitz 矩阵输出 on（默认）| off
  group: ''
- name: Saturate on integer overflow
  summary: 整数溢出时饱和 on（默认）| off
  group: ''
```

### **Symmetric** — 对称 Toeplitz 矩阵输出 `on`（默认）| `off`

当您选中 **Symmetric** 复选框时，模块根据定义矩阵第一行和第一列的单一输入 `u` 生成对称（Hermitian）Toeplitz 矩阵。

以下是等效的 MATLAB 代码。

```
y = toeplitz(u)
```

当您未选中 **Symmetric** 复选框时，Toeplitz 模块根据定义第一列 `Toep Col` 和第一行 `Toep Row` 的输入生成 Toeplitz 矩阵。

以下是等效的 MATLAB 代码。

```
y = toeplitz(Toep Col,Toep Row)
```

矩阵的其他元素遵循以下关系：

```
y(i,j) = y(i-1,j-1)
```

有关详细信息，请参阅 **Output** 端口描述。

### **Saturate on integer overflow** — 整数溢出时饱和 `on`（默认）| `off`

当您使用此模块生成对称 Toeplitz 矩阵时，如果输入向量为复数，则输出为对称 Hermitian 矩阵，其元素满足以下关系：

y(i,j)=conj(y(j,i))

对于定点信号，共轭运算可能导致溢出。当您选中此参数时，溢出将饱和。对于浮点信号，此参数被忽略。

#### 依赖关系

要启用此参数，请选中 **Symmetric** 复选框。
## 所属库

DSP System Toolbox / Math Functions / Matrices and Linear Algebra / Matrix Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

生成具有 Toeplitz 对称性的矩阵

根据输入生成对称或非对称 Toeplitz 矩阵。如果您选中 **Symmetric** 复选框，模块生成对称（或 Hermitian）Toeplitz 矩阵。如果您未选中 **Symmetric** 复选框，模块生成非对称 Toeplitz 矩阵。列和行分别由第一个和第二个输入指定。第一个矩阵元素继承自列。
