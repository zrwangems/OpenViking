---
type: simulink-block
title: 'Byte Packing'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'bytepacking'
documentation_source_path: 'io_ref/bytepacking.html'
language: zh-CN
chinese_source: worker-translation
---

# Byte Packing

## 端口
```yaml
ports:
- name: Port_1
  summary: '*N* 个输入端口中的第一个 标量 | 向量'
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean
- name: Port_1
  summary: 包含打包数据的输出端口 向量
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean
```

### 输入

### **Port\_1** — *N* 个输入端口中的第一个 标量 | 向量

该模块具有从 `1` 到 *N* 个输入端口。通过在参数 **Input port (unpacked) data types (cell array)** 中以元胞数组的形式输入端口数量和类型来指定它们。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean`
### 输出

### **Port\_1** — 包含打包数据的输出端口 向量

该模块显示一个输出端口，用于传输打包数据的向量。您通过设置 **Output port (packed) data type** 来确定打包数据的数据类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean`
## 参数
```yaml
parameters:
- name: Output port (packed) data type
  summary: 打包输出信号的数据类型 uint8（默认） | double | single | int8 | int16 | uint16 | int32 | uint32 | boolean
  group: ''
  block_parameter: MaskPackedDataType
- name: Input port (unpacked) data types (cell array)
  summary: 未打包输入信号的数据类型 {'uint8'}（默认） | double | single | int8 | int16 | uint16 | int32 | uint32 | boolean
  group: ''
  block_parameter: MaskUnpackedDataTypes
- name: Byte Alignment
  summary: 打包后输入信号数据类型的对齐方式 1（默认） | 2 | 4 | 8
  group: ''
  block_parameter: MaskAlignment
```

### **Output port (packed) data type** — 打包输出信号的数据类型 `uint8`（默认） | `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

从列表中选择输出端口的数据类型。

#### 编程使用

|  |
| --- |
| **模块参数**：`MaskPackedDataType` |

### **Input port (unpacked) data types (cell array)** — 未打包输入信号的数据类型 `{'uint8'}`（默认） | `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

以元胞数组的形式指定不同输入信号的输入端口（未打包）的数据类型。元胞数组中元素的数量决定了此模块实例所显示的输入端口数量。要表示向量元素，请在元胞数组中使用方括号。

#### 编程使用

|  |
| --- |
| **模块参数**：`MaskUnpackedDataTypes` |

### **Byte Alignment** — 打包后输入信号数据类型的对齐方式 `1`（默认） | `2` | `4` | `8`

输入信号列表中的每个元素从对齐值的倍数位置开始，该位置从向量的起始处计算。如果对齐值大于数据类型的大小（以字节为单位），则该模块用值为 `0` 的填充字节填充空间。

例如，如果对齐值为 `4`：

- `uint32` 不接收填充
- `uint16` 接收 `2` 字节的填充
- `uint8` 接收 `3` 字节的填充

如果模型频繁访问数据项，请考虑选择等于您要访问的最大数据类型的对齐值。如果模型频繁地以组的形式传输数据项，请考虑使用对齐值 `1`，这样可以将数据打包到尽可能小的空间中。

#### 编程使用

|  |
| --- |
| **模块参数**：`MaskAlignment` |
## 所属库

Simulink Real-Time / Utilities

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

Byte Packing 模块仅支持 C++ 代码生成。

## 版本历史

**在 R2006a 中引入**

## 描述

构造数据帧

Byte Packing 模块将一个或多个用户可选数据类型的信号转换为一个具有不同数据类型的单一向量。该模块的输出通常连接到 Send 模块的输入端口。

Byte Packing 模块和 Byte Unpacking 模块支持 Simulink® Real-Time™ STF 代码生成目标，并生成在 Speedgoat 目标机器上运行的代码。由于字节序和可寻址字长等因素，这些模块对于其他代码生成目标或目标计算机可能会生成不正确的结果。

例如，假设您要将三个信号打包成一个 `uint8` 向量。这些信号具有以下属性：

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
3. 将字节对齐值设置为 `1`。
4. 将信号连接到 Byte Packing 模块。
