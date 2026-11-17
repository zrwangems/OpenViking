---
type: simulink-block
title: 'Power Amplifier'
family: 'idealized-baseband'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Idealized Baseband'
documentation_page: 'poweramplifieridealizedbaseband'
documentation_source_path: 'ref/poweramplifieridealizedbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# Power Amplifier

## 端口

### 输入

### **Port\_1** — 时变输入信号列

时变输入信号，指定为列。列表示连续的时间点。

**数据类型：** `double` | `single`

### 输出

### **Port\_1** — 时变输出信号复数列

时变输出信号，以复数列形式返回。输出时变信号的大小与输入时变信号相同。

**数据类型：** `double` | `single`

## 参数

### **Model** — 用于设计放大器的模型 `Memory polynomial` (默认) | `Cross-term memory`

使用 `Memory polynomial` 模型或 `Cross-term memory` 模型来设计功率放大器。下表总结了这两种模型的特性。

| 模型 | 表征数据 | 系数类型 | 带内频谱再生 | 带外谐波生成 |
| --- | --- | --- | --- | --- |
| `Memory polynomial` (默认) | 带通 (I,Q) | 2-D Complex matrix | 是 | 否 |
| `Cross-term memory` | 带通 (I,Q) | 2-D Complex matrix | 是 | 否 |

有关详细信息，请参阅 Power Amplifier 模块中的 Model Type。

**Model Type** 参数已重命名为 **Model**。*(自 R2024a 起)*

### **Coefficient matrix** — 系数矩阵 `1+0i` (默认) | 2-D complex matrix

系数矩阵，对于 `Memory polynomial` 和 `Cross-term memory` 模型，指定为 2-D complex matrix。

对于 `Memory polynomial` 和 `Cross-term memory` 模型，您可以基于测得的复数 (I,Q) 输出对输入放大器特性来辨识复数系数矩阵。例如，请参阅 Coefficient Matrix Computation 中的辅助函数。

矩阵的大小取决于延迟数量以及系统非线性阶数。

- 对于 `Memory polynomial` 模型，矩阵的维度为 记忆深度 (mem)×电压阶数 (deg)。
- 对于 `Cross-term memory` 模型，矩阵的维度为 记忆深度 (mem)×{记忆深度 (mem)⋅(电压阶数 (deg)−1)+1}。

### **Measured interval of PA data (s)** — 测得的输入-输出数据的采样时间 `1e-6` (默认) | positive scalar

模块用于构造系数矩阵的输入-输出数据的采样时间，以秒为单位。

**Time interval of measured PA data (s)** 参数已重命名为 **Measured interval of PA data (s)**。*(自 R2023b 起)*

### **Simulate using** — 要运行的仿真类型 `Code generation` (默认) | `Interpreted execution`

要运行的仿真类型，指定为以下之一：

- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，C 代码会复用于后续仿真。此选项需要额外的启动时间，但后续仿真的速度快于 `Interpreted execution`。
- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项缩短启动时间，但后续仿真的速度慢于 `Code generation`。在此模式下，您可以调试模块的源代码。

## 所属库

RF Blockset / Idealized Baseband

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

### R2024a：Idealized Baseband 库中 Power Amplifier 模块的参数已重命名

Idealized Baseband 库中 Power Amplifier 模块的以下内容已重命名或更改：

- **Model Type** 参数已重命名为 **Model**。
- **Model** 参数中的 `Cross-Term Memory` 值已重命名为 `Cross-term memory`。
- **Coefficient Matrix** 参数的默认值已从 `1` 更新为 `1+0i`。

当您打开在 R2024a 之前创建的包含 Power Amplifier 模块的模型时，软件会替换以下内容：

- 将 **Model Type** 参数替换为 **Model** 参数。
- 将 `Cross-Term Memory` 值替换为 `Cross-term memory` 值。
- 将 **Coefficient Matrix** 参数的默认值从 `1` 替换为 `1+0i`。

### R2023b：Idealized Baseband 库中 Power Amplifier 模块的参数已重命名

Idealized Baseband 库中 Power Amplifier 模块的 **Time interval of measured PA data (s)** 参数已重命名为 **Measured interval of PA data (s)**。

当您打开在 R2023b 之前创建的包含 Power Amplifer 模块的模型时，软件会将 **Time interval of measured PA data (s)** 参数名称替换为 **Measured interval of PA data (s)**。

## 描述

对具有记忆效应的窄带功率放大器建模

Power Amplifier 模块使用由 Volterra 级数导出的记忆多项式表达式来对双端口功率放大器建模。Volterra 级数对输入和输出信号之间的非线性关系建模。此模块包含记忆效应：输出响应取决于当前输入信号以及先前时刻的输入信号。当向您的 RF 系统发射窄带信号时，请使用此模块。

Power Amplifier 模块的封装图标是动态的，并显示 **Model** 参数中指定的模型。

| Model: `Memory polynomial` | Model: `Cross-term memory` |
| --- | --- |
| Power Amplifier 模块图标，其中 Model 参数设置为 Memory Polynomial。 | Power Amplifier 模块图标，其中 Model 参数设置为 Cross-Term Memory。 |
