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
chinese_source: official
---

# Byte Unpacking

## 端口

### 输入

### **Port\_1** — 包含紧凑数据的输入端口 向量

该模块显示一个输入端口，用于接收打包数据的向量。打包数据的来源通过继承决定了打包数据的数据类型。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean`
### 输出

### **Port\_1** — 第一个 *N* 输出端口 标量 | 向量

该模块显示从 `1` 到 *N* 的输出端口，具体由参数 **Output port (unpacked) data types (cell array)** 中的元胞数组元素指定。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean`

## 参数

### **Output port (unpacked) data types (cell array)** — 未封装输出信号的数据类型 **uint8** (默认) | **double** | **single** | **int8** | **int16** | **uint16** | **int32** | **uint32** | **boolean**

将不同输出信号的输出端口（未打包）的数据类型指定为元胞数组。元胞数组中的元素数量决定了该模块实例所显示的输出端口数量。要表示向量元素，请在元胞数组中使用方括号。

#### 编程用法

|  |
| --- |
| **模块参数：**`MaskUnpackedDataTypes` |

### **Output port (unpacked) dimensions (cell array)** — 每个输出端口的尺寸（未打包） `{[1]}` (默认) | `{[N], [M], ...}`

将输出端口的尺寸指定为一个元胞数组向量。

#### 编程用法

|  |
| --- |
| **模块参数：**`MaskUnpackedDataSizes` |

### **Byte Alignment** — 解包前输出信号数据类型的对齐 **1** (默认) | **2** | **4** | **8**

输出信号列表中的每个元素都从对齐值的倍数处开始，该对齐值是从输入向量起始位置指定的。如果对齐值大于数据类型的字节大小，则向量包含填充字节，其值为 `0`。

例如，如果对齐值为 `4`：

- `uint32` 未接收任何填充数据
- `uint16` 接收了 `2` 字节的填充数据
- `uint8` 接收了 `3` 字节的填充数据

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

Byte Unpacking 模块仅支持 C++ 代码生成。

## 版本历史

**在 R2006a 中推出**

## 描述

分解数据帧

Byte Unpacking 模块将不同数据类型的向量转换为用户可选数据类型的一个或多个信号。该模块的输入端通常连接到 Receive 模块的输出端口。

Byte Packing 模块和 Byte Unpacking 模块支持 Simulink® Real-Time™ STF 代码生成目标，并生成可在 Speedgoat 目标计算机上运行的代码。由于字节序和可寻址字长等因素，这些模块在其他代码生成目标或目标计算机上可能产生错误结果。

例如，假设您正在将一个 `uint8` 矢量信号拆解为三个信号。这些信号具有以下属性：

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
2. 将输出端口尺寸设置为：

   ```
   {[1],[3],[3]}
   ```
3. 将对齐值设置为 **1**。
4. 将输出信号连接至 Byte Unpacking 模块。
