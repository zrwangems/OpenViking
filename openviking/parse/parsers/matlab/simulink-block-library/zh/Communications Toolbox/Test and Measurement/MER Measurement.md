---
type: simulink-block
title: 'MER Measurement'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Test and Measurement'
documentation_page: 'mermeasurement'
documentation_source_path: 'ref/mermeasurement.html'
language: zh-CN
chinese_source: worker-translation
---

# MER Measurement

## 端口

### 输入

### **Ref** — 参考信号 标量 | 向量 | 矩阵 | 三维数组

参考信号，指定为标量、向量、矩阵或三维数组。
如果指定此输入，该模块将此输入用作参考星座，测量 `Rcv` 输入的 MER。

此输入的维度必须与 `Rcv` 输入的维度匹配。该模块将此输入的每个元素用作 `Rcv` 输入对应元素的参考符号。

#### 依赖关系

要启用此端口，请将 **Reference signal** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** Yes

### **Rcv** — 接收信号 标量 | 向量 | 矩阵 | 三维数组

接收信号，指定为标量、向量、矩阵或三维数组。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** Yes
### 输出

### **MS** — 接收信号的百分比 MER 标量

在配置的测量区间内接收信号的百分比 MER，以分贝为单位返回标量。

**数据类型：** `double`

### **min** — 最小百分比 MER 标量

在配置的测量区间内的最小百分比 MER，以分贝为单位返回标量。

#### 依赖关系

要启用此端口，请选择 **Output minimum MER** 参数。

**数据类型：** `double`

### **X%** — 有 *X*% 的 MER 测量值低于此值的标量

自上次重置以来，有 *X*% 的 MER 测量值低于此值，以分贝为单位返回标量。在 **X-percentile value (%)** 参数中设置 *X* 的值。

#### 依赖关系

要启用此端口，请选择 **Output X-percentile MER** 参数。

**数据类型：** `double`

### **nSym** — 符号数 正整数

该模块用于测量输出的符号数，以正整数返回。

#### 依赖关系

要启用此端口，请选择 **Output X-percentile MER** 和 **Output the number of symbols processed** 参数。

**数据类型：** `double`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### **Reference signal** — 参考信号源 `Input port` | `Estimated from reference constellation`

参考信号源，指定为 `Input port` 或 `Estimated from reference constellation`。

### **Reference constellation** — 参考星座 `constellation(pskmod((0:3)',4,pi/4,"bin"))`（默认） | 向量

参考星座点，指定为复数值或实数值的向量。

#### 依赖关系

要启用此参数，请将 **Reference signal** 参数设置为 `Estimated from reference constellation`。

### **Measurement interval** — 测量区间源 `Input length`（默认） | `Entire history` | `Custom` | `Custom with periodic reset`

MER 和最小 MER 测量的测量区间源，指定为以下值之一。

- `Input length` — 仅使用当前样本测量 MER。
- `Entire history` — 测量所有样本的 MER。
- `Custom` — 在您指定的区间上使用滑动窗口测量 MER。
- `Custom with periodic reset` — 在您指定的区间上测量 MER，并在每个区间测量后重置模块。

### **Custom measurement interval** — 自定义测量区间 `100`（默认） | 正整数

自定义测量区间（以样本为单位），指定为正整数。

#### 依赖关系

要启用此参数，请将 **Measurement interval** 参数设置为 `Custom` 或 `Custom with periodic reset`。

### **Averaging dimensions** — 平均维度 `1`（默认） | 范围 [1, 3] 内的整数向量

该模块对 MER 测量值进行平均所沿的维度，指定为范围 [1, 3] 内的整数或整数行向量。例如，要沿列平均，请将此参数设置为 `2`。

此模块支持沿平均所在维度的可变大小输入。但是，非平均维度的输入大小必须保持不变。例如，如果输入的大小为 `[1000 3 2]`，并且您将此参数设置为 `[1 3]`，则输出大小为 `[1 3 1]`，并且第二个维度中的元素数必须固定为 `3`。

### **Output minimum MER** — 用于添加 `min` 端口以输出最小 MER 测量的选项 `Off`（默认） | `On`

用于添加 `min` 端口以输出最小 MER 测量的选项。要启用最小 MER 测量，请选择此参数。

### **Output X-percentile MER** — 用于添加 `X%` 端口以输出 *X* 百分位 MER 测量的选项 `Off`（默认） | `On`

用于添加 `X%` 端口以输出 *X* 百分位 MER 测量的选项。要启用 *X* 百分位 MER 测量，请选择此参数。选择此参数后，*X* 百分位 MER 测量将一直保留，直到重置模块。该模块使用自上次重置以来的所有输入帧执行这些测量。您可以在 **X-percentile value (%)** 参数中设置 *X* 的值。

### **X-Percentile value (%)** — 有 *X*% 的 MER 测量值低于此值 `95`（默认） | 范围 [0, 100] 内的标量

有 *X*% 的 MER 测量值低于此值，指定为范围 [0, 100] 内的标量。

#### 依赖关系

要启用此参数，请选择 **Output X-percentile MER** 参数。

### **Output the number of symbols processed** — 用于添加 `nSym` 端口以输出符号数的选项 `Off`（默认） | `On`

用于添加 `nSym` 端口以输出用于测量 *X* 百分位 MER 的符号数的选项。要测量用于 *X* 百分位 MER 测量的符号数，请选择此参数。

#### 依赖关系

要启用此参数，请选择 **Output X-percentile MER** 参数。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认） | `Code generation`

要运行的仿真类型，指定为 `Interpreted execution` 或 `Code generation`。

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项需要的启动时间较少，但后续仿真的速度比 `Code generation` 选项慢。在此模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。除非模型发生变化，否则模型会在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度比 `Interpreted execution` 选项快。

有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。

## 所属库

Communications Toolbox / Utility Blocks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

要使用此模块在模型中生成代码，必须启用 **Dynamic Memory Allocation in MATLAB Functions**。有关详细信息，请参阅 Dynamic memory allocation in MATLAB functions (Simulink)。

## 版本历史

**在 R2009b 中引入**

## 描述

在数字调制应用中测量调制误差比

MER Measurement 模块计算一种信噪比 (SNR) 测量，可用于评估接收机准确解调信号的能力。具体而言，它为接收信号返回调制误差比 (MER)、最小 MER 和百分位 MER。您可以使用 MER 测量值来确定通信应用中的系统性能。例如，要确定是否符合适用的 DVB-T 系统无线电传输标准，一致性测试需要准确的 MER 测量。

此图标显示了启用了所有端口的模块。启用了所有端口的 MER Measurement 模块
