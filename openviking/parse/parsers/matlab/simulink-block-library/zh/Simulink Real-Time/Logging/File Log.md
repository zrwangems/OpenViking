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
chinese_source: official
---

# File Log

## 端口

### 输入

### **S** — 文件日志的信号数据 标量 | 向量 | 矩阵 | 数组 | 总线 | 非虚拟总线

为文件日志提供信号数据输入。

## 参数

### **Decimation** — 对文件日志数据应用抽取处理 `1` (默认) | 整数

抽取参数值用于选择对文件日志中捕获的样本进行抽取处理。

通过使用 File Log 降采样函数，后续加载的实时应用程序 MLDATX 文件将在目标设备上运行，此时 File Log 模块的降采样值已被修改。这些函数是：

- `getAllFileLogBlocks`
- `getFileLogDecimation`
- `setFileLogDecimation`

有关详细信息，请参阅Tune Decimation for File Log Data Without Model Rebuild。

#### 编程用法

```
decimation
```

### **Input Processing** — 选择文件日志数据的处理模式 `Elements as channels (sample based)` (默认) | `Columns as channels (frame based)`

输入处理参数值用于选择记录的信号数据是在采样处理模式还是帧处理模式下进行处理并发送至仿真数据检查器。有关仿真数据检查器中基于样本的数据和基于帧的数据的更多信息，请参阅在仿真数据检查器中查看仿真数据。

#### 编程用法

```
inputProcessing
```

## 所属库

Simulink Real-Time / Logging

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2020b 中推出**

### R2022a: 十进制化、日志保留与基于帧的输入

函数可用于获取和设置模型中 File Log 模块的抽取值。此外，这些功能还允许您控制 File Log 录制的开始和结束时间。

## 描述

在目标计算机上写入信号数据文件日志

当启用日志记录服务时，File Log 模块会将输入端口接收到的信号记录到 Speedgoat® 目标计算机的文件系统中。

有关文件日志记录工作流的更多信息，请参阅 Real-Time Signal Logging and Streaming Basics。
