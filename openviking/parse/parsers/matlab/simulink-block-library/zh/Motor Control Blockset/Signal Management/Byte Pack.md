---
type: simulink-block
title: 'Byte Pack'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Signal Management'
documentation_page: 'bytepack'
documentation_source_path: 'ref/bytepack.html'
language: zh-CN
chinese_source: worker-translation
---

# Byte Pack

## 端口
```yaml
ports:
- name: Port_1
  summary: 要转换的信号，类型为 double（默认）| 信号数据数组
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated | bus
- name: Port_1
  summary: 转换后的信号数据向量
  direction: output
  data_types: uint8
```

### 输入

### **Port\_1** — 要转换的信号，类型为 `double`（默认）| 信号数据数组

一个或多个数据类型的输入信号数组。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **Port\_1** — 转换后的信号数据向量

转换后的模块输入，以 `uint8` 数据向量形式返回。

**数据类型：** `uint8`
## 参数
```yaml
parameters:
- name: Input port data types (cell array)
  summary: 模块输入信号的数据类型 {'double'}（默认）| Simulink® 数据类型的元胞数组
  group: ''
- name: Byte alignment
  summary: 数据类型对齐的字节边界 1（默认）| 2 | 4 | 8
  group: ''
```

### **Input port data types (cell array)** — 模块输入信号的数据类型 {'double'}（默认）| Simulink® 数据类型的元胞数组

以元胞数组形式指定模块接收的输入信号的 Simulink 数据类型。
在元胞数组中，按照模块输入端口接收信号数据的顺序指定数据类型。例如，如果模块按顺序接收
`uint32`、`uint32`、
`uint16`、`double`、`uint8`、
`double` 和 `single` 数据，请指定以下元胞
数组：

```
 {'uint32','uint32','uint16','double','uint8','double','single'}
```

然后模块会提供相应数量的模块输入。

### **Byte alignment** — 数据类型对齐的字节边界 1（默认）| 2 | 4 | 8

指定如何将输入数据的数据类型按字节对齐以形成
`uint8` 向量输出。对齐可以按 1、2、
4 或 8 字节边界进行。根据对齐值，每个信号数据值从对齐值的倍数处开始。输出向量中每个
元素的对齐算法从对齐值指定的字节边界开始。字节对齐设置相对于向量起始点的边界。

要在各种数据类型组合中获得数据类型之间无空洞的最紧凑打包，请选择 `1`。

您可以有多个不同长度的数据类型。在这种情况下，2 字节
对齐可能会在 `uint8` 或
`int8` 值与另一个数据类型之间产生 1 字节间隙。在打包
实现中，模块一次 1 字节地将数据复制到输出数据缓冲区。

例如，假设您为 **Input port
data types (cell array)** 指定以下元胞数组：

```
 {'uint32','uint32','uint16','double','uint8','double','single'}
```

假设您将 **Byte alignment** 设置为
`2`。每个新值从前一个数据
边界起 2 字节处开始。当信号为标量值时：

- 向量中的第一个信号值从 0 字节开始。
- 第二个信号值从 2 字节开始。
- 第三个信号值从 4 字节开始。
- 第四个信号值从 6 字节开始。
- 第五个信号值从 8 字节开始。
- 第六个信号值从 10 字节开始
- 第七个信号值从 12 字节开始。

打包算法在 `uint8`
数据值与 double 值之间留下 1 字节间隙。
## 所属库

Motor Control Blockset / Signal Management C2000 Microcontroller Blockset / Target Communication

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2024a 中引入**

## 描述

将输入信号转换为 uint8 向量

Byte Pack 模块接收一个或多个数据类型的输入信号，并将
数据转换为一个 `uint8` 向量用于输出。使用模块参数指定
输入信号的数据类型以及模块输出向量中数据的对齐方式。由于 UDP 协议以 `uint8` 格式传输数据，
您可以使用此模块重新格式化数据以进行 UDP 传输，方法是将此
模块的输出连接到 UDP Send (Embedded Coder) 模块的输入。
