---
type: simulink-block
title: 'Carrier Synchronizer'
family: 'synchronization'
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

### 输入

### **In** — 输入信号 标量 | 列向量

输入信号，指定为标量或向量。

此端口在模块上未命名。

**数据类型：** `double` | `single`
**复数支持：** Yes

### 输出

### **Out** — 相位校正后的输出信号 标量 | 列向量

相位校正后的输出信号，返回为与输入信号具有相同数据类型和长度的标量或列向量。该输出信号调整输入信号，以补偿使用单载波调制方案的信号中的载波频率偏移和相位偏移。

在选择 **Estimated phase error output port** 参数之前，此端口在模块上未命名。

**数据类型：** `double` | `single`
**复数支持：** Yes

### **PhEst** — 以 radians 为单位的相位估计 标量 | 列向量

以 radians 为单位的相位估计，返回为与输入信号长度相同的标量或列向量。

#### 依赖关系

要启用此端口，请选择 **Estimated phase error output port** 参数。

**数据类型：** `double` | `single`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上，在 **准备** 库中选择 **属性检查器**。

### **Modulation** — 调制类型 `QAM`（默认） | `8PSK` | `BPSK` | `OQPSK` | `PAM` | `QPSK`

调制类型，指定为 `QAM`、`8PSK`、`BPSK`、`OQPSK`、`PAM` 或 `QPSK`。

### **Modulation phase offset** — 调制相位偏移方法 `Auto`（默认） | `Custom`

调制相位偏移方法，指定为 `Auto` 或 `Custom`。

- `Auto` — 对指定的调制类型应用传统偏移。

  | 调制 | 相位偏移 (radians) |
  | --- | --- |
  | `BPSK`、`QAM` 或 `PAM` | 0 |
  | `OQPSK` 或 `QPSK` | *π*/4 |
  | `8PSK` | *π*/8 |
- `Custom` — 使用 CustomPhaseOffset 属性指定用户定义的相位偏移。

**可调：** Yes

### **Custom phase offset (radians)** — 以 radians 为单位的自定义相位偏移 `0`（默认） | 标量

以 radians 为单位的自定义相位偏移，指定为标量。

#### 依赖关系

当您将 **Modulation phase offset** 设置为 `Custom` 时，此参数适用。

### **Samples per symbol** — 每符号的采样点数 `2`（默认） | 正整数

每符号的采样点数，指定为正整数。

**可调：** Yes

### **Damping factor** — 环路的阻尼因子 `0.707`（默认） | 正标量

环路的阻尼因子，指定为正标量。

**可调：** Yes

### **Normalized loop bandwidth** — 环路的归一化带宽 `0.01`（默认） | 标量

环路的归一化带宽，指定为范围 (0,1] 内的标量。环路带宽由同步器的采样率归一化。

减小环路带宽会缩短同步器的收敛时间，但也会减小同步器的牵引范围。

**可调：** Yes

### **Estimated phase error output port** — 启用估计相位误差输出端口 `on`（默认） | `off`

选中此复选框可将估计相位误差提供给输出端口 **phEst**。

### **Simulate using** — 要运行的仿真类型 `Code generation`（默认） | `Interpreted execution`

要运行的仿真类型，指定为 `Code generation` 或 `Interpreted execution`。

- `Code generation` — 通过使用生成的 C 代码来仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。除非模型发生变化，否则模型会在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度快于 `Interpreted execution` 选项。
- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但后续仿真的速度慢于 `Code generation` 选项。在此模式下，您可以调试模块的源代码。

有关详细信息，请参阅解释执行与代码生成 (Simulink)。

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

Carrier Synchronizer 模块补偿使用单载波调制方案的信号中的载波频率偏移和相位偏移。载波同步器算法与 BPSK、QPSK、OQPSK、8-PSK、PAM 和矩形 QAM 调制方案兼容。

**注意**

同步算法可能会引入取决于调制类型的相位模糊。有关详细信息，请参阅潜在相位模糊。

此图标显示不带可选端口的模块。
