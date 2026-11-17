---
type: simulink-block
title: 'EVM Measurement'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Utility Blocks'
documentation_page: 'evmmeasurement'
documentation_source_path: 'ref/evmmeasurement.html'
language: zh-CN
chinese_source: worker-translation
---

# EVM Measurement

## 端口
```yaml
ports:
- name: Ref
  summary: 参考信号数组
  direction: input
  data_types: single | double | fixed point
- name: Rcv
  summary: 接收信号数组
  direction: input
  data_types: single | double | fixed point
- name: RMS
  summary: 百分比 RMS EVM 标量
  direction: output
  data_types: double
- name: max
  summary: 最大百分比 EVM 标量
  direction: output
  data_types: double
- name: X%
  summary: '*X*% 的 EVM 测量值低于此值的标量，范围为 [0, 100]'
  direction: output
  data_types: double
- name: nSym
  summary: 符号数量正整数
  direction: output
  data_types: double
```

### 输入

### **Ref** — 参考信号数组

参考信号，指定为最多三维的数组。如果指定此输入，该对象通过将此输入用作参考星座来测量 `Rcv` 输入的 EVM。

此输入的维度必须与 `Rcv` 输入的维度匹配。该对象将此输入的每个元素用作 `Rcv` 输入对应元素的参考符号。

#### 依赖关系

要启用此端口，请将 **Reference signal** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** 是

### **Rcv** — 接收信号数组

接收信号，指定为最多三维的数组。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** 是
### 输出

### **RMS** — 百分比 RMS EVM 标量

在配置的测量区间内的百分比 RMS EVM，以标量形式返回。

**数据类型：** `double`

### **max** — 最大百分比 EVM 标量

在配置的测量区间内的最大百分比 EVM，以标量形式返回。

#### 依赖关系

要启用此端口，请将 **Output maximum EVM** 参数设置为 `On`。

**数据类型：** `double`

### **X%** — *X*% 的 EVM 测量值低于此值的标量，范围为 [0, 100]

自上次重置以来 *X*% 的 EVM 测量值低于此值，以 [0, 100] 范围内的标量形式返回。在 **X-percentile value (%)** 参数中设置 *X* 的值。

#### 依赖关系

要启用此端口，请将 **Output X-percentile EVM** 参数设置为 `On`。

**数据类型：** `double`

### **nSym** — 符号数量正整数

用于测量 *X* 百分位 EVM 的符号数量，以正整数形式返回。

#### 依赖关系

要启用此端口，请将 **Output X-percentile EVM** 和 **Output the number of symbols processed** 参数设置为 `On`。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Normalize RMS error vector by
  summary: 归一化方法 Average reference signal power（默认）| Average constellation power | Peak constellation power
  group: ''
- name: Average constellation power
  summary: 平均星座功率 1（默认）| 正标量
  group: ''
- name: Peak constellation power
  summary: 峰值星座功率 1（默认）| 正标量
  group: ''
- name: Reference signal
  summary: 参考信号源 Input port | Estimated from reference constellation
  group: ''
