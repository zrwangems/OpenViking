---
type: simulink-block
title: 'Input Port'
family: 'simrf'
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
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: Treat input Simulink signal as
  summary: 用于解释输入 Source voltage 的选项（默认）| Incident power wave | 标量
  group: ''
- name: Source impedance (ohms)
  summary: RF 网络的源阻抗 50（默认）| 标量
  group: ''
- name: Finite impulse response filter length
  summary: 基带等效冲激响应的期望长度 128（默认）| 标量
  group: ''
- name: Fractional bandwidth of guard bands
  summary: 建模带宽的比例 0（默认）| 标量
  group: ''
- name: Modeling delay (samples)
  summary: 延迟基带等效模型冲激响应的时间采样数 0（默认）| 标量
  group: ''
- name: Center frequency (Hz)
  summary: 建模频率的中心 2e9（默认）| 标量
  group: ''
- name: Sample time (s)
  summary: 连续采样之间的时间间隔 1e-7（默认）| 标量
  group: ''
- name: Input Processing
  summary: 指定处理模式的类型 Elements as channels (sample based)（默认）| Columns as channels (frame based)
  group: ''
- name: Add noise
  summary: 向模块添加噪声数据 on（默认）| off
  group: ''
- name: Initial seed
  summary: 随机数生成器模块的初始种子 67987（默认）| 非负整数
  group: ''
```

### **Treat input Simulink signal as** — 用于解释输入 `Source voltage` 的选项（默认）| `Incident power wave` | 标量

用于解释输入 Simulink 信号的选项，指定为以下之一：

- `Incident power wave` — 将输入信号解释为
  其所连接物理模型中描述的 RF 系统的入射功率波。当您选择此选项时，RF 系统的输出信号为
  发射功率波。这是最常见的 RF 建模解释。
- `Source voltage` — 将输入信号解释为
  其所连接物理模型中描述的 RF 系统的源电压。因此，
  基带等效模型包含通过源阻抗的损耗。当
  您选择此选项时，RF 系统的输出信号为负载电压。

有关这些选项的详细信息，请参阅 Convert to and from Simulink Signals。

### **Source impedance (ohms)** — RF 网络的源阻抗 `50`（默认）| 标量

其所连接物理模型中描述的 RF 网络的源阻抗，
以欧姆为单位指定为标量。

### **Finite impulse response filter length** — 基带等效冲激响应的期望长度 `128`（默认）| 标量

物理模型的基带等效冲激响应的期望长度，
指定为标量。时域中的 FIR 滤波器越长，频域中的频率
分辨率越精细。频率分辨率约等于 1/
（**Finite impulse response filter length**\***Sample time
(s)**）。有关此参数的图形表示，请参阅 Baseband-Equivalent Modeling。

**注意**

等效基带仿真算法在其计算中使用大于指定滤波器长度的下一个 2 的幂，然后将冲激响应截断为
指定长度。因此，当您将 **Finite
impulse response filter length** 参数设置为不是 2 的幂的数时，会得到不同的结果。
有关详细信息，请参阅 Calculate the Baseband-Equivalent Impulse Response。

### **Fractional bandwidth of guard bands** — 建模带宽的比例 `0`（默认）| 标量

建模带宽的比例，指定为标量。在创建
基带等效模型时，对系统传递函数的边缘进行渐变的建模带宽比例。此参数定义使用
Tukey 窗（即余弦渐变窗）进行渐变的区段带宽与恒定（即未渐变）区段带宽的比值。

小于或等于 0 的值告诉 Input Port 模块使用矩形
（`rectwin`（Signal Processing Toolbox））窗。大于或等于 1 的值告诉 Input Port 模块
使用 hann 窗。

### **Modeling delay (samples)** — 延迟基带等效模型冲激响应的时间采样数 `0`（默认）| 标量

延迟基带等效模型冲激响应的时间采样数，
指定为标量。设置 `Modeling delay (samples)` 可确保
基带等效模型具有因果响应。

有关 Input Port 模块如何应用此延迟以确保因果响应的信息，请参阅 Create Complex Baseband-Equivalent Model。

### **Center frequency (Hz)** — 建模频率的中心 `2e9`（默认）| 标量

建模频率的中心，指定为标量。有关计算建模
频率的信息，请参阅 Output
Port 模块参考页。

### **Sample time (s)** — 连续采样之间的时间间隔 `1e-7`（默认）| 标量

输入信号连续采样之间的时间间隔，指定为标量。

**注意**

Input Port 模块不会自动从其输入信号继承采样时间。
指定的 **Sample time (s)** 值必须与输入信号的采样时间匹配。

### **Input Processing** — 指定处理模式的类型 `Elements as channels (sample based)`（默认）| `Columns as channels (frame based)`

将模块执行的处理模式类型指定为以下之一：

- `Elements as channels (sample based)`：如果您的模块需要基于 sample-based 模型进行处理，请将 **Input processing** 设置为 `Elements as channels (sample based)`。在 sample-based 处理中，模块一次处理一个采样。输入信号的每个元素表示不同通道中的一个采样。
- `Columns as channels (frame based)`：如果您的模块需要基于 frame-based 模型进行处理，请将 **Input processing** 设置为 `Columns as channels (frame based)`。在 frame-based 处理中，模块一次处理一帧数据。每帧数据包含来自独立通道的连续采样。每个通道由输入信号的一列表示。

### **Add noise** — 向模块添加噪声数据 `on`（默认）| `off`

向模块添加噪声数据，指定为 `on` 或 `off`。
如果选择此参数，则会考虑由 Input Port 模块和 Output Port 模块括起来的 RF physical 模块中的噪声数据。如果不选择此参数，则忽略噪声数据。

### **Initial seed** — 随机数生成器模块的初始种子 `67987`（默认）| 非负整数

随机数生成器模块用于生成噪声的初始种子，指定为非负整数以生成噪声。如果选择 **Add noise** 参数，此参数将可见。如果使用变量指定初始种子参数，则每次运行模型时初始种子都会改变。

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

从 Simulink 环境到 RF physical 模块的连接模块

Input Port 模块是从模型的 Simulink®（或数学）部分到模型 RF physical 部分的连接端口。Input Port 模块允许您提供计算物理子系统建模频率和基带等效冲激响应所需的参数数据。它还允许您指定有关如何解释传入 Simulink 信号的信息。

有关 Input Port 模块如何将数学 Simulink 信号转换为物理建模环境信号的详细信息，请参阅 Convert to and from Simulink Signals。

**注意**

某些 RF 模块使用采样时间执行基带建模计算。为确保这些计算的准确性，Input Port 模块以及数学 RF 模块会将输入采样时间与您在 Input Port 掩码中提供的采样时间进行比较。如果它们不匹配，或者由于模块未连接而缺少输入采样时间，则会出现错误消息。
