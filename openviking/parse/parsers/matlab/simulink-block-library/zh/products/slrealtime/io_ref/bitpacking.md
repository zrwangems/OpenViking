---
type: simulink-block
title: 'Bit Packing'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / I/O Connectivity / Utilities'
documentation_page: 'bitpacking'
documentation_source_path: 'io_ref/bitpacking.html'
language: zh-CN
chinese_source: official
---

# Bit Packing

## 端口

R2025b 官方文档未提供。

## 参数

### **Bit Patterns** — 压缩数据位模式 {[0:31]} (默认)

指定位模式。控件中输入的数据类型必须为 MATLAB® 元胞数组向量。元胞数组中的元素数量决定了该模块实例所显示的输入端口数量。元胞数组元素必须为双精度数组类型，并定义输入值（数据类型输入端口）中每个位在输出双精度值（数据帧）中的位置。从数据类型角度（输入端口）来看，该模块的行为类似于 Simulink® 接收器模块。输入端口的数据类型继承自驱动模块。

#### 编程用法

|  |
| --- |
| **模块参数：**`BitPatterns` |

### **Output port (packed) data type** — 紧凑数据类型 `uint32` (默认) | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `boolean`

从列表中选择输出端口（紧凑）数据类型。

#### 编程用法

|  |
| --- |
| **模块参数：**`PackDataType` |

### **Output port (packed) dimensions** — 压缩数据维度 [1] (默认)

指定输出端口的尺寸（紧凑格式）。请将此值作为向量输入。使用与 MATLAB `size` 命令兼容的格式指定端口大小。

#### 编程用法

|  |
| --- |
| **模块参数：**`PackDataSize` |

## 所属库

Simulink Real-Time / Utilities

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2006a 中推出**

## 描述

构建数据帧

Bit Packing 模块构建数据帧。其输出端口通常连接到 Send 模块或 Digital Output 模块的输入端口。该模块有一个输出端口。该端口可以是任意大小的向量。它表示由进入该模块输入端口的信号构成的数据帧实体。输入端口的数量取决于模块对话框中的设置。