- name: Reference constellation
  summary: 参考星座 constellation(pskmod((0:3)',4,pi/4,"bin"))（默认）| 向量
  group: ''
- name: Measurement interval
  summary: 测量区间源 Input length（默认）| Entire history | Custom | Custom with periodic reset
  group: ''
- name: Custom measurement interval
  summary: 自定义测量区间 100（默认）| 正整数
  group: ''
- name: Averaging dimensions
  summary: 平均维度 1（默认）| [1, 3] 范围内的整数向量
  group: ''
- name: Output maximum EVM
  summary: 添加 max 端口以输出最大 EVM 测量的选项 Off（默认）| On
  group: ''
- name: Output X-percentile EVM
  summary: 添加 X% 端口以输出 *X* 百分位 EVM 测量的选项 Off（默认）| On
  group: ''
- name: X-percentile value (%)
  summary: '*X*% 的 EVM 测量值低于此值 95（默认）| [0, 100] 范围内的标量'
  group: ''
- name: Output the number of symbols processed
  summary: 添加 nSym 端口以输出符号数量的选项 Off（默认）| On
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Interpreted execution（默认）| Code generation
  group: ''
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡中，在 **Prepare** 库中选择 **Property Inspector**。

### **Normalize RMS error vector by** — 归一化方法 `Average reference signal power`（默认）| `Average constellation power` | `Peak constellation power`

用于 EVM 计算的归一化方法，指定为 `Average reference signal power`、`Average constellation power` 或 `Peak constellation power`。有关详细信息，请参阅算法。

### **Average constellation power** — 平均星座功率 `1`（默认）| 正标量

平均星座功率，以瓦特为单位，指定为正标量。

#### 依赖关系

要启用此参数，请将 **Normalize RMS error vector** 参数设置为 `Average constellation power`。

### **Peak constellation power** — 峰值星座功率 `1`（默认）| 正标量

峰值星座功率，以瓦特为单位，指定为正标量。

#### 依赖关系

要启用此参数，请将 **Normalize RMS error vector** 参数设置为 `Peak constellation power`。

### **Reference signal** — 参考信号源 `Input port` | `Estimated from reference constellation`

参考信号源。要提供用于测量接收信号的显式参考信号，请将此参数设置为 `Input port`。要针对参考星座测量接收信号的 EVM，请将此参数设置为 `Estimated from reference constellation`。

### **Reference constellation** — 参考星座 `constellation(pskmod((0:3)',4,pi/4,"bin"))`（默认）| 向量

参考星座点，指定为复数值或实数值向量。

#### 依赖关系

要启用此参数，请将 **Reference signal** 参数设置为 `Estimated from reference constellation`。

### **Measurement interval** — 测量区间源 `Input length`（默认）| `Entire history` | `Custom` | `Custom with periodic reset`

用于 RMS 和最大 EVM 测量的测量区间源，指定为以下值之一。

- `Input length` — 仅使用当前样本测量 EVM。
- `Entire history` — 对所有样本测量 EVM。
- `Custom` — 在指定的区间内测量 EVM 并使用滑动窗口。
- `Custom with periodic reset` — 在指定的区间内测量 EVM，并在每个区间测量完成后重置模块。

### **Custom measurement interval** — 自定义测量区间 `100`（默认）| 正整数

以样本为单位的自定义测量区间，指定为正整数。

#### 依赖关系

要启用此参数，请将 **Measurement interval** 参数设置为 `Custom` 或 `Custom with periodic reset`。

### **Averaging dimensions** — 平均维度 `1`（默认）| [1, 3] 范围内的整数向量

模块对 EVM 测量值进行平均的维度，指定为 [1, 3] 范围内的整数或整数行向量。例如，要跨行平均，请将此参数设置为 `2`。

此模块支持在平均所沿维度上具有可变大小的输入。但是，非平均维度的输入大小必须保持不变。例如，如果输入的大小为 `[1000 3 2]` 且您将此参数设置为 `[1 3]`，则输出大小为 `[1 3 1]`，并且第二维中的元素数量必须固定为 `3`。

### **Output maximum EVM** — 添加 `max` 端口以输出最大 EVM 测量的选项 `Off`（默认）| `On`

添加 `max` 端口以输出最大 EVM 测量的选项。

### **Output X-percentile EVM** — 添加 `X%` 端口以输出 *X* 百分位 EVM 测量的选项 `Off`（默认）| `On`

添加 `X%` 端口以输出 *X* 百分位 EVM 测量的选项。当您将此参数设置为 `On` 时，*X* 百分位 EVM 测量值将保持，直到您重置模块。模块使用自上次重置以来的所有输入帧执行这些测量。您可以在 **X-percentile value (%)** 参数中设置 *X* 的值。

### **X-percentile value (%)** — *X*% 的 EVM 测量值低于此值 `95`（默认）| [0, 100] 范围内的标量

*X*% 的 EVM 测量值低于此值，指定为 [0, 100] 范围内的标量。

#### 依赖关系

要启用此参数，请将 **Output X-percentile EVM** 参数设置为 `On`。

### **Output the number of symbols processed** — 添加 `nSym` 端口以输出符号数量的选项 `Off`（默认）| `On`

添加 `nSym` 端口以输出用于测量 *X* 百分位 EVM 的符号数量的选项。

#### 依赖关系

要启用此参数，请将 **Output X-percentile EVM** 参数设置为 `On`。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

要运行的仿真类型，指定为 `Interpreted execution` 或 `Code generation`。

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项需要较少的启动时间，但后续仿真的速度比 `Code generation` 选项慢。在此模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为模块生成 C 代码。除非模型发生变化，否则模型会在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度比 `Interpreted execution` 选项快。

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

要在使用此模块的模型中生成代码，您必须启用 **Dynamic Memory Allocation in MATLAB Functions**。有关详细信息，请参阅 Dynamic memory allocation in MATLAB functions (Simulink)。

## 版本历史

**在 R2009b 中引入**

## 描述

测量误差向量幅度（EVM）

EVM Measurement 模块测量接收信号的均方根（RMS）EVM、最大 EVM 和百分位 EVM。EVM 是调制器或解调器性能的指标。

此图标显示了启用所有端口的模块。启用所有端口的 EVM 测量模块。
