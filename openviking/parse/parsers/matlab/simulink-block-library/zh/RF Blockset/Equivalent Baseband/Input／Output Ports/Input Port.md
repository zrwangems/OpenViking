---
type: simulink-block
title: 'Input Port'
family: 'equivalent-baseband'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Equivalent Baseband / Input/Output Ports'
documentation_page: 'inputport'
documentation_source_path: 'ref/inputport.html'
language: zh-CN
chinese_source: worker-translation
---

# Input Port

## 端口

R2025b 中未记录。

## 参数

### **Treat input Simulink signal as** — 用于解释输入的选项 `Source voltage`（默认值） | `Incident power wave` | scalar

用于解释输入 Simulink 信号的选项，指定为以下之一：

- `Incident power wave` — 将输入信号解释为与其连接的物理模型所描述的 RF 系统的入射功率波。选择此选项时，RF 系统的输出信号为传输功率波。这是最常见的 RF 建模解释。
- `Source voltage` — 将输入信号解释为与其连接的物理模型所描述的 RF 系统的源电压。因此，基带等效模型包含通过源阻抗的损耗。选择此选项时，RF 系统的输出信号为负载电压。

有关这些选项的详细信息，请参阅 Convert to and from Simulink Signals。

### **Source impedance (ohms)** — RF 网络的源阻抗 `50`（默认值） | scalar

与其连接的物理模型所描述的 RF 网络的源阻抗，指定为以 ohms 为单位的标量。

### **Finite impulse response filter length** — 基带等效冲激响应的期望长度 `128`（默认值） | scalar

物理模型的基带等效冲激响应的期望长度，指定为标量。时域中的 FIR 滤波器越长，频域中的频率分辨率越精细。频率分辨率约等于 1/ (**Finite impulse response filter length**\***Sample time (s)**)。有关此参数的图形化表示，请参阅 Baseband-Equivalent Modeling。

**注意**

等效基带仿真算法在计算中使用大于指定滤波器长度的下一个 2 的幂，然后将冲激响应截断为指定长度。因此，当您将 **Finite impulse response filter length** 参数设置为不是 2 的幂的数字时，会得到不同的结果。有关详细信息，请参阅 Calculate the Baseband-Equivalent Impulse Response。

### **Fractional bandwidth of guard bands** — 建模带宽的分数 `0`（默认值） | scalar

建模带宽的分数，指定为标量。在创建基带等效模型时，用于对系统传递函数的边缘进行渐变的建模带宽分数。此参数定义使用 Tukey（即余弦渐变）窗进行渐变的区段带宽与恒定（即未渐变）区段带宽之比。

小于或等于 0 的值告诉 Input Port 模块使用矩形（`rectwin` (Signal Processing Toolbox)）窗。大于或等于 1 的值告诉 Input Port 模块使用 hann 窗。

### **Modeling delay (samples)** — 用于延迟基带等效模型冲激响应的时间样本数 `0`（默认值） | scalar

用于延迟基带等效模型冲激响应的时间样本数，指定为标量。设置 `Modeling delay (samples)` 可确保基带等效模型具有因果响应。

有关 Input Port 模块如何应用此延迟以确保因果响应的信息，请参阅 Create Complex Baseband-Equivalent Model。

### **Center frequency (Hz)** — 建模频率的中心 `2e9`（默认值） | scalar

建模频率的中心，指定为标量。有关计算建模频率的信息，请参阅 Output Port 模块参考页。

### **Sample time (s)** — 连续样本之间的时间间隔 `1e-7`（默认值） | scalar

输入信号连续样本之间的时间间隔，指定为标量。

**注意**

Input Port 模块不会从其输入信号自动继承采样时间。指定的 **Sample time (s)** 值必须与输入信号的采样时间匹配。

### **Input Processing** — 指定处理模式的类型 `Elements as channels (sample based)`（默认值） | `Columns as channels (frame based)`

将模块执行的处理模式类型指定为以下之一：

- `Elements as channels (sample based)`：如果您的模块需要基于基于样本的模型进行处理，请将 **Input processing** 设置为 `Elements as channels (sample based)`。在基于样本的处理中，模块一次处理一个样本信号。输入信号的每个元素表示不同通道中的一个样本。
- `Columns as channels (frame based)`：如果您的模块需要基于基于帧的模型进行处理，请将 **Input processing** 设置为 `Columns as channels (frame based)`。在基于帧的处理中，模块一次处理一个数据帧。每个数据帧包含来自独立通道的连续样本。每个通道由输入信号的一列表示。

### **Add noise** — 向模块添加噪声数据 `on`（默认值） | `off`

向模块添加噪声数据，指定为 `on` 或 `off`。如果选择此参数，则 Input Port 模块和 Output Port 模块所包围的 RF 物理模块中的噪声数据会被纳入考虑。如果不选择此参数，则忽略噪声数据。

### **Initial seed** — 随机数生成器模块的初始种子 `67987`（默认值） | 非负整数

用于生成噪声的随机数生成器模块的初始种子，指定为用于生成噪声的非负整数。如果选择 **Add noise** 参数，此参数将可见。如果使用变量指定初始种子参数，则每次连续运行模型时初始种子都会改变。

#### 依赖关系

要启用此参数，请选择 **Add noise** 参数。

## 所属库

RF Blockset / Equivalent Baseband / Input / Output Ports

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2006a 之前引入**

## 描述

从 Simulink 环境到 RF 物理模块的连接模块

Input Port 模块是从模型的 Simulink®（即数学）部分到模型的 RF 物理部分的连接端口。Input Port 模块允许您提供计算物理子系统的建模频率和基带等效冲激响应所需的参数数据。它还允许您指定有关如何解释传入 Simulink 信号的信息。

有关 Input Port 模块如何将数学 Simulink 信号转换为物理建模环境信号的详细信息，请参阅 Convert to and from Simulink Signals。

**注意**

某些 RF 模块使用采样时间来执行基带建模计算。为确保这些计算的准确性，Input Port 模块以及数学 RF 模块会将输入采样时间与您在 Input Port 掩码中提供的采样时间进行比较。如果二者不匹配，或者由于模块未连接而导致输入采样时间缺失，则会出现错误消息。
