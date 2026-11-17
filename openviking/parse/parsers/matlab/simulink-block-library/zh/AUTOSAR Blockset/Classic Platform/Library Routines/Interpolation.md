---
type: simulink-block
title: 'Interpolation'
family: 'dsp'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Signal Operations'
documentation_page: 'interpolation'
documentation_source_path: '../dsp/ref/interpolation.html'
language: zh-CN
chinese_source: worker-translation
---

# Interpolation

## 端口
```yaml
ports:
- name: In
  summary: 输入信号 标量 | 向量 | 矩阵 | *N* 维数组
  direction: input
  data_types: single | double
- name: Pts
  summary: 插值点 标量 | 向量 | 矩阵 | *N* 维数组
  direction: input
  data_types: single | double
- name: Out
  summary: 输出信号 标量 | 向量 | 矩阵 | *N* 维数组
  direction: output
  data_types: single | double
```

### 输入

### **In** — 输入信号 标量 | 向量 | 矩阵 | *N* 维数组

输入信号，指定为标量、向量、矩阵或 *N* 维数组。

当 `Source of interpolation points` 设置为 `Input port` 之前，此端口未命名。

**数据类型：** `single` | `double`

### **Pts** — 插值点 标量 | 向量 | 矩阵 | *N* 维数组

插值点，指定为标量、向量、矩阵或 *N* 维数组。

有关当 `Source of interpolation points` 参数设置为 `Input port` 时模块行为的更多详细信息，请参阅 How the Block Applies Interpolation Arrays to Inputs。

#### 依赖关系

当 `Source of interpolation points` 设置为 `Input port` 之前，此端口不可用。

**数据类型：** `single` | `double`
### 输出

### **Out** — 输出信号 标量 | 向量 | 矩阵 | *N* 维数组

输出信号，指定为向量、矩阵或 *N* 维数组。

当 `Source of interpolation points` 设置为 `Input port` 之前，此端口未命名。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Source of interpolation points
  summary: 插值点输入方法 Specify via dialog（默认）| Input port
  group: ''
- name: Interpolation points
  summary: 插值点 [1.1 4.8 2.67 1.6 3.2]'（默认）| 标量 | 向量 | 矩阵 | *N* 维数组
  group: ''
- name: Interpolation mode
  summary: 插值模式 Linear（默认）| FIR
  group: ''
- name: Interpolation filter half-length
  summary: FIR 插值滤波器的半长度 3（默认）| 正整数
  group: ''
- name: Interpolation points per input sample
  summary: 每个输入采样的插值点数 3（默认）
  group: ''
- name: Normalized input bandwidth
  summary: 归一化输入带宽 0.5（默认）| (0 1] 范围内的标量
  group: ''
- name: Out of range interpolation points
  summary: 超出范围点的错误处理 Clip（默认）| Clip and warn | Error
  group: ''
```

### **Source of interpolation points** — 插值点输入方法 `Specify via dialog`（默认）| `Input port`

选择指定插值点的方式：

- `Specify via dialog` —— `Interpolation points` 参数变为可用。将此选项用于静态插值点。
- `Input port` —— 模块上出现 `Pts` 端口。模块将此端口的输入用作插值点。将此选项用于时变插值点。

有关更多信息，请参阅 Specifying Static Interpolation Points 和 Specifying Time-Varying Interpolation Points。

### **Interpolation points** — 插值点 `[1.1 4.8 2.67 1.6 3.2]'`（默认）| 标量 | 向量 | 矩阵 | *N* 维数组

对输入信号进行插值的时间点数组（*I*Pts）。*I*Pts 中的条目 1 指输入的第一个采样，条目 2.5 指第二个和第三个输入采样之间的中间采样，依此类推。请参阅 How the Block Applies Interpolation Arrays to Inputs。

**可调：** 是

#### 依赖关系

仅当 `Source of interpolation points` 设置为 `Specify via dialog` 时，此参数才可用。有关更多信息，请参阅 Specifying Static Interpolation Points。

### **Interpolation mode** — 插值模式 `Linear`（默认）| `FIR`

将模块设置为通过 `Linear` 或 `FIR` 插值进行插值。有关更多信息，请参阅 Linear Interpolation Mode 和 FIR Interpolation Mode。

### **Interpolation filter half-length** — FIR 插值滤波器的半长度 `3`（默认）| 正整数

指定 FIR 插值滤波器的半长度（`P`）。要以 `FIR` 模式执行插值，模块使用最近的 2×`P` 个低速率采样。在大多数情况下，每个插值点的下方和上方必须出现 `P` 个低速率采样。如果在低速率采样点处插值，模块将该低速率采样包含在所需的 2\*`P` 个采样中，并且仅需要 2\*`P`–1 个相邻低速率采样。如果某个插值点没有所需数量的相邻低速率采样，模块将使用线性插值对该点进行插值。

