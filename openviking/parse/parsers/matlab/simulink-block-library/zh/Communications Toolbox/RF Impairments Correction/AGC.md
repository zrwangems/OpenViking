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

输入信号，指定为列向量。此端口在模块掩码中未命名。

**数据类型：** `single` | `double` | `int` | `uint`
**复数支持：** 是

### 输出

### **y** — 输出信号 *N*S 元素列向量

输出信号，返回为 *N*S 元素列向量。*N*S 是输入信号的长度。输出信号的数据类型与输入信号相同。

### **Px** — 功率水平估计 *N*S 元素列向量

功率水平估计，返回为 *N*S 元素列向量。*N*S 是输入信号的长度。您可以将 `powerlevel` 用作能量检测器输出。

#### 依赖关系

要启用此端口，请选中 **启用估计输入功率输出** 参数。

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上的 **准备** 库中，选择 **属性检查器**。

### **增益更新步长** — 增益更新步长 `0.01` | 正标量

增益更新步长，指定为正标量。增大步长可使 AGC 更快响应输入信号电平的变化，但会增加达到稳态运行后输出信号电平的变化。有关详细信息，请参阅 AGC 性能标准。

### **目标输出功率水平** — 目标输出功率水平 (W) `1` | 正标量

目标输出功率水平，指定为正标量。功率水平以 watts 为单位，参考 1 ohm。

### **平均窗口长度** — 平均窗口长度 (samples) `100` | 正整数

平均窗口长度（以 samples 为单位），指定为正整数。有关平均长度如何影响稳态运行中 AGC 输出信号的方差以及执行速度的详细信息，请参阅提示。

### **最大功率增益** — 最大功率增益 (dB) `60`（默认）| 正标量

最大功率增益，以 dB 为单位，指定为正标量。当小输入信号功率突然增大时，大的增益调整可能导致削波。使用此属性可通过限制 AGC 应用于输入信号的增益来避免大的增益调整。有关示例，请参阅比较不同最大增益下的 AGC 性能。

### **启用估计输入功率输出** — 输出估计输入功率的选项 off（默认）| on

选中此复选框可提供输出端口 `Px`，该端口返回输入信号功率的估计值。

### **仿真方式** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

要运行的仿真类型，指定为 `Interpreted execution` 或 `Code generation`。

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项需要的启动时间较少，但后续仿真的速度比使用 `Code generation` 选项时慢。在此模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为模块生成 C 代码。除非模型发生变化，否则模型会在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度比使用 `Interpreted execution` 选项时更快。

有关详细信息，请参阅解释执行与代码生成 (Simulink)。

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

自动增益控制器 (AGC) 模块自适应调整其增益，以在输出端实现恒定信号电平。

此图标显示带可选 Px 端口的 AGC 模块。显示了带可选端口的 AGC 模块
