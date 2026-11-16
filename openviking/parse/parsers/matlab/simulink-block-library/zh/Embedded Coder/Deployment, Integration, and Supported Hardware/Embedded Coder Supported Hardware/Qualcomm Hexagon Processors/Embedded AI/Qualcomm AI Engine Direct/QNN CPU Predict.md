---
type: simulink-block
title: 'QNN CPU Predict'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Qualcomm Hexagon Processors / Embedded AI / Qualcomm AI Engine Direct'
documentation_page: 'qnncpupredict'
documentation_source_path: 'qualcommhexagon/ref/qnncpupredict.html'
language: zh-CN
chinese_source: worker-translation
---

# QNN CPU Predict

## 端口

### 输入

### **Port\_1** — 用于预测响应的输入信号 `n`–D 数组

用于使用所选 QNN 模型进行推理的输入张量，表示为 `n`-D 数组，并与 QNN 模型的 `Input layer size` 参数一致。

QNN CPU Predict 模块支持最多 4 维的多输入多输出张量，但批大小必须始终为 1。例如，如果原始深度学习网络的输入层为 128-by-128-by-3，则输入维度应为 128-by-128-by-3 或 1-by-128-by-128-by-3。

如果前导维度为 1（单例维度），则通常可以删除这些维度而不影响兼容性。例如，如果 AI 模型的输入层期望输入大小为 1-by-1-by-128-by-3，则输入可以提供为 1-by-1-by-128-by-3，或者直接为 128-by-3。这是因为大小为 1 的维度可以广播以匹配预期形状。

QNN CPU Predict 模块接受浮点输入或定点输入。输入数据类型必须与 QNN 网络输入层的数据类型一致。此外，即使对于量化 QNN 网络，输入也可以是浮点类型。

**数据类型：** `single` | `half` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### 输出

### **Port\_2** — 推理后的输出信号 `n`–D 数组

用于使用所选 QNN 模型进行推理的输出张量，表示为 `n`-D 数组，并与 QNN 输出层一致。输出数据类型与 QNN 网络输出层的数据类型匹配。

**数据类型：** `single` | `half` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## 参数

### **主机(x86) QNN 模型文件** — 用于在主机 (x-86) 上预测响应的 QNN 模型 `<filename>`.dll

单击 **浏览** 并选择 QNN 模型（编译后的共享对象 (.so) 或 .dll）以执行推理。有关创建可在 CPU 等设备处理器上运行的 QNN 模型的详细信息，请参阅 Qualcomm AI Engine Direct SDK 文档。

### **目标 QNN 模型文件** — CPU 后端上的目标 QNN 模型 `<filename>`.so

单击 **浏览** 并选择目标上的 QNN 模型（编译后的共享对象 (.so)）以在主机上执行推理。有关创建可在 CPU 等设备处理器上运行的 QNN 模型的详细信息，请参阅 Qualcomm AI Engine Direct SDK 文档。

### **输出去量化** — 使用输出去量化预测响应 off（默认）| on

选中该复选框以对模块的输出进行去量化。启用此选项后，无论深度学习神经网络输出层的数据类型是什么，输出数据类型始终为 `single`。

## 所属库

Embedded Coder Support Package for Qualcomm Hexagon Processors / Hexagon / QNN

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025b 中引入**

## 描述

预测 CPU 后端的 QNN 模型的响应

QNN CPU Predict 模块基于给定输入数据，预测以 QNN 模型表示的深度学习网络在 Qualcomm® AI Direct Engine 的 CPU 后端上的响应。

要将该模块添加到您的 Simulink 模型，请打开模型（例如 `myQNNModel`），并在 MATLAB 命令提示符下输入以下命令：

    add_block("mwqnnlib/QNN CPU Predict","myQNNModel/QNN CPU Predict")

QNN CPU Predict 模块允许您选择 QNN 模型作为编译后的共享对象 (.so)，以在基于 x86 的主机上运行。对于目标，您可以选择已优化为在 CPU 后端上运行的编译后的共享对象 (.so) 或 .dll。包含此模块的 Simulink 模型可以部署到 Qualcomm Android Board，该开发板在支持包中作为支持的开发板提供。

使用此模块生成的代码可以部署到以下开发板之一，这些开发板可在“配置参数”的 **Hardware board** 参数下找到：

- Qualcomm Android Board
- Qualcomm Linux Board

该模块还提供了在需要时将输出去量化为单精度的选项。
