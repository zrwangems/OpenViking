---
type: simulink-block
title: 'MSK Demodulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Modulation / Digital Baseband Modulation / Continuous Phase Modulation'
documentation_page: 'mskdemodulatorbaseband'
documentation_source_path: 'ref/mskdemodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# MSK Demodulator Baseband

## 端口

R2025b 中未提供文档。

## 参数

**输出类型**
:   确定输出由双极性值还是二进制值组成。

**相位偏移 (rad)**
:   已调制波形的初始相位。

**每符号采样点数**
:   表示每个已调制符号的输入采样点数量，该数量必须为正整数。有关详细信息，请参阅信号上采样和速率变化。

**速率选项**
:   选择模块的速率处理方法。

    - `Enforce single-rate processing` —
      选择此选项时，输入和输出信号具有相同的端口采样时间。该模块通过使输出的大小相对于输入发生变化来实现速率变化。输出宽度为符号数（当 **输出类型** 参数设置为 `Integer` 时，符号数由输入长度除以 **每符号采样点数** 参数值得到）。
    - `Allow multirate processing` —
      选择此选项时，输入和输出信号具有不同的端口采样时间。输出周期与符号周期相同，且等于输入周期与 **每符号采样点数** 参数值的乘积。

    有关详细信息，请参阅本页“描述”一节中的“单速率处理”和“多速率处理”。

**回溯深度**
:   MSK Demodulator Baseband 模块用于构建每条回溯路径的网格分支数量。

**输出数据类型**
:   输出数据类型可以是 `boolean`、`int8`、`int16`、`int32` 或 `double`。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

对差分编码的 MSK 调制数据进行解调

MSK Demodulator Baseband 模块对采用差分编码最小频移键控方法调制的信号进行解调。该模块要求输入信号是未经预编码的相干调制信号的基带表示。**相位偏移**参数表示已调制波形的初始相位。

### 脉冲成形滤波

差分编码最小频移键控调制使用脉冲成形来平滑已调制信号的相位过渡。函数 *q*(*t*) 是根据频率脉冲 *g*(*t*) 通过以下关系得到的相位响应：q(t)=∫− ∞tg(t)dt。

指定的频率脉冲形状对应于 *g*(*t*) 的以下矩形脉冲形状表达式。

| 脉冲形状 | 表达式 |
| --- | --- |
| `Rectangular` | g(t)={12LT,0≤t≤LT0otherwise |

- *L* 是主瓣脉冲持续时间，以符号间隔为单位。
- 脉冲持续时间 *LT* 是以符号间隔为单位的脉冲长度。

### 整数值信号和二进制值信号

该模块接受数据类型为 `single` 或 `double` 的标量值或列向量输入信号。如果将 **输出类型** 参数设置为 `Integer`，则模块输出 1 和 -1。如果将 **输出类型** 参数设置为 `Bit`，则模块输出 0 和 1。

### 单速率处理

在单速率处理模式下，输入和输出信号具有相同的端口采样时间。该模块通过使输出大小相对于输入发生变化来隐式实现速率变化。输入宽度必须是 **每符号采样点数** 参数值的整数倍，并且输入可以是列向量。

- 当将 **输出类型** 设置为 `Bit` 时，输出宽度为输入符号数量的 *K* 倍。
- 当将 **输出类型** 设置为 `Integer` 时，输出宽度为输入符号的数量。

### 多速率处理

在多速率处理模式下，输入和输出信号具有不同的端口采样时间。输入必须为标量。输出符号时间是输入采样时间与 **每符号采样点数** 参数值的乘积。

- 当将 **输出类型** 设置为 `Bit` 时，输出宽度等于每个符号的位数。
- 当将 **输出类型** 设置为 `Integer` 时，输出为标量。

### 回溯深度和输出延迟

在内部，该模块创建调制方案的网格描述，并使用 Viterbi 算法。此模块中的 **回溯深度** 参数 D 是用于构建每条回溯路径的网格分支数量。D 会影响输出延迟，输出延迟是输出中第一个有效解调值之前的零符号数量。

- 当将 **速率选项** 参数设置为 `Allow multirate processing`，并且模型使用变步长求解器，或使用 **任务模式** 参数设置为 `SingleTasking` 的定步长求解器时，延迟由 D+1 个零符号组成。
- 当将 **速率选项** 参数设置为 `Enforce single-rate processing` 时，延迟由 D 个零符号组成。

最优 **回溯深度** 参数值取决于最小平方欧氏距离的计算。或者，可以根据状态数，采用“五倍约束长度”规则选择一个典型值，该规则对应于 5×log2(*numStates*)。状态数由以下方程确定：

numStates={p⋅2(L−1), for even m2p⋅2(L−1), for odd m}

其中：

- *h* = m/p 是以既约有理数形式表示的调制指数

  - *m* = 调制指数的分子
  - *p* = 调制指数的分母
- *L* 是脉冲长度
