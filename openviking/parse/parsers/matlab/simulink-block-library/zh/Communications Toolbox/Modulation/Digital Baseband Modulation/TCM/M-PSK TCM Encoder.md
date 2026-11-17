---
type: simulink-block
title: 'M-PSK TCM Encoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / TCM'
documentation_page: 'mpsktcmencoder'
documentation_source_path: 'ref/mpsktcmencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# M-PSK TCM Encoder

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

**Operation mode**
:   在 `Continuous` 模式（默认设置）下，模块在每帧结束时保留编码器状态，以供下一帧使用。

    在 `Truncated (reset every frame)` 模式下，模块独立处理每一帧。即，编码器状态在每帧开始时重置为全零状态。

    在 `Terminate trellis by appending bits` 模式下，模块独立处理每一帧。对于每个输入帧，使用额外的比特在帧结束时将编码器状态设置为全零状态。输出长度由 y=n⋅(x+s)/k 给出，其中 *x* 是输入比特数，s=约束长度−1（或者，在多个约束长度的情况下，*s* =`sum(ConstraintLength(i)-1)`）。该模块支持此模式用于列向量输入信号。

    在 `Reset on nonzero input via port` 模式下，模块有一个额外的输入端口，标记为 `Rst`。当 `Rst` 输入非零时，编码器重置为全零状态。

**M-ary number**
:   信号星座图中的点数。

**输出数据类型**
:   模块的输出类型可以指定为 `single` 或 `double`。默认情况下，模块将其设置为 `double`。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

对二进制数据进行卷积编码并使用 PSK 方法进行调制

M-PSK TCM Encoder 模块通过对二进制输入信号进行卷积编码并将结果映射到 PSK 信号星座图来实现网格编码调制（TCM）。

**M-ary number** 参数是信号星座图中的点数，它也等于卷积编码器可能的输出符号数。（即，对于码率为 k/n 的卷积码，log2(**M-ary number**) 等于 n。）

### 输入信号和输出信号

如果由网格结构描述的卷积编码器表示码率为 *k*/*n* 的码，则模块输入信号必须是长度为 *L*\**k* 的二进制列向量，其中 *L* 为某个正整数。

该模块接受二值输入信号。输出信号是长度为 *L* 的复数列向量。

### 指定编码器

要定义卷积编码器，请使用 **Trellis structure** 参数。该参数是一个 MATLAB® 结构体，其格式在卷积码的网格描述中描述。您可以通过两种方式使用此参数字段：

- 如果您想使用约束长度、生成多项式和可能的反馈连接多项式来指定编码器，请在 **Trellis structure** 字段中使用 `poly2trellis` 命令。例如，要使用约束长度为 7、码生成多项式为 171 和 133（八进制数）、反馈连接为 171（八进制）的编码器，请将 **Trellis structure** 参数设置为

  `poly2trellis(7,[171 133],171)`
- 如果 MATLAB 工作区中有一个包含网格结构的变量，则输入其名称作为 **Trellis structure** 参数。这种方式更快，因为与上一项中的用法相比，它使 Simulink® 软件在每次仿真开始时花费更少的时间更新图。

编码器寄存器从全零状态开始。您可以配置编码器，使其在仿真过程中将寄存器重置为全零状态。为此，请将 `Operation mode` 设置为 **Reset on nonzero input via port**。模块随后打开第二个输入端口，标记为 `Rst`。`Rst` 端口上的信号是标量信号。当其非零时，编码器在处理第一个输入端口的数据之前进行重置。

### 信号星座图

网格编码调制技术将星座图划分为称为陪集的子集，以最大化每个陪集中点对之间的最小距离。该模块根据您为 **M-ary number** 参数选择的值在内部形成有效的划分。

下图显示了当 **M-ary number** 为 8 时模块使用的带标签的集划分信号星座图。对于其他大小的星座图，请参见 [1]。

### 编码增益

在多相网格码存在 AWGN 的情况下，相对于未编码情况，可以实现 3 到 6 分贝的编码增益 [3]。
