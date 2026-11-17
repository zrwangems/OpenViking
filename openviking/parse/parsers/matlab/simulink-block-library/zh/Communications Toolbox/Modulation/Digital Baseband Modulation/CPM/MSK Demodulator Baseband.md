---
type: simulink-block
title: 'MSK Demodulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / CPM'
documentation_page: 'mskdemodulatorbaseband'
documentation_source_path: 'ref/mskdemodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# MSK Demodulator Baseband

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters: []
```

**输出类型**
:   确定输出由双极性值还是二进制值组成。

**Phase offset (rad)**
:   调制波形的初始相位。

**Samples per symbol**
:   表示每个调制符号的输入样本数，必须为正整数。有关详细信息，请参阅 Signal Upsampling and Rate Changes。

**Rate options**
:   选择模块的速率处理方法。

    - `Enforce single-rate processing` —
      选择此选项时，输入和输出信号具有相同的端口采样时间。该模块通过使输出相对于输入发生大小变化来实现速率变化。当 **输出类型** 参数设置为 `Integer` 时，输出宽度为符号数（由输入长度除以 **Samples per symbol** 参数值得到）。
    - `Allow multirate processing` —
      选择此选项时，输入和输出信号具有不同的端口采样时间。输出周期与符号周期相同，等于输入周期与 **Samples per symbol** 参数值的乘积。

    有关详细信息，请参阅本页描述部分中的 Single-Rate Processing 和 Multirate Processing。

**Traceback depth**
:   MSK Demodulator Baseband 模块用于构建每条回溯路径的网格分支数。

**输出数据类型**
:   输出数据类型可以为 `boolean`、`int8`、`int16`、`int32` 或 `double`。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

解调差分编码的 MSK 调制数据

MSK Demodulator Baseband 模块解调使用差分编码最小频移键控方法调制的信号。该模块期望输入信号为无预编码的相干调制信号的基带表示。**Phase offset** 参数表示调制波形的初始相位。

### 脉冲成形滤波

差分编码最小频移键控调制使用脉冲成形来平滑调制信号的相位过渡。函数 *q*(*t*) 是通过以下关系从频率脉冲 *g*(*t*) 获得的相位响应：q(t)=∫− ∞tg(t)dt。

指定的频率脉冲形状对应于 *g*(*t*) 的以下矩形脉冲形状表达式。

| 脉冲形状 | 表达式 |
| --- | --- |
| `Rectangular` | g(t)={12LT,0≤t≤LT0otherwise |

- *L* 是以符号间隔表示的主瓣脉冲持续时间。
- 脉冲的持续时间 *LT* 是以符号间隔表示的脉冲长度。

### 整数值信号和二进制值信号

该模块接受数据类型为 `single` 或 `double` 的标量值或列向量输入信号。如果将 **输出类型** 参数设置为 `Integer`，则该模块生成值 1 和 -1。如果将 **输出类型** 参数设置为 `Bit`，则该模块生成值 0 和 1。

### 单速率处理

在单速率处理模式下，输入和输出信号具有相同的端口采样时间。该模块通过使输出相对于输入发生大小变化来隐式实现速率变化。输入宽度必须是 **Samples per symbol** 参数值的整数倍，并且输入可以是列向量。

- 当将 **输出类型** 设置为 `Bit` 时，输出宽度为 *K* 乘以输入符号数。
- 当将 **输出类型** 设置为 `Integer` 时，输出宽度为输入符号数。

### 多速率处理

在多速率处理模式下，输入和输出信号具有不同的端口采样时间。输入必须为标量。输出符号时间是输入采样时间与 **Samples per symbol** 参数值的乘积。

- 当将 **输出类型** 设置为 `Bit` 时，输出宽度等于每符号的比特数。
- 当将 **输出类型** 设置为 `Integer` 时，输出为标量。

### 回溯深度和输出延迟

在内部，该模块创建调制方案的网格描述并使用 Viterbi 算法。该模块中的 **Traceback depth** 参数 D 是用于构建每条回溯路径的网格分支数。D 影响输出延迟，即输出中第一个有意义的解调值之前的零符号数。

- 当将 **Rate options** 参数设置为 `Allow multirate processing`，并且模型使用变步长求解器或将 **Tasking Mode** 参数设置为 `SingleTasking` 的定步长求解器时，延迟由 D+1 个零符号组成。
- 当将 **Rate options** 参数设置为 `Enforce single-rate processing` 时，延迟由 D 个零符号组成。

最佳的 **Traceback depth** 参数值取决于最小平方欧几里得距离计算。或者，可以使用“五倍约束长度”规则选择取决于状态数的典型值，该规则对应于 5×log2(*numStates*)。状态数由以下方程确定：

numStates={p⋅2(L−1), for even m2p⋅2(L−1), for odd m}

其中：

- *h* = m/p 是调制指数的真分数形式

  - *m* = 调制指数的分子
  - *p* = 调制指数的分母
- *L* 是脉冲长度
