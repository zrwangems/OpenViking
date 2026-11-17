---
type: simulink-block
title: 'MSK Modulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / CPM'
documentation_page: 'mskmodulatorbaseband'
documentation_source_path: 'ref/mskmodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# MSK Modulator Baseband

## 端口

R2025b 中未记录。

## 参数

**输入类型**
:   指示输入由双极性值还是二进制值组成。

**Phase offset (rad)**
:   输出波形的初始相位，以弧度为单位。

**Samples per symbol**
:   模块为输入中的每个整数或二进制字产生的输出样本数，必须为正整数。对于所有非二进制方案（由脉冲形状定义），此值必须大于 1。

    有关详细信息，请参阅 Signal Upsampling and Rate Changes。

**Rate options**
:   选择模块的速率处理选项。

    - `Enforce single-rate processing` —
      选择此选项时，输入和输出信号具有相同的端口采样时间。模块通过使输出相对于输入发生大小变化来实现速率变化。输出宽度等于符号数与 **Samples per symbol** 参数值的乘积。
    - `Allow multirate processing` —
      选择此选项时，输入和输出信号具有不同的端口采样时间。输出采样时间等于符号周期除以 **Samples per symbol** 参数值。

**输出数据类型**
:   将模块输出数据类型指定为 `double` 和 `single`。默认情况下，模块将此设置为 `double`。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

使用差分编码最小频移键控方法进行调制

MSK Modulator Baseband 模块使用差分编码最小频移键控方法进行调制。输出是已调制信号的基带表示。

此模块接受标量值或列向量输入信号。对于列向量输入信号，输出宽度等于符号数与 **Samples per symbol** 参数值的乘积。

### 脉冲形状滤波

差分编码最小频移键控调制使用脉冲整形来平滑已调制信号的相位过渡。函数 *q*(*t*) 是通过以下关系从频率脉冲 *g*(*t*) 获得的相位响应：q(t)=∫− ∞tg(t)dt。

指定的频率脉冲形状对应于 *g*(*t*) 的以下矩形脉冲形状表达式。

| 脉冲形状 | 表达式 |
| --- | --- |
| `Rectangular` | g(t)={12LT,0≤t≤LT0otherwise |

- *L* 是主瓣脉冲持续时间，以符号间隔为单位。
- 脉冲的持续时间 *LT* 是脉冲长度，以符号间隔为单位。

### 整数值信号和二进制值信号

当将 **输入类型** 参数设置为 `Integer` 时，模块接受值 1 和 -1。

当将 **输入类型** 参数设置为 `Bit` 时，模块接受值 0 和 1。

有关每个模块端口支持的数据类型的信息，请参阅此页面上的 Supported Data Types 表。

### 单速率处理

在单速率处理模式下，输入和输出信号具有相同的端口采样时间。模块通过使输出相对于输入发生大小变化来隐式实现速率变化。在此模式下，模块的输入可以是多个符号。

- 当将 **输入类型** 设置为 `Integer` 时，输入可以是列向量，其长度为输入符号数。
- 当将 **输入类型** 设置为 `Bit` 时，输入宽度必须是 *K*（每符号位数）的整数倍。

输出宽度等于输入符号数与 **Samples per symbol** 参数值的乘积。

### 多速率处理

在多速率处理模式下，输入和输出信号具有不同的端口采样时间。在此模式下，模块的输入必须是一个符号。

- 当将 **输入类型** 设置为 `Integer` 时，输入必须是标量。
- 当将 **输入类型** 设置为 `Bit` 时，输入宽度必须等于每符号位数。

输出采样时间等于符号周期除以 **Samples per symbol** 参数值。
