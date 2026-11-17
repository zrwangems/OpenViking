---
type: simulink-block
title: 'Frequency-Domain Adaptive Filter'
family: 'filtering'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Adaptive Filters'
documentation_page: 'frequencydomainadaptivefilter'
documentation_source_path: 'ref/frequencydomainadaptivefilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Frequency-Domain Adaptive Filter

## 端口

### 输入

### **Input** — 数据输入列向量

要由频域 FIR 自适应滤波器滤波的信号。数据输入和期望信号输入必须具有相同的大小和数据类型。输入向量的长度必须能被 **Block length** 参数值整除。

只要帧长度是 **Block length** 的倍数，数据输入就可以是可变大小信号。您可以在模型仿真期间更改列向量中的元素数量。

**数据类型：** `single` | `double`
**复数支持：** Yes

### **Desired** — 期望信号列向量

频域自适应滤波器调整其滤波器权重以最小化误差 **Error**，并使输入信号尽可能接近期望信号。

数据输入和期望信号必须具有相同的大小和数据类型。期望信号向量的长度必须能被 **Block length** 参数值整除。

只要帧长度是 **Block length** 的倍数，期望信号就可以是可变大小信号。您可以在模型仿真期间更改列向量中的元素数量。

**数据类型：** `single` | `double`
**复数支持：** Yes

### **Mu** — 步长输入，范围 (0,1] 内的实标量

自适应步长因子，指定为范围 (0,1] 内的实标量。使用小的步长可确保小的稳态误差。但是，小的步长会降低自适应滤波器的收敛速度。增大步长可提高收敛速度，但代价是稳态均方误差增大。当步长值为 `1` 时，该算法在收敛速度和稳态均方误差之间提供最佳折衷。

#### 依赖关系

当您选择 **Specify step size from port** 参数时，此端口出现。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Leak** — 泄漏因子输入，范围 (0,1] 内的实标量

泄漏自适应滤波器中使用的泄漏因子，指定为范围 (0,1] 内的实标量。当该值小于 1 时，该模块实现泄漏自适应算法。当该值为 `1` 时，该模块在自适应方法中不提供泄漏。

#### 依赖关系

当您选择 **Specify leakage factor from port** 复选框时，此端口出现。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Avrg** — 平均因子输入，范围 (0,1] 内的实标量

用于计算系数更新的指数加窗快速傅里叶变换 (FFT) 输入信号功率的平均因子，指定为范围 (0,1] 内的实标量。

#### 依赖关系

当您选择 **Specify averaging factor from port** 复选框时，此端口出现。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Offset** — 归一化项的偏移，非负实标量

系数更新中归一化项的偏移，指定为非负实标量值。如果任一 FFT 输入信号功率变得非常小，使用此值可避免除以零或除以非常小的数。

#### 依赖关系

当您选择 **Specify offset from port** 复选框时，此端口出现。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Adapt** — 启用滤波器系数更新，非负实标量

如果通过此端口输入非零标量值，则该模块会连续更新其滤波器系数。如果通过此端口输入零，则滤波器系数不更新，其值保持当前值。

#### 依赖关系

当您选择 **Enable adapt port** 复选框时，此端口出现。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Reset** — 启用滤波器状态重置，非负实标量

如果通过此端口输入非零标量值，则该模块会重置所有内部状态。如果通过此端口输入零，则内部状态不会重置。

#### 依赖关系

当您选择 **Enable reset port** 复选框时，此端口出现。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### 输出

### **Output** — 滤波输出列向量

滤波输出，以列向量形式返回。该模块调整其滤波器权重，使输入信号尽可能接近期望信号。滤波器输出收敛后的信号。

**数据类型：** `single` | `double`
**复数支持：** Yes

### **Error** — 输出与期望信号之间的差值，列向量

输出信号与期望信号之间的差值，以列向量形式返回。自适应滤波器的目标是最小化此误差。该模块调整其权重以收敛到最优滤波器权重，从而产生尽可能接近期望信号的输出信号。有关如何计算 **Error** 的更多详细信息，请参阅参考文献。

**数据类型：** `single` | `double`
**复数支持：** Yes

### **FFTCoeffs** — 滤波器的当前 FFT 系数，行向量

滤波器系数的当前离散傅里叶变换，以行向量形式返回。对于 `Constrained FDAF` 和 `Unconstrained FDAF` 算法，此向量的长度等于 **Filter length** 值与 **Block length** 值之和。此端口最初输出 **Initial time-domain coefficients** 参数的 FFT 值。在模型仿真期间，此端口输出当前滤波器系数的 FFT 值。

#### 依赖关系

当您选择 **Output filter FFT coefficients** 复选框时，此端口出现。

**数据类型：** `single` | `double`
**复数支持：** Yes

## 参数

### **Method** — 计算滤波器系数的方法 `Constrained FDAF`（默认） | `Partitioned constrained FDAF` | `Unconstrained FDAF` | `Partitioned unconstrained FDAF`

用于计算滤波器系数的方法，指定为：

- `Constrained FDAF` –– 对滤波器抽头权重施加梯度约束。
- `Partitioned constrained FDAF` –– 对滤波器的脉冲响应进行分区以减少延迟。
- `Unconstrained FDAF` –– 不对滤波器抽头权重施加梯度约束。
- `Partitioned unconstrained FDAF` –– 对滤波器的脉冲响应进行分区以减少延迟。不对滤波器抽头权重施加梯度约束。

有关更多详细信息，请参阅算法。

### **Filter length** — 滤波器系数向量的长度 `32`（默认） | 正整数值标量

