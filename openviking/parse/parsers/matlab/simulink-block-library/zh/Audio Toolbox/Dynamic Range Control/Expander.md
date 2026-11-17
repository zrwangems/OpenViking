---
type: simulink-block
title: 'Expander'
family: 'dynamic-range-control'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Dynamic Range Control'
documentation_page: 'expander'
documentation_source_path: 'ref/expander.html'
language: zh-CN
chinese_source: worker-translation
---

# Expander

## 端口

### 输入

### **x** — 输入信号矩阵 | 1-D 向量

- 矩阵输入 –– 输入的每一列被视为独立通道。
- 1-D 向量输入 –– 输入被视为单通道。

除非指定其他输入端口，否则此端口未命名。

**数据类型：** `single` | `double`

### **R** — Ratio 标量

#### 依赖关系

要启用此端口，请为 Ratio 参数选择 **Specify from input port**。

**数据类型：** `single` | `double`

### **T** — Threshold (dB) 标量

#### 依赖关系

要启用此端口，请为 Threshold (dB) 参数选择 **Specify from input port**。

**数据类型：** `single` | `double`

### **K** — Knee width (dB) 标量

#### 依赖关系

要启用此端口，请为 Knee width (dB) 参数选择 **Specify from input port**。

**数据类型：** `single` | `double`

### **AT** — Attack time (s) 标量

#### 依赖关系

要启用此端口，请为 Attack time (s) 参数选择 **Specify from input port**。

**数据类型：** `single` | `double`

### **RT** — Release time (s) 标量

#### 依赖关系

要启用此端口，请为 Release time (s) 参数选择 **Specify from input port**。

**数据类型：** `single` | `double`

### **HT** — Hold time (s) 标量

#### 依赖关系

要启用此端口，请为 Hold time (s) 参数选择 **Specify from input port**。

**数据类型：** `single` | `double`
### 输出

### **Y** — 输出信号矩阵

Expander 模块输出的信号与输入信号具有相同的数据类型。输出的大小取决于输入的大小：

- 矩阵输入 –– 模块输出与输入信号大小和数据类型相同的矩阵。
- 1-D 向量输入 –– 模块输出 *N*×1 矩阵（列向量），其中 *N* 是 1-D 向量中的元素数。

在选择 **Output gain (dB)** 参数之前，此端口未命名。

**数据类型：** `single` | `double`

### **G** — 应用于每个输入样本的增益矩阵

#### 依赖关系

要启用此端口，请选择 **Output gain (dB)** 参数。

**数据类型：** `single` | `double`

## 参数

如果参数列为可调，则可以在仿真期间更改其值。

#### 主选项卡

### **Ratio** — 扩展比 `5`（默认值）| 1 到 50（含）范围内的标量

*扩展比* 是低于操作阈值的信号的输入/输出比。

假设具有硬拐点特性且稳态输入满足 *x*[*n*] dB < **Threshold (dB)**，则扩展比定义为 R=(y[n]−T)(x[n]−T)，其中

- *R* 是扩展比。
- *y*[*n*] 是以 dB 为单位的输出信号。
- *x*[*n*] 是以 dB 为单位的输入信号。
- *T* 是以 dB 为单位的阈值。

要从输入端口指定 **Ratio**，请为该参数选择 **Specify from input port**。

**可调：** Yes

### **Threshold (dB)** — 操作阈值 `–10`（默认值）| –140 到 0（含）范围内的标量

*操作阈值* 是低于该级别时将增益应用于输入信号的级别。

要从输入端口指定 **Threshold (dB)**，请为该参数选择 **Specify from input port**。

**可调：** Yes

### **Knee width (dB)** — 压缩特性中的过渡区域 `0`（默认值）| 0 到 20 范围内的标量

对于软拐点特性，过渡区域由以下关系定义

y=x+(1−R)×(x−T−W2)2(2×W)

在范围 (2×|x−T|)≤W 内，其中

- *y* 是以 dB 为单位的输出电平。
- *x* 是以 dB 为单位的输入电平。
- *R* 是扩展比。
- *T* 是以 dB 为单位的阈值。
- *W* 是以 dB 为单位的拐点宽度。

要从输入端口指定 **Knee width (dB)**，请为该参数选择 **Specify from input port**。

**可调：** Yes

### **View static characteristic** — 打开动态范围扩展器的静态特性图按钮

当 Expander 模块的参数更改时，绘图会自动更新。

**可调：** Yes

### **Attack time (s)** — 应用增益斜坡上升的时间 `0.05`（默认值）| 0 到 4（含）范围内的标量

*起音时间* 是当输入低于阈值时，扩展器增益从其最终值的 10% 上升到 90% 所需的时间。**Attack time (s)** 参数会平滑应用增益曲线。

要从输入端口指定 **Attack time (s)**，请为该参数选择 **Specify from input port**。

**可调：** Yes

### **Release time (s)** — 应用增益斜坡下降的时间 `0.2`（默认值）| 0 到 4（含）范围内的标量

*释放时间* 是当输入高于阈值时，扩展器增益从其最终值的 90% 下降到 10% 所需的时间。**Release time (s)** 参数会平滑应用增益曲线。

要从输入端口指定 **Release time (s)**，请为该参数选择 **Specify from input port**。

**可调：** Yes

### **Hold time (s)** — 应用增益保持稳定的时间 `0.05`（默认值）| 0 到 4（含）范围内的标量

*保持时间* 是当输入电平降至阈值以下时，在（负）增益开始朝其稳态值减小之前保持该增益的时段。

要从输入端口指定 **Hold time (s)**，请为该参数选择 **Specify from input port**。

**可调：** Yes

### **Inherit sample rate from input** — 指定输入采样率的来源 `on`（默认值）| `off`

选择此参数时，模块从输入信号继承其采样率。清除此参数时，请在 **Input sample rate (Hz)** 参数中指定采样率。

**可调：** No

### **Input sample rate (Hz)** — 输入的采样率 `44100`（默认值）| 正标量

**可调：** Yes

#### 依赖关系

要启用此参数，请清除 **Inherit sample rate from input** 参数。

#### 高级选项卡

### **Output gain (dB)** — 应用于每个输入样本的增益 `off`（默认值）| `on`

选择此参数时，模块会添加一个额外的输出端口 **G**。**G** 端口以 dB 为单位输出应用于每个输入通道的增益。

**可调：** No

### **Sidechain** — 启用侧链输入 `off`（默认值）| `on`

选择此参数时，模块会添加一个额外的输入端口 **SC**。**SC** 端口使用单独的侧链信号对输入信号 **x** 启用动态范围扩展。

输入到 **SC** 端口的数据类型和（帧）长度必须与输入到 **x** 端口的数据类型和（帧）长度相同。

侧链输入的通道数必须等于 `x` 的通道数，或者等于一。

- `Sidechain channel count is equal to one` –– 基于此通道计算出的增益 `G` 会应用于 `x` 的所有通道。
- `Sidechain channel count is equal to channel count of``x` –– 针对每个侧链通道计算出的增益 `G` 会应用于 `x` 的对应通道。

**可调：** No

### **Simulate using** — 指定要运行的仿真类型 `Interpreted execution`（默认值）| `Code generation`

- `Interpreted execution` –– 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，并且仿真速度与 `Code generation` 相当。在此模式下，您可以调试模块的源代码。
- `Code generation` –– 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，后续仿真会重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。

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

动态范围扩展器

Expander 模块跨每个输入通道独立执行动态范围扩展。动态范围扩展会衰减低于给定阈值的安静声音的音量。该模块使用指定的起音、释放和保持时间来实现平滑的应用增益曲线。
