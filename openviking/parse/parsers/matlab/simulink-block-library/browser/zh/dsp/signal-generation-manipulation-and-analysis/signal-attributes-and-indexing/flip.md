---
type: simulink-block
title: 'Flip'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Generation, Manipulation, and Analysis / Signal Attributes and Indexing'
documentation_page: 'flip'
documentation_source_path: 'ref/flip.html'
language: zh-CN
chinese_source: official
---

# Flip

## 端口

### 输入

### **Input** — 输入信号 矩阵

输入信号，指定为大小为 *M*×*N* 的矩阵。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated`
### 输出

### **Output** — 翻转的输出 矩阵

翻转的输出，以大小为 *M*×*N* 的矩阵形式返回。输出始终与输入具有相同的维度。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated`

## 参数

### **翻转维度** — 指定要沿其翻转的维度 **列** (默认) | **行**

将要沿其翻转输入的维度指定为**列**或**行**。当您将此参数设置为**列**时，此模块垂直翻转输入。当您将此参数设置为**行**时，此模块水平翻转输入。

当您将此参数设置为**列**时，此模块*垂直*翻转输入，因此输入的第一行变为输出的最后一行。

```
y = flipud(u) % Equivalent MATLAB code
```

当垂直翻转输入时，该模块将长度为 *M* 的无向向量输入视为 *M*×1 列向量。

当您将此参数设置为**行**时，此模块*水平*翻转输入，因此输入的第一列变为输出的最后一列。

```
y = fliplr(u) % Equivalent MATLAB code
```

当水平翻转输入时，该模块将长度为 *N* 的无向向量输入视为 1×*N* 行向量。

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

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

垂直或水平翻转输入

Flip 模块垂直或水平反转 *M*×*N* 输入矩阵 *u*。该模块使用**翻转维度**参数确定要沿其翻转的维度。

此模块支持 Simulink® 虚拟总线。
