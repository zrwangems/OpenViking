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
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters: []
```

**Trellis structure**
:   包含卷积编码器网格描述的 MATLAB 结构体。

**Signal constellation**
:   一个复向量，按集合划分顺序列出信号星座中的点。

**Traceback depth**
:   该模块在 Viterbi 算法中用于构造每条回溯路径的网格分支数（等价地，符号数）。

**Operation mode**
:   Viterbi 解码器的工作模式。可选值为
    `Continuous`、
    `Truncated` 和
    `Terminated`。

**启用复位输入端口**
:   选中此复选框时，该模块具有第二个输入端口，标记为
    `Rst`。向此端口提供非零值会使该模块在处理
    输入数据之前将其内部存储器设置为初始状态。仅当您将 **Operation
    mode** 设置为 `Continuous` 时，此字段才会出现。

**输出数据类型**
:   选择模块输出信号的数据类型，可选值为
    `boolean` 或 `single`。
    默认情况下，该模块将其设置为 `double`。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

解码网格编码调制数据，使用任意星座映射

General TCM Decoder 模块使用 Viterbi 算法解码先前使用任意信号
星座调制的网格编码调制（TCM）信号。

此模块中的 **Trellis structure** 和 **Signal
constellation** 参数应与 General TCM Encoder 模块中的参数匹配，以确保正确解码。特别是，
**Signal constellation** 参数必须按集合划分
顺序排列。

### 输入和输出信号

此模块接受包含复数的列向量输入信号。输入
信号必须为 `double` 或 `single`。复位端口信号必须为 `double` 或 `Boolean`。
有关每个模块端口支持的数据类型的信息，请参阅支持的数据类型。

如果网格结构所描述的卷积编码器表示码率为
*k*/*n* 的码，则 General TCM Decoder
模块的输出是一个二进制列向量，其长度为 *k* 乘以
输入信号的向量长度。

### 工作模式

该模块有三种在连续帧之间转换的可能方法。
**Operation mode** 参数控制该模块使用哪种方法。此参数还
影响 **Traceback depth** 参数 D 的可能取值范围。

- 在 `Continuous` 模式下，该模块在仿真开始时将所有
  状态度量初始化为零，等待直到累积 D 个符号，然后使用 D 个符号的序列来计算每条
  回溯路径。D 可以是任何正整数。在每帧结束时，该模块保存其内部状态度量以供下一
  帧使用。

  如果您选中 **启用复位输入端口**，该模块
  会显示另一个输入端口，标记为 `Rst`。此端口
  接收整数标量信号。每当 `Rst`
  端口的值非零时，该模块将所有状态
  度量重置为零，并将回溯存储器设置为零。
- 在 `Truncated` 模式下，该模块独立处理每一帧。
  回溯路径从具有最低度量的状态开始。D 必须小于或等于
  输入的向量长度。
- 在 `Terminated` 模式下，该模块独立处理每一帧。回溯路径
  始终从全零状态开始。D
  必须小于或等于输入的向量长度。如果您知道
  每帧数据通常在全零状态结束，那么此
  模式是合适的选择。

### 解码延迟

如果您将 **Operation mode** 设置为
`Continuous`，则对于码率为 k/n 的
卷积码，此模块引入等于 **Traceback depth**\*k 位的解码
延迟。解码延迟是输出中第一个
解码位之前的零的个数。

对于其他 **Operation
mode** 值，该模块不产生延迟。
