---
type: simulink-block
title: 'Deep Signal Anomaly Detector'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'AI for DSP'
documentation_page: 'deepsignalanomalydetector'
documentation_source_path: 'ref/deepsignalanomalydetector.html'
language: zh-CN
chinese_source: worker-translation
---

# Deep Signal Anomaly Detector

## 端口

### 输入

### **Input** — 输入信号向量 | 矩阵

通过此端口将输入信号指定为向量或矩阵。

当输入有多个通道时，该模块假定所有输入通道中异常的存在是均匀的，并生成单通道输出用于异常检测。

在您启用 **Threshold** 端口之前，此端口未命名。

**数据类型：** `single` | `double`

### **Threshold** — 检测阈值 非负标量

将检测阈值指定为非负标量。该模块将此值用作窗口损失的阈值以检测异常。

#### 依赖关系

要启用此端口，请设置：

- **Parameters for post-processing** 为
  `Specify on dialog`。
- **Threshold source** 为 `Input port`。

**数据类型：** `single` | `double`
### 输出

### **Anomaly flag** — 异常标志 逻辑标量

异常标志，返回为逻辑标量：

- `1` –– 输入数据中存在异常。
- `0` –– 输入数据中不存在异常。

当输入有多个通道时，该模块假定所有输入通道中异常的存在是均匀的，并生成单通道输出用于异常检测。

此端口的采样时间等于 *Ts* × *HS*，
其中 *Ts* 是输入端口处的采样时间（或采样周期），*HS* 是相邻窗口之间的跳跃大小。跳跃大小等于 *WL* − *OL*，其中 *WL* 是窗口长度，*OL* 是重叠长度。有关模块采样时间的详细信息，请参阅基于样本和帧的概念。

**数据类型：** `Boolean`

### **Window loss** — 聚合窗口损失 标量

聚合窗口损失，返回为标量。该模块使用 **Window length**、**Overlap length** 和 **Window loss aggregation** 参数计算此值。

该模块使用聚合窗口损失来检测异常。有关详细信息，请参阅算法。

此端口的采样时间等于 *Ts* × *HS*，
其中 *Ts* 是输入端口处的采样时间（或采样周期），*HS* 是相邻窗口之间的跳跃大小。跳跃大小等于 *WL* − *OL*，其中 *WL* 是窗口长度，*OL* 是重叠长度。有关模块采样时间的详细信息，请参阅基于样本和帧的概念。

**数据类型：** `single`

### **Delay** — 延迟估计 标量

输入和输出信号之间延迟的估计（以采样点为单位），返回为标量。要将输入数据与异常标志和窗口损失对齐，请在进一步处理之前将此延迟估计应用于输入。有关示例，请参阅在正弦信号中检测异常。

此端口处的输出始终为标量，并且此端口的采样时间始终为常量。

#### 依赖关系

要启用此端口，请在模块对话框中选中 **Enable delay port** 复选框。

**数据类型：** `single`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink Toolstrip 的 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### **Detector MAT-file path** — 检测器 MAT-file 的路径 `untitled.mat`（默认） | MAT-file 名称

指定使用 `saveModel` 函数生成的 MAT-file 的路径。此 MAT-file 包含经过训练的 LSTM 自编码器或 LSTM forecaster 深度学习网络模型，以及用于后处理的参数，例如窗口长度、重叠长度、检测阈值和窗口损失聚合。

### **Parameters for post-processing** — 后处理参数的来源 `Read from MAT-file`（默认） | `Specify on dialog`

将后处理参数的来源指定为以下之一：

- `Read from MAT-file` –– 该模块使用从 MAT-file 读取的默认参数。
- `Specify on dialog` –– 在模块对话框中指定参数。

后处理的目的是检测信号异常，并确定窗口损失，该损失是衡量模块重建数据好坏的一种度量。

### **Window length** — 窗口长度 `1`（默认） | 正整数

将模块在后处理中使用的窗口长度 *WL* 指定为正整数。默认情况下，该模块使用一个采样点的窗口长度和相邻窗口之间零个采样点的重叠长度。此设置检测点异常。增大窗口长度以在更大的信号范围内聚合窗口损失。

#### 依赖关系

