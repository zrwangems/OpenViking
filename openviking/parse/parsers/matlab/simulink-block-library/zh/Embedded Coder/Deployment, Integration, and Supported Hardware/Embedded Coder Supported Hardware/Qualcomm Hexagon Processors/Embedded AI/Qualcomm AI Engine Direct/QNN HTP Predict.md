---
type: simulink-block
title: 'QNN HTP Predict'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Qualcomm Hexagon Processors / Embedded AI / Qualcomm AI Engine Direct'
documentation_page: 'qnnhtppredict'
documentation_source_path: 'qualcommhexagon/ref/qnnhtppredict.html'
language: zh-CN
chinese_source: worker-translation
---

# QNN HTP Predict

## 端口

### 输入

### **Port\_1** — 用于预测响应的输入信号 `n`–D 数组

用于使用所选 QNN 模型进行推理的输入张量，表示为 `n`-D 数组，并与 QNN 模型的 `Input layer size` 一致。

QNN HTP Predict 模块支持最多 4 维的多输入多输出张量，但批大小必须始终为 1。例如，如果原始深度学习网络的输入层为 128×128×3，则输入维度应为 128×128×3 或 1×128×128×3。

如果前导维度为 1（单例维度），则通常可以移除这些维度而不影响兼容性。例如，如果 AI 模型的输入层期望输入大小为 1×1×128×3，则输入可以提供为 1×1×128×3，或直接提供为 128×3。这是因为大小为 1 的维度可以广播以匹配预期形状。

QNN HTP Predict 模块接受浮点输入或定点输入。输入数据类型必须与 QNN 网络输入层的数据类型一致。此外，即使对于量化 QNN 网络，输入也可以是浮点类型。

**数据类型：** `single` | `half` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### 输出

### **Port\_2** — 推理后的输出信号 `n`–D 数组

用于使用所选 QNN 模型进行推理的输出张量，表示为 `n`-D 数组，并与 QNN 输出层一致。输出的数据类型与 QNN 网络的输出层数据类型匹配。

**数据类型：** `single` | `half` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## 参数

### **深度学习网络格式** — 针对目标上 HTP (NPU) 后端优化运行的深度学习网络格式 `QNN-Model` | `Binary`

选择针对目标上 HTP (NPU) 后端优化运行的深度学习网络格式。

### **主机(x86) QNN-model 文件** — 用于预测响应的主机 (x-86) 上的 QNN 模型 `<filename>`.so | `<filename>`.dll

点击 **Browse**，选择要执行推理的 QNN 模型（编译后的共享对象 (.so) 或 .dll）。有关创建可在 HTP 等设备处理器上运行的 QNN 模型的详细信息，请参阅 Qualcomm AI Engine Direct SDK 文档。

**注意**

如果主机操作系统为 Linux®，并且您为 **深度学习网络格式** 参数选择 `BINARY`，则此参数不会出现。在这种情况下，该模块也会将同一个上下文二进制文件（您使用 **上下文二进制文件** 参数选择的文件）用作主机(x86) QNN-model 文件。

### **目标 QNN-model 文件** — HTP (NPU) 后端上的目标 QNN 模型 `<filename>`.so

点击 **Browse**，选择目标上的 QNN 模型（编译后的共享对象 (.so)），以便在主机上执行推理。有关创建可在 HTP 等设备处理器上运行的 QNN 模型的详细信息，请参阅 Qualcomm AI Engine Direct SDK 文档。

#### 依赖关系

仅当您为 **深度学习网络格式** 参数选择 `QNN-model` 时，此参数才会出现。

### **上下文二进制文件** — HTP (NPU) 后端上的 QNN 上下文二进制文件 `<filename>`.bin

点击 **Browse**，选择目标上的 QNN 上下文二进制文件 (.bin)，以便在主机上执行推理。有关创建可在 HTP 等设备处理器上运行的二进制文件的详细信息，请参阅 Qualcomm AI Engine Direct SDK 文档。

### **反量化输出** — 使用输出反量化来预测响应 off（默认）| on

选中该复选框以反量化模块的输出。启用此选项后，无论深度神经网络输出层的数据类型如何，输出数据类型始终为 `single`。

## 所属库

Embedded Coder Support Package for Qualcomm Hexagon Processors / Hexagon / QNN

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025b 中引入**

## 描述

为 HTP (NPU) 后端预测 QNN 模型或 QNN context binary 的响应

QNN HTP Predict 模块基于给定输入数据，为 Qualcomm® AI Direct Engine 的 HTP (NPU) 后端预测表示为 QNN 模型或 QNN context binary 的深度学习网络的响应。

要将该模块添加到 Simulink 模型，请打开模型（例如 `myQNNModel`），并在 MATLAB 提示符下输入以下命令：

    add_block("mwqnnlib/QNN HTP Predict","myQNNModel/QNN HTP Predict")

QNN HTP Predict 模块允许您选择 QNN 模型作为编译后的共享对象 (.so)，以便在基于 x86 的主机上运行。对于目标，您可以选择编译后的共享对象 (.so) 或针对 HTP (NPU) 后端优化运行的 QNN 上下文二进制文件 (.bin)。

使用该模块生成的代码可以部署到以下开发板之一，这些开发板可在配置参数的 **硬件板** 参数下找到：

- Qualcomm Android Board
- Qualcomm Linux Board
- Qualcomm Hexagon Android Board, with Processor Version `cDSP`
- Qualcomm Hexagon Linux Board, with Processor Version `cDSP`

该模块还提供在需要时将输出反量化为单精度的选项。
