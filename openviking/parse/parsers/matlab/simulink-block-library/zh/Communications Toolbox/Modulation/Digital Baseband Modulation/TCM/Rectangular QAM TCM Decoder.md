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

R2025b 中未记录。

## 参数

**Trellis structure**
:   包含卷积编码器网格描述的 MATLAB® 结构体。

**M-ary number**
:   信号星座图中的点数。

**Traceback depth**
:   该模块在 Viterbi 算法中用于构造每条回溯路径的网格分支数（等价地，符号数）。

**Operation mode**
:   Viterbi 解码器的工作模式。可选值为
    `Continuous`、
    `Truncated` 和
    `Terminated`。

**启用复位输入端口**
:   选中此复选框时，该模块具有第二个输入端口，标记为
    `Rst`。向此端口提供非零输入值会使该模块在处理输入数据之前将其内部存储器设置为初始状态。此选项仅在将
    **Operation mode** 设置为
    `Continuous` 时出现。

**输出数据类型**
:   将模块输出信号的数据类型选择为
    `boolean` 或 `single`。
    默认情况下，该模块将其设置为 `double`。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

解码使用 QAM 方法调制的网格编码调制数据

Rectangular QAM TCM Decoder 模块使用 Viterbi 算法解码先前使用 QAM 信号星座图调制的网格编码调制（TCM）信号。

**M-ary number** 参数表示信号星座图中的点数，它也等于卷积编码器可能的输出符号数。（也就是说，
log2(**M-ary number**) 是卷积编码器的输出比特流数量。）

此模块中的 **Trellis structure** 和 **M-ary number**
参数应与 Rectangular QAM TCM Encoder 模块中的相应参数匹配，以确保正确解码。

### 输入和输出信号

此模块接受包含复数的列向量输入信号。有关每个模块端口支持的数据类型的信息，请参阅 Supported Data Types。

如果由网格结构描述的卷积编码器表示码率为
*k*/*n* 的码，则 Rectangular QAM TCM
Decoder 模块的输出是长度为
*k* 乘以输入信号向量长度的二进制列向量。

### 工作模式

该模块有三种在连续帧之间转换的可能方法。
**Operation mode** 参数控制该模块使用哪种方法。此参数还会影响
**Traceback depth** 参数 D 的可能取值范围。

- 在 `Continuous` 模式下，该模块在仿真开始时将所有状态度量初始化为零，等待直到累积 D 个符号，然后使用 D 个符号的序列来计算每条回溯路径。D 可以是任何正整数。在每帧结束时，该模块保存其内部状态度量以供下一帧使用。

  如果选中 **Enable the reset input**，该模块会显示另一个输入端口，标记为 `Rst`。此端口接收整数标量信号。只要
  `Rst` 端口处的值非零，该模块就会将所有状态度量重置为零，并将回溯存储器设置为零。
- 在 `Truncated` 模式下，该模块独立处理每一帧。回溯路径从具有最低度量的状态开始。D 必须小于或等于输入的向量长度。
- 在 `Terminated` 模式下，该模块独立处理每一帧。回溯路径始终从全零状态开始。D
  必须小于或等于输入的向量长度。如果您知道每帧数据通常在全零状态结束，那么此模式是合适的选择。

### 解码延迟

如果将 **Operation mode** 设置为
`Continuous`，则对于码率为 k/n 的卷积码，此模块会引入等于 **Traceback depth**\*k 比特的解码延迟。解码延迟是输出中第一个解码比特之前的零的数量。

对于 **Operation
mode** 的其他值，该模块不产生延迟。
