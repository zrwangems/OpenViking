---
type: simulink-block
title: 'G711 Codec'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Quantizers'
documentation_page: 'g711codec'
documentation_source_path: 'ref/g711codec.html'
language: zh-CN
chinese_source: worker-translation
---

# G711 Codec

## 端口

R2025b 中未提供文档。

## 参数

**Mode**
:   - 当选择 `Encode PCM to A-law` 时，
      模块实现 A 律编码器。
    - 当选择 `Encode PCM to mu-law` 时，
      模块实现 μ 律编码器。
    - 当选择 `Decode A-law to PCM` 时，
      模块使用 A 律查找表将输入索引值解码为量化输出值。
    - 当选择 `Decode mu-law to PCM` 时，
      模块使用 μ 律查找表将输入索引值解码为量化输出值。
    - 当选择 `Convert A-law to mu-law` 时，
      模块将输入 A 律索引值转换为 μ 律索引值。
    - 当选择 `Convert mu-law to A-law` 时，
      模块将输入 μ 律索引值转换为 A 律索引值。

**Overflow diagnostic**
:   使用此参数确定发生溢出时模块的行为。

    - 选择 `Ignore` 可在不显示警告消息的情况下继续计算。
    - 选择 `Warning` 可在 MATLAB 命令行窗口中显示警告消息，并继续仿真。
    - 选择 `Error` 可显示错误对话框并终止仿真。

    仅当 **Mode** 参数选择 `Encode PCM to A-law` 或
    `Encode PCM to mu-law` 时，此参数才可见。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

对窄带语音输入信号进行量化

G711 Codec 模块是专为窄带语音设计的对数标量量化器。窄带语音定义为模拟带宽为 4 kHz、奈奎斯特采样频率为 8 kHz 的语音信号。该模块对窄带语音输入信号进行量化，使其仅需 8 位即可传输。G711 Codec 模块具有三种工作模式：编码、解码和转换。可以通过设置 **Mode** 参数来选择模块的工作模式。

如果为 **Mode** 参数选择 `Encode PCM to A-law`，模块将假定线性 PCM 输入信号的动态范围为 13 位。由于模块始终工作在饱和模式下，它会将任何高于 2¹²−1 的输入值赋值为 2¹²−1，并将任何低于 −2¹² 的输入值赋值为 −2¹²。模块对输入信号实现 A 律量化，并输出 A 律索引值。当选择 `Encode PCM to mu-law` 时，模块将假定线性 PCM 输入信号的动态范围为 14 位。由于模块始终工作在饱和模式下，它会将任何高于 2¹³−1 的输入值赋值为 2¹³−1，并将任何低于 −2¹³ 的输入值赋值为 −2¹³。模块对输入信号实现 μ 律量化，并输出 μ 律索引值。

如果为 **Mode** 参数选择 `Decode A-law to PCM`，模块将使用 A 律查找表把输入 A 律索引值解码为量化输出值。当选择 `Decode mu-law to PCM` 时，模块将使用 μ 律查找表把输入 μ 律索引值解码为量化输出值。

如果为 **Mode** 参数选择 `Convert A-law to mu-law`，模块会将输入 A 律索引值转换为 μ 律索引值。当选择 `Convert mu-law to A-law` 时，模块会将输入 μ 律索引值转换为 A 律索引值。

**注意**

仅当模块的输入为 A 律或 μ 律索引值时，才将 **Mode** 参数设置为 `Convert A-law to mu-law` 或 `Convert mu-law to A-law`。

如果为 **Mode** 参数选择 `Encode PCM to A-law` 或 `Encode PCM to mu-law`，模块参数对话框中将显示 **Overflow diagnostic** 参数。使用此参数确定发生溢出时模块的行为。可用选项如下：

- `Ignore` — 继续计算，不发出警告消息。
- `Warning` — 在 MATLAB® 命令行窗口中显示警告消息，并继续仿真。
- `Error` — 显示错误对话框并终止仿真。

**注意**

与 Configuration Parameters 对话框上的所有诊断参数一样，在 Simulink® Coder™ 代码生成软件为此模块生成的代码中，**Overflow diagnostic** 参数设置为 `Ignore`。
