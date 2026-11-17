---
type: simulink-block
title: 'Symbol Synchronizer'
family: 'synchronization'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Synchronization'
documentation_page: 'symbolsynchronizer'
documentation_source_path: 'ref/symbolsynchronizer.html'
language: zh-CN
chinese_source: worker-translation
---

# Symbol Synchronizer

## 端口

### 输入

### **Samp** — 输入样本 标量（默认）| 列向量

输入样本，指定为 PAM、PSK、QAM 或 OQPSK 调制的单载波信号的标量或列向量。此端口在模块上未命名。

**数据类型：** `double` | `single`
**复数支持：** 是

### 输出

### **Sym** — 输出信号符号 标量 | 列向量

输出信号符号，返回为可变大小标量或列向量，其数据类型与输入相同。对于维度为 *N*samp-by-1 的输入，**Sym** 处的输出维度为 *N*sym-by-1。*N*sym 大约等于 *N*samp 除以 *N*sps。*N*sps 等于 **每个符号的样本数** 参数值。如果输出长度超过最大输出大小 ⌈NsampNsps×1.1⌉，则会被截断。

当未选择 **归一化定时误差输出端口** 时，此端口未命名。

### **Err** — 估计的定时误差 标量 | 列向量

每个输入样本的估计定时误差，返回为值在范围 [0, 1] 内的标量或列向量。估计的定时误差由输入样本时间归一化。**Err** 与输入信号具有相同的数据类型和大小。

#### 依赖项

要启用此端口，请选择 **归一化定时误差输出端口**。

## 参数

要交互式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上，在 **准备** 库中，选择 **属性检查器**。

### **调制类型** — 调制类型 `PAM/PSK/QAM`（默认）| `OQPSK`

调制类型，指定为 `PAM/PSK/QAM` 或 `OQPSK`。使用 OQPSK 调制时，请参阅提示。

### **定时误差检测器** — 定时误差检测器类型 `Zero-Crossing (decision-directed)`（默认）| `Gardner (non-data-aided)` | `Early-Late (non-data-aided)` | `Mueller-Muller (decision-directed)`

定时误差检测器类型，指定为 `Zero-Crossing (decision-directed)`、`Gardner (non-data-aided)`、`Early-Late (non-data-aided)` 或 `Mueller-Muller (decision-directed)`。此参数指定同步器中使用的定时误差检测方案。

有关详细信息，请参阅定时误差检测 (TED)。

### **每个符号的样本数** — 每个符号的样本数 `2`（默认）| 大于 1 的正整数

每个符号的样本数，指定为大于 1 的正整数。有关详细信息，请参阅环路滤波器中的 *N*sps。

### **阻尼因子** — 环路滤波器的阻尼因子 `1`（默认）| 正标量

环路滤波器的阻尼因子，指定为正标量。有关详细信息，请参阅环路滤波器中的 *ζ*。

**可调：** 是

### **归一化环路带宽** — 环路滤波器的归一化带宽 `0.01`（默认）| 小于 1 的正标量

环路滤波器的归一化带宽，指定为小于 1 的正标量。环路带宽 (*B*n) 由输入信号的符号率 (*T*s) 归一化。有关详细信息，请参阅环路滤波器中的 *B*n*T*s。

**注意**

为确保符号同步器锁定，请将 **归一化环路带宽** 参数设置为小于 `0.1` 的值。

**可调：** 是

### **检测器增益** — 相位检测器增益 `2.7`（默认）| 正标量

相位检测器增益，指定为正标量。有关详细信息，请参阅环路滤波器中的 *K*p。

**可调：** 是

### **归一化定时误差输出端口** — 启用归一化定时误差输出端口 `on`（默认）| `off`

选择此参数可在输出端口 **Err** 处输出归一化定时误差数据。

### **仿真方式** — 要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

要运行的仿真类型，指定为 `Code generation` 或 `Interpreted execution`。

- `Code generation` — 通过使用生成的 C 代码对模型进行仿真。首次运行仿真时，Simulink 会为该模块生成 C 代码。除非模型发生变化，否则模型会在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度快于 `Interpreted execution` 选项。
- `Interpreted execution` — 通过使用 MATLAB® 解释器对模型进行仿真。此选项可缩短启动时间，但后续仿真的速度慢于 `Code generation` 选项。在此模式下，您可以调试模块的源代码。

有关详细信息，请参阅解释执行与代码生成 (Simulink)。

## 所属库

Communications Toolbox / Synchronization

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015a 中引入**

## 描述

校正符号定时时钟偏移

Symbol Synchronizer 模块校正单载波发射机与接收机之间针对 PAM、PSK、QAM 或 OQPSK 调制方案的符号定时时钟偏移。有关详细信息，请参阅符号同步概述。

**注意**

输入信号以采样率为基础运行，而输出信号以符号率为基础运行。