#### 依赖关系

仅当 `Interpolation mode` 设置为 `FIR` 时，此参数才可用。有关更多信息，请参阅 FIR Interpolation Mode。

### **Interpolation points per input sample** — 每个输入采样的插值点数 `3`（默认）

每个输入采样的点数，即*上采样因子*（`L`），模块在该点数处计算唯一的 FIR 插值滤波器。要执行 FIR 插值，模块使用具有 `L` 个长度为 2\*`P` 的滤波器支路的多相结构。

例如，如果 `L`=`4`，模块构造具有四个支路的多相滤波器。然后模块在对应于 1 +*i*/`L`、2 +*i*/`L`、3 +*i*/`L`... 的点处进行插值，其中整数 1、2 和 3 表示低速率采样，*i*=`0,1,2,3`。要在不直接对应于多相滤波器某个支路的点处进行插值，需要额外的计算。模块首先将该点向下舍入到确实对应于多相滤波器某个支路的最近值。要在点 2.2 处插值，模块将 2.2 向下舍入到 2，并使用多相滤波器结构的第一个支路计算 FIR 插值。类似地，要对点 2.65 进行插值，模块将该值向下舍入到 2.5，并使用多相滤波器结构的第三个支路。

#### 依赖关系

仅当 `Interpolation mode` 设置为 `FIR` 时，此参数才可用。有关更多信息，请参阅 FIR Interpolation Mode。

### **Normalized input bandwidth** — 归一化输入带宽 `0.5`（默认）| (0 1] 范围内的标量

输入带宽除以 Fs/2（输入采样频率的一半），指定为 (0 1] 范围内的标量。

#### 依赖关系

仅当 `Interpolation mode` 设置为 `FIR` 时，此参数才可用。有关更多信息，请参阅 FIR Interpolation Mode。

### **Out of range interpolation points** — 超出范围点的错误处理 `Clip`（默认）| `Clip and warn` | `Error`

插值数组 *I*Pts 中的有效值范围为 1 到输入每个通道中的采样数。例如，给定长度为 5 的输入向量 `D`，*I*Pts 的所有条目必须在 1 到 5 的范围内。*I*Pts 不能包含诸如 7 或 -9 之类的条目，因为 `D` 中没有第 7 个或第 -9 个条目。

**Out of range interpolation points** 参数设置模块如何处理超出有效范围的插值点。该参数具有以下设置：

- `Clip` —— 模块将 *I*Pts 中任何超出范围的值替换为有效范围内（从 1 到输入采样数）的最近值，然后使用 *I*Pts 的裁剪版本继续计算。
- `Clip and warn` —— 除 `Clip` 外，模块每次发生裁剪时在 MATLAB® 命令行发出警告。
- `Error` —— 当模块在 *I*Pts 中遇到超出范围的值时，仿真停止，模块在 MATLAB 命令行发出错误。

作为裁剪的示例，假设模块设置为裁剪超出范围的插值点，并获得以下输入向量和插值点：

- `D = [11 22 33 44]'`
- `IPts = [10 2.6 -3]'`

由于 *D* 有四个采样，有效插值点范围为 1 到 4。模块将插值点 10 裁剪为 4，将点 -3 裁剪为 1，得到裁剪后的插值向量 `IPtsClipped = [4 2.6 1]'`。
## 所属库

DSP System Toolbox / Signal Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

对实数输入采样值进行插值

Interpolation 模块使用线性或 FIR 插值对离散实数输入进行插值。该模块接受向量、矩阵或 *N* 维数组。模块输出插值后的标量、向量、矩阵或 *N* 维数组。

您必须指定插值点，即在基于一的插值数组 *I*Pts 中要插值的时间。*I*Pts 中的条目 1 指输入数据的第一个采样，条目 2.5 指第二个和第三个输入采样之间的中间采样，依此类推。根据输入数据的维度，*I*Pts 可以是标量、长度为 *P* 的行或列向量、*P*×*N* 矩阵，或 *N* 维数组，其中 *P* 是 *N* 维数组第一维的大小。在大多数情况下，*P* 可以是任何正整数。有关有效插值数组的更多信息，请参阅 Pts 和 Interpolation points 中的表格。

在大多数情况下，模块将 *I*Pts 应用于 *N* 维输入数组的第一维或应用于每个输入向量。您可以将模块设置为对所有输入数据应用相同的插值数组（在模块掩码上输入的静态插值点），或对每个 *N* 维数组、矩阵或向量输入使用不同的插值数组（通过 `Pts` 输入端口接收的时变插值点）。
