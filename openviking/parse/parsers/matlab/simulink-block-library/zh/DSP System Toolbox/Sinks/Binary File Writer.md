---
type: simulink-block
title: 'Binary File Writer'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'binaryfilewriter'
documentation_source_path: 'ref/binaryfilewriter.html'
language: zh-CN
chinese_source: worker-translation
---

# Binary File Writer

## 端口
```yaml
ports:
- name: Port_1
  summary: 要写入的数据 列向量 | 行向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64
```

### 输入

### **Port\_1** — 要写入的数据 列向量 | 行向量 | 矩阵

写入模块将数据写入 **File name** 参数指定的文件中。如果 **File header** 结构不为空，则写入模块在写入数据之前先写入文件头。该模块可以写入浮点数据和整数数据。输入数据可以是实数或复数。当数据为复数时，模块将数据写为实部和虚部交错的形式。写入模块假定使用主机的默认字节序。

输入可以是可变大小信号，即您可以在仿真期间更改信号的帧大小（行数），但通道数（列数）必须保持不变。*（自 R2025a 起）*

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: File name
  summary: 文件名 'Untitled.bin'（默认）| 字符向量
  group: ''
- name: File header
  summary: 文件头大小 struct([])（默认）| 结构体
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Interpreted execution（默认）| Code generation
  group: ''
```

### **File name** — 文件名 `'Untitled.bin'`（默认）| 字符向量

模块将数据写入的文件名。

### **File header** — 文件头大小 `struct([])`（默认）| 结构体

该结构体可以具有任意数量的字段。结构体的每个字段必须是内置类型的实数矩阵。例如，如果 **File header** 设置为 `struct('field1',1:10,'field2',single(1))`，则模块写入的文件头由 10 个双精度值 `(1:10)` 组成，后跟 1 个单精度值 `single(1)`。如果没有要写入的文件头，请将此参数设置为空结构体 `struct([])`。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` —— 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` —— 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，C 代码将在后续仿真中重复使用。此选项需要额外的启动时间，但可提供更快的后续仿真。
## 所属库

DSP System Toolbox / Sinks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

### R2025a：支持可变大小信号

Binary File Writer 模块支持可变大小输入信号，即您可以在仿真期间更改信号的帧大小（行数），但通道数（列数）必须保持不变。

### R2024a：**Simulate using** 参数默认值变更

**Simulate using** 参数的默认值现在为 `Interpreted execution`。通过此变更，模块默认使用 MATLAB 解释器进行仿真。

## 描述

将数据写入二进制文件

Binary File Writer 模块将多通道信号数据写入二进制文件。该模块指定文件名以及位于信号数据之前的文件头结构。如果没有要写入的文件头，模块指定一个空结构体 `struct([])`。首次写入文件时，模块先写入文件头，然后写入数据。在后续调用中，模块写入剩余数据。如果文件头为空，则不写入文件头。

模块以行优先格式写入数据。例如，如果输入数组为 `[1 2 4 5; 8 7 9 2]`，则模块将数据写为 `[1 2 4 5 8 7 9 2]`。
