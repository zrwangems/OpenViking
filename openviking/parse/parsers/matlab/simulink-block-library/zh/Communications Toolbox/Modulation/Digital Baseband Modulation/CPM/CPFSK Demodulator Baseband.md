---
type: simulink-block
title: 'CPFSK Demodulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / CPM'
documentation_page: 'cpfskdemodulatorbaseband'
documentation_source_path: 'ref/cpfskdemodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# CPFSK Demodulator Baseband

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters: []
```

**M-ary number**
:   字母表的大小。

**输出类型**
:   确定输出由整数还是比特组组成。

**Symbol set ordering**
:   确定模块如何将每个整数映射到一组输出比特。仅当 **输出类型** 设置为 `Bit` 时，此字段才处于活动状态。

**Modulation index**
:   指定调制指数 {hi}。默认值为 `0.5`。此属性的值必须为实数、非负标量或列向量。

    此模块支持多 h **Modulation index**。有关详细信息，请参阅 CPM Modulator Baseband。

**Phase offset (rad)**
:   调制波形的初始相位。

**Samples per symbol**
:   表示每个调制符号的输入样本数，必须为正整数。有关详细信息，请参阅 *Communications Toolbox™ User's Guide* 中的 Signal Upsampling and Rate Changes。

**Rate options**
:   选择模块的速率处理方法。

    - `Enforce single-rate processing` —
      选择此选项时，输入和输出信号具有相同的端口采样时间。模块通过使输出相对于输入发生大小变化来实现速率变化。输出宽度为符号数（当 **输出类型** 参数设置为 `Integer` 时，该值由输入长度除以 **Samples per symbol** 参数值得到）。
    - `Allow multirate processing` —
      选择此选项时，输入和输出信号具有不同的端口采样时间。输出周期与符号周期相同，等于输入周期与 **Samples per symbol** 参数值的乘积。

    有关详细信息，请参阅本页描述部分中的 Single-Rate Processing 和 Multirate Processing。

**Traceback depth**
:   CPFSK Demodulator Baseband 模块用于构造每条回溯路径的网格分支数。

**Output datatype**
:   输出数据类型可以为 `boolean`、`int8`、`int16`、`int32` 或 `double`。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

解调 CPFSK 调制数据

CPFSK Demodulator Baseband 模块解调使用连续相位频移键控方法调制的信号。此模块的输入是调制信号的基带表示。**M-ary number** 参数 *M* 是输入字母表的大小。*M* 必须具有 2*K* 的形式，其中 *K* 为某个正整数。

此模块支持多 h **Modulation index**。有关详细信息，请参阅 CPM Modulator Baseband。

### 整数值信号和二值信号

当将 **输出类型** 参数设置为 `Integer` 时，模块产生 -(M-1) 到 M-1 之间的奇数整数。

当将 **输出类型** 参数设置为 `Bit` 时，模块产生 *K* 个比特的分组。每个分组称为一个二进制*字*。

在二进制输出模式下，模块首先像整数输出模式那样将每个输入符号映射为中间值。然后模块将奇数整数 k 映射为非负整数 (k+M-1)/2。最后，模块将每个非负整数映射为二进制字，所使用的映射取决于 **Symbol set ordering** 参数设置为 `Binary` 还是 `Gray`。

此模块接受数据类型为 `single` 或 `double` 的标量值或列向量输入信号。

### 单速率处理

在单速率处理模式下，输入和输出信号具有相同的端口采样时间。模块通过使输出相对于输入发生大小变化来隐式实现速率变化。输入宽度必须是 **Samples per symbol** 参数值的整数倍，并且输入可以是列向量。

- 当将 **输出类型** 设置为 `Bit` 时，输出宽度为 *K* 乘以输入符号数。
- 当将 **输出类型** 设置为 `Integer` 时，输出宽度为输入符号数。

### 多速率处理

在多速率处理模式下，输入和输出信号具有不同的端口采样时间。输入必须为标量。输出符号时间是输入采样时间与 **Samples per symbol** 参数值的乘积。

- 当将 **输出类型** 设置为 `Bit` 时，输出宽度等于每符号的比特数。
- 当将 **输出类型** 设置为 `Integer` 时，输出为标量。

### 回溯深度和输出延迟

在内部，此模块创建调制方案的网格描述并使用 Viterbi 算法。此模块中的 **Traceback depth** 参数 *D* 是算法用于构造每条回溯路径的网格分支数。*D* 影响输出延迟，即输出中第一个有意义的解调值之前出现的零符号数。

- 当将 **Rate options** 参数设置为 `Allow multirate processing`，并且模型使用变步长求解器或 **Tasking Mode** 参数设置为 `SingleTasking` 的定步长求解器时，延迟由 D+1 个零符号组成。
- 当将 **Rate options** 参数设置为 `Enforce single-rate processing` 时，延迟由 D 个零符号组成。

最佳的 **Traceback depth** 参数值取决于最小平方欧几里得距离计算。或者，可以使用“五倍约束长度”规则选择取决于状态数的典型值，该规则对应于 5·log2(*numStates*)。

有关状态数的定义，请参阅 CPM Demodulator Baseband 帮助页面。
