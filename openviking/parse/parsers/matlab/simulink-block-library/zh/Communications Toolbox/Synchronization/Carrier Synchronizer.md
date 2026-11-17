---
type: simulink-block
title: 'Carrier Synchronizer'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Synchronization'
documentation_page: 'carriersynchronizer'
documentation_source_path: 'ref/carriersynchronizer.html'
language: zh-CN
chinese_source: worker-translation
---

# Carrier Synchronizer

## 端口
```yaml
ports:
- name: In
  summary: 输入信号 标量 | 列向量
  direction: input
  data_types: double | single
- name: Out
  summary: 相位校正后的输出信号 标量 | 列向量
  direction: output
  data_types: double | single
- name: PhEst
  summary: 相位估计（弧度） 标量 | 列向量
  direction: output
  data_types: double | single
```

### 输入

### **In** — 输入信号 标量 | 列向量

输入信号，指定为标量或向量。

此端口在模块上未命名。

**数据类型：** `double` | `single`
**复数支持：** 是
### 输出

### **Out** — 相位校正后的输出信号 标量 | 列向量

相位校正后的输出信号，返回为与输入信号具有相同数据类型和长度的标量或列向量。输出信号调整输入信号，以补偿使用单载波调制方案的信号中的载波频率和相位偏移。

在选中 **Estimated phase error output port** 参数之前，此端口在模块上未命名。

**数据类型：** `double` | `single`
**复数支持：** 是

### **PhEst** — 相位估计（弧度） 标量 | 列向量

相位估计（弧度），返回为与输入信号长度相同的标量或列向量。

#### 依赖关系

要启用此端口，请选中 **Estimated phase error output port** 参数。

**数据类型：** `double` | `single`
## 参数
```yaml
parameters:
- name: Modulation
  summary: 调制类型 QAM（默认）| 8PSK | BPSK | OQPSK | PAM | QPSK
  group: ''
- name: Modulation phase offset
  summary: 调制相位偏移方法 Auto（默认）| Custom
  group: ''
- name: Custom phase offset (radians)
  summary: 自定义相位偏移（弧度） 0（默认）| 标量
  group: ''
- name: Samples per symbol
  summary: 每个符号的采样数 2（默认）| 正整数
  group: ''
- name: Damping factor
  summary: 环路阻尼因子 0.707（默认）| 正标量
  group: ''
- name: Normalized loop bandwidth
  summary: 归一化环路带宽 0.01（默认）| 标量
  group: ''
- name: Estimated phase error output port
  summary: 启用估计相位误差输出端口 on（默认）| off
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Code generation（默认）| Interpreted execution
  group: ''
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### **Modulation** — 调制类型 `QAM`（默认）| `8PSK` | `BPSK` | `OQPSK` | `PAM` | `QPSK`

调制类型，指定为 `QAM`、`8PSK`、`BPSK`、`OQPSK`、`PAM` 或 `QPSK`。

### **Modulation phase offset** — 调制相位偏移方法 `Auto`（默认）| `Custom`

调制相位偏移方法，指定为 `Auto` 或 `Custom`。

- `Auto` — 对指定的调制类型应用传统偏移。

  | 调制 | 相位偏移（弧度） |
  | --- | --- |
  | `BPSK`、`QAM` 或 `PAM` | 0 |
  | `OQPSK` 或 `QPSK` | *π*/4 |
  | `8PSK` | *π*/8 |
- `Custom` — 使用 CustomPhaseOffset 属性指定用户定义的相位偏移。

**可调：** 是

### **Custom phase offset (radians)** — 自定义相位偏移（弧度） `0`（默认）| 标量

自定义相位偏移（弧度），指定为标量。

#### 依赖关系

此参数在将 **Modulation phase offset** 设置为 `Custom` 时适用。

### **Samples per symbol** — 每个符号的采样数 `2`（默认）| 正整数

每个符号的采样数，指定为正整数。

**可调：** 是

### **Damping factor** — 环路阻尼因子 `0.707`（默认）| 正标量

环路阻尼因子，指定为正标量。

**可调：** 是

### **Normalized loop bandwidth** — 归一化环路带宽 `0.01`（默认）| 标量

归一化环路带宽，指定为 (0,1] 范围内的标量。环路带宽由同步器的采样率归一化。

减小环路带宽会缩短同步器收敛时间，但也会减小同步器的牵引范围。

**可调：** 是

### **Estimated phase error output port** — 启用估计相位误差输出端口 `on`（默认）| `off`

选中此复选框以将估计相位误差提供给输出端口 **phEst**。

### **Simulate using** — 要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

要运行的仿真类型，指定为 `Code generation` 或 `Interpreted execution`。

- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。除非模型发生变化，否则模型会在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度快于 `Interpreted execution` 选项。
- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但后续仿真的速度慢于 `Code generation` 选项。在此模式下，您可以调试模块的源代码。

有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。
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

补偿载波频率偏移

Carrier Synchronizer 模块补偿使用单载波调制方案的信号中的载波频率和相位偏移。载波同步器算法与 BPSK、QPSK、OQPSK、8-PSK、PAM 和矩形 QAM 调制方案兼容。

**注意**

同步算法可能会引入依赖于调制类型的相位模糊。有关详细信息，请参阅 Potential Phase Ambiguity。

此图标显示不带可选端口的模块。
