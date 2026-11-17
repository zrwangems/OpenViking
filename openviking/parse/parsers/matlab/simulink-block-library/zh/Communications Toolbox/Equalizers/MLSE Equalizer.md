---
type: simulink-block
title: 'MLSE Equalizer'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Equalizers'
documentation_page: 'mlseequalizer'
documentation_source_path: 'ref/mlseequalizer.html'
language: zh-CN
chinese_source: worker-translation
---

# MLSE Equalizer

## 端口

R2025b 中未记录。

## 参数

**Specify channel via**
:   指定信道估计的方法。如果选择 `Input port`，模块会显示第二个输入端口，用于接收信道估计。如果选择 `Dialog`，可以在 **Channel coefficients** 字段中将信道估计指定为 FIR 滤波器的系数向量。

**Channel coefficients**
:   包含模块用于信道估计的 FIR 滤波器系数的向量。仅当将 **Specify channel via** 设置为 `Dialog` 时，此字段才可见。

**Signal constellation**
:   指定调制星座图的复数向量。

**Traceback depth**
:   模块在 Viterbi 算法中用于构造每条回溯路径的网格分支数（等价地，符号数）。

**Operation mode**
:   Viterbi 解码器的工作模式。可选值为 `Continuous with reset option` 和 `Reset every frame`。

**Input contains preamble**
:   选中后，可以在 **Expected preamble** 字段中设置前导码。仅当将 **Operation mode** 设置为 `Reset every frame` 时，此选项才会出现。

**Expected preamble**
:   表示前导码的、介于 0 和 M-1 之间的整数向量，其中 M 是星座图的大小。仅当将 **Operation mode** 设置为 `Reset every frame` 并随后选择 **Input contains preamble** 时，此字段才可见且可用。

**Input contains postamble**
:   选中后，可以在 **Expected postamble** 字段中设置后导码。仅当将 **Operation mode** 设置为 `Reset every frame` 时，此选项才会出现。

**Expected postamble**
:   表示后导码的、介于 0 和 M-1 之间的整数向量，其中 M 是星座图的大小。仅当将 **Operation mode** 设置为 `Reset every frame` 并随后选择 **Input contains postamble** 时，此字段才可见且可用。

**Samples per input symbol**
:   每个星座点对应的输入样本数。

**启用复位输入端口**
:   选中此框后，模块会有一个标记为 `Rst` 的第二个输入端口。向此端口提供非零输入值会使模块在处理输入数据之前将其内部存储器设置为初始状态。仅当将 **Operation mode** 设置为 `Continuous with reset option` 时，此选项才会出现。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

使用 Viterbi 算法进行均衡

MLSE Equalizer 模块使用 Viterbi 算法对通过色散信道传输的线性调制信号进行均衡。该模块处理输入帧，并使用建模为有限输入响应（FIR）滤波器的信道估计，输出信号的最大似然序列估计（MLSE）。

此模块支持 `single` 和 `double` 数据类型。

### 信道估计

信道估计采用列向量的形式，其中包含按幂次降序排列的 FIR 滤波器系数。此向量的长度就是信道记忆长度，它必须是模块 **Samples per input symbol** 参数的倍数。

要指定信道估计向量，请使用以下方法之一：

- 将 **Specify channel via** 设置为 `Dialog`，并在 **Channel coefficients** 字段中输入该向量。
- 将 **Specify channel via** 设置为 `Input port`，模块会显示一个额外的输入端口，标记为 `Ch`，用于接受列向量输入信号。

### 信号星座图

**Signal constellation** 参数指定调制信号的星座图，由模型中的调制器决定。**Signal constellation** 是一个复数向量，其中第 k 个复数是对应于调制器将整数 k-1 映射到的星座点。

**注意**

星座点序列在模型中的调制器与此模块中的 **Signal constellation** 参数之间必须保持一致。

例如，要指定由以下映射给出的星座图

0→+1+i1→−1+i2→−1−i3→+1−i

请将 **Constellation points** 设置为 `[1+i, -1+i, -1-i, 1-i]`。请注意，向量中数字的顺序表示调制器如何将整数映射到星座点集合。带标签的星座图如下所示。

### 前导码和后导码

如果数据带有前导码（前缀）或后导码（后缀），请相应地配置模块：

- 如果选择 **Input contains preamble**，则 **Expected preamble** 参数指定你期望在输入信号中数据之前出现的前导码。
- 如果选中 **Input contains postamble**，则 **Expected postamble** 参数指定你期望在输入信号中数据之后出现的后导码。

**Expected preamble** 或 **Expected postamble** 参数必须是介于 0 和 M-1 之间的整数向量，其中 M 是星座点的数量。向量中整数值 k-1 对应于 **Constellation points** 向量中的第 k 个条目，因此也对应于调制器输入 k-1。

前导码或后导码必须已经分别包含在此模块输入信号的开头或末尾。如有必要，可以在 Simulink® 软件中使用 Matrix Concatenation 模块连接向量。

要了解模块如何使用前导码和后导码，请参见下面的“Reset Every Frame”工作模式。

### “Reset Every Frame”工作模式

Viterbi 算法在连续帧之间进行转换的一种方式称为 `Reset every frame` 模式。可以使用 **Operation mode** 参数选择此模式。

在 `Reset every frame` 模式下，模块独立解码每一帧数据，并在每帧结束时重置状态度量。回溯解码始终从具有最小状态度量的状态开始。

状态度量的初始化取决于是否指定前导码和/或后导码：

- 如果未指定前导码，解码器会在每帧数据开始时将所有状态的度量初始化为 0。
- 如果指定了前导码，模块会使用它在每帧数据开始时初始化状态度量。更具体地说，模块解码前导码，并为解码后的状态分配度量 0。如果前导码不能解码为唯一状态——也就是说，如果前导码的长度小于信道记忆长度——解码器会为前导码可表示的所有状态分配度量 0。只要指定了前导码，回溯路径就会终止于前导码所表示的状态之一。
- 如果未指定后导码，回溯路径从具有最小度量的状态开始。
- 如果指定了后导码，回溯路径从后导码所表示的状态开始。如果后导码不能解码为唯一状态，解码器会识别后导码所表示的所有可能解码状态中最小的那个，并从该状态开始回溯解码。

  **注意**

  在 `Reset every frame` 模式下，MLSE Equalizer 模块的输入必须至少包含 T 个符号，不包括可选的前导码，其中 T 是 **Traceback depth** 参数。

### 连续工作模式

Viterbi 算法在连续帧之间进行转换的另一种方式称为 `Continuous with reset option` 模式。可以使用 **Operation mode** 参数选择此模式。

在 `Continuous with reset option` 模式下，模块会在仿真开始时将所有状态的度量初始化为 0。在每帧结束时，模块会保存内部状态度量，以便在下一帧中计算回溯路径时使用。

如果选择 **启用复位输入端口**，模块会显示另一个输入端口，标记为 `Rst`。在这种情况下，只要 `Rst` 端口处的标量值非零，模块就会重置状态度量。

### 解码延迟

MLSE Equalizer 模块在 `Continuous with reset option` 模式下会引入等于 **Traceback depth** 的输出延迟，而在 `Reset every frame` 模式下没有延迟。
