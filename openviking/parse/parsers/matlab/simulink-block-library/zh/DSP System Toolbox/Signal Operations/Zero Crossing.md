---
type: simulink-block
title: 'Zero Crossing'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Operations'
documentation_page: 'zerocrossing'
documentation_source_path: 'ref/zerocrossing.html'
language: zh-CN
chinese_source: worker-translation
---

# Zero Crossing

## 端口

### 输入

### **Port\_1** — 数据输入 向量 | 矩阵

指定为实值向量或矩阵的输入信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
### 输出

### **Cnt** — 过零次数 标量 | 行向量

该模块将数据输入中的过零次数输出为以下之一：

- 标量 –– 当数据输入为列向量时，该模块输出一个标量值，表示数据输入中的过零次数。
- 行向量 –– 当数据输入为矩阵时，该模块输出一个行向量，行向量中的每个元素表示数据输入对应列中的过零次数。

**数据类型：** `uint32`

## 参数

### **Input processing** — 处理输入信号的方法 `Columns as channels (frame based)`（默认）| `Elements as channels (sample based)`

指定该模块应如何处理输入。

- `Columns as channels (frame based)`
  — 当您选择此选项时，该模块将输入的每一列视为一个单独的通道。
- `Elements as channels (sample based)`
  — 当您选择此选项时，该模块将输入的每一个元素视为一个单独的通道。

## 所属库

DSP System Toolbox / Signal Operations

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

统计单个时间步内信号过零的次数

如果给定通道中的信号满足以下任一条件，则 Zero Crossing 模块判定该信号已过零，其中
*xi* 是信号的当前值，
*x**i*−1 是前一个值，依此类推：

- *xi* < 0 且
  *x**i*−1 >
  0
- *xi* > 0 且
  *x**i*−1 <
  0
- 对于正整数 *L*，
  *xi* < 0，
  *x**i*−1 = 0，且
  *x**i*−*L*−1
  > 0，其中 0≤l≤L。
- 对于正整数 *L*，
  *x**i* > 0，
  *x**i*−1 = 0，且
  *x**i*−*L*−1
  < 0，其中 0≤l≤L。

对于输入信号的第一个值，
*x**i*−1 和
*x**i*−2 为零。该模块在
**Cnt** 端口输出信号在单个时间步内过零的次数。
