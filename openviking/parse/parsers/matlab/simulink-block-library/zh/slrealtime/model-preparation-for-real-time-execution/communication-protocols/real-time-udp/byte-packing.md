---
type: simulink-block
title: 'Byte Packing'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / I/O Connectivity / Utilities'
documentation_page: 'bytepacking'
documentation_source_path: 'io_ref/bytepacking.html'
language: zh-CN
chinese_source: official
---

# Byte Packing

## 端口

### 输入

### **Port\_1** — 第一个 *N* 输入端口 标量 | 向量

该模块具有从 `1` 到 *N* 的输入端口。通过在参数 **Input port (unpacked) data types (cell array)** 中输入元胞数组，指定输入端口的数量及其类型。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean`
### 输出

### **Port\_1** — 输出端口包含打包数据 向量

该模块显示一个输出端口，用于传输一个打包数据向量。通过设置 **Output port (packed) data type** 来确定打包数据的数据类型。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean`

## 参数

### **Output port (packed) data type** — 打包输出信号的数据类型 **uint8** (默认) | **double** | **single** | **int8** | **int16** | **uint16** | **int32** | **uint32** | **boolean**

从列表中选择输出端口的数据类型。

#### 编程用法

|  |
| --- |
| **模块参数：**`MaskPackedDataType` |

### **Input port (unpacked) data types (cell array)** — 未封装输入信号的数据类型 `{'uint8'}` (默认) | `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

将不同输入信号的输入端口数据类型（未打包）指定为元胞数组。元胞数组中的元素数量决定了该模块实例所显示的输入端口数量。要表示向量元素，请在元胞数组中使用方括号。

#### 编程用法

|  |
| --- |
| **模块参数：**`MaskUnpackedDataTypes` |

### **Byte Alignment** — 输入信号数据类型在打包后的对齐 **1** (默认) | **2** | **4** | **8**

输入信号列表中的每个元素从对齐值的倍数处开始，该对齐值从向量起始点开始指定。如果对齐值大于数据类型的字节大小，则该模块用值为 `0` 的填充字节填充剩余空间。

例如，如果对齐值为 `4`：

- `uint32` 未接收任何填充数据
- `uint16` 接收了 `2` 字节的填充数据
- `uint8` 接收了 `3` 字节的填充数据

如果模型频繁访问数据项，请考虑选择一个对齐值，该值应等于您希望访问的最大数据类型。若模型频繁以组形式传输数据项，建议采用对齐值 **1**，该值可将数据压缩至最小空间。

#### 编程用法

|  |
| --- |
| **模块参数：**`MaskAlignment` |

## 所属库

Simulink Real-Time / Utilities

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

Byte Packing 模块仅支持 C++ 代码生成。

## 版本历史

**在 R2006a 中推出**

## 描述

构建数据帧

Byte Packing 模块将一个或多个用户可选数据类型的信号转换为单个变长数据类型的向量。该模块的输出端通常连接到 Send 模块的输入端口。

Byte Packing 代码模块和 Byte Unpacking 代码模块支持 Simulink® Real-Time™ STF 代码生成目标，并生成可在 Speedgoat 目标计算机上运行的代码。由于字节序和可寻址字长等因素，这些模块在其他代码生成目标或目标计算机上可能产生错误结果。

例如，假设您将三个信号打包到一个 `uint8` 向量中。这些信号具有以下属性：

| 维度 | 大小 | 类型 |
| --- | --- | --- |
| 标量 | `1` | `single` |
| 向量 | `3` | `uint8` |
| 向量 | `3` | `uint8` |

1. 将打包输出端口数据类型设置为 `uint8`。
2. 将输入端口数据类型设置为编码数据类型的元胞数组：

   ```
   {'single', ['uint8'], ['uint8']}
   ```

   使用方括号表示向量。
3. 将字节对齐值设置为 **1**。
4. 将信号连接到 Byte Packing 模块。
