---
type: simulink-block
title: 'Byte Unpack'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Embedded Targets / Host Communication'
documentation_page: 'byteunpack'
documentation_source_path: 'ref/byteunpack.html'
language: zh-CN
chinese_source: worker-translation
---

# Byte Unpack

## 端口

### 输入

### **Port\_1** — 要转换的信号向量

`uint8` 类型的输入向量。

**数据类型：** `uint8`
### 输出

### **Port\_1** — 转换后的信号数据，类型为 `double`（默认）| 信号数据数组

一个或多个数据类型的输入信号数组。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **Output port dimensions (cell array)** — 模块输出信号的维度 {[1]}（默认）| 数据维度规范的元胞数组

在元胞数组中指定模块输出的输出信号维度。
数组中的每个元素指定 MATLAB®
`size` 函数为对应信号返回的维度。指定的维度应与模型中对应 Byte Pack 模块转换的数据一致。

例如，假设对应的 Byte Pack 模块指定了以下输入端口数据类型：

```
 {'uint32','uint32','uint16','double','uint8','double','single'}
```

要指定标量和矩阵输出，可以将 **Output port dimensions (cell array)** 参数设置为：

```
 {1,1,[2,4],[4,4],[2,2],1,[3,3]}
```

要对所有输出信号应用相同的维度，可以只指定一个维度值。

### **Output port data types (cell array)** — 模块输出信号的数据类型 {'double'}（默认）| Simulink 数据类型的元胞数组

在元胞数组中指定模型中对应 Byte Pack 模块接收的各个输入信号的 Simulink 数据类型。

例如，如果对应的 Byte Pack 模块指定了以下输入端口数据类型，请为此参数指定相同的元胞数组。

```
 {'uint32','uint32','uint16','double','uint8','double','single'}
```

要对每个输出信号应用相同的数据类型，只需指定一次数据类型。

### **Byte Alignment** — 数据类型对齐的字节边界 1（默认）| 2 | 4 | 8

指定如何对齐输出数据的数据类型，以按字节形成 `uint8` 向量输入。指定的对齐值应与模型中对应 Byte Pack 模块指定的值一致。

例如，如果对应的 Byte Pack 模块将字节对齐设置为 2，请将此参数设置为 2。

## 所属库

Embedded Coder / Embedded Targets / Host Communication

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2011a 中引入**

## 描述

将 uint8 向量转换为输入信号

Byte Unpack 模块接收一个 `uint8` 向量，并根据输入向量的内容将该向量转换为不同 Simulink® 数据类型的输出信号。您可以使用模块参数指定输出信号的维度和数据类型，以及模块输出的各个向量中数据的对齐方式。由于 UDP 协议以 `uint8` 格式传输数据，您可以将此模块的输入连接到 UDP Send 模块的输出，以重新格式化作为 UDP 数据包接收的数据，以便在模型中使用。
