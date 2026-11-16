---
type: simulink-block
title: 'Coarse Frequency Compensator'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'RF Impairments Correction'
documentation_page: 'coarsefrequencycompensator'
documentation_source_path: 'ref/coarsefrequencycompensator.html'
language: zh-CN
chinese_source: worker-translation
---

# Coarse Frequency Compensator

## 端口

### 输入

### **In** — 输入信号列向量

输入信号，指定为列向量。

**数据类型：** `single` | `double`
**复数支持：** Yes
### 输出

### **Out** — 补偿后的输出信号复数列向量

补偿后的输出信号，返回为复数列向量，其维度和数据类型与输入 **In** 相同。

**数据类型：** `single` | `double`

### **FreqEst** — 频率偏移的估计值，标量

频率偏移的估计值，返回为标量。

如果将 **Modulation type of input signal** 参数设置为 `OQPSK` 或 `QAM`，或将 **Estimation algorithm** 参数设置为 `FFT-based`，则返回的频率偏移估计值是 **Frequency resolution (Hz)** 参数的整数倍。

#### 依赖关系

要添加此端口，请选择 **Estimated frequency offset output port**。

**数据类型：** `single` | `double`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条中，在 **仿真** 选项卡上的 **准备** 库中，选择 **属性检查器**。

### **Modulation type of input signal** — 调制类型 `QAM`（默认） | `8PSK` | `BPSK` | `OQPSK` | `PAM` | `QPSK`

调制类型，指定为 `QAM`、`8PSK`、`BPSK`、`OQPSK`、`PAM` 或 `QPSK`。

### **Estimation algorithm** — 用于估计频率偏移的算法 `FFT-based`（默认） | `Correlation-based`

将频率偏移估计算法指定为 `FFT-based` 或 `Correlation-based`。有关详细信息，请参阅算法。

**注意**

当将 **Modulation type of input signal** 参数设置为 `'OQPSK'` 或 `'QAM'` 时，模块使用基于 FFT 的估计算法。

#### 依赖关系

此参数在将 **Modulation type of input signal** 设置为 `8PSK`、`BPSK`、`PAM` 或 `QPSK` 时显示。

### **Frequency resolution (Hz)** — 频率分辨率 `100`（默认） | 正标量

频率分辨率，以 Hz 为单位，指定为正实数标量。

#### 依赖关系

此参数在将 **Modulation type of input signal** 设置为 `OQPSK` 或 `QAM`，或将 **Estimation algorithm** 设置为 `FFT-based` 时适用。

### **Samples per symbol** — 每个符号的采样数 `4`（默认） | 大于或等于 `4` 的偶数整数

每个符号的采样数，指定为大于或等于 4 的偶数整数标量。

#### 依赖关系

此参数在将 **Modulation type of input signal** 设置为 `OQPSK` 时显示。

### **Maximum frequency offset (Hz)** — 最大可测量频率偏移 `5e3`（默认） | 正标量

最大可测量频率偏移，以 Hz 为单位，指定为正标量。

#### 依赖关系

此参数在将 **Estimation algorithm** 设置为 `Correlation-based` 时显示。

### **Estimated frequency offset output port** — 添加估计的频率偏移输出端口的选项 `on`（默认） | `off`

选中此复选框可添加 **FreqEst** 输出端口。**FreqEst** 端口输出以 Hz 为单位的估计频率偏移。

### **Simulate using** — 要运行的仿真类型 `Code generation`（默认） | `Interpreted execution`

要运行的仿真类型，指定为 `Code generation` 或 `Interpreted execution`。

- `Code generation` — 通过使用生成的 C 代码来仿真模型。首次运行仿真时，Simulink 会为模块生成 C 代码。除非模型发生变化，否则模型会将 C 代码重用于后续仿真。此选项需要额外的启动时间，但后续仿真的速度快于使用 `Interpreted execution` 选项。
- `Interpreted execution` — 通过使用 MATLAB® 解释器来仿真模型。此选项可缩短启动时间，但后续仿真的速度慢于使用 `Code generation` 选项。在此模式下，您可以调试模块的源代码。

有关详细信息，请参阅解释执行与代码生成 (Simulink)。

## 所属库

Communications Toolbox / RF Impairments Correction Communications Toolbox / Synchronization

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015b 中引入**

### R2025a：估计的频率偏移以频率分辨率的整数倍返回

当配置为使用基于 FFT 的算法时，Coarse Frequency Compensator 模块现在将估计的频率偏移 **FreqEst** 作为 **Frequency resolution (Hz)** 参数值的整数倍返回。

### R2023b：默认设置更改

Coarse Frequency Compensator 模块参数有新的默认值。

| 参数 | 新默认值 | 以前的默认值 |
| --- | --- | --- |
| **Frequency resolution (Hz)** | `100` | `0.001` |
| **Maximum frequency offset (Hz)** | `5e3` | `0.05` |

当执行在以前的版本中创建的代码时，请确认 Coarse Frequency Compensator 设置。新的默认设置会改变您的结果。要使用以前的默认设置产生结果，您可以手动更新模块的设置。

## 描述

补偿 PAM、PSK 或 QAM 中的载波频率偏移

Coarse Frequency Compensator 模块补偿 QAM、8-PSK、BPSK、OQPSK、PAM 和 QPSK 调制方案中的载波频率偏移。
