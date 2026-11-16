---
type: simulink-block
title: 'Rectangular QAM TCM Decoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / TCM'
documentation_page: 'rectangularqamtcmdecoder'
documentation_source_path: 'ref/rectangularqamtcmdecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Rectangular QAM TCM Decoder

## 端口

R2025b 中未提供文档说明。

## 参数

**网格结构**
:   包含卷积编码器网格描述的 MATLAB® 结构体。

**M 元数**
:   信号星座图中的点数。

**回溯深度**
:   模块在 Viterbi 算法中用于构建每条回溯路径的网格分支数（等价于符号数）。

**操作模式**
:   Viterbi 解码器的操作模式。可选值为 `Continuous`、`Truncated` 和 `Terminated`。

**启用复位输入端口**
:   选中此复选框后，模块将具有第二个标记为 `Rst` 的输入端口。向此端口提供非零输入值会使模块在处理输入数据之前将其内部存储器设置为初始状态。仅当将**操作模式**设置为 `Continuous` 时，才会显示此选项。

**输出数据类型**
:   将模块输出信号的数据类型选择为 `boolean` 或 `single`。默认情况下，模块将其设置为 `double`。

## 所属库

R2025b 中未提供文档说明。

## 模块特性

R2025b 中未提供文档说明。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

对采用 QAM 方法调制的网格编码调制数据进行解码

Rectangular QAM TCM Decoder 模块使用 Viterbi 算法对网格编码调制 (TCM) 信号进行解码，该信号先前已使用 QAM 信号星座图进行调制。

**M 元数**参数表示信号星座图中的点数，它也等于卷积编码器可能输出的符号数。（即 log2(**M 元数**) 是卷积编码器的输出比特流数量。）

此模块中的**网格结构**和 **M 元数**参数应与 Rectangular QAM TCM Encoder 模块中的相应参数匹配，以确保正确解码。

### 输入和输出信号

此模块接受包含复数的列向量输入信号。有关每个模块端口支持的数据类型的信息，请参阅“支持的数据类型”。

如果网格结构所描述的卷积编码器表示码率为 *k*/*n* 的编码，则 Rectangular QAM TCM Decoder 模块的输出为二进制列向量，其长度为输入信号向量长度的 *k* 倍。

### 操作模式

模块在连续帧之间有三种可能的过渡方式。**操作模式**参数控制模块使用哪种方式。此参数还影响**回溯深度**参数 D 的可能取值范围。

- 在 `Continuous` 模式下，模块在仿真开始时将所有状态度量初始化为零，等到累积 D 个符号后，再使用 D 个符号的序列计算每条回溯路径。D 可以是任意正整数。在每帧结束时，模块会保存其内部状态度量，以供下一帧使用。

  如果选择**启用复位输入**，模块会显示另一个标记为 `Rst` 的输入端口。此端口接收整数标量信号。每当 `Rst` 端口的值非零时，模块就会将所有状态度量重置为零，并将回溯存储器设置为零。
- 在 `Truncated` 模式下，模块独立处理每一帧。回溯路径从度量值最低的状态开始。D 必须小于或等于输入向量的长度。
- 在 `Terminated` 模式下，模块独立处理每一帧。回溯路径始终从全零状态开始。D 必须小于或等于输入向量的长度。如果您知道每帧数据通常在全零状态结束，则此模式是合适的选择。

### 解码延迟

如果将**操作模式**设置为 `Continuous`，则对于码率为 k/n 的卷积码，此模块引入的解码延迟等于**回溯深度**\*k bits。解码延迟是输出中第一个解码位之前的零的数量。

对于**操作模式**的其他取值，模块不会产生延迟。
