---
type: simulink-block
title: 'Baseband File Writer'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Comm Sinks'
documentation_page: 'basebandfilewriter'
documentation_source_path: 'ref/basebandfilewriter.html'
language: zh-CN
chinese_source: worker-translation
---

# Baseband File Writer

## 端口

### 输入

### **Port\_1** — 基带信号 标量 | 向量 | 矩阵

此端口接受要保存在由 **Baseband file name** 参数指定的文件名下的基带信号。保存的信号始终为复数。

**数据类型：** `single` | `double`
**复数支持：** 是

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### **Baseband file name** — 要写入的基带文件名 `untitled.bb`（默认）| 字符向量

要写入的基带文件名，指定为字符向量。

要指定文件的保存位置，请点击 **Browse**。

### **Center frequency (Hz)** — 基带信号的中心频率 `1e8`（默认）| 非负标量

基带信号的中心频率，以 Hz 为单位，指定为正标量或行向量。当此属性为行向量时，每个元素是多通道信号中一个通道的中心频率。向量长度等于输入信号 **Port\_1** 的列数。

### **Metadata (structure or object)** — 描述基带信号的数据 空结构体（`struct()`）（默认）| 结构体 | 对象

描述基带信号的数据，指定为标量结构体或对象。

**数据类型：** `struct` | `object`

### **Number of latest samples to write** — 要写入的样本数 `inf`（默认）| 正整数

要保存的样本数，指定为正整数或 `Inf`。

- 要将所有基带信号样本写入文件，请将此属性设置为 `inf`。
- 要仅将最后 `NumSamplesToWrite` 个样本写入文件，请将此属性设置为正整数。

### **Simulate using** — 选择仿真模式 `Code generation`（默认）| `Interpreted execution`

`Code generation`
:   在首次模型运行时，仅使用支持代码生成的 MATLAB® 函数对模块进行仿真并生成代码。如果模块的结构不发生更改，后续模型运行不会重新生成代码。

`Interpreted execution`
:   使用所有支持的 MATLAB 函数对模型进行仿真。选择此选项可能会降低仿真性能。

## 所属库

Communications Toolbox / Comm Sinks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

### R2024a：支持将对象写入元数据

Baseband File Writer 模块现在支持将对象和结构体的结构体写入保存的元数据。

## 描述

将基带信号写入文件

Baseband File Writer 模块将基带信号写入特定类型的二进制文件。基带信号通常从非零中心频率下变频至 0 Hz。当信号写入文件时，会保存采样率（由输入信号采样时间和帧大小决定）和中心频率。
