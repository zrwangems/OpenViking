---
type: simulink-block
title: 'Deep Signal Anomaly Detector'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'AI'
documentation_page: 'deepsignalanomalydetector'
documentation_source_path: 'ref/deepsignalanomalydetector.html'
language: zh-CN
chinese_source: worker-translation
---

# Deep Signal Anomaly Detector

## 端口

### 输入

### **Input** — 输入信号 向量 | 矩阵

通过此端口将输入信号指定为向量或矩阵。

当输入具有多个通道时，模块假设异常的存在情况在所有输入通道中一致，并生成用于异常检测的单通道输出。

在您启用 **Threshold** 端口之前，此端口没有名称。

**数据类型：** `single` | `double`

### **Threshold** — 检测阈值 非负标量

将检测阈值指定为非负标量。模块使用此值作为窗口损失的阈值来检测异常。

#### 依赖关系

要启用此端口，请设置：

- 将 **Parameters for post-processing** 设置为 `Specify on dialog`。
- 将 **Threshold source** 设置为 `Input port`。

**数据类型：** `single` | `double`
### 输出

### **Anomaly flag** — 异常标志 逻辑标量

异常标志，以逻辑标量形式返回：

- `1` –– 输入数据中存在异常。
- `0` –– 输入数据中不存在异常。

当输入具有多个通道时，模块假设异常的存在情况在所有输入通道中一致，并生成用于异常检测的单通道输出。

此端口的采样时间等于 *Ts* × *HS*，其中 *Ts* 是输入端口的采样时间（或采样周期），*HS* 是相邻窗口之间的跳跃大小。跳跃大小等于 *WL* − *OL*，其中 *WL* 是窗口长度，*OL* 是重叠长度。有关模块采样时间的详细信息，请参阅基于样本和基于帧的概念。

**数据类型：** `Boolean`

### **Window loss** — 聚合窗口损失 标量

聚合窗口损失，以标量形式返回。模块使用 **Window length**、**Overlap length** 和 **Window loss aggregation** 参数计算此值。

模块使用聚合窗口损失来检测异常。有关详细信息，请参阅算法。

此端口的采样时间等于 *Ts* × *HS*，其中 *Ts* 是输入端口的采样时间（或采样周期），*HS* 是相邻窗口之间的跳跃大小。跳跃大小等于 *WL* − *OL*，其中 *WL* 是窗口长度，*OL* 是重叠长度。有关模块采样时间的详细信息，请参阅基于样本和基于帧的概念。

**数据类型：** `single`

### **Delay** — 延迟估计值 标量

输入信号与输出信号之间的延迟估计值（以样本数表示），以标量形式返回。为使输入数据与异常标志和窗口损失对齐，请在进一步处理之前将此延迟估计值应用于输入。有关示例，请参阅检测正弦信号中的异常。

此端口的输出始终为标量，且此端口的采样时间始终为常量。

#### 依赖关系

要启用此端口，请在模块对话框中选中 **Enable delay port** 复选框。

**数据类型：** `single`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。从 Simulink 工具条中，在 **Simulation** 选项卡的 **Prepare** 图库中，选择 **Property Inspector**。

### **Detector MAT-file path** — 检测器 MAT 文件的路径 `untitled.mat` (默认) | MAT 文件名

指定使用 `saveModel` 函数生成的 MAT 文件的路径。此 MAT 文件包含经过训练的 LSTM 自编码器或 LSTM 预测器深度学习网络模型，以及用于后处理的参数，例如窗口长度、重叠长度、检测阈值和窗口损失聚合。

### **Parameters for post-processing** — 后处理参数的来源 `Read from MAT-file` (默认) | `Specify on dialog`

将后处理参数的来源指定为以下值之一：

- `Read from MAT-file` –– 模块使用从 MAT 文件读取的默认参数。
- `Specify on dialog` –– 在模块对话框中指定参数。

后处理的目标是检测信号异常并确定窗口损失，后者用于衡量模块重建数据的效果。

### **Window length** — 窗口长度 `1` (默认) | 正整数

将模块在后处理中使用的窗口长度 *WL* 指定为正整数。默认情况下，模块使用一个样本的窗口长度，并且相邻窗口之间的重叠长度为零个样本。此设置可检测点异常。增大窗口长度可在信号的更大范围内聚合窗口损失。

