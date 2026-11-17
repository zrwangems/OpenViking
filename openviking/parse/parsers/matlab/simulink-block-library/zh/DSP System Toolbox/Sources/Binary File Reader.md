---
type: simulink-block
title: 'Binary File Reader'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'binaryfilereader'
documentation_source_path: 'ref/binaryfilereader.html'
language: zh-CN
chinese_source: worker-translation
---

# Binary File Reader

## 端口

### 输出

### **data** — 二进制文件数据 列向量 | 行向量 | 矩阵

读取器模块从 **File name** 参数指定的文件中读取二进制数据。模块输出的数据维度为 **Samples per frame** × **Number of channels**。该模块可以读取浮点数据和整数数据。输入数据可以是实数或复数。当数据为复数时，模块将数据读取为交错的实部和虚部分量。读取器假定使用宿主机的默认字节序。

在您选择 **Output end-of-file indicator** 参数之前，此端口没有名称。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
**复数支持：** 是

### **EOF** — 文件结束指示符 布尔标量

当模块到达文件末尾时，端口输出 `1`。否则，端口输出 `0`。

在您选择 **Output end-of-file indicator** 参数之前，此端口没有名称。

**数据类型：** `Boolean`

## 参数

### **File name** — 文件名 `'Untitled.bin'`（默认）| 字符向量

模块从中读取数据的文件名。如果文件不在 MATLAB® 路径上，请指定文件的完整路径。

### **File header** — 文件头大小 `struct([])`（默认）| 结构体

该结构体指定文件头的原型，即文件头的大小和字段值的数据类型。该结构体可以有任意数量的字段。结构体的每个字段必须是内置类型的实数矩阵。例如，如果 **File header** 设置为 `struct('field1',1:10,'field2',single(1))`，则模块假定文件头由 10 个实数双精度值后跟 1 个单精度值组成。如果文件不包含文件头，可以将此参数设置为空结构体 `struct([])`。

### **Export header to base workspace** — 检索文件头 按钮

要检索文件头，请点击 **Export header to base workspace**。模块将文件头导出到基础工作区。

### **Storage data type** — 文件中数据的存储类别 `'double'`（默认）| `'single'` | `'int8'` | `'int16'` | `'int32'` | `'int64'` | `'uint8'` | `'uint16'` | `'uint32'` | `'uint64'`

文件中数据的存储类别，指定为字符向量。此参数定义模块输出的矩阵的数据类型。

### **Samples per frame** — 每个输出帧的采样数 `1024`（默认）| 正整数

**Samples per frame** 指定模块输出的输出矩阵的行数。输出矩阵的维度为 **Samples per frame** × **Number of channels**。一旦到达文件末尾，模块将返回指定数据类型、大小和复数性的零值。

### **Data is complex** — 指定数据复数性 关（默认）| 开

当您选择此参数时，读取器将数据视为复数数据。模块将数据读取为交错的实部和虚部分量。将模块配置为将数据读取为 2×2 矩阵。模块将 `[1 5 2 6 3 7 4 8]` 读取为 `[1 2; 3 4]+1j*[5 6; 7 8]`。当您不选择此参数时，模块将数据读取为 `[1 5; 2 6]`。

### **Number of channels** — 通道数 `1`（默认）| 正整数

**Number of channels** 指定模块输出的输出矩阵的列数。此参数定义文件中为每个时间时刻存储的连续交错数据采样数。数据的大小为 **Samples per frame** × **Number of channels**。一旦到达文件末尾，如果输出矩阵未满，模块将用零填充矩阵以使其成为完整大小的矩阵。

### **Output end-of-file indicator** — 文件结束指示符 关（默认）| 开

当您选择此参数时，模块上会出现一个名为 **EOF** 的附加输出端口。当模块到达文件末尾时，端口输出 `1`。否则，端口输出 `0`。

### **Sample time (s)** — 采样时间 1（默认）| 非负标量

**Sample time (s)** 控制模块输出端口的采样时间。此值表示 1/*Fs*，其中 *Fs* 是信号数据的采样率。输出端口处的 Simulink 采样时间为 **Samples per frame** × **Sample time (s)**。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` —— 使用 MATLAB 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` —— 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不发生变化，C 代码将在后续仿真中重复使用。此选项需要额外的启动时间，但可提供更快的后续仿真。

## 所属库

DSP System Toolbox / Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

### R2024a：**Simulate using** 参数默认值变更

**Simulate using** 参数的默认值现在为 `Interpreted execution`。通过此变更，模块默认使用 MATLAB 解释器进行仿真。

## 描述

从二进制文件读取数据

Binary File Reader 模块从二进制文件中读取多通道信号数据。该模块读取数据之前的文件头。**File header** 参数指定文件头的结构。您可以通过模块参数指定数据的类型、大小和复数性。您还可以通过点击 **Export header to base workspace** 按钮将文件头导出到基础工作区。

首次读取文件时，读取器先读取文件头，然后读取数据。在后续调用中，读取器读取剩余数据。一旦到达文件末尾，读取器将返回指定数据类型、大小和复数性的零值。读取器可以从并非由 Binary File Writer 模块创建的二进制文件中读取信号数据。
