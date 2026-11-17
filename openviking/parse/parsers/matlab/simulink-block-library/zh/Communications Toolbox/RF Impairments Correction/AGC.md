---
type: simulink-block
title: 'AGC'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'RF Impairments Correction'
documentation_page: 'agc'
documentation_source_path: 'ref/agc.html'
language: zh-CN
chinese_source: worker-translation
---

# AGC

## 端口

### 输入

### **In** — 输入信号列向量

输入信号，指定为列向量。此端口在模块掩码上未命名。

**数据类型：** `single` | `double` | `int` | `uint`
**复数支持：** 是
### 输出

### **y** — 输出信号 *N*S 元素列向量

输出信号，以 *N*S 元素列向量形式返回。
*N*S 是输入信号的长度。输出信号的数据类型与输入信号相同。

### **Px** — 功率电平估计 *N*S 元素列向量

功率电平估计，以 *N*S 元素列向量形式返回。
*N*S 是输入信号的长度。您可以将 `powerlevel` 用作能量检测器输出。

#### 依赖关系

要启用此端口，请选中 **Enable output of estimated input power** 参数。

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### **Step size for gain updates** — 增益更新的步长 `0.01` | 正标量

增益更新的步长，指定为正标量。增大步长可使 AGC 更快地响应输入信号电平的变化，但会增加达到稳态运行后输出信号电平的变化。有关详细信息，请参阅 AGC Performance Criteria。

### **Target output power level** — 目标输出功率电平 (W) `1` | 正标量

目标输出功率电平，指定为正标量。功率电平以瓦特为单位，参考 1 欧姆。

### **Length of averaging window** — 平均窗口长度（样本） `100` | 正整数

平均窗口长度（以样本为单位），指定为正整数。有关平均长度如何影响稳态运行中 AGC 输出信号的方差以及执行速度的详细信息，请参阅 Tips。

### **Maximum power gain** — 最大功率增益 (dB) `60`（默认）| 正标量

最大功率增益（以 dB 为单位），指定为正标量。当较小的输入信号功率突然增大时，较大的增益调整可能导致削波。使用此属性通过限制 AGC 应用于输入信号的增益来避免大幅增益调整。有关示例，请参阅 Compare AGC Performance for Different Maximum Gains。

### **Enable output of estimated input power** — 输出估计输入功率的选项 off（默认）| on

选中此复选框可提供一个输出端口 `Px`，该端口返回输入信号功率的估计值。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

要运行的仿真类型，指定为 `Interpreted execution` 或 `Code generation`。

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项需要较少的启动时间，但后续仿真的速度比使用 `Code generation` 选项时慢。在此模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。除非模型发生变化，否则模型会在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度比使用 `Interpreted execution` 选项时更快。

有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。

## 所属库

Communications Toolbox / RF Impairments Correction

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013a 中引入**

## 描述

自适应调整增益以实现恒定信号电平输出

自动增益控制器 (AGC) 模块自适应地调整其增益，以在输出端实现恒定的信号电平。

此图标显示了带有可选 Px 端口的 AGC 模块。显示了带有可选端口的 AGC 模块
