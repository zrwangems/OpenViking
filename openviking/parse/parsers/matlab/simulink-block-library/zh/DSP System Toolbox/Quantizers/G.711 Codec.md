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

R2025b 中未记录。

## 参数

**Mode**
:   - 当您选择 `Encode PCM to A-law` 时，该模块实现 A-law 编码器。
    - 当您选择 `Encode PCM to mu-law` 时，该模块实现 mu-law 编码器。
    - 当您选择 `Decode A-law to PCM` 时，该模块使用 A-law 查找表将输入索引值解码为量化输出值。
    - 当您选择 `Decode mu-law to PCM` 时，该模块使用 mu-law 查找表将输入索引值解码为量化输出值。
    - 当您选择 `Convert A-law to mu-law` 时，该模块将输入的 A-law 索引值转换为 mu-law 索引值。
    - 当您选择 `Convert mu-law to A-law` 时，该模块将输入的 mu-law 索引值转换为 A-law 索引值。

**Overflow diagnostic**
:   使用此参数确定模块在发生溢出时的行为。

    - 选择 `Ignore` 以继续计算而不发出警告消息。
    - 选择 `Warning` 以在 MATLAB 命令窗口中显示警告消息并继续仿真。
    - 选择 `Error` 以显示错误对话框并终止仿真。

    仅当 **Mode** 参数选择 `Encode PCM to A-law` 或 `Encode PCM to mu-law` 时，此参数才可见。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

量化窄带语音输入信号

G711 Codec 模块是专为窄带语音设计的对数标量量化器。窄带语音定义为模拟带宽为 4 kHz、奈奎斯特采样频率为 8 kHz 的语音信号。该模块对窄带语音输入信号进行量化，使其仅使用 8 位即可传输。G711 Codec 模块具有三种操作模式：编码、解码和转换。您可以通过设置 **Mode** 参数来选择模块的操作模式。

如果 **Mode** 参数选择 `Encode PCM to A-law`，该模块假定线性 PCM 输入信号的动态范围为 13 位。由于该模块始终在饱和模式下运行，它将任何高于 212−1 的输入值赋值为 212−1，将任何低于 −212 的输入值赋值为 −212。该模块对输入信号实现 A-law 量化器并输出 A-law 索引值。当您选择 `Encode PCM to mu-law` 时，该模块假定线性 PCM 输入信号的动态范围为 14 位。由于该模块始终在饱和模式下运行，它将任何高于 213−1 的输入值赋值为 213−1，将任何低于 −213 的输入值赋值为 −213。该模块对输入信号实现 mu-law 量化器并输出 mu-law 索引值。

如果 **Mode** 参数选择 `Decode A-law to PCM`，该模块使用 A-law 查找表将输入 A-law 索引值解码为量化输出值。当您选择 `Decode mu-law to PCM` 时，该模块使用 mu-law 查找表将输入 mu-law 索引值解码为量化输出值。

如果 **Mode** 参数选择 `Convert A-law to mu-law`，该模块将输入 A-law 索引值转换为 mu-law 索引值。当您选择 `Convert mu-law to A-law` 时，该模块将输入 mu-law 索引值转换为 A-law 索引值。

**注意**

仅当模块的输入为 A-law 或 mu-law 索引值时，才将 **Mode** 参数设置为 `Convert A-law to mu-law` 或 `Convert mu-law to A-law`。

如果 **Mode** 参数选择 `Encode PCM to A-law` 或 `Encode PCM to mu-law`，则 **Overflow diagnostic** 参数会出现在模块参数对话框中。使用此参数确定模块在发生溢出时的行为。以下选项可用：

- `Ignore` — 继续计算且不发出警告消息。
- `Warning` — 在 MATLAB® 命令窗口中显示警告消息，并继续仿真。
- `Error` — 显示错误对话框并终止仿真。

**注意**

与配置参数对话框上的所有诊断参数一样，Simulink® Coder™ 代码生成软件为此模块生成的代码中，**Overflow diagnostic** 参数设置为 `Ignore`。
