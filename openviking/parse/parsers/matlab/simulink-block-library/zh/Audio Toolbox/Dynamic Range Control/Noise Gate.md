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

### **x** — 输入信号矩阵 | 1-D 向量

- 矩阵输入 —— 输入的每一列被视为一个独立通道。
- 1-D 向量输入 —— 输入被视为单个通道。

除非指定额外的输入端口，否则此端口未命名。

**数据类型：** `single` | `double`

### **T** — 阈值 (dB) 标量

#### 依赖关系

要启用此端口，请为 Threshold (dB) 参数选择 **Specify from input port**。

**数据类型：** `single` | `double`

### **AT** — 起音时间 (s) 标量

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

Noise Gate 模块输出与输入信号数据类型相同的信号。输出的大小取决于输入的大小：

- 矩阵输入 —— 该模块输出与输入信号大小和数据类型相同的矩阵。
- 1-D 向量输入 —— 该模块输出一个 *N*×1 矩阵（列向量），其中 *N* 是 1-D 向量中的元素数。

直到您选择 **Output gain (dB)** 参数，此端口才会命名。

**数据类型：** `single` | `double`

### **G** — 应用于每个输入样本的增益矩阵

#### 依赖关系

要启用此端口，请选择 **Output gain (dB)** 参数。

**数据类型：** `single` | `double`

## 参数

如果参数列为可调，则可以在仿真期间更改其值。

#### 主选项卡

### **Threshold (dB)** — 工作阈值 `–10`（默认）| 范围 –140 到 0（含端点）的标量

*工作阈值* 是低于该电平就会向输入信号施加增益的电平。

要从输入端口指定 **Threshold (dB)**，请为该参数选择 **Specify from input port**。

**可调：** Yes

### **View static characteristic** — 打开动态范围门静态特性图按钮

当 Noise Gate 模块的参数更改时，绘图会自动更新。

**可调：** Yes

### **Attack time (s)** — 施加增益斜坡上升的时间 `0.05`（默认）| 范围 0 到 4（含端点）的标量

*起音时间* 是当输入低于阈值时，施加增益从最终值的 10% 上升到 90% 所需的时间。**Attack time (s)** 参数会平滑施加增益曲线。

要从输入端口指定 **Attack time (s)**，请为该参数选择 **Specify from input port**。

**可调：** Yes

### **Release time (s)** — 施加增益斜坡下降的时间 `0.2`（默认）| 范围 0 到 4（含端点）的标量

*释放时间* 是当输入高于阈值时，施加增益从最终值的 90% 下降到 10% 所需的时间。**Release time (s)** 参数会平滑施加增益曲线。

要从输入端口指定 **Release time (s)**，请为该参数选择 **Specify from input port**。

**可调：** Yes

### **Hold time (s)** — 施加增益保持稳定的时间 `0.05`（默认）| 范围 0 到 4 的标量

*保持时间* 是当输入电平低于阈值时，在（负）增益开始向其稳态值减小之前保持的时段。

要从输入端口指定 **Hold time (s)**，请为该参数选择 **Specify from input port**。

**可调：** Yes

### **Inherit sample rate from input** — 指定输入采样率的来源 `on`（默认）| `off`

当您选择此参数时，该模块从输入信号继承其采样率。当您清除此参数时，您可以在 **Input sample rate (Hz)** 中指定采样率。

**可调：** No

### **Input sample rate (Hz)** — 指定输入采样率 `44100`（默认）| 标量

**可调：** Yes

#### 依赖关系

要启用此参数，请清除 **Inherit sample rate from input** 参数。

#### 高级选项卡

### **Output gain (dB)** — 应用于每个输入样本的增益 `off`（默认）| `on`

当您选择此参数时，会向该模块添加一个额外的输出端口 **G**。**G** 端口输出以 dB 为单位应用于每个输入通道的增益。

**可调：** No

### **Sidechain** — 启用侧链输入 `off`（默认）| `on`

当您选择此参数时，会向该模块添加一个额外的输入端口 **SC**。**SC** 端口可使用单独的侧链信号对输入信号 **x** 进行动态范围门控。

输入到 **SC** 端口的数据类型和（帧）长度必须与输入到 **x** 端口的相同。

侧链输入的通道数必须等于 `x` 的通道数，或等于一。

- `Sidechain channel count is equal to one` —— 基于此通道计算出的增益 `G` 会应用于 `x` 的所有通道。
- `Sidechain channel count is equal to channel count of``x` —— 为每个侧链通道计算出的增益 `G` 会应用于 `x` 的对应通道。

**可调：** No

### **Simulate using** — 指定要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

- `Interpreted execution` —— 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，并且仿真速度与 `Code generation` 相当。在此模式下，您可以调试该模块的源代码。
- `Code generation` —— 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不更改，后续仿真会重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。

**可调：** No

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

动态范围门

Noise Gate 模块对每个输入通道独立执行动态范围门控。动态范围门控会抑制低于给定阈值的信号。该模块使用指定的起音、释放和保持时间来实现平滑的施加增益曲线。
