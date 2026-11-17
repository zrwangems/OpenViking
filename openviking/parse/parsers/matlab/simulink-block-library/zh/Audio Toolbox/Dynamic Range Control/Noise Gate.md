---
type: simulink-block
title: 'Noise Gate'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Dynamic Range Control'
documentation_page: 'noisegate'
documentation_source_path: 'ref/noisegate.html'
language: zh-CN
chinese_source: worker-translation
---

# Noise Gate

## 端口

### 输入

### **x** — 输入信号矩阵 | 一维向量

- 矩阵输入 –– 输入的每一列被视为一个独立通道。
- 一维向量输入 –– 输入被视为单通道。

除非您指定额外的输入端口，否则此端口未命名。

**数据类型：** `single` | `double`

### **T** — 阈值 (dB) 标量

#### 依赖关系

要启用此端口，请为 Threshold (dB) 参数选择 **Specify from input port**。

**数据类型：** `single` | `double`

### **AT** — 启动时间 (s) 标量

#### 依赖关系

要启用此端口，请为 Attack time (s) 参数选择 **Specify from input port**。

**数据类型：** `single` | `double`

### **RT** — 释放时间 (s) 标量

#### 依赖关系

要启用此端口，请为 Release time (s) 参数选择 **Specify from input port**。

**数据类型：** `single` | `double`

### **HT** — 保持时间 (s) 标量

#### 依赖关系

要启用此端口，请为 Hold time (s) 参数选择 **Specify from input port**。

**数据类型：** `single` | `double`
### 输出

### **Y** — 输出信号矩阵

Noise Gate 模块输出的信号与输入信号具有相同的数据类型。输出的大小取决于输入的大小：

- 矩阵输入 –– 模块输出与输入信号大小和数据类型相同的矩阵。
- 一维向量输入 –– 模块输出 *N*×1 矩阵（列向量），其中 *N* 是一维向量中的元素数量。

在您选择 **Output gain (dB)** 参数之前，此端口未命名。

**数据类型：** `single` | `double`

### **G** — 应用于每个输入样本的增益矩阵

#### 依赖关系

要启用此端口，请选择 **Output gain (dB)** 参数。

**数据类型：** `single` | `double`

## 参数

如果参数被列为可调，则您可以在仿真期间更改其值。

#### 主选项卡

### **Threshold (dB)** — 操作阈值 `–10`（默认）| 范围 –140 到 0（含）的标量

*操作阈值*是低于该电平即对输入信号应用增益的电平。

要从输入端口指定 **Threshold (dB)**，请为该参数选择 **Specify from input port**。

**可调：** 是

### **View static characteristic** — 打开动态范围门限的静态特性图 按钮

当 Noise Gate 模块的参数更改时，该图会自动更新。

**可调：** 是

### **Attack time (s)** — 应用增益上升的时间 `0.05`（默认）| 范围 0 到 4（含）的标量

*启动时间*是当输入低于阈值时，应用增益从其最终值的 10% 上升到 90% 所需的时间。**Attack time (s)** 参数平滑应用增益曲线。

要从输入端口指定 **Attack time (s)**，请为该参数选择 **Specify from input port**。

**可调：** 是

### **Release time (s)** — 应用增益下降的时间 `0.2`（默认）| 范围 0 到 4（含）的标量

*释放时间*是当输入高于阈值时，应用增益从其最终值的 90% 下降到 10% 所需的时间。**Release time (s)** 参数平滑应用增益曲线。

要从输入端口指定 **Release time (s)**，请为该参数选择 **Specify from input port**。

**可调：** 是

### **Hold time (s)** — 应用增益保持稳定的时间 `0.05`（默认）| 范围 0 到 4 的标量

*保持时间*是当输入电平降至阈值以下时，（负）增益在开始向其稳态值下降之前保持的时段。

要从输入端口指定 **Hold time (s)**，请为该参数选择 **Specify from input port**。

**可调：** 是

### **Inherit sample rate from input** — 指定输入采样率的来源 `on`（默认）| `off`

当您选择此参数时，模块从输入信号继承其采样率。当您清除此参数时，您在 **Input sample rate (Hz)** 中指定采样率。

**可调：** 否

### **Input sample rate (Hz)** — 指定输入采样率 `44100`（默认）| 标量

**可调：** 是

#### 依赖关系

要启用此参数，请清除 **Inherit sample rate from input** 参数。

#### 高级选项卡

### **Output gain (dB)** — 应用于每个输入样本的增益 `off`（默认）| `on`

当您选择此参数时，一个额外的输出端口 **G** 会添加到模块中。**G** 端口输出以 dB 为单位应用于每个输入通道的增益。

**可调：** 否

### **Sidechain** — 启用边链输入 `off`（默认）| `on`

当您选择此参数时，一个额外的输入端口 **SC** 会添加到模块中。**SC** 端口使用单独的边链信号对输入信号 **x** 进行动态范围门限处理。

输入到 **SC** 端口的数据类型和（帧）长度必须与输入到 **x** 端口的相同。

边链输入的通道数必须等于 `x` 的通道数或等于一。

- `Sidechain channel count is equal to one` –– 基于此通道计算出的增益 `G` 应用于 `x` 的所有通道。
- `Sidechain channel count is equal to channel count of``x` –– 为每个边链通道计算出的增益 `G` 应用于 `x` 的对应通道。

**可调：** 否

### **Simulate using** — 指定要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

- `Interpreted execution` –– 使用 MATLAB® 解释器仿真模型。此选项缩短启动时间，并且仿真速度与 `Code generation` 相当。在此模式下，您可以调试模块的源代码。
- `Code generation` –– 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不更改，C 代码会在后续仿真中重用。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。

**可调：** 否

## 所属库

Audio Toolbox / Dynamic Range Control

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

## 描述

动态范围门限

Noise Gate 模块独立地对每个输入通道执行动态范围门限处理。动态范围门限抑制低于给定阈值的信号。该模块使用指定的启动、释放和保持时间来实现平滑的应用增益曲线。
