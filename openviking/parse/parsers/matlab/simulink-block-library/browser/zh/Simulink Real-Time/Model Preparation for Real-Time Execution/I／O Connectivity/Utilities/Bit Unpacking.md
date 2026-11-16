---
type: simulink-block
title: 'Bit Unpacking'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / I/O Connectivity / Utilities'
documentation_page: 'bitunpacking'
documentation_source_path: 'io_ref/bitunpacking.html'
language: zh-CN
chinese_source: official
---

# Bit Unpacking

## 端口

R2025b 官方文档未提供。

## 参数

### **Bit Patterns** — 选择位模式 {[0:31]} (默认)

指定位模式。数据类型必须为 MATLAB® 元胞数组向量。元胞数组中的元素数量决定了该模块实例所显示的输入端口数量。元胞数组元素必须为双精度数组类型，并定义输入值（数据类型输入端口）中每个位在输出双精度值（数据帧）中的位置。从数据类型角度来看，该模块的行为类似于接收器模块。**Input port (packed) data types** 指定输入端口的数据类型。

#### 编程用法

|  |
| --- |
| **模块参数：**`BitPatterns` |

### **Input port (packed) data types** — 紧凑数据类型 `uint32` (默认) | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `boolean`

从列表中选择一个输入端口（紧凑）数据类型。

#### 编程用法

|  |
| --- |
| **模块参数：**`PackDataType` |

### **Input port (packed) dimension** — 压缩数据维度 [1] (默认)

指定输入端口的尺寸（紧凑格式）。请将此值作为向量输入。使用与 MATLAB `size` 命令兼容的格式指定端口大小。

#### 编程用法

|  |
| --- |
| **模块参数：**`PackDataSize` |

### **Output port (unpacked) data types (cell array)** — 未封装的数据类型 `{'uint32'}` (默认)

输出端口（紧凑格式）可以是任意数据类型。元胞数组中的元素数量决定了该模块实例所显示的输出端口数量。数据类型包括：

- `double`
- `single`
- `int8`
- `uint8`
- `int16`
- `uint16`
- `int32`
- `uint32`
- `boolean`

#### 编程用法

|  |
| --- |
| **模块参数：**`UnpackDataTypes` |

### **Output port (unpacked) dimension (cell array)** — 未打包数据维度 {[1]} (默认)

指定每个输出端口的尺寸（未打包）。将此值作为向量尺寸的元胞数组输入。

#### 编程用法

|  |
| --- |
| **模块参数：**`UnpackDataSizes` |

### **Sign extend** — 启用符号扩展 `on` (默认) | `off`

选中此复选框以启用符号扩展。若选中此复选框并将数据帧解压为带符号类型（`int8`、`int16` 或 `int32`），该模块将执行符号扩展。例如，若位模式为 `[0:4]`，数据类型为 `int8`，则表示将 5 位数据提取到 8 位宽的有符号类型中。在此情况下，第 5、6、7 位与第 4 位相同，导致符号扩展。此功能可让您在打包和解包负数时保持精度不变。

#### 编程用法

|  |
| --- |
| **模块参数：**`SignExtend` |

## 所属库

Simulink Real-Time / Utilities

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2006a 中推出**

## 描述

分解数据帧

Bit Unpacking 模块提取数据帧。其输入端口通常连接到 Receive 模块或 Digital Input 模块的输出端口。

该模块具有一个输入端口，该端口代表数据帧实体，信号从中提取并通过其输出端口离开模块。输出端口的数量及每个输出端口的数据类型取决于模块对话框中的设置。

### 位解包四字节

此示例演示如何配置一个 Bit Upacking 模块以实现：

- 使用输入端口数据类型 `uint32` 接收 32 位字作为输入。
- 使用位模式从输入数据中解包四个 8 位字（字节）。
- 使用输出数据类型 `uint8` 发送四个 8 位字作为输出。

Configure the block by using the Bit Unpacking block parameters dialog box.

配置完模块参数后，Bit Upacking 模块将如图所示呈现。

This Bit Unpacking block is configured to have four byte-wide outputs.