要启用此参数，请将 **Parameters for post-processing** 设置为 `Specify on dialog`。

### **Overlap length** — 相邻窗口之间的重叠长度 `0`（默认） | 非负整数

将相邻窗口之间的重叠长度 *OL* 指定为非负整数。当 *OL* 为 *WL* − 1 时，该模块对每个输入采样点获得一次检测，即跳跃大小为 1 个采样点。跳跃大小是窗口长度与重叠长度之差，*WL* − *OL*。如果要按跳跃大小 *HS* 的因子对输出进行下采样，请将 *OL* 设置为 *WL* − *HS*。

#### 依赖关系

要启用此参数，请将 **Parameters for post-processing** 设置为 `Specify on dialog`。

### **Threshold source** — 检测阈值的来源 `Dialog`（默认） | `Input port`

将检测阈值的来源指定为以下之一：

- `Dialog` –– 在模块对话框中使用 **Threshold** 参数指定阈值。
- `Input port` –– 通过 **Threshold** 输入端口指定阈值。

#### 依赖关系

要启用此参数，请将 **Parameters for post-processing** 设置为 `Specify on dialog`。

### **Threshold** — 检测阈值 `0.01`（默认） | 非负标量

将检测阈值指定为非负标量。该模块基于您在 **Window loss aggregation** 参数中指定的统计方法计算每个窗口的损失。要设置异常标志，该模块将聚合窗口损失与您在此参数中指定的阈值进行比较。如果窗口损失大于阈值，则该模块将异常标志设置为 1，否则设置为 0。较低的阈值会导致该模块将更多采样点分类为异常。根据在异常和非异常区域中观察到的窗口损失来调整阈值。

**可调：** 是

#### 依赖关系

要启用此参数，请设置：

- **Parameters for post-processing** 为 `Specify
  on dialog`。
- **Threshold source** 为
  `Dialog`。

### **Window loss aggregation** — 聚合窗口损失的统计方法 `Mean`（默认） | `Max` | `Min` | `Median`

将模块用于聚合每个窗口段中样本损失的统计方法指定为以下之一：

- `Mean`
- `Max`
- `Min`
- `Median`

#### 依赖关系

要启用此参数，请将 **Parameters for post-processing** 设置为 `Specify on dialog`。

### **Parameter values from MAT-file** — 显示来自 MAT-file 的后处理参数值 只读：文本框

此参数为只读。

显示该模块从 MAT-File 读取的后处理参数值。显示的参数为：

- **Window length**
- **Overlap length**
- **Threshold**
- **Window loss aggregation**

如果您想通过将 **Parameters for post-processing** 设置为 `Specify
on dialog` 来调整后处理参数，请将这些值用作基线。

#### 依赖关系

要启用此参数，请将 **Parameters for post-processing** 设置为 `Read from MAT-file`。

### **Enable delay port** — 输出估计延迟 `off`（默认） | `on`

选中此复选框以启用 **Delay** 输出端口。该模块通过此端口输出输入信号和重建信号之间延迟的估计值（以采样点为单位）。

## 所属库

DSP System Toolbox / AI

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持无库代码生成。

## 版本历史

**在 R2024a 中引入**

### R2024b：支持 LSTM forecaster 模型

Deep Signal Anomaly Detector 模块现在支持 LSTM forecaster 模型。要生成此模型，在使用 `deepSignalAnomalyDetector` 函数创建信号异常检测器时，将 `ModelType` 设置为 `"lstmforecaster"`。

## 描述

使用 Simulink 中的深度学习网络检测信号异常

Deep Signal Anomaly Detector 模块使用经过训练的长短期记忆 (LSTM) 自编码器或经过训练的长短期记忆 (LSTM) forecaster *(自 R2024b 起)* 深度学习网络模型，在 Simulink® 中检测实时信号异常。

您必须首先在 MATLAB® 中使用 `deepSignalAnomalyDetector` 函数创建并训练检测器对象，然后配置该模块以在 Simulink 中使用此模型。要配置该模块，请在模块对话框中指定检测器模型的路径。有关这些步骤的详细信息，请参阅用户工作流。

**注意**

此模块还需要 Deep Learning Toolbox™ 许可证。
