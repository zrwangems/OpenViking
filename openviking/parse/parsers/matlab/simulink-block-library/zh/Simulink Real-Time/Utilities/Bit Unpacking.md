---
type: simulink-block
title: 'Bit Unpacking'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'bitunpacking'
documentation_source_path: 'io_ref/bitunpacking.html'
language: zh-CN
chinese_source: worker-translation
---

# Bit Unpacking

## 端口

R2025b 中未记录。

## 参数

### **Bit Patterns** — 选择位模式 {[0:31]}（默认）

指定位模式。数据类型必须是 MATLAB® 元胞数组向量。元胞数组中元素的数量定义此模块实例所显示的输入端口数量。元胞数组元素必须是 double 数组类型，并定义传入值（数据类型输入端口）的每一位在传出 double 值（数据帧）中的位置。从数据类型的角度来看，该模块的行为类似于 Sink 模块。**Input port (packed) data types** 指定输入端口的数据类型。

#### 编程使用

|  |
| --- |
| **模块参数**：`BitPatterns` |

### **Input port (packed) data types** — 打包数据类型 `uint32`（默认）| `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `boolean`

从列表中选择输入端口（打包）数据类型。

#### 编程使用

|  |
| --- |
| **模块参数**：`PackDataType` |

### **Input port (packed) dimension** — 打包数据维度 [1]（默认）

指定输入端口（打包）的维度。将此值以向量形式输入。使用与 MATLAB `size` 命令兼容的格式指定端口的大小。

#### 编程使用

|  |
| --- |
| **模块参数**：`PackDataSize` |

### **Output port (unpacked) data types (cell array)** — 解包数据类型 `{'uint32'}`（默认）

输出端口（打包）可以是任意数据类型。元胞数组中元素的数量定义此模块实例所显示的输出端口数量。数据类型包括：

- `double`
- `single`
- `int8`
- `uint8`
- `int16`
- `uint16`
- `int32`
- `uint32`
- `boolean`

#### 编程使用

|  |
| --- |
| **模块参数**：`UnpackDataTypes` |

### **Output port (unpacked) dimension (cell array)** — 解包数据维度 {[1]}（默认）

指定每个输出端口（解包）的维度。将此值以向量大小的元胞数组形式输入。

#### 编程使用

|  |
| --- |
| **模块参数**：`UnpackDataSizes` |

### **Sign extend** — 启用符号扩展 `on`（默认）| `off`

选中此复选框以启用符号扩展。如果选中此复选框并将数据帧解包为有符号类型（`int8`、`int16` 或 `int32`），则该模块执行符号扩展。例如，如果位模式为 `[0:4]`，数据类型为 `int8`，则您将 5 位提取为 8 位宽的有符号类型。在这种情况下，第 5、6 和 7 位与第 4 位相同，从而产生符号扩展。此功能使您能够在不丢失精度的情况下打包和解包负数。

#### 编程使用

|  |
| --- |
| **模块参数**：`SignExtend` |

## 所属库

Simulink Real-Time / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 中引入**

## 描述

解构数据帧

Bit Unpacking 模块提取数据帧。其输入端口通常连接到 Receive 模块或 Digital Input 模块的输出端口。

该模块有一个输入端口，它表示数据帧实体，信号从该实体中提取，并在其输出端口离开模块。输出端口的数量和每个输出端口的数据类型取决于模块对话框中的设置。

### 解包四个字节

此示例展示如何配置 Bit Unpacking 模块以：

- 通过使用输入端口数据类型 `uint32` 接收 32 位字作为输入。
- 通过使用位模式从输入数据中解包四个 8 位字（字节）。
- 通过使用输出数据类型 `uint8` 发送四个 8 位字作为输出。

使用 Bit Unpacking 模块参数对话框配置该模块。

配置模块参数后，Bit Unpacking 模块如图所示。

此 Bit Unpacking 模块配置为具有四个字节宽的输出。
