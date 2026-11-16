---
type: simulink-block
title: 'General TCM Decoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / TCM'
documentation_page: 'generaltcmdecoder'
documentation_source_path: 'ref/generaltcmdecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# General TCM Decoder

## 端口

R2025b 中未提供相关文档。

## 参数

**网格结构**
:   包含卷积编码器网格描述的 MATLAB 结构体。

**信号星座**
:   一个复数向量，按集合划分顺序列出信号星座中的点。

**回溯深度**
:   模块在 Viterbi 算法中用于构建每条回溯路径的网格分支数（即符号数）。

**操作模式**
:   Viterbi 解码器的操作模式。可选值为 `Continuous`、`Truncated` 和 `Terminated`。

**启用重置输入端口**
:   选中此复选框后，模块将具有第二个输入端口，标签为 `Rst`。向此端口提供非零值会使模块在处理输入数据之前将其内部存储器设置为初始状态。仅当您将 **操作模式** 设置为 `Continuous` 时，才会显示此字段。

**输出数据类型**
:   将模块输出信号的数据类型选择为 `boolean` 或 `single`。默认情况下，模块将其设置为 `double`。

## 所属库

R2025b 中未提供相关文档。

## 模块特性

R2025b 中未提供相关文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

对使用任意星座映射的网格编码调制数据进行解码

General TCM Decoder 模块使用 Viterbi 算法，对先前使用任意信号星座进行调制的网格编码调制 (TCM) 信号进行解码。

此模块中的 **网格结构** 和 **信号星座** 参数应与 General TCM Encoder 模块中的对应参数相匹配，以确保正确解码。特别是，**信号星座** 参数必须按集合划分顺序排列。

### 输入和输出信号

此模块接受包含复数的列向量输入信号。输入信号必须为 `double` 或 `single`。重置端口信号必须为 `double` 或 `Boolean`。有关每个模块端口支持的数据类型的信息，请参阅支持的数据类型。

如果网格结构所描述的卷积编码器表示码率为 *k*/*n* 的编码，则 General TCM Decoder 模块的输出为二进制列向量，其长度为输入信号向量长度的 *k* 倍。

### 操作模式

此模块在相继帧之间过渡时有三种可能的方法。**操作模式** 参数控制模块使用哪种方法。此参数还会影响 **回溯深度** 参数 D 的可能取值范围。

- 在 `Continuous` 模式下，模块在仿真开始时将所有状态度量初始化为零，等待累积 D 个符号，然后使用由 D 个符号组成的序列计算各条回溯路径。D 可以是任意正整数。在每帧结束时，模块保存其内部状态度量，以供下一帧使用。

  如果选择 **启用重置输入端口**，模块将显示另一个输入端口，标签为 `Rst`。此端口接收整数标量信号。每当 `Rst` 端口的值为非零时，模块就会将所有状态度量重置为零，并将回溯存储器设置为零。
- 在 `Truncated` 模式下，模块独立处理每一帧。回溯路径从度量值最低的状态开始。D 必须小于或等于输入信号的向量长度。
- 在 `Terminated` 模式下，模块独立处理每一帧。回溯路径始终从全零状态开始。D 必须小于或等于输入信号的向量长度。如果您知道每帧数据通常结束于全零状态，则此模式是合适的选择。

### 解码延迟

如果将 **操作模式** 设置为 `Continuous`，则对于码率为 k/n 的卷积码，此模块引入的解码延迟等于 **回溯深度**\*k bits。解码延迟是输出中第一个解码比特之前出现的零的个数。

对于 **操作模式** 的其他值，模块不会产生延迟。
