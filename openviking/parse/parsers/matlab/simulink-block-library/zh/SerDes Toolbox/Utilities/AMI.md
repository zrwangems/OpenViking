---
type: simulink-block
title: 'AMI'
family: 'serdes'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'ami'
documentation_source_path: 'ref/ami.html'
language: zh-CN
chinese_source: worker-translation
---

# AMI

## 端口
```yaml
ports:
- name: WaveIn
  summary: 输入信号 标量 | 向量
  direction: input
  data_types: double
- name: WaveOut
  summary: 修改后的输出数据 标量 | 向量
  direction: output
  data_types: double
```

### 输入

### **WaveIn** — 输入信号 标量 | 向量

输入信号，指定为波形。

**数据类型：** `double`
### 输出

### **WaveOut** — 修改后的输出数据 标量 | 向量

修改后的输出数据，包含有损印刷电路板传输线模型的影响，依据 [1] 中概述的方法。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: DLL File
  summary: 可执行文件 DLL 文件 | SO 文件
  group: ''
- name: AMI File
  summary: AMI 设置文件 文本文件
  group: ''
- name: Operation
  summary: 定义模块用作发射器还是接收器 Tx（默认）| Rx
  group: ''
- name: Correlation Flow
  summary: 定义模块是否与另一个发射器或接收器并行运行 off（默认）| on
  group: ''
```

### **DLL File** — 可执行文件 DLL 文件 | SO 文件

浏览选择包含执行 SerDes 系统的代码和数据的 DLL 或 SO 文件。您可以从正在协同设计的第三方供应商处获取这些文件。您也可以从您设计并导出的另一个 SerDes 系统获取它们，以便与当前系统进行相关性分析。

### **AMI File** — AMI 设置文件 文本文件

浏览选择包含 AMI 参数和设置的 AMI 文件。AMI 文件的内容设置 AMI 树并定义如何运行 DLL 文件。AMI 树在模块参数对话框中表示。有关如何管理 AMI 参数的更多信息，请参阅管理 IBIS 和 AMI 文件的内容。

AMI 树的简短摘要由 **Input String** 参数报告。如果您对树参数进行任何更改，**Input String** 参数将更新以反映更改。

### **Operation** — 定义模块用作发射器还是接收器 `Tx`（默认）| `Rx`

定义模块用作发射器（Tx）还是接收器（Rx）。这设置了操作的优先级，并按正确的顺序调用模块以进行 Init 仿真。有关 Init 仿真的更多信息，请参阅 SerDes 系统中的统计分析。

### **Correlation Flow** — 定义模块是否与另一个发射器或接收器并行运行 off（默认）| on

选择此选项可使 AMI 模块与另一个发射器（Tx）或接收器（Rx）并行运行。
## 所属库

SerDes Toolbox / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023b 中引入**

## 描述

与其他供应商设计协同设计 SerDes 架构

AMI 模块允许您与其他供应商 IP 协同设计 SerDes 项目。它还允许您将代码生成/编译的 IBIS-AMI 模型与生成它们的 Simulink® 模型进行相关性分析。

该模块可以替换发射器或接收器组件，或与它们一起运行。要将发射器或接收器组件恢复为其默认设置，请用 Tx 或 Rx 模块替换 AMI 模块。

您只能在从 SerDes Designer 应用导出的 Simulink 模型中使用该模块。SerDes Designer 设置模块正常工作所需的 AMI 树。该模块必须在 SerDes Simulink 模型的顶层使用。

为了在 Rx 和 AMI 之间获得精确的相关性，您必须在 Rx 之后添加一个长度为 1024 的延迟模块。此延迟补偿了 AMI 模块内部处理 Block Size 的缓冲/解缓冲。

**注意**

您需要 SerDes Toolbox™ 和 Signal Integrity Toolbox™ 的许可证才能使用此模块。
