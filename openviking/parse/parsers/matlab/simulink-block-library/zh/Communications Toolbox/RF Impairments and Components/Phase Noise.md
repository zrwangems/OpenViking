---
type: simulink-block
title: 'Phase Noise'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'RF Impairments and Components'
documentation_page: 'phasenoise'
documentation_source_path: 'ref/phasenoise.html'
language: zh-CN
chinese_source: worker-translation
---

# Phase Noise

## 端口

### 输入

### **In** — 输入信号向量 | 矩阵

输入信号，指定为
*N*S-by-1 数值向量或
*N*S-by-*M*
数值矩阵。*N*S 表示
样本数，*M* 表示
通道数。

**数据类型：** `double` | `single`
**复数支持：** Yes
### 输出

### **Out** — 输出信号向量 | 矩阵

输出信号，返回为复值信号，其数据类型和大小与输入信号相同。

## 参数

要交互式编辑模块参数，请使用
属性检查器。在 Simulink 工具条的 **仿真** 选项卡上的
**准备** 库中，选择 **属性检查器**。

### **相位噪声电平 (dBc/Hz)** — 相位噪声电平 `[-80 -100]`（默认） | 负标量向量

相位噪声电平，以相对于载波每赫兹的分贝（dBc/Hz）为单位，指定为负标量向量。**相位噪声电平 (dBc/Hz)** 和 **频率偏移 (Hz)** 参数必须具有相同长度。

### **频率偏移 (Hz)** — 频率偏移 `[2000 20000]`（默认） | 正递增值的向量

频率偏移，以 Hz 为单位，指定为正递增值的向量。最大频率偏移值必须小于 *F*S / 2，其中 *F*S 表示 **采样率 (Hz)** 参数值。

**相位噪声电平 (dBc/Hz)** 和 **频率偏移 (Hz)** 参数必须具有相同长度。

### **采样率 (Hz)** — 采样率 `1e6`（默认） | 正标量

采样率，以 Hz 为单位，指定为大于 **频率偏移 (Hz)** 参数所指定最大值的两倍的正标量。

### **初始种子** — 噪声发生器的初始种子 `2137`（默认） | 正标量

噪声发生器的初始种子，指定为正标量。

此模块使用 Random Source 模块生成噪声。该模块使用 Ziggurat 方法（V5 RANDN 算法）生成随机数。每次重新运行仿真时，该模块都会重用相同的初始种子。这样，每次运行仿真时该模块都会输出相同的信号。

### **查看滤波器响应** — 显示滤波器幅值响应按钮

显示由该模块定义的滤波器的幅值响应。

### **仿真方式** — 要运行的仿真类型 `Interpreted execution`（默认） | `Code generation`

要运行的仿真类型，指定为 `Interpreted execution` 或 `Code generation`。

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项需要较少的启动时间，但后续仿真的速度比使用 `Code generation` 选项慢。在此模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。除非模型发生变化，否则模型会在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度比使用 `Interpreted execution` 选项快。

有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。

## 所属库

Communications Toolbox / RF Impairments and Components

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

### R2024a：对高频相位噪声损伤建模

使用 Phase Noise 模块准确地对更高频率信号处的相位噪声建模。使用 Phase Noise 模块封装上的 **查看滤波器响应** 按钮来验证所实现相位噪声的准确性。

## 描述

将接收机相位噪声应用于复基带信号

Phase Noise 模块向复信号添加相位噪声。该模块模拟无线通信发射机或接收机本振引入的损伤。该模块根据指定的频谱掩码生成经过滤波的相位噪声，并将其添加到输入信号。有关相位噪声建模的描述，请参阅算法。
