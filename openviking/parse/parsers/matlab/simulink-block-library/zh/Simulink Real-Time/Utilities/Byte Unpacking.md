---
type: simulink-block
title: 'Byte Unpacking'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'byteunpacking'
documentation_source_path: 'io_ref/byteunpacking.html'
language: zh-CN
chinese_source: worker-translation
---

# Byte Unpacking

## 端口

### 输入

### **Port\_1** — 包含打包数据向量的输入端口

该模块显示一个输入端口，用于接收打包数据向量。打包数据的来源通过继承决定打包数据的数据类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean`
### 输出

### **Port\_1** — *N* 个输出端口中的第一个 标量 | 向量

该模块显示从 `1` 到 *N* 个输出端口，具体数量由参数 **Output port (unpacked) data types (cell array)** 中元胞数组的元素指定。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean`

## 参数

### **Output port (unpacked) data types (cell array)** — 解包输出信号的数据类型 `uint8`（默认） | `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

以元胞数组的形式指定不同输出信号的输出端口（解包）数据类型。元胞数组中元素的数量决定了该模块实例所显示的输出端口数量。要表示向量元素，请在元胞数组中使用方括号。

#### 编程使用

|  |
| --- |
| **模块参数：** `MaskUnpackedDataTypes` |

### **Output port (unpacked) dimensions (cell array)** — 每个输出端口（解包）的维度 `{[1]}`（默认） | `{[N], [M], ...}`

以向量元胞数组的形式指定输出端口的维度。

#### 编程使用

|  |
| --- |
| **模块参数：** `MaskUnpackedDataSizes` |

### **Byte Alignment** — 解包前输出信号数据类型的对齐方式 `1`（默认） | `2` | `4` | `8`

输出信号列表中的每个元素从对齐值的倍数位置开始，该位置从输入向量的起始处计算。如果对齐值大于数据类型的大小（以字节为单位），则向量中包含值为 `0` 的填充字节。

例如，如果对齐值为 `4`：

- `uint32` 不接收填充
- `uint16` 接收 `2` 字节的填充
- `uint8` 接收 `3` 字节的填充

#### 编程使用

|  |
| --- |
| **模块参数：** `MaskAlignment` |

## 所属库

Simulink Real-Time / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

Byte Unpacking 模块仅支持 C++ 代码生成。

## 版本历史

**在 R2006a 中引入**

## 描述

解构数据帧

Byte Unpacking 模块将不同数据类型的向量转换为一个或多个用户可选择数据类型的信号。该模块的输入通常连接到 Receive 模块的输出端口。

Byte Packing 模块和 Byte Unpacking 模块支持 Simulink® Real-Time™ STF 代码生成目标，并生成可在 Speedgoat 目标机器上运行的代码。由于字节序和可寻址字长等因素，这些模块对于其他代码生成目标或目标计算机可能会生成不正确的结果。

例如，假设您要将一个 `uint8` 向量信号解包为三个信号。这些信号具有以下属性：

| 维度 | 大小 | 类型 |
| --- | --- | --- |
| 标量 | `1` | `single` |
| 向量 | `3` | `uint8` |
| 向量 | `3` | `uint8` |

1. 将输出端口数据类型设置为：

   ```
   {'single', ['uint8'], ['uint8']}
   ```

   使用方括号表示向量。
2. 将输出端口维度设置为：

   ```
   {[1],[3],[3]}
   ```
3. 将对齐值设置为 `1`。
4. 将输出信号连接到 Byte Unpacking 模块。
