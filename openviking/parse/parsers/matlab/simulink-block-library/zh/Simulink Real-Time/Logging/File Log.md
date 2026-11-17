---
type: simulink-block
title: 'File Log'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Logging'
documentation_page: 'filelog'
documentation_source_path: 'io_ref/filelog.html'
language: zh-CN
chinese_source: worker-translation
---

# File Log

## 端口

### 输入

### **S** — 文件日志的信号数据 标量 | 向量 | 矩阵 | 数组 | 总线 | 非虚拟总线

为文件日志提供信号数据输入。

## 参数

### **Decimation** — 对文件日志数据应用抽取 `1`（默认）| 整数

抽取参数值选择文件日志中捕获的样本的抽取。

通过使用 File Log 抽取函数，实时应用程序 MLDATX 文件的后续加载将在目标上以 File Log 模块修改后的抽取值运行。这些函数是：

- `getAllFileLogBlocks`
- `getFileLogDecimation`
- `setFileLogDecimation`

有关详细信息，请参阅 Tune Decimation for File Log Data Without Model Rebuild。

#### 编程使用

```
decimation
```

### **Input Processing** — 选择文件日志数据的处理模式 `Elements as channels (sample based)`（默认）| `Columns as channels (frame based)`

输入处理参数值选择记录的信号数据是以采样还是帧处理模式处理并发送到 Simulation Data Inspector。有关 Simulation Data Inspector 中基于采样的数据和基于帧的数据的详细信息，请参阅 View Simulation Data in Simulation Data Inspector。

#### 编程使用

```
inputProcessing
```

## 所属库

Simulink Real-Time / Logging

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

### R2022a：抽取、日志保留和基于帧的输入

函数允许您获取和设置模型中 File Log 模块的抽取值。此外，函数允许您控制 File Log 记录何时开始和停止。

## 描述

在目标计算机上写入信号数据文件日志

当您启用日志记录服务时，File Log 模块将其输入端口处的信号记录到 Speedgoat® 目标计算机文件系统。

有关文件日志记录工作流的详细信息，请参阅 Real-Time Signal Logging and Streaming Basics。
