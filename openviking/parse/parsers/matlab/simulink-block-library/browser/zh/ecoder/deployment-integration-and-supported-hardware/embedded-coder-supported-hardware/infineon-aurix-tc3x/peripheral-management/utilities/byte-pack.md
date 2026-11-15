---
type: simulink-block
title: 'Byte Pack'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Architecture and Component Design / Blocks for Embedded Targets'
documentation_page: 'bytepack'
documentation_source_path: 'ref/bytepack.html'
language: zh-CN
chinese_source: official
---

# Byte Pack

## 端口

### 输入

### **Port\_1** — 要转换的信号 `double` 类型的信号 (默认) | 信号数据数组

一种或多种数据类型的输入信号数组。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **Port\_1** — 转换后的信号数据 向量

转换后的模块输入，以 `uint8` 数据向量形式返回。

**数据类型:** `uint8`

## 参数

### **输入端口数据类型（元胞数组）** — 模块输入信号的数据类型 {'double'} (默认) | 由 Simulink® 数据类型组成的元胞数组

以元胞数组的形式指定模块接收的输入信号的 Simulink 数据类型。在该元胞数组中，按照模块输入端口接收信号数据的顺序指定数据类型。例如，如果模块以 `uint32`、`uint32`、`uint16`、`double`、`uint8`、`double` 和 `single` 的顺序接收数据，请按以下顺序指定此元胞数组：

```
 {'uint32','uint32','uint16','double','uint8','double','single'}
```

然后，该模块提供模块输入数目。

### **字节对齐方式** — 数据类型对齐方式的字节边界 1 (默认) | 2 | 4 | 8

指定如何对齐输入数据的数据类型，以形成以字节为单位的 `uint8` 向量输出。在 1、2、4 或 8 字节边界上可能会出现需要对齐的情况。基于对齐值，每个信号数据值从对齐值的倍数开始。输出向量中每个元素的对齐算法从对齐值指定的字节边界开始。字节对齐设置相对于向量起点的边界。

要在各种数据类型组合中获得最紧凑的打包（数据类型之间没有空位），请选择 `1`。

可以有多种不同长度的数据类型。在这种情况下，2 字节对齐会在 `uint8` 或 `int8` 值和另一种数据类型之间产生 1 个字节的空位。在打包实现中，模块以一次 1 个字节的方式将数据复制到输出数据缓冲区。

例如，假设您为**输入端口数据类型(元胞数组)** 指定以下元胞数组：

```
 {'uint32','uint32','uint16','double','uint8','double','single'}
```

假设您将**字节对齐方式**设置为 `2`。每个新值从距前一个数据边界 2 个字节处开始。当信号是标量值时：

- 向量中的第一个信号值从 0 字节开始。
- 第二个信号值从 2 字节开始。
- 第三个信号值从 4 字节开始。
- 第四个信号值从 6 字节开始。
- 第五个信号值从 8 字节开始。
- 第六个信号值从 10 字节开始
- 第七个信号值从 12 字节开始。

打包算法在 `uint8` 数据值和双精度值之间留有 1 个字节的间隙。

## 所属库

Embedded Coder / Embedded Targets / Host Communication

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2011a 中推出**

## 描述

将输入信号转换为 uint8 向量

Byte Pack 模块接收一种或多种数据类型的输入信号，并将数据转换为一个 `uint8` 向量进行输出。使用模块参数指定输入信号的数据类型以及模块输出的向量中的数据对齐方式。由于 UDP 协议以 `uint8` 格式传输数据，因此您可以通过将此模块的输出连接到 UDP Send 模块的输入，使用此模块来重新格式化用于 UDP 传输的数据。
