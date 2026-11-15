---
type: simulink-block
title: 'QNN LPAI Predict'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Qualcomm Hexagon Processors / Embedded AI / Qualcomm AI Engine Direct'
documentation_page: 'qnnlpaipredict'
documentation_source_path: 'qualcommhexagon/ref/qnnlpaipredict.html'
language: zh-CN
chinese_source: worker-translation
---

# QNN LPAI Predict

## 端口

### 输入

### **Port\_1** — 预测响应的输入信号 `n`–D 数组

用于所选 QNN 模型推理的输入张量，表示为 `n`-D 数组，与 QNN 模型的 `Input layer size` 参数一致。

QNN LPAI Predict 模块支持最多 4 维的多输入多输出张量，但批量大小必须始终为 1。例如，如果原始深度学习网络的输入层为 128-by-128-by-3，则输入维度应为 128-by-128-by-3 或 1-by-128-by-128-by-3。

如果前导维度为 1（单例维度），则通常可以移除这些维度而不影响兼容性。例如，如果 AI 模型的输入层期望输入大小为 1-by-1-by-128-by-3，则输入可以提供为 1-by-1-by-128-by-3 或简单地 128-by-3。这是因为大小为 1 的维度可以广播以匹配预期形状。

QNN LPAI Predict 模块接受浮点输入或定点输入。输入数据类型必须符合 QNN 网络输入层的数据类型。此外，即使对于量化 QNN 网络，输入也可以是浮点。

**数据类型：** `single` | `half` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### 输出

### **Port\_2** — 推理后的输出信号 `n`–D 数组

用于所选 QNN 模型推理的输出张量，表示为 `n`-D 数组，与 QNN 输出层一致。输出数据类型与 QNN 网络输出层的数据类型匹配。如果选择 **Dequantize Ouptut**，输出始终为 `single`。

**数据类型：** `single` | `half` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## 参数

### **Host(x86) QNN-model file** — 主机 (x-86) 上用于预测响应的 QNN 模型 `<filename>`.dll

点击 **Browse** 并选择 QNN 模型（.dll 格式）以执行推理。有关创建在 LPAI 等设备处理器上运行的 QNN 模型的详细信息，请参阅 Qualcomm AI Engine Direct SDK 文档。

**注意**

如果主机操作系统是 Linux®（仅对 Windows 主机显示），则此参数不显示。对于 Linux，该模块也使用相同的上下文二进制文件（您通过 **Context binary file** 参数选择）作为 host(x86) QNN-model 文件。

### **Context binary file** — LPAI 后端上的 QNN 上下文二进制文件 `<filename>`.bin

点击 **Browse** 并选择目标上的 QNN 上下文二进制文件（.bin），以在主机上执行推理。有关创建在 LPAI 等设备处理器上运行的二进制文件的详细信息，请参阅 Qualcomm AI Engine Direct SDK 文档。

### **Dequantize output** — 使用输出反量化来预测响应 off（默认）| on

选中该复选框以对模块的输出进行反量化。启用此选项后，无论深度学习神经网络的输出层数据类型如何，输出数据类型始终为 `single`。

## 所属库

Embedded Coder Support Package for Qualcomm Hexagon Processors / Hexagon / QNN

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025b 中引入**

## 描述

预测 LPAI 后端的 QNN 上下文二进制的响应

QNN LPAI Predict 模块基于给定输入数据，预测表示为 QNN 上下文二进制文件的深度学习网络在 Qualcomm® AI Direct Engine 的 LPAI 后端上的响应。

要将该模块添加到您的 Simulink 模型，请打开模型（例如 `myQNNModel`），并在 MATLAB 命令提示符下输入以下命令：

    add_block("mwqnnlib/QNN LPAI Predict","myQNNModel/QNN LPAI Predict")

该模块允许您选择 QNN 模型作为编译的共享对象（.so），以在基于 x86 的主机上运行。对于目标，您可以选择针对 LPAI 后端运行而优化的 QNN 上下文二进制文件（.bin）。

使用该模块生成的代码可以部署到配置参数中 **Hardware board** 参数下可用的 Qualcomm Android Board。

该模块还提供在需要时将输出反量化为单精度的选项。