FIR 滤波器系数向量的长度，指定为正整数值标量。

### **Block length** — 用于系数更新的块长度 `32`（默认） | 正整数值标量

用于系数更新的块长度，指定为正整数值标量。自适应滤波器将输入数据和期望信号作为长度由此参数设置的样本块进行处理。有关滤波器如何处理此数据的详细信息，请参阅算法。输入向量的长度必须能被 **Block length** 参数值整除。**Block length** 参数的默认值设置为 **Filter length** 参数的值。

### **Specify step size from port** — 用于指定步长的标志 off（默认） | on

当您选择此复选框时，自适应步长通过 **Mu** 端口输入。当您清除此复选框时，步长通过 **Step size** 参数在模块对话框中指定。

### **Step size** — 自适应步长 `1`（默认） | 范围 (0,1] 内的实标量

自适应步长因子，指定为范围 (0,1] 内的实标量。将 **Step size** 参数设置为 `1` 可在自适应期间提供最快收敛。

**可调：** Yes

#### 依赖关系

当您清除 **Specify step size from port** 复选框时，此参数出现。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Specify leakage factor from port** — 用于指定泄漏因子的标志 off（默认） | on

当您选择此复选框时，泄漏因子通过 **Leak** 端口输入。当您清除此复选框时，泄漏因子通过 **Leakage factor** 参数在模块对话框中指定。

### **LeakageFactor** — 自适应泄漏因子 `1`（默认） | 范围 (0,1] 内的实标量

泄漏自适应滤波器中使用的泄漏因子，指定为范围 (0,1] 内的实标量。当该值小于 `1` 时，该模块实现泄漏自适应算法。当该值为 `1` 时，该模块在自适应方法中不提供泄漏。

**可调：** Yes

#### 依赖关系

当您清除 **Specify leakage factor from port** 复选框时，此参数出现。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Specify averaging factor from port** — 用于指定平均因子的标志 off（默认） | on

当您选择此复选框时，信号功率的平均因子通过 **Avrg** 端口输入。当您清除此复选框时，平均因子通过 **Averaging factor** 参数在模块对话框中指定。

### **Averaging factor** — 信号功率的平均因子 `0.9`（默认） | 范围 (0,1] 内的实标量

用于计算系数更新的指数加窗 FFT 输入信号功率的平均因子，指定为范围 (0,1] 内的实标量。

**可调：** Yes

#### 依赖关系

当您清除 **Specify averaging factor from port** 复选框时，此参数出现。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Specify offset from port** — 用于指定偏移的标志 off（默认） | on

当您选择此复选框时，系数更新中归一化项的偏移通过 **Offset** 端口输入。当您清除此复选框时，偏移通过 **Offset** 参数在模块对话框中指定。

### **Offset** — 归一化项的偏移 `0`（默认） | 非负实标量

系数更新中归一化项的偏移，指定为非负实标量值。如果任一 FFT 输入信号功率变得非常小，使用此值可避免除以零或除以非常小的数。

**可调：** Yes

#### 依赖关系

当您清除 **Specify offset from port** 复选框时，此参数出现。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Initial FFT input signal power** — 初始 FFT 输入信号功率 `1`（默认） | 正数值标量

所有 FFT 输入信号功率的初始公共值，指定为正数值标量。

如果您在仿真期间更改此值，则该更改仅在发生重置事件后生效。

**可调：** Yes

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Initial time-domain coefficients** — 滤波器的初始时域系数 `0`（默认） | 标量 | 向量

自适应滤波器的初始时域系数，指定为标量或长度等于 **Filter length** 参数中指定值的向量。自适应滤波器模块使用这些系数来计算初始频域滤波器系数。

如果您在仿真期间更改此值，则该更改仅在发生重置事件后生效。

**可调：** Yes

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Enable adapt port** — 用于启用系数更新的标志 off（默认） | on

当您选择此复选框时，**Adapt** 输入端口启用。如果通过此端口输入非零标量值，则该模块会连续更新其滤波器系数。如果通过此端口输入零，则滤波器系数不更新，其值保持当前值。

### **Enable reset port** — 用于重置内部状态的标志 off（默认） | on

当您选择此复选框时，**Reset** 输入端口启用。如果通过此端口输入非零标量值，则该模块会重置所有内部状态。如果通过此端口输入零，则内部状态不会重置。

### **Output filter FFT coefficients** — 用于输出滤波器系数 DFT 的标志 off（默认） | on

当您选择此复选框时，**FFTCoeffs** 输出端口启用。通过此端口，该模块输出当前滤波器系数的离散傅里叶变换。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认） | `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` –– 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` –– 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，C 代码就会在后续仿真中重用。此选项需要额外的启动时间，但可提供更快的后续仿真。

## 所属库

DSP System Toolbox / Filtering / Adaptive Filters

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

**在 R2018a 中引入**

### R2024a：**Simulate using** 参数默认值变更

**Simulate using** 参数的默认值现在为 `Interpreted execution`。通过此更改，该模块默认使用 MATLAB 解释器进行仿真。

## 描述

使用频域 FIR 自适应滤波器计算输出、误差和系数

Frequency-Domain Adaptive Filter 模块使用快速块最小均方 (LMS) 算法在频域中实现自适应有限脉冲响应 (FIR) 滤波器。**Filter length** 和 **Block length** 参数指定该算法使用的滤波器长度和块长度值。当您选择 **Output filter FFT coefficients** 复选框时，该模块输出当前滤波器系数的离散傅里叶变换。该模块提供该算法的受限和非受限版本以及分区和非分区模式。有关详细信息，请参阅算法。
