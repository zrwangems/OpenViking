---
type: simulink-block
title: 'Flip'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Management / Indexing'
documentation_page: 'flip'
documentation_source_path: 'ref/flip.html'
language: zh-CN
chinese_source: worker-translation
---

# Flip

## 端口
```yaml
ports:
- name: Input
  summary: 输入信号矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point | enumerated
- name: Output
  summary: 翻转后的输出矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point | enumerated
```

### 输入

### **Input** — 输入信号矩阵

输入信号，指定为大小为 *M*-by-*N* 的矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated`
### 输出

### **Output** — 翻转后的输出矩阵

翻转后的输出，以大小为 *M*-by-*N* 的矩阵形式返回。输出始终与输入具有相同的维度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated`
## 参数
```yaml
parameters:
- name: Flip along
  summary: 指定沿其翻转的维度 Columns（默认）| Rows
  group: ''
```

### **Flip along** — 指定沿其翻转的维度 `Columns`（默认）| `Rows`

指定沿其翻转输入的维度，可选 `Columns` 或 `Rows`。
当您将此参数设置为 `Columns` 时，模块垂直翻转输入。当您将此参数设置为
`Rows` 时，模块水平翻转输入。

当您将此参数设置为 `Columns` 时，模块*垂直*翻转输入，因此输入的第一行变为输出的最后一行。

```
y = flipud(u) % Equivalent MATLAB code
```

垂直翻转输入时，模块将长度为 *M* 的无向向量输入视为
*M*-by-1 列向量。

当您将此参数设置为 `Rows` 时，模块*水平*翻转输入，因此输入的第一列变为输出的最后一列。

```
y = fliplr(u) % Equivalent MATLAB code
```

水平翻转输入时，模块将长度为 *N* 的无向向量输入视为
1-by-*N* 行向量。
## 所属库

DSP System Toolbox / Signal Management / Indexing

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

垂直或水平翻转输入

Flip 模块垂直或水平反转 *M*-by-*N* 输入矩阵 *u*。该模块使用 **Flip along** 参数确定沿其翻转的维度。

该模块支持 Simulink® 虚拟总线。
