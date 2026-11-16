---
type: simulink-block
title: 'eNPU Predict'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Qualcomm Hexagon Processors / Embedded AI / Micro NPU'
documentation_page: 'enpupredict'
documentation_source_path: 'qualcommhexagon/ref/enpupredict.html'
language: zh-CN
chinese_source: worker-translation
---

# eNPU Predict

## 端口

### 输入

### **Port\_1** — 用于预测响应的输入数据 `N`–维数组

输入数据，指定为 *N* 维数组。
数组大小必须与 eAI 模型的 `Input layer size` 参数中指定的大小相同。

eNPU Predict 模块支持最多四个维度的多输入多输出张量，但批量大小必须始终为 1。例如，如果原始深度学习网络的输入层为 128-by-128-by-3，则输入信号维度必须为 128-by-128-by-3 或 1-by-128-by-128-by-3。

如果前导维度为 1（单一维度），则可以在不影响兼容性的情况下删除这些维度。例如，如果 AI 模型的输入层期望输入大小为 1-by-1-by-128-by-3，则可以将输入指定为大小为 1-by-1-by-128-by-3 或 128-by-3。可以删除这些维度，因为大小为 1 的维度可以广播以匹配期望的形状。

eNPU Predict 模块接受浮点（需要使用其他模块参数进行量化）或定点输入信号。

如果 eAI 模型（eAI 网络文件）的输入层类型为 `int8`、`int16` 或 `int32`，则输入信号的数据类型必须与该模型匹配。如果输入信号数据类型为 `single`，请指定 **输入值范围 [Min Value, Max Value]** 参数。

**数据类型：** `single` | `int8` | `int16` | `int32`

### 输出

### **Port\_2** — 预测响应后的输出信号 `n`–维数组

输出张量，指定为 *N* 维数组。
数组大小必须与 eAI 模型的 `Output layer size` 参数中指定的大小相同。

eNPU Predict 模块支持最多四个维度的多输入多输出张量，但批量大小必须始终为 1。

如果 eAI 模型（eAI 网络文件）的输入层类型为 `int8`、`int16` 或 `int32`，则输出信号的数据类型必须与该模型匹配。如果输出信号数据类型为 `single`，请选择 **反量化输出** 参数并指定 **输出值范围 [MinValue,MaxValue]** 参数。

**数据类型：** `single` | `int8` | `int16` | `int32`

## 参数

### **eAI 网络文件** — 用于预测响应的 eAI 模型 `<filename>`.eai

点击 **浏览**，选择已编译的 eAI 模型（eAI 网络文件）以预测响应。有关使用 eAI Builder 工具创建 eAI 模型的详细信息，请参阅 Qualcomm LPAI SDK 文档。

### **输入值范围 [MinValue,MaxValue]** — 用于浮点输入最小-最大量化的输入值范围 `M`-by-2 数组

用于浮点输入量化的输入值最小和最大范围，指定为包含 `M` 个 [`min`,`max`] 值的 *M*-by-2 数组，其中 `M` 是输入层的数量。

例如，要量化具有两个输入的张量布局的两个输入，请指定值：`[[0, 255];[0,255]]`。

该模块同时支持对称量化（最小值和最大值的绝对值相同）和非对称量化（最小值和最大值的绝对值不同）。

**注意**

如果使用的是最新 LPAI Add-on 版本 2.5.0.0，则无需指定量化值范围。因此，仅较早版本的 LPAI Add-On 需要此参数。

### **反量化输出** — 用于预测响应时使用输出反量化的选项 off（默认）| on

选择此参数可对模块的输出进行反量化。

### **输出值范围 [MinValue,MaxValue]** — 用于浮点输出最小-最大量化的输出值范围 `M`-by-2 数组

用于浮点输出量化的输出值最小和最大范围，指定为包含 `M` 个 [`min`,`max`] 值的 *M*-by-2 数组，其中 `M` 是输出层的数量。

该模块同时支持对称量化（最小值和最大值的绝对值相同）和非对称量化（最小值和最大值的绝对值不同）。

**注意**

如果使用的是最新 LPAI Add-on 版本 2.5.0.0，则无需指定量化值范围。因此，仅较早版本的 LPAI Add-On 需要此参数。

#### 依赖关系

仅当选中 **反量化输出** 复选框时，此参数才会显示。

### **使用默认性能配置** — 用于为 eAI 客户端使用默认性能配置值的选项 `on`（默认）| `off`

选择此参数可在获取响应时为 eAI 客户端使用默认性能配置值。根据 LPAI SDK Addon 文档，默认值为：

- 每秒帧数：1
- 快于实时 (FTRT) 比率：10
- 优先级：3

### **每秒帧数** — 每秒的帧数 `1`（默认）| 数值标量

使用 eAI 模型预测响应时每秒要处理的帧数。有关详细信息，请参阅 Qualcomm LPAI SDK 文档。

#### 依赖关系

要启用此参数，请清除 **使用默认性能配置** 参数。

### **快于实时 (FTRT) 比率** — FTRT 比率 `10`（默认）| 数值标量

使用 eAI 模型预测响应时用于快于实时性能的比率。有关详细信息，请参阅 Qualcomm LPAI SDK 文档。

#### 依赖关系

要启用此参数，请清除 **使用默认性能配置** 参数。

### **优先级** — 用于 eNPU 调度的客户端优先级 `3`（默认）| `2` | `1` | `0`

使用 eAI 模型预测响应时用于 eNPU 调度的客户端优先级。您可以指定以下值之一及其对应优先级：

- 3 – 非常低
- 2 – 低
- 1 – 中
- 0 – 高

有关详细信息，请参阅 Qualcomm LPAI SDK 文档。

#### 依赖关系

要启用此参数，请清除 **使用默认性能配置** 参数。

### **实时处理** — 用于通过实时处理预测响应的选项 `on`（默认）| `off`

选择此参数可在预测响应的同时对输入数据执行实时处理。

#### 依赖关系

要启用此参数，请清除 **使用默认性能配置** 参数。

## 所属库

Embedded Coder Support Package for Qualcomm Hexagon Processors / Hexagon / eNPU Library

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

使用已编译的 eAI 模型预测 eNPU 的响应

eNPU Predict 模块基于给定输入数据，通过使用为 Qualcomm® eNPU 设计的已编译嵌入式人工智能 (eAI) 模型来预测响应。该模块可帮助您仿真和评估 eAI 网络文件中表示的神经网络。

使用此模块可选择通过 LPAI SDK Addon for Qualcomm Hexagon® SDK 生成的、以 eAI 模型（eAI 网络文件）表示的深度学习网络。对于主机仿真，eNPU Predict 模块在后台使用 LPAI SDK 的主机运行时库来处理输入数据。

如果输入数据的数据类型为 `single`，请使用模块中提供的输入值范围选项，根据所选 eAI 模型对输入进行量化。

默认情况下，输出数据经过量化。要获得单精度输出，请选择模块中的反量化选项，并根据所选 eAI 模型提供输出值范围。

在使用 eAI 模型预测响应之前，还可以使用模块中提供的其他性能选项来自定义 eAI 客户端的一些性能配置参数。有关这些参数的详细信息，请参阅 Qualcomm LPAI SDK 文档。

**注意**

eNPU Predict 模块不支持 `Rapid Accelerator` 仿真模式。将 eNPU Predict 模块添加到模型时，请使用 `Normal` 或 `Accelerator` 模式。

**注意**

要使用此模块，请确保安装 LPAI Add-on；该附加功能在硬件设置过程中提供。有关更多详细信息，请参阅