#### 依赖关系

要启用此参数，请将 **Parameters for post-processing** 设置为 `Specify on dialog`。

### **Overlap length** — 相邻窗口之间的重叠长度 `0` (默认) | 非负整数

将相邻窗口之间的重叠长度 *OL* 指定为非负整数。当 *OL* 为 *WL* − 1 时，模块对每个输入样本进行一次检测，即跳跃大小为 1 个样本。跳跃大小是窗口长度与重叠长度之差，即 *WL* − *OL*。如果要按跳跃大小 *HS* 的因子对输出进行降采样，请将 *OL* 设置为 *WL* − *HS*。

#### 依赖关系

要启用此参数，请将 **Parameters for post-processing** 设置为 `Specify on dialog`。

### **Threshold source** — 检测阈值的来源 `Dialog` (默认) | `Input port`

将检测阈值的来源指定为以下值之一：

- `Dialog` –– 使用 **Threshold** 参数在模块对话框中指定阈值。
- `Input port` –– 通过 **Threshold** 输入端口指定阈值。

#### 依赖关系

要启用此参数，请将 **Parameters for post-processing** 设置为 `Specify on dialog`。

### **Threshold** — 检测阈值 `0.01` (默认) | 非负标量

将检测阈值指定为非负标量。模块根据您在 **Window loss aggregation** 参数中指定的统计方法计算每个窗口的损失。为了设置异常标志，模块将聚合窗口损失与您在此参数中指定的阈值进行比较。如果窗口损失大于阈值，模块将异常标志设置为 1，否则将其设置为 0。较低的阈值会使模块将更多样本分类为异常。请根据在异常区域和非异常区域中观察到的窗口损失调整阈值。

**可调：** 是

#### 依赖关系

要启用此参数，请设置：

- 将 **Parameters for post-processing** 设置为 `Specify on dialog`。
- 将 **Threshold source** 设置为 `Dialog`。

### **Window loss aggregation** — 聚合窗口损失的统计方法 `Mean` (默认) | `Max` | `Min` | `Median`

将模块用于聚合每个窗口段中样本损失的统计方法指定为以下值之一：

- `Mean`
- `Max`
- `Min`
- `Median`

#### 依赖关系

要启用此参数，请将 **Parameters for post-processing** 设置为 `Specify on dialog`。

### **Parameter values from MAT-file** — 显示来自 MAT 文件的后处理参数值 只读：文本框

此参数为只读。

显示模块从 MAT 文件读取的后处理参数值。显示的参数包括：

- **Window length**
- **Overlap length**
- **Threshold**
- **Window loss aggregation**

如果要通过将 **Parameters for post-processing** 设置为 `Specify on dialog` 来调整后处理参数，请将这些值用作基准。

#### 依赖关系

要启用此参数，请将 **Parameters for post-processing** 设置为 `Read from MAT-file`。

### **Enable delay port** — 输出估计延迟 `off` (默认) | `on`

选中此复选框可启用 **Delay** 输出端口。模块通过此端口输出输入信号与重建信号之间的估计延迟（以样本数表示）。

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

此模块支持不依赖库的代码生成。

## 版本历史

**在 R2024a 中引入**

### R2024b：支持 LSTM 预测器模型

Deep Signal Anomaly Detector 模块现在支持 LSTM 预测器模型。要生成此模型，请在使用 `deepSignalAnomalyDetector` 函数创建信号异常检测器时，将 `ModelType` 设置为 `"lstmforecaster"`。

## 描述

在 Simulink 中使用深度学习网络检测信号异常

Deep Signal Anomaly Detector 模块使用经过训练的长短期记忆 (LSTM) 自编码器或经过训练的长短期记忆 (LSTM) 预测器*（自 R2024b 起）*深度学习网络模型，在 Simulink® 中实时检测信号异常。

您必须先在 MATLAB® 中使用 `deepSignalAnomalyDetector` 函数创建并训练检测器对象，然后将模块配置为在 Simulink 中使用此模型。要配置模块，请在模块对话框中指定检测器模型的路径。有关这些步骤的详细信息，请参阅用户工作流程。

**注意**

此模块还需要 Deep Learning Toolbox™ 许可证。
